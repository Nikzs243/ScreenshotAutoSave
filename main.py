import pyautogui as pag, os, configparser, logging, re, sys, shutil, platform, pymsgbox
from pynput import keyboard


if getattr(sys, 'frozen', False):
    program_path = os.path.dirname(sys.executable)
else:
    program_path = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(program_path, "config.ini")
log_path = os.path.join(program_path, "log.txt")
config = configparser.ConfigParser()

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"

)

def verificar_plataforma():
    plataforma = platform.system()

    if plataforma == "Linux":
        if shutil.which("scrot") is None:
            logging.error("O utilitário 'scrot' não está instalado. Instale com: sudo apt install scrot")
            sys.exit("Encerrando: 'scrot' é necessário para capturar screenshots no Linux.")
    if plataforma == "Darwin":
        logging.info("macOS detectado. Certifique-se de que o programa tem permissão de Acessibilidade nas Configurações.")
    if plataforma == "Windows":
        logging.info("Windows detectado. Nenhuma dependência extra necessária.")
    logging.info("Ambiente verificado...")

def config_padrao():
    logging.info("Criando arquivo config.ini com valores padrão.")
    with open(config_path, "w", encoding="utf-8") as f:
        f.write("[config]\n")
        f.write("# Caminho onde as screenshots serão salvas\n")        
        f.write(f"pasta = {os.path.join(program_path, 'screenshots')}\n")
        f.write("\n# Tecla para encerrar o programa (ex: ctrl_l, esc, q)\n")
        f.write("tecla_sair = ctrl_l\n")
        f.write("\n# Tecla para tirar o screenshot (ex: print_screen, s)\n")
        f.write("tecla_screenshot = print_screen\n")
        f.write("\n# define com True ou False se deve mostrar avisos na tela\n")
        f.write("avisos = True\n")
def verificar_config():
    logging.info("Iniciando verificação de integridade do arquivo config.ini...")
    valores_padrao = {
        "pasta": os.path.join(program_path, "screenshots"), 
        "tecla_sair": "ctrl_l", 
        "tecla_screenshot": "print_screen",
        "avisos": "True" 
    }
    try:
        with open(config_path, encoding="utf-8") as f:
            config.read_file(f)
    except configparser.MissingSectionHeaderError:
        logging.warning("seção [config] não encontrada, restaurando config.ini padrão...")
        config_padrao()
        return
    if "config" not in config:
        logging.warning("seção [config] não encontrada, restaurando config.ini padrão...")
        config_padrao()
        return
    alterado = False
    for chave, valor in valores_padrao.items():
        if not chave in config["config"]:
            logging.warning(f"chave '{chave}' não encontrada, restaurando e definindo valor padrão...")
            config["config"][chave] = valor
            alterado = True
    if alterado:
        with open(config_path, "w", encoding="utf-8") as f:
            config.write(f) 
        logging.info("arquivo config.ini corrigido e salvo!")
    else:
        logging.info("verificação concluida com sucesso: tudo ok!")


def get_tecla(teclastr, padrao, key):
    try:
        tecla = getattr(keyboard.Key, teclastr)
    except AttributeError:
        if len(teclastr) == 1:
            tecla = keyboard.KeyCode.from_char(teclastr)
        else:
            logging.warning(f"Key: {key}, com definição incorreta: '{teclastr}', valor padrao definido")
            tecla = getattr(keyboard.Key, padrao)
            config["config"][key] = padrao
            with open(config_path, "w") as f:
                config.write(f)
    return tecla

def get_next_index(pasta):
    arquivos = os.listdir(pasta)
    indices = [
        int(re.search(r"screenshot_(\d+)\.png", a).group(1))
        for a in arquivos if re.match(r"screenshot_\d+\.png", a)
    ]
    return max(indices) + 1 if indices else 0

def on_press(key):
    if key == tecla_sair:
        print("saindo...")
        logging.info("Fechando programa...")
        if avisos:
            pymsgbox.alert("Progama fechado!", "Alerta")
        listener.stop()
    if key == tecla_screenshot:
        if not os.path.exists(screenshots_folder):
            os.makedirs(screenshots_folder)
            logging.info(f"pasta: {screenshots_folder} criada com sucesso!")
        indice = get_next_index(screenshots_folder)
        screenshot = pag.screenshot()
        screenshot.save(os.path.join(screenshots_folder, f"screenshot_{indice}.png"))
        logging.info(f"screenshot_{indice}.png salva em: {screenshots_folder}")

if not os.path.exists(config_path):
    config_padrao()
    config.read(config_path)
else:
    verificar_config()
verificar_plataforma()

try:
    avisos = config.getboolean("config", "avisos")
except ValueError:
    config["config"]["avisos"] = "true"
    avisos = config.getboolean("config", "avisos")
    logging.warning("chave 'avisos' com valor inválido definido, retornando aos valores padrão...")
    with open(config_path, "w") as f:
        config.write(f)

screenshots_folder = config["config"].get("pasta")
if not os.path.exists(screenshots_folder):
    os.makedirs(screenshots_folder)
    logging.info(f"Pasta de screenshots criada: {screenshots_folder}")


tecla_sair = get_tecla(config["config"].get("tecla_sair"), "ctrl_l", "tecla_sair")
tecla_screenshot = get_tecla(config["config"].get("tecla_screenshot"), "print_screen", "tecla_screenshot")

logging.info("Programa inicializado com sucesso!")
if avisos:
    pymsgbox.alert("progama iniciado! ", "Aviso")
listener = keyboard.Listener(
    on_press=on_press
)
listener.start()
listener.join()

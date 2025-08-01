📸 ScreenshotAutoSave

🌍 Este projeto também está disponível em [Inglês](README.md)

Um script simples e rápido em Python que tira print da tela e salva automaticamente com um nome único. Sem precisar abrir o Snipping Tool, nem clicar em “Salvar como” ou digitar nomes de arquivos — só executar e pronto.

⚙️ Funcionalidades

- 📷 Captura a tela inteira
- 💾 Salva a imagem com nome sequencial
- 📁 As imagens vão direto pra pasta do script (ou outra, se quiser)
- ⚡ Rápido, leve e fácil de rodar


🧠 Por que usar?

As ferramentas nativas do Windows geralmente pedem:
- Abrir a ferramenta de captura
- Selecionar a área
- Salvar manualmente
- Digitar um nome

Esse script **automatiza tudo isso de uma vez só**.


🚀 Como usar

1. Clone o repositório:

git clone [https://github.com/Nikzs243/ScreenshotAutoSave]
cd ScreenshotAutoSave


2. Instale as dependências:

pip install -r requirements.txt


3. Rode o script:

python main.py


Ele vai tirar um print e salvar na pasta atual com um nome sequencial ex:"screenshot_1.png".

📦 Dependências

- `pyautogui`
- `Pillow`

Já incluídas no `requirements.txt`.

⭐ Apoie

Se curtir o projeto, deixa uma ⭐ no repositório — ajuda muito!

Funcionamento:

Ao iniciar, o programa verifica se o arquivo "config.ini" existe e está correto. Se não estiver, ele cria um novo com valores padrão.

O programa então começa a escutar o teclado em segundo plano, aguardando os atalhos definidos.

Quando a tecla de captura (por padrão: print_screen) é pressionada, ele tira um screenshot e salva na pasta definida.

Quando a tecla de saída (por padrão: ctrl_l) é pressionada, o programa é encerrado imediatamente.

Todas as ações feitas são registradas no arquivo "log.txt".

Personalização:
Você pode alterar algumas configurações no arquivo "config.ini" para adaptar o comportamento do programa às suas preferências. As opções disponíveis são:

[config]

pasta = caminho onde os screenshots serão salvos

tecla_sair = tecla que encerra o programa (ex: ctrl_l, esc, q)

tecla_screenshot = tecla para tirar screenshot (ex: print_screen, s)

avisos = valor booleano que define se o usuário quer que apareça caixas de aviso ou não

*adicionado key_name_helper.py para te ajudar a descobrir o nome certo da tecla

Observação:
O arquivo .zip contém todos progamas necessários ja compilados em .exe

Se algum valor estiver incorreto no "config.ini", o programa substitui automaticamente pelo valor padrão e registra a mudança no log.

Autor: Nikzs243


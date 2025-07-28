Este é um programa em Python que permite tirar screenshots de forma automática usando atalhos de teclado. 
Ele funciona em segundo plano e salva as imagens em uma pasta específica, com nomes organizados de forma sequencial (screenshot_0.png, screenshot_1.png, etc).

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

Observação:
Se algum valor estiver incorreto no "config.ini", o programa substitui automaticamente pelo valor padrão e registra a mudança no log.

Autor: Nikzs


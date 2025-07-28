from pynput import keyboard

def on_press(key):
    key = str(key)
    if key.startswith("Key"):
        key = key.split(".")
        key = key[1]
    elif key.startswith("'"):
        key = key.split("'")
        key = key[1]
    print(f"pressionou: {key}                    ", end="\r")
listener = keyboard.Listener(
    on_press=on_press
)
print("esse progama tem como função mostrar o nome de cada tecla pressionada,\na fim de ser adicionado no config.ini")
print("pressione uma tecla...")
listener.start()
listener.join() 


📸 ScreenshotAutoSave

🇧🇷 This project is also available in [Portuguese](README.pt.md)

A simple and fast Python script that takes a screenshot and saves it automatically with a unique name. No Snipping Tool, no Save As, no typing filenames — just press a key and done.

⚙️ Features

- 📷 Captures the full screen
- 💾 Saves the image with a unique timestamp-based filename
- 📁 All images go to the script’s directory (or your custom path)
- ⚡ Instant, lightweight and easy to run


🧠 Why use it?

The default screenshot tools on Windows often require:
- Opening a snipping tool
- Selecting the region
- Saving manually
- Naming the file

This script automates all of that in one shot.


🚀 How to Use

1. Clone the repository:

git clone [https://github.com/Nikzs243/ScreenshotAutoSave]
cd ScreenshotAutoSave


2. Install dependencies:

pip install -r requirements.txt


3. Run the script:

python main.py


The script will take a screenshot and save it in the current directory with a sequencial name e.g: "screenshot_1.png".


📦 Dependencies

- `pyautogui`
- `Pillow`

Already included in `requirements.txt`.


⭐ Support

If you like this project, consider giving it a ⭐ — it helps a lot!

Functionality:

When started, the program checks if the file "config.ini" exists and is correct. If not, it creates a new one with default values.

The program then begins listening to the keyboard in the background, waiting for the defined shortcuts.

When the capture key (default: print_screen) is pressed, it takes a screenshot and saves it in the defined folder.

When the exit key (default: ctrl_l) is pressed, the program terminates immediately.

All actions performed are logged in the file "log.txt".

Customization:

You can change some settings in the "config.ini" file to adapt the program's behavior to your preferences. The available options are:

[config]

pasta = path where the screenshots will be saved

tecla_sair = key that exits the program (e.g., ctrl_l, esc, q)

tecla_screenshot = key to take a screenshot (e.g., print_screen, s)

avisos = boolean value that defines whether the user wants warning boxes to appear or not

*Added key_name_helper.py to help you find the correct key name.*

Note:

The .zip file contains all necessary programs already compiled as .exe.

If any value in "config.ini" is incorrect, the program automatically replaces it with the default value and logs the change.

Author: Nikzs243

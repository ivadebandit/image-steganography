# Image Steganography Tool

## Project Overview
This project is an interactive Command-Line Interface (CLI) application built as a final project for Stanford's Code in Place course. The tool implements **steganography**—the art and science of hiding secret pieces of data inside an ordinary file. Specifically, this application allows users to safely encode a hidden text message within the pixel data of a standard PNG image, and conversely, decode a modified image to extract and reveal the hidden text. 

To a human observer, the original image and the encoded image look completely identical, making it an excellent way to pass secret messages.

---

## How It Works
Digital images are made up of millions of tiny squares called pixels. Each pixel contains three color channels: **Red, Green, and Blue (RGB)**, with values ranging from 0 to 255. 

This program manipulates the **Red channel** to hide your text, using the following methodology:

1. **Text-to-ASCII Conversion:** The application takes the secret text message and converts each character into its corresponding numerical ASCII value (for example, the letter `'H'` becomes `72`, `'i'` becomes `105`).
2. **Pixel Alteration:** The algorithm loops through the image pixel-by-pixel, replacing the exact numerical value of the pixel's Red channel with the ASCII number of a character from the message.
3. **The Stop Signal:** Because an image usually has more pixels than the message has characters, the program embeds a termination marker (`0`) immediately after the final character of the message. This tells the decoder exactly when to stop reading pixels so it doesn't print out random image data.

During decoding, the process is reversed: the program reads the Red values of each pixel one by one, translates those numbers back into text characters, and finishes instantly when it hits the `0` stop signal.

---

## Repository Components
* **`steganography.py`**: The primary executable application containing the terminal menus, input validation loops, and the pixel iteration encoding/decoding engines.
* **`simpleimage.py`**: A custom local compatibility wrapper mimicking Stanford’s proprietary cloud-based image handling structures, enabling the script to run independently on any computer.
* **`requirements.txt`**: Declares the necessary third-party package dependency (`Pillow`) used for handling lower-level pixel operations.
* **`picture.png`**: The default baseline image used to test and verify the operational integrity of the system.

---

## Local Installation & Usage

### 1. Requirements Setup
Before running the script locally, ensure you have Python installed and run the following command within an activated environment to install the image handling engine:
```bash
pip install -r requirements.txt

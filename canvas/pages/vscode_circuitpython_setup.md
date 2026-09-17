# Visual Studio Code & CircuitPython Setup Guide

This guide walks you through configuring **Visual Studio Code**, installing the **CircuitPython extension**, connecting your **Raspberry Pi Pico**, and opening the **Serial Port Monitor / REPL** to write and debug physical computing code.

---

## Overview

VS code is an _intgrated development environment_.
Meaning, a variety of programming tools are built into one application.

With this tool we will edit the code on our Pico microcontroller.
We also need to set it up to let to see information that code outputs (_like from the <code>print()</code>_).

We need to install an _extension_ in VS code that we will download the extension from the _extension marketplace_ inside the application.
The extension is called **circuitpython**.

Once we install the extension we can _open folder_ from the _File_ menu.
We open the **circuitpy** drive that is our microntroller.

Use _command + shift + P to open VS code's _command menu_.
Search for select serial port or serial monitor.
Choose the correct serial port which will have in the name _usbmodem_ or _pico_.
Then choose

---

## 1. Install Visual Studio Code

If you do not have VS Code installed:

1. Download VS Code for macOS, Windows, or Linux from [code.visualstudio.com](https://code.visualstudio.com/).
2. Install and launch the application.

---

## 2. Install Required Extensions

Open the Extensions sidebar in VS Code (`Cmd + Shift + X` on macOS, `Ctrl + Shift + X` on Windows):

### Essential Extension: CircuitPython

- Search for **`CircuitPython`** (by _Joe Sheets_ / _Adafruit Community_).
- Click **Install**.
- **What this extension provides:**
  - Auto-detects connected CircuitPython boards.
  - Automatically configures IntelliSense / code autocompletion for `board`, `digitalio`, `analogio`, `pwmio`, and other microcontroller modules.
  - Adds a 1-click **Serial Monitor** button to the bottom blue status bar.

### Recommended Extension: Python

- Search for **`Python`** (by _Microsoft_).
- Click **Install**.
- Provides syntax highlighting, auto-formatting, and indentation helpers.

---

## 3. The "Run on Save" Workflow in CircuitPython

CircuitPython microcontrollers have a built-in auto-reload engine:

- Whenever you save `code.py` (`Cmd + S` on macOS / `Ctrl + S` on Windows), CircuitPython automatically soft-reboots the chip and executes your updated code **instantly**.
- **Optional (VS Code Auto Save)**:
  - If you want VS Code to automatically save whenever you pause typing: Go to **File $\to$ Auto Save** (or set `"files.autoSave": "afterDelay"` in Settings).
  - _Recommendation_: Leaving manual save on (`Cmd + S`) is often preferred so you control precisely when the hardware reboots and starts running your new instructions.

---

## 4. Plugging In Your Microcontroller

1. **Use a Data-Capable USB Cable**:
   - Ensure your USB cable supports both power **and** data transfer (some cheap charging cables only supply power and will not communicate with your computer).
2. **Connect to Your Computer**:
   - Plug the micro-USB cable into the Raspberry Pi Pico and your computer.
3. **Verify Drive Mounting**:
   - The Pico will appear on your desktop / file explorer as an external storage drive named **`CIRCUITPY`**.
   - If your Pico mounts as `RPI-RP2` instead, it needs the CircuitPython `.uf2` file dragged onto it first (see [Microcontroller Intro](pico_microcontroller_intro.md)).

---

## 5. Opening `CIRCUITPY` in VS Code

1. In VS Code, go to **File $\to$ Open Folder...** (`Cmd + O` or `Ctrl + K Ctrl + O`).
2. Navigate to and select the **`CIRCUITPY`** drive.
3. Click **Open**.
4. In the left file explorer panel, click on **`code.py`**.
5. You are now editing the live firmware running directly on the chip!

---

## 6. Opening & Viewing the Serial Port Monitor (REPL)

The **Serial Port Monitor** is your debugging window. Any `print()` statements in your code output here, and all Python error traces appear here live.

### Method 1: Status Bar (1-Click)

- Look at the bottom blue status bar in VS Code.
- Click the **`[CIRCUITPY]`** or **`Open Serial Device`** button.

### Method 2: Command Palette

1. Press `Cmd + Shift + P` (macOS) or `Ctrl + Shift + P` (Windows).
2. Type **`CircuitPython: Open Serial Monitor`** and press `Enter`.
3. If prompted to select a device, choose the USB Serial / RP2040 port.
4. An integrated terminal tab will open at the bottom of VS Code showing the live serial stream.

---

## 7. Useful Serial Port & REPL Keyboard Shortcuts

Click inside the Serial Monitor terminal window to use these interactive controls:

| Shortcut   | Action             | Description                                                                                         |
| :--------- | :----------------- | :-------------------------------------------------------------------------------------------------- |
| `Ctrl + C` | **Interrupt Code** | Stops the currently running `code.py` script and enters the interactive Python REPL prompt (`>>>`). |
| `Ctrl + D` | **Soft Reboot**    | Re-runs `code.py` from line 1 without unplugging the USB cable.                                     |
| `Ctrl + E` | **Paste Mode**     | Allows you to paste multi-line Python blocks directly into the live REPL.                           |
| `Any Key`  | **Wake REPL**      | Press any key after an error or `Ctrl+C` to start typing live Python commands directly to the chip. |

---

## 8. Verifying Your Setup ("Hello, World!")

1. In `code.py` on your `CIRCUITPY` drive, type:
   ```python
   print("Raspberry Pi Pico Connected Successfully!")
   counter = 0
   while True:
       counter += 1
       print(f"Loop count: {counter}")
       time.sleep(1)
   ```
2. Save the file (`Cmd + S` / `Ctrl + S`).
3. Look at your **Serial Monitor**: You will see the counter printing every second.
4. Look at your **Pico board**: The green onboard LED will blink synchronously with your print statements!

---

Next: Continue to the [Microcontroller Intro & Breadboarding Tutorials](pico_microcontroller_intro.md).

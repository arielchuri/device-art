# Using the Terminal as a Serial Port Monitor

---

## Overview

When programming microcontrollers like the Raspberry Pi Pico running CircuitPython, the board communicates with your computer over a USB Serial connection (CDC UART). A serial monitor displays `print()` debugging statements from your running `code.py` script and provides direct access to the interactive CircuitPython REPL (Read-Evaluate-Print Loop).

While code editors like VS Code and Mu provide built-in graphical serial monitors, using a command-line terminal serial monitor provides a fast, lightweight, and robust tool for hardware debugging.

---

## 1. macOS Terminal

### Step 1: Identify the Serial Port
Connect your Pico to your Mac via USB and run in Terminal:
```bash
ls /dev/cu.usbmodem*
```
Your Pico will appear with a device name such as `/dev/cu.usbmodem14101` or `/dev/cu.usbmodem1101`.

> [!NOTE]
> Always use the **`/dev/cu.*`** (Call-Up) device rather than `/dev/tty.*` on macOS. `/dev/cu.*` allows direct communication without waiting for carrier-detect line handshakes.

---

### Option A: Built-in `screen` (No Installation Required)

macOS includes the `screen` utility by default. Connect using the exact device path found in Step 1 (e.g. `14101` or `1101`) and the baud rate (`115200`):

```bash
# Replace 14101 with the specific device number found in Step 1
screen /dev/cu.usbmodem14101 115200
```

#### Essential `screen` Shortcuts:
- **Disconnect & Exit**: Press `Ctrl + A`, then press `Ctrl + \` (press `y` to confirm).
- **Kill Session**: If screen becomes unresponsive, press `Ctrl + A`, then `k`, then `y`.

---

### Option B: `tio` (Recommended for Prototyping)

`tio` is a modern serial terminal that automatically reconnects whenever you unplug the board or whenever CircuitPython restarts after saving a file:

```bash
# Install via Homebrew
brew install tio

# Connect to Pico (replace 14101 with your device number from Step 1)
tio /dev/cu.usbmodem14101
```

#### Essential `tio` Shortcuts:
- **Disconnect & Exit**: Press `Ctrl + T`, then `q`.
- **Clear Screen**: Press `Ctrl + T`, then `l`.
- **Show Help**: Press `Ctrl + T`, then `?`.

---

## 2. Windows (PowerShell / Command Prompt)

### Step 1: Identify the COM Port
1. Open **Device Manager** (`Win + X` -> **Device Manager**).
2. Expand the **Ports (COM & LPT)** section.
3. Look for **USB Serial Device (COM3)**, **COM4**, or similar.

Alternatively, find available ports directly in PowerShell:
```powershell
[System.IO.Ports.SerialPort]::getportnames()
```

---

### Option A: `tio` on Windows (via Windows Package Manager)

```powershell
# Install via winget
winget install tio-community.tio

# Connect (replace COM3 with your port number)
tio COM3
```
- **Exit**: Press `Ctrl + T`, then `q`.

---

### Option B: Python `miniterm` (Built into `pyserial`)

If you have Python installed on Windows:

```powershell
pip install pyserial
python -m serial.tools.miniterm COM3 115200
```
- **Exit**: Press `Ctrl + ]`.

---

### Option C: PuTTY Graphical Serial Client

1. Download and open **PuTTY**.
2. Select **Serial** under Connection type.
3. Set **Serial line** to your COM port (e.g. `COM3`).
4. Set **Speed** to `115200`.
5. Click **Open**.

---

## 3. Linux (Ubuntu, Debian, Fedora, Arch, Raspberry Pi OS)

### Step 1: Serial Group Permissions
On Linux, serial devices belong to the `dialout` (or `uucp`) group. Ensure your user account has serial access permissions:

```bash
# Add your user to the dialout group
sudo usermod -aG dialout $USER

# On Arch Linux:
# sudo usermod -aG uucp $USER
```
*Note: Log out and log back in for group permission changes to take effect.*

---

### Step 2: Identify the Port
```bash
ls /dev/ttyACM*
```
The Pico typically appears as `/dev/ttyACM0` or `/dev/ttyACM1`.

---

### Option A: `tio` (Recommended)

```bash
# Install on Ubuntu / Debian
sudo apt install tio

# Install on Fedora
sudo dnf install tio

# Install on Arch Linux
sudo pacman -S tio

# Connect
tio /dev/ttyACM0
```
- **Exit**: Press `Ctrl + T`, then `q`.

---

### Option B: `screen`

```bash
screen /dev/ttyACM0 115200
```
- **Exit**: Press `Ctrl + A`, then `Ctrl + \` (confirm with `y`).

---

## 4. Universal CircuitPython Control Shortcuts

Once connected to your Pico through any terminal monitor, you can use standard control sequences:

| Shortcut | Function | Description |
| :--- | :--- | :--- |
| `Ctrl + C` | **Interrupt Code / Enter REPL** | Halts running `code.py` loop and opens interactive Python `>>>` shell. |
| `Ctrl + D` | **Soft Reboot** | Reloads file system and restarts `code.py` from line 1. |
| `Ctrl + B` | **Exit Raw REPL** | Returns to standard interactive REPL prompt if stuck in raw mode. |

---

## 5. Troubleshooting Common Serial Issues

1. **`Resource busy` / `Access Denied` / `Port in Use`**:
   - Only **one application** can open a serial port at a time.
   - Close any open VS Code Serial Monitors, Arduino Serial Plotters, Mu REPLs, or background terminal sessions before connecting.
2. **No Output Appearing**:
   - Press `Enter` in the terminal to verify the board is responsive.
   - Press `Ctrl + D` to reload and trigger initial startup `print()` messages.
3. **Pico Not Listed in `/dev` or Device Manager**:
   - Verify the USB cable is a **data + power cable** (some micro-USB cables are charge-only).
   - Check that the Pico power LED is illuminated.

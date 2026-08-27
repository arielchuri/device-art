# Live Demo Guide: Writing & Running Python via `nano` in Terminal

This simple 3-minute hands-on demonstration introduces students to terminal interaction, plain-text code editing in `nano`, and executing Python.

---

## 1. Quick Terminal Commands to Show on the Projector

### Step 1: Open Terminal & Create a Code Directory
```bash
mkdir device-art-code
cd device-art-code
```

### Step 2: Open `nano` to Write the Script
```bash
nano hello.py
```

---

## 2. Interactive Python Script (Type in front of the class)

```python
# hello.py - Device Art First Code Demo
import time

print("=" * 40)
print("  WELCOME TO DEVICE ART (Fall 2026)")
print("=" * 40)

name = input("Enter your name: ")
print(f"\nHello {name}!")

print("\nCounting down to physical computing:")
for i in range(3, 0, -1):
    print(f"  {i}...")
    time.sleep(1)

print("\n🚀 Ready to build physical devices!\n")
```

---

## 3. Nano Keyboard Shortcuts to Highlight
- **Save file**: `Ctrl + O` $\to$ Press `Enter` (WriteOut)
- **Exit nano**: `Ctrl + X`

---

## 4. Run the Python Script
```bash
python3 hello.py
```

---

## 5. Pedagogical Takeaways to Mention to Students
1. **Code is Just Plain Text**: No magic IDE or complicated software required—any text editor (`nano`, VS Code, Mu) can write instructions for a computer or microcontroller.
2. **From Terminal to Microcontroller**: This same Python logic (`print`, `time.sleep`, variables, loops) is what we will upload to the **Raspberry Pi Pico** in CircuitPython to control physical LEDs, motors, and OLED screens.

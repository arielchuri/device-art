# Python Cheat Sheet & Quick Intro

---

## 1. What is Python?
Python is a plain-text, human-readable programming language. The exact same Python syntax we use in the terminal will run on your **Raspberry Pi Pico** (via CircuitPython) to control hardware sensors, lights, and motors.

---

## 2. Interactive Python REPL (No Files Needed)
The **REPL** (Read-Eval-Print Loop) lets you test code instantly line-by-line.

### Launch REPL:
- **macOS / Linux**: Type `python3` $\to$ press `Enter`.
- **Windows**: Type `python` (or `py`) $\to$ press `Enter`.

*(You will see the `>>>` prompt appear).*

### Quick Commands to Try in REPL:
```python
# 1. Math & Variables
voltage = 3.3
resistor = 220
current = voltage / resistor
print(current)

# 2. Text (Strings)
name = "Ada"
print("Hello, " + name + "!")

# 3. Lists (Arrays of Sensors/Pins)
pins = ["GP0", "GP1", "GP2"]
print(pins[0])
print(len(pins))
```

### Exit REPL:
Type `exit()` or press `Ctrl + D` (`Ctrl + Z` then `Enter` on Windows).

---

## 3. Writing & Running a Script via `nano`

### Step 1: Create a Script
```bash
nano age_check.py
```

### Step 2: Write Minimal Script
```python
# Prompt the user for input
user_input = input("Enter your age: ")

# Check if input is an integer
try:
    age = int(user_input)
    print(f"You are {age} years old.")
    
    # Extra credit: Estimated birth year
    birth_year = 2026 - age
    print(f"You were born around {birth_year}.")
except ValueError:
    print("Error: Please enter a whole number.")
```

### Step 3: Save & Exit `nano`
- **Save**: `Ctrl + O` $\to$ press `Enter`
- **Exit**: `Ctrl + X`

### Step 4: Run the Script
- **macOS / Linux**: `python3 age_check.py`
- **Windows**: `python age_check.py`

---

## 4. Summary Table

| Goal | macOS / Linux | Windows |
| :--- | :--- | :--- |
| **Launch REPL** | `python3` | `python` or `py` |
| **Exit REPL** | `exit()` or `Ctrl + D` | `exit()` or `Ctrl + Z` + `Enter` |
| **Edit File** | `nano filename.py` | `nano filename.py` (or `notepad filename.py`) |
| **Run Script** | `python3 filename.py` | `python filename.py` |

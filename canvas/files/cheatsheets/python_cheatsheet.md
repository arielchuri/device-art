# Python Cheat Sheet & REPL Quick Intro

---

## 1. What is Python?

Python is a plain-text, human-readable programming language. The exact same Python syntax we type here will run on your **Raspberry Pi Pico** (via CircuitPython) to control hardware sensors, lights, and motors.

---

## 2. Interactive Python in the Terminal (No Files Needed)

The **REPL** (Read-Eval-Print Loop) lets you run Python commands line-by-line directly inside your terminal window.

### Step 1: Open Your Terminal & Start Python

Open your Terminal application (or PowerShell on Windows). In the terminal prompt, type:

- **macOS / Linux**:

```bash
python3
```

- **Windows**:

```bash
python
```

*Press `Return` (Enter). Your prompt will change from `$` to `>>>`. You are now inside Python!*

---

### Step 2: Running Commands Line-by-Line in REPL

#### A. Storing a Voltage Variable

Type this into the `>>>` prompt and press `Return`:

```python
voltage = 3.3
```

- **What this does**: Creates a memory variable named `voltage` and stores the number `3.3` (the standard operating voltage of our Raspberry Pi Pico).
- **Response**: None (Python silently remembers the value).

---

#### B. Storing a Resistor Value

Type this into the `>>>` prompt and press `Return`:

```python
resistor = 220
```

- **What this does**: Creates a variable named `resistor` holding `220` (the Ohms rating of our LED protective resistors).
- **Response**: None (Python silently stores it).

---

#### C. Calculating Current (Ohm's Law)

Type this into the `>>>` prompt and press `Return`:

```python
current = voltage / resistor
```

- **What this does**: Divides voltage by resistance to calculate electrical current ($I = V / R$) and stores the result in `current`.
- **Response**: None.

---

#### D. Inspecting the Result

Type this into the `>>>` prompt and press `Return`:

```python
current
```

- **Response**:

```python
0.015
```

- **What this does**: Prints the stored value. `0.015` Amperes (or 15 milliamps)—the exact safe current for powering an LED!

---

#### E. Storing and Printing Text (Strings)

Type this into the `>>>` prompt and press `Return`:

```python
name = "Ada"
```

- **What this does**: Stores the text string `"Ada"` in a variable named `name`.

Now print a greeting:

```python
print("Hello, " + name + "!")
```

- **Response**:

```python
Hello, Ada!
```

- **What this does**: Combines the text strings and prints the output to your terminal screen.

---

#### F. Storing a List of Microcontroller Pins

Type this into the `>>>` prompt and press `Return`:

```python
pins = ["GP0", "GP1", "GP2"]
```

- **What this does**: Creates a list containing three Raspberry Pi Pico pin names.

Ask Python for the first pin (computers start counting at 0):

```python
pins[0]
```

- **Response**:

```python
'GP0'
```

Ask Python how many pins are in the list:

```python
len(pins)
```

- **Response**:

```python
3
```

---

### Step 3: How to Exit Python

When you are done testing in Python, return back to your regular terminal prompt:

Type this and press `Return`:

```python
exit()
```

*(Or press `Ctrl + D` on Mac/Linux, `Ctrl + Z` then `Enter` on Windows).*

Your prompt will change back to `$` (or `%`). You are now back in the standard terminal shell.

---

## 3. Formatting Python Code & Canvas Submission

### Python Indentation Rule:
In Python, indentation (tabs or 4 spaces) defines which lines of code belong inside an `if` block, loop, or function:

```python
if fred == 42:
    # This indented line runs ONLY when fred equals 42
    print("Hello World")
```

### Comment Lines (`#`): All Code Must Be Commented!
Comments are notes written directly in your code that Python ignores during execution. They begin with a `#` symbol:

```python
# Calculate LED current using Ohm's Law (I = V / R)
voltage = 3.3   # Pico logic level
resistor = 220  # Current limiting resistor in Ohms
current = voltage / resistor
```

- **Why use comments?**
  - **Self-Documentation**: Explains your logic so future-you and collaborators understand *why* you wrote the code a certain way.
  - **Debugging**: Helps you trace where values change and temporarily disable lines of code without deleting them.
  - **Course Requirement**: **All code submitted for homework and studio projects must include clear comments** explaining each major variable, calculation, condition, and function.

### How to Format Code Blocks on Canvas:
To make sure Canvas preserves your indentation and displays syntax highlighting properly, wrap your code in triple backticks with the `python` tag:

````markdown
```python
# Prompt user for their age and validate input
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```
````

---

## 4. Writing & Running a Standalone Script via `nano`

When you want to save your Python instructions permanently into a file rather than typing them line-by-line, use `nano`.

### Step 1: Create a New File in `nano`

From your regular terminal prompt (`$`), type:

```bash
nano age_check.py
```

*Press `Return`. The `nano` text editor will open inside your terminal.*

---

### Step 2: Type Your Python Script

Type or paste the following code into the editor:

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

---

### Step 3: Save and Exit `nano`

1. Press `Ctrl + O` $\to$ press `Return` (to write/save the file).
2. Press `Ctrl + X` (to exit `nano` and return to the terminal prompt).

---

### Step 4: Run the Script in the Terminal

Run your saved script by telling Python to execute the file:

- **macOS / Linux**:

```bash
python3 age_check.py
```

- **Windows**:

```bash
python age_check.py
```

---

## 5. Summary Quick Reference

| Action | What You Type | Where You Type It |
| :--- | :--- | :--- |
| **Enter Python** | `python3` (Mac/Linux) or `python` (Win) | Terminal Prompt (`$`) |
| **Run Python Line** | `voltage = 3.3` + press `Return` | Python Prompt (`>>>`) |
| **Exit Python** | `exit()` | Python Prompt (`>>>`) |
| **Create/Edit Script** | `nano age_check.py` | Terminal Prompt (`$`) |
| **Run Script File** | `python3 age_check.py` | Terminal Prompt (`$`) |

# Terminal Cheat Sheet & Quick Intro

---

## 1. What is the Terminal?
The Terminal (or Command Line Interface) is a direct, text-based way to control your computer without a graphical user interface (GUI).

> **Rule #1**: **No mouse or trackpad.** Everything is navigated, created, and executed using your keyboard.

---

## 2. Opening the Terminal
- **macOS**: Press `Cmd + Space` $\to$ type `Terminal` $\to$ press `Enter`.
- **Linux**: Press `Ctrl + Alt + T`.
- **Windows**: Press `Win + S` $\to$ type `PowerShell` or `Git Bash` $\to$ press `Enter`. *(Git Bash is recommended for Unix commands).*

---

## 3. The Prompt & Directory Navigation

### The Prompt
When you open your terminal, you see a prompt ending in `$` or `%`. It waits for your command:
```bash
username@computer:~$ 
```

### Paths & Special Symbols
- `/` : Root directory (the very top of your file system).
- `~` : Home directory (e.g. `/Users/yourname` on Mac or `C:\Users\yourname` on Windows).
- `.` : Current directory.
- `..` : Parent directory (one level up).
- **Absolute Path**: Starts from root `/` (e.g. `/Users/ariel/Desktop`).
- **Relative Path**: Starts from where you are right now (e.g. `Desktop/projects`).

---

## 4. Essential Commands (Step-by-Step)

### Create a Folder & Enter It
```bash
mkdir testDir
cd testDir
```

### List Files
```bash
ls
```

### Command Help & Options (Flags)
Add flags to change how commands behave:
```bash
ls -ltrh
```
*(Lists all files sorted by time in reverse order, with human-readable file sizes).*
- **macOS / Linux Help**: `man ls` or `ls --help`
- **Windows (PowerShell)**: `Get-Help Get-ChildItem`

### Print Text & Redirect to Files
Print text directly to terminal output:
```bash
echo "hello"
```
Write (redirect) text into a new file using `>`:
```bash
echo "hello" > hello.txt
ls
```
Read the file contents:
```bash
cat hello.txt
```

---

## 5. Editing Files with `nano`

Open `nano` to create a file called `world.txt`:
```bash
nano world.txt
```
1. Type: `world!`
2. **Save**: Press `Ctrl + O` $\to$ press `Enter`.
3. **Exit**: Press `Ctrl + X`.

Verify the file:
```bash
ls
cat hello.txt world.txt
```

---

## 6. Counting & Piping (`|`)

Count lines, words, and characters:
```bash
wc hello.txt
```

Combine multiple files and **pipe (`|`)** the stream directly into another tool:
```bash
cat hello.txt world.txt | wc
```

Save your directory listing directly into a text file:
```bash
ls > file-list.txt
cat file-list.txt
```

---

## 7. Hands-on Terminal Quiz

1. Use `nano` to create a list of 6 fruits, each on its own line.
2. Save and write it to a file called `fruits.txt`, then exit `nano`.
3. In a **single command line**: `cat` the contents of `fruits.txt`, pipe (`|`) the output into `sort`, and redirect (`>`) the sorted output into `sorted-fruits.txt`.

<details>
<summary><b>Click to reveal solution</b></summary>

```bash
# Step 1 & 2:
nano fruits.txt
# (type apple, banana, orange, etc., then Ctrl+O, Enter, Ctrl+X)

# Step 3:
cat fruits.txt | sort > sorted-fruits.txt

# Verify:
cat sorted-fruits.txt
```
</details>

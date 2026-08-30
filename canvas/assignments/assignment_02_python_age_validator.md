# Assignment 02: Python Interactive Script (Age Validator)

- **Due Date**: Wednesday, September 2, 2026 at 7:00 PM
- **Points**: 20 Points (+ Extra Credit)
- **Submission Type**: Text Entry (Paste your code formatted as a code block) & File Upload (`.py`)
- **Quick Reference**: 📖 **[Python Cheatsheet & Syntax Guide](https://github.com/arielchuri/device-art/blob/main/canvas/files/cheatsheets/python_cheatsheet.md)**

---

## Assignment Brief

Create a standalone Python script (e.g. `age_check.py`) that runs in the terminal.

### Core Requirements (20 Points):
1. **Interactive Prompt**: Prompt the user to enter their age via `input()`.
2. **Integer Validation & Output**:
   - If a valid integer is entered, print a clean confirmation message stating their age.
   - If the input is not a valid integer (e.g. text, decimal, empty), handle the error gracefully and print a clear error message (using `try / except ValueError` or string validation).

---

## 📝 How to Submit on Canvas:
1. Open the Canvas assignment submission.
2. Select **Text Entry** and paste your Python code directly into the box formatted inside a code block (` ```python ... ``` `).
3. *(Optional)* You may also attach your raw `age_check.py` file.

---

## Extra Credit (Bonus Points):
- **Year of Birth Calculation**: Automatically compute and display the user's estimated year of birth (e.g. `2026 - age`).
- **Zodiac Sign**: Prompt for the user's birth month/day (or birth year for Chinese Zodiac) and print their corresponding zodiac sign.

---

## Rubric Point Table

| Criterion | Description | Points |
| :--- | :--- | :---: |
| **Interactive User Input** | Script prompts for user input in the terminal and accepts values | 5 pts |
| **Type Checking & Error Handling** | Correctly distinguishes integer inputs from invalid strings with a helpful error message | 10 pts |
| **Output Formatting & Code Quality** | Clean printed output, readable code, and proper script execution without unhandled crashes | 5 pts |
| **Extra Credit: Birth Year & Zodiac** | Accurately calculates birth year and determines zodiac sign | *Bonus* |
| **Total** | | **20 pts** |

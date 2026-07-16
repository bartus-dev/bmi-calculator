# BMI Calculator

A simple, beginner-friendly command-line application written in Python that calculates a user's Body Mass Index (BMI) based on their weight and height, and classifies the result into standard health categories.

## Description

This project is a console-based BMI (Body Mass Index) calculator. It prompts the user to enter their weight (in kilograms) and height (in centimeters), then computes their BMI and displays a classification (e.g., Underweight, Normal, Overweight, Obese) based on standard medical BMI ranges. The application includes input validation to handle invalid or non-numeric input gracefully.

## Features

- ⚖️ **BMI Calculation** — Computes BMI using the standard formula: `BMI = weight (kg) / height (m)²`
- 🩺 **Health Classification** — Categorizes the result into six standard classes:
  - Underweight
  - Normal
  - Overweight
  - Class I Obese
  - Class II Obese
  - Class III Obese
- ✅ **Input Validation** — Rejects weight or height values that are zero or negative, prompting the user to re-enter valid data.
- 🛡️ **Error Handling** — Catches non-numeric input (e.g., letters or symbols) using a `try/except` block and returns a clear error message instead of crashing.
- 🔁 **Retry Loop** — Keeps asking for input until a valid value is provided, improving the user experience.

## Technologies

- [Python 3.x](https://www.python.org/) — no external dependencies required
- Built-in Python features only:
  - `input()` for user interaction
  - `try/except` for error handling
  - f-strings for formatted output

## Installation and Setup Guide

Follow these steps to run the BMI Calculator on your own machine.

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Verify Python Installation

Make sure Python 3 is installed on your system:

```bash
python --version
```

If it's not installed, download it from [python.org](https://www.python.org/downloads/).

### 3. Run the Application

No additional libraries are required. Simply run the script:

```bash
python bmi_calculator.py
```

### 4. Follow the Prompts

The program will ask you to enter your weight and height:

```
---- BMI CALCULATOR ----

Type your weight (kg): 70

Type your height (cm): 175
Your bmi: 22.9

Classification: Normal
```

## Usage Notes

- Weight must be entered in **kilograms**.
- Height must be entered in **centimeters** (it is automatically converted to meters internally).
- If you enter `0`, a negative number, or non-numeric text, the program will display an error message and prompt you again (or exit with an error, depending on the input type).

## Possible Future Improvements

- Support for imperial units (lbs/inches)
- Save BMI history to a file
- Graphical user interface (GUI)
- Unit tests for the calculation logic

## License

This project is open-source and available for personal or educational use. Feel free to modify and expand it.
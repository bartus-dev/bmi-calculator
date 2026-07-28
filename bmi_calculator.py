import json
from datetime import datetime

def save_history(weight, height, bmi, classification):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_measurment = {
        "date": current_time,
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 1),
        "classification": classification
    }

    file_name = "history.json"

    try:
        with open(file_name, "r") as file:
            history_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history_list = []

    history_list.append(new_measurment)

    with open(file_name, "w") as file:
        json.dump(history_list, file, indent=4)

    print("\n[SUCCESS] Measurement saved to history.json!")
    

def calculate():
    print("---- BMI CALCULATOR ----")
    
    while True:
        try:
            user_weight = int(input("\nType your weight (kg): "))
            if user_weight <= 0:
                print("Error: Weight must be greater than 0")
            else:
                break
        except ValueError:
            print("Error: It is not a number. Please enter a valid digit.")

    while True:
        try:
            user_height = int(input("\nType your height (cm): "))
            if user_height <= 0:
                print("Error: Height must be greater than 0")
            else:
                break
        except ValueError:
            print("Error: It is not a number. Please enter a valid digit.")
        
    user_height = user_height / 100
    bmi = user_weight / (user_height)**2

    print(f"\nYour bmi: {bmi:.1f}")

    if bmi < 18.5:
        result_class = "Underweight"
    elif bmi < 25.0:
        result_class = "Normal" 
    elif bmi < 30.0:
        result_class = "Overweight"
    elif bmi < 35.0:
        result_class = "Class I obese"
    elif bmi < 40.0:
        result_class = "Class II obese"
    else:
        result_class = "Class III obese"

    save_history(user_weight, user_height * 100, bmi, result_class)

    return f"\nClassification: {result_class}\n"

print(calculate())

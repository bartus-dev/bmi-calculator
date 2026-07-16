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
        return "Classification: Underweight\n"
    elif bmi < 25.0:
        return "Classification: Normal\n" 
    elif bmi < 30.0:
        return "Classification: Overweight\n"
    elif bmi < 35.0:
        return "Classification: Class I obese\n"
    elif bmi < 40.0:
        return "Classification: Class II obese\n"
    else:
        return "Classification: Class III obese\n"
    
print(calculate())

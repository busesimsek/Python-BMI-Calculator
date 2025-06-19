"""
BMI Calculator Project
👩🏻‍💻 Owner: Buse Şimşek
🗓️ Date: June 19, 2025

📌 Description: This project calculates the Body Mass Index (BMI) using a person's height and weight.
It then classifies the result into standard health categories such as underweight, normal, overweight, and obese.

🎯 Goal: Provide a simple and interactive way to assess an individual's BMI and interpret the result using Python.

Classification      BMI range (kg/m²)
Severe Thinness     < 16
Moderate Thinness   16 - 17
Mild Thinness       17 - 18.5
Normal              18.5 - 25
Overweight          25 - 30
Obese Class I       30 - 35
Obese Class II      35 - 40
Obese Class III     > 40

BMI classification ranges referenced from Calculator.net BMI Calculator, accessed June 2025.
"""

name = input("Enter your name: ")

while True:
    try:
        weight = float(input(f"{name.title()}, enter your weight in kgs: "))
        height = float(input(f"{name.title()}, enter your height in cms: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers. Please try again.\n")
            continue

        height_m = height / 100  # converting height from cm to meters for the BMI formula
        bmi = weight / (height_m ** 2)
        
        print(f"{name.title()}, your BMI is {bmi:.1f}.")

        if bmi > 0:
            if bmi < 16:
                print("You are in the Severe Thinness category. Please consult a healthcare provider as soon as possible.")
            elif 16 <= bmi < 17:
                print("You are in the Moderate Thinness category. It's recommended to seek medical advice for proper guidance.")
            elif 17 <= bmi < 18.5:
                print("You are in the Mild Thinness category. A healthcare provider can help you reach a healthier weight.")
            elif 18.5 <= bmi < 25:
                print("You are in the Normal weight range. Keep up the good work maintaining a healthy lifestyle!")
            elif 25 <= bmi < 30:
                print("You are in the Overweight range. Consider reviewing your diet and activity level with a professional.")
            elif 30 <= bmi < 35:
                print("This falls under Obese Class I. It may be beneficial to consult with a healthcare provider for guidance.")
            elif 35 <= bmi < 40:
                print("This falls under Obese Class II. Professional support could help you take positive steps for your health.")
            else:
                print("This falls under Obese Class III. It's important to seek medical advice to manage your health effectively.")
                
            break  # valid input and result shown, time to exit the loop

    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
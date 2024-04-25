height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you're underweight")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi}, you're weight is normal")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you're overweight")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you're obese")
else:
    print(f"Your BMI is {bmi}, you're clinically obese")

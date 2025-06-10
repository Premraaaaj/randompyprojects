print("Hello user, welcome to the BMI calculator!")
height= float(input("Please enter your height in meters: "))
weight= float(input("Please enter your weight in kilograms: "))

bmi=weight/(height**2)
print("Your BMI is: ", bmi)

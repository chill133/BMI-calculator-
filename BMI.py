height = input("What is your height?")
weight = input("What is your weight?")
BMI = 703 * (int(weight))/(int(height)**2)
print("Your BMI " + str(BMI))
if (BMI <= 18):
	print("You are underweight")
elif (BMI >= 18) and (BMI <= 26):
	print("You are normal weight")
else:
	print("You are overweight")


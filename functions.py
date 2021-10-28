your_height = int(input('enter your height in inches: '))
your_weight = int(input('enter your weight in lbs.: '))
def bmi(weight, height):
    return  (weight/(height**2))*703
your_bmi = bmi(your_weight, your_height)
print(your_bmi)
if (your_bmi < 20):
    print("You have a bmi of " + str(your_bmi) + " which is good.")
elif (your_bmi < 30):
    print("You have a bmi of " + str(your_bmi) + " which is ok.")
elif (your_bmi < 40):
    print("You have a bmi of " + str(your_bmi) + " which is not that good.")
else:
    print("You have a bmi ok " + str(your_bmi) + " and should go to the doctors.")
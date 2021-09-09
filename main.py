# x = int(input("Please enter your first number: "))
# y = int(input("Second number please: "))
# print(x + y)


#height = int(input('enter your height in inches: '))
#weight = int(input('enter your weight in lbs.: '))

#bmi = (weight/(height**2))*703
#print("Your BMI is: " + str(bmi))

#if(bmi < 20):
 #   print("Good")
#elif(bmi < 30):
 #   print("Not as good")
#elif(bmi < 40):
   # print("Uh Oh... better see a doctor.")
#else:
   # print("Seriously need some help. You might be in a coma soon.")


#lovely_loveseat_description = " Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

#lovely_loveseat_price = 254.00

#stylish_settee_description = " Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

#stylish_settee_price = 180.50

#luxurious_lamp_description = " Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

#luxurious_lamp_price = 52.15

#sales_tax = .088

#customer_one_total = 0
#customer_one_itemization = ""

#customer_one_total += lovely_loveseat_price
#customer_one_itemization += lovely_loveseat_description
#customer_one_total += luxurious_lamp_price
#customer_one_itemization += luxurious_lamp_description

#customer_one_tax = customer_one_total * sales_tax
#customer_one_total += sales_tax

#print("Customer One Items: ")
#print(customer_one_itemization)

#print("Customer One Total: ")
#print(customer_one_total)


print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("your weight:", weight)
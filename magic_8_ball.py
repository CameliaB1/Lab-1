import random
random_number = random.randint(1, 12)
name = "Sarah"
question = "Will I win the game?"
answer = " "
print("Ask Magic 8-Ball a question.")
if name == " ":
  print("Question: " + question)
elif name == "Sarah":
  print( name + " asks: " + question )
else:
  print("Error")

if question == " ":
  print("You must ask a question.")
else:
  print("Magic 8-Ball's answer: " + answer )

if random_number == 1:
  print("Yes - definitely.")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Outlook not so good.")
elif random_number == 9:
  print("Very doubtful.")
elif random_number == 10:
  print("More that likely.")
elif random_number == 11:
  print("Probaly not.")
elif random_number == 12:
  print("Not likely.")
else:
  print("Error")

print("Would you like to ask the Magic 8-Ball another question?")
ask1 = "No"
ask = "Yes"
ask = "No"
if ask1 == "No":
    print("You can always come back and ask the Magic 8-ball a question later.")
    print("THE END")
elif ask1 == "Yes":
    print("Ask Magic 8-Ball a question.")
else:
    print("Would you like to ask the Magic 8-Ball another question?")
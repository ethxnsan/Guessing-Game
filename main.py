import random
computerNumber = random.randint(0, 10)
userGuess = int(input("Guess what number I am thinking of between 0-10:"))                              
if (userGuess == computerNumber) :
  print("You guessed correctly!")
else:
  print("Wrong! My number was "+ str(computerNumber) + ".")
  
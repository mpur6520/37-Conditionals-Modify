#Maru Puran
#October 23, 2023
#modify and add to prexisting code to further get comfortable with using if else and else if statements and get familiar with its usage in a program as well as recognize the usage it has

# Starter Code

number = 5 #set number variable (create) equal to five
print("I have thought of a number between 1 and 10,") #print they've guessed a number between 1 and 10
guess = int(input("\nCan you guess what it is? ")) #create variable guess and store the users answer to the question "guess the number" as an integer


if guess < number: #checks if user's input is less than the number
  print("You guessed too low!") #if true then print the number's low
if guess > number: #checks if the user's input is greater than the number
  print("You guessed too high!") #if it is then print the number is too high

#add code to alert user whether their guess was correct or not by comparing values
if guess == number: #check if the guess is equal to number, or if the guess is 5
  print("You got it!") #print the statement "you got it!" if conditional is true
else: #runs if the conditional is false
  print("Bad luck.") #print "bad luck" if the conditional in line 14 is false
  guess = int(input("\nTry again! Enter a guess: "))
  if guess != number: #check if the guess is not equal to number
    print("You guessed wrong again... :(")
    print("\nThe number was", number) #print the number for user to see
  else:
    print("You guessed right this time!")
    print("\nThe number was", number)

#add code to ask user if they guessed correctly
correct = input("\nDid you guess correctly? Yes or No? ").lower() #asks user if they got the number right and stores that answer into a variable called correct; transforms string into lowercase to make it easier to check if its right, but user capitalized something, etc.

#conditional statement to check the user's answer and respond to it
if correct == "yes" or correct == " yes": #checks if the user input the word "yes" in response to asking if they were correct
  print("\nWell done!") #print the words well done if the user inputted yes in response to asking if they were correct
elif correct == "no" or correct == " no": #checks if the user input the word "no" in response to asking if they were correct
  print("\nNevermind.") #print the words nevermind if the user inputted no in response to asking if they were correct
else: #runs if both conditionals are false
  print("\nI don't understand. Please enter 'yes' or 'no'.") #print the words I don't understand if the user inputted something else not "yes" or "no"
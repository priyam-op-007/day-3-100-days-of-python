a = type(int("5") / int(2.7))
print(a)
###########################################
birthday_date = input("whats your birthdate? ")
if int(birthday_date)>20:
  print("they are late birthday makers")
else:
  print("get out")
#####################################################
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if int(number)%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")
################################################################
#Adventure ride
age = input("whats your age? ")
height = input("whats your height? ")
if int(age) < 12:
  if float(height) > 120:
    print("You have to pay rs 5")
  else:
    print("you cannot go on the ride")
elif (int(age) >= 12 & int(age) < 18):
  if float(height) > 120:
    print("You have to pay rs 7")
  else:
    print("you cannot go on the ride")
else:
  if float(height) > 120:
    print("You have to pay rs 12")
  else:
    print("you cannot go on the ride")
########################################################
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 ==0:
    if year%100==0:
        if year%400==0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
#####################################################################
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S":
    bill = bill + 15
    if add_pepperoni == "Y":
        bill = bill + 2
    elif add_pepperoni == "N":
        bill = bill + 0
    else:
        print("Enter Y or N only")

elif size == "M":
    bill = bill + 20
    if add_pepperoni == "Y":
        bill = bill + 3
    elif add_pepperoni == "N":
        bill = bill + 0
    else:
        print("Enter Y or N only")
elif size == "L":
    bill = bill + 25
    if add_pepperoni == "Y":
        bill = bill + 3
    elif add_pepperoni == "N":
        bill = bill + 0
    else:
        print("Enter Y or N only")
else:
    print("Enter a valid pizza size!")
if extra_cheese == "Y":
    bill = bill + 1
elif extra_cheese == "N":
    bill = bill + 0
else:
    print("Enter Y or N only")

print(f"Your final bill is: ${bill}.")
##########################################################
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1.lower() + name2.lower()

no_of_letter_t= combined_name.count("t") 
no_of_letter_r= combined_name.count("r") 
no_of_letter_u= combined_name.count("u") 
no_of_letter_e= combined_name.count("e") 
no_of_letter_l= combined_name.count("l") 
no_of_letter_o= combined_name.count("o") 
no_of_letter_v= combined_name.count("v") 

true_score = no_of_letter_t + no_of_letter_r + no_of_letter_u + no_of_letter_e
love_score = no_of_letter_l + no_of_letter_o + no_of_letter_v + no_of_letter_e

final_love_score = true_score*10 + love_score

if final_love_score < 10 or final_love_score > 90:
    print(f"Your score is {final_love_score}, you go together like coke and mentos.")
elif final_love_score > 40 and final_love_score < 50:
    print(f"Your score is {final_love_score}, you are alright together.")
else:
    print(f"Your score is {final_love_score}.")




Output -
<class 'float'>
whats your birthdate? 34
they are late birthday makers
Which number do you want to check? 344
This is an even number.
whats your age? 20
whats your height? 234
You have to pay rs 7
Which year do you want to check? 606
Not leap year.
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M, or L L
Do you want pepperoni? Y or N Y
Do you want extra cheese? Y or N Y
Your final bill is: $29.
Welcome to the Love Calculator!
What is your name? 
priyam
What is their name? 
terracota
Your score is 62.

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
  



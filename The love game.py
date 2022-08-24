print('''┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈ 
╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈
▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈
▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏
▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲
▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕
▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱
┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈
''')
print('''______$¦$¦$¦$ ____ $¦$¦$¦$
____$¦$_____$$__$$_____$¦$
___$¦$________$$________$¦$
__ $¦$___________________$¦$
___$¦$__________________$¦$
_(¯`.´¯)$¦$___________$¦$(¯`.´¯)
(¯≻ ✦ ≺¯)$¦$_______$¦$(¯≻ ✦ ≺¯)
_(_.^._)____$¦$___$¦$____ (_.^._)
_____(¯`.´¯) __$¦$__ (¯`.´¯)
___ (¯≻ ✦ ≺¯) _ $_ (¯≻ ✦ ≺¯)
_____(_.^._) (¯`.´¯)_(_.^._)
__________(¯≻ ✦ ≺¯)
_____(¯`.´¯) (_.^._) (¯`.´¯)
___ (¯≻ ✦ ≺¯) ____(¯≻ ✦ ≺¯)
_____(_.^._) ______ (_.^._)
''')

print("Welcome to the Love Game!!")
print("Your mission is to find love be forever with him!! Make your choices wisely because at any point you could lose him forever!")
school = input('You are at the school, and two boys named "Ekansh" and "Priyam" ask you for a date. Whom would you choose?\n')
if school.lower() == "priyam":
  print("You chose priyam! Love grows to 25%. You went for a date with him! ")
  drink = input('The waiter comes and asks you for what you would drink! You have two options - "Cocktails" and "Mocktails". What would you choose?\n')
  if drink.lower() == "mocktails":
    print("You chose mocktails! and coincidently priyam loves mocktails too!! Love grows to 50%!")
    vacation = input('You both decide to go on a vacation during the summer break! Priyam asks you where do you want to go? He gives you three options - "Snowy Hills" , "Desert" , "Beach". What would you choose?\n')
    if vacation.lower() == "snowy hills":
      print('You chose to go to the Snowy Hills for vacation and for Priyam it is his favourite place to go on summer holidays! Love grows to 75%')
      affair = input('After 5 years of dating, one day you are approached by a very rich and handsome guy who happens to be of your age! Would you go on a affair date with him? Answer in "Yes" or "No" \n')
      if affair.lower() == "no":
        print('You are loyal to Priyam and your relationship! Love grows to 100%')
        proposal = input('Priyam proposes you in a very scenic location and gave you the biggest surprise of your life! Will you say "Yes" or "No"? \n')
        if proposal.lower() == "yes":
          print('You said YES and you get married to Priyam who treats you like a qween and you both live your happiest life!')
        elif proposal.lower() == "no" :
          print('You said NO to the proposal and that made Priyam very sad and you both go your own ways to live a individual new life')
        else:
          print("Type a valid answer")
      elif affair.lower() == "yes" :
        print('You start dating that other guy secretly , after a few weeks Priyam came to know about this and you two break up........')
      else:
        print("Type a valid answer")
    elif vacation.lower() == "desert" :
      print("you two go to the desert for vacation in the summer , Priyam gets very irritated and angry about this idea of yours as he cant withstand heat and atlast he breaks up with you! ")
    elif vacation.lower() == "beach" :
      print("You both go to the beach and had a great time together!! Love grows to 60%")
      offer = input('Your friends from work offered you to go on a cruise with them "free of cost". You call Priyam to ask about the same but he didnt pick up the call. Will you go on the cruise? "Yes" or "No"? \n')
      if offer.lower() == "no" :
        print("You value the decisions of Priyam and decide not to go without asking him about the same! Love grows to 75%")
        affair = input('After 5 years of dating, one day you are approached by a very rich and handsome guy who happens to be of your age! Would you go on a affair date with him? Answer in "Yes" or "No" \n')
      if affair.lower() == "no":
        print('You are loyal to Priyam and your relationship! Love grows to 100%')
        proposal = input('Priyam proposes you in a very scenic location and gave you the biggest surprise of your life! Will you say "Yes" or "No"? \n')
        if proposal.lower() == "yes":
          print('You said YES and you get married to Priyam who treats you like a qween and you both live your happiest life!')
        elif proposal.lower() == "no" :
          print('You said NO to the proposal and that made Priyam very sad and you both go your own ways to live a individual new life')
        else:
          print("Type a valid answer")
      elif affair.lower() == "yes" :
        print('You start dating that other guy secretly , after a few weeks Priyam came to know about this and you two break up........')
      else:
        print("Type a valid answer")
  elif drink.lower() == "cocktails":
    print("Priyam hates cocktails and doesnt want to be with someone who drinks it. He breaks up with you!")
  else:
    print("Type a valid answer")
elif school.lower() == "ekansh":
  print("You chose ekansh! Love grows to 25%. You went for a date with him! ")
  drink = input('The waiter comes and asks you for what you would drink! You have two options - "Cocktails" and "Mocktails". What would you choose?\n')
  if drink.lower() == "cocktails":
    print("You chose cocktails! and coincidently ekansh loves cocktails too!! Love grows to 50%!")
    vacation = input('You both decide to go on a vacation during the summer break! Ekansh asks you where do you want to go? He gives you three options - "Snowy Hills" , "Desert" , "Beach". What would you choose?\n')
    if vacation.lower() == "beach":
      print('You chose to go to the Beach for vacation and for Ekansh it is his favourite place to go on summer holidays! Love grows to 75%')
      affair = input('After 5 years of dating, one day you are approached by a very rich and handsome guy who happens to be of your age! Would you go on a affair date with him? Answer in "Yes" or "No" \n')
      if affair.lower() == "no":
        print('You are loyal to Ekansh and your relationship! Love grows to 100%')
        proposal = input('Ekansh proposes you in a very scenic location and gave you the biggest surprise of your life! Will you say "Yes" or "No"? \n')
        if proposal.lower() == "yes":
          print('You said YES and you get married to Ekansh who treats you like a qween and you both live your happiest life!')
        elif proposal.lower() == "no" :
          print('You said NO to the proposal and that made Ekansh very sad and you both go your own ways to live a individual new life')
        else:
          print("Type a valid answer")
      elif affair.lower() == "yes" :
        print('You start dating that other guy secretly , after a few weeks Ekansh came to know about this and you two break up........')
      else:
        print("Type a valid answer")
    elif vacation.lower() == "desert" :
      print("you two go to the desert for vacation in the summer , Ekansh gets very irritated and angry about this idea of yours as he cant withstand heat and atlast he breaks up with you! ")
    elif vacation.lower() == "snowy hills" :
      print("You both go to the snowy hills and had a great time together!! Love grows to 60%")
      offer = input('Your friends from work offered you to go on a cruise with them "free of cost". You call Ekansh to ask about the same but he didnt pick up the call. Will you go on the cruise? "Yes" or "No"? \n')
      if offer.lower() == "no" :
        print("You value the decisions of Ekansh and decide not to go without asking him about the same! Love grows to 75%")
        affair = input('After 5 years of dating, one day you are approached by a very rich and handsome guy who happens to be of your age! Would you go on a affair date with him? Answer in "Yes" or "No" \n')
      if affair.lower() == "no":
        print('You are loyal to Ekansh and your relationship! Love grows to 100%')
        proposal = input('Ekansh proposes you in a very scenic location and gave you the biggest surprise of your life! Will you say "Yes" or "No"? \n')
        if proposal.lower() == "yes":
          print('You said YES and you get married to Ekansh who treats you like a qween and you both live your happiest life!')
        elif proposal.lower() == "no" :
          print('You said NO to the proposal and that made Ekansh very sad and you both go your own ways to live a individual new life')
        else:
          print("Type a valid answer")
      elif affair.lower() == "yes" :
        print('You start dating that other guy secretly , after a few weeks Ekansh came to know about this and you two break up........')
      else:
        print("Type a valid answer")
  elif drink.lower() == "mocktails":
    print("Ekansh hates mocktails, he thinks those are very bland and tasteless. He doesnt want to be with someone who drinks it. He breaks up with you!")
  else:
    print("Type a valid answer")
else:
  print("Type a valid answer.")


        
Output - 

┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈ 
╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈
▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈
▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏
▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲
▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕
▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱
┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈

______$¦$¦$¦$ ____ $¦$¦$¦$
____$¦$_____$$__$$_____$¦$
___$¦$________$$________$¦$
__ $¦$___________________$¦$
___$¦$__________________$¦$
_(¯`.´¯)$¦$___________$¦$(¯`.´¯)
(¯≻ ✦ ≺¯)$¦$_______$¦$(¯≻ ✦ ≺¯)
_(_.^._)____$¦$___$¦$____ (_.^._)
_____(¯`.´¯) __$¦$__ (¯`.´¯)
___ (¯≻ ✦ ≺¯) _ $_ (¯≻ ✦ ≺¯)
_____(_.^._) (¯`.´¯)_(_.^._)
__________(¯≻ ✦ ≺¯)
_____(¯`.´¯) (_.^._) (¯`.´¯)
___ (¯≻ ✦ ≺¯) ____(¯≻ ✦ ≺¯)
_____(_.^._) ______ (_.^._)

Welcome to the Love Game!!
Your mission is to find love be forever with him!! Make your choices wisely because at any point you could lose him forever!
You are at the school, and two boys named "Ekansh" and "Priyam" ask you for a date. Whom would you choose?
Priyam
You chose priyam! Love grows to 25%. You went for a date with him! 
The waiter comes and asks you for what you would drink! You have two options - "Cocktails" and "Mocktails". What would you choose?
mocktails
You chose mocktails! and coincidently priyam loves mocktails too!! Love grows to 50%!
You both decide to go on a vacation during the summer break! Priyam asks you where do you want to go? He gives you three options - "Snowy Hills" , "Desert" , "Beach". What would you choose?
snowy hills
You chose to go to the Snowy Hills for vacation and for Priyam it is his favourite place to go on summer holidays! Love grows to 75%
After 5 years of dating, one day you are approached by a very rich and handsome guy who happens to be of your age! Would you go on a affair date with him? Answer in "Yes" or "No" 
no
You are loyal to Priyam and your relationship! Love grows to 100%
Priyam proposes you in a very scenic location and gave you the biggest surprise of your life! Will you say "Yes" or "No"? 
yes
You said YES and you get married to Priyam who treats you like a qween and you both live your happiest life!

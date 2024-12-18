input ("Welcome to Rainbow Six Siege today we will be testing if you are a attacker or a defender press enter to continue")

defense_points = 0
attack_points = 0

answer = input("do you like playing A( play more slow, or B) play more fast?\n")
if answer == "A":
    defense_points += 1
elif answer == "B":
    attack_points += 1

answer = input("do you like playing A( play with cooler gadgets, or B) play with more destructive gadgets?\n")
if answer == "A":
    defense_points += 1
elif answer == "B":
    attack_points += 1

answer = input("do you like playing A( use cameras , or B) use drones?\n")
if answer == "A":
    defense_points += 1
elif answer == "B":
    attack_points += 1

answer = input("do you like playing A( more heals, or B) more damage output?\n")
if answer == "A":
    defense_points += 1
elif answer == "B":
    attack_points += 1

answer = input("do you like playing A( weaker weapons and better gadgets, or B) better weapons but weaker gadgets?\n")
if answer == "A":
    defense_points += 1
elif answer == "B":
    attack_points += 1

if defense_points > attack_points :
    print("welcome to the defense")
elif attack_points > defense_points :
    print("welcome to the attack")
elif defense_points == attack_points :
    print("you are a one person army")

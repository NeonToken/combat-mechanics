import random
Character_Name = ("x")
Character_Weapon = ("x")
Character_XP = 0

print("Welcome to Combat Simulator")
print("----------------------------------------------------------------------------------------------------")
Character_Name = (input("What do you want to name your character?"))
print("Hello", Character_Name, "!")
print("---------------------------------------------------------------------------------------------------")
print("What do you want your weapon to be?")
print("Sword(1)")
print("Spear(2)")
print("Bow(3)")
print("Dagger(4)")
Character_Weapon = input("")
if Character_Weapon == ("1"):
    Character_Weapon = ("Sword")
elif Character_Weapon == ("2"):
    Character_Weapon = ("Spear")
elif Character_Weapon == ("3"):
    Character_Weapon = ("Bow")
elif Character_Weapon == ("4"):
    Character_Weapon = ("Dagger")
else:
    print("Incorrect Option, re-run the script")
print("----------------------------------------------------------------------------------------------------")


def First_level(Name, Weapon, XP):
    print("Welcome to the first level!{}".format(Name))
    print("You are practicing your {}".format(Weapon), "In athens, when suddenly your village is under attack!")
    print("----------------------------------------------------------------------------------------------------------")
    print("What do you decide to do?")
    print("Grab my {}".format(Weapon), "and prepare to defend the village!(1)")
    print("Run away to the nearby forest(2)")
    print("Hide in the village well(3)")
    print("BURN THE VILLAGE(4)")
    Choice_1 = input("")
    if Choice_1 == ("1"):
        print("You quickly grab your {}, As the village people cheer the name {}, you charge towards the invaders!".format(Weapon, Name))
        XP += 50
        Setting = ("Burning Village")
        Enemy = ("Barbarian")
        return (XP, Setting, Enemy)
    elif Choice_1 == ("2"):
        print("As you run into the forest, you see the village burning behind you, you have nothing but your trusty {}.".format(Weapon))
        XP += 25
        Setting = ("Dark Woods")
        Enemy = ("Goblin")
        return (XP, Setting, Enemy)
    elif Choice_1 == ("3"):
        print("You jump into the village well, Hoping to avoid the slaugher, But eventually you run out of breath and drown!")
        return ("YOU DIED")
    elif Choice_1 == ("4"):
        print("You go insane, burning your own village, even the invaders are confused and begin to wonder if you are on their side, nontheless they decide to kill you anyway.")
        return ("YOU DIED")
    else:
        print("Invalid choice, re-run the script.")

(Character_XP, Character_Setting, Character_Enemy) = (First_level(Character_Name, Character_Weapon, Character_XP))
print("---------------------------------------------------------------------------------------------------------------")
def combat_mechanics(name, weapon, setting, XP, enemy):
    print("As you advance into the {}".format(setting), "With your reliable {}".format(weapon), "You encounter a blood-hungry {}".format(enemy))
    print("What is your next move?")
    dmg = random.randint(10,100)
    hp = 100
    XP_gain = random.randint(1,50)
    XP = XP + XP_gain
    if dmg <= 25:
        dmg_message = ("Weak Attack")
    elif dmg <= 50:
        dmg_message =("Average Attack")
    elif dmg <= 75:
        dmg_message =("Powerfull Attack")
    elif dmg <= 100:
        dmg_message =("Decisive Attack")
    hp2 = (hp - dmg)

    print("Slash(1)")
    print("Punch(2)")
    print("Stab(3)")
    print("Smash(4)")
    attack_move = input("")
    if attack_move == ("1"):
        attack_move = ("Slash")
    elif attack_move == ("2"):
        attack_move = ("Punch")
    elif attack_move == ("3"):
        attack_move = ("Stab")
    elif attack_move == ("4"):
        attack_move = ("Smash")
        
        
    print("You grab your {} and proceed to {} the {}, You succesfully cause {} damage to your enemy!".format(weapon, attack_move, enemy, dmg))
    print("The {} now has a total of {} HP, That was a {}!".format(enemy, hp - dmg, dmg_message))
    print("You gained {} XP, you now have a total of {} XP".format(XP_gain, XP + XP_gain))
    if hp <= 0:
        loot_xp = random.randint(50,100)
        XP = XP + loot_xp
        return print("You have defeated the {} and gained {} XP, You now have a total of {} XP".format(enemy, loot_xp, XP))
    else:
        attacks = ["Slash", "Punch", "Stab", "Smash"]
        attack_move_enemy = random.choices(attacks)
        dmg_enemy = random.randint(10,100)
        hp_enemy = 150
        if dmg_enemy <= 25:
            dmg_message = ("Weak Attack")
        elif dmg_enemy <= 50:
            dmg_message =("Average Attack")
        elif dmg_enemy <= 75:
            dmg_message =("Powerfull Attack")
        elif dmg_enemy <= 100:
            dmg_message =("Decisive Attack")
        print("After recieving your hit, the enemy proceeds to {} you, causing {} damage, leaving you with {} and causing a {}".format(attack_move_enemy, dmg_enemy, hp_enemy - dmg_enemy, dmg_message))
        if hp_enemy - dmg_enemy <= 0:
            return print("You have been defeated by the {}".format(enemy))
        else:
        
            dmg = random.randint(10,100)
            hp3 = hp2 - dmg
            XP_gain = random.randint(1,50)
            XP = XP + XP_gain
            if dmg <= 25:
                dmg_message = ("Weak Attack")
            elif dmg <= 50:
                dmg_message =("Average Attack")
            elif dmg <= 75:
                dmg_message =("Powerfull Attack")
            elif dmg <= 100:
                dmg_message =("Decisive Attack")
            hp2 = (hp - dmg)
            
            print("Now you must choose your next attack!")
            print("Slash(1)")
            print("Punch(2)")
            print("Stab(3)")
            print("Smash(4)")
            attack_move2 = input("")

            if attack_move2 == ("1"):
                attack_move2 = ("Slash")
            elif attack_move2 == ("2"):
                attack_move2 = ("Punch")
            elif attack_move2 == ("3"):
                attack_move2 = ("Stab")
            elif attack_move2 == ("4"):
                attack_move2 = ("Smash")
            print("In your second attack, You grab your {} and proceed to {} the {}, You succesfully cause {} damage to your enemy!".format(weapon, attack_move2, enemy, dmg))
            print("The {} now has a total of {} HP, That was a {}!".format(enemy, hp2 - dmg, dmg_message))
            print("You gained {} XP, you now have a total of {}".format(XP_gain, XP + XP_gain))
            if hp2 - dmg <= 0:
                loot_xp = random.randint(50,100)
                XP = XP + loot_xp
                return print("You have defeated the {} and gained {}, You now have a total of {}".format(enemy, loot_xp, XP))
            else:
                attacks = ["Slash", "Punch", "Stab", "Smash"]
                attack_move_enemy = random.choices(attacks)
                dmg_enemy = random.randint(10,100)
                hp_enemy2 = hp_enemy - dmg_enemy
                if dmg_enemy <= 25:
                    dmg_message = ("Weak Attack")
                elif dmg_enemy <= 50:
                    dmg_message =("Average Attack")
                elif dmg_enemy <= 75:
                    dmg_message =("Powerfull Attack")
                elif dmg_enemy <= 100:
                    dmg_message =("Decisive Attack")
                print("After recieving your second hit, the enemy proceeds to {} you, causing {} damage, leaving you with {} and causing a {}".format(attack_move_enemy, dmg_enemy, hp_enemy2 - dmg_enemy, dmg_message))
                if hp_enemy2 - dmg_enemy <= 0:
                    return print("You have been defeated by the {}".format(enemy))
                else:
                    print("thats all folks")
                
            
combat_mechanics(Character_Name, Character_Weapon, Character_Setting, Character_XP, Character_Enemy)

Character_Enemy











    
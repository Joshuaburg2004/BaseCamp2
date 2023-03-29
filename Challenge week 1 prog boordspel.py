import os
import random
import time


player_dict = {}
buy_dict = {}


#rolls dice, for usage in other functions
def dice():
    print("Rolling..")
    time.sleep(1.5)
    r = random.randint(1, 6)
    return r


#gives players the option to buy some of the items required to win - a gps, sail, cleaner, sailor, pirate, steering wheel
def shop(player0, player1, player2, player3, player4, e):
    player_list = [player0, player1, player2, player3, player4]
    if player_list[3] is True:
        print("You enter the store and a loud voice says: ")
        time.sleep(1)
        print("\"Looking for something truly special? You've come to the right place. Let me show you what I have.\"")
        time.sleep(0.5)
        print("\"Lately I found a lot of ship components, I wonder who those belong to..\"")
        time.sleep(1)
        bought = False
        player = player_list[0]
        temp = buy_dict[player]
        money = player_list[2]
        print(f'You have {money} gold')
        while bought is True:
            if bought is False:
                return
            items = str(input("""
            A GPS --- 5 Gold
            SAIL --- 3 Gold
            CLEANER --- 4 Gold
            SAILOR --- 6 Gold
            PIRATE --- 5 Gold
            STEERING WHEEL --- 4 Gold
            Please copy the item name exactly!
            """))
            if money > 3:
                if items.lower() == "a gps":
                    if player_list[2] >= 5:
                        if 'gps' not in buy_dict[player]:
                            print("You got the GPS! A nifty tool for getting around!")
                            if player_list[0] in player_dict.values():
                                money = player_list[2] - 5
                                player_dict[e] = [player_list[0], player_list[1], money, player_list[3]]
                                temp.append('gps')
                                buy_dict[player] = temp
                                bought = False
                        else:
                            print("You already have this item.")
                    else:
                        print("You don't have enough gold for this item.")
                elif items.lower() == "sail":
                    if player_list[2] >= 3:
                        if 'sail' not in buy_dict[player]:
                            print("You got the sail! Very useful on a sailboat!")
                            if player_list[0] in player_dict.values():
                                money = player_list[2] - 3
                                player_dict[e] = [player_list[0], player_list[1], money, player_list[3]]
                                temp.append('sail')
                                buy_dict[player] = temp
                                bought = False
                        else:
                            print("You already have this item.")
                    else:
                        print("You don't have enough gold for this item.")
                elif items.lower() == "cleaner":
                    if player_list[2] >= 4:
                        if 'cleaner' not in buy_dict[player]:
                            print("You got the cleaner of your ship! Needed for getting your ship squeeky clean!")
                            if player_list[0] in player_dict.values():
                                money = player_list[2] - 4
                                player_dict[e] = [player_list[0], player_list[1], money, player_list[3]]
                                temp.append('cleaner')
                                buy_dict[player] = temp
                                bought = False
                        else:
                            print("You already have this item.")
                    else:
                        print("You don't have enough gold for this person.")
                elif items.lower() == "sailor":
                    if player_list[2] >= 6:
                        if 'sailor' not in buy_dict[player]:
                            print("You got the sailor of your ship! Needed for keeping your ship straight!")
                            if player_list[0] in player_dict.values():
                                money = player_list[2] - 6
                                player_dict[e] = [player_list[0], player_list[1], money, player_list[3]]
                                temp.append('sailor')
                                buy_dict[player] = temp
                                bought = False
                        else:
                            print("You already have this item.")
                    else:
                        print("You don't have enough gold for this person.")
                elif items.lower() == "pirate":
                    if player_list[2] >= 5:
                        if 'pirate' not in buy_dict[player]:
                            print("You got the pirate of your ship! Needed for stealing from the innocent!")
                            if player_list[0] in player_dict.values():
                                money = player_list[2] - 5
                                player_dict[e] = [player_list[0], player_list[1], money, player_list[3]]
                                temp.append('pirate')
                                buy_dict[player] = temp
                                bought = False
                        else:
                            print("You already have this item.")
                    else:
                        print("You don't have enough gold for this person.")
                elif items.lower() == "steering wheel":
                    if player_list[2] >= 3:
                        if 'steering wheel' not in buy_dict[player]:
                            print("You got the steering wheel! Quintessential to steer a boat!")
                            if player_list[0] in player_dict.values():
                                money = player_list[2] - 4
                                player_dict[e] = [player_list[0], player_list[1], money, player_list[3]]
                                temp.append('steering wheel')
                                buy_dict[player] = temp
                                bought = False
                        else:
                            print("You already have this item.")
                    else:
                        print("You don't have enough gold for this item.")
                else:
                    print('This item does not exist, please try again!')
            else:
                print('You do not have enough money, please come back later!')
                bought = False
    else:
        print("The shopkeeper speaks a language you can't quite place. Come back here when you have the translator.")


#keeps player in place until 2 of the same type are rolled.
def jail(player0, player1, player2, player3, player4, e):
    player_list = [player0, player1, player2, player3, player4]
    d = dice()
    f = dice()
    player_list[4] = True
    player_dict[e] = player_list
    if d != f:
        print(f"Oh no! {player_list[0]} failed to escape!")
    else:
        print('The Tribal Police (TBPD) went after you but you managed to escape!')
        player_list[4] = False
        player_dict[f] = player_list


#gives a random event which can give a lower gold requirement
def event(player0, player1, player2, player3, player4, e):
    player_list = [player0, player1, player2, player3, player4]
    rand = random.randint(1, 5)
    player = player_list[0]
    temp = buy_dict[player]
    if rand == 1:
        print("You find a small machine in the dirt.")
        time.sleep(0.5)
        if player_list[3] is True:
            print("Upon closer inspection, it seems like another version of your translator.")
            time.sleep(0.5)
            print("As you already have a working translator, you leave it in the dirt.")
        else:
            print("You realize it is a translator! This machine can translate native words to english.")
            time.sleep(0.5)
            print("You dig it out. You got the translator!")
            player_list[3] = True
            player_dict[e] = player_list
    if rand == 2:
        print("You see something shiny in a hill!")
        time.sleep(1)
        print("You dig it up and find 2 pieces of gold!")
        if player_list[0] in player_dict.values():
                money = player_list[2] + 2
                player_dict[e] = [player_list[0], player_list[1], money, player_list[3], player_list[4]]
    elif rand == 3:
        if 'steering wheel' not in buy_dict[player]:
            print("You find some twigs on the ground. After a bit of work, you manage to make a rough steering wheel!")
            time.sleep(0.5)
            print('You made a steering wheel!')
            if player_list[0] in player_dict.values():
                temp.append('steering wheel')
                buy_dict[player] = temp
        else:
            print("You find some useable twigs on the ground...")
            time.sleep(1)
            print("But as you have a steering wheel already it is of no use to you.")
    elif rand == 4:
        if 'cleaner' in buy_dict[player]:
            print('You find some rope tied around a tree, in a position to keep someone stuck.')
            time.sleep(0.5)
            print("While you ponder for a moment who could have been stuck here, you shrug it off and continue on your way.") 
        else:
            print('You hear screams in the distance..')
            time.sleep(2)
            print('Upon closer inspection, it seems like there is a cleaner tied to a tree!')
            time.sleep(0.5)
            print('You help the man off the tree, and he agrees to clean your ship when you escape!')
            time.sleep(0.5)
            print('You got the cleaner!')
            temp = buy_dict[player]
            temp.append('cleaner')
            buy_dict[player] = temp
    elif rand == 5:
        print('You see a group of what seem to be shamans circling a sailor!')
        if 'sailor' in buy_dict[player]:
            print('However much you wish to help this poor fellow, you already have a sailor waiting and ready.')
            time.sleep(0.5)
            print('You decide not to intervene, walking back towards the nearby trail.')
        else:
            print('You make a loud noise, scaring away the shamans and freeing the sailor.')
            temp = buy_dict[player]
            temp.append('sailor')
            buy_dict[player] = temp
            time.sleep(0.5)
            print('In exchange for your kind act, the sailor agrees to sail your ship.')
            time.sleep(0.5)
            print('You got the sailor!')


#gives a random question which gives gold or the translator
def queries(player0, player1, player2, player3, player4, e):
    player_list = [player0, player1, player2, player3, player4]
    ans_bool = False
    print("You come across a wandering tribal member.")
    time.sleep(1) #sleep(x) delays by x seconds.
    print("He tells you:\"I'm the wandering trader in this land and I give VERY special items.\"")
    time.sleep(1)
    print("BUT")
    time.sleep(1)
    print("\"you will need to answer my questions VERY correctly to get those special items of mine.. \"")
    time.sleep(1)
    print("I'll make it easy for you for now.")
    r = random.randint(1, 10)
    if r == 1:
        print("What's the first thing to do when lost on the island?\n")
        time.sleep(2)
        print("A) Panic and scream for help")
        print("B) Start building a shelter immediately")
        print("C) Look for sources of food and water")
        print("D) Wander aimlessly to try and find your way back home")
        ans_1 = input("Enter your answer: ")
        if ans_1.lower() == 'c':
            ans_bool = True
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 2:
        print("Which of the following is a way to signal for help if you're stranded on an island?\n")
        time.sleep(2)
        print("A. Yell for help")
        print("B. Use a flare gun")
        print("C. Build a sandcastle")
        print("D. Use social media")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "b":
            ans_bool = True
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 3:
        print("What should you do in a lightning storm on an island?\n")
        time.sleep(2)
        print("A) Stand under a tall tree")
        print("B) Stay on the beach")
        print("C) Go inside a cave or rock shelter")
        print("D) Swim in the water")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "c":
            ans_bool = True
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 4:
        print("How can you fully purify water on an island?\n")
        time.sleep(2)
        print("A) Boiling")
        print("B) Filtering")
        print("C) Chemical treatment")
        print("D) All of the above")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "a":
            ans_bool = True
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 5:
        print("What are some ways to keep warm on an island?\n")
        time.sleep(2)
        print("A) Wear warm clothing")
        print("B) Huddle with other people")
        print("C) Build a fire")
        print("D) All of the above")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "a":
            ans_bool = True
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 6:
        print("What should you do if you encounter a bear on an island?\n")
        time.sleep(2)
        print("A) Run away as fast as possible")
        print("B) Stay completely still and pretend to be dead")
        print("C) Make loud noises and try to scare the bear away")
        print("D) Slowly back away while speaking softly to the bear")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "b" or ans_2.lower() == "d":
            ans_bool = True
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 7:
        print("There could be predators on the island - what should you do to protect yourself?\n")
        time.sleep(2)
        print("A) Dig a hole and hide in it")
        print("B) Make a spear out of a stick")
        print("C) Paint yourself camouflage colors with mud")
        print("D) Start howling - now the predators are scared of YOU")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "b":
            ans_bool = True 
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 8:
        print("What would be the best place for shelter?\n")
        time.sleep(2)
        print("A) Near a water source")
        print("B) A and C")
        print("C) On top of a tree")
        print("D) Where you can easily be seen by boats and planes")
        print("E) A and D")
        print("F) C and E")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "e":
            ans_bool = True
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 9:
        print("Some insects are safe to eat. If you eat them, you will get...\n")
        time.sleep(2)
        print("A) a lot of protein")
        print("B) a lot of vitamins")
        print("C) a lot of fats")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "a":
            ans_bool = True 
            print("That's correct!")
        else:
            print("That's incorrect!")
    elif r == 10:
        print("If you need food, which is the safest food to eat?\n")
        time.sleep(2)
        print("A) Hairy or brightly-coloured insects")
        print("B) Worms")
        print("C) Mushrooms")
        print("D) Wild berries")
        ans_2 = input("Enter your answer: ")
        if ans_2.lower() == "c":
            ans_bool = True 
            print("That's correct!")
        else:
            print("That's incorrect!")
    if ans_bool is True:
        translator = player_list[3]
        if translator is True:
            money = player_list[2]
            bonus = random.randint(1, 4)
            money += bonus
            print(f'You got {bonus}! You now have {money}G')
            player_dict[e] = [player_list[0], player_list[1], money, player_list[3], player_list[4]]
        if translator is False:
            player_list[3] = True
            player_dict[e] = player_list
            print('The trader gives you a translator!')
            

#backbone above code
def main():
    b = True
    while b is True:
        for i in range(1, len(player_dict.values()) + 1):
            player = player_dict[i]
            input(f"It is {player[0]}'s turn!")
            if player[4] is False:
                die = dice() + dice()
                player_pos = (player[1] + die) % 40
                input(f"They move {die} spaces to {player_pos}.")
                player_dict[i] = [player[0], player_pos, player[2], player[3], player[4]]
                player[1] = player_pos
                query = [4, 14, 19, 23, 28, 32, 35, 38]
                events = [1, 6, 12, 17, 26, 33]
                shop_pos = [11, 18, 29, 37]
                jail_pos = [20]
                if player_pos in query:
                    queries(player[0], player[1], player[2], player[3], player[4], i)
                if player_pos in events:
                    event(player[0], player[1], player[2], player[3], player[4], i)
                if player_pos in jail_pos:
                    input('You have been caught by the Tribal Police, you are now stuck until you escape')
                    player[4] = True
                    jail(player[0], player[1], player[2], player[3], player[4], i)
                if player_pos in shop_pos:
                    shop(player[0], player[1], player[2], player[3], player[4], i)
                if len(buy_dict[player[0]]) == 6:
                    print(f'{player[0]} has collected all pieces of their ship and has gathered a crew.')
                    time.sleep(1)
                    print('Now standing on the deck, they bid goodbye to the island they thoroughly explored.')
                    time.sleep(1)
                    print(f'{player[0]} WINS!')
                    print(buy_dict[player[0]])
                    b = False
            else:
                jail(player[0], player[1], player[2], player[3], player[4], i)
    print(f'{player[0]} has collected all pieces of their ship and has gathered a crew.')
    time.sleep(1)
    print('Now standing on the deck, they bid goodbye to the island they thoroughly explored.')
    time.sleep(1)
    print(f'{player[0]} WINS!')


#gives name and initiates dicts and lists
def start():
    n = 0
    inputter = True
    player_count = int(input("How many players are you playing with?\n"))
    while inputter is True:
        n += 1
        name = input("Please give your name: ")
        if name == '':
            n -= 1
            continue
#[name, position on the board, money]
        player_dict[n] = [name, 0, 0, False, False]
        buy_dict[name] = []
        if n == player_count:
            inputter = False
            return


if __name__ == "__main__":
    start()
    main()
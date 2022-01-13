#!/usr/bin/env python3
#shebang line has to be the very first line

#Basic story, Decision Tree, Finalize story at each decision, code the logic with functions and if/elif, add time delay effect for text

# ''' Patricks RPG game'''

# Ask the users name so that the statement returned welcomes them to the game
              
name = input("Type your name: ")


print('Welcome', name, 'to the Underworld!')

answer = input('You have passed thorugh a portal, when you exit the portal there are two directions you can take, left toward a bridge or right down a dirt path. Both directions meet on the far side of the bridge. Please choose left or right? '  ).lower()

if answer == 'left':
    answer = input("On the bridge you are confronted by rock troll with a battle club. He is massive but slow! Type fight to fight or run to bypass:  ")

if answer == "fight":
    print("You fought the troll but the bridge was damaged in the fight, so you and the troll fall to your death")
    
elif answer == "run":
        print("You avoided the troll and crossed the bridge, the troll tried to strike you but damaged the bridge and fell to his death. The bridge is no longer accessabile")

elif answer == 'right':
    answer = input("As you are walking down the path you hear rustling in the bushes and a wereworlf jumps out to confront you! What do you do? Type fight to fight or run to run" )

if answer == "fight":
    print("You choose to fight with no silver....you are torn to shreds, game over!")
elif answer == "run":
    print("You attempt to run from the wereworlf, he chases you down and tears you to shreds")
else: 
    print('Not a valid option. You perish') 
        

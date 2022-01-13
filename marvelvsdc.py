#!/usr/bin/env python3

#Introduction to game
print('Welcome to Marvel vs DC')
answer=input('Are you ready to play? (yes/no) :')
score=0
total_questions=5

#If the player states yes then proceed to game
if answer.lower()=='yes':
    answer=input('Question 1: Which superhero world does Wolverine live?')
    if answer.lower()=='marvel':
        score += 1
        print('Correct, heal all wounds')
    else:
        print('Wrong, stuck in stasis')
        score -= 1

    answer=input('Question 2: What is Supermans weakness?') 
    if answer.lower()=='kryptonite':
        score += 1
        print('Correct, gain power like the yellow sun!')
    else:
        print('Wrong, red sun drain life strength')
        score -= 1

    answer=input('Question 3: What color fur on Beast?')
    if answer.lower()=='blue':
        score += 1
        print('Correct, intellegence increase')
    else:
        print('Wrong, your body turns blue')
        score -= 1

    answer=input('Question 4: What is Batmans real name?')
    if answer.lower()=='bruce wayne':
            score += 1
            print('Correct, currency increase')
    else:
        print('Wrong, currency depleted')
        score -= 1

    answer=input('Question 5: What world does Deathstroke belong to?')
    if answer.lower()=='dc':
        score += 1
        print('Correct, promoted to Assassin')
    else:
        print('Wrong, you are assassinated')
        score -= 1

    print('Thank you for Playing Marvel vs DC, you attempted', score, "questions correctly!")
    mark=(score/total_questions)*100
    print('Marks obtained:',mark)
    print('Bye for now!')

    

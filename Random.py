import random
secretNimber=str(random.randint(1,20))
print('I am thinking a number between 1 and 20')
for guesses in range(10):
    print("Take a guess")
    guess=input()
    if guess<secretNimber:
        print("Your guess is too low")
    elif guess>secretNimber:
        print("Too high value")
    else:
        break
if guess==secretNimber:
    print("Good Job,you are made")
else:
    print("It was "+str(secretNimber))

import random
target=random.randint(1,100)
while True:
    userNo=int(input("Enter the no : "))
    if(userNo== target):
        print("You guessed the correct...")
        break
    elif(userNo < target):
        print("You guessed the less...")
    else:
        print("You guessed the more...")
print("======Won the game=====")
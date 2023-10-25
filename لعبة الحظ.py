from random import randint
computer_number =randint(0,100)
print('computer choose number between 0 and 100')
print('Allow 5 attempts to know number')
attempts = 0
length_number = len(str(computer_number))
print(f'Number is {length_number} digits')
while attempts < 5 :
    user_number=int(input('Enter number between 0 and 100 : '))
    attempts +=1
    if attempts == 5:
        print('Game Over')
        break
    else:
        if user_number < computer_number:
            print('Try again ,choose greater number')
        elif user_number > computer_number:
            print('Try again ,choose lower number')
        else:
            print(f'you own after {attempts} attempts')
            break
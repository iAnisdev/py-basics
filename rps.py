from random import choice

choices = ['rock', 'paper', 'scissors']

computer = choice(choices)

player = None

while player not in choices:
    player = input('rock, paper or scissors? ').lower()

print('You:', player.title())
print('Computer:', computer.title())

if player == computer:
    print('Draw!')
elif player == 'rock' and computer == 'scissors':
    print('You win!')
elif player == 'paper' and computer == 'rock':
    print('You win!')
elif player == 'scissors' and computer == 'paper':
    print('You win!')
else:
    print('Draw!')
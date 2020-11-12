import time

import random
import secrets

print('### WELCOME TO SPIN THE BOTTLE GAME ###')
time.sleep(3)
for i in range(1,2):
    print('\n')
d=int(input('Enter the number of players (>=2): '))
player=[]
for i in range(1,d+1):
    print('Name of Player',i)
    p=input()
    player.append(p)
print('Players are',player)
print('\n')
print('### BOTTLE IS SPINNING ###\n')

time.sleep(3)
heads=secrets.choice(player)

tails=secrets.choice(player)
print('### BOTTLE HEADS TOWARDS  ###\n',heads)
if heads!=tails:
    print('### BOTTLE TAILS TOWARDS  ###\n',tails)
else:
    print('###BOTTLE TAILS TOWARDS ###',tails)
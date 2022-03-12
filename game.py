import random
from tkinter import N

options=['Rock','Paper','Scissor']
scores={'user':0 ,'computer':0}
n=int(input('chand dast mikhay bazi koni:'))

for i in range(n):
    com_choice = random.choice(options)
    us_choice = input('Rock \n Paper \n Scissor \n play game: ')

    if us_choice== 'Rock': 
        if com_choice=='Paper' :
            scores['computer']+=1
            print('computer won!')
        elif com_choice=='Rock':
            print('mosavi')
        elif com_choice=='Scissor':
            scores['user']+=1
            print('you won!')

    elif us_choice=='Paper':
        if com_choice=='Scissor' :
            scores['computer']+=1
            print('computer won!')
        elif com_choice=='Paper':
            print('mosavi')
        elif com_choice=='Rock':
            scores['user']+=1
            print('you won!')

    elif us_choice=='Scissor':
        if com_choice=='Scissor':
            print('mosavi')
        elif com_choice=='Paper':
            scores['user']+=1
            print('you won!')
        elif com_choice=='Rock':
            scores['computer']+=1
            print('computer won!')                

print('End of game')
if scores['computer'] > scores['user']:
    print('Game over :( ')
elif scores['computer'] < scores['user']:
    print('You won finally :)')    
elif scores['computer'] == scores['user']:
    print('Tie game ')
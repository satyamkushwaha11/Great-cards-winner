import random
import json
from time import sleep

#list of all card
cards=[]
gen=['Ace',2,3,4,5,6,7,8,9,10,'Joker','Queen','King']
card_type=['spades','heart','dimond','club']
for i in card_type :
	for j in gen :
		cards.append(list((i,j)))
player=['player1','player2','player3','player4']
#print(cards)

#each player get 4 unique cards
suffle={}
for i in player:
	card_get=[]
	for j in range(4):
		c=random.choice(cards)
		card_get.append(c)
		cards.remove(c)
	suffle[i]=card_get
	
#giving the value to face card  and their sum

sum ={}
for j in player:
	sleep(2)
	add=0
	a=suffle.get(j)
	print('---------',j,'----------------\n',flush= True)
	for i in a: 
		sleep(0.5)
		if i[1]=='King':
			b=13
		elif i[1]=='Joker':
			b=11
		elif i[1]=='Ace':
			b=1
		elif i[1]=='Queen':
			b=12
		else:
			b=i[1]
		s1=15-len(i[0]+str(i[1]))
		
		print(i[1],"of ",i[0],' '*s1,b,flush=True)
		add+=b
	print()
	print(f'    Total    ---->   {add} ')
	sum[j]=add
	print()

print('----------------------')

print()

for i in range(35):
    sleep(0.08)
    print("#", end = '', flush=True)
print()

# sleep(2)

# find greater
p1,p2,p3,p4=sum['player1'],sum['player2'],sum['player3'],sum['player4']

l=[p1,p2,p3,p4]
l.sort()
greater=l[-1]
for i in player:
	if sum[i]==greater :
		print(i,' is winner.')


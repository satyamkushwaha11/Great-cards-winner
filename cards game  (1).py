import random

#list of all card
cards=[]
gen=['Ace',2,3,4,5,6,7,8,9,10,'Joker','Queen','King']
card_type=['spades','heart','dimond','club']
for i in card_type :
	for j in gen :
		cards.append(list((i,j)))
player=['player1','player2','player3','player4']
#print(cards)

#each player get 4 cards
suffle={}
for i in player:
	card_get=[]
	for j in range(4):
		c=random.choice(cards)
		card_get.append(c)
		cards.remove(c)
	suffle[i]=card_get

for i in suffle.items():
	print(i)
	print()
	
#giving the value to face card  and their sum

sum ={}
for j in player:
	add=0
	a=suffle.get(j)
	print(j)
	for i in a: 
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
		print(i,'  ',b)
		add+=b
	sum[j]=add
	print()

print()

import json
print(json.dumps(sum,indent=5+2))


# find greater
p1,p2,p3,p4=sum['player1'],sum['player2'],sum['player3'],sum['player4']

l=[p1,p2,p3,p4]
l.sort()
greater=l[-1]
for i in player:
	if sum[i]==greater :
		print(i,' is winner.')

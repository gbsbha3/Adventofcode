resp_one = { 'X':'Rock','Y':'Paper','Z':'Scissors'}
resp_two = { 'A':'Rock','B':'Paper','C':'Scissors'}
d = { 'R' : 'P' , 'P' : 'S' , 'S' : 'R'}


file = [ i.strip() for i in open('input.txt')]


count = 0
for i in file:
	i = i.strip()
	a,b = i.split()
	
	count += {'X':1,'Y':2,'Z':3}[b]
	print(count)
	# count += {('A','X'):3,('A','Y'):6,('A','Z'):0,
	# 		('B','X'):0,('B','Y'):3,('B','Z'):6,
	# 		('C','X'):6,('C','Y'):0,('C','Z'):3}[(a,b)]
	# count += {'X':0,'Y':3,'Z':6}[b]
	# count += {('A','X'):3,('A','Y'):1,('A','Z'):2,
	# 		('B','X'):1,('B','Y'):2,('B','Z'):3,
	# 		('C','X'):2,('C','Y'):3,('C','Z'):1}[(a,b)]



# print(count)






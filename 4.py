file = [ i.strip() for i in open('input.txt')]

count = 0
second = 0
for i in file:
	a,b = i.split(',')
	a1,a2 = a.split('-')
	b1,b2 = b.split('-')
	a1,a2,b1,b2 = [ int(i) for i in [a1,a2,b1,b2]]
	if a1<=b1 and b2<=a2 or b1<=a1 and a2<=b2:
		count += 1
	if not (a2 < b1 or b2 < a1):
		second +=1

print(count)
print(second)

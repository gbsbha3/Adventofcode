import string

file = [ i.strip() for i in open('input.txt')]
priority = list(string.ascii_letters)
rankings = []
for i in file:
	length = len(i)
	first = i[:int(len(i)/2)]
	second = i[int(len(i)/2):]
	common_characters = ''.join(set(first).intersection(second))
	rankings.append(priority.index(common_characters)+1)

print(sum(rankings))

badges = []
counts = []
count = 0
chunks = [file[x:x+3] for x in range(0, len(file),3)]
for i in chunks:
	common = ''.join(set.intersection(*map(set,i)))
	badges.append(priority.index(common)+1)

print(sum(badges))







	









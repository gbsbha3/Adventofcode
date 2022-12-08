

# file = open("input.txt")
# total_calories = []
# count = 0
# for line in file:
# 	line = line.strip()
# 	for l in line.split('\n'):
# 		print(l)
# 		count += int(l)
# 	total_calories.append(count)


# print(total_calories)





cal = [ i.strip() for i in open("input.txt")]

out = []
for i in ('\n'.join(cal).split('\n\n')):
	count = 0
	for j in i.split('\n'):
		count += int(j)
	out.append(count)


print(sum(sorted(out,reverse=True)[:3]))






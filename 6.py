signal = [ i.strip() for i in open('input.txt')]
string = ""
for i in signal:
	string+=i


list_string = list(string)
groupedchars = [ list_string[i:i+4] for i in range(len(list_string[:-3]))]



ogroup = []
for group in groupedchars:
	if len(group) == len(set(group)):
		ogroup.append(group)

temp = ""
for i in ogroup[0]:
	temp +=i

print(int(string.index(temp))+4)




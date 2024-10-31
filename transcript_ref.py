import re
mydict = {}

file_list = ['IN1001/IN1001.A.words.txt','IN1001/IN1001.B.words.txt','IN1001/IN1001.C.words.txt','IN1001/IN1001.D.words.txt']
speakers = ['SPEAKER_00','SPEAKER_02','SPEAKER_03','SPEAKER_04']

for n in range(len(file_list)):

	file = open(file_list[n], 'r')
	lines = file.readlines()

	for i in lines:
		i = i.split()
		if len(i) != 0 and i[0] == '<w' and len(i) == 4:
			poi = i[3]
			num = poi[poi.find('\"')+1:]
			num = num[:num.find('\"')]
			key = float(num)		
			value = poi[poi.find('>')+1:poi.find('<')]	
			value = speakers[n]+':'+value
			mydict[key] = value
		file.close()

mydict_sort = sorted(mydict)

insert_lines = []

for i in mydict_sort:
	first = mydict[i].split(':')[0]
	break

input_str = first+":"
for i in mydict_sort:
	spl = mydict[i].split(':')
	if spl[0] == first:
		input_str += " " + spl[1]
	else:
		first = spl[0]
		insert_lines.append(input_str + ".\n")
		input_str = first+":"+spl[1]

split_parameter = 4  
i = 0  
j = 0
while i != len(insert_lines)-3:
	a = re.split('\.|\:',insert_lines[i])
	b = re.split('\.|\:',insert_lines[i+2])
	if a[0] == b[0]:		
		if len(a[1].split(' ')) <= split_parameter and len(b[1].split(' ')) <= split_parameter:
			insert_lines[i] = a[0] + ':' + a[1] + ' ' + b[1] + '.\n'
			del insert_lines[i+2]
	i+=1
	
	a = re.split('\.|\:',insert_lines[j])
	b = re.split('\.|\:',insert_lines[j+1])
	if a[0] == b[0]:
		if len(a[1].split(' ')) <= split_parameter and len(b[1].split(' ')) <= split_parameter:
			insert_lines[i] = a[0] + ':' + a[1] + ' ' + b[1] + '.\n'
			del insert_lines[j+1]
	j+=1
	
	
file = open("INI1001.txt","w")
file.writelines(insert_lines)
file.close()
print("Transcription done!")
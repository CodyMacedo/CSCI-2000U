

def has_no_e(a_string):
	is_there_e = a_string.find('e')
	if is_there_e == -1:
		return True
	else:
		return False
	
	
	
reader = open('gadsby_stripped.txt','r')
data = reader.readline()
count = 0

while data != '':
	if has_no_e(data) == False:
		print("Line ", count, "contains an 'e'")
	data = reader.readline()
	count += 1
	
reader.close()

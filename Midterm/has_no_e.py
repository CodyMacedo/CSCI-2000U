


def _no_e(a_string):
	is_there_e = a_string.find('e')
	if is_there_e == -1:
		return false
	else:
		return true
	
	
	
reader = open('gadsby_stripped.txt','r')
data = reader.readline()

while data != '':
	_no_e(data)
	data = reader.readline()
	
reader.close()


def which_is_smaller(x,y):
	return min(x,y)

def lowercase(x):
	if x in ['a', 'e', 'i', 'o', 'u']:
		return True
	else:
		return False

def count_len_words(my_list):
	number_char = []
	for word in my_list:
		number_char.append(len(word))
	return number_char

def beer_on_the_wall(number):
	while number > 0:
		print(f'{number} bottles of beer on the wall, {number} bottles of beer on the wall, if one of them just happens to fall, {number-1} bottles of beer on the wall')
		number = number - 1

a = which_is_smaller(3,4)
b = lowercase('e')
c = count_len_words(['boy', 'child', 'tractor', 'monster'])

print(a,b,c)
#beer_on_the_wall(99)

import random
import array
MAX_LEN = 12
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
low= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

up= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
total= numbers+ up + low + SYMBOLS
rand_digit = random.choice(numbers)
rand_upper = random.choice(up)
rand_lower = random.choice(low)
rand_symbol = random.choice(SYMBOLS)
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(total)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
		password = password + x
print(password)

#!usr/bin.python3.6

import pyperclip


matches = []
print('Historty :')
while True:
	if pyperclip.paste() not in matches:
		text = str(pyperclip.paste())
		matches.append(text)
		print('\n')
		print(len(matches),pyperclip.paste())
		

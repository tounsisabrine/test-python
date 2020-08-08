import re
#def text_match(text):
text_match=input('enter a string: ')
patterns = 'ab*?'
if re.search(patterns,  text_match):
   print('Found a match!')
else:
   print('Not matched!')

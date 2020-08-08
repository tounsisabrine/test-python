import re
text_match= input()
patterns = 'a.*?b$'
if re.search(patterns,  text_match):
    print ('Found a match!')
else:
    print('Not matched!')

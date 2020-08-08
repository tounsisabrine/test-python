import re
text_match=input()
patterns = '^[a-z]+_[a-z]+$'
  if not re.search(patterns, text_match):
    print ('Found a match!')
  else:
    print('Not matched!')

import re
text = input('enter a sentence: ')
print(re.split('; |, |\*|\n',text))

import re, datetime
s = "I have a meeting on 19/09/2020 in New York"
match = re.search('\d{2}/\d{2}/\d{4}', s)
#date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
date = datetime.datetime.strptime(match.group(), '%d/%m/%Y').date()
print (date)

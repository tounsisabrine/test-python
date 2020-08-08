import re
text = "lately i've been losing sleep"
for m in re.finditer(r"\w+ly", text):
    print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

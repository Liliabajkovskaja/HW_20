import re


# ? +, *, {}, [], /d, /w

#   - findall
#   - sub
#   - split
#   - match/fullmatch
with open(r'F:\Tests_0324\lessons\lesson_20\test_html.html') as f:
    data = f.read()

# name + phone

print('findall', re.findall(r' \d{4}', data))
print('findall', re.findall(r'\s[A-Z]{1}[a-z]+\s[A-Z]{1}[a-z]+.+\+\d{10}', data))
fa = re.findall(r'(([A-Z]{1}[a-z]+\s){2}.+\+\d{10})', data)
print('findall', [k[0] for k in fa])

match = re.match(r'.+\w{4}', data)
matchs = re.fullmatch(r'^.+\w$', data)

print('findall', re.findall(r'peter\w*\W?\w*@\w+\.\w{2,3}', data))

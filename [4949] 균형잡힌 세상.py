import re
q = re.compile('[(]|[)]|\[|\]')

while True:
    string = input()
    
    if string == '.':
        break
    
    string = ''.join(q.findall(string))

    for _ in range(50):
        string = string.replace('()','')
        string = string.replace('[]','')

    if not string:
        print('yes')
    else:
        print('no')

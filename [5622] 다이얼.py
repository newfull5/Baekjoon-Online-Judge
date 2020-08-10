def f(a):
    if a in ['A','B','C']:
        return 2
    if a in ['D','E','F']:
        return 3
    if a in ['G','H','I']:
        return 4
    if a in ['J','K','L']:
        return 5
    if a in ['M','N','O']:
        return 6
    if a in ['P','Q','R','S']:
        return 7
    if a in ['T','U','V']:
        return 8
    if a in ['W','X','Y','Z']:
        return 9

print(sum(map(lambda x: f(x)+1, list(input()))))

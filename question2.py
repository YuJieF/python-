while True:
    a = input()
    c = []
    b = [''] * len(a)
    for i in range(len(a)):
        if a[i] == '(':
            c.append(i)
            b[i] = ' '
        elif a[i] == ')':
            if c:  
                b[i] = ' '
                c.pop()
            else:
                b[i] = '?' 
        else:
            b[i] = ' '
    while c: 
        b[c[-1]] = 'X'
        c.pop()
    print(''.join(b))

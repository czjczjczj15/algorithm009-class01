if n <=2:
    return n
f, s = 1,2
for _ in range(n-2):
    t = f + s
    f = s
    s = t
return t
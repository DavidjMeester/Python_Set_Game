def is_set(a,b,c):
    zippie = zip(a,b,c)
    z = tuple(zippie)
    for x in range(4):
        if z[x][0] == z[x][1] != z[x][2] or z[x][0] == z[x][2] != z[x][1] or z[x][1] == z[x][2] != z[x][0]:
            return False
    return True

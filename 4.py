a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

pocet = 0
rule1 = False
rule2 = False
group1 = []
group2 = []
group = []
vylouceny = []


for i in range(356261, 846304):
    numstr = str(i)
    a = int(numstr[0:1])
    b = int(numstr[1:2])
    c = int(numstr[2:3])
    d = int(numstr[3:4])
    e = int(numstr[4:5])
    f = int(numstr[5:6])

    heslo = [a, b, c, d, e, f]

  #  print(heslo)

    for p in enumerate(heslo):
        if a == b or b == c or c == d or d == e or e == f:
            rule1 = True
            # if a == b:
            #     double = a
            # elif b == c:
            #     double = c
            # elif c == d:
        #print(j[0])
        # if p[0] < 5:
        #     if heslo[p[0]] == heslo[p[0]+1]:
        #         rule1 = True

    for j in enumerate(heslo):

        if j[0] < 4:
            if heslo[j[0]] == heslo[j[0] + 1] == heslo[j[0] + 2]:
                for x in enumerate(heslo):
                    if x[0] < 5:
                        if heslo[x[0]] == heslo[x[0]+1] and heslo[x[0]] != heslo[j[0]]:
                            #print(heslo[x[0]], heslo[x[0]+1], j[0])

                            group1.append(i)
                        if heslo[x[0]] == heslo[x[0] + 1] and heslo[x[0]] == heslo[j[0]]:
                            rule1 = False

    for r in enumerate(heslo):
        if r[0] < 3:
            if heslo[r[0]] == heslo[r[0] + 1] == heslo[r[0] + 2] == heslo[r[0] + 3]:
                for s in enumerate(heslo):
                    if s[0] < 5:
                        if heslo[s[0]] == heslo[s[0]+1] and heslo[s[0]] != heslo[r[0]]:
                            #print(heslo[x[0]], heslo[x[0]+1], j[0])
                            group2.append(i)
                        if heslo[s[0]] == heslo[s[0] + 1] and heslo[s[0]] == heslo[r[0]]:
                            rule1 = False

    for g in enumerate(heslo):
        if g[0] < 3:
            if heslo[g[0]] == heslo[g[0] + 1] == heslo[g[0] + 2] == heslo[g[0] + 3]:
                for h in enumerate(heslo):
                    if h[0] < 3:
                        if heslo[h[0]] == heslo[h[0]+1] == heslo[h[0]+2] and heslo[h[0]] != heslo[g[0]]:
                            #print(heslo[x[0]], heslo[x[0]+1], j[0])
                            group2.append(i)
                        if heslo[h[0]] == heslo[h[0] + 1] == heslo[h[0]+2] and heslo[h[0]] == heslo[g[0]]:
                            rule1 = False

    # if a == b or b == c or c == d or d == e or e == f:
    #     rule1 = True
    #     # if a == b:
    #     #     double = a
    #     # elif b == c:
    #     #     double = c
    #     # elif c == d:
    # else:
    #     rule1 = False

    if a <= b and b <= c and c <= d and d <= e and e <= f:
        rule2 = True
    else:
        rule2 = False


    if rule1 and rule2:
        group.append(i)
        pocet += 1
    if not rule1 and rule2:
        vylouceny.append(i)


print(pocet)
print(group)
print(vylouceny)
#print(group2)
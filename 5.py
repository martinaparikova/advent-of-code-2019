values = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]
#values = [1,9,10,3,2,3,11,0,99,30,40,50]
#values=[1,0,0,0,99]
#values = [1,95,7,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]

#values =


def myfunc(values):
    #for i in range(0, 10000):#range(0, len(values), 4):
    i = 0
    while i < 10000:
        if values[i] in (1, 2):
            if values[i] == 1:
                values[values[i + 3]] = values[values[i + 1]] + values[values[i + 2]]
            elif values[i] == 2:
                values[values[i + 3]] = values[values[i + 1]] * values[values[i + 2]]
            print(values[i])
            posunseo = 4
        elif values[i] in (3, 4):
            if values[i] == 3:
                values[values[i]] = values[i]
            elif values[i] == 4:
                values[values[i]] = values[i + 1]
            posunseo = 1
        elif values[i] == 99:
            break
        i = i + posunseo
    return values[0]

res = myfunc(values)
print(res)
def myfunc2(values):
    for i in range(0, len(values), 4):
        if values[i] == 1:
            values[values[i + 3]] = values[values[i + 1]] + values[values[i + 2]]
        elif values[i] == 2:
            values[values[i + 3]] = values[values[i + 1]] * values[values[i + 2]]
    return values[0]


# mylist = []
# for j in range(0,100):
#     for k in range(0,100):
#         mylist.append([j, k])
#         k += 1
#     j += 1
#
# print(mylist)
#
# for i in mylist:
#     vals =  [1,i[0],i[1],3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0]
#     res = myfunc2(vals)
#     if res == 19690720:
#         answer = i[0] * 100 + i[1]
#         print("ANSWER: " + str(answer))
#         # print("result: " + str(res))
#         # print("noun: " + str(i[0]))
#         # print("verb: " + str(i[1]))





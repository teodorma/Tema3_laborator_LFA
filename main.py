def partitionStates(list,aux):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if transitionReturn(list[i],list[j],p0):
                if aux == []:
                    aux.append([list[i],list[j]])
                elif [list[j]] not in aux:
                    for k in aux:
                        if transitionReturn(k[0],list[j],p0) and list[j] not in k:
                            k.append(list[j])
                            break
            else:
                if aux == []:
                    aux.append([list[i]])
                    aux.append([list[j]])
                elif [list[j]] not in aux:
                    for k in aux:
                        if transitionReturn(k[0],list[j],p0) and list[j] not in k:
                            k.append(list[j])
                            break
                    else:
                        aux.append([list[j]])
        break

def transitionReturn(state1,state2,p0):
    aux1 = []
    aux2 = []
    sem = 0
    for i in l:
        if state1 == i[0]:
            aux1.append((i[1],i[2]))
        if state2 == i[0]:
            aux2.append((i[1],i[2]))
    if len(aux1) == len(aux2):
        for i in range(len(aux1)):
            for j in p0:
                if (aux1[i][1] in j and aux2[i][1] in j) and aux1[i][0] == aux2[i][0]:
                    sem += 1
                    break
    if sem == len(aux1):
        return True
    else:
        return False

f = open('inputtt.txt',"r")
l = [[x for x in line.split()] for line in f]
f.close()

finalStates = l[len(l)-1]
l.pop()

reachableStates = [l[0][0]]
for i in l:
    if i[0] in reachableStates and i[2] not in reachableStates:
        reachableStates.append(i[2])

p0 = [[x for x in reachableStates if x not in finalStates],[x for x in reachableStates if x in finalStates]]
pk = []
while pk != p0:
    if pk != []:
        p0 = pk
    pk = []
    for i in p0:
        aux = []
        if len(i) > 1:
            partitionStates(i,aux)
        else:
            pk.append(i)
        for j in aux:
            pk.append(j)

minimizedDFA = []
copy_l = l
print(copy_l)
for i in pk:
    for j in range(len(copy_l)):
        if copy_l[j][0] == i[0]:
            minimizedDFA.append(l[j])
            if transitionReturn(copy_l[j][2],copy_l[j][0],pk):
                copy_l[j][2] = copy_l[j][0]

minimizedDFA.sort(key=lambda x:x[0])
finalStates = [x for x in finalStates for i in minimizedDFA if x==i[0]]
finalStates = [*set(finalStates)]
minimizedDFA.append(finalStates)

print(pk)
for i in minimizedDFA:
    print(*i)

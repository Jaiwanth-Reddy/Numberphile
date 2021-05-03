import matplotlib.pyplot as p

start = int(input('what do you want the starting element to be?\n'.title()))

current = [start,0]

size = int(input('how many terms do you want\n'.title()))

for i in range(0,size - 2):
    out = 0
    l = len(current)
    last = current[-1]                

    for i in range(l - 2,-1,-1):
        if current[i] == last:
            out = l - 1 - i
            break
    
    current.append(out)

xc = [i+1 for i in range(len(current))]

p.plot(xc,current)
p.ylabel('nth Term')
p.xlabel('Value of Term')
p.title("Van Eck's Sequence")
p.show()
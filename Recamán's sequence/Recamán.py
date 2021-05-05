def get_steps(n):
    used_nos = [0]
    steps = 1
    for i in range(n):
            temp = used_nos[-1] - steps
            if (temp > 0) and temp not in used_nos:
                used_nos.append(temp)
            else:
                used_nos.append(used_nos[-1] + steps)
            steps += 1
    return(used_nos)

n = int(input('how many terms do you want?\n'.title()))

out = get_steps(n)

for i in range(len(out)):
    print(i+1,out[i]) 

'''
import itertools

all_combinations = []

def get_edge_state(height_diff):
    if height_diff == 1:
        return ['s','c']
    if height_diff ==0:
        return ['f']
    else:
        return ['c']

def get_rotated_combination(combination, angle):
    # rotate the combination clockwise by angle
    if angle == 90:
        return [combination[3], combination[0], combination[1], combination[2],]
    elif angle == 180:
        return [combination[2], combination[3], combination[0], combination[1]]
    elif angle == 270:
        return [combination[1], combination[2], combination[3], combination[0]]
    else:
        return combination

def print_combination_and_edge_state(combination,old_combination=None,angle=0):
    edge_states = []
    for i in range(4):
        edge_states.append(get_edge_state(abs(combination[i]-combination[(i+1)%4])))
    if angle==0:
        all_combinations.append(combination)
        for edge_state_combination in itertools.product(*edge_states):
            print("".join(str(x) for x in (combination)), edge_state_combination)
    else:
        print("".join(str(x) for x in (combination)), "".join(str(x) for x in (old_combination)), angle)
        pass

combinations = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                combinations.append([i, j, k, l])

for combination in combinations:
    if combination[0] == 0:
        print("*"*50+"\n",combination)
        print_combination_and_edge_state(combination)
        for angle in [90, 180, 270]:
            rotated_combination = get_rotated_combination(combination, angle)
            print_combination_and_edge_state(rotated_combination,old_combination=combination,angle=angle)

print(len(all_combinations))
print(all_combinations)
'''
count = 1
c = {}
new = []
h = ["0","1","2","3"]
for i in h:
    for j in h:
        for k in h:
            for l in h:
                key = i+j+k+l
                if "0" in key:
                    if key[3:]+key[:3] in new:
                        c[key]=[key[3:]+key[:3],90]
                    elif key[2:]+key[:2] in new:
                        c[key]=[key[2:]+key[:2],180]
                    elif key[1:]+key[:1] in new:
                        c[key]=[key[1:]+key[:1],270]
                    else:
                        c[key]="new"
                        new.append(key)

for i in c.keys():
    print(count,i,c[i])
    count+=1
print(len(c))
# for i in new:
#     print(i,"new")
# print(len(new))

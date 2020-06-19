my_input={}

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_input[name]=score

init_min_val = min(my_input,key=my_input.get)
init_min_vals=[init_min_val]

for person in my_input:
    if person==init_min_val:
        next
    elif my_input[person]==my_input[init_min_val]:
        init_min_vals.append(person)

for person in init_min_vals:
    my_input.pop(person)

new_min_val = min(my_input,key=my_input.get)

min_vals = [new_min_val]

for person in my_input:
    if person == new_min_val:
        next
    elif my_input[person] == my_input[new_min_val]:
           min_vals.append(person)

min_vals.sort()

for name in min_vals:
    print(name)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

def runner_up(n, my_data):
    data=list(my_data)
    maximum=data[0]
    for i in range(n):
        if maximum<data[i]:
            maximum=data[i]

#Get index of max value

    data.remove(maximum)
    while max(data)==maximum:
        data.remove(maximum)
        if max(data)!=maximum:
            break

    new_max=max(data)
    return new_max




print(runner_up(n, arr))

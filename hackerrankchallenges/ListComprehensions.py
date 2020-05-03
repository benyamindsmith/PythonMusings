if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


def combinations(x,y,z,n):
    output = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                matrix=[i,j,k]
                output.append(matrix)
    output2=[]
    for i in output:
        if sum(i)!=n:
            output2.append(i)

    return output2

print(combinations(x,y,z,n))

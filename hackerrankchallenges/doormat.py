import math

length,width= map(int,input().split())

def designer_doormat(n, m):
    # Floor division

    split = n // 2

    # Top half
    for i in range(1, split + 1):
        # math.ceil() rounds division up.
        cp_split = (math.ceil(m / 2) + 1) - i * 3
        cp_art = 2 * i - 1
        print('-' * cp_split + '.|.' * cp_art + '-' * cp_split)
    # Welcome Sign
    print('-' * (m // 2 - 3) + 'WELCOME' + '-' * (m // 2 - 3))
    # Bottom Half
    # Just the reverse of the top half
    for j in range(1,split+1):
        cp_split = 3*j
        cp_art = int((m-(2*cp_split))/3)
        print('-'*cp_split+'.|.'*cp_art+'-'*cp_split)

designer_doormat(length,width)


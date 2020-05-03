if __name__ == '__main__':
    n = int(input().strip())

def weird_not_weird(number):
    if number%2!=0:
        print("Weird")
    elif 2 <= number <= 5 and number%2==0:
        print("Not Weird")
    elif 6<= number <= 20 and number%2==0:
        print("Weird")
    elif number>20 and number%2==0:
        print("Not Weird")


weird_not_weird(n)



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
def get_average(marks, q_name):
    selected=marks[q_name]
    aver=sum(selected)/3
    print("{:.2f}".format(aver))

get_average(student_marks,query_name)

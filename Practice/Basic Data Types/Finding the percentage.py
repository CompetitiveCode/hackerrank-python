#Answer to Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score = []
    score = student_marks[query_name]
    j=0.00
    for i in score:
        j+=i
    j/=3
    print("%.2f" %(j))
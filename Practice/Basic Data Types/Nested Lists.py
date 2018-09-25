#Answer to Nested Lists

if __name__ == '__main__':
    n = int(input())
    name = []
    names = []
    score = []
    scores = []
    for i in range(n):
        name.append(input())
        score.append(float(input()))
    l=min(score)
    j=0
    scores=score.copy()
    score.sort()
    for q in score:
        if(q>l and j==0):
            l=q
            j=1
    for t in range(n):
        if(scores[t]==l):
            names.append(name[t])
    names.sort()
    for y in names:
        print(y)
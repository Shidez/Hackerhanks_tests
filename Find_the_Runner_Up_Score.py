
n= int(input())
score = list(map(int, input().split()))
score.sort()
runner = score.index(max(score)) -1
print(score[runner])
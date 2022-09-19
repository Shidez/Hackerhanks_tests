
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for key in student_marks:
    if query_name == key:
        new_value = sum(student_marks[key]) / len(student_marks[key])
        print(f'{new_value:.2f}')
        print('{:.2f}'.format(new_value))

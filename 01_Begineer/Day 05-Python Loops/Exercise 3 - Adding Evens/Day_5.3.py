student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

total_even = 0
for i in range(0, 101):
    if i % 2 == 0:
        total_even += i

print(total_even)


student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

count = 0
total_height = 0
for height in student_heights:
    total_height += height
    count += 1

average_height = total_height / count
print("Average Height =", round(average_height, 2))

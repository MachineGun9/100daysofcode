# python loops
# for loop

fruits = ["Apple", "Mango", "Grapes", "Peach", "Tomato"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Sum & Highest Scores

student_scores = [44, 76, 34, 99, 67, 33, 94, 13, 76, 55, 98, 11, 80]

print(sum(student_scores))

sum_score = 0
for score in student_scores:
    sum_score = sum_score + score
print(sum_score)

print(max(student_scores))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

#range function (start, end, step)
total = 0
for number in range(1, 101):
    total += number
print(total)
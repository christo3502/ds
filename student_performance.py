def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

def highest_mark(marks):
    return max(marks)

def lowest_mark(marks):
    return min(marks)

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B+"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "D"
    else:
        return "Failed"


students = []

n = int(input("Enter the number of students: "))

for i in range(n):
    print("\n Student", i + 1)
    name = input("Enter name of the student : ")

    marks = []

    for j in range(3):
        mark = int(input("Enter the marks for subject : " + str(j + 1) + ": "))
        marks.append(mark)

    total = total_marks(marks)
    average = average_marks(marks)
    highest = highest_mark(marks)
    lowest = lowest_mark(marks)
    g = grade(average)

    students.append({
        'name': name,
        'total': total,
        'average': average,
        'highest': highest,
        'lowest': lowest,
        'grade': g
    })

students.sort(key=lambda x: x['name'], reverse=False
              )

print("\n----Students Performance----")

for student in students:
    print("\nName:", student['name'])
    print("Total Marks:", student['total'])
    print("Average Marks:", student['average'])
    print("Highest Mark:", student['highest'])
    print("Lowest Mark:", student['lowest'])
    print("Grade:", student['grade'])
    
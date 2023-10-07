# zip , Filter , Map , Enumerate , Lambda
students = ["Ahmed", "Mohamed", "Ali", "Sara", "Fatima", "Mona"]
grades = [75, 86, 90, 95, 65, 87]
threshold = 85
student_grade = zip(students,grades)
print('-'*10 , ' student name','-'*10)
for count ,  (std ,grade) in enumerate(student_grade ,1):
    print(f'{count}.\t{std:15} {grade}')
print('-'*10 , 'top student name','-'*10)
student_grade = zip(students,grades)
# print(list(student_grade))
top_student = filter(lambda grade : grade[1] >= threshold,student_grade)
# print(list(top_student))
top_student = sorted(top_student, key=lambda grade :grade[1],reverse=True)
for count ,(std , grade) in enumerate(top_student[:3] ,1):
    print(f'{count}.\t{std:15} {grade}')
top_name = map(lambda name : name[0] , top_student[:3])
print('-'*10 , 'top  name','-'*10)
for name in top_name:
    print(name)
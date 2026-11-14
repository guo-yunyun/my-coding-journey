student = {'name': '张三', 'age': 23, 'score': 89}
print(student['name'])
print(student['age'])
print(student['score'])

student['age'] = 19
student['score'] = 90
print(student)

del student['score']
print(student)

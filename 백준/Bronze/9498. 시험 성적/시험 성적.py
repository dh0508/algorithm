pnt = int(input())
level = pnt//10
grades={10:'A',9:'A',8:'B',7:'C',6:'D'}
grade = grades.get(level, 'F')
print(grade)
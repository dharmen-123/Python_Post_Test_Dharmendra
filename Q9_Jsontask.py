# Q9. JSON — Student Database: (5 Marks)
# • Create a list of 4 students:
# Each student: name, age, city, course, marks
# • Save to 'students.json' with indent=4
# • Read the file back
# • Print only students with marks > 70
# • Print total number of students
import json
student=[{"name":'Ravi','age':'20','city':'Bhopal','course':'DBMS','marks':50},
        {"name":'Aman','age':'22','city':'Rewa','course':'ML','marks':60},
        {"name":'Vikas','age':'23','city':'Dewas','course':'OS','marks':75},
        {"name":'Raj','age':'24','city':'Pune','course':'CN','marks':80}]

with open('Student.json','w') as f:
    json.dump(student,f,indent=4)

with open('Student.json','r') as f:
    for i in f:
        if(i['marks']>70):
            print(i['name'])
        

# Q7. Set & Dictionary Operations: (6 Marks)
# • Create a set of 6 students (with 2 duplicates)
# • Print set — duplicates automatically removed
# • Add 2 new students to set
# • Create a dictionary of 4 students with their marks
# • Loop through dictionary:
# fi marks >= 75: print 'Distinction'
# fi marks >= 60: print 'Pass'
# fi marks < 60 : print 'Fail'

S={"Raj","Aman","Raju","Vikas","Raj","Aman"}
print(S)

S.add("Tanish")
S.add("Yuraj")
print(S)

D={"Amit":85,"Raju":65,"Suryansh":90,"Vikas":50}
for j in D:
    if(D[j]>=75):
        print(j," Distinction")
    elif(D[j]>=60):
        print(j," Pass")
    else:
        print(j," Fail")

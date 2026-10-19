s1="Ali"
s2="Ahmed"
# covert input from string to int
m1=int(input("Enter the marks of Student 1 : ")) 
m2=int(input("Enter the marks of Student 2 : ")) 
if m1>=80:
    print("Grade : A")
elif m1>=70:
    print("Grade : b")
elif m1>=60:
    print("Grade : c")
elif m1>=50:
    print("Grade : D")
elif m1<50:
    print("Grade : F")

if m2>=80:
    print("Grade : A")
elif m2>=70:
    print("Grade : b")
elif m2>=60:
    print("Grade : c")
elif m2>=50:
    print("Grade : D")
elif m2<50:
    print("Grade : F")
if m1>m2:
    print("Student : ",s1," has greater marks ",m1)
else:
    print("Student : ",s2," has greater marks ",m2)

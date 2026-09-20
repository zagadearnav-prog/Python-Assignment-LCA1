#Dictionary
student= {
    101: ("Arnav","Computer Science","A+++"),
    102: ("Sadie_Sink","Computer Science", "A++"),
    103: ("Sayyam", "Mettalurgy","B"),
    104: ("Sarthak", "Mech", "B"),
    105: ("Swarnim","ECE","B-"),
}
#Addition of new student
def add_student(roll_no,name,branch,marks):
    student[roll_no] = (name,branch,marks)

add_student(106,"Jayesh","ECE","A")

#Deletion of student
def del_student(roll_no):
    if roll_no in student:
        del student[roll_no]
    else:
        print("Roll no. not found")    

del_student(104)

#Updation of student
def update_student(roll_no,name,branch,marks):
    if roll_no in student:
        student[roll_no] = (name,branch,marks)
    else:
        print("Roll no. not found")
update_student(105,"Swarnim","ECE","A++")

def display_student():
    for key, value in student.items():
        print(key, value)
display_student()
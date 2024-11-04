student_name = ["Sandra","Patricia","Phiona","Anita"]
student_marks = [80,56,78,90]

#Print Patricia, Faith, Phiona and Anitah
student_name.remove("Sandra")
student_name.insert(1,"Faith")
print(student_name)
#Add Masha at the fourth position.
student_name.insert(3,"Masha")
print(student_name)
#Update the name Phiona to Phiona Aladina
student_name[2] = "Phiona Aladina"
print(student_name)
#Display the length of the student list
length1 = len(student_name)
length2 = len(student_marks)
print(f"The length of the student name list is {length1} and the length of the student marks list is {length2}")
#Print all the student names using a for loop.
for character in student_name:
    print(character)
#Calculate the total marks for the student marks variable
total_marks = sum(student_marks)
print(f"The total marks of the students is {total_marks}")
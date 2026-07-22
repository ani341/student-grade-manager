#--------------STUDENT GRADE MANAGER------------------

usr_name = input("enter your full name here :")
usr_age = int(input("enter your age here :"))

name_parts = usr_name.split()

initials = ""

for part in name_parts:
    initials = initials + part[0].upper()+"."

print(f"WELCOME mr {usr_name.title()} {initials}")

subject_tuple = ("Bangla","english","math","science","somaj")
print("Here are your subjects :")

for subject in subject_tuple:
    print(f"\t{subject}") #here i not used \n intentionally because print automatically print a new line after executes,now if i add \n it wil print one more new line . 

print()

subject_marks_lst= []

for subject in subject_tuple:
    mark = int(input(f"enter your marks for {subject} : "))
    subject_marks_lst.append(mark)

print()

sub_and_mark_dict= {}

for i in range(len(subject_tuple)) :
    sub_and_mark_dict[subject_tuple[i]] = subject_marks_lst[i]


total_marks = sum(sub_and_mark_dict.values()) #not used in this project
average_marks = total_marks / len(subject_tuple) #not used in this project


for sub, mark in sub_and_mark_dict.items():
    sentence= f"subject {sub} mark is : "
    print(f"{sentence:<27}{mark}")

    if(mark<40):
        print(f"you have failed in {sub}")

    else:
        print(f"you have passed in {sub}")


for i in subject_marks_lst:
    if(i<40):
        print(f"you have got warning becasuse you have failed\n")
        # print() #it also add new line . print() function tells it: "Move down after you're done."
        break
else:
    print(f"congratulations.you have passed in all the subjects\n")
    # print() #it also add new line print() function tells it: "Move down after you're done."



highest_marks = max(subject_marks_lst)
lowest_marks = min(subject_marks_lst)

print(f"the highest mark from the marks is :{highest_marks}")
print(f"the lowest mark from the marks is :{lowest_marks}")


unique_marks_set = set(subject_marks_lst)
print(f"you have got {len(unique_marks_set)} unique marks")

print()

print(f"GOOD BYE MR {usr_name} {initials} \nand your birth year is : {2026-usr_age}")

# print("GOOD BYE MR",usr_name,initials+"\nand your birth year is :",2026-usr_age) #this is old method 

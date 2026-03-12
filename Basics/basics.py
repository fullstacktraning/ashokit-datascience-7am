# lists
# tuples
# set
# dictionary
# numpy
# pandas
# matplotlib
# seaborn
# tensorflow




# msg = " welcome to python basics "
# print(msg.upper())
# print(msg.lower())
# print(msg.strip())
# print(msg.replace("python","python3").strip())
# for x in msg.strip().split(" "):
#     print(x)



# lists = [10,20,30,40,50]
# print(lists[0], lists[-5])
# print(lists[1:4])
# print(lists[4:])
# print(lists[:3])


#lists. ---  append().   remove() 
# tasks = []

# while True:
#     print("\n1.Add 2. View. 3. Remove. 4. Exit")
#     choice = input("Enter Choice :")
#     match choice:
#         case "1":
#             task = input("Enter Task:")
#             tasks.append(task)

#         case "2":
#             print("Tasks", tasks)
        
#         case "3":
#             task = input("Enter Task to Remove")
#             if task in tasks:
#                 tasks.remove(task)
#         case "4":
#             break
            
#         case _:
#             print("Invalid Choice")





# marks = [85, 72, 48, 90, 33]

# for mark in marks:    
#     if mark >= 90:
#         grade = "A++"
#     elif mark >= 70:
#         grade = "A"
#     elif mark >= 50:
#         grade = "C"
#     else:
#         grade = "Fail"

#     print("Marks :", mark, "Grades :", grade)



# salary = 60000
# credit_score = 720

# match salary:
#     case salary if salary > 50000 and credit_score > 700:
#         print("Eligible for Loan")
#     case _:
#         print("Loan Rejected")






# marks = 75

# match marks:
#     case grade if grade>=90:
#         print("Grade A")
#     case grade if grade<=90:
#         print("Grade B")
#     case _:
#         print("Invalid")




# age = 20
# day = 8
# match day:
#     case 1 | 2 | 3 | 4 | 5:
#         print("Weekday")
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Invalid")



# marks = 75
# match marks:
#     case 90:
#         print("Grade A")
#     case 75:
#         print("Grade B")
#     case 50:
#         print("Grade C")
#     case _:
#         print("Fail")

# if marks >= 90:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")


# if age >= 18:
#     print("Eligible For Vote !!!")
# else:
#     print("Not Eligible For Vote !!!")




# if age >= 18:
#     print("Eligible for Vote")


# msg = "Good Morning !!!"
# print(msg)

# num1 = 200
# num2 = 100
# print("Addition :",num1+num2)
# print("Subtraction :",num1-num2)

# flag = False
# print(flag)

# res = "Hello" if flag else "Welcome"
# print(res)
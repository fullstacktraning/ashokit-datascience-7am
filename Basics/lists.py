# matrix = [[1,2,3],
#            [4,5,6]]

# target = 50
# Found = False
# for row in matrix:
#     for num in row:
#         if num == target:
#             Found = True


# if not Found:
#     print("Not Found")
# else:
#     print("Found")



# matrix = [[1,2,3],
#           [4,5,6]]

# transpose = []
# for i in range(len(matrix[0])):      # i = 0,1,2
#    row=[] 
#    for j in range(len(matrix)):        # j = 0,1
#       row.append((matrix[j][i]))
      
#    transpose.append(row)

# print(transpose) 
      



# matrix1 = [[1,2],
#            [3,4]]
# matrix2 = [[5,6],
#            [7,8]]
# result = []

# for i in range(2):
#     row = []
#     for j in range(2):
#         row.append(matrix1[i][j] + matrix2[i][j])
#     result.append(row)

# print(result)



# numbers = [[1,2],[3,4]]

# max_value = numbers[0][0]
# for row in numbers:
#     for num in row:
#         if num > max_value:
#             max_value = num
# print(max_value)


# total = 0
# for row in numbers:
#     for num in row:
#         total += num
# print(total)


# rows = 3
# cols = 3

# matrix = [[1 for _ in range(cols)] for _ in range(rows)]
# print(matrix)



# nested = [[10,20,30],
#           [40,50,60],
#           [70,80,90]]
# for row in nested:
#     print(" ".join(map(str, row)))




# nested = [[10,20,30],
#           [40,50,60],
#           [70,80,90]]
# for row in nested:
#    for num in row:
#        if num%2 != 0:
#             print(num)




# nested = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# print(nested[0][0])
# print(nested[2][2])




# ages = [12,30.45,35,70,80]
# new_list = list(filter(lambda age:age<18,ages))
# print(new_list)

# numbers = [1,2,3,4,5]
# new_numbers = list(map(lambda num:num*100,numbers))
# print(new_numbers)



# marks = [10,20,30,40,50]
# new_marks = list(map(lambda x:x+5, marks))
# print(new_marks)


# numbers = [10,20,30,10,10,10,20,20,40,30]
# duplicates = []
# # print(numbers.count(10))
# # print(numbers.count(20))
# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)
# print(duplicates)




# numbers = [10,11,12,13,14,15]
# even = []
# odd = []
# for num in numbers:
#     if num%2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print(even)
# print(odd)

# tasks = []
# while True:
#     print("1. Add Task")
#     print("2. Remove Task")
#     print("3. View Tasks")
#     print("4. Exit")

#     choice = input("Enter Your Choice: ")
#     if choice == "1":
#         task = input("Enter Task :")
#         tasks.append(task)

#     elif choice == "2":
#         task = input("Enter Task to remove :")
#         tasks.remove(task)

#     elif choice=="3":
#         for task in tasks:
#             print(task)
#     elif choice == "4":
#         break




# marks = []

# for sub in range(6):
#     marks.append(int(input("Enter Student Marks :")))

# print(marks)
# print(sum(marks))
# print(sum(marks) / len(marks))
# print(max(marks))
# print(min(marks))



# print( [x for x in range(10) if x%2  == 0] )

# print( [x*x for x in range(5)] )


# numbers = [100,200,300,400,500]
# new_arr = numbers[::-1]
# print(numbers)
# print(new_arr)




#numbers = [100,500,200,400,300]
#len()
#sum()
#max()
#min()
#sort()
#reverse()
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# numbers.sort()
# numbers.reverse()
# print( numbers[::-1] )

# numbers = [100,200,300,400,500]
# if 200 in numbers:
#     print("Search Success !!!")
# else:
#     print("Not Found !!!")


# numbers = [100,200,300,400,500]
# for num in numbers:
#     print(num)


# numbers = [100,200,300,400,500]
# numbers.remove(300)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.pop(1)
# print(numbers)


# numbers = [10,20,30,40,50]
# print(numbers[0],numbers[-5])
# print(numbers[2],numbers[-3])
# print(numbers[1:4]) 
# print(numbers[:2])
# print(numbers[2:])
# numbers[1] = 25
# numbers.insert(1,20)
# numbers.extend([60,70]);
# numbers.append(80)
# print(numbers)




# list = []
# print(list)

# numbers = [10,20,30,40,50]
# print(numbers)

# mixed = ["Hello",100,True,None]
# print(mixed)
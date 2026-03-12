# student = ("Ravi",21,"CSE")
# print( student[0] )
# print( student[1] )
# print( student[2] )

# student[1] = 22. #TypeError: 'tuple' object does not support item assignment


# numbers = (10,20,10,30)
# print( numbers.count(10) )
# print( numbers.count(20) )


# numbers = (10,20,30,40,50)
# print(numbers[2:4])
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[3:])


# subjects = ("Python","ML","DL","NLP","GenAI","AgenticAI")
# for sub in subjects:
#     print(sub)


# data = 10,20,30
# t1,t2,t3 = data
# print(t1, t2, t3)


# def test_func():
#     return ("Std1",21)

# sname,age = test_func()
# print(sname,age)

# nested = (
#     ("Emp1",10000),
#     ("Emp2",20000),
#     ("Emp3",30000)
# )
# for tup in nested:
#     empName,salary = tup
#     print(empName)
#     print(salary)

# tuple = (10,)
# print(tuple)


# tuple = (10,20,30,40,50,10,20,30)
# print(tuple.index(50))
# print(tuple.count(10))
# print(tuple.index(10))
# print(tuple.index(20))


# list1 = [("Emp1",10000),("Emp2",20000)]
# list1.append( ("Emp3",30000) )
# #print(list1)
# for l in list1:
#     for e in l:
#         print(e)


tuple = (10,20,30,40,50,5)
#print(len(tuple))
#print(max(tuple))
#print(min(tuple))
#print( tuple[::-1] )


# a = 10
# b = 20
# a,b = b,a
# print(a,b)


# t = (10,20,30,40,50)
# l = list(t)
# l.append(60)
# z = tuple(l)
# print(z)



# t = (10,20,30,40,50)
# found = False
# for e in t:
#     if e == 50:
#         found = True

# print(found)


# nums = (10,20,30,40,50)
# remove = 30
# tuple to list
# remove(30)
# list to tuple
# tuple

# nested = ((10,20),(30,40),(50,60))
# flat = ()
# for pair in nested:
#     flat += pair

# print(flat)

# numbers = (10,40,20,90,60)
# 60
# first = second = float('-inf')
# print(first)
# first = -inf
# second = -inf
# for num in numbers:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num
# print(second)
# print(first)

# data = [10,20,30,10,20,30]
# data1 = set(data)
# print(data1)


# numbers = (10,20,30,40,50)
# minimum = maximum = numbers[0]
# for num in numbers:
#     if num < minimum:
#         minimum = num
#     if num > maximum:
#         maximum = num

# print(minimum)
# print(maximum)

numbers = (10,20,30,40,50)
a, *b, c = numbers
print(a)
print(b)
print(c)





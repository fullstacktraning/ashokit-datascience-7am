import matplotlib.pyplot as plt

plt.subplot(1,2,1)
x = [1,2,3,4,5]
y1 = [10,20,30,40,50]
plt.plot(x,y1)
plt.grid()
plt.title("Line Graph !!!")

plt.subplot(1,2,2)
students = ["Std1","Std2","Std3","Std4","Std5"]
marks = [90,80,70,60,50]
plt.bar(students,marks,color="green")
plt.title("Students Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()



# x = [1,2,3,4,5]
# y1 = [10,20,30,40,50]
# plt.plot(x,y1,label="Line 1",color="red")
# y2 = [15,25,35,45,55]
# plt.plot(x,y2,label="Line 2",color="aqua")
# plt.legend()
# plt.show()




# x = [1,2,3,4,5]
# y = [10,20,30,40,50]
# plt.scatter(x,y)
# plt.title("Demo Scatter")
# plt.xlabel("X Label")
# plt.ylabel("Y value")
# plt.show()


# marks = [45,60,70,80,90,55,67,73,88,92]
# plt.hist(marks,bins=5)
# plt.title("Students Histogram")
# plt.xlabel("Marks Range")
# plt.ylabel("No of Students")
# plt.show()




# students = ["Std1","Std2","Std3","Std4","Std5"]
# marks = [90,80,70,60,50]
# plt.pie(marks,labels=students,autopct='%1.2f%%')
# plt.title("Students Pie Chart")
# plt.show()

# students = ["Std1","Std2","Std3","Std4","Std5"]
# marks = [90,80,70,60,50]
# plt.barh(students,marks,color="red")
# plt.title("Students Bar Chart")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.show()



# students = ["Std1","Std2","Std3","Std4","Std5"]
# marks = [90,80,70,60,50]
# plt.bar(students,marks,color="green")
# plt.title("Students Bar Chart")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.show()





# x = ["Std1","Std2","Std3","Std4","Std5"]
# y = [90,80,70,60,50]
# plt.plot(x,y,marker='D', markersize=10,markerfacecolor='red',markeredgecolor='green')
# plt.title("Students Progress")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.show()




# x = [1,2,3,4,5]
# y = [10,20,30,40,50]
# plt.plot(x,y)
# plt.title("Line Graph !!!")
# plt.xlabel("X Value")
# plt.ylabel("Y Value")
# plt.show()
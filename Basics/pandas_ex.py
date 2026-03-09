import pandas as pd

df = pd.read_excel("Book2.xlsx")
print(
    df.groupby("Department")["Salary"].mean()
)
print(
    df.groupby("Department")["Salary"].max()
)
print(
    df.groupby("Department")["Salary"].min()
)
print(
    df.groupby("Department")["Salary"].sum()
)

#df = pd.read_excel("Book1.xlsx")
#print(df)
#print(df.isnull())
#print(df.dropna())
#print(df.fillna(77))


#df = pd.read_excel("Students.xlsx") # read excel sheet, pandas and openpyxl
#print(df)
#print(df.head()) #display first 5 rows
#print(df.tail()) #display last 5 rows
#print(df.shape)  #know rows & colums (rows,columns)
#print(df.columns) #display columns (names)
#print(df.dtypes) #display datatypes
#print(df["Name"]) #display single column
#print(df[["Name","Marks"]]) #display more columns
#print(df.loc[0]) #access based on index (location)
#print(df.loc[0:2]) # display from 0 to 2
#print(df[df["Marks"]>80]) # applying conditions
#df["Grades"] = ["C","B","A"] # add new columns
#df.loc[0,"Marks"]=95 # modify particular cell data
#print(df.drop("Grades",axis=1) ) #drop the column
#print(df.sort_values("Marks",ascending=False) ) #sort the data either ascending / decending





# df = pd.read_csv("students.csv")
# print(df)


# data =  {
#     "name" : ["Std1","Std2","Std3"],
#     "age" : [20,22,24],
#     "marks" : [70,80,90]
# }
# df = pd.DataFrame(data)
# print(df)






#data = [10,20,30,40]
#s = pd.Series(data)
#s = pd.Series(data,index=['a','b','c','d'])
#s = pd.Series(data,index=["Std1","Std2","Std3","Std4"])
#print(s)
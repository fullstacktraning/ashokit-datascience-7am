import pandas as pd
data = {
    "salesperson":["s1","s1","s2","s2"],
    "product":["Laptop","Mobile","Laptop","Mobile"],
    "sales":[50000,20000,60000,30000]
}
df = pd.DataFrame(data)
df1 = pd.pivot_table(
        df,
        index="salesperson",
        columns="product",
        values="sales",
        aggfunc="max",
        margins=True
)
print("\nPivot Table\n")
print(df1)




# import pandas as pd
# data = {
#     "salesperson":["s1","s1","s2","s2"],
#     "product":["Laptop","Mobile","Laptop","Mobile"],
#     "sales":[50000,20000,60000,30000]
# }
# df = pd.DataFrame(data)
# df["sales"].mean()
# df1 = pd.pivot_table(df,index="salesperson",columns="product",values="sales",aggfunc="mean")
# print(df1)



# df = pd.read_excel("p1.xlsx")
# df1 = pd.pivot_table(df,index="Name",columns="Subject",values="Marks")
# df1.to_excel("p2.xlsx")
# df2 = pd.read_excel("p2.xlsx")
# print(df2)


# data = {
#     "name":["Std1","Std2","Std3","Std4"],
#     "marks":[60,70,80,35]
# }
# df = pd.DataFrame(data)
# print("Average :",df["marks"].mean())
# print("Maximum :",df["marks"].max())
# print("Minimum :",df["marks"].min())
# print("Sum :",df["marks"].sum())
# print( df[df["marks"]<50] )



# df1 = pd.read_excel("sheet1.xlsx")
# df2 = pd.read_excel("sheet2.xlsx")
# df3 = pd.merge(df1,df2,on="id")
# df3.to_excel("output.xlsx",index=False)
# output = pd.read_excel("output.xlsx")
# print(output)


# df = pd.read_excel("Book2.xlsx")
# print(
#     df.groupby("Department")["Salary"].mean()
# )
# print(
#     df.groupby("Department")["Salary"].max()
# )
# print(
#     df.groupby("Department")["Salary"].min()
# )
# print(
#     df.groupby("Department")["Salary"].sum()
# )

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
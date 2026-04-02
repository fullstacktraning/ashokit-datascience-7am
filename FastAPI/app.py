# "FastAPI" is the class available in "fastapi" module/library
from fastapi import FastAPI
from student import Student
from fastapi.middleware.cors import CORSMiddleware


# app object, used to develop API calls GET,POST,PUT,DELETE,HEAD,....
app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.get("/")
def home():
    return ({"msg" : "welcome to basic examples of FastAPI !!!"})

#path parameter
@app.get("/student/{id}")
def get_student(id: int):
    return {"student_id" : id}


#query parameter
@app.get("/search")
def search(name: str,age: int):
    return {"name" : name, "age" : age}


@app.post("/add")
def add_student(student : Student):
    return {"data" : student}


@app.put("/update/{id}")
def update_student(id: int, std: Student):
    return {"id":id, "updated_data": std}

@app.delete("/delete/{id}")
def delete_student(id: int):
    return {"message" : f"Student {id} deteled"}
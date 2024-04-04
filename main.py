import requests
from models import Student
import json


# Option 1: Download file from Source
# url = "https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v3.json"
# response = requests.get(url)
# data = response.json()

# Option 2: Open file from local file (Same file)
with open("student_v3.json") as file:
    data = json.load(file)


for student in data:
    # print(student)
    model = Student(**student)
    print(model)
    break

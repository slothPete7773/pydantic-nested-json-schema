import requests
from models import Student

url = "https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v3.json"
response = requests.get(url)
data = response.json()

for student in data:
    # print(student)
    model = Student(**student)
    print(model)
    break

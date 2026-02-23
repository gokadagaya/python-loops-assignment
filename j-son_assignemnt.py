import json
print("******************************")
print("***********Tak 1**************")
print("******************************")

user_profile={"Name":"Gayatri","Age":25,"Email":"gayatri@gmail.com","is_active":True,"Skills":["Python","SQL","Java"]}
js=json.dumps(user_profile,indent=2)
print(js)


print("******************************")
print("***********Tak 2**************")
print("******************************")


api_res='{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'

py=json.loads(api_res)

username=py["data"]["username"]
score=py["data"]["score"]

print(username)
print(score)

print(f"User {username} scored {score} points")

print("******************************")
print("***********Tak 3**************")
print("******************************")

js_user='''{
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}'''

py_user=json.loads(js_user)

print("city",py_user["address"]["city"])
print("zipCode",py_user["address"]["zip"])

py_user["address"]["Country"]="India"

print("Updated Json:",json.dumps(py_user,indent=2))


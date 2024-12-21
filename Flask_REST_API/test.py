import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + "/video/5", {'likes' : 10, "name": "Python for Dummies", "views": 15000 })
print(response.json())
# 
# response = requests.put(BASE + "/video/4", {'likes' : 10, "name": "Python for Dummies", "views": 15000 })
# print(response.json())
# names = ["Abdalla", "Alaa", "Homer"] 

# for name in names:
#     response = requests.get(BASE + f'/helloworld/{name}')   
#     # response = requests.post(BASE + '/helloworld')   
#     print(response.json())
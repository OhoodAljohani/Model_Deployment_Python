import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'SLength':6,'SWidth':4, 'PLength':1, 'PWidth':6})

print(r.json())

#print(requests.__version__) #0.16.0

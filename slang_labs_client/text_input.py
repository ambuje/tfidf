import requests
txt_inp = input('Enter Text \n')


files = {'input': txt_inp}
r = requests.post('http://127.0.0.1:5000/input', json=files)
print(r)
data = r.json()

print("Similarity of user input with different text files \n", data['Data'])

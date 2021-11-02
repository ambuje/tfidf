import requests
file_path = input(
    'Please enter full file path. For multiple files, seperate it by","\n')\
    .split(',')


files = [('file', open(f, 'rb')) for f in file_path]
r = requests.post('http://127.0.0.1:5000/files', files=files)
print(r)
print("Status = ", r.status_code)

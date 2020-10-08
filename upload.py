import requests
from pathlib import Path
import json, os, sys
import mimetypes

file_path = input("Enter file path? ")
if os.path.exists(file_path):
    try:
        file = open(file_path, 'rb')
        files = {'file': (file_path, file, mimetypes.guess_type(file_path)[0])}
        server = "http://127.0.0.1:8000"
        response = requests.post(f"{server}/file/upload", files=files)
        print('\n')
        response_dict = json.loads(response.text)
        print(f"\tstatus: {response_dict['status']}")
        print(f"\tmessage: {response_dict['message']}")
        file_details = response_dict['file_details']
        for i in file_details:
            print(f"\t{i}: {file_details[i]}")
        print('\n')
    except BaseException as e:
        print("\t", e)
else:
    print("\t File doesnot Exist!!!")

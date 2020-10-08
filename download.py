import os
import requests
import json
from tqdm import tqdm
import wget

def fetch_file():
    name = input("Enter file name? ")
    # output_path = input("Enter the path to the folder where you want to save? ")
    # if (os.path.exists(output_path)):
    server = "http://127.0.0.1:8000"
    url = f"{server}/file/fetch?name={name}"
    response = requests.get(url)
    file_dict = json.loads(response.text)
    try:
        if file_dict['file']:
            print(f"Downloading {file_dict['file']}")
            download_file(f"{server}/media/files/{file_dict['file']}")
    except:
        print("File doesnot exist")
    # else:
    #     print("Output folder doesnot exists!!!")

def download_file(url):
    local_filename = url.split('/')[-1]
    local_filename = local_filename.replace("_", " ")
    # NOTE the stream=True parameter below
    if ('.gz' in local_filename):
        wget.download(url)
    else:
        with requests.get(url, stream=True) as r:
            total_size = int(r.headers.get('content-length', 0))/(32*1024)
            r.raise_for_status()
            t = tqdm(total=total_size, unit='iB', unit_scale=True, unit_divisor=1024)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=32*1024): 
                    if chunk: # filter out keep-alive new chunks
                        t.update(len(chunk))
                        f.write(chunk)
                        # f.flush()
                r.close()
    print('\n'+str(local_filename) + " downloaded successfully")

fetch_file()

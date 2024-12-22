import requests

url = "https://raw.githubusercontent.com/Abarnika08/First_Repository/refs/heads/main/hello.py"
response = requests.get(url)

if response.status_code == 200:
    print("File fetched successfully!")
    print("Content of hello.py:")
    print(response.text)
else:
    print(f"Failed to fetch file. Status code: {response.status_code}")

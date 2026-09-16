#from jsonrpclient import request
#num = 7
#response = request("http://localhost:5000", "double", num=num)
#print("Double", num, "is", response.data.result)

# book example above is deprecated.
# google AI Mode provides the following code:

import requests
from jsonrpcclient import request, parse, Ok

num = 7

payload = request("double", params={"num": num})

response = requests.post("http://localhost:5000", json=payload)

parsed = parse(response.json())

# safely handle response structure
if isinstance(parsed, Ok) :
    print("Double", num, "is", parsed.result)
else :
    print(f"Error: {parsed.message} (Code: {parsed.code})")
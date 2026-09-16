import json
import sys
import requests

def search(title) :
    url = "http://archive.org/advancedsearch.php"
    params = {
        "q": f"title:({title})",
        #"q": f"isbn:({title})", # testing query
        "output": "json",
        "fl[]": ['identifier', 'title'],
        "rows": 50,
        "page": 1,
    }
    resp = requests.get(url, params=params)
    
    return resp.json()

if __name__ == "__main__" :
    title = sys.argv[1]
    data = search(title)

    docs = data["response"]["docs"]
    
    print("\n", f"Found {len(docs)} items, showing first 10", "\n")
    print("identifier\n\ttitle")
    for row in docs[:10] :
        print(row["identifier"], "\n\t", row["title"])

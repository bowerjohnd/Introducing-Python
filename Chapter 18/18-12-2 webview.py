
# interpreter book examples

import webview
url = input("URL? ")
if "http://" not in url :
    url = "http://" + url
    print("'http://' prefix added.")

print("webview opening:", url)

webview.create_window(f"webview display of {url}", url)
webview.start()
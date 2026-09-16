# interpreter book examples

import antigravity  # opens browser to xkcd.com/353 automatically

import webbrowser
url = 'http://www.python.org/'
print(webbrowser.open(url))

print(webbrowser.open_new(url))

print(webbrowser.open_new_tab('http://www.python.org/')) # do not misspell python with pythong, you get... Hasselhoff

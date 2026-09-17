# I improved upon the book example of this program to include:
#       - added optional cli argument for custom search result rows
#       - error handling of cli arguments

"""Find a video at the Internet Archive
by a partial title match and display it."""

import os
import sys
import webbrowser
import requests

def search(title, rows=10):
    """Return a list of 3-item tuples (identifier,
        title, description) about videos
        whose titles partially match :title."""

    search_url = "https://archive.org/advancedsearch.php"
    params = {
        "q": "title:({}) AND mediatype:(movies)".format(title),
        "fl": "identifier,title,description",
        #"fl[]": ['identifier', 'title', 'description'],    # from troubleshooting 18-01. Both work.
        "output": "json",
        "rows": rows,
        "page": 1,
    }
    resp = requests.get(search_url, params=params)
    data = resp.json()

    docs = [( doc["identifier"], doc["title"], doc.get("description", "None")) # using .get to prevent crash when no description key found in results
        for doc in data["response"]["docs"]]

    print("\n\033[34m" 
        + "Found", len(docs), "results for " 
        + "'" + title + "'"
        + "\033[0m\n")

    return docs

def choose(docs):
    """Print line number, title and truncated description for
        each tuple in :docs. Get the user to pick a line
        number. If it's valid, return the first item in the
        chosen tuple (the "identifier"). Otherwise, return None."""

    # ANSI foreground font colors:
    #   \033[0m     reset
    #   \033[31m     red
    #   \033[32m     green
    #   \033[33m     yellow
    #   \033[34m     blue
    #   \033[35m     magenta

    last = len(docs) -1
    for num, doc in enumerate(docs):
        print(f"{num}: (\033[32m{doc[1]}\033[0m])")
        print("\t\033[35m", f"{doc[2][:100]}...\033[0m")
    index = input(f"Which would you like to see (0 to {last})? ")

    try:
        return docs[int(index)][0]
    except:
        return None

def display(identifier):
    """Display the Archive video with :identifier in the browser"""

    details_url = "https://archive.org/details/{}".format(identifier)
    print("Loading", details_url)
    webbrowser.open(details_url)

def main(title, rows=10):
    """Find any movies that match :title.
        Get the user's choice and display it in the browser."""

    identifiers = search(title, rows)

    if identifiers:
        identifier = choose(identifiers)

        if identifier:
            display(identifier)
        else:
            print("Nothing selected")
    else:
        print("Nothing found for", title)

def printArgErrors(args):
        print(
            "\n\033[33m\033[4m"
            + "Invalid or no arguments passed: " + "\033[31m" + str(args) + "\033[33m"
            + "\033[24m\n"
            + "Required argument 1 for title, optional argument 2 for number of results (default 10).\n"
            + "Use \"quotes\" when searching for multiple word titles.\n\n" 
            + "\033[0m"
            + "Example 1: " + "\033[32m py '" + os.path.basename(__file__) + "' \"the matrix\" \033[33m\n"
            + "\t - Searches titles for 'the matrix' and displays up to 10 results." + "\033[33m\033[0m\n"
            + "Example 2: " + "\033[32m py '" + os.path.basename(__file__) + "' matrix 50" + "\033[33m\n"
            +"\t - Searches titles for 'matrix' and displays up to 50 results." + "\033[0m\n"
            )
        exit()

def checkArgsAndRunMain(args):

    if len(args) == 1:
        main(args[0])
    elif len(args) == 2:
        try:
            if int(args[1]) > 0:
                main(args[0], args[1])
            else:
                print("\n\033[33m" + "Second argument for number of results must be greater than 0")
                print("Using default number of results of 10.")
                main(args[0])
        except:
            printArgErrors(args)
    else:
        printArgErrors(args)



if __name__ == "__main__":

    # main(sys.argv[1]) # book example

    args = sys.argv[1:] 
    checkArgsAndRunMain(args)

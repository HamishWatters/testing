import search
import webbrowser
strings = ["bleeding gums", "death", "full blown aids", "cancer", "test",
            "help me I'm dying", "shit it's done", "blood"]
#strings = ["bleeding gums","help me I'm dying"]

#strings = ["help me I'm dying"]

for s in strings:
    webbrowser.open(search.main(s,"relevance","1")[0].get('fullText'))


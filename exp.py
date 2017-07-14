#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 #File Name : exp.py
 #Creation Date : 14-07-2017
 #Created By : Rui An  
#_._._._._._._._._._._._._._._._._._._._._.

import json

with open("./paleocar.jsonld") as request_info:
    data = json.load(request_info)
    print data['title']
    print data['outputs']

def fuck(hello=None, vibe=None):
    if(not hello and not vibe):
        print "fuck"
    else:
        print hello  

hello = "oh yeah"
fuck(hello=hello)


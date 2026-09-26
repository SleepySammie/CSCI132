from pythonds3.basic import Stack

def checkTags(htmlStr):
    s = Stack()
    for tag in htmlStr:
        if tag in "<html>" or tag in "<head>" or tag in "<h1>" or tag in "<body>" or tag in "<title>":
            s.push(tag)
        else:
            if s.is_empty():
                return False
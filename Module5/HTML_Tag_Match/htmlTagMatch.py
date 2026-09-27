from pythonds3.basic import Stack

def checkTags(htmlStr):
    s = Stack()
    for tag in htmlStr:
        if tag in "<html>" or tag in "<head>" or tag in "<h1>" or tag in "<body>" or tag in "<title>":
            s.push(tag)
        else:
            if s.is_empty():
                return False

def main():
    checkTags(test_balanced)

    test_balanced = """<html>
    <head>
        <title>
            Example
        </title>
    </head>
    
    <body>
        <h1>Hello, world</h1>
    </body>
    </html>
    """
    
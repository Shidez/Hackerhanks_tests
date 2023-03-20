import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    
s = wrap('kjkjhghgdfdsdfsghhh', 4)
print(s)
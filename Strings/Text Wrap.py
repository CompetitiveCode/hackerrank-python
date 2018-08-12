#Answer to Text Wrap

def wrap(string, max_width):
    s=textwrap.wrap(string,max_width)
    t=''''''
    for i in s:
        t=t+i+"\n"
    return t
#Answer to Validating Email Addresses With a Filter

def fun(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    
    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True

"""
Let's say you have to make a list of the squares of integers from  to  (both included).

>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
Now, you only require those elements that are greater than  but less than .

>> l = list(filter(lambda x: x > 10 and x < 80, l))
"""
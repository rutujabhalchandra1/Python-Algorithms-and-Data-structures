import re
def check_valid(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False
    if re.match("^(A-Za-z0-9_-)*$", username) and re.match("^(A-Za-z0-9)", website) and len(extension) == 3:
        return True
    return False
n = int(input())
emails = [input() for i in range(0,n)]
valid = list(filter(check_valid, emails))
print(sorted(valid))
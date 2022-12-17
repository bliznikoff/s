

def truncate(text, index):
     res = text[:index] + '...'
     return res

print(truncate('hexlet',2))
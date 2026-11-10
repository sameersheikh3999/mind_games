

if __name__ == '__main__':

    s = input()
    r=""
for char in s:
    if char.isupper():
        r+=char.lower()
    else:
        r+=char.upper()

print(r)
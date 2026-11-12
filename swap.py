def swap_case(s):
    
    r=""
    for char in s:
        if char.isupper():
            r+=char.lower()
        else:
            r+=char.upper()
    print(r)
        
    
    
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
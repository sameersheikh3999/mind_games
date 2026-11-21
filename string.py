def count_substring(string, sub_string):
    c=0

    for i in range(0, len(string)):
        j=i%len(string) 

       
    

        if string[i]==sub_string[j]:
                c=+1
                
    return c


if __name__=="__main__":
    string=input().strip()
    sub_string=input().strip()

    count=count_substring(string, sub_string)
    print(count)

print("I am trying to solve this problem right now")
print("Still not solved")
print("things it up")
print("Now do something new")
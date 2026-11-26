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

print("Now, this is the time to practice, and do something that I like")
print("Now go for the second commit")
print("Now go for the third commit")
print("Do something commit")
print("Now is the time to learn and hit my earning potential")
print("Some additional work and effort might help")
print("Now another day, need to gather my thoughts and learn somehting valid")
print("Now doing this for another contribution")
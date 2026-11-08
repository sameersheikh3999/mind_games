if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        command=input().split()
        a=command[0]
        

        if a=="insert":
            arr.insert(int(command[1]),int(command[2]))
        elif a=="append":
            arr.append(int(command[1]))
        elif a=="remove":
            arr.remove(int(command[1]))
        elif a=="print":
            print(arr)
        elif a=="sort":
            arr.sort()
        elif a=="pop":
            arr.pop()
        elif a=="revers":
            arr.reverse()


        

if __name__ == '__main__':

    n=int(input())
    students=[]

    if n>=2 and n<=5:

     
        for _ in range(n):
            name = input()
            score = float(input())

            students.append([name,score])


for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][1] > students[j][1]:
            students[i], students[j] = students[j], students[i]


print(students[1])

print("Something needs to change right now")
            
      
       

    




        



                         
            
                
if __name__ == '__main__':

    n=int(input())
    students=[]

    if n>=2 and n<=5:

     
        for _ in range(n):
            name = input()
            score = float(input())

            students.append([name,score])


students.sort(key=lambda x: x[1])
print(students[1])
            
      
       

    




        



                         
            
                
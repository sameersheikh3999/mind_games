if __name__ == '__main__':

    n=int(input())
    unique_scores=set()
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




for i in range(len(students)):
    unique_scores.add(students[i][1])

unique_scores=list(unique_scores)

second_lowest=unique_scores[1]


names=[]
for i in range(len(students)):
    if students[i][1]==second_lowest:
        names.append(students[i][0])

names.sort()
for i in range(len(names)):
    print(names[i])
                         


print("This solution has been sorted")

print("One more addition")


print("We need more of that")


print("something contributing in the text")
            
                
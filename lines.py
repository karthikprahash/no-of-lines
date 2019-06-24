# no-of-lines
i=str(input())
if len(i)<=1000:
    
    count=1
    for x in range(len(i)):
        if(i[x]=='.'):
            count+=1
    print(count)

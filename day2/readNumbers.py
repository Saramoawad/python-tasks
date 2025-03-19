def readNumbers():
    total=count=0
    while True:
        num=input("enter a number or 'done' to finish: ")
        if num=="done":
            break
        try:
            num=int(num)
            total+=num
            count+=1
        except ValueError:
            print("error,please enter invalid number")
    average=total/count if count else 0
    return total,count,average
print(readNumbers())
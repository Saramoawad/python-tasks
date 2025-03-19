numbers=[]
for i in range(5):
    num=int(input(f"enter number  {i+1} :"))
    numbers.append(num)
   #numbers +=num
print("ascending:" ,sorted(numbers))
print("descending:" , sorted(numbers , reverse=True))
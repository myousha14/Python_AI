# for loop
# print table of any number
# number=int(input("Enter the number : "))
# for i in range(1,11):
#     print(number," * ",i," = ",number*i)

# while loop
i=1
while i<50:
    if i%5==0: # it skip divisible by 5 value
        i=i+1
        continue
    print(i)
    i=i+1

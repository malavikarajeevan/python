# i=1
# while i<=10:
#     print(i)
#     i+=1
# i=1
# while i<=9:
#     print(i)
#     i+=2
# i=0
# while i<=10:
#     print(i)
#     i+=2
# i=9
# while i>=1:
#     print(i)
#     i-=2
# i=10
# while i>=1:
#     print(i)
#     i-=2
# i=10
# while i>=1:
#     print(i)
#     i-=2
# for i in range(1,10):
#     print(i,end="")
# for i in range(2,10,2):
#     print(i,end="")
# for i in range(1,10,2):
#     print(i,end="")
# for i in range(2,22,2):
#     print(i,end="")
# a=int(input("enter starting range:"))
# b=int(input("enter ending range:"))
# s=sum(range(2,b,a+1))
# print("sum =",s)

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("\n")

# ls=[]
# for i in range(2,100,2):
#     ls.append(i)
# print(ls)
# ls=[]
# for i in range(1,101):
#     if i%3==0:
#        i="fizz"
#     ls.append(i)
# print(ls)

# ls=[]
# for i in range(1,101):
#     if i%5==0:
#         i="buzz"
#     ls.append(i)
# print(ls)

# ls=[]
# for i in range(1,101):
#     if i%3==0 and 1%5==0:
#       ls.append("fizzbuzz")
#     elif i%3==0:
#        ls.append("fizz")
#     elif i%5==0:
#         ls.append("buzz")
#     else:
#         ls.append(i)
# print(ls)

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print("\n")

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print("\n")
# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("\n")


# even,odd=0,0
# for i in range(1,10):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("even number in the list",even)
# print("odd number in the list",odd)

#
# for i in range(0,6):
#         if (i==3 or i==6):
#                 continue
#         print(i,end="")

# i,j=0,1 #fibinocci
# while j<50:
#         print(j)
#         i,j=j,i+j


# for i in range(0,4):
#     for j in range(0,4-i-1):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print("* ",end="")
#     print("\n")

"""q6"""
# for i in range(0,3):
#     for j in range(0,3-i-1):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print("* ",end="")
#     print("\n")
# for i in range(0,3-1):
#     for j in range(0,i+1):
#         print("",end="")
#     for j in range(0,3-i-1):
#         print("* ",end="")
#     print("\n")

""""q9"""
# a=int(input("enter the number"))
# sum=0
# while a!=0:
#     sum=a%10
    
#     print(sum)



""""q10"""
# my_list=[1,5,6,9,18,43]
# for index in range(len(my_list)):
#     value=my_list[index]
#     print(index,value)
"""floyid triangle"""
# a=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a=a+1
#     print()

""""q5 two dimentional array"""

# row_num=int(input("enter number of rows:"))
# col_num=int(input("enter number of colums:"))
# multi_list=[[0 for col in range(col_num)]for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]=row*col
#     print(multi_list)      

                
        
        
        
                 
        
          



        
    
    
    
    
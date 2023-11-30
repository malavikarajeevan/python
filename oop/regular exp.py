# import re
# terms=" "
# x=re.findall(terms,"synnefo hello hello")
# x=re.split(terms,"synnefo hello hello")
# x=re.match(terms," hello synnefo")
# x=re.search(terms,"synnefo hello hello")
# print(x)


# import re
# terms='[A-Za-z0-9]'
# x=re.match(terms,"7aswanth")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
    
# import re
# terms='[a-z]......'
# x=re.match(terms,"aswanth")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
    
# import re
# terms='^aswanth'
# x=re.match(terms,"aswanthhhh")
# if x:
#     print("matched")
# else:
#     print("not matched")
    
    
    
# import re
# terms='aswanth$'
# x=re.search(terms,"aswanth")
# if x:
#     print("matched")
# else:
#     print("not matched")

    
# import re
# terms='aswanth?'
# x=re.match(terms,"aswanthhh")
# if x:
#     print("matched")
# else:
#     print("not matched")


    
# import re
# terms='aswanth*'
# x=re.match(terms,"aswan")
# if x:
#     print("matched")
# else:
#     print("not matched")


    
# import re
# terms='aswanth+'
# x=re.match(terms,"aswanth")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms="\d"
# x=re.match(terms,"8hello synafo")
# if x:
#     print("matched")
# else:
#     print("not matched")


# import re
# terms="^[^h]ello"
# x=re.search(terms,"hello synafo")
# if x:
#     print("matched")
# else:
#     print("not matched")

# import re
# terms="^[5-9]\d{9}$"
# x=re.search(terms,"5678902559")
# if x:
#     print("validate")
# else:
#     print("not validate")


"""""user input"""
# import re
# username=str(input("enter your username: "))
# terms="^[a-zA-Z]\w{3,10}$"
# x=re.search(terms,"username")
# if x:
#     print("validate")
# else:
#     print("not validate")


"""calander"""
# import re

# terms="^([012]\d|3[01])(-|.|/)([0]\d|1[012])(-|.|/)(\d{4})$"
# x=re.search(terms,"23/12/2022")
# if x:
#     print("validate")
# else:
#     print("not validate")



import re
day=str(input("enter the date:"))

terms="^([^00]|[0][1,9]|[12][1,9]|3[1]|[123][0])(-|.|/)([^00]|[0][1,9]|[012])(-|.|/)([^0000]\d{4})$"
b=re.search(terms,"11/11/0000")
if b:
    print("validate")
else:
    print("not validate")



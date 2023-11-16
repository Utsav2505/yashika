# myset=['geeks','for']  
# print(myset)
# myset=['for','geeks']
# print(myset)


# print(3 or 0)
# a="yashika"
# b="yashika1"
# print(a is b)


# a={1,2}
# b={1,2}
# print(a == b)

# print("\r    yashika")


# print("yashika")
# print()
# print()
# print("hello")

# def fun():
#     S = 0
 
#     for i in range(10):
#         S += i
#         yield S
 
 
# print(fun())

# import math 
# print(math.factorial(10))


# a = 4
# b = 2
# try:
# 	k = a//b 
# 	print(k)

# except ZeroDivisionError:
# 	print("Can't divide by zero")

# finally:
# 		print('This is always executed')

# print("The value of a / b is : ")
# assert b != 0, "Divide by 0 error"
# print(a // b)

# temp = "geeks for geeks"
# if temp == "geeks":
# 	raise TypeError("Both the strings are different.")

# print("yashika")


# lst=[1,2,3]
# del lst[0]
# print(lst)

# var1=10
# def fun():
#     var2=3
#     def gun():
            
         
#         var = var2 + 10
#         print(var)
 
#     gun()
# fun()


# print("yashika")print("aggarwal")

# s={2+3+4*
#   5}
# print(s)

# f=4+5+\
# 6
# print(f)
# '''yashika'''
# print("gamma")

# print("yashika".split("s"))

# x = [int(x) for x in input("Enter multiple values: ").split()]
# print("Number of list is: ", x)

# l={1,2,3,4,5,6,7}
# print(*l)

# print('yashika'.split())

# python program to demonstrate the use of "/"
# print(5/5)
# print(10/2)
# print(-10/2)
# print(20.0/2)
# print(10/3)

# print(-4/2)
# print(4/-2)
# print(-4/-2)
# print(4.0//2)
# print(4.0//2.0)
# print(-4.0//2)
# print(4.0//-2.0)
# print(-4.0//-2.0)
# print(4.0//-2)
# print(4//2.0)
# print(5//-2.0)
# print(5//-2)

# a=None
# b=[]
# print(id(a))
# print(id(b))
# print(None == [])

# print(2.0**9)

# for i in {1,2,3,4}:
#     print(i)

# print(4*3//2)

# import operator
# l=[1,2,3,4,5]
# operator.delitem(l,slice(1,3))
# print(l)

# l1={1:'a',2:'b'}
# l2={3:'c',4:'d'}
# l3=l1+l2
# print(l3)

# a='''she\n 
# is
# a fantastic girl'''
# print(a)

# for i in {1,2,3}:
#     print(i)

# print('+'.join('yash1ka'))

# l=['a','b','c','d']
# print(type("*".join(l)))

# b= " geeks "
# print("$".join(b))

# words = ["apple", "", "banana", "cherry", ""]
# separator = "@ "
# result = separator.join(word for word in words if word)
# print(result)
# print([word for word in words if word])
# print(type(words))

# for word in words:
#     if word:
#         print(bool(word))
# print(bool("apple"))
# print(bool(""))
# print("apple"and  "banana")
# print(""==False)

# print(bool(10e12))
# print(type(range(1,6)))

# print([1,2,3])
# a=list(reversed("yashika"))
# print(a)

# a="bottle"
# print(a[-1:0:-1])

# String1 = "Hello, I'm a Geek"
# print(list(String1))

# print(''.join(list[range(1,5)]))

# String1 = "I\'m a \"Geek\""
# print(String1)

# print(R"yash\n")
# print("hello")

# print("{p} is my {f} {}".format("place",p="Rajasthan",f="favorite"))

# print("uni\\corn")
# print("uni\corn")

# print('''fascinated''string''')
# print("invading a \' country")
# print("invading a \\' country")

# l=[1,2,3,4]
# print("heart wants {}".format({1:"python",2:"JS",3:"Matlab"}))
# print(l)

# print("n\
# m\
# ste")

# print("%s is so useful. I tried to look\
# up mobile and they had a nice one that cost %f rupees." % ("Amazon",12000.5))

# print("%100s" %'geeksforgeeks')

# print(repr("yash"))

# print(not('yash'))


# from string import Template
# # t = Template('x is $$$$${x}')
# # print (t.substitute(x=1))

# stu=[("tarun",20),("raju",18),("nityam",17)]
# t=Template("hi ${name}, u have got ${marks} marks")
# for i in stu:
#     print(t.template)

# print(type(repr(1)))

# a="yashika"
# print(a.find("tu"))

# using for loop:- 

# n=1
# def empty(str,sub_str):
#     global n
#     i=str.find(sub_str)
#     if i!=-1:
#         count=i
#         for j in (sub_str):
#             count+=1
#         str=str[0:i]+str[count:]
#         print(f"str after {n} elimination",str)
#         n+=1
#         empty(str,sub_str)
#     elif str=="":
#         print("yes!string can be emptied")
#     else:
#         print("sorry!string cannot be emptied")
# empty("geegeekssk","geeks")


# string="yashika"
# sub_str="yash"
# string = string.replace(sub_str, "")
# print(string) 

# import re
# string="yashika"
# sub_str="yash"
# string=re.search(sub_str,string)
# print(string) 


# using while loop:-

# n=1
# def empty(str,sub_str):
#     global n
#     i=str.find(sub_str)
#     if i!=-1:
#         count=i
#         j=1
#         while (j<=len(sub_str)):
#             count+=1
#             j+=1
#         str=str[0:i]+str[count:]
#         print(f"str after {n} elimination",str)
#         n+=1
#         empty(str,sub_str)
#     elif str=="":
#         print("yes!string can be emptied")
#     else:
#         print("sorry!string cannot be emptied")
# empty("geegeeksks","geeks")


# print("geeksforgeeks".count("g"))

# str=input("enter your string: ")
# str1=list(str)

# for i in str1:
#     print(str1)
#     count=0
#     c=str1.index(i)
#     for j in str1[c:]:
#         if j==i:
#             count+=1
#     print(f"Appearance of {i} in string {str} is {count} times")
#     for a in str1:
#         if a==i:
#             str1.remove(i)



# str=input("enter your string: ")
# str1=str
# print("repeated elements are: ",end="\n")
# for i in str1:
#     count=0
#     c=str1.find(i)
#     for j in str1[c:]:
#         if j==i:
#             count+=1
#     if count>1:
#         print(i,end=",")


# str=[1,2,3]
# str1=str
# print(str1 is str)
        

# dict={1:"apple",2:"banana",3:"orange"}
# print(dict.items())


#using for loop
# ele=[]
# dict={}
# str=input("enter your string: ")
# print("all repeated elements of your string are:")
# for r in str:
#     if r not in dict:
#         dict[r]=1
#     else:
#         dict[r]+=1
# for char,count in dict.items():
#     if count>1:
#         ele.append(char)
#         print(f"{char} appears {count} times")
#     if count==1:
#         print(f"{char} appears only {count} times")

#using while loop
# ele=[]
# dict={}
# str=input("enter your string: ")
# print("all repeated elements of your string are:")
# c=0
# while c<len(str):
#     r=str[c]
#     if r not in dict:
#         dict[r]=1
#     else:
#         dict[r]+=1
#     c+=1
# c1=0
# while c1<len(dict.items()):
#     char,count=list(dict.items())[c1]
#     if count>1:
#         ele.append(char)
#         print(f"{char} appears {count} times")
#     if count==1:
#         print(f"{char} appears only {count} times")
#     c1+=1


# from collections import Counter
# str=input("enter your string: ")
# print("all repeated elements of your string are:")
# dict=Counter(str)
# for char,count in (dict.items()):
#     if count>1:
#         print(char)


# ele=set()
# str=input("enter string: ")
# print("repeated elements are: ")
# for r in str:
#     count=str.count(r)
#     if count>1:
#         ele.add(r)
# print(ele)


# lst=[]
# str=input("enter string: ")
# print("repeated elements are: ")
# for r in str:
#     if r not in lst:
#         count=str.count(r)
#         if count>1:
#             lst.append(r)
# print(lst)

# lst="yashika"
# lst.reverse()
# print(lst)

#using for loop
# str=input("enter your string: ")
# for i in str[::-1]:
#     print(i,end="")

#using while loop
# str=input("enter ur string: ")
# l=len(str)
# i=l-1
# while (i>=0):
#     print(str[i],end="")
#     i-=1

# str=input("enter ur string: ")
# s=""
# for i in str:
    
#     s=s+i
#     print(s)
# print(s) 

# def reverse(s):
#     str = ""
#     for i in s:
#         print(str)
#         str = i + str
#     return str

# print(reverse("yashika"))

# print("a"[4:])

# str=input("enter ur string: ")
# lst=list(str)
# print(lst.pop())
# str1=""
# "a".join(str1)
# for i in (0,len(lst)):
    


# print(str1)
# lst=['a','b']
# 'a'.join(lst)

# str=input("enter ur string: ")
# lst=list(str)
# str1=[]
# print(lst)
# for i in (0,len(lst)):
#     # str1.append(lst.pop())
#     print(lst.pop())
# print(str1)

# str=input("enter the string: ")
# lst=list(str)
# str1=tuple(reversed(lst))
# print(("").join(str1))

# str=input("enter string: ")
# l=len(str)
# for i in (0,(l//2)-1):
#     if str[i]!=str[l-1-i]:
#         print("no")
#         break
#     if (i==l//2-1 ):
#         print("yes")

# s="YAshika"
# print(s.upper())
# print(s)


# l=[]
# m=[4,5,6]
# l.extend(m)
# print(l)

# import string
# import random
# print(type(string.digits))

# l=list(string.ascii_letters + string.digits)
# print(random.choice({1:'a',2:'b',3:'c'}))



# import string
# import random
# def passwd(size,word):
#     l=[random.choice(word) for i in range(size)]
#     passw=''.join(l)
#     return passw

# size=int(input("enter lenght of passwd u want: "))
# word=input("enter the word: ")
# password=passwd(size,word)
# print(password)


# import string
# print("yashika".letter)

# text="geeks for geeks."
# result = text.endswith(('@','_'))
# print(result)

# for i in range (1,10000,):
#     print(chr(i),end=", ")
# # print(ord('⚽'))
# print(chr(9917))

# newstring=""
# count=0
# for i in range(100):
#     b=chr(i)
#     if b.isdigit()==True:
#         count+=1
#         newstring+=b
# print("total digits in range are: ",count)
# print("digits are: ",newstring)

# print(type(ord("⚽")))

# print("iv".isdigit())
# print("iv".isnumeric())

# ch="geeksforgeeks"
# print(ch.find("geeks",2,10))

# print("yashika".title())


# count=0
# str=input("enter the string: ")
# for a in str:
#     if a.isspace()==True:
#         count+=1
# print(count)

# string =" \n\v\t"
# for a in string:
#     if (a.isspace()) == True:
#         count+=1
# print(count)

# t1=[12,3,45]
# t2=t1

# print(t1 is t2)
# t1.append(4)
# print(t1)
# print(t2)

# print("grrksforgrrks".replace('r','e',1))

# my_string = "geeks for geeks "
# old_substring = "k"
# new_substring = "x"
  
# split_list = my_string.split(old_substring)
# new_list = [new_substring if i < len(split_list)-1 else '' for i in range(len(split_list)-1)]
# new_string = ''.join([split_list[i] + new_list[i] for i in range(len(split_list)-1)] + [split_list[-1]])

# print(new_string)

# print('2/3'.isdigit())

# string = "b follows a, c follows b"
# print(string.partition('follows'))

# url = "https://www.example.com/index.html"
# result = url.partition("//")
# result = result[2].partition("/")
# print(result[0])

# string = "101001010"
# print(string.rindex('101', 2))

# print(max("aA"))
# print(min("a/"))
# print(ord("a"))
# print(ord("A"))
# print(ord('/'))

# str="Welcome everyone to\rthe world of Geeks\nGeeksforGeeks\r"
# print(str.splitlines(1.2))
# print(str.splitlines(1))
# print(str.splitlines(3))

# print(bool(19.99))
# s1=[1,2,3]
# s2=s1
# s1=s1.append(5)
# print(s2)
# print(s1 is s2)

# print(int(12.9))
# print(bool(0.000))


# s1=[1,2,3]
# s2 = s1
# print(s1 is s2)
# s1=[2,3]
# print(s1)
# print(s2)
# print(s1 is s2)

# print('\nIndia\nJapan\nUSA\nUK\nCanada\n'.splitlines())

# str=input("enter string: ")
# s1=str
# c=0
# print(s1.splitlines())
# print(l)
# for i in l:
#     c+=len(i)
# print(c)

# print("1yashika aggarwal".title())


# str="\t\tyashika\t\taggarwal"
# print(str.expandtabs(1.1))

# word="geeks for geeks"
# print(word.find('for ', 4, 11))
# print(word.find('g', 4, 10))
# print(word.index('geeks', 2))


# string="geeks for geeks"
# print(string.count("yashika", 0, 15))

# text = 'G3Ek5 F0R gE3K5'

# print("Original String:")
# print(text)

# lower() function to convert
# string to lower_case
# print("\nConverted String:")
# print(text.lower())

# s="gEEksfORgeeKS"
# print(s.lower())
# print(s.casefold())
# print(s.swapcase())

# s1="GEEKSFORGEEKS"
# print(s1.casefold())

# string = "one,two,three"
# words = string.rsplit(',',1)
# print(words)

# print(string.partition('are'))
# print(string.rpartition('are'))
# print(string.splitfields())
# Example of a TypeError when calling splitfields()
# num = {'a','b','c'}
# fields = num.splitfields(",")

# def func():
#     for i in "yashika":
#         yield(i)

# print(type(range(10)))
# str= '.'.join()
# print(str)

# l=[ word for word in func()]
# print(l)

# print('.'.join(i for i in 'yashika'))
# print(type(for i in 'yashika'))

# list1 = " geeks "
# print("$".join(list1))

# s={'1','2','3','4'}
# print('#'.join(s))

# str='@hello world!'yy
# print(str.strip('@h!d'))

# str="as is handy"
# print(str.strip())

# str=' hello world!'
# print(str.strip('!'))

# string = " geeks for geeks "
# print(string)
# print(string.strip())
# print(string.strip(' geeks'))

# str='geeks for geeks'
# print(str.strip('ekgs'))

# string = "\\'Hello, World!\n"
# new_string = string.strip()
# print(new_string)
# # print(string)

# str=' hello yashika! '
# print(str.lstrip())

# d={103:1,101:None,101:None}
# d={'a':'apple','b':'ball'}
# str="geeks"
# print(str.translate(d))
# print(chr(103))
# print(chr(119))
# print(chr(121))
# print(chr(117))
# print(chr(103))
# print(chr(102))

# print(str)
# table=str.maketrans('aeiou','12345')
# print(table)

# print(chr(97))
# print(chr(49))
# print(chr(101))
# print(chr(50))
# print(chr(105))
# print(chr(51))
# print(chr(111))
# print(chr(52))
# print(chr(117))
# print(chr(53))


# print(ord('g'))
# print(ord('e'))
# print(ord('k'))
# print(ord('s'))
# print(ord('f'))


# firstString = "gef"
# secondString = "eks"
# thirdString = "ge"
# string = "geeks"
# print("Original string:", string)
# translation = string.maketrans(firstString,secondString,thirdString)
# print("Translated string:",
# 	string.translate(translation))
# print(translation)

# import string
# print(type(string.punctuation))

# print('yas234'.upper())
# l=8
# st='geeks'
# print(st.rjust(l))

# number = "6041"
# print(number.zfill(8))
# print(type(number))
# number = "+6041"
# print(number.zfill(8))
# print(type(number))
# text = "--anything%(&%(%)*^"
# print(text.zfill(20))
# print(type(number))

# st1= "helloABworld"
# st2 = "fghABsdfABysu"
# print(st1.replace('AB','C'))
# print(st2.replace('AB','C',1))


# def rep(s):
	
# 	for i in range(1, len(s)) :
# 		if (s[i - 1] == 'A' and s[i] == 'B') :
# 			s[i - 1] = 'C'
			
# 			for j in range(i, len(s) - 1) :
# 				s[j] = s[j + 1]
				
# 			s[len(s) - 1] = ''
				
# 	return
# st = list("helloABworldABGfG")
# rep(st)
# print("The modified string is :")
# print(''.join(st))

# s='yashika'
# def er():
    
#     s=s+' aggarwal'
#     print(s)
 
# er()
# print(s)


# s=[1,2,3]
# def er(s):
#     print(s)
#     s[0]=5
#     print(s)
# er(s)
# print(s)

# def rep(s):
#     i,j=0,0
#     while (i<len(s)):
#         if (s[i]=='A' and s[i+1]=='B'):
#             s[i]='C'
#             j=i+1
#             while j<(len(s)-1):
#                 s[j]=s[j+1]
#                 j+=1
#             s[len(s)-1]=""
#         i+=1

# s=list("helloABworldAByashika")
# print(s)
# rep(s)
# print(''.join(s))


# string = "ß"
# print("Using lower():", string.lower())
# print("Using casefold():", string.casefold())

# l={[1,2],45,67,4}
# print(l)

# i=0
# while i<10:
#     a=int(input("enter integer: "))
#     print("Okay")
#     i+=1
# print("yashika")    

# l=[1,2,3,4,5]
# print(l.sum())

# l=[1,2,3,1,2,1,2,3,2,1]
# print(l.index(2,3))
# print(l.index(3,2))

# l=['z','b','#','d']
# print(min(l))
# print(ord('#'))

# print('b'<'ashika')

# print(ord('1'))
# l='yashika'
# l.sort(reverse=True)
# print(type(sorted(l)))
# l.pop(10)
# a=del l
# print(a)

# t=[1,2,3]

# l=[4,5,6]
# l.append(t)
# print(l)

# l=[4,3,5,6,'y',2,'k']
# l.reverse()
# print(l)

# l=[1,1,2,3,1,4,1,66]
# l.pop(4)
# print(l)
# print(l[6:13])


# List = ['G', 'E', 'E', 'K', 'S', 'F','O', 'R', 'G', 'E', 'E', 'K', 'S']

# Sliced_List = List[:-6]
# print(Sliced_List)

# Sliced_List = List[-6:-1]
# print(Sliced_List)

# Import required module
# import time


# define function to implement for loop
# def for_loop(n):
# 	result = []
# 	for i in range(n):
# 		result.append(i**2)
# 	return result


# # define function to implement list comprehension
# def list_comprehension(n):
# 	return [i**2 for i in range(n)]


# # Driver Code

# # Calculate time taken by for_loop()
# begin = time.time()
# for_loop(10**6)
# end = time.time()

# # Display time taken by for_loop()
# print('Time taken for_loop:', round(end-begin, 2))

# # Calculate time takens by list_comprehension()
# begin = time.time()
# list_comprehension(10**6)
# end = time.time()

# # Display time taken by for_loop()
# print('Time taken for list_comprehension:', round(end-begin, 2))

# import time
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())

# print(round(9.88999,5))

# print(zip("apple","yashika"))

# names = ["G", "G", "g"]
# ages = [25, 30, 35]
# person_tuples = [(name, age) for name, age in zip(names, ages)]
# print(person_tuples)

# for name, age in zip(names, ages):
#     print(name,age)

# print(zip(names, ages))

# List = [367, 111, 562, 945, 6726, 873]
# for l in List:
#     if l&1:
#         print(l)

# print(List.count("yashika"))

# lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
# print (dict( (l, lst.count(l) )for l in set(lst)))

# import copy
# l1=[1,[2,3],4]
# l2=copy.copy(l1)
# l3=copy.deepcopy(l1)
# l2.append(5)
# l3.append(6)
# print(l1)
# print(l2)
# print(l3)
# l4=l1
# l4.append(7)
# l3=l1[:]
# l3[1][1]=7
# l3.append(8)
# print(l1)
# print(l3)

# l = [1,-3,0,2,4]
# print([ele > 0 for ele in l])

# print(all([]))
# print(abs(-4))
# print(abs(4))
# print(abs(-4.613748))
# l = {"t":1, "i":1, "m":2, "e":0}
# print(type(l.values()))

# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"
  
# creating enumerate objects
# obj1 = enumerate(l1)
# obj2 = enumerate(s1)
# print(obj1)
# print ("Return type:", type(obj1))

# string_list = ["Geeks", "for", "Geeks"]

# max_val = max(string_list)
# print(max_val)
# print(ord('f'))
# print(ord('G'))

# arr = ["a"]
 
# start parameter is not provided
# Sum = sum(arr)
# print(Sum)

# Python code to demonstrate the practical application
# of sum()

# numbers = [1,2,3,4,5,1,4,5]

# start = 10
# Sum = sum(numbers)
# average= Sum/len(numbers)
# print (average)

# x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
# print(x)

# my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
# print(list(enumerate(my_dict,5)))

# s1={1,2,3}
# s2={4,5,6}
# print(s1^s2)
# s.update({4,5,6})
# print(s)

# print(type({}))
# dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
# print(dict1.get("kotlin"))

# import array

# Create an array of integers
# my_array = array.array('i', [1, 2, 3, 4, 5])

# Print the original array
# print("Original array:", *my_array)

# Reverse the array in place
# my_array.reverse()

# Print the reversed array
# print("Reversed array:", my_array)

# t1=[1,2,3,4,5]
# t1.remove(6)


# def maxinstance(s):
#     s1=list(s)
#     count=0
#     try:
#         while(len(s)>0):
#             for i in "balloon":
#                 s1.remove(i)
#             count+=1
#     except:
#         print("No. of occurences of balloon in given string are: ",count)

# s=input("enter string: ")
# maxinstance(s)

# l=['yash','tish',"mug"]
# print(max(l,key=len))

# def longeststring(s):
#     s1=s.split()
#     s2=set()
#     s3=s1[0]
#     for i in s1:
#         if len(i)>len(s3):
#             s3=i
#             s2={i}
#         elif len(i)==len(s3):
#             s2.add(i)
#     print(min(s2))

# s=input("enter your string: ")
# longeststring(s)

# d={'a':1,'b':2,'c':3,'d':4,'e':5}
# print(d.get('f',5))
# from collections import Counter
# s="wonderfull"
# s1=Counter(s)
# print(s1)


# import math,random
# l=int(input("enter lower limit: "))
# u=int(input("enter upper limit: "))
# x=random.randint(l,u)
# f=math.ceil(math.log((u-(l+1)),2))
# print("you have only {} chances".format(f))
# count=0
# ans=input("do you want to play?(y/n)")
# if ans=="y":
#     while(count<=f):
#         try:
#             a=int(input("guess the no.: "))
        
#             if a==x:
#                 print(f"you won at {count+1} attempt!!")
#                 break
#             elif count==f:
#                 print("better luck next time.")
#             count+=1
#         except: 
#             print("enter only integer guesses")
#         print(f"wrong! you are left with {f-count} chances")
#         ans=input("do you want to continue?(y/n)")
#         if ans=="n":
#             break
# print("thanks for playing :)")        

# n=33
# i=n
# while (i>1):
#     print(i)
#     i=i/2

# for i in range(7):
    # print("gfg")
   

# i=33
# while i>1:
#     i/4

# def fun(n):
#     if n ==1:
#         return
#     for i in range(n):
#         print("gfg")
#     fun(n//2)
#     print("hello")
#     fun(n//2)
#     print("hi")
# print(fun(7))

# print(367 & 1)
# print(111 & 1)
# print(562 & 1)
# print(945 & 1)

# print(6726 & 1)
# print(873& 1)

# l=[367,]
# python code to demonstrate working of enumerate()

# for key in enumerate(('The', 'Big', 'Bang', 'Theory')):
# 	print(key)

# python code to demonstrate working of zip()

# initializing list
# questions = {'a','b','c'}
# answers = ["d",'e']
# using zip() to combine two containers
# and print values
# for question in zip(questions, answers):
# 	print(question)

# s = {'a':1,'b':2,'c':3}
# print(type(s.items()))
# for i in s.items():
#     print(i)
# print(s.items())
# s=['a','f','h','t']
# print(set(reversed(s)))

# def myFun(*argv):
# 	print(argv)
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# def myFun(**kwargs):
# 	print(kwargs)
# myFun(first='Geeks', mid='for', last='Geeks')

# def myFun(arg1, arg2, arg3):
# 	print("arg1:", arg1)
# 	print("arg2:", arg2)
# 	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# print(type(*args))

# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# print(**kwargs)

# def fun():
#     for i in range(5):
#         print("hello")
#     return "yashika"
# 	print("toshima")

# fun()

# A Simple Python program to demonstrate working
# of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time


def simpleGeneratorFun():
	
	yield 1
	yield 2
	yield 3


# print(simpleGeneratorFun())

# Driver code to check above generator function
# for value in reversed(simpleGeneratorFun()):
# 	print(value)

# generator expression
# generator_exp = {i * 5 for i in range(5) if i%2==0}

# for i in generator_exp:
# 	print(i)
# print(type(generator_exp))

# l = [1, 2, 3]
# l_iter = iter(l)
# print(next(l))
# print(type(l_iter))
# import time
# print(time.time_ns())

# print("yashika".split())

# def fact(n):
# 	five=0
# 	f=1
# 	for i in range (n,0,-1):
# 		i2=i
		
# 		while True:
# 			if i2%5==0:
# 				five+=1
# 				i2/=5
# 			else:
# 				break
# 		f=f*i
# 	print("factorial is",f)
# 	print("trailing zeroes are: ",end="")
# 	return five

# print(fact(10))


# import math
# def fac(n):
# 	x=math.floor(math.log(n,5))
# 	print(x)
# 	zero=0
# 	for i in range(1,x+1):
# 		zero+=math.floor(n/(math.pow(5,i)))
# 	return zero

# print(fac(24))

# def gcd(*args):
# 	print(args)
# 	x=min(args)

# 	for i in range(x,0,-1):
# 		# print(i)
# 		if (all(j%i==0 for j in args))==True:
# 			return i

# try:
#         n = int(input("Enter the number of integers you want to calculate the GCD for: "))
#         if n < 2:
#             print("Please enter at least 2 integers.")
#         else:
#             integers = []
#             for i in range(n):
#                 num = int(input(f"Enter integer {i + 1}: "))
#                 integers.append(num)

#             result = gcd(*integers)
#             print(f"The GCD of the given integers is: {result}")
# except ValueError:
#         print("Invalid input. Please enter valid integers.")


# def gcd(a,b):
# 	while a!=b:
# 		if a>b:
# 			a=a-b
# 		else:
# 			b=b-a
# 	return a

# def gcd(a,b):
# 	if b==0:
# 		return a
# 	return gcd(b,a%b)

# print(gcd(6,7))

# def lcm(a,b):
# 	x=max(a,b)
# 	y=min(a,b)
# 	s=0
# 	while True:
# 		s=s+x
# 		if s%y==0:
# 			return s
		
# print(lcm(2,6))

# def pri(n):
# 	n1=n
# 	for i in range(n1-1,0,-1):
# 		if (n1%i==0) and i!=1:
# 			return "no"
# 	return "yes"

# print(pri(101))

# string = 'GeeksforGeeks'

# lambda returns a function object
# print((lambda s: s)(string))


# l= ["1", "2", "9", "0", "-1", "-2"]
# calc=(lambda x: not (int(x) % 2 == 0 and int(x) > 0))
# print(list(filter(calc,l)))


# c=(x for x in range(1,10))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# function that filters vowels
# def fun(variable):
# 	letters = ['a', 'e', 'i', 'o', 'u']
# 	if (variable in letters):
# 		return True
# 	else:
# 		return False

# sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# using filter function
# filtered = filter(fun, sequence)
# print(type(filtered))
# print(list(filtered))
# print('The filtered letters are:')
# for s in filtered:
# 	print(s)


# Python program to demonstrate working
# of map.

# Return double of n
# def addition(n):
# 	return n + n
# We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# Add two lists using map and lambda

# numbers1 = [1, 2, 3,2]
# numbers2 = [4, 5, 6,8]

# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))


# def prime(n):
# 	if n==1:
# 		return False
# 	elif n==2 or n==3:
# 		return True
# 	elif (n%2==0) or (n%3==0):
# 		return False
# 	i=5
# 	while (i*i<=n):
# 		if (n%i==0) or (n% (i+2)==0):
# 			return False
# 		i+=6
# 	return True


# def prime(n):
# 	if n==1:
# 		return False
# 	i=1
# 	while (i*i<=n):
# 		if (n%i==0):
# 			return False
# 		i+=1
# 	return True

# i=2
# while (i*i<=1001):
# 	if 1001%i==0:
# 		break
# 	print(i, end=",")
# 	i+=1
	
 
# print(1001%3==0)

# i=5
# while (i*i<=1001):
# 	if (1001%i ==0 or 1001% (i+1)==0):
# 		break
# 	print(i, end=",")
# 	i+=6



# def isprime(x):
# 	for i in range(2,x):
# 		if x%i==0:
# 			return True
# 	return False

# def pf(n):
# 	for i in range(2,n+1):
# 		if isprime(i):
# 			t=i
# 			while(n%t==0):
# 				print(i)
# 				t*=i

# def div(n):
# 	i=1
# 	while(i*i<=n):
# 		if n%i==0:
# 			print(i)
# 			if (i!=n/i):
# 				print(n//i)
# 		i+=1

# x=int(input("entr no.: "))
# div(x)

# def div(n):
# 	i=1
# 	while(i*i<n):
# 		if n%i==0:
# 			print(i)
# 		i+=1
# 	while (i>=1):
# 		if (n%i==0):
# 			print(n//i)
# 		i-=1

# x=int(input("entr no.: "))
# div(x)

# print(-(-32))

# def ab(n):
# 	if n<0:
# 		return(-n)
# 	else:
# 		return n
	
# x=int(input("enter integer: "))
# print(ab(x))

# print(-1<<32)
# print(list(120))


# import math
# n=5
# print(int(math.ceil(math.log10(math.factorial(n)))))


# def prime(n):
# 	if n==1:
# 		return False

# 	i=2
# 	while(i*i<=n):
# 		if n%i==0:
# 			return False
# 		i+=1
# 	return True

# print(prime(19))


# def div(n):
# 	t=[]
# 	while len(t)<3:
# 		i=1
# 		while(i*i<=n):
# 			if n%i==0:
# 				t.append(i)
# 				if len(t)==3:
# 					break
# 				if i!=n//i:
# 					t.append(n//i)
# 			i+=1
# 	for i in t:
# 		print(i)

# div(100)

# t=[]
# while len(t)<3:
# 	t.append(3)
# print(t)


# def div(n):
# 	t=set()
# 	i=1
# 	while(i*i<n):
# 		if n%i==0:
# 			if len(t)==3:
# 				break
# 			t.add(i)
				
# 		i+=1
# 	while (i>=1):
# 		if (n%i==0):
# 			if len(t)==3:
# 				break
# 			t.add(n//i)
				
# 		i-=1
# 	for i in t :
# 		print(i)

# x=int(input("entr no.: "))
# div(x)

# import math
# a=int(input("enter coeff. of x square: "))
# b=int(input("enter coeff. of : "))
# c=int(input("enter constant term: "))
# x1=x2="yasika"
# print(x1,x2)
# print((math.pow(10,9)+7))
# print(math.log2(15))

# print("050"=="050")
# print(5==True)

# def seq(n):
# 	if n==0:
# 		return 1
# 	return n+ n*seq(n-1)

# print(seq(3))

# def arrele(n,*args):
# 	if n==0:
# 		return
# 	print(args[0],end=" ")
# 	a=list(args)
# 	a.pop(0)
# 	arrele(n-1,*a)
# arrele(4,5,4,2,1)

# print(list(9995544))

# def sn(n):
# 	if len(list(str(n)))==1:
# 		return int(n)
# 	a=list(str(n))
# 	a1=a.pop(0)
	
# 	return int(a1)+sn((''.join(a)))

# print(sn(10001))

# def cn(n):
# 	if len(list(str(n)))==1:
# 		return 1
# 	a=list(str(n))
# 	a1=a.pop(0)
# 	print(a)
	
# 	return 1 + cn((''.join(a)))

# print(cn(10000))

# print(len(list("00000")))

# def comb(n,r):
# 	if r==0 :
# 		return 1
# 	elif n==0 :
# 		return 0
# 	elif r==1 and n>=0:
# 		return n
# 	elif (n<0) or r<0:
# 		return 
# 	return comb(n-1,r-1) + comb(n-1,r)

# print(comb(-1,1))


# def summ(n):
# 	if n<=0:
# 		return 0
# 	return n+summ(n-1) 

# print(summ(4))

# def gcd(a,b):
# 	if a==b:
# 		return a
# 	elif a==0:
# 		return b
# 	elif b==0:
# 		return a
# 	elif a>b:
# 		return gcd(a-b,b)
# 	else:
# 		return gcd(a,b-a)
	
# print(gcd(0,4))

# def gcd(a,b):
# 	if a==0:
# 		return b
# 	elif b==0:
# 		return a
# 	return gcd(b,a%b)

# print(gcd(2,3))

# def bs(x,*l):
# 	count=0
# 	for i in l:
# 		if i==x:
# 			return count
# 		count+=1
# 	return -1

# print(bs(20,10,30,40,50,60))
# t=(1,2,3,4)
# print(t[2:4])

# def bs(x,*l):
# 	s=len(l)
# 	mid=s//2
# 	start=0
# 	end=s-1
# 	if x==l[mid]:
# 		return mid
# 	elif x==l[end]:
# 		return end
# 	elif x==l[start]:
# 		return start
# 	elif x==l[end]:
# 		return end
# 	elif x<l[mid]:
# 		return bs(x,*l[mid+1:s])
# 	elif x>l[mid]:
# 		return bs(x,*l[0:mid+1])
	
# # print(bs(20,10,20,30,40))
# print([1,2,3,4].find(1))


# def bs(x,low,high,*l):
# 	if low>high:
# 		return
# 	mid =(low+high)//2
# 	if x==l[mid]:
# 		return mid
# 	elif x<l[mid]:
# 		return bs(x,low,mid-1,*l)
# 	else:
# 		return bs(x,mid+1,high,*l)
	
# print(bs(10,0,5,2,3,4,6,10,22))

# import math
# print(math.log2(10))

# def bs_1stocc(x,*l):
# 	low =0
# 	high =len(l)-1
# 	while (low<=high):
# 		mid=(low+high)//2
		
# 		if x==l[low]:
# 			return low
# 		elif x==l[mid]:
# 			return mid
# 		elif x>l[mid]:
# 			low=mid+1
# 		elif x<l[mid]:
# 			high =mid-1
# 	return -1

# print(bs_1stocc(15,10,15,15,16,5,15)) 


# def bs_1stocc(x,low,high,*l):
# 	if low>high:
# 		return -1
# 	mid =(low+high)//2
# 	if x==l[low]:
# 		return low
# 	elif x==l[mid]:
# 		return mid
# 	elif x<l[mid]:
# 		return bs_1stocc(x,low,mid-1,*l)
# 	else:
# 		return bs_1stocc(x,mid+1,high,*l)
	
# print(bs_1stocc(20,0,6,1,10,10,10,20,20,40)) 


# import math
# def sr(n):
# 	return math.floor(math.sqrt(n))

# print(sr(10))

# def peakele(*l):

# 	low=0
# 	high=len(l)-1
# 	while (low<=high):
# 		mid=(low+high)//2
# 		if low==high:
# 			return low
# 		elif l[mid]>l[mid-1] and l[mid]>l[mid+1]:
# 			return mid
# 		elif l[mid]<l[mid-1]:
# 			high=mid-1
# 		elif l[mid]<l[mid+1]:
# 			low=mid+1
# 	return -1


# print(peakele(10,9,6,7,6,5,1))
# print(min([1,3,4,5]))


# def peakele(low,high,*l):
# 	# if low>high:
# 	# 	return -1
# 	mid=(low+high)//2
# 	# print(mid)
# 	if l[mid]>l[mid-1] and l[mid]>l[mid+1]:
# 			return mid
# 	elif l[mid]<l[mid-1]:
# 		return peakele(low,mid-1,*l)
# 	elif l[mid]<l[mid+1]:
# 		return peakele(mid+1,high,*l)
	
# print(peakele(0,6,10,9,6,7,6,5,1))


# def floorele(x,*l):
# 	low=0
# 	high=len(l)-1
# 	while(low<=high):
# 		mid=(low+high)//2
# 		if l[mid]<=x and not(l[mid+1]<=x):
# 			return mid
# 		elif l[mid]<x and l[mid+1]<=x:
# 			low=mid+1
# 		elif l[mid]>x:
# 			high=mid-1
# 	return -1

# print(floorele(8,1,2,8,8,10,11,12,19))
	
# print("yashika"+"aggarwal")

# a = 15
# function to change a global value
# def change():
	# increment value of a by 5
	# b = a + 5
	# a = b
	# print(a)
# change()

# l=[10,20,30]
# def change():
# 	global l
# 	l=[20,30,40]

# print(l)
# change()
# print(l)

# import cfg
# cfg.x = 1
# cfg.y = 2
# cfg.z = "geeksforgeeks"

# Python program showing a use of
# global in nested function
# x=100
# def add():
# 	global x 
# 	def change():
# 		x=20
		
# 	print("Before making changing: ", x)
# 	print("Making change")
# 	change()
# 	print("After making change: ", x)

# add()
# print("value of x", x)

'''hi'''
# a=2
# print(a)

# Python program to illustrate functions
# Functions can return another function

# def create_adder(x):
# 	def adder(y):
# 		return x+y
# 	return adder
# add_15 = create_adder(15)
# print (adder(10))

# Python program to illustrate
# closures
# def outerFunction(text):
# 	def innerFunction():
# 		print(text)
# 	return innerFunction
# myFunction = outerFunction('Hey!')
# myFunction()

# d={1:2,3:4,5:6}
# print(*d)

# def deco(func):
# 	print('inside')
# 	def inner(*args,**kwargs):
# 		func()
# 	return print("yeah!")

# @deco
# def func_to():
# 	print('hey')

# Python code to illustrate
# Decorators with parameters in Python

# def decorator(*args, **kwargs):
# 	print("Inside decorator")
	# 	def inner(func):
		
		# code functionality here
		# print("Inside inner function")
		# print("I like", kwargs['like'])
		
		# func()
		
	# returning inner function
# 	return inner

# @decorator(like = "geeksforgeeks")
# def my_func():
# 	print("Inside actual function")


# l=['fgf','gfg']
# l.sort(key=len)
# print(l)

# l=['fgf','gfg']
# print(sorted(l,key=len))

# def bubblesort(l):
# 	n=len(l)
# 	for i in range (1,n):
# 		for j in range(0,n-i):
# 			if l[j]>l[j+1]:
# 				temp=l[j]
# 				l[j]=l[j+1]
# 				l[j+1]=temp

# l=[5,6,2,1,4,9,10,13,12,0]
# bubblesort(l)
# print(l)

# def bubblesort(l):
# 	n=len(l)
# 	for i in range(0,n-1):
# 		swapped= False
# 		print(i+1,"times")
# 		for j in range(0,n-i-1):
# 			if l[j]>l[j+1]:
# 				temp=l[j]
# 				l[j]=l[j+1]
# 				l[j+1]=temp
# 				swapped=True
# 		if swapped==False:
# 			return

# l=[4,3,2,1]
# bubblesort(l)
# print(l)


# def selsort(l):
# 	n=len(l)
# 	for i in range(0,n-1):
# 		minele=l[i]
# 		k=i
# 		for j in range(i+1,n):
# 			if l[j]<minele:
# 				minele=l[j]
# 				k=j
# 		if k!=i:
# 			l[i],l[k]=minele,l[i]

# l=[10,5,8,20,2,18]
# selsort(l)
# print(l)


# def swap(a, b):
#     temp = a
#     a = b
#     b = temp
#     return a, b

# def stable_selection_sort(array):
#     for i in range(len(array)):
#         min_index = i
#         for j in range(i + 1, len(array)):
#             if array[j] < array[min_index] and array[j] == array[min_index]:
#                 min_index = j
#         if min_index != i:
#             swap(array, i, min_index)
#     return array

# print(stable_selection_sort([10,5,8,20,2,18]))

# def insertsort(l):
# 	n=len(l)
# 	for i in range(1,n):
# 		x=l[i]
# 		j=i-1
# 		while (j>=0)and(x>l[j]):
# 			l[j+1]=l[j]
# 			j-=1
# 		l[j+1]=x
# 	return l
    
# l=[20,5,40,60,10,30]    
# insertsort(l)
# print(l)

# def insertsort(l):
# 	n=len(l)
# 	for i in range(n-2,-1,-1):
# 		x=l[i]
# 		j=i+1
# 		while (j<n-1)and(x>l[j]):
# 			l[j]=l[j+1]
# 			j+=1
# 		l[j-1]=x
# 	return l
    
# l=[20,5,40,60,10,30]    
# insertsort(l)
# print(l)
		
# def mergesort(a,b):
# 	l=[]
# 	b1=b
# 	for i in a :
# 		for j in b:
# 			if j<=i:
# 				l.append(j)
# 				b1.remove(j)
# 		l.append(i)
# 		b=b1


# a=[10,15,20]
# b=[5,8,7,30]
# print(mergesort(a,b))


# def merge(a,b):
# 	l=[]
# 	m=len(a)
# 	n=len(b)
# 	i=0
# 	j=0
# 	while(i<m)and (j<n):
# 		if a[i]<b[j]:
# 			l.append(a[i])
# 			i+=1
# 		elif a[i]==b[j]:
# 			l.append(a[i])
# 			i+=1
# 			l.append(b[j])
# 			j+=1
# 		else:
# 			l.append(b[j])
# 			j+=1
# 	while i<m:
# 		l.append(a[i])
# 		i+=1
# 	while j<n:
# 		l.append(b[j])
# 		j+=1
# 	return l

# a=[7,15,20]
# b=[6,6,7,30]
# print(merge(a,b))

# def merge(a,b):
# 	res=a+b
# 	res.sort()
# 	return res

# a=[10,15,20]
# b=[5,6,6,30]
# print(merge(a,b))


# def merge(a,low,mid,high):
# 	l=[]
# 	l1=a[low:mid+1]
# 	l2=a[mid+1:high+1]
# 	m=len(l1)
# 	n=len(l2)
# 	i=0
# 	j=0
# 	while(i<m)and (j<n):
# 		if l1[i]<l2[j]:
# 			l.append(l1[i])
# 			i+=1
# 		elif l1[i]==l2[j]:
# 			l.append(l1[i])
# 			i+=1
# 			l.append(l2[j])
# 			j+=1
# 		else:
# 			l.append(l2[j])
# 			j+=1
# 	while i<m:
# 		l.append(l1[i])
# 		i+=1
# 	while j<n:
# 		l.append(l2[j])
# 		j+=1
# 	return l

# print(merge([10,15,20,11,13],0,2,4))

# def union(a,b):
# 	res=a+b
# 	res.sort()
# 	l=[]
# 	for i in range(0,len(res)):
# 		if i!=len(res)-1 and res[i]==res[i+1]:
# 				continue
# 		else:
# 			l.append(res[i])
# 	return l

# def union(a,b):
# 	res=a+b
# 	res.sort()
# 	l=[]
# 	for i in range(0,len(res)):
# 		if i!=len(res)-1 and res[i]!=res[i+1]:
# 			l.append(res[i])
# 		elif i==len(res)-1:
# 			l.append(res[i])
# 	return l

# def union(a,b):
# 	l=[]
# 	m=len(a)
# 	n=len(b)
# 	i=0
# 	j=0
# 	while(i<m)and (j<n):
# 		if i<m-1 and a[i]==a[i+1]:
# 			i+=1
# 		elif j<n-1 and b[j]==b[j+1]:
# 			j+=1
# 		elif a[i]<b[j]:
# 			l.append(a[i])
# 			i+=1
# 		elif a[i]==b[j]:
# 			l.append(a[i])
# 			i+=1
# 			j+=1
# 		else:
# 			l.append(b[j])
# 			j+=1
# 	while i<m:
# 		if i<m-1 and a[i]==a[i+1]:
# 			i+=1
# 		else:
# 			l.append(a[i])
# 			i+=1
# 	while j<n:
# 		if j<n-1 and b[j]==b[j+1]:
# 			j+=1
# 		else:
# 			l.append(b[j])
# 			j+=1
# 	return l

# a=[2,3,3,3,3,3,5]
# b=[3,4,4,6,6,6,7,7,8,8,9,9]
# print(union(a,b))

# a=5
# if a>4:
# 	print("hi")
# if a==5:
# 	print("hello")
# if a<3:
# 	print("tokyo")
# elif a>2:
# 	print("bhutan")
# else:
# 	print("austria")

# a=[]
# print(a[0])

# for i in range(0,5):
# 	print("hi")
# 	for i in range (1,4):
# 		if i==3:
# 			continue
# 		print("hello")

# def intersect(a,b):
# 	l=[]
# 	for i in range(0,len(a)):
# 		if i<len(a)-1 and a[i]==a[i+1]:
# 			continue
# 		for j in range(0,len(b)):
# 			if j<len(b)-1 and b[j]==b[j+1]:
# 				continue
# 			if a[i]==b[j]:
# 				l.append(a[i]) 
# 	return l


# def intersect(a,b):
# 	l=[]
# 	m=len(a)
# 	n=len(b)
# 	i=0
# 	j=0
# 	while i<m and j<n:
# 		if i<m-1 and a[i]==a[i+1]:
# 			i+=1
# 		elif j<n-1 and b[j]==b[j+1]:
# 			j+=1
# 		elif a[i]==b[j]:
# 			l.append(a[i])
# 			i+=1
# 			j+=1
# 		elif a[i]<b[j]:
# 			i+=1
# 		elif a[i]>b[j]:
# 			j+=1
# 	return l
# a=[]
# b=[]
# print(intersect(a,b))


# def countinv(a):
# 	count=0
# 	m=len(a)
# 	for i in range(0,m):
# 		for j in range(i,m):
# 			if a[i]>a[j]:
# 				count+=1
# 	return count


# def countinv(a):
# 	count=0
# 	m=len(a)
# 	for i in range(0,m):
# 		if i<m-1 and a[i]==a[i+1]:
# 			continue
# 		for j in range(i,m):
# 			if j<m-1 and a[j]==a[j+1]:
# 				continue
# 			if a[i]>a[j]:
# 				count+=1
# 	return count

# a=[40,40,30,20,10,10]
# print(countinv(a))

# def partit(p,a):
# 	l=[]
# 	for i in range(0,len(a)):
# 		if a[i]<=a[p]:
# 			l.append(a[i])
# 	l.append(a[p])
# 	for i in range(0,len(a)):
# 		if a[i]>a[p]:
# 			l.append(a[i])
# 	return l

# def partit(p,a):
# 	l=[]
# 	m=len(a)
# 	a[p],a[m-1]=a[m-1],a[p]
# 	for i in range(0,m):
# 		if a[i]<=a[p]:
# 			l.append(a[i])
# 	for j in range(0,m):
# 		if a[j]>a[p]:
# 			l.append(a[j])
# 	return l

# print(partit(5,[3,8,7,6,7,7,7,12,10,7]))

# def lomuto(p,a):
# 	m=len(a)
# 	a[p],a[m-1]=a[m-1],a[p]
# 	pivot=a[m-1]
# 	i=-1
# 	for j in range (0,m-1):
# 		if a[j]<=pivot:
# 			i+=1
# 			a[i],a[j]=a[j],a[i]
# 	a[i+1],a[m-1]=a[m-1],a[i+1]
# 	return a

# print(lomuto(8,[3,8,7,6,7,7,7,12,10,7]))


# def hoare(p,a):
# 	m=len(a)
# 	a[p],a[0]=a[0],a[p]
# 	pivot=a[0]
# 	i=-1
# 	j=m
# 	while True:
# 		i+=1
# 		while a[i]<=pivot:
# 			i+=1
# 			if i==m-1:
# 				break
# 		j-=1
# 		while a[j]>pivot:
# 			j-=1
# 			if j==0:
# 				break
# 		if i>=j:
# 			a[j],a[0]=a[0],a[j]
# 			return a
# 		a[i],a[j]=a[j],a[i]

# print(hoare(9,[3,8,7,6,7,7,7,12,10,7]))


# memory = {}
# def memoize_factorial(f):
# 	def inner(num):
# 		if num not in memory:
# 			memory[num] = f(num)
# 			print('result saved in memory')
# 			print(num,':',memory[num])
# 		else:
# 			print('returning result from saved memory')
# 		return memory[num]
# 	return inner
# @memoize_factorial
# def facto(num):
# 	if num == 1:
# 		return 1
# 	else:
# 		return num * facto(num-1)

# print(facto(5))
# print(facto(5))


# def bubblesort(l):
# 	n=len(l)
# 	for i in range(0,n-1):
# 		swapped=False
# 		for j in range(n-1,i,-1):
# 			if l[j]<l[j-1]:
# 				l[j],l[j-1]=l[j-1],l[j]
# 				swapped=True
# 		if swapped==False:
# 			return l
# 	return l

# l=[1,2,3,4]
# del l[1]
# print(l)
# l=[2]

# l[0]=1
# l[5]=5
# print(l)

# l=[2]*4
# print(l)

# s={10,20}
# s.update({50,60},[30,40])
# s.update({50,60})
# print(s)
# s.remove(30)
# print(s)

# d={1:'a',2:'b',3:'c'}
# print(d.popitem())

# def sumExist(s,l):
# 	s1=set(l)
# 	for i in s1:
# 		if (s-i in s1.difference({i})) or (i-s in s1.difference({i})):
# 			print(i,abs(s-i))
# 			return 1
# 	return 0


# l=[1,2,3,4,5,6,7,8,9,10]
# s=14
# print(sumExist(s,l))

# class MyHash:
# 	def __init__(self,c):
# 		self.cap=c
# 		self.table=[-1]*c
# 	def hash(self,x):
# 		return x%self.cap
# 	def search(self,x):
# 		t=self.table
# 		h=self.hash(x)
# 		i=h
# 		while (t[i]!=-1):
# 			if t[i]==x:
# 				return True
# 			i=(i+1)%self.cap
# 			if i==h:
# 				return False
# 		return False
# 	def insert(self,x):
# 		t=self.table
# 		h=self.hash(x)
# 		i=h
		
# 		if self.search(x)==True:
# 			return False
# 		while t[i] not in (-1,-2):
# 			i=(i+1)%self.cap
# 		t[i]=x
# 		return True


# def ins_in_ht(c,l):
# 	h=MyHash(c)
# 	for i in l:
# 		if h.insert(i)==False:
# 			print(f"repeated element {i},therefore not added again")
# 		h.insert(i)
# 	return h.table

# c=10
# l=[9,99,999,9999,9,99]
# print(ins_in_ht(c,l))


# class MyHash:
# 	def __init__(self,c):
# 		self.cap=c
# 		self.table=[-1]*c
# 	def hash(self,x):
# 		return x%self.cap
# 	def search(self,x):
# 		t=self.table
# 		h=self.hash(x)
# 		i=h
# 		n=1
# 		while (t[i]!=-1):
# 			if t[i]==x:
# 				return True
# 			i=(h+(n**2))%self.cap
# 			n+=1
# 			if i==h:
# 				return False
# 		return False
# 	def insert(self,x):
# 		t=self.table
# 		h=self.hash(x)
# 		i=h
# 		if self.search(x)==True:
# 			return False
# 		n=1
# 		while t[i] not in (-1,-2):
# 			i=(h+(n**2))%self.cap
# 			n+=1
# 			if i==h:
# 				return False
# 		t[i]=x
# 		return True

# def ins_in_ht_qp(c,l):
# 	h=MyHash(c)
# 	for i in l:
# 		if h.insert(i)==False:
# 			print(f"element {i} Repeated or Not able to place,therefore not added")
# 		h.insert(i)
# 	return h.table

# c=10
# l=[42,16,91,33,18,27,36,62]
# print(ins_in_ht_qp(c,l))

# l=[[]]*10
# print(l)

# class MyHash:
# 	def __init__(self,c):
# 		self.cap=c
# 		self.table=[[] for x in range(c)]
# 	def hash(self,x):
# 		return x%self.cap
# 	def search(self,x):
# 		t=self.table
# 		i=self.hash(x)
# 		return x in t[i]
# 	def insert(self,x):
# 		i=self.hash(x)
# 		t=self.table
# 		if self.search(x)==True:
# 			return False
# 		t[i].append(x)
# 		return True
	
# def ins_in_ht_chain(c,l):
# 	h=MyHash(c)
# 	for i in l:
# 		if h.insert(i)==False:
# 			print(f"element {i} Repeated or Not able to place,therefore not added")
# 		# h.insert(i)
# 	return h.table

# c=10
# l=[92,4,14,14,24,44,91]
# print(ins_in_ht_chain(c,l))


# l=[[]]*5
# l[3].append(4)
# print(l)

# d={1:'a',2:'b'}
# print(d.items())

# def count_npe_in_str(s):
# 	d={}
# 	for i in s: 
# 		if i not in d:
# 			d[i]=1
# 		else:
# 			d[i]+=1
# 	for i in d.items():
# 		if i[1]==1:
# 			print(i[0])
# 			break
# 	if 1 not in d.values():
# 		print('$')

# s='hheelloo'
# count_npe_in_str(s)



# class Employee:
#     no_of_leaves = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)


# class Programmer(Employee):
#     no_of_holiday = 56
#     def __init__(self, aname, asalary, arole, languages):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.languages = languages


#     def printprog(self):
#         return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")

# shubham = Programmer("Shubham", 555, "Programmer", ["python"])
# karan = Programmer("Karan", 777, "Programmer", ["python", "Cpp"])
# karan.change_leaves(55)
# rohan.change_leaves(48)
# print(Programmer.__dict__)




# class Employee:
#     no_of_leaves = 8
#     var = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)

# class Player:
#     var = 9
#     no_of_games = 4
#     def __init__(self, name, game):
#         self.name = name
#         self.game =game

#     def printdetails(self):
#         return f"The Name is {self.name}. Game is {self.game}"

# class CoolProgramer(Employee,Player):

#     language = "C++"
#     def printlanguage(self):
#         print(self.language)

# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")

# shubham = Player("Shubham", ["Cricket"])
# karan = CoolProgramer("Karan",454,'instructor')
# det = karan.printdetails()
# karan.printlanguage()
# print(det)
# print(karan.var)
# print(karan.game)


# class Dad:
    # def __init__(self,aname):
        # self.name=aname
#     basketball =6
    

# class Son(Dad):
#     def __init__(self,aname,age):
#          self.name=aname
#          self.age=age
#     dance =1
#     basketball = 9
#     def isdance(self):
#         return f"Yes I dance {self.dance} no of times"

# class Grandson(Son):
#     dance =6
#     guitar = 1

#     def isdance(self):
#         return f"Jackson yeah!" \
#             f"Yes I dance very awesomely {self.dance} no of times"

# darry = Dad()
# larry = Son("larry",21)
# harry = Grandson("arry",12)
# print(larry.__dict__)
# print(darry.guitar)


# class A:
#     classvar1 = "I am a class variable in class A"
#     def __init__(self,name,section):
#         self.name=name
#         self.var1 = "I am inside class A's constructor"
#         self.classvar1 = "Instance var in class A"
#         self.section=section
#         self.special ="special"

        
# class B(A):
#     classvar1 = "I am in class B"

#     def __init__(self,age):
#         self.age=age
#         self.var1 = "I am inside class B's constructor"
#         self.classvar1 = "Instance var in class B"
#         super().__init__("aggarwal","y")
        # print(super().classvar1)


# a = A("yashika","q")
# b = B(7)

# print(b.age,b.special, b.var1, b.classvar1,b.name,b.section)
# print(a.__dict__)
# print(b.__dict__)
# print(A.__dict__)
# print(B.__dict__)

# class A:
#     def __init__(self,aname,aroll):
#          self.name=aname
#          self.roll=aroll
    # def met(self):
    #     print("This is a method from class A")
    
# class B(A):
#     def __init__(self,aname,aroll,amarks):
#          self.name=aname
#          self.roll=aroll
#          self.marks=amarks
#          super().__init__("bholu",23)
    # def met(self):
    #     print("This is a method from class B")
    # pass
    
# class E:
    # def met(self):
    #     print("This is a method from class E")
    # def __init__(self,aname,aroll,amarks,asection):
    #      self.name=aname
    #      self.roll=aroll
    #      self.marks=amarks
    #      self.section=asection

    # pass
# class C(E):
    # def met(self):
    #     print("This is a method from class C")
    # def __init__(self,aname,aroll,amarks,asection,aclass):
    #      self.name=aname
    #      self.roll=aroll
    #      self.marks=amarks
    #      self.section=asection
    #      self.aclass=aclass
    #      super().__init__("kalia",656,32222,'s',5)
    # pass
# class D(B,C):
    # def met(self):
    #     print("This is a method from class D")
    # def __init__(self,aname,aroll,amarks,asection,aclass,abrand):
    #      self.name=aname
    #      self.roll=aroll
    #      self.marks=amarks
    #      self.section=asection
    #      self.aclass=aclass
    #      self.brand=abrand
    #      super().__init__("dholu",23,1222)
         
# a = A("bheem",12)
# b = B("chutki",120,150)
# c = C("jaggu",321,345,"s",3)
# d = D("kichak",45,231,"q",4,"Lenovo")
# e = E("raju",65,43,'u')
# print(d.__dict__)


# class Employee:
#     no_of_leaves = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    # @classmethod
    # def change_leaves(cls, newleaves):
    #     cls.no_of_leaves = newleaves

    # def __add__(self, other):
    #     return self.salary + other.salary

    # def __truediv__(self, other):
    #     return self.salary / other.salary
    
    # @classmethod
    # def __repr__(cls):
    #     return f'{cls}({cls.printdetails()})'

    # def __str__(self):
    #     return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
# print(repr(emp1))


# from abc import ABCMeta, abstractmethod
# from abc import ABC, abstractmethod

# class Shape(ABC):
#      c="classs"
#      @abstractmethod
#      def printarea(self):
#         return 0
#      def printperimeter(self):
#           return 0

# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#     def __init__(self):
#         self.length = 6
#         self.breadth = 7
#     def printarea(self):
#         return self.length * self.breadth

# rect1 = Rectangle()
# print(rect1.printarea())


# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
# # def printlist(head):
# # 	while (head!=None):
# # 		print(head.key,end=" ")
# # 		head=head.next

# def printlist(head):
# 	if (head==None):
# 		return 0
# 	print(head.key,end=" ")
# 	printlist(head.next)
    
# head=Node(10)
# head.next=Node(15)
# head.next.next=Node(20)
# head.next.next.next=Node(30)
# head.next.next.next.next=Node(45)
# # head.next.next.next.next.next=None
# print(printlist(head))



# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
# def search(head,x):
# 	count=1
# 	while (head!=None):
# 		if head.key==x:
# 			return count
# 		count+=1
# 		head=head.next
# 	return -1

# def search(head,x):
# 	count=1
# 	if (head==None):
# 		return -1
# 	# global count
# 	if head.key==x:
# 		return count
# 	count+=1
# 	search(head.next,x)
# head=Node(10)
# head.next=Node(15)
# head.next.next=Node(20)
# head.next.next.next=Node(30)
# head.next.next.next.next=Node(45)

# x=20
# print(search(head,x))


# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
		
# def printlist(head):
# 	while (head!=None):
# 		print(head.key,end=" ")
# 		head=head.next	
		
# def delPos(head,pos):
# 	if pos==1:
# 		return head.next
# 	temp=head
# 	for i in range(pos-2):
# 		temp=temp.next
# 		if temp==None:
# 			return head
# 	temp.next=temp.next.next
# 	return head 

# def delPos(ptr):
# 	temp=ptr.next
# 	ptr.key=temp.key
# 	ptr.next=temp.next
		
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)
# head.next.next.next.next=Node(50)	
# head=delPos(head,2)
# delPos(head.next.next.next.next)
# printlist(head)
# print(head.next.next.key)


# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
		
# def printlist(head):
# 	while (head!=None):
# 		print(head.key,end=" ")
# 		head=head.next	

# def sortedInsert(head,x):
# 	temp=Node(x)
# 	if head==None:
# 		return temp
# 	if x<head.key:
# 		temp.next=head
# 		return temp
# 	curr=head
# 	while (curr!=None):
# 		if curr.next==None:
# 			curr.next=temp
# 			return head
# 		if (x<curr.next.key):
# 			break
# 		curr=curr.next
# 	temp.next=curr.next
# 	curr.next=temp
# 	return head

# head=None
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)
# head.next.next.next.next=Node(50)	
# head=sortedInsert(head,13)
# printlist(head)


class Node:
	def __init__(self,key):
		self.key=key
		self.next=None
		
def printlist(head):
	while (head!=None):
		print(head.key,end=" ")
		head=head.next
		
# def printMiddle(head):
# 	if head==None:
# 		return (" ")
# 	slow=head
# 	fast=head
# 	if slow.next==None:
# 		return slow.key
# 	while fast!=None and fast.next!=None:
# 		slow=slow.next
# 		fast=fast.next.next
# 	return slow.key

# head=None
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)
# head.next.next.next.next=Node(50)	
# print(printMiddle(head))
# printlist(head)


# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
		
# def printlist(head):
# 	while (head!=None):
# 		print(head.key,end=" ")
# 		head=head.next
		
# def printNfromEnd(head,n):
# 	if head==None:
# 		return (" ")
# 	count=0
# 	curr=head
# 	while curr:
# 		curr=curr.next
# 		count+=1
# 	if n>count:
# 		return (' ')
# 	curr=head
# 	for i in range(count-n):
# 		curr=curr.next
# 	return curr.key

# head=None
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)
# head.next.next.next.next=Node(50)	
# print(printNfromEnd(head,2))
# printlist(head)


# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
		
# def printlist(head):
# 	while (head!=None):
# 		print(head.key,end=" ")
# 		head=head.next

# def removeDup(head):
# 	if head==None:
# 		return head
# 	curr=head
# 	while curr.next!=None:
# 		if curr.key!=curr.next.key:
# 			curr=curr.next
# 		else:
# 			curr.next=curr.next.next
# 	return head	

# def countele(head):
# 	if head==None:
# 		return 0
# 	count=0
# 	while head!=None:
# 		count+=1
# 		head=head.next
# 	return count

# def sumele(head):
# 	if head==None:
# 		return 0
# 	sum=0
# 	while head!=None:
# 		sum=sum+head.key
# 		head=head.next
# 	return sum

# def searchele(head,x):
# 	while head!=None:
# 		if (head.key==x):
# 			return 1
# 		head=head.next
# 	return 0
# print(next)
# head=None
# head=Node(20)
# head.next=Node(10)
# head.next.next=Node(10)
# head.next.next.next=Node(20)
# head.next.next.next.next=Node(30)
# head.next.next.next.next.next=Node(30)
# head.next.next.next.next.next.next=Node(120)

# print(countele(head))
# print(sumele(head))
# removeDup(head)
# printlist(head)
# print(searchele(head,12))
# print(head is  None)

# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
		
# def printlist(head):
# 	while (head!=None):
# 		print(head.key,end=" ")
# 		head=head.next
# 	print()

# def insertBeg(head,key):
# 	curr=Node(key)
# 	curr.next=head
# 	return curr

# def insertEnd(head,key):
# 	curr=Node(key)
# 	temp=head
# 	if head==None:
# 		return curr
# 	while temp!=None:
# 		if temp.next==None:
# 			temp.next=curr
# 			return head
# 		temp=temp.next

# class newLL:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None

# def delPos(ptr):
# 	temp1=ptr.next
# 	ptr.key=temp1.key
# 	ptr.next=temp1.next

# def improveLL(head):
# 	temp=head
# 	if head==None:
# 		return head
# 	while temp.next!=None:
# 		# print(temp.key)
# 		if temp.next.key==1:
# 			# print("ok")
# 			head=insertEnd(head,temp.key)
# 			temp1=temp.next.next
# 			delPos(temp)
# 			delPos(temp.next)
# 			temp=temp1
# 			# temp=temp.next
# 		elif temp.next.key==0:
# 			# print("ok")
# 			head=insertBeg(head,temp.key)
# 			temp1=temp.next.next
# 			delPos(temp)
# 			delPos(temp.next)
# 			temp=temp1
			# temp=temp.next
		# elif (temp.next!=1) or (temp.next!=1):
		# 	print("wrong LL provided")
# 	return head

# head=Node(9)
# head.next=Node(0)
# head.next.next=Node(5)
# head.next.next.next=Node(1)
# head.next.next.next.next=Node(6)
# head.next.next.next.next.next=Node(1)
# head.next.next.next.next.next.next=Node(2)
# head.next.next.next.next.next.next.next=Node(0)
# head.next.next.next.next.next.next.next.next=Node(5)
# head.next.next.next.next.next.next.next.next.next=Node(0)
# printlist(head)
# head=improveLL(head)
# head=insertEnd(head,head.key)
# printlist(head)


# def insertafterpos(head,pos,data):
# 	temp=Node(data)
# 	if pos==0:
# 		temp.next=head
# 		return temp
# 	curr=head
# 	for i in range(pos-1):
# 		if curr==None:
# 			break
# 		curr=curr.next
# 	if curr!=None:
# 		temp.next=curr.next
# 		curr.next=temp
# 	return head

# def insertAtMiddle(head,data):
# 	temp=Node(data)
# 	if head==None:
# 		temp.next=head
# 		return temp
# 	slow=head
# 	fast=head
# 	if slow.next==None:
# 		temp.next=head
# 		return temp
# 	while fast!=None and fast.next!=None:
# 		prev=slow
# 		slow=slow.next
# 		fast=fast.next.next
# 	prev.next=temp
# 	temp.next=slow
# 	return head


# def min_and_max(head):
# 	if head==None:
# 		print("min and max ele is",head)
# 		return 
# 	min=head
# 	max=head
# 	curr=head
# 	while(curr!=None):
# 		if curr.key<min.key:
# 			min=curr
# 		if curr.key>max.key:
# 			max=curr
# 		curr=curr.next
# 	print("min ele is: ",min.key)
# 	print("max ele is: ",max.key)
# 	return 


# head=None
# head=Node(190)
# head.next=Node(-0.1)
# head.next.next=Node(5)
# head.next.next.next=Node(1)
# head.next.next.next.next=Node(6)
# head.next.next.next.next.next=Node(1)
# head.next.next.next.next.next.next=Node(2)
# head.next.next.next.next.next.next.next=Node(0)
# head.next.next.next.next.next.next.next.next=Node(5)
# head.next.next.next.next.next.next.next.next.next=Node(0)
# printlist(head)
# min_and_max(head)
# head=insertafterpos(head,11,20)
# head=insertAtMiddle(head,1000)
# printlist(head)


# class Node1:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None

# class Node2:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
	
# def areidentical(head1,head2):
# 	if head1==None or head2==None:
# 		print("no")
# 		return 
# 	curr1=head1
# 	curr2=head2
# 	while curr1!=None or curr2!=None:
# 		if curr1.key!=curr2.key:
# 			print("no")
# 			return
# 		curr1=curr1.next
# 		curr2=curr2.next
# 	print("yes")
# 	return

# head1=Node1(2)
# head1.next=Node1(3)
# head2=Node2(2)
# head2.next=Node2(4)
# printlist(head1)
# printlist(head2)
# areidentical(head1,head2)



# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None

# def lenghtOfCLL(head):
# 	if head==None:
# 		return 0
# 	curr=head
# 	count=1
# 	while curr.next!=head:
# 		count+=1
# 		curr=curr.next
# 	return count

# def delTail(head):
# 	if head==None:
# 		return head
# 	if head.next==head:
# 		return None
# 	curr=head
# 	while curr.next.next!=head:
# 		curr=curr.next
# 	curr.next=head
# 	return head

# def printCLL(head):
# 	if head==None:
# 		return None
# 	curr=head
# 	print(curr.key)
# 	curr=curr.next
# 	while curr!=head:
# 		print(curr.key)
# 		curr=curr.next
# 	return
		
# def checkCLL(head):
# 	if head==None:
# 		return 0
# 	curr=head
# 	while True:
# 		if curr.next==None:
# 			return 0
# 		elif curr.next==head:
# 			return 1
# 		curr=curr.next


# head=None
# head=Node(10)
# head.next=Node(29)
# head.next.next=Node(39)
# head.next.next.next=Node(476)
# head.next.next.next.next=head
# head=delTail(head)
# printCLL(head)
# print(lenghtOfCLL(head))
# print(checkCLL(head))
# for i in range(1):
# 	print("hi")

class Node:
	def __init__(self,key):
		self.key=key
		self.prev=None
		self.next=None

# def printDLL(head):
# 	if head==None:
# 		print(head)
# 		return 
# 	curr=head
# 	while (curr!=None):
# 		print(curr.key,end=" ")
# 		curr=curr.next
# 	print()
# 	return 

# def insertBegin(head,x):
# 	temp=Node(x)
# 	if head==None:
# 		return temp
# 	temp.next=head
# 	head.prev=temp
# 	return temp

# def insertEnd(head,x):
# 	temp=Node(x)
# 	if head==None:
# 		return temp
# 	curr=head
# 	while (curr.next!=None):
# 		curr=curr.next
# 	curr.next=temp
# 	temp.prev=curr
# 	return head

# head=None
# head=insertBegin(head,10)
# head=insertBegin(head,20)
# head=insertBegin(head,30)

# head=insertEnd(head,100)
# head=insertEnd(head,200)
# head=insertEnd(head,300)
# printDLL(head)


# def printDLLFandB(head):
# 	if head==None:
# 		print("None","None",sep='\n')
# 		return 
# 	curr=head
# 	print(curr.key,end=" ")
# 	while curr.next!=None:
# 		print(curr.next.key,end=" ")
# 		curr=curr.next
# 	print()
# 	while curr!=None:
# 		print(curr.key,end=" ")
# 		curr=curr.prev
# 	print()
# 	return 

# head=None
# head=Node(10)
# temp1=Node(20)
# temp2=Node(30)
# head.next=temp1
# temp1.prev=head
# temp1.next=temp2
# temp2.prev=temp1
# printDLLFandB(head)

# def printCDLLFandB(head):
# 	if head==None:
# 		print("None","None",sep='\n')
# 		return 
# 	curr=head
# 	print(curr.key,end=" ")
# 	while (curr.next!=head):
# 		print(curr.next.key,end=" ")
# 		curr=curr.next
# 	print()
# 	print(curr.key,end=" ")
# 	tail =curr
# 	while (curr.prev!=tail):
# 		print(curr.prev.key,end=" ")
# 		curr=curr.prev
# 	print()
# 	return 


# def checkDCLL(head):
# 	if head==None:
# 		return 0
# 	curr=head
# 	if curr.prev==head and curr.prev==head:
# 		return 1
# 	while True:
# 		if curr.next==None:
# 			return 0
# 		elif curr.next==head:
# 			break
# 		curr=curr.next
# 	tail=curr
# 	if head.prev==tail and tail.next==head:
# 		return 1
# 	else:
# 		return 0

# # head=None
# head=Node(10)
# temp1=Node(20)
# temp2=Node(30)
# head.prev=temp2
# head.next=temp1
# temp1.prev=head
# temp1.next=temp2
# temp2.prev=temp1
# temp2.next=head

# head.prev=head
# head.next=head

# head.next=temp1
# head.prev=temp1
# temp1.prev=head
# temp1.next=head
# printCDLLFandB(head)
# print(checkDCLL(head))
	
# len()

# class ar:
# 	def __init__(self,ap):
# 		self.ap=ap
# 		return
# 	def __pr__(self,a):
# 		count=0
# 		while a:
# 			count+=1
# 		self.count=count
# 	def lent(self):
# 		return self.count
	
# a=[1,2,3,4]
# b=ar(a)
# print(b.lent(a))
# a=[1,2,3,4]
# print(__pr__(a))

# import math
# print(type(math.inf))

# def insertintoStack(n,arr):
# 	stack=[]
# 	for i in range(n-1,-1,-1):
# 		stack.append(arr[i])
# 	return stack

# l=[]
# print(insertintoStack(0,l))

# class Node:
# 	def __init__(self,key):
# 		self.key=key
# 		self.next=None
		
# def insertintoStack()

# while 2/3:
# 	print("hllo earth")

# s=[1,2,3,4]
# copy=s.copy()
# copy.pop()
# print(copy)
# print(s)


# def findInStack(stack,x):
# 	copy=stack
		

# d={1:'a',2:'b',3:'c',4:'d'}
# print('a' in d)

# fruit_list = [{"name": "apple", "color": "red"}, {"name": "banana", "color": "yellow"}, {"name": "orange", "color": "orange"}]

# if "apple" in fruit_list:
#   print("The value 'apple' is found in the list of dictionaries.")
# else:
#   print("The value 'apple' is not found in the list of dictionaries.")

# x=10
# x=list('hello')
# x=''.join(x)
# print(x)

# l=[1,2,3,4]
# print(l.pop(),l.pop())
# print(f'({l.pop()/l.pop()})')

# def PrefixToInfix(exp):
# 	stack=[]
# 	# print(exp[::-1])
# 	for i in exp[::-1]:
# 		if i.isalpha():
# 			# print(i)
# 			stack.append(i)
# 		else:
# 			stack.append(f'({stack.pop()}{i}{stack.pop()})')
# 	return ''.join(stack)

# print(PrefixToInfix("*-A/BC-/AKL"))

# def infix_to_postfix(expression):
#   stack = []
#   postfix_expression = []

#   for token in expression:
#     if token.isalpha():
#       postfix_expression.append(token)
#     elif token == "(":
#       stack.append(token)
#     elif token == ")":
#       while stack[-1] != "(":
#         postfix_expression.append(stack.pop())
#       stack.pop()
#     else:
#       while len(stack) > 0 and (precedence(stack[-1]) >= precedence(token)):
#         postfix_expression.append(stack.pop())
#       stack.append(token)

#   while len(stack) > 0:
#     postfix_expression.append(stack.pop())

#   return "".join(postfix_expression)

# def precedence(token):
#   if token == "+" or token == "-":
#     return 1
#   elif token == "*" or token == "/":
#     return 2
#   else:
#     return 0

# print(infix_to_postfix('((A+B)/(C-D))'))
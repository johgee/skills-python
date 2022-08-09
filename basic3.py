
# bigstring = "The big string would contain a lot of words and it is hard to find if "
# x = "rd" in bigstring 
# print(x)

# mult = """This is a sample of 
# multiple line text which is otherwise hard
# to read in single line."""
# print(mult)

# name = "grace joh"
# phone = "12393459"
# email = "joh@test.com"

# msg = "call {} at {} or send email to {}."
# print(msg.format(name, phone, email))

# msg2 = "call {2} at {0} or send email at {1}."
# print(msg2.format(name, phone, email))

# s4 = "He said, \"Hello Everyone\""
# print(s4)

# i = 10
# j = 9


# print (10 > 8)
# print(10 > 11)

# bln = (10 > 9)
# print(type(bln))

# theList = ["cycle", "scooter", "car"]
# print(theList)
# print(type(theList))

# theDictionary = {
#     "1": "abc",
#     "2": "def",
#     "3": "ghi"
# }
# print(theDictionary)
# print(type(theDictionary))

# num = 5
# allNums = {1,2,3,4,5,6,7,8,9,10}
# for i in allNums:
#     print(i*num)

# nums = {1,2,3,4,5,6,7,8,9}
# for i in nums:
#     print(i)

# myname = "grace joh"
# for s in myname:
#     print(s)

# nums1 = {1,2,3,4,5,6,7,8,9}
# for j in nums1:
#     if(j==5):
#         break 
#     else: 
#         print(j)

# for i in range(10):
#     print(i)
  

# for i in range(2,10):
#     print(i)

# for i in range(2, 21, 2):
#     print(i)

# for i in range(5):
#     print(i)
# else: 
#     print("done")

# num = 5
# for i in range(1,11):
#     print(i*num)

# n = 1
# while n < 11:
#     print(n)
#     n+=1 

# i = 1
# blnFlag = True 
# while blnFlag:
#     print(i)
#     if(i == 10):
#         blnFlag = False 
#     i+=1

# j = 1
# while (j < 10):
#     if(j == 5):
#         break 
#     else:
#         print(j)
#     j+= 1

# k = 1
# while (k<10):
#     if k != 9:
#         pass 
#     else:
#         print(k)
#     k+=1

# def addition(num1, num2):
#     print(num1 + num2)

# addition(10,20)

# def my_function():
#     print("hello")
# my_function()

# def my_function(myname):
#     print("hello from " + myname)
# my_function("grace")

# def my_function3(firstname, lastname):
#     return "hello from " + firstname + " " + lastname 
# print(my_function3("grace", "joh"))

# print(my_function3(lastname = "joh", firstname = "grace"))

# def my_function5(myname = "no name!!!"):
#     print("my name is : " + myname)
# my_function5("grace")
# my_function5()

# def divide(num1, num2):
#     print(num1/num2)

# divide(20, 2)
# divide(30, 10)
# divide(40, 0) # zero division error: division by zero 
# divide(30, 15)

# def divide2(num1, num2):
#     if(num2!=0):
#         print(num1/num2)
#     else:
#         print("can't be divided by zero")
# divide2(20, 2)
# divide2(30, 10)
# divide2(40, 0) 
# divide2(30, 15)

# def divide2(num1, num2):
#     print(num1/num2)

# try:
#     divide2(20, 2)
# except:
#     print("there is an error")

# try:
#     divide2(40, 0)
# except:
#     print("there is an error")

# try:
#     divide2(30, 15)
# except: 
#     print("there is an error")

# def divide4(num1, num2):
#     try:
#         print(num1/num2)
#     except:
#         print("there is an error")
# divide4(10, 5)
# divide4(9, 0)
# divide4(30, 15)

# a = 10
# b = 20
# result = a + b
# print(result)

# num1 = input("enter the first number: ")
# num2 = input("enter the second number: ")
# result = num1+num2 
# print(result)

# def sayHello(name):
#     print("Hello "+name)

# import basic3
# basic3.sayHello("Grace")

# import basic3 as b
# b.sayHello("Grace")

# class MyClass:
#     a = 10
#     b = 20 
# #calling the class
# classObject = MyClass()
# print(classObject.a) # this will print 10
# print(classObject.b) # this will print 20

# class MyClass2:
#     a = 0
#     b = 0

#     def initiate(self, x, y):
#         self.a = x
#         self.b = y 

#         print(self.a)
#         print(self.b)

# #calling class MyClass2
# classObj2 = MyClass2()
# classObj2.initiate(22, 33) # this will print 22 and 33

# class MyClass3:
#     def __init__(self, x, y):
#         self.a = x 
#         self.b = y
    
#     def printall(self):
#         print(self.a)
#         print(self.b)
# #calling class MyClass3
# classObj3 = MyClass3(62, 70)
# classObj3.printall() # this will print 62 and 70

# built in method in a class 

# class MyClass4:
#     pass 
# #calling dir() function
# print(dir(MyClass4))


# practicepython.org


###### character input

# create a program that asks for user input
# print out a message addressed to them that tells them the year tha they wil turn 100 years old 

# name = input("enter your name: ")
# print("your name is " + name)

# # age = int(input("enter your age: "))
# # age = int(age)

# # or 
# age = int(input("enter your age: "))
# print("your age is " + age) # can only concatenate string not integer 

# name = input("enter your name: ")
# age = int(input("enter your age: "))
# year = 2020 - age + 100 
# print(name + ", you will be 100 years old in the year " + str(year))

##### odd or even
# ask for a number. put message for odd or even

# 5 % 3 = 2
# 6 % 3 = 0
# 7 % 3 = 1

# age = int(input("enter your age: "))
# if age > 17: 
#   print("can see a rated r movie")
# elif age < 17 and age > 12: 
#   print("can see a rated pg-13 movie")
# else:
#   print("can only see rated pg movies")

# x = int(input("please enter a number "))

# if x < 0: 
#   x = 0 
#   print("negative changed to zero")
# elif x == 0: 
#   print("zero")
# elif x == 1: 
#   print("single")
# else: 
#   print("more")

# words = ["cat", "window", "defenestrate"]
# for w in words: 
#   print(w, len(w))

# for w in words[:]:
#   if len(w) > 6:
#     words.insert(0, w)
 
# num = input("enter a number: ") # didn't work 
# mod = num % 2 
# if mod > 0: 
#   print("you picked an odd number.")
# else: 
#   print("you picked an even number.")

# num = int(input("give me a number to check: "))
# check = int(input("give me a number to divide by: "))

# if num % 4 == 0:
#   print(num, "is a multiple of 4")
# elif num % 2 == 0:
#   print(num, "is an even number")
# else: 
#   print(num, "is an odd number")

# if num % check == 0:
#   print(num, "divides evenly by", check)
# else: 
#   print(num, "does not divide evenly by", check)

##### list less than ten 

# my_list = [1, 3, "Michele", [5, 6, 7]]
# for element in my_list: 
#   print(element)

# grade = input("enter your grade: ") # >= not supported between instances 'str' and 'int'
# if grade >= 90:
#   print("A")
# elif grade >= 80: 
#   print("B")
# elif grade >= 70:
#   print("C")
# elif grade >= 65: 
#   print("D")
# else: 
#   print("F")

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# #basic problem:
# for x in a:
#   if x < 5: print(x)

# #combine challenges 1 and 2:
#   print([ x for x in a if x < 5 ])

#create lists 
# numbers = [7, 3, 13, 6, 8, 5, 1, 2, 4, 15, 9, 10, 12, 14, 11]
# lessFnums = []
# lessNnums = []

# #instead ofp rinting the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list
# for num in numbers: 
#   if num < 5: #compare numbers in list against 5 
#     lessFnums.append(num) #add numbers that are less than 5 to our list 
#     lessFnums.sort() #sort list 
# #print the list 
# print(lessFnums)
# print()

# #ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user
# num = int(input("enter a number: ")) #get a number from user 
# for n in numbers: 
#   if n < num: #compare user number against numbers in list 
#     lessNnums.append(n) #add numbers that are less than user name to our list 
#     lessNnums.sort() #sort list 
# #print the list
# print(lessNnums)

##### divisors

# x = range(2, 11)
# for elem in x: 
#   print (elem)

# __author__ = "jeffreyhunty"

# num = int(input("please choose a number to divide: "))
# listRange = list(range(1, num+1))

# divisorList = []

# for number in listRange: 
#   if num % number == 0: 
#     divisorList.append(number)

# print(divisorList)

##### list overlap 

# a = [5, 10, 15, 20]
# print(10 in a)
# print(3 in a)

# list_of_students = ["Michele", "Sara", "Cassie"]

# name = input("type name to check: ")
# if name in list_of_students:
#   print("this student is enrolled.")

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = set(a).intersection(set(b))
# print(list(c))

##### string lists (PALINDROME)
# a = [5, 10, 15, 20, 25]
# print(a[3])
# print(a[0])

# a = [5, 10, 15, 20, 25, 30, 35, 40]
# print(a[1:4])
# print(a[6:])
# print(a[:-1])

# print(a[1:5:2])
# print(a[3:0:-1])

# string = "example"
# for c in string:
#   print("one letter: " + c) 

# string = "example"
# s = string[0:5]
# print(s)

# wrd = input("enter a word: ")
# wrd = str(wrd)
# rvs = wrd[::-1]
# print(rvs)
# if wrd == rvs: 
#   print("this word is a palindrome")
# else: 
#   print("this word is not a palindrome")

# def reverse(word):
#   x = " "
#   for i in range(len(word)):
#     x += word[len(word) -1 -i]
#   return x 
# word = input("give me a word:\n")
# x = reverse(word)
# if x == word: 
#   print("this is a palindrome")
# else: 
#   print("this is NOT a palindrome")

##### list comprehensions

# years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
# ages = []
# for year in years_of_birth:
#   ages.append(2014 - year)

# ages = [2014 - year for year in years_of_birth]

# __author__ = "jhunt"
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [element for element in a if element % 2 == 0]

# print(b)

##### rock paper scissors

# a = 5 # while loop
# while (a > 0):
#   print(a)
#   a -= 1

# quit = input("type 'enter' to quit: ")
# while quit != "enter":
#   quit = input("type 'enter' to quit: ")

# i = 5 # infinite loop
# while i > 0:
#   print("inside the loop")

# while True: # break statements 
#   usr_command = input("enter your command: ")
#   if usr_command == "quit":
#     break 
#   else: 
#     print("you typed " + usr_command)

# import sys 

# user1 = input("what's your name?")
# user2 = input("and your name?")
# user1_answer = input("%s, do you want to choose rock, paper or scissors?" % user1)
# user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

# def compare(u1, u2):
#   if u1 == u2:
#     return("it's a tie!")
#   elif u1 == "rock":
#     if u2 == "scissors":
#       return("rock wins!")
#     else: 
#       return("paper wins!")
#   elif u1 == "scissors":
#     if u2 == "paper":
#       return("scissors win!")
#     else: 
#       return("paper wins!")
#   elif u1 == "paper":
#     if u2 == "rock":
#       return("paper wins!")
#     else: 
#       return("scissors win!")
#   else: 
#     return("invalid input! you have not entered rock, paper or scissors, try again.")
#     sys.exit()
  
# print(compare(user1_answer, user2_answer))

# print('''please pick one:
# rock
# scissors
# paper''')

# while True:
#   game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
#   player_a = str(input("player a: "))
#   player_b = str(input("player b: "))
#   a = game_dict.get(player_a)
#   b= game_dict.get(player_b)
#   dif = a - b

#   if dif in [-1, 2]:
#     print('player a wins.')
#     if str(input('do you want to plau another game, yes or no?\n')) == 'yes':
#       continue 
#     else: 
#       print('game over.')
#       break 
#   elif dif in [-2, 1]:
#     print('player b wins')
#     if str(input('do you want to play another game, yes or no?\n')) == 'yes':
#       continue 
#     else: 
#       print('game over.')
#       break 
#   else: 
#     print('draw. please continue.')
#     print('')

# def square(x):
#   return x * x 
# print(square(5))

# def square(x):
#   return x + x 
# print(square(5))

# def square(x, y):
#   return x + y 
# print(square(1, 2))

# def square(x, y):
#   return x / y
# print(square(8, 4))

# def numbers(x, y):
#   return x - y
# print(numbers(10, 5))

##### guessing game one 

# generte a random number betwen 1 and 9 

# import random 

# rd = random.randint(1, 9)
# guess = 0 
# c = 0
# while guess != rd and guess != "exit":
#   guess = input("enter a number between 1 and 9")

#   if guess == "exit":
#     break 
#   guess = int(guess)
#   c += 1

#   if guess < rd: 
#     print("too low")
#   elif guess > rd: 
#     print("too high")
#   else: 
#     print("right")
#     print("you took only", c, "tries!")
# input()

##### check primality functions solutions (PRIME NUMBER?)

# ask the user for a number and determine whether the number is prime or not

# import sys 
# number = input("please enter a number" + "\n")
# number = int(number)
# prime = False #initiate boolean for true false, default false 
# if number > 0:
#   for x in range (2, number - 1): # this range excludes number and 1, both of which number is divisible 
#     if number % x != 0: # if number isn't evenly divisible by x, start over with thenext one 
#       continue 
#     elif number % x == 0: # if number is evenly divisible by x, it can't be prime 
#       sys.exit("not a prime number")
#   sys.exit("the number is prime") # number wasn't evenly divislbe by any x, so it's prime 
# elif number == 0: 
#   sys.exit("number is not prime") # 0 is not prime 
# else: # if number is elss than 0, the number is not prime 
#   sys.exit("number is not prime")
  
##### list ends

# take a list of numbers and make a new list with only first and last elements 

# a_list = [5, 10, 15, 20, 25]
# def list_ends(a_list):
#   return [a_list[0], a_list[len(a_list)-1]]

# print(list_ends(a_list))

##### fibonacci (sum of the previous two numbers in the sequence)

# def gen_fib():
#   count = int(input("enter a number for fibonacci"))
#   i = 1
#   if count == 0:
#     fib = []
#   elif count == 1:
#     fib = [1]
#   elif count == 2:
#     fib = [1, 1]
#   elif count > 2:
#     fib = [1, 1]
#     while i < (count - 1):
#       fib.append(fib[i] + fib[i - 1])
#       i += 1
  
#   return fib 

# print(gen_fib())

# def fibonacci():
#   num = int(input("enter a number for fibonacci"))
#   i = 1 
#   if num == 0:
#     fib = []
#   elif num == 1:
#     fib = [1]
#   elif num == 2:
#     fib = [1,1]
#   elif num > 2:
#     fib = [1,1]
#     while i < (num - 1):
#       fib.append(fib[i] + fib[i-1])
#       i += 1
#   return fib 

# print(fibonacci())

##### list remove duplicates

# write a function that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates

# this one uses a for loop
# def dedupe_v1(x):
#   y = []
#   for i in x: 
#     if i not in y:
#       y.append(i)
#   return y 

# this one uses set 
# def dedupe_v2(x):
#   return list(set(x))

# a = [1, 2, 3, 4, 3, 2, 1]
# # print(a)
# print(dedupe_v1(a))
# print(dedupe_v2(a))

##### reverse word order 
# write a function that asks the user for a long string containung multiple words. prit back the user same string except w. words reversed

# loop thru the words and insert each word at the beginning of the result 
# def reverse_v1(x):
#   y = x.split()
#   result = []
#   for word in y:
#     result.insert(0,word)
#   return " ".join(result)

# method 2
# def reverse_v2(x):
#   y = x.split()
#   return " ".join(y[::-1])

# method 3
#def reverse_v3(x):
#  y = x.split()
#  return " ".join(reversed(y))
  
# method 4 
# def reverse_v4(x):
#   y = x.split()
#   y.reverse()
#   return " ".join(y)

# test1 = input("enter a sentence: ")
# print(reverse_v1(test1))
# print(reverse_v2(test1))
# print(reverse_v3(test1))
# print(reverse_v4(test1))

##### password generator

# import random 

# a = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 8 
# b = "".join(random.sample(a,passlen))
# print(b)

# why is there size = 8
# import string 
# import random 

# def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
#   return ''.join(random.choice(chars) for _ in range(size))

# print(pw_gen(int(input("how many characters in your password?"))))

##### max of three 

# def max_of_three(a,b,c):
#   max_3 = 0 
#   if a > b:
#     if a > c: 
#       max_3 = c 
#     else: 
#       max_3 = a 
#   else: 
#     if b > c:
#       max_3 = b 
#     else: 
#       max_3 = c 
#   return max_3 
# print(max_of_three(11, 5, 7))

# import sys # this one not working either 

# if len(sys.argv) < 4: 
#   print("Usage <value1> <valu2> <value3>")
#   sys.exit ( 1 )

# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
# arg3 = sys.argv[3]

# def maxfunction(a, b, c):
#   if (a > b) and (a > c):
#     print("max value is :"), a
#   elif (b > a) and (b > c):
#     print("max value is :"), b
#   elif (c > a) and (c > b): 
#     print("max value is :"), c
  
# print(maxfunction(arg1, arg2, arg3))


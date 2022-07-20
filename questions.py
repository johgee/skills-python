##### password generator

# why is there size = 8
import string 
import random 

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
  return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input("how many characters in your password?"))))

##### max of three 
# this gives me the third number not the largest number

def max_of_three(a,b,c):
  max_3 = 0 
  if a > b:
    if a > c: 
      max_3 = c 
    else: 
      max_3 = a 
  else: 
    if b > c:
      max_3 = b 
    else: 
      max_3 = c 
  return max_3 
print(max_of_three(11, 5, 7))
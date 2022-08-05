# class Fibber(object):

#   def __init__(self):
#       self.memo = {}
    
#   def fib(self, n):
#     if n < 0: 
#       raise ValueError("no such thing as a negative")
    
#     elif n in [0, 1]:
#         return n 
    
#     if n in self.memo: 
#         return self.memo[n]

#     result = self.fib(n - 1) + self.fib(n - 2)


#     self.memo[n] = result 

#     return result 

# n = 5 
# ob1 = Fibber()
# print(ob1.fib(n))

class Fibber(object):

  def fib(n):
    if n < 0:
        raise ValueError("no such thing as a negative")

    elif n in [0, 1]:
        return n 
  
    prev_prev = 0
    prev = 1 

    for _ in range(n - 1):

        current = prev + prev_prev 
        prev_prev = prev 
        prev = current 
  
    return current 


n = 5 
ob1 = Fibber()
print(ob1.fib(n))
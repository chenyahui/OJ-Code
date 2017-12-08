# https://www.codewars.com/kata/a-chain-adding-function
class AddFunctional:
    def __init__(self,num):
        self.num = num
    
    def __call__(self, num):
        return AddFunctional(self.num + num)

    def __add__(self,num):
        return self.num + num

    def __sub__(self,num):
        return self.num - num
    
    def __eq__(self, num):
        return self.num == num

    def __str__(self):
       return str(self.num)
       
        
def add(num):
   return AddFunctional(num)

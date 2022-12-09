
class Test():
    
    no = 60

    def sum(self, a, b):
        return a+b

    def sum(self, a,b,c):
        return a+b+c

    def subtract(self, a, b):
        pass


class Main(Test):

    age = 20

    def sum(self, a, b):
        return (100-a+b)

    # def subtract(self, a, b):
    #     return a-b

    def multiply(self, a, b):
        return a*b

    


_obj = Main()

print(_obj.sum(4,6))
print(_obj.subtract(4,6))
multi_result = _obj.multiply(4,6)
print(multi_result)


print('age is ', _obj.age)
print('no is ', _obj.no)


t = Test()

t = Main()


_obj = Test()

print(_obj.subtract(2,5))

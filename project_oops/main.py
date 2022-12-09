
class Student:
    
    def __init__(self, input_age, connect_str):
        print('from constructer')
        self.age = input_age

        self.connection = connect_str
        self.connection.open()



    age_1=30

    def marks(self):
        print(self.age_1)
        print(self.age)

        self.connection.exe('select * from table_name')
        self.connection.close()

        return 'topper'

    

stu = Student(12)
print(stu.age)
mk = stu.marks()
print(mk)



print("from test1py file")
print("from test1py file updated")

money = 10.5
name="prabhakr"

count = 1

def sum(x, y):
    print(x+y)

    global count
    count += 1
    print(count)

    # if count >= 10:
    #     pass
    # else:
    #     sum()

    # if count < 10:
    #     sum()


sum(10, 20)


# read csv/excel
# Apply logic
# return result 
# send mail with result as a attachment ot in body

x = ['a','b','c','d']
print(x[0])
print(x[-1])
print(x[len(x)-1])

print(x[1:3])


for data in x:
    print(data)


print("Line No 45")
print("*****************")

print(range(5))
print(range(len(x)-1))

for i in range(len(x)):
    print(x[i])


# append
# extend

print(list.__sizeof__(x))


x.append('t')
print(x)

# print(list.__sizeof__(x))

y = ['ram','sita']

x.extend(y)
print(x)
print(list.__sizeof__(x))

t = ('a','b','c')
print(tuple.__sizeof__(t))

t = ('a','x','d','d')
print(tuple.__sizeof__(t))

# tuple
# set
# dict





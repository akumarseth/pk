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

print(type(x))
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

# tuple

t = ('a','b','c')
print(tuple.__sizeof__(t))

t = ('a','x','d','d')
print(tuple.__sizeof__(t))

print(type(t))

t_list = list(t)

print(type(t_list))

t_list.append('7')

print(tuple(t_list))


# set
t_set = {'a','2','56',1, 'a', 2}
print(t_set)
t_set.add(40)
print(t_set)

t_set.remove(2)
print(t_set)

# lis = [1,3,4,5,9,'a','b','c',4, 6, 9]
# print(list(set(lis)))


# dict

cv = {'4', 6}
print(type(cv))

dict_obj = {
    'name':'prabhakar',
    'id':1,
    'phone':323567
}

print(type(dict_obj))
print(dict_obj['name'])
print(dict_obj['id'])

print(dict_obj.keys())
print(dict_obj.values())

input_key = ['phone','name']

for x in dict_obj.keys():
    if x in input_key:
        print(f'key is {x} and value is {dict_obj[x]}')



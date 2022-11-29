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

def hello():
    print("Hello")

def pack(i, e, u):
    list = [i, e, u]
    return list
def eat_lunch(list):
    if(len(list)==0):
            print("Lunchbox is empty")
    for i in list:
        if (i == list[0]):
            print("First I eat " + str(i))
        elif(i != list[0]):
            print("Next I eat "+ str(i))


# Testing each function
# hello()
# print(pack(2, 3, 5))
# eat_lunch([3,4,5])
# eat_lunch([])
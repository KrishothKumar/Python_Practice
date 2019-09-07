# Never user list as variable name if you using list() in your program
# map and filter never accepet [] convention user list()
lists = [x for x in range(1,11)]
ls = []
print(pow(lists,2))
print(*lists,"\n")

y=list(filter(lambda x: x%2, lists)) # lambda is a fn its work like function ids()
print(y,"filter odd values \n")
# map list of element to fn(function)
y=list(map(lambda x: x%2, lists)) # lambda is a fn its work like function ids()
print(y,"map \n")

# filter list of element from fn(function)
y=list(filter(lambda x: x%2, lists)) # lambda is a fn its work like function ids()
print(y,"filter odd values \n")

# map list of element to fn
y=list(map(lambda x: x%2 == 0, lists))# lambda is a fn its work like function ids()
print(y,"map \n")

# filter list of element from fn(function)
y=list(filter(lambda x: x%2 == 0, lists))# lambda is a fn its work like function ids()
print(y,"filter even values \n")

# map fn with lambda
y = map(lambda x: x + 1, lists)
print(list(y),"map \n")

print(*[i**2 for i in lists if i%2 ==0])

for i in lists:
    lss = i+1 if i ==1 else i + 3 if i <=5 else i + 5 # one line statement of if-elif-else statement
    ls.append(lss)
print(*ls)

def ids(s):
    for i in s:
        if i%2 ==0:  # if i%2 means if its gives 0 skip that process
            print(i)

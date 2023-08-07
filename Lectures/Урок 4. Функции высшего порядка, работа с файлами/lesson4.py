# def f(x):
#     return x*x

# a = f
# print(f(5))
# print(a(5))

# def calc1(a,b):
#     return a + b

# def calc2(a,b):
#     return a * b

# def math(op,x,y):
#     print(op(x,y))
# calc1 = lambda a,b : a + b

# math(lambda a,b: a + b,5,45)


# list_1 = [1,2,3,5,8,15,23,38]
# # def even_squares(list_1):
# #     return [(item, item ** 2) for item in list_1 if item % 2 == 0]
# # print(even_squares(list_1))
# def select(f,col):
#     return [f(x) for x in col]

# def where(f,col):
#     return [x for x in col if f(x)]

# res = select(int,list_1)
# print(res)
# res = where(lambda x: x % 2 == 0,res)
# print(res)
# res = list(select(lambda x: (x ,x **2),res))
# print(res)

# list_1 = [x for x in range(1,20)]
# print(list_1)
# list_1 = list(map(lambda x : x + 10,list_1))
# print(list_1)

# data = '15 195 21 52 95 12'
# print(data)

# data = list(map(int,data.split()))
# print(data)

# data = [15, 65 , 9, 36 ,175]

# res = list(filter(lambda x: x % 10 == 5,data))
# print(res)

# colors = ['red','8889','blue']
# data = open('file.txt','a')
# data.writelines(colors)
# data.close()

# with open('file.txt','w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')
    
# path = 'file.txt'
# data = open(path,'r')
# for line in data:
#     print(line)
# data.close()

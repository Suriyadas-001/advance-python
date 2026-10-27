# Lambda function
# square = lambda x:x*x
# print(square(x=4))

# # map function
# # syntax :- map(function,iterable.........)
# nums = [1,2,4,5,6]
# squares = map(square,nums) # It return map type object
# print(list(squares))

# def sum(a,b):
#     return a+b

# data1 = [2,6,9,1]
# data2 = [6,3,7,2]
# result = list(map(sum,data1,data2))

# print(result)


# filter
# syntax :- filter((function,iterable)
nums = [1,2,4,5,6]
def even(num):
    if num%2 == 0:
        return num
filtered_val = list(map(even,nums))
# output : [None, 2, 4, None, 6]
filtered_val = list(filter(even,nums))
# output : [2, 4, 6]
print(filtered_val)
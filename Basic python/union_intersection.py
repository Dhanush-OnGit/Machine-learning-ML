def union_intersection(fir,sec):
    union = list(set(fir) | set(sec))
    intersection = list(set(fir) & set(sec))
    return union, intersection
num1 = [1,2,3,4,5]
num2 = [3,4,5,6,7]
print(num1)
print(num2)
result = union_intersection(num1,num2)
print("union set of two list")
print(result[0])
print("intersection of two list")
print(result[1])
color1 = ["red","green","blue"]
color2 = ["red","white","pink","black"]
print(color1)
print(color2)
result = union_intersection(color1,color2)
print("union of two list")
print(result[0])
print("intersection of two list")
print(result[1])


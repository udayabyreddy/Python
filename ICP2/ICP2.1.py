lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())

    lst.append(element)

new_list = [i * 0.454 for i in lst]

print(new_list)
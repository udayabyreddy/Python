

g = input("please enter a string: ")



k=g.strip()
k=k.replace(k[len(k)-2],'')
k=k.replace(k[len(k)-2],'')

def my_function(x):
  return x[::-1]

mytxt = my_function(k)

print(mytxt)
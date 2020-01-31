text = open("text.txt","r")

final = dict()

for line in text:

    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in final:
            final[word] = final[word] + 1
        else:
            final[word] = 1

for i in list(final.keys()):
    print(i, ":", final[i])

f=open("finaltext.txt","w")
f.write(str(final))
f.close()
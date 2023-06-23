f = open("1.txt", encoding="utf-8")
a = f.readlines()
f1 = open("2.txt", "w")
print(a)
i = 0
while i < len(a):
    b = a[i].split()
    print(b)
    c = ""
    for k in b:
        k += " "
        c += k
    c += "\n"
    a[i] = c
    i += 1

f1.writelines(a)
1

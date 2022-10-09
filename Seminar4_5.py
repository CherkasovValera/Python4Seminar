with open("filea.txt", "r") as filea:
    data1 = filea.read()

if len(data1) > 20:
    a1, b1, c1 = int(data1[0]), int(data1[9]), int(data1[18])
    print(a1, b1, c1)
elif len(data1) > 8:
    a1, b1, c1 = int(data1[0]), int(data1[9]), 0
    print(a1, b1, c1)
else:
    a1, b1, c1 = int(data1[0]), 0, 0
    print(a1, b1, c1)
with open("fileb.txt", "r") as fileb:
    data2 = fileb.read()
if len(data2) > 20:
    a, b, c = int(data2[0])+a1, int(data2[9])+b1, int(data2[18])+c1
    print(a, b, c)
elif len(data2) > 8:
    a, b, c = int(data2[0])+a1, int(data2[9]), 0 +c1
    print(a, b, c)
else:
    a, b, c = int(data2[0])+a1, 0 + b1, 0 + c1
    print(a, b, c)

result = ""
if b == 0: result = f"{a}*x**2 + {c}*x**0 = 0"
if b == 0 and c == 0: result =  f"{a}*x**2 = 0"

else: result =  f"{a}*x**2 + {b}*x**1 + {c}*x**0 = 0 "

with open("file_res.txt", "w") as file_res:
    file_res.write(result)
print(result)
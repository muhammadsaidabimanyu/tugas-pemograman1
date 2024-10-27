a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
c = int(input("Masukkan bilangan C: "))

if a > b:
    if a > c:
        print("A adalah terbesar")
        terbesar = a
    else:
        print("C adalah terbesar")
        terbesar = c
else:
    if b > c:
        print("B adalah terbesar")
        terbesar = b
    else:
        print("C adalah terbesar")
        terbesar = c

print(f"Bilangan terbesar adalah: {terbesar}")
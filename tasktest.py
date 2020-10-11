X = float(input("Enter your X number"))
Y = float(input("Enter your Y number"))

signs = [(X + Y), (X - Y), (X / Y), (X * Y) or "0"]
index = 0

while True:
    print("Enter 0 to quit")
    Z = input(signs[index])
    if Z == "0":
        break
    index = (index + 1) % 3



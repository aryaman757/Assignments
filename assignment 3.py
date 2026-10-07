def is_right_angled(a, b, c):
    if a * a + b * b == c * c:
        return True
    elif a * a + c * c == b * b:
        return True
    elif b * b + c * c == a * a:
        return True
    else:
        return False


a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if is_right_angled(a, b, c):
    print("It is a right-angled triangle")
else:
    print("It is not a right-angled triangle")

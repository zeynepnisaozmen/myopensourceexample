

# TOPLAMA
def add(x, y):
    return x + y


# ÇIKARMA
def subtract(x, y):
    return x - y


# ÇARPMA
def multiply(x, y):
    return x * y


# BÖLME
def divide(x, y):
    return x / y


print("IŞLEMLER")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

while True:

    choice = input("Seçtiğiniz işlemi tuşlayınız(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("İlk sayı: "))
        num2 = float(input("ikinci sayı: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


        next_calculation = input("Yeni bir işlem yapmak ister misiniz? (evet/hayır): ")
        if next_calculation == "hayır":
            break

    else:
        print("Geçersiz Yanıt")
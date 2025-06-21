while True:
    num1 = input(f"[+] Masukan angka pertama: ")
    operator = input(f'''

    [+] Masukan operator yang anda inginkan 
    | + | - | * | / | % | // | ** |
    pilih salah satunya! 

    ''')
    num2 = input(f"[+] Masukan angka kedua: ")

    num1_int = int(num1)
    num2_int = int(num2)

    if operator == "+":
        print(f"hasilnya adalah", num1_int+num2_int)
        break

    elif operator == "-":
        print(f"hasilnya adalah", num1_int-num2_int)
        break

    elif operator == "*":
        print(f"hasilnya adalah", num1_int*num2_int)
        break

    elif operator == "/":
        print(f"hasilnya adalah", num1_int/num2_int)
        break

    elif operator == "%":
        print(f"hasilnya adalah", num1_int%num2_int)
        break

    elif operator == "//":
        print(f"hasilnya adalah", num1_int//num2_int)
        break

    elif operator == "**":
        print(f"hasilnya adalah", num1_int**num2_int)
        break

    else:
        print(f"Input yang kamu masukan salah, berikan input yang benar")
        continue



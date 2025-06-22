while True:
    try:
        print(f'''

                    __
 ___ ____________ _/ /
/ _ `/ __/ __/ _ `/ / 
\_,_/_/  \__/\_,_/_/  
arithmetic-calculator
              
SIMPLE CALCULATOR WITH PYTHON :) start with math and py

''')

        num1 = input(f"[+] Masukan angka pertama: ")
        operator = input(f'''

[+] Masukan operator yang anda inginkan
                          
|  +  |  -  |  *  |  /  |  %  |  //  |  **  |

PILIH SALAH SATU OPERATOR!: ''')
        num2 = input(f"\n[+] Masukan angka kedua: ")

        num1_int = int(num1)
        num2_int = int(num2)

        if operator == "+":
            print(f"\nhasilnya adalah", num1_int+num2_int)
            break

        elif operator == "-":
            print(f"\nhasilnya adalah", num1_int-num2_int)
            break

        elif operator == "*":
            print(f"\nhasilnya adalah", num1_int*num2_int)
            break

        elif operator == "/":
            print(f"\nhasilnya adalah", num1_int/num2_int)
            break

        elif operator == "%":
            print(f"\nhasilnya adalah", num1_int%num2_int)
            break

        elif operator == "//":
            print(f"\nhasilnya adalah", num1_int//num2_int)
            break

        elif operator == "**":
            print(f"\nhasilnya adalah", num1_int**num2_int)
            break

        else:
            print(f"\nInput yang kamu masukan salah, berikan input yang benar")
            continue

    except ValueError:
        print(f"\nberikan inputan dengan format yang sesuai")
        break

    except ZeroDivisionError:
        print(f"\nPembagian dengan pembagi nol tidak di izinkan.")
        break

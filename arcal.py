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

        num1 = input(f"[+] Masukan angka pertama(bebas): ")
        operator = input(f'''

[+] Masukan operator yang anda inginkan
                          
|  +  |  -  |  *  |  /  |  %  |  //  |  **  |

PILIH SALAH SATU OPERATOR!: ''')
        num2 = input(f"\n[+] Masukan angka kedua(bebas): ")

        num1_float = float(num1)
        num2_float = float(num2)

        if operator == "+":
            print(f"\nhasilnya adalah", num1_float+num2_float)
            

        elif operator == "-":
            print(f"\nhasilnya adalah", num1_float-num2_float)
        

        elif operator == "*":
            print(f"\nhasilnya adalah", num1_float*num2_float)
            

        elif operator == "/":
            print(f"\nhasilnya adalah", num1_float/num2_float)
            

        elif operator == "%":
            print(f"\nhasilnya adalah", num1_float%num2_float)
            

        elif operator == "//":
            print(f"\nhasilnya adalah", num1_float//num2_float)
            

        elif operator == "**":
            print(f"\nhasilnya adalah", num1_float**num2_float)
            

        else:
            print(f"\nInput yang kamu masukan salah, berikan input yang benar")
            continue

        lanjut = input("\nHitung lagi? (ya/ga): ").lower()
        if lanjut != "ya":
            break

    except ValueError:
        print(f"\nberikan inputan dengan format yang sesuai")
        break

    except ZeroDivisionError:
        print(f"\nPembagian dengan pembagi nol tidak di izinkan.")
        break

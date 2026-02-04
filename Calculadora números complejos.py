def complex_addition(num1:tuple, num2: tuple) -> tuple:
    r = num1[0] + num2[0]
    c = num1[1] + num2[1]
    return r,c

def complex_subtraction(num1:tuple, num2: tuple) -> tuple:
    r = num1[0] - num2[0]
    c = num1[1] - num2[1]
    return r,c

def complex_multiplication(num1:tuple, num2: tuple) -> tuple:
    r = (num1[0] * num2[0]) - (num1[1] * num2[1])
    c = (num1[0] * num2[1]) + (num2[0] * num1[1])
    return r, c

def complex_division(num1: tuple, num2: tuple) -> tuple:
     r = ((num1[0] * num2[0]) + (num1[1] * num2[1]))/ round(complex_modulus(num2) ** 2)
     c = ((-(num1[0] * num2[1]) + (num2[0] * num1[1])))/ round(complex_modulus(num2) ** 2)
     return int(r), int(c)

def complex_modulus(num1: tuple) -> tuple:
    answer = ((num1[0]**2) + (num1[1]**2)) ** (1/2)
    return answer

def complex_conjugation(num1: tuple) -> tuple:
    r = num1[0]
    c = num1[1] * -1
    return r,c
    
def string_to_complex(num: str) -> tuple:
    remove_pharenteses = num.strip("()")
    numbers = remove_pharenteses.split(",")
    numbers = [int(i) for i in numbers]
    r,c = numbers[0], numbers[1]   
    return r,c

def main():
    # Recursos para usar
    message_1 = ["                                             ████                                             ████                      ████             █████                      ",
                 "                                            ░░███                                            ░░███                     ░░███            ░░███                       ",
                 "  ██████   ██████  █████████████   ████████  ░███   ██████  █████ █████     ██████   ██████   ░███   ██████  █████ ████ ░███   ██████   ███████    ██████  ████████ ",
                 " ███░░███ ███░░███░░███░░███░░███ ░░███░░███ ░███  ███░░███░░███ ░░███     ███░░███ ░░░░░███  ░███  ███░░███░░███ ░███  ░███  ░░░░░███ ░░░███░    ███░░███░░███░░███",
                 "░███ ░░░ ░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███████  ░░░█████░     ░███ ░░░   ███████  ░███ ░███ ░░░  ░███ ░███  ░███   ███████   ░███    ░███ ░███ ░███ ░░░ ",
                 "░███  ███░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███░░░    ███░░░███    ░███  ███ ███░░███  ░███ ░███  ███ ░███ ░███  ░███  ███░░███   ░███ ███░███ ░███ ░███     ",
                 "░░██████ ░░██████  █████░███ █████ ░███████  █████░░██████  █████ █████   ░░██████ ░░████████ █████░░██████  ░░████████ █████░░████████  ░░█████ ░░██████  █████    ",
                 " ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░███░░░  ░░░░░  ░░░░░░  ░░░░░ ░░░░░     ░░░░░░   ░░░░░░░░ ░░░░░  ░░░░░░    ░░░░░░░░ ░░░░░  ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░     ",
                 "                                   ░███                                                                                                                             ",
                 "                                   █████                                                                                                                            ",
                 "                                  ░░░░░                                                                                                                             "]
    division_line = "=============================================================="
    options = ["1. Suma", "2. Resta", "3. Muliplicación",
               "4. División", "5. Módulo", "6. Conjugado"]
    
    # =======================================================
    
    for i in message_1:
        print(i)        
    print(division_line)         
    for i in options:
        print (i)
    selection = int(input("Seleccione una operación: "))
    print(division_line)
    
    if selection == 1:
        print("SUMA")
        c_1 = string_to_complex(input("Escriba C_1 como una tupla: "))
        c_2 = string_to_complex(input("Escriba C_2 como una tupla: "))
        answer = complex_addition(c_1, c_2)
        print(f"Su resultado es {answer}")
        
    elif selection == 2:
        print("RESTA")
        c_3 = string_to_complex(input("Escriba C_1 como una tupla: "))
        c_4 = string_to_complex(input("Escriba C_2 como una tupla: "))
        answer = complex_subtraction(c_3, c_4)
        print(f"Su resultado es {answer}")
        
    elif selection == 3:
        print("MULTIPLICACIÓN")
        c_5 = string_to_complex(input("Escriba C_1 como una tupla: "))
        c_6 = string_to_complex(input("Escriba C_2 como una tupla: "))
        answer = complex_multiplication(c_5, c_6)
        print(f"Su resultado es {answer}")
        
    elif selection == 4:
        print("DIVISIÓN")
        c_7 = string_to_complex(input("Escriba C_1 como una tupla: "))
        c_8 = string_to_complex(input("Escriba C_2 como una tupla: "))
        answer = complex_division(c_7, c_8)
        print(f"Su resultado es {answer}")

    elif selection == 5:
        print("MÓDULO")
        c_9 = string_to_complex(input("Escriba C_1 como una tupla: "))
        answer = complex_modulus(c_9)
        print(f"Su resultado es {answer}")
                
    elif selection == 6:
        print("CONJUGADO")
        c_10 = string_to_complex(input("Escriba C_1 como una tupla: "))
        answer = complex_conjugation(c_10)
        print(f"Su resultado es {answer}")
        
        
main()


















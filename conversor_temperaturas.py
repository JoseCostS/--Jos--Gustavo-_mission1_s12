class ConversorTemperaturas:
    def __init__(self):
        pass
    
    def converter_c_para_f(valor_f):
        valor_c = valor_f * 1.8 + 32
        return valor_c
    
    def converter_f_para_c(valor_c):
        valor_f = (valor_c - 32) / 1.8
        return valor_f
    
def menu():

    print("Conversor de Temperaturas")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")
    while True:
        opc=input("escolha a opção desejada: ")

        if opc == '1' :

            valor_c=float(input('Digite o valor de Celsius: '))
            resultado=ConversorTemperaturas.converter_c_para_f(valor_c)
            print("Celsius =",resultado)
            break

        elif opc == "2" :

            valor_f=float(input('Digite o valor de Fahrenheit: '))
            resultado=ConversorTemperaturas.converter_f_para_c(valor_f)
            print("Fahrenheit =",resultado)
            break

        elif opc == '3':
            print("Saindo do conversor...")
            break

        else:
            print("Opção invalida, Tente novamente.")
            continue
menu()
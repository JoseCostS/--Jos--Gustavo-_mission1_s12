class ConversorMedidas:
    def __init__(self):
      pass
    
    def converter_cm_para_m(valor_cm):
        valor_m = valor_cm / 100
        return valor_m

    def converter_m_para_cm(valor_m):
        valor_cm = valor_m * 100
        return valor_cm
def menu():

    print("Conversor de Medidas")
    print("1. Centímetros para Metros")
    print("2. Metros para Centímetros")
    print("3. Sair")
    while True:
        opc=input("escolha a opção desejada: ")

        if opc == '1' :

            valor_cm=float(input('Digite o valor de Centímetros: '))
            resultado=ConversorMedidas.converter_cm_para_m(valor_cm)
            print("Centímetros =",resultado)
            break

        elif opc == "2" :

            valor_m=float(input('Digite o valor de Metros: '))
            resultado=ConversorMedidas.converter_m_para_cm(valor_m)
            print("Metros =",resultado)
            break

        elif opc == '3':
            print("Saindo do conversor...")
            break

        else:
            print("Opção invalida, Tente novamente.")
            continue
menu()  
from conversor_medidas import ConversorMedidas
from conversor_temperaturas import ConversorTemperaturas

print('''
1. Conversor de Centímetros para Metros
2. Conversor de Metros para Centímentros
3. Conversor de Fahrenheit para Celsius
4. Conversor de Celsius para Fahrenheit''')

opc=input("Escolha uma opção: ")
valor=float(input("Digite o valor: "))
if opc == "1": 
    resultado=ConversorMedidas.converter_cm_para_m(valor)
elif opc == "2":
    resultado=ConversorMedidas.converter_m_para_cm(valor)
elif opc == "3":
    resultado=ConversorTemperaturas.converter_f_para_c(valor)
elif opc == "4":
    resultado=ConversorTemperaturas.converter_c_para_f(valor)
else:
   print("não tem essa opção")
print(resultado)
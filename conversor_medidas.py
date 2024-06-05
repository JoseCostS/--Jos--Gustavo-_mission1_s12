class ConversorMedidas:
    def __init__(self):
      pass
    
    def converter_cm_para_m(valor_cm):
        valor_metros = valor_cm / 100
        return valor_metros

    
    def converter_m_para_cm(valor_m):
        valor_cm = valor_m * 100
        return valor_cm
      

# Testing Area
# Vamos testar e converter 100cm para metros
resultado = ConversorMedidas.converter_m_para_cm(1)

# O resultado esperando é 1 metro
print('Resultado: ', resultado)
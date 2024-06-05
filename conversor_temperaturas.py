class ConversorTemperaturas:
    def __init__(self):
        pass
    
    def converter_c_para_f(valor_c):
        valor_f = valor_c * 1.8 + 32
        return valor_f
    
    def converter_f_para_c(valor_f):
        valor_c = (valor_f) - 32 / 1.8
        return valor_c
    
   
resultado=ConversorTemperaturas.converter_f_para_c(40)
print(resultado)
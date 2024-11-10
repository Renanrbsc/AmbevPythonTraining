
def calculo_inss(salario): # BLOCO DE CODIGO def, recebe o valor de salario no parametro
    if salario >= 0 and salario <= 1751.81:
        inss = salario * 0.08
    elif salario >= 1751.82 and salario <= 2919.72:
        inss = salario * 0.095
    elif salario >= 2919.72 and salario <= 5839.45:
        inss = salario * 0.11
    else:
        inss = 642.33
    return inss # retorna o valor para quem chamou o bloco de codigo DEF

def calculo_irrf(salario,inss):
    irrf = 0
    if salario > 1903.98 and salario <= 2826.65:
        irrf = (salario - inss) * 0.075
    elif salario > 2826.66 and salario <= 3751.05:
        irrf = (salario - inss) * 0.15
    elif salario > 3751.06 and salario <= 4664.68:
        irrf = (salario - inss) * 0.225
    else:
        irrf = (salario - inss) * 0.275
    return irrf

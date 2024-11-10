def calculoISS(op):
    if op == 1:
        orcamento = float(input('Digite o Orçamento da empresa:'))
        iss = 0.02
        desconto = orcamento * iss
        return {'orcamento':orcamento,'iss':iss,'desconto':desconto}

    else:
        orcamento = float(input('Digite o Orçamento da empresa:'))
        iss = 0.05
        desconto = orcamento * iss
        return {'orcamento':orcamento,'iss':iss,'desconto':desconto}

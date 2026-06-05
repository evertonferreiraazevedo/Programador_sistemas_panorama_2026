valor_hora = float(input("Quando vc vale? "))
horas_trabalhadas = float(input("Quantas h trabalhadas"))

sal_bruto = valor_hora * horas_trabalhadas
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindicato = sal_bruto * 0.05
sal_liquido = sal_bruto - ir - inss - sindicato
print(f"""Salario bruto R${sal_bruto}
      salario liquido R${sal_liquido}
      IR R${ir}
      INSS R${inss}
      sindicato R${sindicato}""")
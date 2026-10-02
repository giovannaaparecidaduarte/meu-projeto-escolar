# revisando a logica booleana

#----simulador de criterios escolares----

# 1 dados exxemplo do aluno
nota_final = 7.5
frequencia = 0.85 # frequencia em decimal (85%)
historico_ruim = False # historico ruim do aluno (tre ou false)
eh_atleta = True # o aluno é atleta (true ou false)

print("=== Analise Cadastral do Aluno===")

#----------------------------------------------
# Cenario 1: Operador AND (aprovaçao resgular)
# criterio: nota maior ou igual a 7.0 e frequencia maior ou igual  a 75%
#----------------------------------------------

passou_por_media = nota_final >= 7.0
passou_por_frequencia = frequencia >= 0.75
aprovado_regular = passou_por_media and passou_por_frequencia


print(f"Passou por média: {passou_por_media}")
print(f"Passou por frequência: {passou_por_frequencia}")
print(f"Aprovado Regular: {aprovado_regular}")


# ---------------------------------------------------------------------
# Cenário 2: Operador OR (Bolsa de Incentivo)
# Critério: Nota fantástica (>= 9.0) OU ser atleta da escola
# ---------------------------------------------------------------------
nota_fantastica = nota_final >= 9.0
eh_atleta = eh_atleta  # Já é um valor booleano
bolsa_incentivo = nota_fantastica or eh_atleta

print(f"Nota Fantástica: {nota_fantastica}")
print(f"É Atleta: {eh_atleta}")
print(f"Bolsa de Incentivo: {bolsa_incentivo}")


# ---------------------------------------------------------------------
# Cenário 3: Operador NOT (Ficha Limpa)
# Critério: O aluno NÃO pode ter um histórico ruim para ser
# monitor
# ---------------------------------------------------------------------

pode_ser_monitor = not historico_ruim
print(f"3. Elegível para monitor: {pode_ser_monitor}")


# ---------------------------------------------------------------------
# Cenário 4: Misturando tudo (Aprovação de Aluno Atleta)
# Critério: (Nota >= 6.0 E Presença >= 70%) E ser atleta
# -

aprovacao_especial = (nota_final >= 6.0 and frequencia >= 0.70) and eh_atleta
print(f"4. Aprovado pelo critério especial de atleta? {aprovacao_especial}")
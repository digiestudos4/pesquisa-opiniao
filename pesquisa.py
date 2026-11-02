
excelente = 0
bom = 0
ruim = 0

for i in range(1, 51):
    print("\n--- Pesquisa de Atendimento ---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    opiniao = int(input("Digite sua opinião (1-Excelente, 2-Bom, 3-Ruim): "))

    if opiniao == 1:
        excelente += 1

    elif opiniao == 2:
        bom += 1

    elif opiniao == 3:
        ruim += 1
print("\n===== RESULTADO DA PESQUISA =====")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
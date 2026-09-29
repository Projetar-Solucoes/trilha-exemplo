# Central de Solicitações — versão 2 (semana 2): menu e validação
solicitacoes = []
while True:
    print("\n1 - Cadastrar  2 - Listar  0 - Sair")
    opcao = input("Escolha: ").strip()
    if opcao == "1":
        assunto = input("Assunto: ").strip()
        if not assunto:
            print("O assunto não pode ficar vazio.")
            continue
        solicitacoes.append(assunto)
        print("Cadastrada!")
    elif opcao == "2":
        for numero, assunto in enumerate(solicitacoes, start=1):
            print(f"{numero}. {assunto}")
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")

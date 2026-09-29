# Central de Solicitações — versão 3 (semana 3): funções, módulos e JSON
from armazenamento import carregar, salvar


def cadastrar(solicitacoes: list[dict]) -> None:
    assunto = input("Assunto: ").strip()
    if not assunto:
        print("O assunto não pode ficar vazio.")
        return
    solicitacoes.append({"assunto": assunto, "status": "Aberta"})
    salvar(solicitacoes)
    print("Cadastrada!")


def listar(solicitacoes: list[dict]) -> None:
    for numero, s in enumerate(solicitacoes, start=1):
        print(f"{numero}. {s['assunto']} ({s['status']})")
    print(f"Total: {len(solicitacoes)} solicitação(ões)")


def main() -> None:
    solicitacoes = carregar()
    while True:
        opcao = input("\n1 - Cadastrar  2 - Listar  0 - Sair\nEscolha: ").strip()
        if opcao == "1":
            cadastrar(solicitacoes)
        elif opcao == "2":
            listar(solicitacoes)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 0.")


if __name__ == "__main__":
    main()

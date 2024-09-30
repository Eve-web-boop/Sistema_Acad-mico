import time

print('=-' * 20)
print('           SISTEMA ACADÊMICO')
print('=-' * 20)
time.sleep(1)

alunos = []

def menu():
    print("\nMENU PRINCIPAL")
    print("1 - Adicionar aluno(a)")
    print("2 - Editar aluno(a)")
    print("3 - Excluir aluno(a)")
    print("4 - Adicionar notas")
    print("5 - Listar alunos(as)")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def adicionar_aluno():
    nome = input("Digite o nome do aluno(a): ")
    alunos.append({"nome": nome, "notas": []}) 
    print(f"Aluno(a) {nome} adicionado com sucesso!\n")

def editar_aluno():
    listar_alunos()
    if alunos:
        nome = input("Digite o nome do aluno(a) que deseja editar: ")
        for aluno in alunos:
            if aluno['nome'] == nome:
                novo_nome = input("Digite o novo nome do aluno(a): ")
                aluno['nome'] = novo_nome
                print("Informações atualizadas com sucesso!\n")
                return
        print("Aluno(a) não encontrado!\n")

def excluir_aluno():
    listar_alunos()
    if alunos:
        nome = input("Digite o nome do aluno(a) que deseja excluir: ")
        for aluno in alunos:
            if aluno['nome'] == nome:
                alunos.remove(aluno)
                print(f"Aluno(a) {aluno['nome']} excluído com sucesso!\n")
                return
        print("Aluno(a) não encontrado!\n")

def adicionar_notas():
    listar_alunos()
    if alunos:
        nome = input("Digite o nome do aluno(a) para adicionar notas: ")
        for aluno in alunos:
            if aluno['nome'] == nome:
                aluno['notas'] = []
                for i in range(4): 
                    nota = float(input(f"Digite a Nota {i + 1}: "))
                    aluno['notas'].append(nota)
                    print(f"Nota {nota} adicionada com sucesso!")
                return
        print("Aluno(a) não encontrado!\n")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno(a) cadastrado.\n")
    else:
        print("\nLista de alunos:")
        for i, aluno in enumerate(alunos, start=1):
            notas_str = ", ".join(map(str, aluno['notas'])) 
            print(f"{i}. Nome: {aluno['nome']}, Notas: {notas_str}")
        print()

while True:
    opcao = menu()

    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        editar_aluno()
    elif opcao == '3':
        excluir_aluno()
    elif opcao == '4':
        adicionar_notas()
    elif opcao == '5':
        listar_alunos()
    elif opcao == '6':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")

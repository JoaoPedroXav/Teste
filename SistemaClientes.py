# Lista global para armazenar os clientes
clientes = []

# Variável para controlar o proximo ID
proximo_id = 1

"""Função para cadastrar um novo cliente no sistema. Solicita nome, telefone e serviço contratado."""
def cadastrar_cliente():
   
    global proximo_id
    
    print("\nCADASTRAR NOVO CLIENTE")
    
    # Solicita e valida o nome
    nome = input("Digite o nome do cliente: ").strip()
    if not nome:
        print("Erro: O nome não pode estar vazio.")
        return
    
    # Solicita e valida o telefone
    telefone = input("Digite o telefone do cliente: ").strip()
    if not telefone:
        print("Erro! O telefone não pode estar vazio.")
        return
    
    # Solicita e valida o serviço contratado
    servico = input("Digite o serviço contratado: ").strip()
    if not servico:
        print("Erro! O serviço não pode estar vazio.")
        return
    
    # Cria o dicionário do cliente
    cliente = {
        "id": proximo_id,
        "nome": nome,
        "telefone": telefone,
        "serviço": servico
    }
    
    # Adiciona o cliente na lista
    clientes.append(cliente)
    proximo_id += 1
    
    print(f"\nCliente '{nome}' cadastrado com sucesso! ID: {cliente['id']}")

"""Função para listar todos os clientes cadastrados. Exibe as informações de cada cliente de forma organizada."""
def listar_clientes():
    
    print("\nLISTA DE CLIENTES")
    
    if not clientes:
        print("Nenhum cliente cadastrado no sistema.")
        return
    
    print(f"\nTotal de clientes cadastrados: {len(clientes)}\n")
    
    for cliente in clientes:
        print(f"ID: {cliente['id']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"Serviço: {cliente['serviço']}")
        print("-" * 40)

"""Função para atualizar os dados de um cliente existente.Permite editar nome, telefone e serviço contratado."""
def atualizar_cliente():
   
    print("\nATUALIZAR CLIENTE")
    
    if not clientes:
        print("Nenhum cliente cadastrado no sistema.")
        return
    
    # Solicita o ID do cliente
    try:
        id_busca = int(input("Digite o ID do cliente que deseja atualizar: "))
    except ValueError:
        print("Erro! ID inválido. Digite apenas números.")
        return
    
    # Busca o cliente pelo ID
    cliente_encontrado = None
    for cliente in clientes:
        if cliente["id"] == id_busca:
            cliente_encontrado = cliente
            break
    
    if not cliente_encontrado:
        print(f"Cliente com ID {id_busca} não encontrado.")
        return
    
    # Exibe os dados atuais
    print("\nDados atuais do cliente:")
    print(f"Nome: {cliente_encontrado['nome']}")
    print(f"Telefone: {cliente_encontrado['telefone']}")
    print(f"Serviço: {cliente_encontrado['serviço']}")
    
    # Solicita novos dados
    print("\nDigite os novos dados (pressione Enter para manter o valor atual):")
    
    novo_nome = input(f"Novo nome [{cliente_encontrado['nome']}]: ").strip()
    if novo_nome:
        cliente_encontrado['nome'] = novo_nome
    
    novo_telefone = input(f"Novo telefone [{cliente_encontrado['telefone']}]: ").strip()
    if novo_telefone:
        cliente_encontrado['telefone'] = novo_telefone
    
    novo_servico = input(f"Novo serviço [{cliente_encontrado['serviço']}]: ").strip()
    if novo_servico:
        cliente_encontrado['serviço'] = novo_servico
    
    print("\nCliente atualizado com sucesso!")

"""Função para remover um cliente do sistema. Solicita confirmação antes de excluir."""
def remover_cliente():
    
    print("\nREMOVER CLIENTE")
    
    if not clientes:
        print("Nenhum cliente cadastrado no sistema.")
        return
    
    # Solicita o ID do cliente
    try:
        id_busca = int(input("Digite o ID do cliente que deseja remover: "))
    except ValueError:
        print("Erro! ID inválido. Digite apenas números.")
        return
    
    # Busca o cliente pelo ID
    cliente_encontrado = None
    indice = -1
    for i, cliente in enumerate(clientes):
        if cliente["id"] == id_busca:
            cliente_encontrado = cliente
            indice = i
            break
    
    if not cliente_encontrado:
        print(f"Cliente com ID {id_busca} não encontrado.")
        return
    
    # Exibe os dados e solicita confirmação
    print("\nCliente encontrado:")
    print(f"Nome: {cliente_encontrado['nome']}")
    print(f"Telefone: {cliente_encontrado['telefone']}")
    print(f"Serviço: {cliente_encontrado['serviço']}")
    
    confirmacao = input("\nDeseja realmente remover este cliente? (S/N): ").strip().upper()
    
    if confirmacao == "S":
        clientes.pop(indice)
        print("\nCliente removido com sucesso!")
    else:
        print("\nRemoção cancelada.")

"""Função para gerar um relatorio resumido do sistema. Exibe total de clientes e lista de serviços contratados."""
def gerar_relatorio():
    
    print("\n  RELATÓRIO DO SISTEMA   ")
    
    if not clientes:
        print("Nenhum cliente cadastrado no sistema.")
        return
    
    # Total de clientes
    total_clientes = len(clientes)
    print(f"\nTotal de clientes cadastrados: {total_clientes}")
    
    # Conta os serviços contratados
    servicos = {}
    for cliente in clientes:
        servico = cliente['serviço']
        if servico in servicos:
            servicos[servico] += 1
        else:
            servicos[servico] = 1
    
    # Exibe os serviços
    print("\nServiços contratados:")
    for servico, quantidade in servicos.items():
        print(f"- {servico}: {quantidade} cliente(s)")
    
    print("\nTotal de servicos diferentes: " + str(len(servicos)))

"""Função principal que exibe o menu e controla o fluxo do programa."""
def menu():
    
    while True:
        print("SISTEMA DE GERENCIAMENTO DE CLIENTES")
        print("1 - Cadastrar novo cliente")
        print("2 - Listar todos os clientes")
        print("3 - Atualizar dados de um cliente")
        print("4 - Remover cliente")
        print("5 - Gerar relatório")
        print("6 - Sair do sistema")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            atualizar_cliente()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            print("\nEncerrando o sistema")
            print("Obrigado por utilizar o Sistema de Gerenciamento de Clientes!")
            break
        else:
            print("\nOpção inválida! Por favor, escolha uma opção de 1 a 6.")


# Executa o programa
if __name__ == "__main__":
    menu()
import re

opcoes =  """
Faca o seu cadastro abaixo: 
[1] Nome: 
[2] Email: 
[3] CPF: 
[4] Data atual: 
[5] Telefone: 
[6] CEP: 
[7] Visualizar cadastros
[0] Sair
"""

cadastro  = []

cadastro_atual = {}


def cadastro_completo(d):
    for campo in ["Nome", "Email", "CPF", "Data", "Telefone", "CEP"]:
        if campo not in d:
            return False
    return True

while True:
        opcao = int(input(opcoes))
    
        if opcao == 1:
            cadastro_atual["Nome"] = input("Digite o seu nome: ")
            print("Nome cadastrado")
    
        elif opcao == 2:
            email = input("Digite o seu email: ")
            if re.fullmatch(r"[A-z0-9._%+-]+@[A-Za-z0-9_.%+-]+\.[A-Za-z]{2,}", email):
                cadastro_atual["Email"] = email
                print("Email cadastrado")
            else:
                print("Email inválido")

        elif opcao == 3:
            cpf = input("Digite o seu CPF: ")
            if re.fullmatch(r"\d{3}.\d{3}.\d{3}-\d{2}", cpf):
                cadastro_atual["CPF"] = cpf
                print("CPF cadastrado")
            else:
                print(f"CPF inválido")

        elif opcao == 4:
            data = input("Insira a data atual com as barras: ")
            if re.fullmatch(r"\d{2}\/\d{2}\/\d{4}", data):
                cadastro_atual["Data"] = data
                print("Data cadastrada")
            else:
                print("Digite a data correta")

        elif opcao == 5:
            telefone= input("Digite um número de teleofone com DDD: ")
            if re.fullmatch(r"\(\d{2}\) \d{4,5}-\d{4}|\d{2} \d{4,5}-\d{4}", telefone):
                cadastro_atual["Telefone"] = telefone
                print("Telefone cadastrado")
            else:
                print(f"{telefone} é inválido, por favor insira um número válido")
            
        elif opcao == 6:
            cep = input("Insira o CEP corretamente: ")
            if re.fullmatch(r"\d{5}-\d{3}", cep):
                cadastro_atual["CEP"] = cep
                print("CEP cadastrado")
            else:
                print(f"{cep} é inválido, por favor insira um válido")

        if cadastro_completo(cadastro_atual):
            cadastro.append(cadastro_atual.copy())
            print("Cadastrado")
            cadastro_atual.clear()
        
        elif opcao == 7:
            if not cadastro:
                print("Nenhum cadastro relaizado")
            else:
                for idx, c in enumerate(cadastro, 1):
                    print(f"""
--- Cadastro {idx} ---
Nome: {c.get('Nome', 'Não informado')}
Email: {c.get('Email', 'Não informado')}
CPF: {c.get('CPF', 'Não informado')}
Data: {c.get('Data', 'Não informado')}
Telefone: {c.get('Telefone', 'Não informado')}
CEP: {c.get('CEP', 'Não informado')}
""")
        elif opcao == 0:
            print("Saindo do cadastro")
            break
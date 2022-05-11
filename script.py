import mysql.connector # Biblioteca necessária para realizar a conexão entre o Python e o banco de dados MySQL

conexao = mysql.connector.connect(
    host='', # Caso o banco de dados esteja na sua máquina, utiliza-se "localhost"
    user='', # Nome do usuário do banco de dados, por padrão o MySQL define como "root"
    password='', # Senha para acessar seu usuário do Banco de Dados
    database='', # Nome do Banco de Dados que será utilizado
)

cursor = conexao.cursor() # Cursor seria quem executará as funções. A função conexao.cursor() é utilizada para criar a conexão com banco de dados
escolha = [0, 1, 2, 3, 4] # Opções a serem escolhidas

while True:
    try:
        print('-'*30)
        opc = int(input("""Escolha uma opção:
1- Novo cadastro (CREATE);
2- Usuários cadastrados (READ);
3- Alterar senha (UPDATE); 
4- Remover cadastro (DELETE);
0- Sair

Opção: """))

        if opc not in escolha:
            print('Opção inválida')
            continue
        elif opc == 1: # CREATE
            nome = input('Usuário: ')
            valor = input('Senha: ')

            comando = f'INSERT INTO usuarios (login, senha) VALUES ("{nome}", "{valor}")'
            cursor.execute(comando) # Execução do comando acima
            conexao.commit() # Realizado alteração no banco de dados
        elif opc == 2: # READ
            comando = f'SELECT * FROM usuarios' # Puxa todos os valores da tabela
            cursor.execute(comando) # Execução do comando acima
            resultado = cursor.fetchall() # Salva a tabela dentro da variável RESULTADO

            for users in resultado: # Percorrer a tabela salva e exibida na tela
                print(f'Usuário: {users[1]}\nsenha: {users[2]}\n')
        elif opc == 3: # UPDATE
            nome = input('Informe o usuário que deseja alterar a senha: ')
            
            while True:
                valor = input('Nova Senha: ')
                valor2 = input('Repita a senha: ')

                if valor != valor2: # Função para validar se as duas senhas foram inseridas iguais
                    print('As senhas são diferentes, tente novamente')
                    continue
                else:
                    print('\nSenha alterada com sucesso!')
                    break

            comando = f'UPDATE usuarios SET senha = "{valor}" WHERE login = "{nome}"' # Realizado alteração da senha
            cursor.execute(comando) # Executa o comando acima de UPDATE
            conexao.commit() # Comitado no banco de dados a alteração executada
        elif opc == 4: # DELETE
            nome = input('Usuário: ')

            comando = f'DELETE FROM usuarios WHERE login = "{nome}"' # Realiza a exclusão do usuário informado

            cursor.execute(comando) # Executa o comando acima de DELETE
            conexao.commit() # Comitado no banco de dados a alteração executada
        elif opc == 0:
            print('Programa finalizado!!!')
            cursor.close() # Utilizado para finalizar a conexão com o banco de dados
            conexao.close() # Utilizado para finalizar a conexão com o banco de dados
            break
    except:
        print('Opção inválida')

import mysql.connector

con = mysql.connector.connect(host='****',
                              database='projetodb',
                              user='root',
                              password='****')
cursor = con.cursor()


def inserir():
  tabela = input("Digite o nome da tabela: ")

  if tabela == "boardgame":
    codigo = int(input("Digite o código do tabuleiro: "))
    nome = input("Digite o nome do tabuleiro: ")
    estilo = input("Digite o estilo do tabuleiro: ")
    preco = int(input("Digite o preço do tabuleiro: "))
    cod_edit = int(input("Digite o código da editora: "))

    comando = "INSERT INTO {} (codigo, nome, estilo, preço, codigo_editora) \
    VALUES (%s, %s, %s, %s, %s)".format(tabela)
    valores = (codigo, nome, estilo, preco, cod_edit)
    cursor.execute(comando, valores)
    con.commit()

  elif tabela == "cliente":
    codigo = int(input("Digite o código do cliente: "))
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    endereço = input("Digite o endereço do cliente: ")
    telefone = int(input("Digite o telefone do cliente: "))
    email = input("Digite o email do cliente: ")

    comando = "INSERT INTO {} (codigo, nome, cpf, endereço, telefone, email) VALUES \
    (%s, %s, %s, %s, %s, %s)".format(tabela)
    valores = (codigo,nome,cpf,endereço,telefone,email)
    cursor.execute(comando, valores)
    con.commit()
    
  elif tabela == "editora":
    codigo = int(input("Digite o código da editora: "))
    nome = input("Digite o nome da editora: ")
    comando = "INSERT INTO {} (codigo, nome) VALUES (%s, %s)".format(tabela)
    valores = (codigo, nome)
    cursor.execute(comando, valores)
    con.commit()
    
  elif tabela == "itens_pedido":
    codigo = int(input("Digite o código do tabuleiro: "))
    numpedido = int(input("Digite o número do pedido: "))

    comando = "INSERT INTO {} (codigo_boardgame, numero_pedido) VALUES \
    (%s, %s)".format(
        tabela)
    valores = (codigo, numpedido)
    cursor.execute(comando, valores)
    con.commit()
    
  elif tabela == "pedido":
    numpedido = int(input("Digite o número do pedido: "))
    valortotal = int(input("Digite o valor da compra: "))
    datacompra = input("Digite a data de compra (aaaa-mm-dd): ")
    codigo = int(input("Digite o código do cliente: "))

    comando = "INSERT INTO {} (numero_pedido, valor_total, data_compra, codigo_cliente)\
    VALUES (%s, %s, %s, %s)".format(tabela)
    valores = (numpedido, valortotal, datacompra, codigo)
    cursor.execute(comando, valores)
    con.commit()


def selecionar():
  tabela = input("Digite o nome da tabela: ")
  comando = "SELECT * FROM {}".format(tabela)
  cursor.execute(comando)
  resultado = cursor.fetchall()
  print(resultado)


def atualizar():
  tabela = input("Digite o nome da tabela: ")
  linha = input("Digite o que você quer mudar: ")

  newline = None
  entrada = input("Digite para o que você quer mudar: ")
  newline = int(entrada) if entrada.isdigit() else entrada

  where = input("Digite o nome da chave primária ou de uma coluna: ")

  anything = None
  entrada = input("Digite um valor dentro da coluna: ")
  anything = int(entrada) if entrada.isdigit() else entrada

  comando = "UPDATE {} SET {} = %s WHERE {} = %s".format(tabela, linha, where)
  valores = (newline, anything)

  cursor.execute(comando, valores)
  con.commit()


def excluir():
  tabela = input("Digite o nome da tabela: ")
  where = input("Digite o nome da chave primária ou de uma coluna: ")

  anything = None
  entrada = input("Digite um valor dentro da coluna: ")
  anything = int(entrada) if entrada.isdigit() else entrada

  comando = "DELETE FROM {} WHERE {} = %s".format(tabela, where)
  valores = (anything, )

  cursor.execute(comando, valores)
  con.commit()


def realizar_juncao():
  tabela1 = input("Digite o nome da primeira tabela: ")
  tabela2 = input("Digite o nome da segunda tabela: ")
  coluna1 = input("Digite o nome da primeira coluna: ")
  coluna2 = input("Digite o nome da segunda coluna: ")
  primary = input("Digite a chave: ")
  foreign = input("Digite a chave secundária: ")

  comando = "SELECT {}.{}, {}.{} AS nome_{} FROM {}, {} WHERE {}.{} = {}.{};".format(
      tabela1, coluna1, tabela2, coluna2, tabela2, tabela1, tabela2, tabela1,
      foreign, tabela2, primary)
  cursor.execute(comando)
  resultado = cursor.fetchall()
  print("Aqui está o seu resultado: ")
  print(resultado)


while True:
  print("Selecione a operação:")
  print("1. Inserir")
  print("2. Selecionar")
  print("3. Atualizar")
  print("4. Excluir")
  print("5. Junção")
  print("6. Sair")

  opcao = input("Digite o número da operação desejada: ")

  if opcao == "1":
    inserir()
  elif opcao == "2":
    selecionar()
  elif opcao == "3":
    atualizar()
  elif opcao == "4":
    excluir()
  elif opcao == "5":
    realizar_juncao()
  elif opcao == "6":
    break

con.close()

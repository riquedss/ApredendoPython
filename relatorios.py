import manipulacaoBanco


def verifica_se_existe_dados_na_tabela(tabela):
    dados = manipulacaoBanco.ler_dados_do_banco()
    if not dados[0]:
        return False, dados[1]
    
    if dados[1][tabela]:
        return True, dados[1][tabela]

    return False, f"No data in table {tabela}"


def lista_elemento(tabela_pessoa, elemento):
    pessoas = []
    for pessoa in tabela_pessoa:
        if pessoa['tipo'] == elemento.upper():
            pessoas.append(pessoa)

    return pessoas


def lista_pessoas_sexo(tipo="", sexo =""):
    pessoas = []
    dados_pessoas = verifica_se_existe_dados_na_tabela(0)
    if not dados_pessoas[0]:
        return False, dados_pessoas[1]
      
    if tipo != "" and sexo != "":
        for pessoa in dados_pessoas[1]:
            if pessoa['tipo'] == tipo.upper() and pessoa['sexo'] == sexo.upper():
                pessoas.append(pessoa)
        return True, pessoas
    
    elif tipo != "" and sexo == "":
        return True, lista_elemento(dados_pessoas[1], tipo)
    
    elif tipo == "" and sexo != "":
        print("Só sexo")
        return True, lista_elemento(dados_pessoas[1], sexo)
        
        
def lista_disciplina():
    dados_disciplina = verifica_se_existe_dados_na_tabela(1)
    if not dados_disciplina[0]:
        return False, dados_disciplina[1]
    
    return True, dados_disciplina[1]

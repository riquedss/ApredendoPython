import manipulacaoBanco
import relatorios
import pandas as pd


def comando(diretorio):
    try:
        comando = input(diretorio).split()
        return True, comando[0]
    except:
        return False,  "ValueError: invalid command!"


def cadastro(funcao_cadastro, tabela):
    dados_cadastro = funcao_cadastro
    if not dados_cadastro[0]:
        return False, dados_cadastro[1]  
    
    if tabela == 0:
        return True, manipulacaoBanco.adiciona_dados_na_tabela(dados_cadastro[1], 0)[1]
    elif tabela == 1:
        return True, manipulacaoBanco.adiciona_dados_na_tabela(dados_cadastro[1], 1)[1]

    return False, "Error"


def add_del_turma():
    try:
        codigo = int(input("código da turma:>"))
        matricula = int(input("Matrícula da(o) aluna(o):>"))

        opcao = int(input("<0>matricula na disciplina|<1>Desmatrícula:>"))
        if not opcao in (0,1):
            return False, "ValueError: data type not expected"
        
        return True, matricula, codigo, opcao

    except:
        return False, "Error"


def executa_comando(funcao_ralatorio):
    relatorio = funcao_ralatorio
    if not relatorio[0]:
        return True,  False, relatorio[1]
    
    if not relatorio[1]:
        return True, False, "Data not found"
    
    return True, True, relatorio[1]


def comandos_relatorio():
    comando0 = comando("main/relatorio>")
    if not comando0[0]:
        return True, False, comando[1]
    
    if comando0[1] == "/la":
        return executa_comando(relatorios.lista_pessoas_sexo("ALUNO"))

    elif comando0[1] == "/lp":
        return executa_comando(relatorios.lista_pessoas_sexo("PROFESSOR"))

    elif comando0[1] == "/ld":
        return executa_comando(relatorios.lista_disciplina())

    elif comando0[1] in ("/las:M", "/las:F"):
        if comando0[1] == "/las:F":
            return executa_comando(relatorios.lista_pessoas_sexo("ALUNO", "F"))      
        else:
            return executa_comando(relatorios.lista_pessoas_sexo("ALUNO", "M"))
  
    elif comando0[1] in ("/lps:M", "/lps:F"):
        if comando0[1] == "/lps:F":
            return executa_comando(relatorios.lista_pessoas_sexo("PROFESSOR", "F"))
        else:
            return executa_comando(relatorios.lista_pessoas_sexo("PROFESSOR", "M"))

    elif comando0[1] == "/voltar":
        return False, False, "Back to main screen"

    return True, False, "ValueError: invalid command!"
    

def print_tabela_dados(lista_dic):
    print(pd.DataFrame(lista_dic))
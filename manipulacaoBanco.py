""" Estas funções ficarão responsáveis com a entrada e saída de dados do banco de dados(banco.txt) que se dar por uma lista com duas tabela.
Ex: [[Tabela - 0], [Tabela - 1]]
Tabela - 0 => Irá receber dicionários com dados de professores e alunos.
{'matricula': matricula,'nome': nome,'sexo': sexo,'cpf': cpf, 'tipo': tipo,'nascimento': nascimento}
Tabela - 1 => Irá receber dicionários com dados de cada disciplina.
{'codigo': geraId(comando),'nome': nome_disciplina,'professor': professor,'semestre': semestre,'alunos': []}
"""
import pickle

def ler_dados_do_banco(): 
    try:
        with open("banco.txt", "rb") as arq:
            return True, pickle.load(arq)
    except:
        return False, "Database does not exist"


def escreve_dados_no_banco(dados):
    if len(dados) == 2:
        with open("banco.txt", "wb") as arq:
            pickle.dump(dados, arq)
            return True, 'Registered!' 
    else:
        return False, "ValueError: Unexpected data type"


def matricula_de_pessoa():
    dados = ler_dados_do_banco()  
    try:
        return dados[1][0][-1]["matricula"] + 1
    except:
        return 1
   
        
def codigo_tuma():
    dados = ler_dados_do_banco()  
    try:
        return dados[1][0][-1]["codigo"] + 1
    except:
        return 300
    

def validacao_tipo_user():
    button = input("|<1> para cadastrar professor |<2> para cadastrar aluno|:>")
    if button == '1':
        return True, 'PROFESSOR'
    elif button == '2':
        return True, 'ALUNO'
    else:
        return False, "ValueError: data type not expected"


def procura_elemento_no_banco(key, value, tabela):
    dados = ler_dados_do_banco()
    if not dados[0]:
        return False, f"Value: {key} not registered in the database"

    pos = 0
    for dicionario_de_pessoas in dados[1][tabela]:
        if dicionario_de_pessoas[key] == value:
            return True, f"Value: {key} registered in the database", dados[1], pos
        pos += 1
  
    return False, f"Value: {key} not registered in the database"


def validacao_numero_cpf(): 
    cpf = input("CPF[###.###.###-##]:>")
    cpf1 = cpf.split("-")
    cpf2 = cpf1[0].split(".")
    try:
        for i in range(3):
            if not int(cpf2[i])//1000 == 0:
                return False, "ValueError: incorrect CPF"

        if not int(cpf1[1])//100 == 0:
            return False, "ValueError: incorrect CPF"  

        return True, cpf      

    except:
        return False, "ValueError: incorrect CPF"


def validacao_dataNascimento():
    nascimento = input("Data de nascimento (dd/mm/aa):>").split('/')  
    try:          
        return True, f'{int(nascimento[0])}/{int(nascimento[1])}/{int(nascimento[2])}'      
    except:
        return False, "ValueError: Date not informed or outside the expected standard"
        

def cadastra_pessoa():   
    inf_tipo = validacao_tipo_user()        
    if not inf_tipo[0]:
        return False, inf_tipo[1]
    
    nome = input("nome:>").upper()

    sexo = input("Sexo ['F'ou'M']:>").upper()
    if not sexo in ("M", "F"):
        return False, "ValueError: data type not expected" 
    
    inf_cpf = validacao_numero_cpf()
    if not inf_cpf[0]:
        return False, inf_cpf[1]
    
    inf_cpf1 = procura_elemento_no_banco('cpf', inf_cpf[1], 0) 
    if  inf_cpf1[0]:
        return False, inf_cpf1[1] 

    inf_nascimento = validacao_dataNascimento()
    if not inf_nascimento[0]:
        return False, inf_nascimento[1]
    
    return True, {
                'matricula': matricula_de_pessoa(),
                'nome': nome,
                'sexo': sexo,
                'cpf': inf_cpf[1],
                'tipo': inf_tipo[1],
                'nascimento': inf_nascimento[1],
                'disciplina': 0
            }
    

def cadastra_disciplina():    
    semestre = input("Semestre ['1'ou'2']:>")

    if not semestre in ("1", "2"):
        return False, "ValueError: data type not expected"

    nome_disciplina = input("Nome da disciplina:>")

    professor = input("Nome do professor:>") 

    return True, {
                'codigo': codigo_tuma(),
                'nome': nome_disciplina,
                'professor': professor,
                'semestre': semestre,
                'alunos': []
            }
 

def adiciona_dados_na_tabela(dic, tabela): 
    if type(dic) == type({}):
        dados = ler_dados_do_banco()
        if not dados[0]:
            if tabela == 0:      
                return True, escreve_dados_no_banco([[dic],[]])[1]

            elif tabela == 1:       
                return True, escreve_dados_no_banco([[],[dic]])[1]
            
            return False, "Error"        

        dados[1][tabela].append(dic)
         
        return True, escreve_dados_no_banco(dados[1])[1]
                            
    else:
        return False, "ValueError: a dictionary is expected."

 
def exclui_adiciona_na_turma(matricula, codigo, opcao): 
    if not procura_elemento_no_banco('matricula', matricula, 0)[0]:
        return False, "Value: matrícula not registered in the database"

    status_codigo = procura_elemento_no_banco('codigo', codigo, 1)
    if not status_codigo[0]:   
        return False, "Value: código not registered in the database"

    if opcao == 0:
    
        if matricula in status_codigo[2][1][status_codigo[3]]['alunos']:
            return False, "Value: matrícula existing in the class"
        status_codigo[2][1][status_codigo[3]]['alunos'].append(matricula)
    
    elif opcao == 1:

        if matricula not in status_codigo[2][1][status_codigo[3]]['alunos']:
            return False, "ValueError: matrícula not registered in this codigo"
        status_codigo[2][1][status_codigo[3]]['alunos'].remove(matricula)
    
    status_banco = escreve_dados_no_banco(status_codigo[2])
    if not status_banco[0]:
        return False, status_banco[1]  

    return True, "Value: Success!"
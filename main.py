import manipulacaoBanco
import interface

print(f'''-------------------------------------[COMANDOS DO SISTEMA ESCOLAR]-------------------------------------------

>/c - [Cadastrar professor ou aluno]
>/d - [Cadastrar disciplina]
>/r - [Menu de relatórios]
>/a - [Adiciona e remove aluno na disciplina]
>/s - [Sair]

-------------------------------------------------------------------------------------------------------------''')

menu = True
while menu:
    print()
    comando = interface.comando("main>")

    if comando[1] == '/c':
        print(interface.cadastro(manipulacaoBanco.cadastra_pessoa(), 0)[1])   
        
    elif comando[1] == '/d':
        print(interface.cadastro(manipulacaoBanco.cadastra_disciplina(), 1)[1])   
        
    elif comando[1] == '/a': 
        turma_status = interface.add_del_turma() 
        if turma_status[0]:
            print(manipulacaoBanco.exclui_adiciona_na_turma(turma_status[1], turma_status[2], turma_status[3])[1])
        else:
            print(turma_status[1])
        
    elif comando[1] == '/r':
        print(f'''---------------------------------------[COMANDOS DOS RELATÓRIOS]---------------------------------------------

>/la     - [Listar alunos]
>/lp     - [Listar professores]
>/ld     - [Listar uma disciplina (dados da disciplina e os alunos matriculados)]
>/las:M  - [Listar alunos por sexo (Masculino)] 
>/las:F  - [Listar alunos por sexo (Feminino)] 
>/lps:M  - [Listar professor por sexo (Masculino)] 
>/lps:F  - [Listar professor por sexo (Feminino)]
>/voltar - [Retorna ao menu principal]

-------------------------------------------------------------------------------------------------------------''')
        menu1 = True
        while menu1:
            print()
            inf_retorno = interface.comandos_relatorio()
            if inf_retorno[1]:
                interface.print_tabela_dados(inf_retorno[2])
            else:
                menu1 = inf_retorno[0]
                print(inf_retorno[2])    

    elif comando[1] == '/s':
        menu = False
        print(f"\nFinished program!")

    else:
        print("\nValueError: invalid command!")
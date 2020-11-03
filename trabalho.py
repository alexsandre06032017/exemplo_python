#-*-coding:utf-8-*-
print("		Glossário de palavras\n")
opcao = input("Informe a opção desejada:\n\na) Listar palavras\nb) Adicionar palavras\nc) busca em português\nd) buscar em inglês\ne) Adicionar descrição f) cadastrar sinônimo\ng) buscar sinônimo\nh) excluir palavras\ni) Sair\n")
l = ["Português","Inglês","descrição","sinônimos"]
while opcao != "i":
	if opcao == "a":
                for d in l:
                        print(d)
	elif opcao == "b":
		op = int(input("Digite a quantidade de palavras a ser cadastradas:\n"))
		for i in range(1,op):
                        cod = i
                        nome_ingles = input("Nome em Ingles:")
                        nome_portugues = input("Nome em Portugues:")
                        descricao = input("Descricao:")
                        sinonimo = ""
                	l.append((nome_portugues,nome_ingles,descricao,sinonimo))
                for d in l:
                        print(d)
		
	elif opcao == "c":
                palavra = input("Informe a palavra em português que deseja visualizar:\n")                        
                for p,i,d,s in l:
                        if palavra == p:
                                print(p)
                        else:
                                print("Palvras não localizada") 
	elif opcao == "d":
                palavra = input("Informe a palavra em português que deseja visualizar:\n")                        
                for p,i,d,s in l:
                        if palavra == i:
                                print(p)
                        else:
                                print("Palvras não localizada") 
	elif opcao == "e":
                palavra = input("Informe a palavra que deseja adicionar descrição:\n")
                for p,i,d,s in l:
                        if palavra == p or palavra == i:
                                d = raw_input("Digite a descrição:\n")
                        else:
                                print("Palvras não localizada") 
                for p,i,d,s in l:
                        if palavra == p or palavra == i :
                                l[j]== (c,p,i,d,s)
	elif opcao == "f":
                #cadastrar sinônimo
                palavra = input("Informe a palavra(portugues ou inglês) que deseja adicionar sinônimo:\n")
                for p,i,d,s in l:
                        if palavra == p or palavra == i:
                                s = raw_input("Digite a sinônimo:\n")
                        else:
                                print("Palvras não localizada") 
                for j in range(len(l)):
                        if palavra == d:
                                l[j]==(p,i,d,s)
	elif opcao == "g":
		pass
	elif opcao == "h":
                palavra = input("Informe a palavra que deseja excluir do dicionario:\n")
                for j in (len(l)+1):
                        p,i,d,s = l[j]
                                if palavra == p or palavra == i:                
                                        del(l[j])
                                else:    
                                        print("Palavra não encontrada!\n")
        
	else:
		print("Opção inválida:\n")

	opcao = raw_input("Informe a opção desejada:\n\na) Listar palavras\nb) Adicionar palavras\nc) busca em português\nd) buscar em inglês\ne) Adicionar descrição f) cadastrar sinônimo\ng) buscar sinônimo\nh) excluir palavras\ni) Sair\n")	

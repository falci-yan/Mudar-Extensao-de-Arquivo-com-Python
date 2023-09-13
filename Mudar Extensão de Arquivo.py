#Primeiro importamos duas bibliotecas simples.
import os
import glob

#Depois vamos pegar as informações. 
try: 
    #Pegar o caminho que está o arquivo ou os arquivos.
    diretorio = input ("Informe o caminho do diretorio desejado: \nExemplo: C:/documentos \n")
    print (" ")
    #Depois pegar a informação de qual extensão desejamos mudar.
    extensao        = input ("Qual a extensão de deseja mudar? \n")
    print (" ")
    #E por último qual exntesão que desejamos.
    extensao_novo   = input ("Qual a nova exntesão desejada? \n")
    print (" ")

    #Cria uma lista com o nome e a extensão dos arquivos
    listar_arquivos = glob.glob(f"{diretorio}/*{extensao}")

    #Para cada arquivo na lista é feito a mundaça da extensão,
    #Separando a extensão do nome e depois adicionando a extensão nova.
    for arquivos in listar_arquivos:
        nome_novo = str.split(arquivos,f"{extensao}")
        nome_arquivo = os.rename(f"{arquivos}",f"{nome_novo[0]}{extensao_novo}")
        print(f"Nomes alterados com sucesso: {arquivos}")

#Tratamento de exceções
except Exception as e:
    print("Ocorreu o seguinte erro", e)

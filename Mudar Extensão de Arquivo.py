import os
import glob

try: 
    diretorio = input ("Informe o caminho do diretorio desejado: \nExemplo: C:/documentos \n")
    print (" ")
    extensao        = input ("Qual a extensão de deseja mudar? \n")
    print (" ")
    extensao_novo   = input ("Qual a nova exntesão desejada? \n")
    print (" ")

    listar_arquivos = glob.glob(f"{diretorio}/*{extensao}")


    for arquivos in listar_arquivos:
        nome_novo = str.split(arquivos,f"{extensao}")
        nome_arquivo = os.rename(f"{arquivos}",f"{nome_novo[0]}{extensao_novo}")
        print(f"Nomes alterados com sucesso: {arquivos}")

except Exception as erros:
    print("Deu ruim porque", erros)
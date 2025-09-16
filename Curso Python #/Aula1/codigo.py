import pyautogui
import time
import pandas

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.PAUSE = -> Pausa um tempo

pyautogui.PAUSE = 1

# Divida em passo a passo
# Passo 1: Entrar no sistema da empresa -   https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # abrir o chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

# digitar o site
# Precisa colocar delay, pq os comandos são realizados automáticamente, ai usamos o pause

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")




# Passo 2: Fazer login

    # Precisamos fazer com que os comandos sejam executados só depois do site ter carregado

    # Usamos o time.sleep

# Espera de 3 segundos
time.sleep(3)

# Agora vamos aprender a clicar

#IMPORTANTE!!!! SE LIGA NA TELA DUPLA QUE AFETA NA POSIÇÃO DO MOUSE

#Pega posição do mouse
pyautogui.click(x=500, y=450)

# Preencher gmail
pyautogui.write("VascodaGama@gmail.com")

# Botão logar
pyautogui.press("Tab") #Passa para o próximo campo

# Preenche senha
pyautogui.write("Vasco7042#")
pyautogui.press("Enter")


# Passo 3: Importar a base de dados

# Espera de 3 segundos
time.sleep(3)

# Como importar uma base de dados: Usamos o pacote chamado pandas
# Reservamos a base de dados em uma variável
tabela = pandas.read_csv("produtos.csv") # Aqui usamos a função read para ler arquivos com extensão csv



# Passo 4: Cadastrar 1 produto
for linha in tabela.index: # Para cada linha da minha tabela: 
# Tabela.index = Lista com todos os números das linhas

    pyautogui.click(x=425, y=309)

    codigo = tabela.loc[linha, "codigo"] #  Localiza uma informação (linha, coluna)
    pyautogui.write(str(codigo))
    pyautogui.press("Tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("Tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("Tab")

    categoria = str(tabela.loc[linha, "categoria"]) # Como aqui é um número, pode dar erro, por isso colocamos dentro de um str
    pyautogui.write(str(categoria))
    pyautogui.press("Tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(str(preco_unitario))
    pyautogui.press("Tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(str(custo))
    pyautogui.press("Tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(str(obs)) 

    pyautogui.press("Tab")
    pyautogui.press("Enter")

    # Agora teremos que voltar lá pra cima da página, usando o scroll

    pyautogui.scroll(10000) # Numero positivo, pra cima. Usamos um valor alto pra voltar pro inicio.

# Passo 5: Repetir para todos os produtos

# Precisamos percorrer a tabela toda


# pyautogui -> fazer automações com python
# Bibliotecas = pacotes de código
# pip install pyautogui

# pyautogui.click - Clica
# pyautogui.write - Escreve um texto
# pyautogui.press - Aperta uma tecla
# pyautogui.hotkey - Aperta um atalho (hotkey)

import pyautogui
pyautogui.FAILSAFE = True
import time

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# Abriria o navegador
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

pyautogui.write(link)
pyautogui.press("Enter")
# Fazer uma pausa maior pro site carregar
time.sleep(3) # pyautogui hashtag

# Passo 2: Fazer login
# Clicar no campo de e-mail
pyautogui.click(755, 378)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # Passar para o próximo campo
pyautogui.write("sua senha muito muito muito dificilima")
pyautogui.press("tab") # Passar para o botão
pyautogui.press("Enter")
# Fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(725, 261)

    # Codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # Preco Unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # Passar para o botão enviar

    pyautogui.press("enter")
    # Voltar para o inicio do site
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos

# Número de Suporte para dúvida: (21) 96721-8715
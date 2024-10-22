import tkinter as tk
from tkinter import messagebox, ttk
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Variável de controle para parar o processo
parar_execucao = False

# Função para formatar a lista (Código 1)
def formatar_lista(lista):
    lista_formatada = []
    
    for item in lista:
        partes = item.split('\t')  # Divide o item em partes usando tabulação como delimitador
        if len(partes) < 2:
            continue  # Ignora entradas que não têm pelo menos um nome e uma matrículagit
        
        # Extrai o nome completo e mantém os dois primeiros nomes
        nome_completo = partes[0].strip()  # Nome completo
        nomes = nome_completo.split()  # Divide o nome completo em partes
        nome_formatado = ' '.join(nomes[:3])  # Mantém apenas os dois primeiros nomes
        
        # Extrai a matrícula e pega os últimos 8 dígitos
        matricula = partes[1].strip()  # Remove espaços em branco ao redor
        matricula_formatada = matricula[-8:]  # Pega os últimos 8 dígitos
        matricula_formatada = matricula_formatada.zfill(8)  # Garante que tenha 8 dígitos

        lista_formatada.append(f"{matricula_formatada}, {nome_formatado}")
    
    return lista_formatada

def salvar_em_arquivo(lista_formatada, filename="lista_formatada.txt"):
    # Cria o caminho para o desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, filename)
    
    # Salva a lista formatada em um arquivo
    with open(file_path, 'w') as f:
        f.write("\n".join(lista_formatada))
    
    return file_path

def processar():
    texto_entrada = texto.get("1.0", tk.END)  # Pega o texto da caixa de texto
    lista = [linha for linha in texto_entrada.splitlines() if linha]  # Cria lista sem linhas vazias
    
    resultado = formatar_lista(lista)  # Formata a lista
    
    # Exibe o resultado em uma mensagem
    if resultado:
        # Salva o resultado em um arquivo
        file_path = salvar_em_arquivo(resultado)
        messagebox.showinfo("Resultado", f"Resultados salvos em: {file_path}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma entrada válida foi encontrada.")

# Função do segundo código
def gerar_registro(matricula, nome):
    return f"4+1+I[[000000000000{matricula}[[[1[1[1[[[[[2[[[[[0[{nome}[[[[["

def processar_arquivo():
    alunos = []
    arquivo_entrada = os.path.join(os.path.expanduser("~"), "Desktop", "lista_formatada.txt")  # Caminho do arquivo
    arquivo_saida = os.path.join(os.path.expanduser("~"), "Desktop", "registros_alunos.txt")
    
    try:
        with open(arquivo_entrada, "r") as arquivo:
            for linha in arquivo:
                matricula, nome = linha.strip().split(", ")
                registro = gerar_registro(matricula, nome)
                alunos.append(registro)
    except FileNotFoundError:
        messagebox.showerror("Erro", f"Arquivo '{arquivo_entrada}' não encontrado.")
        return
    
    with open(arquivo_saida, "w") as arquivo:
        for aluno in alunos:
            arquivo.write(aluno + "\n")
    
    messagebox.showinfo("Sucesso", f"Arquivo '{arquivo_saida}' gerado com sucesso!")

# Função do terceiro código
def iniciar_processo():
    global parar_execucao
    parar_execucao = False  # Resetar a variável de controle

    # Obter o IP selecionado
    ip_selecionado = combo_ip.get()
    
    # Dicionário de IPs e seus nomes
    ips = {
        "PMAT": "",
        "LP7 DEV-Us": "",
        "BLACK BEE": "",
        "LP5 BYRON": ""
    }
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 30)  # Aumentando o tempo de espera

    try:
        print("Acessando a página de login...")
        driver.get(ips[ip_selecionado])
        time.sleep(5)  # Aguarda a página carregar

        # Tentar clicar em "Voltar" ou "Sair"
        try:
            print("Tentando clicar em 'Voltar' ou 'Sair'...")
            voltar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Voltar')]")))
            voltar_button.click()
            print("Clicou em 'Voltar' ou 'Sair'!")
        except Exception as e:
            print("Botão 'Voltar' ou 'Sair' não encontrado, seguindo para o próximo passo.")

        # Preencher o campo de usuário
        print("Tentando encontrar o campo de usuário...")
        usuario_input = wait.until(EC.visibility_of_element_located((By.NAME, 'lblLogin')))
        usuario_input.send_keys('p')  # Substitua 'seu_usuario'


        print("Tentando encontrar o campo de senha...")
        senha_input = wait.until(EC.visibility_of_element_located((By.NAME, 'lblPass')))
        senha_input.send_keys('')  # Substitua 'sua_senha'

        print("Clicando no botão de entrada...")
        entrar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@onclick='subComp(1,7,0);']")))
        entrar_button.click()

        print("Login enviado!")
        time.sleep(5)  # Esperar o login processar

        # Navegar para a aba de dados
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Dados'))).click()
        time.sleep(2)

        # Ir para a importação de dados
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Importação'))).click()
        time.sleep(2)

        # Enviar o arquivo
        FILE_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "registros_alunos.txt")

        # Usar o ID correto para encontrar o campo de upload
        upload_input = wait.until(EC.presence_of_element_located((By.ID, 'fileinput')))
        upload_input.send_keys(FILE_PATH)

        # Submeter o formulário de importação (se necessário)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@onclick='subComp(1,7,0);']"))).click()

        print("Arquivo enviado com sucesso!")
        time.sleep(5)  # Esperar o processo de importação

    finally:
        # Fechar o navegador
        driver.quit()

# Função para parar o processo
def parar_processo():
    global parar_execucao
    parar_execucao = True  # Define a variável de controle para parar

# Criação da interface gráfica
root = tk.Tk()
root.title("Aplicativo de Formatação e Processamento")
root.geometry("500x500")  # Tamanho da janela
root.configure(bg="#F0F0F0")  # Cor de fundo

# Frame principal
frame = tk.Frame(root, bg="#FFFFFF", bd=5, relief=tk.RAISED)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Label
label = tk.Label(frame, text="Cole a lista de nomes e matrículas:", font=("Arial", 12), bg="#FFFFFF")
label.pack(pady=10)

# Caixa de texto para entrada
texto = tk.Text(frame, wrap='word', height=10)
texto.pack(pady=10, padx=10, expand=True, fill='both')

# Botão para processar a entrada do primeiro código
botao_processar = tk.Button(frame, text="Formatar Lista", command=processar, bg="#4CAF50", fg="white", font=("Arial", 12))
botao_processar.pack(pady=10)

# Botão para processar o segundo código
botao_processar_arquivo = tk.Button(frame, text="Gerar Registros", command=processar_arquivo, bg="#2196F3", fg="white", font=("Arial", 12))
botao_processar_arquivo.pack(pady=10)

# Label para seleção de IP
label_ip = tk.Label(frame, text="Selecione o IP:", font=("Arial", 12), bg="#FFFFFF")
label_ip.pack(pady=10)

# Combobox para seleção de IP
combo_ip = ttk.Combobox(frame, values=["PMAT", "LP7 DEV-Us", "BLACK BEE", "LP5 BYRON"], state="readonly")
combo_ip.pack(pady=10)

# Botão para iniciar o processo de envio
botao_enviar = tk.Button(frame, text="Enviar Arquivo", command=iniciar_processo, bg="#FF9800", fg="white", font=("Arial", 12))
botao_enviar.pack(pady=10)

# Botão para parar o processo
botao_parar = tk.Button(frame, text="Parar Processo", command=parar_processo, bg="#F44336", fg="white", font=("Arial", 12))
botao_parar.pack(pady=10)

# Iniciar a aplicação
root.mainloop()

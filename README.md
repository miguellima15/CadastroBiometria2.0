# CadastroBiometria2.0
# Aplicativo de Formatação e Processamento

Este projeto é um aplicativo desenvolvido em Python com interface gráfica usando a biblioteca `tkinter`. Ele permite formatar listas de nomes e matrículas, gerar registros específicos e enviar arquivos para um sistema externo via Selenium.

## Funcionalidades

1. **Formatar Lista**: Formata uma lista de nomes e matrículas, mantendo os dois primeiros nomes e os últimos 8 dígitos da matrícula, e salva o resultado em um arquivo.
2. **Gerar Registros**: Gera registros formatados a partir de uma lista de nomes e matrículas e os salva em um arquivo.
3. **Enviar Arquivo**: Utiliza Selenium para realizar o upload do arquivo gerado para um sistema externo, simulando o processo de login e navegação no sistema.
4. **Parar Processo**: Permite interromper o processo em execução.

## Requisitos O conteúdo de requirements.txt deve incluir:

- Python 3.7 ou superior 
- Google Chrome instalado
- Dependências listadas em `requirements.txt`

### Dependências

As bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Para instalar as dependências, execute o comando:

``bash
`pip install -r requirements.txt `

##O conteúdo de requirements.txt deve incluir:
`tk
selenium
webdriver-manager`

##Configuração
Certifique-se de ter o Google Chrome instalado.
Instale as dependências do projeto com o comando acima.
Execute o aplicativo com o comando:

`python nome_do_arquivo.py`
Substitua nome_do_arquivo.py pelo nome do arquivo do código fonte.

Como Usar
Formatar Lista: Cole uma lista de nomes e matrículas na caixa de texto e clique no botão "Formatar Lista". O resultado será salvo em um arquivo lista_formatada.txt na área de trabalho.
Gerar Registros: Após formatar a lista, clique no botão "Gerar Registros". O aplicativo vai gerar um arquivo registros_alunos.txt na área de trabalho com os registros formatados.
Enviar Arquivo: Selecione um IP na lista suspensa e clique em "Enviar Arquivo" para realizar o upload do arquivo registros_alunos.txt para o sistema.
Parar Processo: Caso deseje parar o processo, clique em "Parar Processo".
Estrutura do Código
formatar_lista(lista): Formata a lista de nomes e matrículas.
salvar_em_arquivo(lista_formatada, filename): Salva a lista formatada em um arquivo.
processar(): Lida com a entrada do usuário e chama as funções de formatação e salvamento.
gerar_registro(matricula, nome): Gera o formato de registro necessário.
processar_arquivo(): Processa o arquivo lista_formatada.txt para gerar os registros formatados.
iniciar_processo(): Usa Selenium para automatizar o envio do arquivo para o sistema.
parar_processo(): Para a execução do processo.
Avisos
Certifique-se de fornecer as credenciais corretas para acessar o sistema ao usar Selenium.
O Selenium pode ser sensível a mudanças na interface do usuário do site, então certifique-se de que os seletores de elementos estão corretos.
Contribuição
Sinta-se à vontade para contribuir com melhorias ou sugestões para o projeto.

Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Esse `README.md` oferece uma descrição abrangente do projeto, desde a funcionalidade até a configuração e uso.






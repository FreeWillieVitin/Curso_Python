import PyPDF2

with open('C:\\Users\\HSVP\\Desktop\\Escala Final de Semana.pdf', 'rb') as arquivo:  # Abre o arquivo em modo de leitura byte(rb)
    leitor = PyPDF2.PdfReader(arquivo)  # Classe de leitura que recebe a variável do arquivo aberto

    qtd_pages = len(leitor.pages)  # Faz a contagem de páginas

    num_pages = 0  # Indíce da página 0 = primeira página
    pagina = leitor.pages[num_pages]  # Armazena a estrutura abstrata da página passada como índice
    page_text = pagina.extract_text()

    linhas = page_text.split('\n')

    # linhas['VICTOR HUGO JURCZYSZYN  Informática  08:00h às 12:00h  '] = 'VICTOR HUGO JURCZYSZYN  Informática  10:00h às 12:00h  '


print(linhas)

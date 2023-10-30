import PyPDF2

with open('C:\\Users\\HSVP\\Desktop\\Escala Final de Semana.pdf', 'rb') as arquivo:  # Abre o arquivo em modo de leitura byte(rb)
    pdf_reader = PyPDF2.PdfReader(arquivo)  # Classe de leitura que recebe a variável do arquivo aberto
    page_number = len(pdf_reader.pages)  # Faz a contagem de páginas
    page_number = 0  # Indíce da página 0 = primeira página
    page = pdf_reader.pages[page_number]  # Armazena a estrutura abstrata da página passada como índice
    page_text = page.extract_text()

    linhas = page_text.split('\n')
    linhas[9] = 'É nois Brow'
    novo_pdf = '\n'.join(linhas)

    # escrever_pdf = PyPDF2.PdfWriter()

    # for i, pages in enumerate(pdf_reader.pages):
    #     escrever_pdf = PyPDF2.PdfWriter()
    #     with open('C:\\Users\\HSVP\\Desktop\\NovoPdf.pdf', 'wb') as new_file:
    #         # Escreve o conteúdo modificado no novo arquivo PDF
    #         escrever_pdf.add_page(pages)
    #         escrever_pdf.write(new_file)

print(linhas)

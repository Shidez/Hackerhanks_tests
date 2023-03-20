import PyPDF2

# Abre o arquivo PDF em modo leitura binária
with open('Batch 269193.pdf', 'rb') as pdf_file:

    # Cria um objeto PDFReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    print("Número de páginas:", len(pdf_reader.pages))

    # Lê o conteúdo da primeira página do PDF
    page = pdf_reader.pages[0]
    print("Conteúdo da página 1:")
    print(page.extract_text())

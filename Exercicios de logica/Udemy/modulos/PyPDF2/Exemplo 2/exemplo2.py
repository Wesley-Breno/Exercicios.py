from PyPDF2 import PdfReader, PdfWriter  # Chamando as classes para ler e escrever os PDFs

leitor = PdfReader('pdf_original.pdf')  # Pegando o PDF que sera separado
escritor_arquivo1 = PdfWriter()  # Variavel que sera responsavel por pegar uma pagina especifica

escritor_arquivo1.add_page(leitor.pages[0])  # Pegando a primeira pagina do arquivo.pdf

with open('arquivo1.pdf', 'wb') as pdf:  # Criando um novo arquivo apenas com esta pagina
    escritor_arquivo1.write(pdf)

escritor_arquivo2 = PdfWriter()  # Criando uma nova variavel para pegar a outra pagina do arquivo.pdf
escritor_arquivo2.add_page(leitor.pages[1])  # Pegando a segunda pagina

with open('arquivo2.pdf', 'wb') as pdf2:  # Criando um novo arquivo com esta segunda pagina
    escritor_arquivo2.write(pdf2)

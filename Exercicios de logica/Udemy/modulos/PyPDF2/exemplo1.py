import os  # Importando modulo os para percorrer pelos arquivos
from PyPDF2 import PdfMerger  # Importando a classe PdfMerger para unir PDFs

unir = PdfMerger()
arquivos_pdf = []  # Lista onde ficara o caminho de cada arquivo PDF

for root, dirs, files in os.walk(r'C:\Users\jaosd\PycharmProjects\pythonProject\udemy\modulos\PyPDF2'):  # Percorrendo pelos arquivos
    for file in files:
        if os.path.splitext(file)[1] == '.pdf':  # Se a extensao do arquivo for '.pdf'
            arquivos_pdf.append(os.path.join(root, file))  # Adicionando o caminho do arquivo.pdf para a lista

for arq in arquivos_pdf:  # Unindo cada arquivo.pdf que estiver na lista
    unir.append(arq)

unir.write('novo_pdf.pdf')  # Criando novo arquivo.pdf onde estao todos os outros arquivos juntos.
unir.close()

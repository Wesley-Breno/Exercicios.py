import ctypes

atributo_ocultar = 0x02  # Atributo hexadecimal que faz o arquivo ser ocultado

# Reescrevendo arquivo e ocultando ele.
retorna = ctypes.windll.kernel32.SetFileAttributesW('arquivo.txt', atributo_ocultar)

if retorna:
    print('\n\tArquivo ocultado')
else:
    print('\n\tNão foi possivel ocultar o arquivo')

import shutil

try:
    arquivo_mkv = '2022-07-05 18-50-17.mkv'
    arquivo_mp4 = '2022-07-05 18-49-13.mp4'
    arquivo_novo = shutil.move(arquivo_mkv, arquivo_mp4)

except:
    print('Arquivo MP4 modificado para MKV com sucesso garanhao')
    arquivo_novo = shutil.move(arquivo_mp4, arquivo_mkv)

else:
    print('Arquivo MKV modificado para MP4 com sucesso gostosao')

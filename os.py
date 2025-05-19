import os

#cwd = Current Working Directory
#obetener el directorio de trabajo actual
"""cwd = os.getcwdb()
print("Directorio de trabajo actual", cwd)"""

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]  #El '.' indica el directorio actual
print("loa archivos txt:", txt_files)

#Podemos renombrar
os.rename('Cuento cambiado.txt', 'Cuento cambiadito.txt')
print("Archivo renombrado")

#Listar los archivos .txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]  #El '.' indica el directorio actual
print("loa archivos txt:", txt_files)
import os
import shutil

from_dir = "C:/Users/lului/Downloads"
to_dir = "C:/Users/lului/OneDrive/Área de Trabalho/códigos em python/progeto 111/arquivos_documentos"
list_of_files = os.listdir(from_dir)
#sprint(list_of_files)

for lop in (list_of_files):
    name, extension = os.path.splitext(lop)
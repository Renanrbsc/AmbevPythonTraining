#----- Estruturas de dados e DB

from pessoa_db import listar_todos
from pessoa_converte import converter_tabela_dicionario
from pessoa_exporta import exportar_txt

lpd = listar_todos()
lpd = converter_tabela_dicionario(lpd)
exportar_txt(lpd)


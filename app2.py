# rows = linha, passando e interando sobe cada linha, min_rows = começar pela linha
import openpyxl

# carregando arquivo
book = openpyxl.load_workbook('planilia de compras.xlsx')

# selecinando uma pagina especifica
frutas_page = book['Frutas']

# Imprimindo os dados de cada linha
from rows in frutas_page.iter_rows(min_rows=2, max_rows=5)

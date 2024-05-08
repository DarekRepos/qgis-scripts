
# import os
# from fpdf import FPDF
# from pathlib import Path
# import shutil
#
# class PDF(FPDF):  # stopka z numerem strony
#     def footer(self):
#         self.set_y(-15)
#         self.cell(0, 10, f'Strona {self.page_no()}', 0, 0, 'C')
#
#
# def create_pdf(filename):
#     pdf = PDF()
#     pdf.add_page()
#
#     walidator_sciezka = os.path.dirname(os.path.realpath(__file__))
#
#     print(walidator_sciezka)
#
#     current_dir = Path(__file__).parent  # Get the directory of the current script
#     # jesli skrytp znajduje sie w subfolderze (project_folder/class-file.py) to wtedy
#     print(current_dir)
#     font_dir = str(current_dir / "fonts")
#     print(font_dir)
#     #pdf.add_font('Verdana', '', walidator_sciezka + "\Verdana.ttf", uni=True)
#     #pdf.add_font('Verdana', '', str(font_dir / "Verdana.ttf"))
#     #pdf.add_font("Verdana", "B", str(font_dir / "Verdana-bold.ttf"))
#
#     # ponizej czcionka skopiowana z folderu windowsa dziala na pythonie 3.7
#     pdf.add_font("Verdana", "", font_dir + "/verdanab.ttf", uni=True)
#
#
#     # to poniżej szuka w folderze projektu ,
#     # pdf.add_font(fname="Verdana.ttf")
#     # project_name /
#     # ├── run-script.py
#     # ├── Verdana-bold.ttf
#     # ├── Verdana.ttf
#     # ├── folder/
#     # │   ├── file.py
#     # │   ├── another-file.py
#     # #jak nei znajdzie to suzka foldru font w zainstalowanym pakiecie
#
#
#
#
#
#
#
#     # absoulte path
#     #pdf.add_font("Verdana", "B", r"C:\Windows\Fonts\verdanab.ttf",  uni=True)
#
#     pdf.set_font("Verdana", "", 16)  #
#     pdf.cell(40, 20, "Hello Arial_TTF! v5")
#     pdf.output(filename)
#     # skopiować plik
#     # Source and destination file paths
#     source_file = filename
#     destination_file = "plik_docelowy.pdf"
#
#     # Copy the file with error handling
#     try:
#         shutil.copy(source_file, destination_file)
#         print("File copied successfully!")
#
#         # lub przeniesc plik bez kopiowania
#         shutil.move(source_file, destination_file)
#
#     except shutil.Error as e:
#         print(f"Error copying file: {e}")
#     # usunąć stworzony plik
#     os.remove(filename)
#
# create_pdf("core_fonts.pdf")
#
# print("koniec")
# #do pdf dodajemy atrybuty qgisa ktore wciaz zyja i nie da sie zamknac obirektu gargbae collectorem

import os
from fpdf import FPDF
from fpdf.fonts import CORE_FONTS
from pathlib import Path
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode
import csv
with open("countries.txt", encoding="utf8") as csv_file:
    data = list(csv.reader(csv_file, delimiter=","))

pdf = FPDF()
pdf.set_font("helvetica", size=14)

# Basic table:
pdf.add_page()
with pdf.table() as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

# Styled table:
pdf.add_page()
pdf.set_draw_color(255, 0, 0)
pdf.set_line_width(0.3)
headings_style = FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 0))
with pdf.table(
    borders_layout="NO_HORIZONTAL_LINES",
    cell_fill_color=(224, 235, 255),
    cell_fill_mode=TableCellFillMode.ROWS,
    col_widths=(42, 39, 35, 42),
    headings_style=headings_style,
    line_height=6,
    text_align=("LEFT", "CENTER", "RIGHT", "RIGHT"),
    width=160,
) as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output("tuto5.pdf")

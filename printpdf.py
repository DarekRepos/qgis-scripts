import os
from fpdf import FPDF
from fpdf.fonts import CORE_FONTS
from pathlib import Path
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode


class PDF(FPDF):  # stopka z numerem strony
    def footer(self):
        self.set_y(-15)
        self.cell(0, 10, f'Strona {self.page_no()}', 0, 0, 'C')


def create_pdf(filename):
    pdf = PDF()
    pdf.set_font("helvetica", size=14)
    
    pdf.add_page()
    
    headings_style = FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 0))	# i tak nagłowek stylujemy
    override_style = FontFace(emphasis="BOLD")
    TABLE_DATA = [
        ["A",           "B",            "C",            "D"],
        ["A1",           "B",   "C1",           "B", ],
        
        ["A6",          "B6",           "B",   "D6"],
        
    ]

    with pdf.table(TABLE_DATA,
        borders_layout="NO_HORIZONTAL_LINES",
        cell_fill_color=(54, 54, 124), # stylowanie pozostałych komórek
        cell_fill_mode=TableCellFillMode.ROWS, # to koloruje nieparzyste komorki lub  TableCellFillMode.ALL jesli wszystkie komorki maja byc kolorowe 
        headings_style=headings_style, #stylowanie nagłowka
        line_height=6,
        col_widths=(40,20,50,70), 
        text_align = "CENTER",
        padding = (1)
    ) as table1:
        headings = table1.row()
        headings.cell("KONTROLOWANY PLIK", style=override_style)
        headings.cell("KLASA", style=override_style)
        headings.cell("LOKALNY ID")
        headings.cell("KOMUNIKAT BleDU")
        for data_row in TABLE_DATA:
            table1.row(data_row)

    pdf.set_font("Helvetica", size=24)
    pdf.cell(40, 20, "Hello Arial_TTF! v5")
    pdf.output(filename)
    os.startfile(filename) #otworz plik


create_pdf("d:\core_fonts.pdf")
print("koniec")
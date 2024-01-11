import openpyxl
from openpyxl import Workbook
from datetime import datetime, timedelta


class ExcelRecorder:
    def __init__(self, filename="video_info.xlsx"):
        self.filename = filename
        self.initialize_excel()

    def initialize_excel(self):
        # Crear un archivo Excel o añadir encabezados si no existen
        try:
            workbook = openpyxl.load_workbook(self.filename)
            sheet = workbook.active
            if sheet.max_row == 1:
                # Si solo hay una fila, probablemente necesitemos agregar encabezados
                sheet.append(["URL", "Título", "Fecha Última Comprobacion"])
        except FileNotFoundError:
            workbook = Workbook()
            sheet = workbook.active
            # Añadir encabezados
            sheet.append(["URL", "Título", "Fecha Última Comprobacion"])

        workbook.save(self.filename)

    def add_video_info(self, url, title):
        workbook = openpyxl.load_workbook(self.filename)
        sheet = workbook.active

        # Buscar si la URL ya existe
        for row in range(2, sheet.max_row + 1):
            if sheet.cell(row=row, column=1).value == url:
                last_time = datetime.strptime(sheet.cell(
                    row=row, column=3).value, "%Y-%m-%d %H:%M:%S")
                if datetime.now() - last_time > timedelta(weeks=1):
                    # Actualizar registro
                    sheet.cell(row=row, column=2).value = title
                    sheet.cell(row=row, column=3).value = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S")
                    workbook.save(self.filename)
                return

        # Añadir la información en una nueva fila si la URL no existe
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append([url, title, current_time])

        # Guardar el archivo
        workbook.save(self.filename)

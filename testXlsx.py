import openpyxl

wb_form = openpyxl.load_workbook(filename='time.xlsx')
wb_val = openpyxl.load_workbook(filename='time.xlsx', data_only=True)

sheet_val = wb_val['Лист1']
sheet_form = wb_form['Лист1']

L6_val = sheet_val['L6'].value

for cellObj in sheet_val['L34':'L46']:
    for cell in cellObj:
        if cell.value is not None:
            days = openpyxl.utils.cell.coordinate_from_string(cell.coordinate)
            daysList = list(days)
            daysList[0] = 'B'
            days = tuple(daysList)
            print(cell.value, " - допустим предмет")
            print(days , " - номер")

# print(L6_val)

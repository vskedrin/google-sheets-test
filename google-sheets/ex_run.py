from openpyxl import load_workbook

wb = load_workbook('./TestExcel.xlsx')
print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Лист1')

print(sheet['A1'].value)
for cellObj in sheet['A1':'C6']:
    for cell in cellObj:
        print(cell.coordinate, cell.value)
    print('--- END ---')

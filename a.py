import xlrd as x  
loc_file = ("/home/pi/Desktop/demo")

wb = x.open_workbook(loc_file) 
sheet = wb.sheet_by_index(0)

for i in range(sheet.nrows): 
    print(sheet.cell_value(0, i)) 
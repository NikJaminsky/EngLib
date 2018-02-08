import xlrd


readFile = xlrd.open_workbook("C:/Users/"userName"/Desktop/engl.xlsx")          #path to library
sh = readFile.sheet_by_index(0)                                             #read list of book
libr = {sh.cell_value(a,3): sh.row_values(a, 4, 8) for a in range(9, 300)}  #filling dict from library

def showAll():
    for lb,val in libr.items():
        print(lb, "-", val)

#Add
#func
#form
#random show letters

from openpyxl import load_workbook

workbook = load_workbook(r"D:\Python_Practice-1\18-03-2021\Train_Data.xlsx")
# Getting the sheet names
sheet_list=workbook.get_sheet_names()
# Printing the total sheets
print(sheet_list)   

def train_number(workbook, sheet_name, train_num):
    mastersheet = workbook["Mastersheet"]
    for i in range(1, sheet_name.max_row + 1):
        # to check the value in column 1
        if (sheet_name.cell(row=i, column=1).value == train_num):
            mastersheet.append([cell_value(sheet_name,1,1), cell_value(sheet_name,i,1)])
            for j in range(2, sheet_name.max_column + 1):
                mastersheet.append([cell_value(sheet_name,1,j), cell_value(sheet_name,i,j)])
                workbook.save(r"D:\Python_Practice-1\18-03-2021\Train_Data.xlsx")

def cell_value(wo,ro,co):
    return (wo.cell(row=ro, column=co).value)


# workbook = load_workbook(r"D:\Python_Practice-1\18-03-2021\Train_Data.xlsx")
# # Getting the sheet names
# sheet_list=workbook.get_sheet_names()
# # Printing the total sheets
# print(sheet_list)    

if 'Mastersheet' in workbook.sheetnames:
    mas = workbook['Mastersheet']
    workbook.remove(mas)
workbook.create_sheet("Mastersheet")

train_num = int(input("Enter the train number : "))
for k in range(0, len(sheet_list)):
    sheetName = workbook[sheet_list[k]]
    train_number(workbook, sheetName, train_num)


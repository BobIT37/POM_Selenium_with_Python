import openpyxl

wb = openpyxl.Workbook()
sheet = wb.create_sheet("Users", 0)
sheet["A1"].value = "RegisterPageTitle"
sheet["B1"].value = "Users"

class writeData:

    def writeRTitle(rTitle):
        sheet["A2"].value = rTitle

    def writeUser(user):
        us = user.split('.')[0]
        print(us)
        sheet["B2"].value = us
        wb.save("users_list.xlsx")
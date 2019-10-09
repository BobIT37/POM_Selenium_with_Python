import xlrd

def getData(colvaluee):
    book = xlrd.open_workbook("C:\\Users\\vikky\\OneDrive\\Desktop\\Java\\TestData.xls")
    sheet = book.sheet_by_name("Sheet2")
    rows = sheet.row_values(0)
    col = sheet.col_values(0)
    scenarioname = "Login"
    column = -1
    row = -1
    columnValue = 0
    rowValue = 0
    for i in rows:
        if (i == colvaluee):
            columnValue = column + 1
        column = column + 1
    for j in col:
        if (j == scenarioname):
            rowValue = row + 1
        row = row + 1
    return sheet.cell(rowValue, columnValue).value
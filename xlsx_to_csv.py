# xlsx to csv util
import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('jesse_data.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    jesse_data = open('jesse_data.csv', 'w')
    wr = csv.writer(jesse_data, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    jesse_data.close()

csv_from_excel()
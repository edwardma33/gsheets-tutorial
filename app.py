import gspread

sa = gspread.service_account(filename='gsheets-tutorial-375204-6231900cc68b.json')
sh = sa.open('student-tests')

wks = sh.worksheet('class-data')

class gspread.cell.Cell(row, col, value='')
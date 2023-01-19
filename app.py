import gspread
import random

#Init service acc with service account file
sa = gspread.service_account(filename='gsheets-tutorial-375204-6231900cc68b.json')
#Open and assign specific sheet to var sh
sh = sa.open('student-tests')
#Pick a specific worksheet in the sheet
wks = sh.worksheet('class-data')


sports = ['basketball', 'soccer', 'football', 'track', 'cross country', 'hockey', 'volleyball', 'wrestling', 'cheer', 'baseball', 'lacrosse', 'golf', 'bowling']

ethnicities = ['black', 'white', 'hispanic', 'native american', 'asian', 'mixed']

cols_in_use = ['A', 'B', 'C', 'D', 'E']
def create_student():
    global wks
    stu_id = random.randint(100,1000)
    if str(stu_id) in wks.col_values(1):
        create_student()
    else:
        sex = random.randint(0, 1)
        if sex == 0:
            sex = "Male"
        else:
            sex = "Female"

        sport = sports[random.randint(0, len(sports) - 1)]
        ethnicity = ethnicities[random.randint(0, len(ethnicities) - 1)]
        test_score = random.randint(0, 101)

        new_student = {
            'A': stu_id,
            'B': sex,
            'C': sport,
            'D': ethnicity,
            'E': test_score,
        }

        row = len(wks.col_values(1)) + 1

        for col in cols_in_use:
            wks.update(f'{col}{row}', new_student[col])


for i in range(0, 12):
    create_student()
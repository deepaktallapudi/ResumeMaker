# Resume Builder in Python 
from turtle import color
from fpdf import FPDF
 
name = input("Enter name :-")
address = input("Enter your city :-")
phone = input("Enter your phone number :- ")
emailadress = input("Enter your email adress :- ")
linkedin = input("Enter your linkedin username :- ")

skills = []
print("Enter all your skills line by line, enter 0 to break :- ")
while True:
    ele  = input()
    if ele == '0' or ele == 0 :
        break  
    skills.append(ele)
       

outputskills = " "
for i in range(0 , len(skills)):
     outputskills += (skills[i] + ", ")

edeno = int(input(("Enter the number of courses you completed or completing :- ")))
InstName = []
CourseName = []
eduStartDate = []
eduEndDate = []
Score = []

for i in range(1 , edeno+1):
    print("Enter the details of course" , i )
    ede1 = input("Enter the name of the institution :-")
    ede2 = input("Enter the name of the course :-")
    ede3 = input("Enter the score of this course :-")
    ede4 = input("Enter the start date of this course (mm/yyyy) :-")
    ede5 = input("Enter the end date of this course (mm/yyyy) (enter 'p' if you are currently pursuing this course) :-")

    if ede5 == "p":
       ede5 = "present"

    InstName.append(ede1)
    CourseName.append(ede2)
    Score.append(ede3)
    eduStartDate.append(ede4)
    eduEndDate.append(ede5)
    print("\n\n")

prono = int(input(("Enter the number of projects :-")))
ProName = []
ProjectDescreption = []
proStartDate = []
proEndDate = []

for i in range(1 , prono+1):
    print("Enter the details of project" , i )
    pro1 = input("Enter the name of the project :-")
    pro2 = input("Enter the descreption of the project :-")
    pro3 = input("Enter the start date of this project (mm/yyyy) :-")
    pro4 = input("Enter the end date of this project (mm/yyyy) (enter 'p' if you are currently doing this project) :-")
    if pro4 == "p":
       pro4 = "present"
    ProName.append(pro1)
    ProjectDescreption.append(pro2)
    proStartDate.append(pro3)
    proEndDate.append(pro4)
    print("\n\n")


workno = int(input(("Enter the number of firms you have worked in :- ")))
companyName = []
workDescreption = []
compStartDate = []
compEndDate = []
role = []

for i in range(1, workno+1):
    print("Enter the details of work experience" , i )
    we1 = input("Enter the name of the firm :-")
    we2 = input("Enter the name of your role in the company :-")
    we3 = input("Enter the details of your work experience :-")
    we4 = input("Enter the start date (mm/yyyy)  :-")
    we5 = input("Enter the end date (mm/yyyy) (enter 'p' if you are currently working in this firm) :-")
    if we5 == "p":
       we5 = "present"
    companyName.append(we1)
    role.append(we2)
    workDescreption.append(we3)
    compStartDate.append(we4)
    compEndDate.append(we5)
    print("\n\n")


accomplishments = []
print("Enter your accomplishments and achievements line by line, enter 0 to break :- ")
while True: 
    ele  = input()
    if ele == '0' or ele == 0 :
        break
    accomplishments.append(ele)
   

intrests = []
print("Enter your intrests line by line, enter 0 to break :- ")
while True: 
    ele  = input()
    if ele == '0' or ele == 0 :
        break
    intrests.append(ele)
    
outputintrests = " "
for i in range(0 , len(intrests)):
     outputintrests += (intrests[i] + ", ")


######################################################################################################################################################

pdf = FPDF()
pdf.add_page()
pdf.image('face.png', 20, 2, 20)
pdf.image('line.png', 100, 4, 12)

pdf.set_x(110)
pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size = 13)
pdf.cell(20, 5, txt = phone,ln = 2, align = 'S')
pdf.cell(20, 5, txt = emailadress,ln = 3, align = 'S')
pdf.cell(20, 5, txt = linkedin,ln = 4, align = 'S')
pdf.cell(20, 5, txt = address,ln = 5, align = 'S')

pdf.set_text_color(0,0,0)
pdf.set_font("Arial", 'B' ,  size = 17)
pdf.set_y(30)
pdf.cell(10, 5, txt = name,ln = 6, align = 'S')

pdf.set_text_color(60, 121, 235)
pdf.set_y(35)
pdf.set_font("Times", size = 22)
pdf.cell(10, 15, "Skills",ln = 7, align = 'S')

pdf.set_text_color(0,0,0)
pdf.set_font("Arial", size = 15)
pdf.cell(10, 2, txt = outputskills,ln = 8, align = 'S')

if edeno>0:
  pdf.set_text_color(60, 121, 235)
  pdf.set_y(56)
  pdf.set_font("Times", size = 22)
  pdf.cell(10, 10, "Education",ln = 9, align = 'S')


  for i in range(0 , edeno):
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial"  , size = 13)
    x = InstName[i]
    x.strip()
    for j in range(0 , 35-len(x)):
        x +=  "  "

    x += '- ' + CourseName[i] 
    pdf.cell(30, 5, txt = x.upper(),ln = 9+i ,  align = 'S')
    pdf.set_text_color(143, 143, 143)
    pdf.set_font("Arial"  , size = 10)
    y = eduStartDate[i] + ' - ' + eduEndDate[i]  + "                                                                    " + Score[i]
    pdf.cell(30, 5, txt = y,ln = 10+i ,  align = 'S')

if prono>0:
  pdf.set_text_color(60, 121, 235)
  pdf.set_font("Times", size = 22)
  pdf.cell(10, 13, "Projects",ln = 12+edeno, align = 'S')


  for i1 in range(0 , prono):
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial", 'B'  , size = 15)
    x = ProName[i1]
    pdf.cell(10, 5, txt =x ,ln = 13+edeno+i1 ,  align = 'S')
    y = eduStartDate[i1] + ' - ' + eduEndDate[i1]
    pdf.set_text_color(143, 143, 143)
    pdf.set_font("Arial"  , size = 10)
    pdf.cell(10, 5, txt =y ,ln = 14+edeno+i1 ,  align = 'S')
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial" , size = 11)
    pdf.multi_cell(190 , 5 , ProjectDescreption[i1])

if workno>0 :
  pdf.set_text_color(60, 121, 235)
  pdf.set_font("Times", size = 22)
  pdf.cell(10, 13, "Work Experience",ln = 12+edeno, align = 'S')

  for i2 in range(0 , workno):
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial" , 'B'  , size = 15)
    x = role[i2]
    x.strip()
    for j in range(0 , 35-len(x)):
        x +=  "  "
    x +=  '- ' + companyName[i2] 
    pdf.cell(30, 5, txt = x,ln = 9+i2 ,  align = 'S')
    pdf.set_text_color(143, 143, 143)
    pdf.set_font("Arial"  , size = 10)
    y = compStartDate[i2] + ' - ' + compEndDate[i2]  
    pdf.cell(30, 5, txt = y,ln = 9+i2 ,  align = 'S')
    pdf.set_text_color(0,0,0)
    pdf.set_font("Arial" , size = 12)
    pdf.multi_cell(190 , 5 , workDescreption[i2])
    pdf.cell(30 , 2 , " " , ln = 9+i2 ,  align = 'S' )

if len(accomplishments)>0 :
  pdf.set_text_color(60, 121, 235)
  pdf.set_font("Times", size = 22)
  pdf.cell(10, 13, "Achievements and Acomplishments",ln = 7, align = 'S')

  pdf.set_text_color(0,0,0)
  pdf.set_font("Arial", size = 12)
  for l in range(0 , len(accomplishments)):
     o = "> " + accomplishments[l]
     pdf.multi_cell(190, 5, txt = o, align = 'S')

if len(intrests) > 0:
  pdf.set_text_color(60, 121, 235)
  pdf.set_font("Times", size = 22)
  pdf.cell(10, 10, "Intrests",ln = 7, align = 'S')

  pdf.set_text_color(0,0,0)
  pdf.set_font("Arial", size = 12)
  pdf.multi_cell(190, 5, txt = outputintrests, align = 'S')


pdf.output("MyResume.pdf")

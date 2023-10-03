from tkinter import *

questions = ["How many Dragon Balls are there?" ,
             "In the anime 'Hunter X Hunter', which family is famous for being assassins?" ,
             "Who is known as the 'One Punch Man'?" ,
             "What type of food does Naruto Uzumaki love the most?" ,
             "What was Ash ketchum's second pokemon?" ,
             "What is the title of the first Pokémon movie?" ,
             "What is the associated animal of the Sin of Pride (Escanor)?"]

options = [["3","7","10","99"],
           ["Zoldyck","Freeces","Uzumaki","Krueger"],
           ["Naruto","Saitama","Goku","Ash"],
           ["Pizza","Waffles","Ramen","Ice Cream"],
           ["Caterpie","Bulbasaur","Tauros","Pidgeotto"],
           ["Pokemon: The First Movie - Mewtwo Strikes Back","I Choose You!","Pokemon: A Journey Has Begun","Detective Pikachu"],
           ["Bear","Lion","Snake","Rhino"]]

answers = [2 , 1 , 2 , 3 , 4 , 1 , 2]

score = 0

total_No_questions = 7

question_No = 1

def next():
    global score, question_No
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    elif val4.get() == 1:
        selected_option = 4
    else:
        selected_option = - 1
    if(answers[question_No - 1] == selected_option):
        score += 1

    question_No += 1

    if question_No > total_No_questions:
        root.pack_forget()
        Score.place(relx = .40, rely = .40)
        Score.config(text = "Score: " + str(score))
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        val4.set(0)
        question.config(text = questions[question_No - 1])
        option1.config(text = options[question_No - 1][0])
        option2.config(text = options[question_No - 1][1])
        option3.config(text = options[question_No - 1][2])
        option4.config(text = options[question_No - 1][3])

def check(option):
    if(option == 1):
        val2.set(0)
        val3.set(0)
        val4.set(0)
    elif(option == 2):
        val1.set(0)
        val3.set(0)
        val4.set(0)
    elif(option == 3):
        val1.set(0)
        val2.set(0)
        val4.set(0)
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)

win = Tk()
win.title("Anime Trivia")

root = Frame()
root.pack()

question = Label(root, width = 60, font = (20), text = questions[0])
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()
val4 = IntVar()

option1 = Checkbutton(root, variable = val1, text = options[0][0], command = lambda: check(1))
option1.pack()

option2 = Checkbutton(root, variable = val2, text = options[0][1], command = lambda: check(2))
option2.pack()

option3 = Checkbutton(root, variable = val3, text = options[0][2], command = lambda: check(3))
option3.pack()

option4 = Checkbutton(root, variable = val4, text = options[0][3], command = lambda: check(4))
option4.pack()

next_b = Button(root, text = "Next", command = next)
next_b.pack()

Score = Label(win)
Score.place_forget()

win.mainloop()

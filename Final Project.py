# Author = Gabriel Bennett
# Last edited = October 2nd, 2023
# this is a GUI for the Anime N'cyclopedia website to help a person decide what anime to watch.


from tkinter import *
from tkinter import ttk
import subprocess

main_window = Tk()

main_window.geometry("1280x720")

canvas = Canvas(main_window,
                width = 1280,
                height = 720,
                background = "DeepPink2")

def main():
    button_quiz1 = ttk.Button
    button_quiz2 = ttk.Button
    button_quiz3 = ttk.Button
    
    quiz_1 = button_quiz1(main_window, 
        text = "What type of anime should I watch?", 
        command = quiz_one)
    quiz_1.pack(side = TOP)
    
    quiz_2 = button_quiz2(main_window, 
        text = "Which anime should I watch?",
        command = quiz_two)
    quiz_2.pack(side = TOP)

    quiz_3 = button_quiz3(main_window,
        text = "Your mom",
        command = quiz_three)
    quiz_3.pack(side = TOP)

def quiz_one():
    quiz_one_window = Tk()
    quiz_one_window.geometry("1280x720")
    quiz_one_canvas = Canvas(quiz_one_window, 
                            width = 1280,
                            height = 720,
                            bg = "DeepPink2")
    quiz_one_canvas.create_text(CENTER, text = "Anime N'Cyclopedia", fill = "Cyan", font = ('Times New Roman 24 Bold'))
    quiz_one_canvas.pack()
    quiz_one_window.mainloop()

def quiz_two():
    subprocess.run(["python", "GUI ANIME TRIVIA.py"])

def quiz_three():
    quiz_three_window = Tk()
    quiz_three_window.geometry("1280x720")

    root = Frame()
    root.pack()

    question = Label(root, width = 60, font = (20), text = anime_trivia_questions[0])
    question.pack()

    def next():
        global anime_trivia_score, anime_trivia_question_No, anime_trivia_score
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
        if(anime_trivia_answers[anime_trivia_question_No - 1] == selected_option):
            anime_trivia_score += 1

        anime_trivia_question_No += 1

        if anime_trivia_question_No > anime_trivia_total_No_questions:
            root.pack_forget()
            anime_trivia_score.place(relx = .40, rely = .40)
            anime_trivia_score.config(text = "Score: " + str(anime_trivia_score))
        else:
            val1.set(0)
            val2.set(0)
            val3.set(0)
            val4.set(0)
            question.config(text = anime_trivia_questions[anime_trivia_question_No - 1])
            option1.config(text = anime_trivia_questions[anime_trivia_question_No - 1][0])
            option2.config(text = anime_trivia_questions[anime_trivia_question_No - 1][1])
            option3.config(text = anime_trivia_questions[anime_trivia_question_No - 1][2])
            option4.config(text = anime_trivia_questions[anime_trivia_question_No - 1][3])



    option1 = Checkbutton(quiz_three_window, variable = val1, text = anime_trivia_options[0][0], command = lambda: check(1))
    option1.pack()

    option2 = Checkbutton(quiz_three_window, variable = val2, text = anime_trivia_options[0][1], command = lambda: check(2))
    option2.pack()

    option3 = Checkbutton(quiz_three_window, variable = val3, text = anime_trivia_options[0][2], command = lambda: check(3))
    option3.pack()

    option4 = Checkbutton(quiz_three_window, variable = val4, text = anime_trivia_options[0][3], command = lambda: check(4))
    option4.pack()

    next_b = Button(quiz_three_window, text = "Next", command = next)
    next_b.pack()


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


val1 = IntVar()
val2 = IntVar()
val3 = IntVar()
val4 = IntVar()

anime_trivia_answers = [2 , 1 , 2 , 3 , 4 , 1 , 2]

anime_trivia_score = 0

anime_trivia_total_No_questions = 7

anime_trivia_question_No = 1

anime_trivia_questions = ["How many Dragon Balls are there?" ,
                          "In the anime 'Hunter X Hunter', which family is famous for being assassins?" ,
                          "Who is known as the 'One Punch Man'?" ,
                          "What type of food does Naruto Uzumaki love the most?" ,
                          "What was Ash ketchum's second pokemon?" ,
                          "What is the title of the first Pokémon movie?" ,
                          "What is the associated animal of the Sin of Pride (Escanor)?"]

anime_trivia_options = [["3","7","10","99"],
                        ["Zoldyck","Freeces","Uzumaki","Krueger"],
                        ["Naruto","Saitama","Goku","Ash"],
                        ["Pizza","Waffles","Ramen","Ice Cream"],
                        ["Caterpie","Bulbasaur","Tauros","Pidgeotto"],
                        ["Pokemon: The First Movie - Mewtwo Strikes Back","I Choose You!","Pokemon: A Journey Has Begun","Detective Pikachu"],
                        ["Bear","Lion","Snake","Rhino"]]



main()
main_window.mainloop()

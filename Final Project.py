# Author = Gabriel Bennett
# Last edited = October 2nd, 2023
# this is a GUI for the Anime N'cyclopedia website to help a person decide what anime to watch.


from tkinter import *
from tkinter import ttk


main_window = Tk()

main_window.geometry("1920x1080")


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
    print("Answer with 1 for \"yes\" or 2 for \"no\"")
    answer = int(input("Do you N'joy combat?"))
    if answer == 1:
        print("you should")


def quiz_two():
    print("Not made yet, thank you")


def quiz_three():
    print("Not made yet, thank you")

main()
mainloop()

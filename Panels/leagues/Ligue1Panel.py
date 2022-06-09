from Panels.helper import *


class LiguePanel:
    def __init__(self, season):
        helper = HelperL1(season)

        window = Toplevel()
        window.title("Football project")
        window.geometry("1500x1000+300+0")

        canvas = Canvas(window, width=1500, height=1000, bg="black", highlightthickness=0)
        canvas.grid()

        # dodawanie zdjęcia
        image = ImageTk.PhotoImage(file='./images/stadiums/Parc_des_Princes.jpg')
        canvas.create_image(750, 500, image=image)

        # Przyciski do przechodzenia w inne panele
        button_font = ("Arial Bold", 25)
        searching_btn = Button(window, text="Wyszukiwanie", font=button_font, background='red',
                               command=helper.search)
        selection_of_eleven_btn = Button(window, text="Wybór Składu", font=button_font, background='red',
                                         command=helper.selection_of_lineup)
        generating_eleven_btn = Button(window, text="Generacja Składu", font=button_font, background='red',
                                       command=helper.generating_lineup)

        canvas.create_window(750, 150, window=searching_btn)
        canvas.create_window(750, 300, window=selection_of_eleven_btn)
        canvas.create_window(750, 450, window=generating_eleven_btn)

        window.mainloop()

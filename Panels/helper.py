import datetime
from tkinter import *
from tkinter.ttk import Combobox

from PIL import ImageGrab
from PIL import ImageTk

from application_service import App_controller
from application_service.Player import Player


class Helper:
    def __init__(self, season):
        self.__season = season

        # generowanie app controlera, aby móc obsługiwać wersję graficzną
        self.__app = App_controller.AppController(season)

        self._league = None

        # atrybuty potrzebne do generowania i wybierania składu, potrzebne są do funkcji wyszukiwania piłkarzy według
        # pozycji
        self.__defender = App_controller.Defender(season)
        self.__midfielder = App_controller.Midfielder(season)
        self.__forward = App_controller.Forward(season)

        # atrybuty potrzebne do wybierania składu
        self.__selected_formation_choice = None
        self.__selected_option10_choice = None
        self.__selected_option9_choice = None
        self.__selected_option8_choice = None
        self.__selected_option6_choice = None
        self.__selected_option7_choice = None
        self.__selected_option5_choice = None
        self.__selected_option4_choice = None
        self.__selected_option3_choice = None
        self.__selected_option2_choice = None
        self.__selected_option1_choice = None

        # atrybuty potrzebne do generowania składu
        self.__selected_formation_gen = None
        self.__selected_option_gen = None

        # atrybuty potrzebne do wyszukiwania piłkarzy
        self.__search_scrollbar = None
        self.__search_frame2 = None
        self.__search_frame = None
        self.__search_canvas = None
        self.__search_entry = None
        self.__search_selected_option = None

        # atrybut potrzebny do wyboru i generacji składu
        self.formations = ["4-3-3", "4-4-2", "4-5-1", "4-6-0", "4-2-4", "3-4-3", "3-5-2", "5-3-2", "5-4-1"]

        # domyślna czcionka w klasie
        self.__font = ("Arial Bold", 25)

    # panel do wyszukiwania piłkarzy
    def search(self):
        window = Toplevel()

        window.title("Football project")

        window.geometry("1500x1000+300+0")

        self.__search_frame = Frame(window)
        self.__search_frame.pack(fill=BOTH, expand=1)

        # konfiguracja scroll baru
        self.__search_canvas = Canvas(self.__search_frame)
        self.__search_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.__search_scrollbar = Scrollbar(self.__search_frame, orient=VERTICAL, command=self.__search_canvas.yview)
        self.__search_scrollbar.pack(side=RIGHT, fill=Y)

        self.__search_canvas.configure(yscrollcommand=self.__search_scrollbar.set)
        self.__search_canvas.bind('<Configure>', lambda e: self.__search_canvas.configure(
            scrollregion=self.__search_canvas.bbox("all")))

        # dodanie opisu
        self.__search_canvas.create_text(500, 20,
                                         text="Wybierz opcje według której chcesz szukać piłkarzy  a następnie podaj "
                                              "wartość. \nJeżeli wybierzesz opcję Klub wpisz nazwę klubu,"
                                              "\nw pozostałych przypadkach podaj liczbę a program wypisze piłkarzy"
                                              " o wartościach większych od podanej",
                                         font=("Arial Bold", 18))
        # dodanie comboboksa
        self.__search_selected_option = StringVar()

        values = [
            "Klub", "Gole", "Gole samobójcze", "Gole w pierwszej połowie", "Gole w drugiej połowie",
            "Gole strzelone jako pierwszy zawodnik w meczu", "Gole strzelone jako ostatni zawodnik w meczu",
            "Gole strzelone w meczu domowym", "Gole strzelone w meczu wyjazdowym",
            "Gole strzelone prawą nogą", "Gole strzelone lewą nogą", "Gole strzelone głową", "Gole z karnego",
            "Żółte kartki", "Czerwone kartki", "Liczba wejść", "Liczba zejść", "Gole w pierwszej i drugiej połowie",
            "Gole w domu i na wyjeździe", "Gole z lewej i prawej nogi", "Gole z lewej i prawej nogi oraz głową"]

        combo = Combobox(self.__search_frame, width=60, font=self.__font, values=values,
                         textvariable=self.__search_selected_option)

        # dodawanie labeli, przycisków i pola entry

        self.__search_canvas.create_window(700, 100, window=combo)

        label = Label(self.__search_frame, text="Wybierz opcję", font=self.__font)

        self.__search_canvas.create_window(20, 100, window=label)

        label2 = Label(self.__search_frame, text="Podaj wartość", font=self.__font)

        self.__search_canvas.create_window(20, 145, window=label2)

        self.__search_entry = Entry(self.__search_frame, font=self.__font, width=60)

        self.__search_canvas.create_window(700, 145, window=self.__search_entry)

        button = Button(self.__search_frame, text="Potwierdź", font=self.__font, command=self.__searching_ans)

        self.__search_canvas.create_window(600, 215, window=button)

        self.__search_frame2 = Frame(self.__search_canvas)

        self.__search_canvas.create_window((250, 320), window=self.__search_frame2, anchor="nw")

        window.mainloop()

    def __searching_ans(self):
        # usuwanie niepotrzebnych rzeczy z panelu
        self.__search_frame2.after(100, self.__search_frame2.destroy)
        self.__search_scrollbar.after(100, self.__search_scrollbar.destroy)

        # aktualizacja ramki
        self.__search_frame2 = Frame(self.__search_canvas)
        self.__search_canvas.create_window((250, 250), window=self.__search_frame2, anchor="nw")

        # aktualizacja scroll baru
        self.__search_scrollbar = Scrollbar(self.__search_frame, orient=VERTICAL, command=self.__search_canvas.yview)
        self.__search_scrollbar.pack(side=RIGHT, fill=Y)

        self.__search_canvas.configure(yscrollcommand=self.__search_scrollbar.set)
        self.__search_canvas.bind('<Configure>', lambda e: self.__search_canvas.configure(
            scrollregion=self.__search_canvas.bbox("all")))

        # Obsługa panelu wyszukiwania, dodawanie odpowiedzi według wartości z combo boksa
        value = self.__search_selected_option.get()
        value2 = self.__search_entry.get()
        if value != "Klub":
            value2 = int(self.__search_entry.get())

        if value == "Klub":
            for i in self.__app.search_players_club(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Klub: {}".format(i.get_club), font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()

        elif value == "Gole":
            for i in self.__app.search_players_more_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()

        elif value == "Gole samobójcze":
            for i in self.__app.search_players_more_own_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole samobójcze: {}".format(i.get_own_goals),
                               font=self.__font)
                label2.pack()
        elif value == "Gole w pierwszej połowie":
            for i in self.__app.search_players_more_first_half_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole w pierwszej połowie: {}".format(i.get_first_half_goals),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole w drugiej połowie":
            for i in self.__app.search_players_more_second_half_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole w drugiej połowie: {}".format(i.get_second_half_goals),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole strzelone jako pierwszy zawodnik w meczu":
            for i in self.__app.search_players_more_first_scorer_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2,
                               text="Gole strzelone jako pierwszy zawodnik w meczu: {}".format(i.get_first_scorer),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole strzelone jako ostatni zawodnik w meczu":
            for i in self.__app.search_players_more_last_scorer_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2,
                               text="Gole strzelone jako ostatni zawodnik w meczu: {}".format(i.get_last_scorer),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole strzelone w meczu domowym":
            for i in self.__app.search_players_more_home_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole strzelone w meczu domowym: {}".format(i.get_home_goals),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole strzelone w meczu wyjazdowym":
            for i in self.__app.search_players_more_away_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2,
                               text="Gole strzelone w meczu wyjazdowym: {}".format(i.get_away_goals),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole strzelone prawą nogą":
            for i in self.__app.search_players_more_right_foot_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2,
                               text="Gole strzelone prawą nogą: {}".format(i.get_right_foot_goals),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole strzelone lewą nogą":
            for i in self.__app.search_players_more_left_foot_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole strzelone lewą nogą: {}".format(i.get_left_foot_goals),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole strzelone głową":
            for i in self.__app.search_players_more_head_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole strzelone głową: {}".format(i.get_head_goals),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole z karnego":
            for i in self.__app.search_players_more_penalty_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole z karnego: {}".format(i.get_penalty), font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Żółte kartki":
            for i in self.__app.search_players_more_yellow_cards(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Żółte kartki: {}".format(i.get_yellow_cards),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Czerwone kartki":
            for i in self.__app.search_players_more_red_cards(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Czerwone kartki: {}".format(i.get_red_cards),
                               font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Liczba wejść":
            for i in self.__app.search_players_more_came_on(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Liczba wejść: {}".format(i.get_came_on), font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Liczba zejść":
            for i in self.__app.search_players_more_taken_off(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Liczba zejść: {}".format(i.get_taken_off), font=self.__font)
                label2.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole w pierwszej i drugiej połowie":
            for i in self.__app.search_players_more_first_and_second_half_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole w pierwszej połowie: {}".format(i.get_first_half_goals),
                               font=self.__font)
                label2.pack()
                label3 = Label(self.__search_frame2, text="Gole w drugiej połowie: {}".format(i.get_second_half_goals),
                               font=self.__font)
                label3.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole w domu i na wyjeździe":
            for i in self.__app.search_players_more_home_and_away_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole domowe: {}".format(i.get_home_goals), font=self.__font)
                label2.pack()
                label3 = Label(self.__search_frame2, text="Gole na wyjeździe: {}".format(i.get_away_goals),
                               font=self.__font)
                label3.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole z lewej i prawej nogi":
            for i in self.__app.search_players_more_right_and_left_foot_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole z lewej nogi: {}".format(i.get_left_foot_goals),
                               font=self.__font)
                label2.pack()
                label3 = Label(self.__search_frame2, text="Gole z prawej nogi: {}".format(i.get_right_foot_goals),
                               font=self.__font)
                label3.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        elif value == "Gole z lewej i prawej nogi oraz głową":
            for i in self.__app.search_players_more_right_and_left_foot_and_head_goals(value2):
                label = Label(self.__search_frame2, text=i, font=self.__font)
                label.pack()
                label2 = Label(self.__search_frame2, text="Gole z lewej nogi: {}".format(i.get_left_foot_goals),
                               font=self.__font)
                label2.pack()
                label3 = Label(self.__search_frame2, text="Gole z prawej nogi: {}".format(i.get_right_foot_goals),
                               font=self.__font)
                label3.pack()
                label4 = Label(self.__search_frame2, text="Gole głową: {}".format(i.get_head_goals),
                               font=self.__font)
                label4.pack()
                line = Label(self.__search_frame2, text="\n", font=self.__font)
                line.pack()
        else:
            exit()

    # panel generowania składu
    def generating_lineup(self):
        window = Toplevel()

        window.title("Football project")

        window.geometry("1500x1000+300+0")

        frame = Frame(window)
        frame.pack()

        # wartości do i z combo boksa
        self.__selected_option_gen = StringVar()
        self.__selected_formation_gen = StringVar()

        values = [
            "Gole", "Gole samobójcze", "Gole w pierwszej połowie", "Gole w drugiej połowie",
            "Gole strzelone jako pierwszy zawodnik w meczu", "Gole strzelone jako ostatni zawodnik w meczu",
            "Gole strzelone w meczu domowym", "Gole strzelone w meczu wyjazdowym",
            "Gole strzelone prawą nogą", "Gole strzelone lewą nogą", "Gole strzelone głową", "Gole z karnego",
            "Żółte kartki", "Liczba wejść", "Liczba zejść"]

        # dodanie opisu
        label = Label(frame,
                      text="Wybierz formację jaką chcesz żeby miał twój skład\n a następnie wybierz opcję według której"
                           " ma być generowany.\n Program pobiera zawodników z najlepszą statystyką danej opcji. ",
                      font=("Arial Bold", 18))
        label.grid(row=0, column=1)

        # dodawanie labeli, combo boksa i przycisku
        label = Label(frame, text="Wybierz formację", font=self.__font)
        label.grid(row=1, column=0)

        formation = Combobox(frame, width=60, font=self.__font, values=self.formations,
                             textvariable=self.__selected_formation_gen)
        formation.grid(row=1, column=1)

        combo = Combobox(frame, width=60, font=self.__font, values=values, textvariable=self.__selected_option_gen)
        combo.grid(row=2, column=1)

        label = Label(frame, text="Wybierz opcję", font=self.__font)
        label.grid(row=2, column=0)

        button = Button(frame, text="Potwierdź", font=self.__font, command=self.__football_pitch_generation)
        button.grid(row=3, column=1)

        window.mainloop()

    # Panel do wyświetlania składu wygenerowanego
    def __football_pitch_generation(self):
        window = Toplevel()
        window.title("Football project")
        window.geometry("1500x1000+300+0")
        window.resizable(False, False)

        canvas = Canvas(window, width=1500, height=1000, bg="black", highlightthickness=0)
        canvas.grid()

        # Dodawanie zdjęcia
        image = ImageTk.PhotoImage(file='./images/_boisko.jpg')
        canvas.create_image(750, 500, image=image)

        # pobieranie wartości z poprzedniego panelu
        value = self.__selected_option_gen.get()
        formation = self.__selected_formation_gen.get()

        defender_number = int(formation[0])
        midfielder_number = int(formation[2])
        forward_number = int(formation[4])

        # Ustawianie odległości między zawodnikami z tej samej pozycji
        distance_between_defenders = 1000 / (defender_number + 1)
        distance_between_midfielder = 1000 / (midfielder_number + 1)
        distance_between_forward = 1000 / (forward_number + 1)

        # Wyświetlanie odpowiednich zawodników na kanwie
        for i in range(defender_number):
            canvas.create_text(1200, distance_between_defenders * (i + 1),
                               text=self.__search_player_position(value, defender_number, "Defender")[
                                   i].get_name,
                               font=("Arial Bold", 25), fill="white")
        for i in range(midfielder_number):
            canvas.create_text(800, distance_between_midfielder * (i + 1),
                               text=self.__search_player_position(value, midfielder_number, "Midfielder")[
                                   i].get_name, font=("Arial Bold", 25), fill="white")
        for i in range(forward_number):
            canvas.create_text(400, distance_between_forward * (i + 1),
                               text=self.__search_player_position(value, forward_number, "Forward")[i].get_name,
                               font=("Arial Bold", 25), fill="white")

        # Dodawanie przycisku zapisania zrzutu ekranu
        button = Button(window, text="Zapisz skład", font=self.__font, command=self.screen)
        canvas.create_window(300, 20, window=button)

        window.mainloop()

    # Panel wyboru składu
    def selection_of_lineup(self):
        window = Toplevel()
        window.title("Football project")
        window.geometry("1500x1000+300+0")

        frame = Frame(window)
        frame.pack()

        # wartości z combo boksa
        self.__selected_option1_choice = StringVar()
        self.__selected_option2_choice = StringVar()
        self.__selected_option3_choice = StringVar()
        self.__selected_option4_choice = StringVar()
        self.__selected_option5_choice = StringVar()
        self.__selected_option6_choice = StringVar()
        self.__selected_option7_choice = StringVar()
        self.__selected_option8_choice = StringVar()
        self.__selected_option9_choice = StringVar()
        self.__selected_option10_choice = StringVar()
        self.__selected_formation_choice = StringVar()

        # dodanie opisu
        label = Label(frame,
                      text="Wybierz formację jaką chcesz żeby miał twój skład\n a następnie wybierz opcję "
                           "dla każdego piłkarza\n Program pobiera zawodników z najlepszą statystyką danej opcji. ",
                      font=("Arial Bold", 18))
        label.grid(row=0, column=1)
        # wartości combo boksa
        values = [
            "Gole", "Gole samobójcze", "Gole w pierwszej połowie", "Gole w drugiej połowie",
            "Gole strzelone jako pierwszy zawodnik w meczu", "Gole strzelone jako ostatni zawodnik w meczu",
            "Gole strzelone w meczu domowym", "Gole strzelone w meczu wyjazdowym",
            "Gole strzelone prawą nogą", "Gole strzelone lewą nogą", "Gole strzelone głową", "Gole z karnego",
            "Żółte kartki", "Liczba wejść", "Liczba zejść"]

        # dodawanie labeli, przycisków i combo boksa
        label = Label(frame, text="Wybierz formację", font=self.__font)
        label.grid(row=1, column=0)

        formation = Combobox(frame, width=48, font=self.__font, values=self.formations,
                             textvariable=self.__selected_formation_choice)
        formation.grid(row=1, column=1)

        combo1 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option1_choice)
        combo1.grid(row=2, column=1)
        label1 = Label(frame, text="Wybierz opcję pierwszego piłkarza", font=self.__font)
        label1.grid(row=2, column=0)

        combo2 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option2_choice)
        combo2.grid(row=3, column=1)
        label2 = Label(frame, text="Wybierz opcję drugiego piłkarza", font=self.__font)
        label2.grid(row=3, column=0)

        combo3 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option3_choice)
        combo3.grid(row=4, column=1)
        label3 = Label(frame, text="Wybierz opcję trzeciego piłkarza", font=self.__font)
        label3.grid(row=4, column=0)

        combo4 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option4_choice)
        combo4.grid(row=5, column=1)
        label4 = Label(frame, text="Wybierz opcję czwartego piłkarza", font=self.__font)
        label4.grid(row=5, column=0)

        combo5 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option5_choice)
        combo5.grid(row=6, column=1)
        label5 = Label(frame, text="Wybierz opcję piątego piłkarza", font=self.__font)
        label5.grid(row=6, column=0)

        combo6 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option6_choice)
        combo6.grid(row=7, column=1)
        label6 = Label(frame, text="Wybierz opcję szóstego piłkarza", font=self.__font)
        label6.grid(row=7, column=0)

        combo7 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option7_choice)
        combo7.grid(row=8, column=1)
        label7 = Label(frame, text="Wybierz opcję siódmego piłkarza", font=self.__font)
        label7.grid(row=8, column=0)

        combo8 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option8_choice)
        combo8.grid(row=9, column=1)
        label8 = Label(frame, text="Wybierz opcję ósmego piłkarza", font=self.__font)
        label8.grid(row=9, column=0)

        combo9 = Combobox(frame, width=48, font=self.__font, values=values, textvariable=self.__selected_option9_choice)
        combo9.grid(row=10, column=1)
        label9 = Label(frame, text="Wybierz opcję dziewiątego piłkarza", font=self.__font)
        label9.grid(row=10, column=0)

        combo10 = Combobox(frame, width=48, font=self.__font, values=values,
                           textvariable=self.__selected_option10_choice)
        combo10.grid(row=11, column=1)
        label10 = Label(frame, text="Wybierz opcję dziesiątego piłkarza", font=self.__font)
        label10.grid(row=11, column=0)

        button = Button(frame, text="Potwierdź", font=self.__font, command=self.__football_pitch_select)
        button.grid(row=12, column=1)

        window.mainloop()

    # panel wyświetlania piłkarzy z panelu wyboru składu
    def __football_pitch_select(self):
        window = Toplevel()
        window.title("Football project")
        window.geometry("1500x1000+300+0")
        window.resizable(False, False)

        canvas = Canvas(window, width=1500, height=1000, bg="black", highlightthickness=0)
        canvas.grid()

        # Dodawanie zdjęcia
        image = ImageTk.PhotoImage(file='./images/_boisko.jpg')
        canvas.create_image(750, 500, image=image)

        # pobieranie wartości z poprzedniego panelu
        value1 = self.__selected_option1_choice.get()
        value2 = self.__selected_option2_choice.get()
        value3 = self.__selected_option3_choice.get()
        value4 = self.__selected_option4_choice.get()
        value5 = self.__selected_option5_choice.get()
        value6 = self.__selected_option6_choice.get()
        value7 = self.__selected_option7_choice.get()
        value8 = self.__selected_option8_choice.get()
        value9 = self.__selected_option9_choice.get()
        value10 = self.__selected_option10_choice.get()
        formation = self.__selected_formation_choice.get()

        # lista opcji zawodników
        values = [value1, value2, value3, value4, value5, value6, value7, value8, value9, value10]

        # listy z zawodnikami danej pozycji
        defenders = []
        midfielders = []
        forwards = []

        # pobieranie ilości zawodników danej pozycji
        defender_number = int(formation[0])
        midfielder_number = int(formation[2])
        forward_number = int(formation[4])

        # dodawanie zawodników do odpowiednich list
        for j in range(0, defender_number):
            current_defenders = self.__search_player_position(value=values[j], number=10, position="Defender")

            # sprawdzanie, czy wyszukany zawodnik, nie został znaleziony wcześniej
            for i in range(defender_number):
                if not current_defenders[i] in defenders:
                    defenders.append(current_defenders[i])
                    break

        for q in range(defender_number, (midfielder_number + defender_number)):
            current_midfielders = self.__search_player_position(value=values[q], number=10, position="Midfielder")

            # sprawdzanie, czy wyszukany zawodnik, nie został znaleziony wcześniej
            for i in range(midfielder_number):
                if not current_midfielders[i] in midfielders:
                    midfielders.append(current_midfielders[i])
                    break

        for w in range((midfielder_number + defender_number), (defender_number + midfielder_number + forward_number)):
            current_forwards = self.__search_player_position(value=values[w], number=10, position="Forward")

            # sprawdzanie, czy wyszukany zawodnik, nie został znaleziony wcześniej
            for i in range(forward_number):
                if not current_forwards[i] in forwards:
                    forwards.append(current_forwards[i])
                    break

        # Ustawianie odległości między zawodnikami z tej samej pozycji
        distance_between_defenders = 1000 / (defender_number + 1)
        distance_between_midfielder = 1000 / (midfielder_number + 1)
        distance_between_forward = 1000 / (forward_number + 1)

        # Wyświetlanie odpowiednich zawodników na kanwie
        for defender_num in range(defender_number):
            canvas.create_text(1200, distance_between_defenders * (defender_num + 1),
                               text=defenders[defender_num].get_name,
                               font=("Arial Bold", 25), fill="white")
        for mid_num in range(midfielder_number):
            canvas.create_text(800, distance_between_midfielder * (mid_num + 1),
                               text=midfielders[mid_num].get_name,
                               font=("Arial Bold", 25), fill="white")

        for forward_num in range(forward_number):
            canvas.create_text(400, distance_between_forward * (forward_num + 1),
                               text=forwards[forward_num].get_name,
                               font=("Arial Bold", 25), fill="white")

        # Dodawanie przycisku zapisania zrzutu ekranu
        button = Button(window, text="Zapisz skład", font=self.__font, command=self.screen)
        canvas.create_window(300, 20, window=button)

        window.mainloop()

    # Panel do wyszukiwania odpowiednich piłkarzy z danej pozycji
    def __search_player_position(self, value, number, position):
        position_app = self.__midfielder

        # określenie pozycji
        if position == "Defender":
            position_app = self.__defender
        elif position == "Midfielder":
            position_app = self.__midfielder
        elif position == "Forward":
            position_app = self.__forward

        # wyszukiwanie zawodników z danej pozycji o danej opcji wyszukiwania
        current_list = []
        if value == "Gole":
            for i in range(number):
                if len(position_app.search_players_more_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_goals(0)[i])

        elif value == "Gole samobójcze":
            for i in range(number):
                if len(position_app.search_players_more_own_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_own_goals(0)[i])

        elif value == "Gole w pierwszej połowie":
            for i in range(number):
                if len(position_app.search_players_more_first_half_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_first_half_goals(0)[i])

        elif value == "Gole w drugiej połowie":
            for i in range(number):
                if len(position_app.search_players_more_second_half_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_second_half_goals(0)[i])

        elif value == "Gole strzelone jako pierwszy zawodnik w meczu":
            for i in range(number):
                if len(position_app.search_players_more_first_scorer_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_first_scorer_goals(0)[i])

        elif value == "Gole strzelone jako ostatni zawodnik w meczu":
            for i in range(number):
                if len(position_app.search_players_more_last_scorer_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_last_scorer_goals(0)[i])

        elif value == "Gole strzelone w meczu domowym":
            for i in range(number):
                if len(position_app.search_players_more_home_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_home_goals(0)[i])

        elif value == "Gole strzelone w meczu wyjazdowym":
            for i in range(number):
                if len(position_app.search_players_more_away_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_away_goals(0)[i])

        elif value == "Gole strzelone prawą nogą":
            for i in range(number):
                if len(position_app.search_players_more_right_foot_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_right_foot_goals(0)[i])

        elif value == "Gole strzelone lewą nogą":
            for i in range(number):
                if len(position_app.search_players_more_left_foot_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_left_foot_goals(0)[i])

        elif value == "Gole strzelone głową":
            for i in range(number):
                if len(position_app.search_players_more_head_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_head_goals(0)[i])

        elif value == "Gole z karnego":
            for i in range(number):
                if len(position_app.search_players_more_penalty_goals(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_penalty_goals(0)[i])

        elif value == "Żółte kartki":
            for i in range(number):
                if len(position_app.search_players_more_yellow_cards(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_yellow_cards(0)[i])

        elif value == "Liczba wejść":
            for i in range(number):
                if len(position_app.search_players_more_came_on(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_came_on(0)[i])

        elif value == "Liczba zejść":
            for i in range(number):
                if len(position_app.search_players_more_taken_off(0)) <= i:
                    # dodawanie sztucznego zawodnika, gdyby w bazie zabrakło zawodników o danej opcji wyszukiwania
                    current_list.append(
                        Player(" ", " ", "Brak zawodnika", " ", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0))
                else:
                    current_list.append(position_app.search_players_more_taken_off(0)[i])

        return current_list

    # funkcja do łatwego zmieniania niezbędnych atrybutów przy używaniu podklas
    def _set_league(self, league):
        self._league = league

        if self._league == "Premier League":
            self.__defender = App_controller.DefenderPL(self.__season)
            self.__midfielder = App_controller.MidfielderPL(self.__season)
            self.__forward = App_controller.ForwardPL(self.__season)
            self.__app = App_controller.PremierLeague(self.__season)

        elif self._league == "Bundesliga":
            self.__defender = App_controller.DefenderBL(self.__season)
            self.__midfielder = App_controller.MidfielderBL(self.__season)
            self.__forward = App_controller.ForwardBL(self.__season)
            self.__app = App_controller.Bundesliga(self.__season)

        elif self._league == "La Liga":
            self.__defender = App_controller.DefenderLL(self.__season)
            self.__midfielder = App_controller.MidfielderLL(self.__season)
            self.__forward = App_controller.ForwardLL(self.__season)
            self.__app = App_controller.LaLiga(self.__season)

        elif self._league == "Ligue 1":
            self.__defender = App_controller.DefenderL1(self.__season)
            self.__midfielder = App_controller.MidfielderL1(self.__season)
            self.__forward = App_controller.ForwardL1(self.__season)
            self.__app = App_controller.Ligue(self.__season)

        elif self._league == "Serie A":
            self.__defender = App_controller.DefenderSA(self.__season)
            self.__midfielder = App_controller.MidfielderSA(self.__season)
            self.__forward = App_controller.ForwardSA(self.__season)
            self.__app = App_controller.SerieA(self.__season)

    # funkcja zapisująca screenshot wraz z aktualną datą do katalogu lineups_saves
    def screen(self):
        im = ImageGrab.grab(bbox=(350, 120, 1750, 950))
        date = str(datetime.datetime.now().year) + "_" + str(datetime.datetime.now().month) + "_" + str(
            datetime.datetime.now().day) + "_" + str(datetime.datetime.now().hour) + "_" + str(
            datetime.datetime.now().minute) + "_" + str(datetime.datetime.now().second) + "_" + str(
            datetime.datetime.now().microsecond)
        name = "zapis_skladu" + "_" + str(self._league) + "_" + str(self.__season) + "_" + date + ".jpg"

        im.save('./lineups_saves/{}'.format(name))


# klasy dziedziczące po klasie Helper w celu łatwiejszego przeszukiwania poszczególnych lig
class HelperPL(Helper):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("Premier League")


class HelperBL(Helper):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("Bundesliga")


class HelperLL(Helper):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("La Liga")


class HelperL1(Helper):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("Ligue 1")


class HelperSA(Helper):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("Serie A")

from tkinter import *

from PIL import ImageTk

from Panels.leagues.BundesligaPanel import BundesligaPanel
from Panels.leagues.LaligaPanel import LaLigaPanel
from Panels.leagues.Ligue1Panel import LiguePanel
from Panels.leagues.PremierLeaguePanel import PremierLeaguePanel
from Panels.leagues.SerieAPanel import SerieAPanel
from Panels.leagues.wszystkieLigi import WszystkieLigi


# funkcje do przechodzenia w inne panele
def bundesliga_panel():
    BundesligaPanel("2016-17")


def serie_a_panel():
    SerieAPanel("2016-17")


def ligue_panel():
    LiguePanel("2016-17")


def laliga_panel():
    LaLigaPanel("2016-17")


def premier_league_panel():
    PremierLeaguePanel("2016-17")


def wszystkie_ligi():
    WszystkieLigi("2016-17")


class Gui2016_17:
    def __init__(self):
        self.__image1 = None

        window = Toplevel()
        window.title("Football project")
        window.geometry("1500x1000+300+0")

        canvas = Canvas(window, width=1500, height=1000, bg="black", highlightthickness=0)
        canvas.pack()

        # dodawanie zdjęcia
        image = ImageTk.PhotoImage(file="./images/seasons/2016_17.jpg")
        canvas.create_image(750, 500, image=image)

        # napis tytułu
        canvas.create_text(750, 50, fill="yellow", font=("Arial Bold", 60),
                           text="Baza piłkarzy z sezonu 2016/17")

        # Przyciski do przechodzenia w inne panele
        button_font = ("Arial Bold", 25)

        all_leagues_btn = Button(window, text="Wszystkie Ligi", font=button_font, background='#999999',
                                 command=wszystkie_ligi)
        premier_league_btn = Button(window, text="Premier League", font=button_font, background='#999999',
                                    command=premier_league_panel)
        la_Liga_btn = Button(window, text="La Liga", font=button_font, background='#999999', command=laliga_panel)
        ligue_1_btn = Button(window, text="Ligue 1", font=button_font, background='#999999', command=ligue_panel)
        serie_A_btn = Button(window, text="Serie A", font=button_font, background='#999999', command=serie_a_panel)
        bundesliga_btn = Button(window, text="Bundesliga", font=button_font, background='#999999',
                                command=bundesliga_panel)

        canvas.create_window(125, 150, window=all_leagues_btn)
        canvas.create_window(400, 150, window=la_Liga_btn)
        canvas.create_window(675, 150, window=premier_league_btn)
        canvas.create_window(950, 150, window=serie_A_btn)
        canvas.create_window(1200, 150, window=bundesliga_btn)
        canvas.create_window(1425, 150, window=ligue_1_btn)

        window.mainloop()

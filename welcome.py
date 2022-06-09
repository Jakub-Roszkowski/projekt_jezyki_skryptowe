from tkinter import *

from PIL import ImageTk

from Panels.seasons.season2014_15 import Gui2014_15
from Panels.seasons.season2015_16 import Gui2015_16
from Panels.seasons.season2016_17 import Gui2016_17
from Panels.seasons.season2017_18 import Gui2017_18
from Panels.seasons.season2018_19 import Gui2018_19


# funkcje do przechodzenia w inne panele
def season2014_15():
    Gui2014_15()


def season2015_16():
    Gui2015_16()


def season2016_17():
    Gui2016_17()


def season2017_18():
    Gui2017_18()


def season2018_19():
    Gui2018_19()


class WelcomeGui:
    def __init__(self):
        self.__image1 = None

        window = Tk()
        window.title("Football project")
        window.geometry("1500x1000+300+0")

        self.__canvas = Canvas(window, width=1500, height=1000, bg="black", highlightthickness=0)
        self.__canvas.pack()

        # dodawanie zdjęcia
        image = ImageTk.PhotoImage(file="images/pilka.jpg")
        self.__canvas.create_image(750, 500, image=image)

        # napis tytułu
        self.__canvas.create_text(750, 50, fill="yellow", font=("Arial Bold", 60),
                                  text="Witam w projekcie Football")

        # Przyciski do przechodzenia w inne panele
        button_font = ("Arial Bold", 25)

        season2014_15btn = Button(text="Sezon 2014-2015", font=button_font, background='#999999',
                                  command=season2014_15)
        season2015_16btn = Button(text="Sezon 2015-2016", font=button_font, background='#999999',
                                  command=season2015_16)
        season2016_17btn = Button(text="Sezon 2016-2017", font=button_font, background='#999999', command=season2016_17)
        season2017_18btn = Button(text="Sezon 2017-2018", font=button_font, background='#999999', command=season2017_18)
        season2018_19btn = Button(text="Sezon 2018-2019", font=button_font, background='#999999', command=season2018_19)

        self.__canvas.create_window(150, 300, window=season2014_15btn)
        self.__canvas.create_window(450, 300, window=season2015_16btn)
        self.__canvas.create_window(750, 300, window=season2016_17btn)
        self.__canvas.create_window(1050, 300, window=season2017_18btn)
        self.__canvas.create_window(1350, 300, window=season2018_19btn)

        window.mainloop()


if __name__ == '__main__':
    gui = WelcomeGui()

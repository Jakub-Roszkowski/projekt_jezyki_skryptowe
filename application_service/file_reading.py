from itertools import islice

from application_service.Player import Player

# Ścieżki do odpowiednich plików z bazami danych
FILE_PATH14_15 = "./database_files/baza2014-15.csv"
FILE_PATH15_16 = "./database_files/baza2015-16.csv"
FILE_PATH16_17 = "./database_files/baza2016-17.csv"
FILE_PATH17_18 = "./database_files/baza2017-18.csv"
FILE_PATH18_19 = "./database_files/baza2018-19.csv"


class FileService:
    def __init__(self, season):
        self.__season = season
        self.__players = []
        self.__playersPremierLeague = []
        self.__playersBundesliga = []
        self.__playersLaLiga = []
        self.__playersLigue1 = []
        self.__playersSerieA = []
        self.__file = None

    # Getery do pozyskania odpowiednich list z piłkarzami
    def get_players_list(self):
        return self.__players

    def get_premier_league_players_list(self):
        return self.__playersPremierLeague

    def get_bundesliga_players_list(self):
        return self.__playersBundesliga

    def get_la_liga_players_list(self):
        return self.__playersLaLiga

    def get_ligue1_players_list(self):
        return self.__playersLigue1

    def get_serie_a_players_list(self):
        return self.__playersSerieA

    # Funkcja do odczytania z pliku, zapisania danych do klasy Player, a następnie do odpowiednich list

    def make_data(self):
        if self.__season == "2014-15":
            self.__file = FILE_PATH14_15
        elif self.__season == "2015-16":
            self.__file = FILE_PATH15_16
        elif self.__season == "2016-17":
            self.__file = FILE_PATH16_17
        elif self.__season == "2017-18":
            self.__file = FILE_PATH17_18
        elif self.__season == "2018-19":
            self.__file = FILE_PATH18_19

        file = open(self.__file, 'r', encoding='utf-8')

        for line in islice(file, 1, None):
            temp_line = line.split(',')

            if temp_line[13] == "Player":
                league = temp_line[0]
                club = temp_line[1]
                name = temp_line[4]
                position = temp_line[5]
                appearances = int(temp_line[6])
                goals = int(temp_line[7])

                if temp_line[10] != "" and temp_line[10] != "-":
                    cameOn = int(temp_line[10])
                else:
                    cameOn = 0

                if temp_line[11] != "" and temp_line[11] != "-":
                    takenOff = int(temp_line[11])
                else:
                    takenOff = 0

                if temp_line[12] != "" and temp_line[12] != "-":
                    ownGoals = int(temp_line[12])
                else:
                    ownGoals = 0

                if temp_line[14] != "" and temp_line[14] != "-":
                    firstHalfGoals = int(temp_line[14])
                else:
                    firstHalfGoals = 0

                if temp_line[15] != "" and temp_line[15] != "-":
                    secondHalfGoals = int(temp_line[15])
                else:
                    secondHalfGoals = 0

                if temp_line[16] != "" and temp_line[16] != "-":
                    firstScorer = int(temp_line[16])
                else:
                    firstScorer = 0

                if temp_line[17] != "" and temp_line[17] != "-":
                    lastScorer = int(temp_line[17])
                else:
                    lastScorer = 0

                if temp_line[18] != "" and temp_line[18] != "-":
                    homeGoals = int(temp_line[18])
                else:
                    homeGoals = 0

                if temp_line[19] != "" and temp_line[19] != "-":
                    awayGoals = int(temp_line[19])
                else:
                    awayGoals = 0

                if temp_line[20] != "" and temp_line[20] != "-":
                    rightFootGoals = int(temp_line[20])
                else:
                    rightFootGoals = 0

                if temp_line[21] != "" and temp_line[21] != "-":
                    leftFootGoals = int(temp_line[21])
                else:
                    leftFootGoals = 0

                if temp_line[22] != "" and temp_line[22] != "-":
                    headGoals = int(temp_line[22])
                else:
                    headGoals = 0

                if temp_line[29] != "" and temp_line[29] != "-":
                    penalty = int(temp_line[29])
                else:
                    penalty = 0

                if temp_line[41] != "" and temp_line[41] != "-":
                    yellowCards = int(temp_line[41])
                else:
                    yellowCards = 0

                if temp_line[49] != "" and temp_line[49] != "-":
                    redCards = int(temp_line[49])
                else:
                    redCards = 0

                # Zapisywanie danych poprzez klase Player do odpowiednich list

                self.__players.append(
                    Player(league, club, name, position, appearances, goals, cameOn, takenOff, ownGoals, firstHalfGoals,
                           secondHalfGoals, firstScorer, lastScorer, homeGoals, awayGoals, rightFootGoals,
                           leftFootGoals,
                           headGoals, penalty, yellowCards, redCards))

                if league == 'Premier League':
                    self.__playersPremierLeague.append(
                        Player(league, club, name, position, appearances, goals, cameOn, takenOff, ownGoals,
                               firstHalfGoals,
                               secondHalfGoals, firstScorer, lastScorer, homeGoals, awayGoals, rightFootGoals,
                               leftFootGoals,
                               headGoals, penalty, yellowCards, redCards))

                elif league == 'Bundesliga':
                    self.__playersBundesliga.append(
                        Player(league, club, name, position, appearances, goals, cameOn, takenOff, ownGoals,
                               firstHalfGoals,
                               secondHalfGoals, firstScorer, lastScorer, homeGoals, awayGoals, rightFootGoals,
                               leftFootGoals,
                               headGoals, penalty, yellowCards, redCards))

                elif league == 'La Liga':
                    self.__playersLaLiga.append(
                        Player(league, club, name, position, appearances, goals, cameOn, takenOff, ownGoals,
                               firstHalfGoals,
                               secondHalfGoals, firstScorer, lastScorer, homeGoals, awayGoals, rightFootGoals,
                               leftFootGoals,
                               headGoals, penalty, yellowCards, redCards))

                elif league == 'French Ligue 1':
                    self.__playersLigue1.append(
                        Player(league, club, name, position, appearances, goals, cameOn, takenOff, ownGoals,
                               firstHalfGoals,
                               secondHalfGoals, firstScorer, lastScorer, homeGoals, awayGoals, rightFootGoals,
                               leftFootGoals,
                               headGoals, penalty, yellowCards, redCards))

                elif league == 'Serie A':
                    self.__playersSerieA.append(
                        Player(league, club, name, position, appearances, goals, cameOn, takenOff, ownGoals,
                               firstHalfGoals,
                               secondHalfGoals, firstScorer, lastScorer, homeGoals, awayGoals, rightFootGoals,
                               leftFootGoals,
                               headGoals, penalty, yellowCards, redCards))

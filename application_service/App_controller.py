from application_service.file_reading import FileService


class AppController:
    def __init__(self, season):
        self.__fileService = FileService(season=season)
        self.__fileService.make_data()
        self.__league = None
        self.__position = None
        self.__chosen_list = self.__fileService.get_players_list()

    # funkcja umożliwiająca obsługę dodatkowych klas z ligami
    def _set_league(self, league):
        self.__league = league

        if self.__league == "Premier League":
            self.__chosen_list = self.__fileService.get_premier_league_players_list()

        elif self.__league == "Bundesliga":
            self.__chosen_list = self.__fileService.get_bundesliga_players_list()

        elif self.__league == "La Liga":
            self.__chosen_list = self.__fileService.get_la_liga_players_list()

        elif self.__league == "Ligue 1":
            self.__chosen_list = self.__fileService.get_ligue1_players_list()

        elif self.__league == "Serie A":
            self.__chosen_list = self.__fileService.get_serie_a_players_list()

    # funkcja umożliwiająca obsługę dodatkowych klas z pozycjami
    def _set_position(self, position):
        self.__position = position
        current_list = []

        if self.__position == "Forward":
            for i in self.__chosen_list:
                if i.get_position == "Forward":
                    current_list.append(i)
            self.__chosen_list = current_list

        elif self.__position == "Midfielder":
            for i in self.__chosen_list:
                if i.get_position == "Midfielder":
                    current_list.append(i)
            self.__chosen_list = current_list

        elif self.__position == "Defender":
            for i in self.__chosen_list:
                if i.get_position == "Defender":
                    current_list.append(i)
            self.__chosen_list = current_list

    # funkcje wyszukujące piłkarzy według parametrów
    def search_player_name(self, name):
        for i in self.__chosen_list:
            if i.get_name == name:
                return i

    def search_players_club(self, club):
        current_list = []

        for i in self.__chosen_list:
            if i.get_club == club:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_goals, reverse=True)

    def search_players_more_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_goals, reverse=True)

    def search_players_more_own_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_own_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_own_goals, reverse=True)

    def search_players_more_first_half_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_first_half_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_first_half_goals, reverse=True)

    def search_players_more_second_half_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_second_half_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_second_half_goals, reverse=True)

    def search_players_more_first_scorer_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_first_scorer > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_first_scorer, reverse=True)

    def search_players_more_last_scorer_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_last_scorer > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_last_scorer, reverse=True)

    def search_players_more_home_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_home_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_home_goals, reverse=True)

    def search_players_more_away_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_away_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_away_goals, reverse=True)

    def search_players_more_right_foot_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_right_foot_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_right_foot_goals, reverse=True)

    def search_players_more_left_foot_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_left_foot_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_left_foot_goals, reverse=True)

    def search_players_more_head_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_head_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_head_goals, reverse=True)

    def search_players_more_penalty_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_penalty > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_penalty, reverse=True)

    def search_players_more_yellow_cards(self, cards):
        current_list = []

        for i in self.__chosen_list:
            if i.get_yellow_cards > cards:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_yellow_cards, reverse=True)

    def search_players_more_red_cards(self, cards):
        current_list = []

        for i in self.__chosen_list:
            if i.get_red_cards > cards:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_red_cards, reverse=True)

    def search_players_more_came_on(self, came_on):
        current_list = []

        for i in self.__chosen_list:
            if i.get_came_on > came_on:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_came_on, reverse=True)

    def search_players_more_taken_off(self, taken_off):
        current_list = []

        for i in self.__chosen_list:
            if i.get_taken_off > taken_off:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_taken_off, reverse=True)

    def search_players_more_first_and_second_half_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_first_half_goals > goals and i.get_second_half_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_goals, reverse=True)

    def search_players_more_home_and_away_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_home_goals > goals and i.get_away_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_goals, reverse=True)

    def search_players_more_right_and_left_foot_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_right_foot_goals > goals and i.get_left_foot_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_goals, reverse=True)

    def search_players_more_right_and_left_foot_and_head_goals(self, goals):
        current_list = []

        for i in self.__chosen_list:
            if i.get_right_foot_goals > goals and i.get_left_foot_goals > goals and i.get_head_goals > goals:
                current_list.append(i)

        return sorted(current_list, key=lambda player: player.get_goals, reverse=True)


# generowanie klas w celu wyszukiwania tylko po danych ligach

class PremierLeague(AppController):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("Premier League")


class Bundesliga(AppController):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("Bundesliga")


class LaLiga(AppController):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("La Liga")


class Ligue(AppController):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("Ligue 1")


class SerieA(AppController):
    def __init__(self, season):
        super().__init__(season)
        self._set_league("Serie A")


# generowanie klas w celu wyszukiwania tylko po danych pozycjach

class Forward(AppController):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Forward")


class Midfielder(AppController):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Midfielder")


class Defender(AppController):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Defender")


# generowanie klas w celu wyszukiwania tylko po danych pozycjach i ligach

class ForwardPL(PremierLeague):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Forward")


class MidfielderPL(PremierLeague):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Midfielder")


class DefenderPL(PremierLeague):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Defender")


class ForwardLL(LaLiga):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Forward")


class MidfielderLL(LaLiga):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Midfielder")


class DefenderLL(LaLiga):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Defender")


class ForwardSA(SerieA):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Forward")


class MidfielderSA(SerieA):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Midfielder")


class DefenderSA(SerieA):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Defender")


class ForwardBL(Bundesliga):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Forward")


class MidfielderBL(Bundesliga):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Midfielder")


class DefenderBL(Bundesliga):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Defender")


class ForwardL1(Ligue):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Forward")


class MidfielderL1(Ligue):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Midfielder")


class DefenderL1(Ligue):
    def __init__(self, season):
        super().__init__(season)
        self._set_position("Defender")

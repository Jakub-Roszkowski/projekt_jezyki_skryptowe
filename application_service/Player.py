class Player:
    def __init__(self, league, club, name, position, appearances, goals, came_on, taken_off, own_goals,
                 first_half_goals, second_half_goals, first_scorer, last_scorer, home_goals, away_goals,
                 right_foot_goals, left_foot_goals, head_goals, penalty, yellow_cards, red_cards):
        self.__league = league
        self.__club = club
        self.__name = name
        self.__position = position
        self.__appearances = appearances
        self.__goals = goals
        self.__came_on = came_on
        self.__taken_off = taken_off
        self.__own_goals = own_goals
        self.__first_half_goals = first_half_goals
        self.__second_half_goals = second_half_goals
        self.__first_scorer = first_scorer
        self.__last_scorer = last_scorer
        self.__home_goals = home_goals
        self.__away_goals = away_goals
        self.__right_foot_goals = right_foot_goals
        self.__left_foot_goals = left_foot_goals
        self.__head_goals = head_goals
        self.__penalty = penalty
        self.__yellow_cards = yellow_cards
        self.__red_cards = red_cards

    def __str__(self):
        return "Nazwa zawodnika: {0}\nNazwa klubu: {1}\nStrzelone bramki: {2}".format(self.__name, self.__club,
                                                                                      self.__goals)

    @property
    def get_league(self):
        return self.__league

    @property
    def get_club(self):
        return self.__club

    @property
    def get_name(self):
        return self.__name

    @property
    def get_position(self):
        return self.__position

    @property
    def get_appearances(self):
        return self.__appearances

    @property
    def get_goals(self):
        return self.__goals

    @property
    def get_came_on(self):
        return self.__came_on

    @property
    def get_taken_off(self):
        return self.__taken_off

    @property
    def get_own_goals(self):
        return self.__own_goals

    @property
    def get_first_half_goals(self):
        return self.__first_half_goals

    @property
    def get_second_half_goals(self):
        return self.__second_half_goals

    @property
    def get_first_scorer(self):
        return self.__first_scorer

    @property
    def get_last_scorer(self):
        return self.__last_scorer

    @property
    def get_home_goals(self):
        return self.__home_goals

    @property
    def get_away_goals(self):
        return self.__away_goals

    @property
    def get_right_foot_goals(self):
        return self.__right_foot_goals

    @property
    def get_left_foot_goals(self):
        return self.__left_foot_goals

    @property
    def get_head_goals(self):
        return self.__head_goals

    @property
    def get_penalty(self):
        return self.__penalty

    @property
    def get_yellow_cards(self):
        return self.__yellow_cards

    @property
    def get_red_cards(self):
        return self.__red_cards

import json


class Game:
    def __init__(self):
        with open('data.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_location_text(self, location):
        return self.data['locations'][location]['text']

    def get_location_options(self, location):
        return self.data['locations'][location]['options']

    def next_location(self, current_location, user_choice):
        new_location = current_location
        new_text = self.get_location_text(current_location)

        if current_location == "corridor":
            if user_choice == "Пойти на 3 этаж, 321 кабинет":
                new_location = "321_cabinet"
                new_text = self.get_location_text(new_location)
            elif user_choice == "Пойти на 2 этаж, 222 кабинет":
                new_location = "222_cabinet"
                new_text = self.get_location_text(new_location)
            elif user_choice == "Пойти домой":
                new_text = "Вам надоело учиться и вы решили пойти домой.Ой,какой злой отец важ ждет дома..Вы проиграли,но можете сыграть еще раз: /start"
                new_location = "game_over"  # Set a game-over location

        elif current_location == "321_cabinet":
            if user_choice == "Написать честно":
                new_text = "победа"
            elif user_choice == "Списать":
                new_text = "поражение."

        elif current_location == "222_cabinet":
            if user_choice == "Пойти на 3 этаж":
                new_text = "победа"
            elif user_choice == "Остаться чиллить":
                new_text = "поражение"

        return new_location, new_text

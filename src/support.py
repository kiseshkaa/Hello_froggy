import pygame as pg
import json


class Saver:
    purchased_suits = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
    dressed_suit = None

    @ staticmethod
    def save_coins(data: int):
        with open('data/coins.txt', 'w') as file:
            json.dump(data, file)

    @staticmethod
    def save_point(data: int):
        # Add data in records
        records = Saver.get_data('records')
        if data not in records and data != 0:
            if records:
                for index, record in enumerate(records):
                    if data > record:
                        records.insert(index, data)
                        break
                if data not in records:
                    records.append(data)
            else:
                records.append(data)

            if len(records) > 10:
                del records[-1]

        # Rewriting records
        with open('data/records.txt', 'w') as file:
            json.dump(records, file)

    @staticmethod
    def get_data(data_type=''):
        try:
            with open(f'data/{data_type}.txt') as file:
                return json.load(file)
        except FileNotFoundError:
            return None


def get_highest_cloud(screen: pg.Surface, clouds: pg.sprite.Group):
    highest_cloud = None
    max_height = screen.get_height()
    for cloud in clouds.sprites():
        if cloud.rect.y < max_height:
            max_height = cloud.rect.y
            highest_cloud = cloud

    return highest_cloud


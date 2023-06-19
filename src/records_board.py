import pygame as pg
from support import Saver
from inscription import Inscription

class RecordsBoard:
    def __init__(self):
        self.list = Saver.get_data('records')
        self.records = self.__get_inscriptions()
        self.border = pg.Rect(15, 100, 150, 400)
        self.vision = False

    def __get_inscriptions(self):
        records_inscriptions = []
        for index, data in enumerate(self.list):
            records_inscriptions.append(Inscription(str(data), 25, (80, 130 + 30 * index)))
        return records_inscriptions

    def refresh(self):
        self.list = Saver.get_data('records')
        self.records = self.__get_inscriptions()

    def update(self, surface):
        if self.vision:
            for data in self.records:
                data.update()
            pg.draw.rect(surface, 'seashell3', self.border, 5, 10)









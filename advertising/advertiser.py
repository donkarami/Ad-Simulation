from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    __total_clicks = 0

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

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

    @staticmethod
    def help():
        return "get_name() : returns name of Advertiser\n" + \
               "set_name() : sets name of Advertiser\n" + \
               "get_total_clicks() : returns total number of Clicks\n" + \
               "get_clicks() : returns number of clicks for current advertiser\n" + \
               "get_views() : returns number of views for current advertiser\n" + \
               "inc_clicks() : increases number of clicks\n" + \
               "inc_views() : increases number of views\n" + \
               "describe_me() : describes the duty of current class"

    @staticmethod
    def get_total_clicks():
        return Advertiser.__total_clicks

    def describe_me(self):
        return "this is a Advertiser class that manages Advertisers"

    def inc_clicks(self):
        super(Advertiser, self).inc_clicks()
        Advertiser.__total_clicks += 1

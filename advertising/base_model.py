class BaseAdvertising:

    def __init__(self, id=0):
        self._id = id
        self._clicks = 0
        self._views = 0

    def describe_me(self):
        return "this ia a Parent Of Ad and Advertiser class that handle methods and fields exist in both"

    @property
    def clicks(self):
        return self._clicks

    @property
    def views(self):
        return self._views

    def inc_clicks(self):
        self._clicks += 1

    def inc_views(self):
        self._views += 1

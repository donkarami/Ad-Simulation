from ad import Ad
from advertiser import Advertiser
from base_model import BaseAdvertising

if __name__ == '__main__':
    base_advertising = BaseAdvertising()
    advertiser_1 = Advertiser(1, "name1")
    advertiser_2 = Advertiser(2, "name2")
    ad_1 = Ad(1, "title1", "img-url1", "link1", advertiser_1)
    ad_2 = Ad(2, "title2", "img-url2", "link2", advertiser_2)

    print("describing of BaseAdvertising Class: " + base_advertising.describe_me())
    print("describing of Ad Class: " + ad_2.describe_me())
    print("describing of Advertiser Class: " + advertiser_1.describe_me())
    print("calling get_name() method for advertiser_2: " + advertiser_2.name)

    ad_1.inc_views()
    ad_1.inc_views()
    ad_1.inc_views()
    ad_1.inc_views()
    ad_2.inc_views()
    ad_1.inc_clicks()
    ad_1.inc_clicks()
    ad_2.inc_clicks()
    advertiser_2.name = "new name"

    print("calling get_name() method for advertiser_2:", advertiser_2.name)
    print("number of clicks for ad_1:", ad_1.clicks)
    print("number of clicks for advertiser_2:", advertiser_2.clicks)
    print("number of total clicks for all advertisers:", Advertiser.get_total_clicks())
    print("help method in Advertiser Class:\n" + Advertiser.help())

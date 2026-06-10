
from src.models.listing import Listing


def test_listing_stores_all_fields():
    listing = Listing(
        price=100000.0,
        area_m2=30.2,
        neighbourhood="Downtown",
        url="http://example.com/listing/1"
    )

    assert listing.price == 100000.0
    assert listing.area_m2 == 30.2
    assert listing.neighbourhood == "Downtown"
    assert listing.url == "http://example.com/listing/1"

def test_listing_accepts_none_area():
    listing = Listing(
        price=150000.0,
        area_m2=None,
        neighbourhood="Uptown",
        url="http://example.com/listing/2"
    )

    assert listing.price == 150000.0
    assert listing.area_m2 is None
    assert listing.neighbourhood == "Uptown"
    assert listing.url == "http://example.com/listing/2"
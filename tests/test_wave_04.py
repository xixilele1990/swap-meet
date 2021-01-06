import pytest
# The following lines will try to import Vendor, Item and Clothing.
# If they don't exist, then it will skip these tests.
Vendor = pytest.importorskip("swap_meet.vendor").Vendor
Item = pytest.importorskip("swap_meet.item").Item
Clothing = pytest.importorskip("swap_meet.clothing").Clothing
# The following lines will try to import Decor and Electronics.
# If they don't exist, then it will produce an error.
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_clothing_has_default_category_and_to_str():
    cloth = Clothing()
    assert cloth.category is "Clothing"
    assert str(cloth) == "The finest clothing you could wear."


def test_decor_has_default_category_and_to_str():
    decor = Decor()
    assert decor.category is "Decor"
    assert str(decor) == "Something to decorate your space."


def test_electronics_has_default_category_and_to_str():
    electronics = Electronics()
    assert electronics.category is "Electronics"
    assert str(electronics) == "A gadget full of buttons and secrets."


def test_items_have_condition_as_float():
    items = [
        Clothing(condition=3.5),
        Decor(condition=3.5),
        Electronics(condition=3.5)
    ]
    for item in items:
        assert item.condition == pytest.approx(3.5)



import pytest
from swap_meet.main import Vendor, Item, Clothing, Decor, Electronics

def test_vendor_has_inventory():
    vendor = Vendor()
    assert len(vendor.inventory) is 0

def test_vendor_takes_optional_inventory():
    inventory = ["a", "b", "c"]
    vendor = Vendor(inventory = inventory)
    assert len(vendor.inventory) is 3
    assert "a" in inventory
    assert "b" in inventory
    assert "c" in inventory

def test_adding_to_inventory():
    vendor = Vendor()
    item = "new item"

    result = vendor.add(item)

    assert len(vendor.inventory) is 1
    assert item in vendor.inventory
    assert result is item

def test_removing_from_inventory_returns_item():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c", item]
    )

    result = vendor.remove(item)

    assert len(vendor.inventory) is 3
    assert item not in vendor.inventory
    assert result is item


def test_removing_not_found_is_false():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c"]
    )

    result = vendor.remove(item)

    assert len(vendor.inventory) is 3
    assert result is False


def test_get_items_by_category():
    item_a = Item(category="clothing")
    item_b = Item(category="electronics")
    item_c = Item(category="clothing")
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("clothing")

    assert len(items) is 2
    assert item_a in items
    assert item_c in items
    assert item_b not in items


def test_get_no_matching_items_by_category():
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("electronics")

    assert len(items) is 0

def test_item_overrides_to_string():
    item = Item(category="electronics")

    stringified_item = str(item)

    # In Python, to check if 2 strings have the same value
    # we need to use ==, not is
    assert stringified_item == "Hello World!"

def test_swap_first_item_returns_true():
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) is 3
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_a in jolie.inventory
    assert result is True


def test_swap_first_item_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) is 0
    assert len(jolie.inventory) is 2
    assert result is False


def test_swap_first_item_from_their_empty_returns_false():
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    result = fatimah.swap_first_item(jolie)

    assert len(fatimah.inventory) is 3
    assert len(jolie.inventory) is 0
    assert result is False

def test_clothing_has_default_category():
    cloth = Clothing()

    # These two asserts are redundant, and typically
    # we would only need one of them
    # We're including both in order to give you
    # a hint about how to make it ;)
    assert cloth.category is "Clothing"
    assert cloth.category is Item.CLOTHING
    # Meta: is this cool?????? should this constant be in the child class??

def test_decor_has_default_category():
    decor = Decor()
    assert decor.category is "Decor"
    assert decor.category is Item.DECOR

def test_electronics_has_default_category():
    electronics = Electronics()
    assert electronics.category is "Electronics"
    assert electronics.category is Item.ELECTRONICS

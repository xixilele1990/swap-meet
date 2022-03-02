from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_integration_wave_04_05_06():
    me = Vendor()
    them = Vendor()

    item_clothing1 = Clothing(condition=1.0)
    item_clothing2 = Clothing(condition=2.0)
    item_electronics1 = Electronics(condition=1.0)
    item_electronics2 = Electronics(condition=2.0)
    item_decor1 = Decor(condition=1.0)
    item_decor2 = Decor(condition=2.0)

    me.add(item_clothing1)
    me.add(item_clothing2)
    me.add(item_electronics1)

    them.add(item_decor1)
    them.add(item_decor2)
    them.add(item_electronics2)

    # swap first item
    me.swap_first_item(them)
    
    assert len(me.inventory) == 3
    assert len(them.inventory) == 3

    assert item_clothing1
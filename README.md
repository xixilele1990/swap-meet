# Swap Meet

Entire concept: two users with an inventory should be able to swap items.

```
Messily written notes to communicate the classes and their members

vendor
	inventory
	add item
	remove from inventory
	find items with certain condition
	find items with certain categories
item
> clothing
> decor
> electronics
    category: str
    condition: float
    to_s
	<!-- optionals: description: str, relies on age
	age: int
        long_description(): based on condition and age -->
```


## Wave 1

- Create Vendor class
- Vendor has inventory: str[]
- implement add()
- implement remove()

## Wave 2

- Create Item class
- Item has category: str
- Implement: Vendor#get_by_category()
- If you did everything a certain way, you don't need to refactor add or remove

## Wave 3

- Overwrite Item's `__str__()` method
- Implement Vendor#swap_first_item(other_user)
	- Notes: uses add, remove

## Wave 4

- Create classes Clothing, Decor, Electronics, inherit from Item
    - Classes should hardcode their category
    - Also, overwrite `__str__()`
    - Also, condition: float

## Wave 5

- Implement Vendor#get_best_by_category()

## Wave 6

- Implement Vendor#swap_best_by_category

## Optionals

- Add age attribute to all Items
    - Implement Vendor#swap_by_newest
    - Implement Vendor#swap_by_newest

- Make a method for each Item subclass called long_description(). They follow different rules for each subclass:

Meta: these messages should be cute and distinctly "Clothing"/"Decor"/"Electronics" -- this is to anticipate "why don't we just use the same implementation" aka if all items had the same logic.

    - Clothing
        - if condition > 1.0, "Clothing is clothing"
        - else, "Worn out, possibly fashionable, possibly extreme"
    - Decor
        - if condition >= 4.0, "Very good condition"
        - if condition >= 3.0, "Pretty good condition"
        - if condition >= 2.0, "Noticeable wear and tear"
        - else, "Fashionably rustic"
    - Electronics
        - if condition >= 4.0, "Looks like it was just pulled out of the box for the first time!"
        - else, "Probably broken, but retro!"

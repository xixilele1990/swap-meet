# Swap Meet

## Skills Assessed

- Following directions and reading comprehension
- Reading tests
- Creating classes
  - Classes have attributes and instance methods
- Importing modules
- Working with attributes that are lists of instances
- Implementing instance methods that interact with other instances and objects
- Implementing inheritance
- Overriding methods from superclasses and Object

## Goal

You want to organize a swap meet! You have a bunch of _stuff_. So do your friends! It would be awesome if each person could swap one of their things with another person's things.

For this event, you want each person to register online as a vendor. Also, they should list an inventory list of things.

You envision an app where vendors can swap items between different inventories. But what would that backend logic look like?

For this project, given some features that the vendors want, create a set of classes, following the directions below. The directions will lead you to create many class definitions, their attributes and instance methods, and some other cool features. Vendors will be able to swap their top item and swap items by category!

## One-Time Project Setup

Follow these directions once, a the beginning of your project:

1. Navigate to your projects folder named `projects`

```bash
$ cd ~/Developer/projects
```

2. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `swap-meet`, and then puts the project into this new folder.

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

3. Move your location into this project folder

```bash
$ cd swap-meet
```

4. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

5. Activate this environment:

```bash
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

6. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```

Summary of one-time project setup:

- [ ] `cd` into your `projects` folder
- [ ] Clone the project onto your machine
- [ ] `cd` into the `viewing-party` folder
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependences with `pip`

## Project Development Workflow

1. When you want to begin work on this project, ensure that your virtual environment is activated:

```bash
$ source venv/bin/activate
```

2. Find the test file that contains the test you want to run.

   - Check the `tests` folder, and find the test file you want to run
   - In that test file, read through each test case

3. Run the tests for your specific wave

```bash
# Must be in activated virtual environment
$ pytest tests/test_wave_01.py
```

4. Focus on the top test failure. Read through the test failure, and understand why the failure is happening. Confirm your findings with a classmate.

5. Make a plan to fix the test failure.

6. Write code to fix the test failure.

7. Re-run the tests.

8. Repeat steps 5-7 until that test passes!

9. Repeats steps 4-8 until you have finished all tests in the file.

10. Begin using the test file of the next wave!

11. When you are finished working for the day, deactivate your environment with deactivate or closing the Terminal tab/window

```bash
$ deactivate
```

## Details About How to Run Tests

Run all tests that exist in this project with:

```bash
# Must be in activated virtual environment
$ pytest
```

If you want to run all tests that exist in one file, use:

```bash
# Must be in activated virtual environment
$ pytest tests/test_file_name.py
```

... where `test_file_name.py` is relpaced with the correct test file name.

If you want to see any `print` statements print to the console, add `-s` to the end of any `pytest` command:

```bash
# Must be in activated virtual environment
$ pytest -s
```

## Project Write-Up: How to Complete and Submit

The goal of this project is to write code in various files in the `swap_meet` directory so that as many of the tests pass as possible.

To complete this project, use the above workflow and follow these steps:

1. Start with making the tests in `test_wave_01.py` pass.
1. Review your code in the `swap_meet` directory and see if there are ways you can make the code more readable.
1. Then, work on making the tests in `test_wave_02.py` pass.
1. Review your code in the `swap_meet` directory
1. Repeat on all test files until submission time.

At submission time, no matter where you are, submit the project via Learn.

## Project Directions

This project is designed such that one could puzzle together how to implement this project without many directions.Being able to use tests to drive project completion is a skill that needs to be developed; programmers often take years to develop this skill competently.

When our test failures leave us confused and stuck, let's use the detailed project requirements below.

### Wave 1

The first two tests in wave 1 imply:

- There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
- Inside this module, there is a class named `Vendor`
- Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
- When we create initialize an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`

The remaining tests in wave 1 imply:

- Every instance of `Vendor` has an instance method named `add`, which takes in one item
- This method adds the item to the `inventory`
- This method returns the item that was added

- Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
- This method removes the matching item from the `inventory`
- This method returns the item that was removed
- If there is no matching item in the `inventory`, the method should return `False`

### Wave 2

The first tests in wave 2 imply:

- There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

- Inside this module, there is a class named `Item`
- Each `Item` will have an attribute named `category`, which is an empty string by default
- When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`
- Instances of `Vendor` have an instance method named `get_by_category`
  - It takes one argument: a string, representing a category
  - This method returns a list of `Item`s in the inventory with that category

### Wave 3

The first test in wave 3 implies:

- When we stringify an instance of `Item` using `str()`, it returns `"Hello World!"`
  - This implies `Item` overrides its stringify method

The remaining 5 tests in wave 3 imply:
- Instances of `Vendor` have an instance method named `swap_items`
  - It takes 3 arguments: 
      1. an instance of another `Vendor`, representing the friend that the vendor is swapping with
      2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
      3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
  - It removes the `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
  - It removes the `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
  - It returns `True`
  - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`

### Wave 4

The tests in wave 4 imply:
- Instances of `Vendor` have an instance method named `swap_first_item`
  - It takes one argument: an instance of another `Vendor`, representing the friend that the vendor is swapping with
  - This method considers the first item in the instance's `inventory`, and the first item in the friend's `inventory`
  - It removes the first item from its `inventory`, and adds the friend's first item
  - It removes the first item from the friend's `inventory`, and adds the instances first item
  - It returns `True`
  - If either itself or the friend have an empty `inventory`, the method returns `False`

### Wave 5

The tests in Wave 5 imply there are three new modules with three new classes:

- `Clothing`
  - Has an attribute `category` that is `"Clothing"`
  - Its stringify method returns `"The finest clothing you could wear."`
- `Decor`
  - Has an attribute `category` that is `"Decor"`
  - Its stringify method returns `"Something to decorate your space."`
- `Electronics`
  - Has an attribute `category` that is `"Electronics"`
  - Its stringify method returns `"A gadget full of buttons and secrets."`

- All three classes and the `Item` class have an attribute called `condition`, which can be optionally provided in the initializer. The default value should be `0`.

- All three classes and the `Item` class have an instance method named `condition_description`, which should describe the condition in words based on the value, assuming they all range from 0 to 5. These can be basic descriptions (eg. 'mint', 'heavily used') but feel free to have fun with these (e.g. 'You probably want a glove for this one..."). The one requirement is that the `condition_description` for all three classes above have the same behavior.

#### Using Inheritance

Now, we may notice that these four classes hold the same types of state and have the same behavior. That makes this is a great opportunity to use inheritance! If you haven't already, go back and implement the `Clothing`, `Decor`, and `Electronics` classes so that they inherit from the `Item` class. This should eliminate repetition in your code and greatly reduce the total number of lines code in your program!

Now the these three classes hold the same state and have the same behavior, this is a great opportunity to use inheritance! If you haven't already, go back and implement the `Clothing`, `Decor`, and `Electronics` classes so that they inherit from the `Item` class. This should eliminate repetition in your code and greatly reduce the total number of lines code in your program!
##### Hint: Importing Item

You'll need to refer to `Item` in order to declare it as a parent. To reference the `Item` class into these modules, try this import line:
If you need to import the `Item` class into these modules, try this import line:

```python
from swap_meet.item import Item
```

### Wave 6

The first three tests in wave 6 imply:

- `Vendor`s have a method named `get_best_by_category`, which will get the item with the best condition in a certain category
  - It takes one argument: a string that represents a category
  - This method looks through the instance's `inventory` for the item with the highest `condition` and matching `category`
    - It returns this item
    - If there are no items in the `inventory` that match the category, it returns `None`
    - It returns a single item even if there are duplicates (two or more of the same item with the same condition)

The last three tests in wave 5 imply:

- `Vendor`s have a method named `swap_best_by_category`, which will swap the best item of certain categories with another `Vendor`
  - It takes in three arguments
    - `other`, which represents another `Vendor` instance to trade with
    - `my_priority`, which represents a category that the `Vendor` wants to receive
    - `their_priority`, which represents a category that `other` wants to receive
  - The best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches `my_priority`
    - It returns `True`
    - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
    - If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`

### DRYing up the code

The further reduce the amount of repeated code in your project, consider how `swap_best_by_category` and `swap_first_item` might be able to make use of `swap_items`. Is there a way that these methods could incorporate a call to `swap_items` into the body of these methods?

Try it out and see if the tests still pass! If you can't get them to pass with this refactor, you can always return to the most recent working commit before you submit the project!

## Optional Enhancements

Should a project be completed before submission, and there is a desire for optional enhancements, consider this idea:

- Items have age
  - Add an `age` attribute to all Items
  - Implement a `Vendor` method named `swap_by_newest`, using any logic that seems appropriate

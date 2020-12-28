# Swap Meet

## Learning Goals

- we can make classes
- can make classes have instance methods and attributes
- an instance of a class can "use"/reference an instance of another class/same class
- an attribute can be an array of instances
    - we can do interesting things with this array of instances
- a class can override something from Object, because every class inherits from Object
- we can implement inheritance and use it
    - we can observe that ducktyping works!!
    - we can override things from that super class

## Goal

You want to organize a swap meet! You have a bunch of _stuff_. So do your friends! It would be awesome if each person could swap one of their things with another person's things.

For this event, you want each person to register online as a vendor. Also, they should list an inventory list of things.

You envision an app where vendors can swap items between different inventories. But what would that backend logic look like?

For this project, given some features that the vendors want, create a set of classes, following the directions below. The directions will lead you to create many class definitions, their attributes and instance methods, and some other cool features. Vendors will be able to swap their top item and swap items by category!

## One-Time Project Setup

Follow these directions once, a the beginning of your project:

1. Navigate to your projects folder named `projects`

```
$ cd ~/Developer/projects
```

2. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `swap-meet`, and then puts the project into this new folder.

```
$ git clone ...
```

Use `ls` to confirm there's a new project folder

3. Move your location into this project folder

```
$ cd swap-meet
```

4. Create a virtual environment named `venv` for this project:

```
$ python3 -m venv venv
```

5. Activate this environment:

```
$ source venv/bin/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

6. Install dependencies once at the beginning of this project with

```
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

```
$ source venv/bin/activate
```

2. Find the test file that contains the tests you want to run. Ensure that the tests in the file isn't skipped.

   - Check the `tests` folder, and find the test file you want to run
   - In that test file, read through each test case
   - Remove all lines that contain `@pytest.mark.skip()`

3. Run the tests!

```
$ python -m pytest
```

### !callout-info

## `python -m`?
Why is the command `python -m pytest`? The `python -m` command says "execute what's to the right, and include the current project." In general, the pytest package needs to be able to discover our tests and our source code. Therefore, `python -m pytest` runs the `pytest` command, and ensures that our tests and source code are discoverable.

### !end-callout

4. Focus on the top test failure. Read through the test failure, and understand why the failure is happening. Confirm your findings with a classmate.

5. Make a plan to fix the test failure.

6. Write code to fix the test failure.

7. Re-run the tests.

8. Repeat steps 5-7 until that test passes!

9. Repeats steps 4-8 until you have finished all tests in the file.

10. Begin using the test file of the next wave!

11. When you are finished working for the day, deactivate your environment with

```
$ deactivate
```

### !callout-secondary

## `$ deactivate` or Close Terminal
Alternatively, you could close this Terminal tab/window.

### !end-callout

## Details About How to Run Tests

Run all unskipped tests that exist in this project with:

```
python -m pytest
```

If you want to see any `print` statements print to the console, add `-s` to the end of any `pytest` command:

```
python -m pytest -s
```

If you want to run all unskipped tests that exist in one file, use:

```
$ python -m pytest tests/test_file_name.py
```

... where `test_file_name.py` is relpaced with the correct test file name.

## Project Write-Up: How to Complete and Submit

The goal of this project is to write code in `main.py` so that as many of the tests pass as possible.

To complete this project, use the above workflow and follow these steps:

1. Start with making the tests in `test_wave_01.py` pass.
1. Review your code in `main.py` and see if there are ways you can make the code more readable.
1. Then, work on making the tests in `test_wave_02.py` pass.
1. Review your code in `main.py`
1. Repeat on all test files until submission time.

At submission time, no matter where you are, submit the project via ...

## Project Directions

This project is designed such that one could puzzle together how to implement this project without many directions.Being able to use tests to drive project completion is a skill that needs to be developed; programmers often take years to develop this skill competently.

When our test failures leave us confused and stuck, let's use the detailed project requirements below.

### Wave 1

The first two tests in wave 1 imply:

- There is a class named `Vendor`
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

Entire concept: two users with an inventory should be able to swap items.

### Wave 2

The first tests in wave 2 imply:

- There is a class named `Item`
- Each `Item` will have an attribute named `category`, which is an empty string by default
- When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`
- Instances of `Vendor` have an instance method named `get_by_category`
    - It takes one argument: a string, representing a category
    - This method returns a list of `Item`s in the inventory with that category

### Wave 3

The first test in wave 3 implies:

- When we stringify an instance of `Item` using `str()`, it returns `"Hello World!"`
    - This implies `Item` overrides its stringify method

The remaining tests in wave 3 imply:

- Instances of `Vendor` have an instance method named `swap_first_item`
    - It takes one argument: an instance of another `Vendor`, representing the friend that the vendor is swapping with
    - This method considers the first item in the instance's `inventory`, and the first item in the friend's `inventory`
    - It removes the first item from its `inventory`, and adds the friend's first item
    - It removes the first item from the friend's `inventory`, and adds the instances first item
    - It returns `True`
    - If either itself or the friend have an empty `inventory`, the method returns `False`


### Wave 4

The tests in wave 4 imply there are three classes:

- `Clothing`
    - Has an attribute `category` that is `"Clothing"`
    - Its stringify method returns `"The finest clothing you could wear."`
- `Decor`
    - Has an attribute `category` that is `"Decor"`
    - Its stringify method returns `"Something to decorate your space."`
- `Electronics`
    - Has an attribute `category` that is `"Electronics"`
    - Its stringify method returns `"A gadget full of buttons and secrets."`

- All three classes have an optional keyword argument `condition`

### Wave 5

The first three tests in wave 5 imply:

- `Vendor`s have a method named `get_best_by_category`, which will get the item with the best condition in a certain category
    - It takes one argument: a string that represents a category
    - This method looks through the instance's `inventory` for the item with the highest `condition` and matching `category`
        - It returns this item
        - If there are no items in the `inventory` that match the category, it returns `None`
        - The logic is consistent even if there are duplicates

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


## Optional Enhancements

Should a project be completed before submission, and there is a desire for optional enhancements, consider these ideas:

- Items have Age
    - Add an `age` attribute to all Items
    - Implement a `Vendor` method named `swap_by_newest`, using any logic that seems appropriate

- Make a method for each `Item` called `long_description`. This method returns a long description of the item, based on the condition of the item. They follow different rules for each class:
    - Clothing
        - if condition greater than `1.0`, return "Clothing is clothing"
        - otherwise, return "Worn out, possibly fashionable, possibly extreme"
    - Decor
        - if condition greater than `4.0`, "Very good condition"
        - if condition is between `3.0` and `4.0`, "Pretty good condition"
        - if condition is between `2.0` and `3.0`, "Noticeable wear and tear"
        - otherwise, "Fashionably rustic"
    - Electronics
        - if condition is greater than `4.0`, "Looks like it was just pulled out of the box for the first time!"
        - otherwise, "Probably broken, but retro!"

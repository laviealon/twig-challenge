# Twig Coding Challenge #

---
Implementation of a function outlined in the Twig Coding Challenge spec,
which can be found in this project's directory (twig_coding_challenge.pdf).

## Installation ##

Clone this repo onto your machine, open with your favourite IDE,
and run ``main.py``. Ensure you have Python installed on your machine.

After navigating to the directory you want the project in, clone with

``$ git clone <URL>``

## Explanation ##

The function ``group_array_elements`` utilizes three helper
functions whose docstrings are included in the code, but a brief
elaboration is given in the solution section below.

### Problem ###

Write a function ``group_array_elements(array, n)`` which 
returns a list of ``n`` equally sized lists with elements
from ``array``. Where ``array`` cannot be divided equally,
the "final part should have length equal to the remainder" 
(instructions unclear - this was implemented to the
best of my understanding while keeping in line with the given
example given).

### Solution: High-Level Design ###

Distribute the elements of ``array``, one-by-one, 
into ``n`` empty lists, until all elements have been distributed.

Example (list size 8 into 5 arrays):

``[1, 2, 3, 4, 5, 6, 7, 8] --distribute-->
[[1, 6], [2, 7], [3, 8] ,[4] ,[5]]``

Then, after retrieving how many elements should be in each of the
lists (in this example: 2, 2, 2, 1, 1), rearrange the
elements to match ``array``'s order.

``[[1, 6], [2, 7], [3, 8] ,[4] ,[5]] --rearrange--> [[1, 2], [3, 4], [5, 6], [7], [8]]``

as desired.

### Solution: Low-Level Design ###

To achieve the specification laid out spec
in the high level solution design, ``array`` is
first converted to a ``queue.SimpleQueue`` with 
helper function ``create_queue_copy(array)``, avoiding
aliasing and mutability bugs by creating a copy
of ``array``. Then, a list containing ``n`` empty
lists is initialized. Next, the "distribution" step
is executed with helper function ``distribute_elements(q, empty_lsts)``, and the
"rearrange step" is executed with helper functions
``rearrange(array, lsts)``. 

Helper functions are not tested on runtime as the 
main function that uses them is tested on runtime.

### Annotations ###

All functions are annotated with standard ``typing``
annotations.

### DocTests ###
The function is tested with the ``doctest`` library - all
test cases are included in the function docstring and
are executed at runtime.

---

Copyright (c) Alon Lavie 2022

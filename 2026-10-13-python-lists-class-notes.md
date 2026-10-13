# Python Lists --- Class Notes

-   **Study date:** 2026-10-13
-   **Course:** Full Stack Development / Python Fundamentals
-   **Source:** `List _ Class Explanation.ipynb`
-   **Status:** Organized from the uploaded notebook; original examples
    are retained below.

## Learning objectives

-   Create a list and inspect its type and length.
-   Add items and store different data types in a list.
-   Copy, compare, clear, and delete lists.
-   Count items, extend lists, and find item positions.
-   Use positive and negative indexing and slicing.
-   Access characters within a string stored in a list.
-   Update an item by index.

> **Preservation note:** The code examples below are transcribed from
> the original notebook. Some cells depend on variables created in
> earlier cells, and a few intentionally/accidentally produce errors.
> Notes explaining these are marked separately rather than silently
> changing the original code.

## Quick concept summary

-   A **list** is an ordered, mutable collection written using square
    brackets, for example `numbers = [10, 20, 30]`.
-   `append(item)` adds one item to the end of a list.
-   `len(list_name)` returns the number of top-level items.
-   `copy()` creates a shallow copy; the copied list is a different list
    object.
-   `clear()` removes all items from a list.
-   `count(value)` counts matching items.
-   `extend(iterable)` adds each item from an iterable.
-   `index(value)` returns the position of the first matching item.
-   Slicing uses `list[start:stop:step]`; the stop position is excluded.
-   Negative indexes count from the end; `-1` is the last item.
-   Lists are mutable, so an item can be replaced using
    `list_name[index] = new_value`.

`\n`{=tex}\## 1. Creating and inspecting lists`\n`{=tex}`\n`{=tex}\###
Original notebook cell
1`\n`{=tex}`\n`{=tex}`python\nl = [] #empty list l\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
2`\n`{=tex}`\n`{=tex}`python\ntype(l)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
3`\n`{=tex}`\n`{=tex}`python\nlen(l)\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
4`\n`{=tex}`\n`{=tex}`python\nl.append(10) l\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
5`\n`{=tex}`\n`{=tex}`python\nlen(l)\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
6`\n`{=tex}`\n`{=tex}`python\nl.append(20, 30, 40)\n``\n`{=tex}`\n*`{=tex}\*Important
note:\*\* This original line, `l.append(20, 30, 40)`, raises a
`TypeError` because `append()` accepts one item. The notebook later
demonstrates adding values with separate `append()` calls in cell 8. The
original line is kept unchanged above.`\n`{=tex}`\n`{=tex}\### Original
notebook cell 7`\n`{=tex}`\n`{=tex}`python\nl\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
8`\n`{=tex}`\n`{=tex}`python\nl.append(20) l.append(30) l.append(40) l.append(50) l\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
9`\n`{=tex}`\n`{=tex}`python\nlen(l)\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
10`\n`{=tex}`\n`{=tex}`python\nl\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
11`\n`{=tex}`\n`{=tex}`python\nl.append(10)  l\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\##
2. Lists can contain different data types and nested
lists`\n`{=tex}`\n`{=tex}\### Original notebook cell
12`\n`{=tex}`\n`{=tex}`python\nl1 = [10, 3.5, True, 1+2j, 'welcome']  l1\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
13`\n`{=tex}`\n`{=tex}`python\nl1.append([1,2,3]) # nested list  l1\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
14`\n`{=tex}`\n`{=tex}`python\nprint(l) print(l1)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
15`\n`{=tex}`\n`{=tex}`python\nl\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\## 3.
Copying a list and comparing lists`\n`{=tex}`\n`{=tex}\### Original
notebook cell
16`\n`{=tex}`\n`{=tex}`python\nl3\n``\n`{=tex}`\n*`{=tex}\*Important
note:\*\* `l3` is referenced before it is assigned in the shown notebook
sequence. If run from a fresh kernel at this point, this cell raises
`NameError`; cell 17 creates `l3` using
`l.copy()`.`\n`{=tex}`\n`{=tex}\### Original notebook cell
17`\n`{=tex}`\n`{=tex}`python\nl3 = l.copy() l3\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
18`\n`{=tex}`\n`{=tex}`python\nprint(l) print(l1) print(l3)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
19`\n`{=tex}`\n`{=tex}`python\nl == l3\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
20`\n`{=tex}`\n`{=tex}`python\nlen(l) == len(l3)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
21`\n`{=tex}`\n`{=tex}`python\nid(l) == id(l3)\n``\n`{=tex}`\n*`{=tex}\*Concept:\*\*
Two lists may contain equal values while being different objects. The
comparison using `id()` checks object identity.`\n`{=tex}`\n`{=tex}\###
Original notebook cell
22`\n`{=tex}`\n`{=tex}`python\nid(l) != id(l3)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
23`\n`{=tex}`\n`{=tex}`python\nprint(id(l)) print(id(l3))\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
24`\n`{=tex}`\n`{=tex}`python\nprint(l) print(l1) print(l3)\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\##
4. Clearing and deleting a list`\n`{=tex}`\n`{=tex}\### Original
notebook cell
25`\n`{=tex}`\n`{=tex}`python\nl3.clear()\n``\n`{=tex}`\n*`{=tex}\*Concept:\*\*
`clear()` empties the list object; it does not merely hide the
contents.`\n`{=tex}`\n`{=tex}\### Original notebook cell
26`\n`{=tex}`\n`{=tex}`python\nprint(l) print(l1) print(l3)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
27`\n`{=tex}`\n`{=tex}`python\ndel l3\n``\n`{=tex}`\n*`{=tex}\*Concept:\*\*
`del l3` removes the variable binding. The next cell that evaluates `l3`
will raise `NameError`.`\n`{=tex}`\n`{=tex}\### Original notebook cell
28`\n`{=tex}`\n`{=tex}`python\nl3\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
29`\n`{=tex}`\n`{=tex}`python\nprint(l) print(l1)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
30`\n`{=tex}`\n`{=tex}`python\nl\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\## 5.
Counting and extending list elements`\n`{=tex}`\n`{=tex}\### Original
notebook cell
31`\n`{=tex}`\n`{=tex}`python\nl.count(30)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
32`\n`{=tex}`\n`{=tex}`python\nl.count(10)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
33`\n`{=tex}`\n`{=tex}`python\nl\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
34`\n`{=tex}`\n`{=tex}`python\nprint(l) print(l1)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
35`\n`{=tex}`\n`{=tex}`python\nl.extend(l1)  l\n``\n`{=tex}`\n*`{=tex}\*Concept:\*\*
`extend(l1)` adds the items from `l1` individually to `l`; a nested list
already inside `l1` remains one item within `l1` when extended at this
level.`\n`{=tex}`\n`{=tex}\### Original notebook cell
36`\n`{=tex}`\n`{=tex}`python\nprint(len(l)) print(len(l1))\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
37`\n`{=tex}`\n`{=tex}`python\na1 = [1,2,3] b1 = [4,5,6]\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
38`\n`{=tex}`\n`{=tex}`python\na1.extend(b1) a1\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
39`\n`{=tex}`\n`{=tex}`python\nprint(a1) print(b1)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
40`\n`{=tex}`\n`{=tex}`python\nprint(l) print(l1)\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\##
6. Finding element positions with index()`\n`{=tex}`\n`{=tex}\###
Original notebook cell
41`\n`{=tex}`\n`{=tex}`python\nl.index(20)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
42`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
43`\n`{=tex}`\n`{=tex}`python\nl1.index(1+2j)\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
44`\n`{=tex}`\n`{=tex}`python\nl1.index('welcome')\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
45`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\## 7.
List indexing and slicing`\n`{=tex}`\n`{=tex}\### Original notebook cell
46`\n`{=tex}`\n`{=tex}`python\nl1[:]\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
47`\n`{=tex}`\n`{=tex}`python\nl1[5]\n``\n`{=tex}`\n*`{=tex}\*Note:\*\*
At this point, `l1` contains six top-level items because cell 13
appended a nested list. Therefore `l1[5]` accesses that nested
list.`\n`{=tex}`\n`{=tex}\### Original notebook cell
48`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
49`\n`{=tex}`\n`{=tex}`python\nl1[4]\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
50`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
51`\n`{=tex}`\n`{=tex}`python\nl1[:3]\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
52`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
53`\n`{=tex}`\n`{=tex}`python\nl1[3:]\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
54`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
55`\n`{=tex}`\n`{=tex}`python\nl1[0:5:2]\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
56`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
57`\n`{=tex}`\n`{=tex}`python\nl1[-3]\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
58`\n`{=tex}`\n`{=tex}`python\nl1[-3:]\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
59`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
60`\n`{=tex}`\n`{=tex}`python\nl1[::-1]\n``\n`{=tex}`\n*`{=tex}\*Concept:\*\*
`[::-1]` returns a reversed slice as a new list; it does not reverse
`l1` in place.`\n`{=tex}`\n`{=tex}\### Original notebook cell
61`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
62`\n`{=tex}`\n`{=tex}`python\nl1[::-2]\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
63`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\### Original
notebook cell
64`\n`{=tex}`\n`{=tex}`python\nl1[4]\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\##
8. Accessing characters inside a string stored in a
list`\n`{=tex}`\n`{=tex}\### Original notebook cell
65`\n`{=tex}`\n`{=tex}`python\nprint(l1[4][0]) print(l1[4][1]) print(l1[4][2]) print(l1[4][3]) print(l1[4][4]) print(l1[4][5]) print(l1[4][6]) print(l1[4][7])\n``\n`{=tex}`\n*`{=tex}\*Concept:\*\*
`l1[4]` is the string `'welcome'` in this sequence. Indexing it from `0`
through `6` prints its characters. The final access at index `7` is out
of range for this seven-character string and raises `IndexError`. This
original line is retained.`\n`{=tex}`\n`{=tex}\### Original notebook
cell 66`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}\###
Original notebook cell
67`\n`{=tex}`\n`{=tex}`python\nl1[0]\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\##
9. Updating an item in a list`\n`{=tex}`\n`{=tex}\### Original notebook
cell
68`\n`{=tex}`\n`{=tex}`python\nl1[0] = 100\n``\n`{=tex}`\n*`{=tex}\*Concept:\*\*
This assigns `100` to the first item of `l1`. The change is visible when
cell 69 displays the list.`\n`{=tex}`\n`{=tex}\### Original notebook
cell
69`\n`{=tex}`\n`{=tex}`python\nl1\n``\n`{=tex}`\n`{=tex}`\n`{=tex}\##
10. Incomplete expression from the original
notebook`\n`{=tex}`\n`{=tex}\### Original notebook cell
70`\n`{=tex}`\n`{=tex}`python\nl1.\n``\n`{=tex}`\n*`{=tex}\*Note:\*\*
`l1.` is an incomplete Python expression and raises `SyntaxError` if
executed as shown. It is preserved exactly from the
notebook.`\n`{=tex}`\n`{=tex} \## Practice checklist

-   [ ] Create an empty list and check its type and length.
-   [ ] Add several items using `append()`.
-   [ ] Create a list containing different data types.
-   [ ] Copy a list and compare equality versus object identity.
-   [ ] Try `clear()`, `count()`, `extend()`, and `index()`.
-   [ ] Practice positive indexing, negative indexing, and slicing.
-   [ ] Update an item using its index.

## Original file

Keep the original `List _ Class Explanation.ipynb` alongside this
Markdown note in the repository. This Markdown file is an organized
companion, not a replacement for the notebook.

# ConwaysGameOfLife
A Graphical Representation of Conway's Game of Life using Numpy


Lab Journal

1 October 25

Author: Ritika Roy | Time Spent: ~1 hour

Completed:

Brainstormed and implemented the Third Idea
THIRD IDEA
Cells of neighbors stored in a single list, iterations through the list
Counting of the neighbors without interference
Benefits: efficient solution to remove and add live cells
Drawbacks
- Current bug: incorrectly marking cells as live without removal of overpopulated cells
Future Goals:

Date of Implementation: TBD
Created a numpy implementation of graphical output to replace console
Fix current bug with removal of the overpopulated cells
29 September 25

Author: Ritika Roy | Time Spent: ~2 hour

Completed:

Created a paper pseudocode for Conways Game of Life

implemented an initial consol drawing method

Figured out initial logic of counting neighbors

brainstormed and experimented with different methods to count enightsboard

FIRST IDEA:

Nested ireation to count each square and then its neighbors
Benefits: Simple implementation
Drawbacks: Computational slow process, inefficient, results in double-counting
SECOND IDEA:

Two separate functions to implement the rules
@addneighbors function uses spatial relations of live cells to create new live cells
@removeneighbors function uses similar method as add nieghbors for opposite process
Benefits: makes a more readable and logical code oder
Drawbacks: has error of orioritizing either adding or removing cells,
cannot perform both processes cleanly without interferences
Future Goals:

Date of Implementation: 1 October 2025
Continue Implementation of Secon Idea
Consider better implementation of COnway/s Game
Rebrainstorm problem and rework implementation of methods for efficiency
24 September 25

Author: Ritika Roy | Time Spent: ~0.5 hour

Completed:
Initial On-boarding meeting with Steve to discuss this weeks actions and goals
Read Ant nest geometry, stability, and excavation–inspiration for tunneling
Installed uv and Ruff to system
Set up gitHub Repo for Conway's Game of Life: https://github.com/RitikaRoy72/ConwaysGameOfLife
Future Goals:
Date of Implementation: 26 September 2025
Create Pseudocode of Conway's Game of Life
Create structural basis of Code
Start Graphic Implementation

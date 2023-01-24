# Feeding the Rabbit Game<br />
# 1 How to Play<br />
  In this game, the rabbit which is
placed in a board will move according to the commands and collect points
according to the food it eats. The user plays the game by moving the the
rabbit denoted by \* to horizontally or vertically adjacent cells. The
user earns/lose points if he/she move the rabbit to a cell that contains
Carrot (C), Apple (A) or Meat (M). The game is over and the rabbit
cannot move any more if user can move the rabbit to a cell that contains
Poison (P). The board may contain Walls (W). The rabbit cannot break the
wall, and if the rabbit is in the cell next to the wall, it remains in
the cell where it is, even if commanded to move towards the wall. The
user moves the rabbit (*) by giving directions to the computer about
which direction it is to be moved. There are four allowed moves: Right
(R), Left (L), Up (U), and Down (D). The rabbit can move one cell at a
time. If the cell that the rabbit is trying to move is already occupied,
i.e., if there is another character there, the rabbit replaces those
character with the * character. Moreover, the rabbit can't get out of
the board or move into walls. For example, if the rabbit is on the far
left and is asked to move to the left, he will not move to left any
more. This situation is the same for all directions. In this game, the
user will determine the size of the map such as 4x8, 5x4, 6x6 or so on,
manually enter the elements into the cells and manually enter directions
of movements as a list as exemplified in Section 2. Some rules are
listed for scoring as follow:<br />
• Rabbit earns 10 points if rabbit eats
carrot<br />
• Rabbit earns 5 points if rabbit eats apple <br />
• Rabbit loses 5 points if rabbit eats meats <br />
• Rabbit dies if rabbit eats poison.<br />
Example board:<br /> 
X W X C X <br />
A W X A X <br />
C X X W P <br />
W X X X X <br />
X \* X W X <br />
Symbols on the board and their meanings, *=Rabbit, C=Carrot, A=Apple, P=Poison, M=Meat,
W=Wall and X=Empty 

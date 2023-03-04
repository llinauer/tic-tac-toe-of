# tic-tac-toe-of

After finishing my reinforcement learning based Tic Tac Toe agent (https://github.com/llinauer/tic-tac-toe-rl), I was 
really proud. I thought, how cool that you can train an AI to play the game perfectly
with a mere 200 thousand rounds of training!

Some time later I read the book One Jump Ahead by Jonathan Schaeffer. In this book, Dr. Schaeffer
describes in great detail the development of his checkers playing program CHINOOK, but it also touches
some more general topics about game playing AI. The book is awesome by the way, and I would greatly recommend
anybody interested in such tings to read it.
Anyway, in one chapter, he does a comparison between machine learning and knowledge-based 
approaches and mentions there that learning everything from scratch, even if the knowledge is 
readily available, is at best, cumbersome.

Tic Tac Toe for example, is widely (universally?) known and everybody knows how to play.
Even after only some games, people know how to react in certain situations and probably many of them
develop a strategy to play perfectly.
A quick look on wikipedia confirms: 8 rules is all you need to be unbeatable.
8 rules vs. 200 thousand games! 

That really showed me how a little knowledge can go a long way in AI systems and that's also
why I wanted to create a good old-fashioned Tic Tac Toe program.
This is what this repository is about.


# Pre-requisites

This project is derived from https://github.com/llinauer/tic-tac-toe-rl and uses python3 with numpy.


# The rules

Let me state the rules for perfect play in Tic Tac Toe explicitly here:

The first rule of Tic Tac Toe is: you do not ... (jk)

### 1. Play to win

If you have two in a row, complete it to win. Easy enough.

<p float="left">
  <img src=https://user-images.githubusercontent.com/85884720/222914232-1cc5daaa-a183-4fe3-988c-a7291939e59a.png width=300>
   &nbsp; &nbsp; 
  <img src=https://user-images.githubusercontent.com/85884720/222914244-8f9b91ee-e992-4763-a9b1-7f832d870795.png width=300>
</p>


### 2. Block

If the opponent has two in a row, block it to avert a loss. Also a no-brainer.

<p float="left">
    <img src=https://user-images.githubusercontent.com/85884720/222914252-b7dd37a1-36e1-45d6-b665-7e194047bb1b.png width=300>
     &nbsp; &nbsp; 
    <img src=https://user-images.githubusercontent.com/85884720/222914253-f6fed1db-d07d-4af9-a30b-70c0d0e00dfe.png width=300>
</p>


### 3. Fork

Place your symbol, so that you open up two winning lanes.
In the example here, X plays the lower left corner and now has two rows with
two symbols. O can only block one of them and will loose the turn after.

<p float="left">
    <img src=https://user-images.githubusercontent.com/85884720/222914262-29b263a3-0c97-4ceb-abad-c38540a3d20d.png width=300>
    &nbsp; &nbsp; 
    <img src=https://user-images.githubusercontent.com/85884720/222914270-4fc1fd54-ac46-4b2f-9882-05bce57353cb.png width=300>
</p>


### 4. Block a fork

If your opponent can fork, prevent it. In the example here, X can open a fork by placing
in the lower left corner. O knows this and can block. In this situation, it would be equally
good for O to place in the middle and threaten with a win.

<p float="left">
    <img src=https://user-images.githubusercontent.com/85884720/222914277-2270d3c5-b282-49be-b6b5-12db200c465e.png width=300>
     &nbsp; &nbsp; 
    <img src=https://user-images.githubusercontent.com/85884720/222914280-aeb3600d-44d5-41ef-ac26-2c502c94a566.png width=300>
    &nbsp; &nbsp; 
    <img src=https://user-images.githubusercontent.com/85884720/222914289-7b080f59-67de-49d3-a819-e010cce824a0.png width=300>
</p>

### 5. Center

If free, place in the center. However, if it is the first round, you can increase your opponents
chance of loosing, by placing in the corner. So that's probably a good thing to do.

### 6. Opposite corner

When your opponent plays a corner, go for the opposite corner.

<p float="left">
   <img src=https://user-images.githubusercontent.com/85884720/222914296-70ad1e8c-d8fb-409c-96b6-903b72108061.png width=300>
   &nbsp; &nbsp; 
  <img src=https://user-images.githubusercontent.com/85884720/222914298-05dfdb44-0224-44f5-8abb-621a81ba414f.png width=300>
</p>

### 7. Empty corner

If a corner is empty, place there. 

<p float="left">
  <img src=https://user-images.githubusercontent.com/85884720/222914301-5260a377-38de-44dc-9953-49a9c5f777e8.png width=300>
   &nbsp; &nbsp; 
  <img src=https://user-images.githubusercontent.com/85884720/222914311-3e1b8e87-8218-4b92-9393-af0aabee8c72.png width=300>
</p>

### 8. Empty side

Play the middle square on any of the four side. This rule really only applies in the last move, when you
are forced to draw.

<p float="left">
  <img src=https://user-images.githubusercontent.com/85884720/222914322-bf9d2134-0ebb-4495-b7f0-820e5f636c74.png width=300>
   &nbsp; &nbsp; 
  <img src=https://user-images.githubusercontent.com/85884720/222914328-7f23b031-d0bc-4ed3-8b62-3b37a3eddee9.png width=300>
</p>


# Playing

To play, run the tic_tac_toe.py script via:

    python tic_tac_toe.py -s {x, o}

You can choose which side you wann play with the -s argument.

Enjoy.

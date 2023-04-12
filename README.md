# 2048 AI
> Monte Carlo Tree Search Algorithm used to solve 2048 puzzles.

This Artificial Intelligence algorithm (Monte Carlo Tree Search) attempts to maximize the amount of score gained while also attempting to minimize the number of moves used.

## Visualization
It can be visualised as a tree that displays the current situation as the root node and then roots down across many paths and chooses a valid path that maximizes score (reaching a leaf node) in the shortest amount of moves.<br>
![image](https://user-images.githubusercontent.com/47650058/231334933-192f364e-1c94-4ae9-b0ab-e27d27fdb32b.png)

## Installation and Usage
- Make sure to have Python 3.9 installed on your local system. <br><br>
- Install the required python packages for the project to work (pygame and numpy).<br>
  ```console
  $ pip install requirements.txt
  ```

- Run the <b>game.py</b> script by executing this command in a terminal
  ```console
  $ python3 game.py
  ```

## Results
To my surprise, this algorithm doesn't just beat 2048, it actually demolishes it in every way possible. Just in my 4th attempt, I was able to reach upto ~170k scores. This algorithm has beaten most other 2048 artificial intelligence algorithms that I have seen out there and its potential scares me.

![image](https://user-images.githubusercontent.com/47650058/231336466-a03245e0-f285-4989-84e5-e1a45e95ac96.png)
![image](https://user-images.githubusercontent.com/47650058/231336334-9ca96167-f1be-4e68-ba7e-8d7dc64545ad.png)

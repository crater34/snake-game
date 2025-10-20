# snake-game
the snake game but with a  twist that adds power ups to the game made with python using the pygame library.

Welcome to Snake Game: Power-Up Edition!
This is a fun twist on the classic Snake game — where eating apples makes you grow, but power-ups can give you crazy boosts like double points or super speed.

Built using Python and Pygame.
Features

Classic snake gameplay — grow by eating apples 

Randomly spawning power-ups that change how you play

 Speed boost: Move faster and react quicker

 Double score: Each apple gives twice the points

Background music 

Fun "You Lost" animation when the game ends 

Pause and resume using P
How to Play

Run the game (python main.py).

Use the arrow keys to move:

⬆️ Up

⬇️ Down

⬅️ Left

➡️ Right

Collect apples to grow your snake and earn points.
Setup
Requirements

Python 3.x

Pygame

Pillow (for handling GIFs)
installations
pip install pygame pillow

Then make sure all the game images and sound files are in the same folder:
apple.png
crate.png
head_up.png
head_down.png
head_left.png
head_right.png
body_horizontal.png
body_vertical.png
music.mp3
Sad Spider Man GIF.gif
run:

python main.py
Power-Up System
⚡ Speed	Doubles your movement speed	10 seconds
💰 Double	Apples give double points	10 seconds

File Structure
snake_game/
│
├── main.py          # Main game loop

├── snake.py         # Snake class and logic

├── app_obj.py       # Apple and Power-up classes

├── music.mp3        # Background music

├── *.png            # Game sprite

└── Sad Spider Man GIF.gif  # Game over animation


Controls
Key	Action
↑ ↓ ← →	Move the snake
P	Pause/Resume
ESC / Close window	Quit the game


Don’t crash into walls or yourself — that’s game over!

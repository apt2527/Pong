🏓 Pong Game (Python Turtle)

A classic Pong game built using Python Turtle graphics, featuring:

Two-player controls

Sound effects

Score tracking

Randomized ball bounce for realistic gameplay

📌 Features

🎮 Player A vs Player B

🔊 Sound effects on wall hit and paddle hit

🎯 Scoreboard at the top

🔄 Random ball angle after paddle collision

🖥️ Runs on Windows (uses winsound)

🕹️ Controls
Player	Move Up	Move Down
Player A	W	S
Player B	↑ Up Arrow	↓ Down Arrow
📂 Project Structure
Pong/
│
├── pong.py
├── README.md
└── ASSETS/
    ├── WALL.wav
    └── HIT.wav


⚠️ Important:
Make sure the ASSETS folder is in the same directory as pong.py.

🛠️ Requirements

Python 3.x

Windows OS (for winsound)

No external libraries needed

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/pong-game.git


Navigate into the project folder:

cd pong-game


Run the game:

python pong.py

🧠 How It Works (Brief)

Ball movement is controlled using dx and dy

Paddle collision reverses ball direction

random.choice() changes the ball angle on every hit

Scores update when the ball crosses boundaries

🚀 Future Improvements

🤖 AI opponent

🧠 Difficulty levels

⏸️ Pause / Resume option

🏆 Winning screen

👨‍💻 Author

Arpit Abhinav Chauhan

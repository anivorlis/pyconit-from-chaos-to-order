# Goal: Run the scripts that our colleague gave us

Tools: uv and git
Dependencies: numpy and matplotlib


### Exercise

Step 0: 
- `uv init --python=3.13`

Step 1:
- `uv run -m ex01.e01`

Step 2:
- add to `e02.py`: `from ex01.e01 import roll_dice`
- `uv add numpy`
- `uv run -m ex01.e02`

Step 3:
- add to `e03.py`: `from ex01.e02 import dice_simulation, dice_statistics`
- `uv add matplotlib`
- `uv run -m ex01.e03`

Step 4:
- write a new module: `ex01/e04.py`
- use a seed for consistent values
- `uv run -m ex01.e04`

### Success criteria
- We can roll the dice N times and have consistent results!

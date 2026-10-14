# Lights Out

A desktop puzzle built with **Python** and **CustomTkinter**. A 5×5 grid of lights starts on. Turn every light off.

## How to play

Click a light. That light switches, and so do the lights directly above, below, left, and right. Corners and edges have fewer neighbors.

A light that is on turns off. A light that is off turns on. The board is clear when every light is off.

**All on** puts every light back on. **Scrambled** builds a mixed board that can be solved.

## Download (Windows)

You do not need Python to play.

1. Go to **[Releases](https://github.com/xStylez/Lights-Out/releases)**
2. Open the latest release (for example **v1.0.0**)
3. Download **`dist.zip`**
4. Unzip the folder
5. Double-click **`LightsOut.exe`**

Windows may warn about an unknown publisher. Choose **More info**, then **Run anyway**, if you trust the build.

## Run from source

Use this if you want to change the code.

- Python 3.10+
- CustomTkinter

```bash
pip install customtkinter
python main.py
```

## Project structure

```text
LightsOut/
├── main.py      # Window, board, clicks, win check
└── README.md
```

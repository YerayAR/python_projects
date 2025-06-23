# Python Projects Collection

This repository hosts a variety of small Python applications. Each project lives in its own folder and can be run independently.

## Projects Overview

| Folder | Description | Main dependencies | How to Run |
|-------|-------------|------------------|-----------|
| [`calc/`](calc/) | Graphical calculator with an animated GIF background. | `tkinter`, `Pillow` | `python calculadora.py` |
| [`hangman/`](hangman/) | Console version of the hangman word game in Spanish. | Standard library | `python el_ahorcado.py` |
| [`pong/`](pong/) | Pong clone using Tkinter with basic AI opponent. | `tkinter` | `python pong.py` |
| [`visual_sort/`](visual_sort/) | Sorting algorithm visualiser with audio feedback. | `tkinter`, `matplotlib`, `pygame` | `python ordenacion_visual.py` |
| [`text_to_emoji/`](text_to_emoji/) | Converts English phrases to emojis from a JSON dictionary. | `tkinter` | `python text_to_emoji.py` |
| [`password_genNsave/`](password_genNsave/) | GUI to generate passwords and store them in a CSV file. | `tkinter` | `python passw_genNsave.py` |
| [`XtractAudioFromVideo/`](XtractAudioFromVideo/) | Batch extractor that saves audio tracks from videos. | `moviepy` | `python xtract.py` |

Refer to each subfolder's README for detailed instructions, screenshots and future enhancements.

## Requirements

- Python 3.7 or newer
- Project specific dependencies as listed above

A virtual environment is recommended to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt  # if provided
```

## Usage

Navigate to the desired project directory and run the indicated script. Example for the calculator:

```bash
cd calc
python calculadora.py
```

Some projects rely on additional media files such as GIFs or audio clips. Adjust the file paths in the code if necessary.

Happy coding!

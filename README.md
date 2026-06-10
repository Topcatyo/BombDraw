# BombDraw
An application that generates ideas for things to draw.

Ver 1
BombDraw is technically a fully-functioning applet that works in Python if you have all of the random things that are required to make it run.

THE NEXT STEPS:
- Obviously tuning the lists and probabilities ensure more consistently decent prompts.
- BIG ONE!!!: UPGRADE to VERSION 2!
  - Version 2 will be coded in GoLang so that it will be a more portable file that folks can use (I assume that's how it works).
  - Hopefully it will also, visually, function more like a proper spinner instead of just cycling quickly through entries.
  - Ideally, also, it will include sound.


# BombDraw! — Run & Troubleshoot Guide ✅

A short checklist to get the app running locally and recover if something goes wrong.

## Quick start (the easiest path) 🚀
1. Open a terminal in the project folder (`${workspaceFolder}`).
2. Activate the existing venv (if present):

```bash
source .venv/bin/activate
```

3. Run the app:

```bash
python main.py
```

4. Click **Roll** to generate prompts. If you hear no sounds, that's OK — the app will still run.

---

## Requirements
- `simpleaudio==1.0.4`

## Create a fresh venv (recommended) 🔧
If you prefer a clean environment or the project doesn't have a usable venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install simpleaudio
```

Then run:

```bash
python main.py
```

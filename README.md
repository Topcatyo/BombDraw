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

---

## System packages you may need (Debian/Ubuntu) 🧩
- To create venvs: `sudo apt install python3-venv` (or `python3.12-venv` on some distros)
- For GUI/Tkinter: `sudo apt install python3-tk`
- For building `simpleaudio` C extension: `sudo apt install build-essential libasound2-dev python3-dev`

These commands require sudo.

---

## If pip refuses to install (PEP 668 / "externally managed") ⚠️
- Preferred: create a venv (see above) and install packages inside it.
- If you cannot create a venv, consider using `pipx` or `conda` to isolate packages.
- As a last resort, pip will show how to override with `--break-system-packages` (not recommended).

---

## Why `simpleaudio` might fail to build 🛠️
If `pip install simpleaudio` fails during compilation, the most common cause is missing ALSA dev headers (`alsa/asoundlib.h`). Fix it with:

```bash
sudo apt install libasound2-dev build-essential python3-dev
```

Alternatively, use conda which provides prebuilt packages:

```bash
conda create -n draw python=3.12
conda activate draw
conda install -c conda-forge simpleaudio
```

---

## Notes about sounds and graceful fallback 🎧
- The app uses `simpleaudio` to play .wav feedback but will still run without it.
- If `simpleaudio` is missing, the program prints a warning like:

```
Warning: simpleaudio is not installed; sounds will be disabled.
```

- Missing `tkinter` will raise a `ModuleNotFoundError` — install system `python3-tk`.

---

## Quick verification commands ✅
```bash
# Show which python and venv
which python
echo "$VIRTUAL_ENV"

# Quick import checks
python -c "import simpleaudio; print('simpleaudio OK')"
python -c "import visual_layout; print('visual_layout import OK')"
```

---

## VS Code tips ✨
- Select the project's interpreter: Ctrl+Shift+P → **Python: Select Interpreter** → choose `.venv/bin/python`.
- Use Run → Start Debugging (F5). A sample `.vscode/launch.json` is included for convenience.

---

## I can help more
If you want, I can:
- Add a `Makefile` with common tasks,
- Add a short `CONTRIBUTING.md` / `DEVNOTES` with these tips.

If you want any of those, tell me which one to add next. ✅

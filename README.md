# Dash Hello World

A minimal Plotly Dash app to use as the starting point for the training session.

## Prerequisites

- Python 3.9 or newer. Check with:

  ```bash
  python --version
  ```

  On macOS/Linux you may need to use `python3` instead of `python` in the commands below.

## 1. Create a virtual environment

Open a terminal in this folder and run:

```bash
python -m venv .venv
```

This creates a folder called `.venv` that holds a separate Python installation for this project.

## 2. Activate the virtual environment



```cmd
.venv\Scripts\activate
```


When it is active, you will see `(.venv)` at the start of your terminal prompt.

> If PowerShell says running scripts is disabled, run
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.

## 3. Install the dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the app

```bash
python app.py
```

Open <http://127.0.0.1:8050> in your browser. You should see **Hello, World!**

Because the app runs with `debug=True`, the page reloads automatically when you save changes to `app.py`.

## 5. Stop the app

Press `Ctrl+C` in the terminal.

To leave the virtual environment, run:

```bash
deactivate
```

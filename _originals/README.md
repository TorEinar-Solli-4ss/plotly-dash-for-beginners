# Intro to Plotly Dash – training code

Code for the internal 4Subsea session *Intro to Plotly Dash*.

## Setup

```bash
uv sync
```

Run any file with `uv run <file>.py` and open http://127.0.0.1:8060.
Stop the server with `Ctrl+C` before starting the next one (they all use port 8060).

## Live-coding steps

| File | What's new |
|---|---|
| `step1-hello-world.py` | `Dash()`, `app.layout`, `app.run()` – nothing interactive yet |
| `step2-button.py` | A first callback with only an Input – it prints to the terminal |
| `step3-interactive-button.py` | Add an Output – the return value updates the page |
| `step4-inputs-vs-states.py` | Input vs State, Dash Bootstrap Components, two callbacks |
| `step5-plot.py` | `dcc.Graph` and a helper function that builds the figure |

## Practical exercise

Plot `F(x) = a * trig_func(b*x + c) + d` with a dropdown (sin/cos/tan), number inputs for a–d and a Calculate button.
Build it yourself, one stage at a time. The files below are checkpoints for when you get stuck – try the step files and the docs first.

| File | Stage |
|---|---|
| `exercise-stage1.py` | Layout only |
| `exercise-stage2.py` | Plot on click (Input + States) |
| `exercise-stage3.py` | Show the formula (two Outputs) |
| `exercise-stage4.py` | Live dropdown (State → Input) |
| `exercise-stage5.py` | Reset button (a second callback) |
| `exercise-stretch.py` | Previous curve (`dcc.Store`), x-range slider |
| `exercise-solution.py` | Complete, tidied-up reference solution |
| `exercise-solution-dmc.py` | The same solution built with Dash Mantine Components – only the layout differs |

`assets/style.css` is loaded automatically by Dash and applies the 4Subsea colours.

**Dash Mantine Components (dmc):** dmc 3.x needs React 19. Dash 4.5 includes it but uses React 18 by default, so dmc apps call
`dash._dash_renderer._set_react_version('19.2.4')` before `Dash()` – see `exercise-solution-dmc.py`.

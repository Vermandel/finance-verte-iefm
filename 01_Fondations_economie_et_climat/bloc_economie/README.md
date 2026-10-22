# Session 1 — Optimal growth

This directory is autonomous. Run LaTeX and Jupyter from this directory.

- Slides: `slides_session1.tex` / `slides_session1.pdf`
- Student notebook: `notebook_session1.ipynb`
- Complete worked solutions (five exercises, executed outputs): `notebook_session1_solution.ipynb`
- Mathematical reference: `growth_model.tex` / `growth_model.pdf`
- Original local module: `OptimalGrowth.py`
- Optional Python installation: `python -m pip install -r requirements.txt`
- The first notebook cell checks the six required modules and installs only
  missing packages using the notebook kernel's Python (`sys.executable`).
- Slide build: `latexmk -pdf -shell-escape slides_session1.tex`

The exercises come from `X3A_Climat/Session0/Notebook_OptimalGrowth.ipynb`.
The five worked solutions and expanded mathematical reference were added on
22 September 2026. Row zero contains only initial states; Y, C, I and s
remain NaN. See the dated validation report for the indexing correction.

The worked solutions now use explicit procedural code, with no helper
function definitions or technical assertions inside the notebook. Each
exercise shows parameters, initialization, simulation and plots directly.
Regression tests remain in `../tools/test_course_models.py`.

After updating the files, restart the Jupyter kernel and run from the top.
Keep this notebook alongside this session's `OptimalGrowth.py`; the import
cell reloads the module and prints its path. Do not mix this notebook with
the older module from the original `X3A_Climat/Session0` directory.

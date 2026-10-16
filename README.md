# COMP1205 – Assignment #1

**UWI Five Islands · School of Science, Computing and Artificial Intelligence**
**Due: Sunday 25 October 2026, 23:59 AST** · 75 marks (+10 bonus) · 6% of final grade

The full question specifications are in the handout PDF. This README explains how to
set up, test and submit your work, and the coding standards you will be marked on.
**If you have never used Git or GitHub before, start at Step 1 and go slowly.**

---

## 1. Join the course organization and accept the assignment

This course uses **Classroom 50** (classroom50.org), a free tool that gives each student a
private GitHub repository for the assignment.

1. Create a free GitHub account at <https://github.com> if you do not have one. Use a
   username your instructor can recognise (e.g. `jsmith-uwi`).
2. **Send your GitHub username** to your instructor using the form on the Moodle course
   page. Classroom 50 cannot add you by email alone.
3. Watch your email (and <https://github.com/notifications>) for an **invitation to join
   the course's GitHub organization**, and click **Join**. Assignment links do not work
   until you have accepted this invitation.
4. Open the **assignment acceptance link** posted on Moodle and accept the assignment.
5. Wait a minute and refresh. Your private repository is named
   `comp1205-a2-yourusername`. Bookmark it; you can also find it at <https://github.com>
   → your profile picture → **Your repositories**.
6. **Never rename this repository.** A renamed repository cannot be found or graded.

---

## 2. Choose a way to work

### Option A — Browser only (GitHub Codespaces, recommended if you are new)

Nothing to install. Works on any computer with Chrome, Edge or Firefox.

1. Open your repository page on GitHub.
2. Click the green **`<> Code`** button → **Codespaces** tab → **Create codespace on main**.
3. Wait 1–2 minutes. A VS Code editor opens in your browser, with Python and pytest
   already installed (the `.devcontainer` folder sets this up).
4. Open a file (e.g. `q1_part1.py`) from the file list on the left.
5. Open a terminal with **Terminal → New Terminal** (or `` Ctrl+` ``). To run a program:
   ```bash
   python q1_part1.py
   ```
6. When you finish a session, commit and push (Section 5). Codespaces stop by
   themselves after 30 minutes of inactivity; your files are kept, but **work that is
   not pushed is not submitted**.
7. The free Codespaces allowance is limited each month. Stop a codespace when you are
   done: <https://github.com/codespaces> → `...` → **Stop codespace**.

### Option B — Work on your own computer

1. **Install Python 3.10 or newer** from <https://www.python.org/downloads/>.
   *Windows:* on the first installer screen tick **“Add python.exe to PATH”**.
   Check in a terminal: `python --version` (on macOS/Linux you may need `python3`).
2. **Install Git** from <https://git-scm.com/downloads> (accept the default options).
   Then tell Git who you are (once only):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "the-email-you-used-on-github@example.com"
   ```
3. **Install VS Code** from <https://code.visualstudio.com/> and, inside VS Code, the
   **Python** extension (Extensions icon → search “Python” → Install).
4. **Install pytest:** `python -m pip install pytest`
5. **Clone your repository:** on your repo page click **`<> Code`** → **HTTPS** → copy
   the URL. In a terminal:
   ```bash
   git clone https://github.com/uwi-five-islands-comp1205/assignment-2-yourusername.git
   ```
   The first time you push, Git opens a browser window to sign in to GitHub — allow it.
6. **Open the folder:** VS Code → **File → Open Folder…** → choose the cloned folder.
   Use **Terminal → New Terminal** inside VS Code so commands run in the right folder.

---

## 3. What is in this repository

```
README.md                      this file
AI_LOG.md                      record every AI tool / helper you used (graded)
REFLECTION.md                  trace table, prediction, bug, ethics answers (graded)
q1_part1.py ... q5_part2.py    starter files: function stubs + docstrings to complete
tests/test_public.py           the sample runs from the handout, as tests (DO NOT EDIT)
.classroom50.yaml               added when you accept; links the repo to the course (DO NOT EDIT)
.devcontainer/devcontainer.json  sets up Codespaces                    (DO NOT EDIT)
```

Each **part is a separate file** and is graded separately. Part 2 is a *copy* of your
finished Part 1 plus the new rule. When Part 1 works, copy its code into `q1_part2.py`,
commit, and then add the new rule. **Never** break a finished part to build the next one.

---

## 4. Testing your work

### Run a program by hand
```bash
python q3_part1.py
```
Type the inputs from the handout's sample run and compare your output character by
character — spelling, capitals, spaces and punctuation must match exactly.

### Run the public tests
```bash
python -m pytest tests/test_public.py -v
```
* `PASSED` – your output matches that sample run exactly.
* `FAILED` – scroll up: pytest shows the expected output and yours.
* Run only one question: `python -m pytest tests/test_public.py -v -k q2_part1`

Note: when a test feeds input to your program, what you would have typed is **not**
shown, so a prompt and the next output appear on the same line, e.g.
`Enter plate: Normalised plate: P1234`. That is expected.

**Passing the public tests does NOT guarantee full marks.** They contain only the two
sample runs per part. Your work is graded with **hidden tests** (8–13 program runs plus
several direct function calls per part) covering the edge-case categories listed under
each part in the handout. Write and try your own test inputs for every category.

### Check that you only used allowed constructs
The grader runs an automated checker over every file. These are **prohibited** and are
flagged automatically: lists `[...]`, tuples (including `a, b = ...` and `return a, b`),
sets, dicts, comprehensions, `try`/`except`, classes, `lambda`, recursion, file I/O
(`open`, `with`), `global`, imports other than `math` and `string`, and these calls:
`split`, `rsplit`, `splitlines`, `partition`, `rpartition`, `list()`, `tuple()`,
`dict()`, `set()`, `sorted()`, `enumerate()`, `zip()`, `map()`, `filter()`,
`reversed()`, `eval()`, `exec()`.
AI assistants use these constantly — check every line you accept.

---

## 5. Saving your work: commit and push

A **commit** is a saved snapshot with a message. A **push** uploads your commits to
GitHub. **Only pushed work counts.**

### In VS Code / Codespaces (no typing)
1. Click the **Source Control** icon on the left (three connected dots).
2. Hover over **Changes** and click **+** to stage all changed files.
3. Type a meaningful message in the box, e.g. `q2_part2: add re-prompt loop for invalid numbers`.
4. Click **Commit**, then **Sync Changes** (or **Push**).

### In a terminal
```bash
git status                       # see what changed
git add q2_part2.py AI_LOG.md    # choose the files to save
git commit -m "q2_part2: add re-prompt loop for invalid numbers"
git push
```

### Check the push worked
1. Open your repository page on GitHub and refresh. Your latest message should appear
   next to the changed files, with a recent time.
2. Each push is checked automatically. After a minute or two, open the **Releases**
   section of your repository (right-hand side of the repo page). The newest release,
   named `submit/...`, shows a **feedback check**: which sample runs passed and whether
   any file uses a prohibited construct. **This is feedback, not your mark.**
3. The **Actions** tab shows the same runs: green ✓ passed, red ✗ something failed,
   yellow ● still running. A red ✗ while you are still working is normal.
4. A **Feedback** pull request in your repository is where your instructor may leave
   comments. Do not close or merge it.

### Commit rules (part of your mark — see the handout)
* At least **one commit per part**, with a message that says *what* changed
  (`q1_part3: handle # wildcard`, not `update` or `asdfg`).
* Spread your work over **at least 3 different days**. A single “everything” commit at
  the end is flagged for a follow-up conversation (not an automatic penalty).
* Commit `AI_LOG.md` as you go, not only at the end.

---

## 6. Rules

* **Do not edit, rename or delete** anything in `tests/`, `.github/` (created for you when
  you accept), `.devcontainer/` or the file `.classroom50.yaml`. These files are compared with the originals after the
  deadline; changes are penalised.
* Keep the file names exactly as given (`q1_part1.py`, …). A renamed file cannot be graded.
* **Your submission is the last commit pushed before 23:59 AST on Sunday 25 October 2026.**
  Commits after the deadline are ignored. Push early; GitHub outages are not an excuse.
* The instructor may ask any student for a **5-minute oral check**: explain or change a
  line of your code live. If you cannot explain code you submitted, the mark for that
  part can be capped.

---

## 7. Coding standards (marked under “Code quality”)

| Standard | Example |
|---|---|
| PEP 8 names: `snake_case` for variables and functions, `UPPER_CASE` for constants | `fuel_cost`, `MAX_HOUR` |
| 4-space indentation; lines ≤ 100 characters | (VS Code: bottom bar → “Spaces: 4”) |
| Header comment at the top of **every** file | name, student ID, date, question, collaborators, tools used |
| A PEP 257 docstring for **every** function | `"""Return the litres of fuel used to drive distance_km."""` |
| Comments explain **why**, not what | ✓ `# Compare whole cents so float error cannot flip the result` ✗ `# add 1 to x` |
| No magic numbers — named constants at the top | `LITRES_PER_GALLON = 3.785`, then use the name |
| One task per function | `is_valid_plate()` only checks; it does not print or read input |
| `main()` does input/output; other functions **compute and return** (no `print` or `input` inside them, except the required `read_...` helpers) | lets the hidden tests call your functions directly |
| `main()` is called only under `if __name__ == "__main__":` | already in every starter file — keep it |
| Test as you go | run both sample runs after **every** part before starting the next |

Every required function name, parameter list and return type in the handout must be
kept exactly — hidden tests call them by name. You may add extra helper functions.

---

## 8. Getting help

* Office hours and the course forum are listed on the course page.
* When asking for help, push first and share the link to your repo — never paste your
  whole solution into a public forum.
* If you use AI, record it in `AI_LOG.md`. Using it is allowed; hiding it is not.

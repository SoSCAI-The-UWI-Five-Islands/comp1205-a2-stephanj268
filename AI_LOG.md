# AI_LOG.md — COMP1205 Assignment #2

**Name:** Stephan Javorn Jones **Student ID:** 500004652

Record **every** use of an AI tool (ChatGPT, Claude, Copilot, Gemini, etc.) and any
website or person that helped you. Using AI is allowed; *not* recording it costs 1 mark.
Be honest — a short, accurate log is worth more than a long, polished one.

## Option A — I did not use any AI tools

- [ ] I confirm I did not use AI tools for any part of this assignment.

## Option B — My AI use

Copy the block below once per interaction (one question or conversation).

### Entry 1
- **Date:** 2026-10-25
- **Tool:** Cluade code
- **Question / part:** q4_part1.py
- **Exact prompt I gave** (paste it):  
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"

    if len(code) != 10:                       # exactly 10 characters
        return False
    if code[0] not in letters or code[1] not in letters:   # characters 1-2
        return False
    if code[2] != "-":                        # character 3
        return False
    for i in range(3, 8):                     # characters 4-8 (index 3 to 7)
        if code[i] not in digits:
            return False
    if code[8] != "-":                        # character 9
        return False
    if code[9] not in digits and code[9] != "X":   # character 10
        return False
    return True



### Entry 2
- **Date:** 2026-10-26
- **Tool:** Cluade code
- **Question / part:** q4_part2.py
- **Exact prompt I gave** (paste it): 

return ord(ch) - ord("A") + 1

  ```
- **What I accepted** (which lines/ideas I kept):  return litres / LITRES_PER_GALLON * price_per_gallon
- **What I changed and why** (e.g. "it used `split()`, which is prohibited, so I used `find()` and slicing"):
- **How I checked it was correct** (which sample runs / my own tests): my own test

## Other help
| Who / what (person, website, tutor) | Which part | What kind of help |
|---|---|---|
|  |  |  |

# The Robot Apology

A make.fun bounty entry: a two-line robot confession — one sentence owning a
specific mistake (salting the coffee by grabbing the wrong jar), one naming
the lesson and the fix. The program writes the text to `/output/entry.txt`.

[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/emafajriana/u-suga-the-robot-apology-dd96bb59-entry/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/emafajriana/u-suga-the-robot-apology-dd96bb59-entry/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

## Entry

> I'm sorry — I salted your coffee this morning because the salt and sugar jars sit side by side and I grabbed by position instead of reading the label.
> I learned that position is not identity, so from now on I read every label before I pour, even when I'm sure I already know.

## Run

```sh
python3 -P -s main.py   # writes entry.txt to $MAKEFUN_OUTPUT_DIR (default /output)
```

Stdlib only — runs on a bare `python:3.13-slim` grader image.

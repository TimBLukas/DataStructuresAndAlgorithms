# Usage: fetch_leetcode.py

`fetch_leetcode.py` turns a list of LeetCode URLs into offline Python solution files.
Each problem goes into a subfolder by difficulty. Each generated file contains the
full problem description, the official `Solution` stub, and unittest test cases.
After generation you do not need the internet.

## Requirements

- Python 3.9 or newer. This repository runs scripts with `uv run`.
- Internet access during generation only.
- No external packages. The script uses the standard library only.

## Prepare the input file

Create a text file with one URL per line. Example (`problems.txt`):

```
https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array
https://leetcode.com/problems/house-robber/
```

Rules:

- One URL or one problem slug per line.
- Query parameters such as `?envType=...` are allowed. The script ignores them.
- A bare slug like `two-sum` also works.
- Empty lines and lines that start with `#` are ignored.
- Duplicate slugs are processed once.

## Generate the files

Run from this folder:

```
uv run fetch_leetcode.py problems.txt
```

The script creates `easy/`, `medium/`, and `hard/` next to itself and writes one
file per problem, for example `easy/two_sum.py`. At the end it prints a summary:

```
Done: 14 created, 0 overwritten, 0 skipped, 0 failed (of 16 entries).
```

### Options

| Option | Effect |
| --- | --- |
| `--force` | Download again and overwrite existing files. Without this flag existing files are never touched. |
| `--output-dir DIR` | Write `easy/`, `medium/`, `hard/` into `DIR` instead of next to the script. |
| `--timeout SECONDS` | Network timeout per request. Default is 20. |

Example with options:

```
uv run fetch_leetcode.py problems.txt --force --timeout 30
```

## Work on a problem

Open the generated file, read the description in the header comments, fill in the
`Solution` class, then run its tests:

```
python easy/two_sum.py
```

Or run all problems in one folder:

```
python -m unittest discover -s easy -v
```

Tests fail while your solution returns no result. They pass when your code
matches the official examples.

## Structure of a generated file

1. Header comments: URL, title, difficulty, full description, examples, constraints.
2. Imports: `typing` names used by the signature, plus `unittest`.
3. The `Solution` class with the official method signature and `pass  # TODO`.
4. For tree and linked-list problems: the standard node class definition as comments.
5. A unittest class:
   - Real assertions for examples with plain data (numbers, strings, lists).
   - TODO placeholders for examples with trees, linked lists, or exotic formats.
     The raw example stays in comments above each placeholder.
   - An empty `test_edgecase` stub for your own cases.

## Error handling

- Existing files are skipped. Your solutions are never overwritten unless you
  pass `--force`.
- Premium-only problems are reported and skipped.
- Unknown URL, network error, or missing data: the entry is reported as failed,
  and the remaining entries still process.
- Exit code is 1 only when every entry fails.

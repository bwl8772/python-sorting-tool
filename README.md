# Python Sorting Tool

A command-line program for sorting words, lines, or integers from standard input
or a file. It can print the sorted data naturally or summarize values by
frequency.

## Requirements

Python 3.10 or later. The program uses only the Python standard library.

## Usage

Run from the repository root:

```bash
python "Sorting Tool with Python/task/main.py" [options]
```

Options:

- `-dataType word|line|long` selects words, complete lines, or integers
  (default: `word`).
- `-sortingType natural|byCount` sorts values or displays their frequencies
  (default: `natural`).
- `-inputFile <path>` reads input from a file instead of standard input.
- `-outputFile <path>` writes results to a file instead of standard output.

For example:

```bash
printf '4 1 1 -2 42 1 333\n' | python "Sorting Tool with Python/task/main.py" -dataType long
```

To count word frequencies in a file:

```bash
python "Sorting Tool with Python/task/main.py" -sortingType byCount -inputFile input.txt
```

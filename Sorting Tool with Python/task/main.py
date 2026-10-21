import sys
from collections import Counter
from pathlib import Path


options = {"-dataType": "word", "-sortingType": "natural",
           "-inputFile": None, "-outputFile": None}
allowed = {"-dataType": {"long", "line", "word"},
           "-sortingType": {"natural", "byCount"}}
arguments = sys.argv[1:]
index = 0
while index < len(arguments):
    argument = arguments[index]
    if argument in options:
        if index + 1 >= len(arguments) or arguments[index + 1] in options:
            label = {"-dataType": "data type", "-sortingType": "sorting type"}.get(argument, "file name")
            print(f"No {label} defined!")
            sys.exit()
        if argument in allowed and arguments[index + 1] not in allowed[argument]:
            label = "data" if argument == "-dataType" else "sorting"
            print(f"No {label} type defined!")
            sys.exit()
        options[argument] = arguments[index + 1]
        index += 2
    else:
        print(f'"{argument}" is not a valid parameter. It will be skipped.')
        index += 1
data_type = options["-dataType"]

all_data = []
if options["-inputFile"]:
    try:
        lines = Path(options["-inputFile"]).read_text(encoding="utf-8").splitlines()
    except OSError as error:
        print(f"Unable to read input file: {error}")
        sys.exit()
else:
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
for line in lines:
    if data_type == "line":
        all_data.append(line)
    else:
        all_data.extend(line.split())

converted = []
for value in all_data:
    if data_type == "long":
        try:
            converted.append(int(value))
        except ValueError:
            print(f'"{value}" is not a long. It will be skipped.')
    else:
        converted.append(value)
labels = {"long": "numbers", "word": "words", "line": "lines"}
results = [f"Total {labels[data_type]}: {len(converted)}."]
if options["-sortingType"] == "natural":
    if data_type == "line":
        results.append("Sorted data:")
        results.extend(sorted(converted))
    else:
        results.append("Sorted data: " + " ".join(map(str, sorted(converted))))
else:
    counts = Counter(converted)
    for value, count in sorted(counts.items(), key=lambda item: (item[1], item[0])):
        percentage = int(count / len(converted) * 100)
        results.append(f"{value}: {count} time(s), {percentage}%")
text = "\n".join(results) + "\n"
if options["-outputFile"]:
    try:
        Path(options["-outputFile"]).write_text(text, encoding="utf-8")
    except OSError as error:
        print(f"Unable to write output file: {error}")
else:
    print(text, end="")

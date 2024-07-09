# compare-code-line-by-line
```markdown
# File Comparator

This script compares two text files and finds either similar or non-similar lines between them. The comparison is based on the similarity ratio of the lines, which can be adjusted according to your needs.

## Features

- Compare two text files to find similar lines.
- Compare two text files to find non-similar lines.
- Save the results to a uniquely named file.

## Requirements

- Python 3.x

## Installation

Clone this repository and navigate to the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

## Usage

Run the script with the following options:

```bash
python comparator.py <file1> <file2> [-ss] [-sus]
```

### Arguments

- `file1`: Path to the first file.
- `file2`: Path to the second file.
- `-ss`: (Optional) Find and save similar lines.
- `-sus`: (Optional) Find and save non-similar lines.

### Examples

1. Find and save similar lines between `file1.txt` and `file2.txt`:

```bash
python comparator.py file1.txt file2.txt -ss
```

2. Find and save non-similar lines between `file1.txt` and `file2.txt`:

```bash
python comparator.py file1.txt file2.txt -sus
```

## Functions

### read_file(file_path)

Reads the content of the file at `file_path`.

### write_file(file_path, lines)

Writes the list of `lines` to the file at `file_path`.

### find_similar_lines(file1_lines, file2_lines)

Finds lines in `file1_lines` that are similar to any line in `file2_lines`.

### find_unsimilar_lines(file1_lines, file2_lines, file1_name, file2_name)

Finds lines in `file1_lines` and `file2_lines` that are not similar to any line in the other file.

### get_unique_filename(base_name)

Generates a unique filename by appending a counter if a file with the given `base_name` already exists.

### main()

Main function to parse arguments and execute the comparison.

## License

This project is licensed under the GLP License - see the [LICENSE](LICENSE) file for details.


import argparse
from difflib import SequenceMatcher
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def find_similar_lines(file1_lines, file2_lines):
    similar_lines = []
    for line1 in file1_lines:
        for line2 in file2_lines:
            if SequenceMatcher(None, line1, line2).ratio() > 0.8:
                similar_lines.append(line1)
                break
    return similar_lines

def find_unsimilar_lines(file1_lines, file2_lines, file1_name, file2_name):
    unsimilar_lines = []
    for index1, line1 in enumerate(file1_lines):
        is_similar = False
        for line2 in file2_lines:
            if SequenceMatcher(None, line1, line2).ratio() > 0.8:
                is_similar = True
                break
        if not is_similar:
            unsimilar_lines.append(f"{index1 + 1}, {file1_name}: {line1}")

    for index2, line2 in enumerate(file2_lines):
        is_similar = False
        for line1 in file1_lines:
            if SequenceMatcher(None, line2, line1).ratio() > 0.8:
                is_similar = True
                break
        if not is_similar:
            unsimilar_lines.append(f"{index2 + 1}, {file2_name}: {line2}")

    return unsimilar_lines

def get_unique_filename(base_name):
    counter = 1
    new_name = base_name
    while os.path.exists(new_name):
        new_name = f"{base_name.rsplit('.', 1)[0]}-{counter}.{base_name.rsplit('.', 1)[1]}"
        counter += 1
    return new_name

def main():
    parser = argparse.ArgumentParser(description='Compare two files and find similar or non-similar lines.')
    parser.add_argument('file1', type=str, help='Path to the first file')
    parser.add_argument('file2', type=str, help='Path to the second file')
    parser.add_argument('-ss', action='store_true', help='Find and save similar lines')
    parser.add_argument('-sus', action='store_true', help='Find and save non-similar lines')
    
    args = parser.parse_args()

    file1_lines = read_file(args.file1)
    file2_lines = read_file(args.file2)
    
    if args.ss:
        similar_lines = find_similar_lines(file1_lines, file2_lines)
        result_file = get_unique_filename('file-similar-result.txt')
        write_file(result_file, similar_lines)
        print(f'Similar lines saved to {result_file}')
    
    if args.sus:
        unsimilar_lines = find_unsimilar_lines(file1_lines, file2_lines, args.file1, args.file2)
        result_file = get_unique_filename('file-unsimilar-result.txt')
        write_file(result_file, unsimilar_lines)
        print(f'Non-similar lines saved to {result_file}')

if __name__ == '__main__':
    main()

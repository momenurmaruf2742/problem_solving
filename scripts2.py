def read_file_to_set(file_path):
    """Read a file and return a set of its lines."""
    lines_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            lines_set.add(line.strip())
    return lines_set


def find_unique_to_file2(file1_path, file2_path, output_path):
    """Find lines that are unique to file2 and write them to an output file."""
    file1_lines = read_file_to_set(file1_path)

    with open(file2_path, 'r') as file2, open(output_path, 'w') as output_file:
        for line in file2:
            line = line.strip()
            if line not in file1_lines:
                output_file.write(line + '\n')


def main():
    file1_path = 'output.txt'
    file2_path = 'total details.txt'
    output_path = 'unique_to_file2.txt'

    find_unique_to_file2(file1_path, file2_path, output_path)


if __name__ == "__main__":
    main()
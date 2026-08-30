import argparse
import os
from pathlib import Path

# ===== Argument Handling =====
parser = argparse.ArgumentParser(
    prog="cat",
    description="Prints file content",
)

parser.add_argument("-b", action="store_true", help="Numbers lines that aren't empty")
parser.add_argument("-n", action="store_true", help="Numbers all lines")
parser.add_argument("file_names", nargs="*", help="Files or folders to display")

args = parser.parse_args()

# ===== cat Procedure =====
def cat(args):
    cwd = os.getcwd()
    all_files_contents = read_files(args.file_names, cwd)
    execute_flags(all_files_contents)
    print_lines(all_files_contents)

# ===== Extracting Data from Arguments =====
def read_files(file_names, cwd):
    all_files_contents = []
    
    for file_name in file_names:
        file_content = read_file(file_name, cwd)
        all_files_contents.append(file_content.splitlines())
    return all_files_contents

def read_file(file_name, cwd):
    file_path = Path(cwd) / file_name
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().rstrip()

# ===== Flag Handling =====
def execute_flags(all_files_contents):
    if args.b:
        for file_content in all_files_contents:
            line_number = 1
            for line_idx, line in enumerate(file_content):
                if line != "":
                    file_content[line_idx] = f"{line_number:>6}\t{line}"
                    line_number += 1
 
    elif args.n:
        for file_idx, file_content in enumerate(all_files_contents):
            all_files_contents[file_idx] = [
                f"{line_idx:>6}\t{line}"
                for line_idx, line in enumerate(file_content, start=1)
            ]

def make_list(output_string):
    return output_string.replace("\t", "\n").replace("\n\n", "\n")

# ===== Print Output =====
def print_lines(all_files_contents):
  for file_content in all_files_contents:
    for line in file_content:
      print(line)

# ===== Run cat =====
cat(parser.parse_args())
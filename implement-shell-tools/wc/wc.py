import argparse
import os
from pathlib import Path


# Argument Handling
parser = argparse.ArgumentParser(
    prog="wc",
    description="Print line, word, and byte counts for each file.",
)

parser.add_argument("-l", action="store_true", help="Show line count")
parser.add_argument("-w", action="store_true", help="Show word count")
parser.add_argument("-c", action="store_true", help="Show byte size")
parser.add_argument("files", nargs="*", help="File names to process")

args = parser.parse_args()

# Global Variables
metrics = ["line_count", "word_count", "byte_size"]
displayed_metrics = []

# ===== wc Procedure =====
def wc(args):
    cwd = os.getcwd()
    file_names = args.files

    execute_flags()
    all_files_data = add_totals(extract_files_data(file_names, cwd))
    print_output(all_files_data)

# ===== Flag Handling =====
def execute_flags():
    if args.w:
        displayed_metrics.append("word_count")
    if args.l:
        displayed_metrics.append("line_count")
    if args.c:
        displayed_metrics.append("byte_size")

# ===== Extracting Files Data =====
def extract_files_data(file_names, cwd):
    all_files_data = []

    for file_name in file_names:
        file_data = {}
        file_data["name"] = file_name
        file_data["text"] = read_file(file_name, cwd)
        file_data["line_count"] = calculate_line_count(file_data["text"])
        file_data["word_count"] = calculate_word_count(file_data["text"])
        file_data["byte_size"] = read_byte_size(file_name, cwd)

        all_files_data.append(file_data)

    return all_files_data

def read_file(file_name, cwd):
  file_path = Path(cwd) / file_name
  return file_path.read_text(encoding="utf-8").rstrip()

def calculate_line_count(text):
  if not text:
    return 0
  return len(text.splitlines())

def calculate_word_count(text):
  return len(text.split())

def read_byte_size(file_name, cwd):
  file_path = os.path.join(cwd, file_name)
  return os.path.getsize(file_path)

def add_totals(all_files_data):
    if len(all_files_data) <= 1:
        return all_files_data

    totals_data = {"name": "total"}
    
    for metric in metrics:
        metric_sum = 0
        for file in all_files_data:
            metric_sum += file[metric]
        totals_data[metric] = metric_sum

    all_files_data.append(totals_data)
    return all_files_data

# ===== Outputting Data =====
def print_output(output_data):
    for file in output_data:
        output_string = ""

        for metric in metrics:
            if not displayed_metrics or metric in displayed_metrics:
                output_string += str(file[metric]).rjust(8)

        output_string += f" {file['name']}"
        print(output_string)

# ===== Run wc =====
wc(parser.parse_args())
import argparse
import os
from pathlib import Path

# Argument Handling
parser = argparse.ArgumentParser(
    prog="ls",
    description="Print line, word, and byte counts for each file.",
)

parser.add_argument("-1", action="store_true", help="Show output on separate lines")
parser.add_argument("-a", action="store_true", help="Show hidden files")
parser.add_argument("file_system_items", nargs="*", help="Files or folders to display")

args = parser.parse_args()


# ===== ls Procedure =====
def ls(args):
    flag_status = {"print_in_list": False, "show_all": False}
    execute_flags(flag_status)

    fs_items = check_args_length(args.file_system_items)
    dir_args = get_dir_args(fs_items)
    file_args = get_file_args(fs_items, flag_status)

    print_output(
        populate_output(fs_items, dir_args, file_args, flag_status), flag_status
    )


# ===== Flag Handling =====
def execute_flags(flag_status):
    if getattr(args, "1"):
        flag_status["print_in_list"] = True
    if args.a:
        flag_status["show_all"] = True


def make_list(output_string):
    return output_string.replace("\t", "\n").replace("\n\n", "\n")


# Extracting Data from Arguments
def check_args_length(fs_items):
    if len(fs_items) == 0:
        fs_items.append(".")
    return fs_items


def get_dir_args(fs_items):
    return [p for p in fs_items if Path(p).is_dir()]


def get_file_args(fs_items, flag_status):
    file_args = [p for p in fs_items if not Path(p).is_dir()]
    if not flag_status["show_all"]:
        file_args = remove_dot_files(file_args)
    return file_args


# Populating and Outputting Data
def populate_output(fs_items, dir_args, file_args, flag_status):
    output_string = ""

    if len(fs_items) == 1:
        for file in file_args:
            output_string += file + " "
        for dir_item in dir_args:
            output_string += dir_output(dir_item, flag_status)
    else:
        for file in file_args:
            output_string += file + "\t"
        for dir_item in dir_args:
            output_string += f"\n\n{dir_item}:\n" + dir_output(dir_item, flag_status)
    return output_string


def dir_output(dir_item, flag_status):
    target_path = Path.cwd() / dir_item
    contents = os.listdir(target_path)
    output_str = ""
    if flag_status["show_all"]:
        output_str += ".\t..\t"
    else:
        contents = remove_dot_files(contents)

    for item in contents:
        output_str += item + "\t"
    return output_str


def remove_dot_files(file_list):
    return [item for item in file_list if not item.startswith(".")]


def print_output(output_string, flag_status):
    output = output_string
    if flag_status["print_in_list"]:
        output = make_list(output)
    print(output.rstrip())


# ===== Run ls =====
ls(parser.parse_args())

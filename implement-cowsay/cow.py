import cowsay
import sys
import argparse

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things",
)

parser.add_argument("--animal", choices=cowsay.char_names, help="The animal to be saying things.", default="cow")
parser.add_argument("message", nargs="*", help="The message to say.")

args = parser.parse_args()

if args.animal not in cowsay.char_names:
    sys.exit(f"Unknown animal: {args.animal!r}. Choose from: {', '.join(cowsay.char_names)}")

cowsay.char_funcs[args.animal](" ".join(args.message))
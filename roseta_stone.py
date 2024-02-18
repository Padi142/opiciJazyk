import argparse
import sys

DEFAULT_OUTPUT_FILE = "output.txt"

MONKEY_LANGUAGE_TO_MORSE = {
    "🐒": ".-.-.-",
    "uagh": "/",
    "a": ".",
    "u": "-"
}

MORSE_TO_MONKEY_LANGUAGE = { v: k for k, v in MONKEY_LANGUAGE_TO_MORSE.items() }

def monkey_language_to_morse(monkey_language: str) -> str:
    for letter in MONKEY_LANGUAGE_TO_MORSE:
        monkey_language = monkey_language.replace(letter, MONKEY_LANGUAGE_TO_MORSE[letter])

    return monkey_language

def morse_to_monkey_language(morse: str) -> str:
    for letter in MORSE_TO_MONKEY_LANGUAGE:
        morse = morse.replace(letter, MORSE_TO_MONKEY_LANGUAGE[letter])

    return morse


if __name__ == "__main__":
    argparse = argparse.ArgumentParser(prog="ApeScript.py", description="Provide text for translation as an command line string argument")
    argparse.add_argument("--monkey", metavar="input_file", help="Input file with your monkey language text")
    argparse.add_argument("--morse", metavar="input_file", help="Input file with your morse code text")
    argparse.add_argument("--output", metavar="output_file", help="Output file for your translation (default: output.txt)")

    args = argparse.parse_args()

    out_str = ""

    if args.monkey:
        with open(args.monkey, "r") as file:
            data = file.read()
            out_str = monkey_language_to_morse(data)
    elif args.morse:
        with open(args.morse, "r") as file:
            data = file.read()
            out_str = morse_to_monkey_language(data)
    else:
        print("""
usage: ApeScript.py [-h] [--monkey input_file] [--morse input_file]

Provide text for translation as an command line string argument

options:
  -h, --help           show this help message and exit
  --monkey input_file  Input file with your monkey language text
  --morse input_file   Input file with your morse code text
""")
        sys.exit(0)

    with open(args.output if args.output is not None else DEFAULT_OUTPUT_FILE, "w") as file:
        file.write(out_str)
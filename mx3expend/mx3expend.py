import re
import numpy as np  # noqa: F401
import argparse
import os
import itertools


def parse_template(template_path):
    try:
        with open(template_path, "r") as f:
            return f.read()
    except IOError as e:
        print(f"Error reading template file: {e}")
        exit(1)


def find_expressions(mx3):
    matches = re.finditer(r"\{(.*?)\}", mx3)
    expressions = []
    for match in matches:
        extracted_text = match.group(1)
        prefix, range, fmt, suffix = extracted_text.split(";")
        array = eval(range)
        expressions.append(
            {
                "prefix": prefix,
                "array": array,
                "fmt": fmt,
                "suffix": suffix,
                "original": extracted_text,
            }
        )
    return expressions


def generate_files(parent_dir, mx3, expressions):
    all_combinations = itertools.product(*(exp["array"] for exp in expressions))
    for combination in all_combinations:
        path_parts = [
            f"{exp['prefix']}{item:{exp['fmt']}}{exp['suffix']}"
            for item, exp in zip(combination, expressions)
        ]
        full_path = f"{parent_dir}/{'/'.join(path_parts)}.mx3"
        new_mx3 = mx3
        for item, exp in zip(combination, expressions):
            new_mx3 = new_mx3.replace(
                "{" + exp["original"] + "}", f"{item:{exp['fmt']}}"
            )

        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f2:
            f2.write(new_mx3)


def main():
    parser = argparse.ArgumentParser(description="Parse and expand a mx3 template.")
    parser.add_argument("template_path", type=str, help="Template to parse and expand")
    args = parser.parse_args()
    parent_dir = os.path.dirname(os.path.abspath(args.template_path))

    mx3 = parse_template(args.template_path)
    expressions = find_expressions(mx3)
    generate_files(parent_dir, mx3, expressions)

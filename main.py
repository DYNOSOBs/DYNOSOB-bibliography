import glob

import bibtexparser

import numpy as np

import re


def read_files_write_raw_bib():
    files = glob.glob("assets/*")

    bibliography = ""

    for file in files:
        with open(file, "r") as f:
            entry = f.read()
            bibliography += entry + "\n"

    months = re.findall(r"(?<=month = ).*?(?=,)", bibliography)

    not_edited = [m for m in months if "{" not in m]

    for month in not_edited:
        bibliography = bibliography.replace(
            month + ",", "{" + month.title() + "},"
        )

    with open("bibtex.bib", "w") as bibfile:
        bibfile.write(bibliography)

    return True


def prepare_bibliography():
    with open("bibtex.bib") as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # lower case "ID" and find unique entries indices
    for entry in bib_database.entries:
        key = entry["ID"]
        key = key.split(":")
        if len(key) < 2:
            print(f"Note that entry: {key} does not follow key convention.")
        key = key[0].lower() + ":" + ":".join(key[1:])
        entry["ID"] = key

    keys = [v["ID"] for v in bib_database.entries]
    unique_indices = [keys.index(x) for x in set(keys)]

    # keep unique entries
    entries = [bib_database.entries[i] for i in unique_indices]

    sorted_indices = [
        i[0] for i in sorted(enumerate(entries), key=lambda x: x[1]["ID"])
    ]

    sorted_entries = [entries[i] for i in sorted_indices]

    # title "ID"
    for entry in sorted_entries:
        key = entry["ID"]
        key = key.split(":")
        key = key[0].title() + ":" + ":".join(key[1:])
        entry["ID"] = key

    return sorted_entries, bib_database


def comment_to_bibtex(comment, words_per_line=11):
    words_in_comments = comment.split(" ")
    bibtex = "@comment{"
    for i in np.arange(0, len(words_in_comments), words_per_line):
        bibtex += " ".join(words_in_comments[i : i + words_per_line]) + "\n"

    bibtex = bibtex[:-1] + "}"
    return bibtex


def str_to_bibtex(e):
    return "{" + e + "}"


def entry_to_bibtex(entry):
    bibtex = ""
    indent = "  "

    bibtex += "@" + entry["ENTRYTYPE"] + "{" + entry["ID"] + ","

    field_fmt = "\n{indent} {field} = {value},"

    for field in [i for i in entry.keys() if i not in ["ENTRYTYPE", "ID"]]:
        try:
            bibtex += field_fmt.format(
                indent=indent, field=field, value=str_to_bibtex(entry[field])
            )
        except TypeError:
            raise TypeError(
                "The field %s in entry %s must be a string"
                % (field, entry["ID"])
            )

    bibtex += "\n}\n"
    return bibtex


def export_bib(entries):
    with open("bibtex.bib", "w") as bibfile:
        for entry in entries:
            to_write = f"{entry_to_bibtex(entry)}\n"
            bibfile.write(to_write)
    return True


if __name__ == "__main__":
    wrote = read_files_write_raw_bib()

    if wrote:
        entries, db = prepare_bibliography()

    exported = export_bib(entries)

    if exported == False:
        print("Export failed.")

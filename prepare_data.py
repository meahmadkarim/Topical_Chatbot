"""Convert the official Topical-Chat JSON format to ordered conversation CSV.

Download a split yourself from https://github.com/alexa/Topical-Chat.
The source data remains subject to its CDLA-Sharing-1.0 terms.
"""
import argparse
import csv
import json
from pathlib import Path


def convert(source, destination):
    data = json.loads(Path(source).read_text(encoding="utf-8"))
    rows = []
    for conversation_id, conversation in data.items():
        for turn in conversation["content"]:
            rows.append((conversation_id, turn["message"]))
    if not rows:
        raise ValueError("No conversation turns found")
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["conversation_id", "message"])
        writer.writerows(rows)
    return len(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()
    print(f"Converted {convert(args.source, args.destination)} conversation turns")

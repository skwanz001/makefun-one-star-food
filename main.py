"""One Star, Five Stars for the Food.

Writes a single-sentence alien-tourist one-star review of Earth that
still compliments the food, to /output/entry.txt.

The sentence (190 characters, one sentence, UTF-8):
an alien tourist crosses 40 light-years, hates the gravity, the
exhaust air and the queuing, and rebooks anyway for the dumplings.
"""

import os

REVIEW = (
    "One star: I flew 40 light-years to a planet where gravity "
    "flattened my antennae, the air tastes of exhaust, and humans "
    "queue for everything, but the dumplings were so good I "
    "rebooked anyway."
)


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"review is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    assert text == text.strip() and "\n" not in text, "must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly this text.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the review"
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Word search generator: grid + hidden words + answer key.

Usage:
    python3 wordsearch.py --size 12 --seed 3 MOON LANTERN SWAP STAMP LETTER
    python3 wordsearch.py --size 12 --diagonal --backwards < words.txt
Words come from argv, or one-per-line from stdin.
"""
import argparse, random, string, sys


def make_wordsearch(words, size=12, dirs=None, seed=None):
    rnd = random.Random(seed)
    grid = [["." for _ in range(size)] for _ in range(size)]
    placed = {}
    for w in sorted(words, key=len, reverse=True):
        w = "".join(ch for ch in w.upper() if ch.isalpha())
        if not w or len(w) > size:
            continue
        for _ in range(500):
            dx, dy = rnd.choice(dirs)
            r0, c0 = rnd.randrange(size), rnd.randrange(size)
            cells = [(r0 + i * dy, c0 + i * dx) for i in range(len(w))]
            if any(not (0 <= r < size and 0 <= c < size) for r, c in cells):
                continue
            if all(grid[r][c] in (".", ch) for (r, c), ch in zip(cells, w)):
                for (r, c), ch in zip(cells, w):
                    grid[r][c] = ch
                placed[w] = cells
                break
    for r in range(size):
        for c in range(size):
            if grid[r][c] == ".":
                grid[r][c] = rnd.choice(string.ascii_uppercase)
    return grid, placed


def render(grid, placed=None):
    n = len(grid)
    letters = "".join(chr(65 + i % 26) for i in range(n))
    out = ["    " + " ".join(letters)]
    for i, row in enumerate(grid):
        out.append(f"{i:3d} " + " ".join(row))
    if placed:
        out.append("")
        for w, cells in placed.items():
            out.append(f"{w:<12} " + " -> ".join(f"({r},{c})" for r, c in cells))
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("words", nargs="*")
    p.add_argument("--size", type=int, default=12)
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--diagonal", action="store_true")
    p.add_argument("--backwards", action="store_true")
    a = p.parse_args()

    words = a.words or [l.strip() for l in sys.stdin if l.strip()]
    dirs = [(1, 0), (0, 1)]
    if a.diagonal:
        dirs += [(1, 1), (-1, 1)]
    if a.backwards:
        dirs += [(-x, -y) for x, y in dirs] + [(x, -y) for x, y in dirs]

    grid, placed = make_wordsearch(words, a.size, dirs, a.seed)
    print(render(grid, placed))
    print(f"\n{len(placed)}/{len(words)} words placed in {a.size}x{a.size}")


if __name__ == "__main__":
    main()

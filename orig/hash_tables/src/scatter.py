#!/usr/bin/env python3
import sys
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", required=True)
parser.add_argument("--xlabel", default="X")
parser.add_argument("--ylabel", default="Y")
parser.add_argument("--title", default="")
parser.add_argument("--size", type=float, nargs=2, default=[6, 4])

args = parser.parse_args()

x, y = [], []
for line in sys.stdin:
    a, b = map(float, line.split())
    x.append(a)
    y.append(b)

plt.figure(figsize=args.size)
plt.scatter(x, y)
plt.xlabel(args.xlabel)
plt.ylabel(args.ylabel)
plt.title(args.title)
plt.tight_layout()
plt.savefig(args.output)

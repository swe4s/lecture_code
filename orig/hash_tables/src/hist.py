#!/usr/bin/env python3
import sys
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", required=True)
parser.add_argument("--xlabel", default="Value")
parser.add_argument("--ylabel", default="Count")
parser.add_argument("--title", default="")
parser.add_argument("--size", type=float, nargs=2, default=[6, 4])
parser.add_argument("--bins", type=int, default=30)

args = parser.parse_args()

values = [float(line.strip()) for line in sys.stdin if line.strip()]

plt.figure(figsize=args.size)
plt.hist(values, bins=args.bins)
plt.xlabel(args.xlabel)
plt.ylabel(args.ylabel)
plt.title(args.title)
plt.tight_layout()
plt.savefig(args.output)

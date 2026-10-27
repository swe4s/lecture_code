"""Print the most common words in a text file."""
import argparse
import collections
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description='Print the most common words in a text file.')
    parser.add_argument('--in_file', type=str, required=True,
                        help='Text file to read')
    parser.add_argument('--n', type=int, default=3,
                        help='Number of words to print')
    return parser.parse_args()


def count_words(file_name):
    """Return a Counter of lower-case words in a file."""
    counts = collections.Counter()
    with open(file_name) as f:
        for line in f:
            for word in line.lower().split():
                counts[word.strip('.,;:!?')] += 1
    return counts


def main():
    args = get_args()
    try:
        counts = count_words(args.in_file)
    except FileNotFoundError:
        print('Could not find ' + args.in_file, file=sys.stderr)
        sys.exit(1)
    print('Read ' + str(sum(counts.values())) + ' words', file=sys.stderr)
    for word, count in counts.most_common(args.n):
        print(word, count)


if __name__ == '__main__':
    main()

# Step 2b: ambiguous wildcards.
# Both rules can make counts/forest.txt, so Snakemake refuses to guess.
#
#   snakemake -s step2b.smk -c1 counts/forest.txt   # AmbiguousRuleException
#
# Fix: give each kind of file its own pattern, e.g. counts/{name}.words.txt
# and counts/{name}.lines.txt.

rule count_words:
    input:
        "data/{name}.txt"
    output:
        "counts/{name}.txt"
    shell:
        "wc -w < {input} > {output}"

rule count_lines:
    input:
        "data/{name}.txt"
    output:
        "counts/{name}.txt"
    shell:
        "wc -l < {input} > {output}"

# Step 1: one rule, no wildcards.
# A rule says: to make the OUTPUT from the INPUT, run this command.
#
#   snakemake -s step1.smk -c1 -n    # dry run: what would happen?
#   snakemake -s step1.smk -c1       # do it
#   snakemake -s step1.smk -c1       # again: "Nothing to be done"

rule count_ocean:
    input:
        "data/ocean.txt"
    output:
        "counts/ocean.txt"
    shell:
        "wc -w < {input} > {output}"

# Step 4: chaining rules into a graph.
# summarize needs every count file, so Snakemake runs count_words first.
# glob_wildcards finds the names from the files on disk, so adding
# data/tundra.txt adds it to the pipeline with no code change.
#
#   snakemake -s step4.smk -c1
#   snakemake -s step4.smk --dag | dot -Tpng > dag.png
#   snakemake -s step4.smk -c3 --forceall     # 3 jobs at once

NAMES = glob_wildcards("data/{name}.txt").name

rule all:
    input:
        "summary.txt"

rule count_words:
    input:
        "data/{name}.txt"
    output:
        "counts/{name}.txt"
    shell:
        "wc -w < {input} > {output}"

rule summarize:
    input:
        expand("counts/{name}.txt", name=NAMES)
    output:
        "summary.txt"
    shell:
        "for f in {input}; do echo $f $(cat $f); done > {output}"

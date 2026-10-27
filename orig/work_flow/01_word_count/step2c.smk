# Step 2c: the fix for 2b. Different outputs get different patterns.
#
#   snakemake -s step2c.smk -c1 counts/forest.words.txt counts/forest.lines.txt

rule count_words:
    input:
        "data/{name}.txt"
    output:
        "counts/{name}.words.txt"
    shell:
        "wc -w < {input} > {output}"

rule count_lines:
    input:
        "data/{name}.txt"
    output:
        "counts/{name}.lines.txt"
    shell:
        "wc -l < {input} > {output}"

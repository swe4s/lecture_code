# Step 3: a target rule.
# The first rule in the file is the default target. By convention it is
# called "all" and has only inputs: the final files we want.
# expand() fills in a pattern once for each value in a list.
#
#   snakemake -s step3.smk -c1 -n
#   snakemake -s step3.smk -c1
#   echo "Seals rest on the ice." >> data/ocean.txt
#   snakemake -s step3.smk -c1       # only ocean is redone
#   (touch alone is not enough in Snakemake 9: it also checks the contents)

NAMES = ["ocean", "forest", "desert"]

rule all:
    input:
        expand("counts/{name}.txt", name=NAMES)

rule count_words:
    input:
        "data/{name}.txt"
    output:
        "counts/{name}.txt"
    shell:
        "wc -w < {input} > {output}"

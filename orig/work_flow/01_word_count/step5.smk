# Step 5: config, params, logs, and our own Python script.
# Settings live in config.yaml, not in the code. Change them from the
# command line without editing anything:
#
#   snakemake -s step5.smk -c1
#   snakemake -s step5.smk -c1 --config n_top=5
#   snakemake -s step5.smk -c1 --forceall --printshellcmds

configfile: "config.yaml"

NAMES = glob_wildcards("data/{name}.txt").name

rule all:
    input:
        "summary.txt",
        expand("top_words/{name}.txt", name=NAMES)

rule count_words:
    input:
        "data/{name}.txt"
    output:
        "counts/{name}.txt"
    shell:
        "wc -w < {input} > {output}"

rule top_words:
    input:
        "data/{name}.txt"
    output:
        "top_words/{name}.txt"
    params:
        n=config["n_top"]
    log:
        "logs/top_words/{name}.log"
    shell:
        "python scripts/top_words.py --in_file {input} --n {params.n} "
        "> {output} 2> {log}"

rule summarize:
    input:
        expand("counts/{name}.txt", name=NAMES)
    output:
        "summary.txt"
    shell:
        "for f in {input}; do echo $f $(cat $f); done > {output}"

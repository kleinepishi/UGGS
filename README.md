# Roadmap

## Overview: 
An approach to looking for “low-hanging fruit” in sub-groups of genes that are segregated by “easy” variables. We assume that the gene groups have been identified by various molecular approaches (most typically differential expression in one or more tests), and that we will have concurrently run functional enrichment analysis

## Inputs:
Organism: An accepted identifier of a model organism (this is not likely to be a successful approach for non-model organisms)
Gene sets: One or more sub-groups of genes, with the control/comparison either comprised of the entire genome/transcriptome, or alternatively a group passed in and identified as such

## Possible resources:
Ensembl, UCSC browser (specifically the table browser), ModMine (in the form of yeastMine, mouseMine, wormMine, etc), STRING, modEncode,

## Note 1: 
To start with, I expect most of this to happen manually, but ideally, we will be able to identify patterns and procedures that can be captured in automated workflows. Since we are going to be looking at statistical distributions of various features, some programmatic or statistical environment will be necessary (JMP, Python/numPy/sciPy/pandas, etc).

## Note 2: 
This will be assumed to be in addition to and independent of pathway/ontology analysis, which should, of course, also be carried out.

## Steps to be carried out in the main approach:

For each gene set, retrieve one or more tables of statistical characterizations, including at least (but not necessarily limited to)
a. Transcript length
b. CDS length
c. Number of exons
d. 5’UTR length
e. 3’UTR length
f. Codon Adaptation Index (if available)
g. Known interacting partners (perhaps from String)
h. Known regulatory interactions (e.g., validated or putative TF binding sites)
Visualize in an appropriate manner (box plots, violin plots, etc) the various sets, and
Apply appropriate statistical tests on the equality/consistency of the values within each variable
Generate a visual/text report that shows all tests, with highlighting of any significant differences

# FASTA Sequence Analyzer

My First Bioinformatics Project! 

## Overview

FASTA Sequence Analyzer is a Python-based bioinformatics tool which is designed to perform basic DNA sequence analysis from FASTA files. Using Biopython and Pandas, the tool processes nucleotide sequences and generates a structured report which contains important sequence characteristics which gets exported as a csv file.

The program helps in the automation of common sequence analysis tasks, including nucleotide composition analysis, GC content calculation, reverse complement generation, and translation of DNA sequences into their corresponding amino acid sequences using the standard genetic code.

## Features

- **FASTA File Processing:** Reads and processes multiple DNA sequences from a single FASTA file.
- **Sequence Length:** Determines the total number of nucleotide bases in each sequence.
- **Nucleotide Composition:** Calculates the individual counts of adenine (A), thymine (T), guanine (G), cytosine (C), and ambiguous nucleotide bases.
- **GC Content:** Calculates the percentage of guanine and cytosine bases in each sequence.
- **Reverse Complement:** Generates the complementary DNA strand in the 5′ to 3′ direction.
- **Protein Translation:** Translates DNA nucleotide sequences into amino acid sequences using the standard genetic code.
- **Data Export:** Organizes the analysis results into a Pandas DataFrame and exports them as a CSV file.

## Technologies Used
- Python
- Biopython
- Pandas

## Contents
`sequence.fasta` - sample DNA sequence which is used for testing

`analysis_results.csv` - output file which contains the sequence analysis results generated from the python program

`DNA_Sequence_Analyser.ipynb` - Google Colab notebook explaining the functions of the code and its output 


## Why I Made This Project

This is my first project in bioinformatics as a Biotechnology and Computational Biology Undergraduate. The primary goal of this project was to demonstrate my foundational understanding of Python libraries such as Biopython and Pandas by developing a simple tool that performs basic DNA sequence analysis. Through this project, I gained hands-on experience with handling biological sequence data, FASTA file processing, nucleotide analysis, and data organization.

This project showcases my first step into learning computational methods to help solve biological problems and exploring more possibilities through the work of more projects.

# -*- coding: utf-8 -*-
import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

file_path = "sequence.fasta"

try:
    records = list(SeqIO.parse(file_path, "fasta"))
except FileNotFoundError:
    raise SystemExit(f"File not found: {file_path}")

if not records:
    raise SystemExit("No FASTA records found. Is this a valid FASTA file?")

print(f"Loaded {len(records)} sequences from {file_path}")

def analyse_record(record):
    seq = record.seq.upper()
    standard = sum(seq.count(b) for b in "ATGC")
    trimmed = seq[: len(seq) - len(seq) % 3]

    return {
        "id": record.id,
        "description": record.description,
        "length": len(seq),
        "A": seq.count('A'), "T": seq.count('T'),
        "G": seq.count('G'), "C": seq.count('C'),
        "other_bases": len(seq) - standard,
        "gc_percent": round(gc_fraction(seq) * 100, 2),
        "reverse_complement": str(seq.reverse_complement()),
        "protein": str(trimmed.translate()),
    }


results = [analyse_record(r) for r in records]

for r in results:
    print(f"ID: {r['id']}")
    print(f"Description: {r['description']}")
    print(f"Length: {r['length']} bp")
    print(f"Counts  A:{r['A']}  T:{r['T']}  G:{r['G']}  C:{r['C']}  other:{r['other_bases']}")
    print(f"GC content: {r['gc_percent']}%")
    print(f"Reverse complement: {r['reverse_complement']}")
    print(f"Protein: {r['protein']}")
    print("-" * 60)

df = pd.DataFrame(results)[["id", "length", "A", "T", "G", "C", "other_bases", "gc_percent"]]
df


pd.DataFrame(results).to_csv("analysis_results.csv")
print("Saved analysis_results.csv")
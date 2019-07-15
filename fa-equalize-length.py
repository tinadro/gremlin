from Bio import SeqIO
import sys

f = sys.argv[1]
fl = f.split('.')[0]
seq_len = []

for record in SeqIO.parse(f, "fasta"):
	seq_len.append(len(record.seq))

print(max(seq_len))
print(seq_len)
print(len(seq_len))

with open(fl+'-eqlen.fa', 'a+') as f2:
	for record in SeqIO.parse(f, "fasta"):
		if len(record.seq) < max(seq_len):
			n = max(seq_len) - len(record.seq)
			nn = n*'-'
			record.seq = record.seq + nn
		SeqIO.write(record, f2, 'fasta')

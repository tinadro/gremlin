import urllib.parse
import urllib.request
from Bio import SeqIO, Entrez
import pandas as pd
Entrez.email = 'td1515@ic.ac.uk'

def uniprot_ncbi(up_id):
	# get the GI number of the protein from its uniprot accession

	url = 'https://www.uniprot.org/uploadlists/'

	params = {
	'from': 'ACC',
	'to': 'P_GI',
	'format': 'tab',
	'query': up_id
	}

	data = urllib.parse.urlencode(params)
	data = data.encode('utf-8')
	req = urllib.request.Request(url, data)
	with urllib.request.urlopen(req) as f:
	   response = f.read()
	result = response.decode('utf-8')
	uid = result.split(None)[-1]

	# search for the protein in the ncbi database (using GI number), get the species taxid
	handle = Entrez.esummary(db='protein', id=uid, report='full')
	record = Entrez.read(handle)
	handle.close()
	txid = record[0]['TaxId']

	# check if that organism's taxid is a bacterium or not 
	handle = Entrez.efetch(db='taxonomy', id=txid)
	record = Entrez.read(handle)
	handle.close()
	i = False
	for ele in record[0]['LineageEx']:
		for key in ele.keys():
			if ele[key] == '2':
				i = True
	return i 

f = sys.argv[1]
fname = f.split('.')[0]

#with open(f, 'r') as infile, open(fname+'-bacterial.fa', 'a+') as outfile:
for record in SeqIO.parse(f, 'fasta'):
	print(record.id)
	print(record.description)
	print(record.name)

#result = uniprot_ncbi('A0A087M930')


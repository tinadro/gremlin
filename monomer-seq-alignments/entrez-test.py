from Bio import Entrez
Entrez.email = 'td1515@ic.ac.uk'

def tax_summary(uid):
	handle = Entrez.esummary(db='protein', id=uid, report='full')
	record = Entrez.read(handle)
	handle.close()
	return record

rec = tax_summary('674768908')
print(rec[0]['TaxId'])

#def fetch(txid):
#	handle = Entrez.efetch(db='taxonomy', id=txid)
#	record = Entrez.read(handle)
#	handle.close()
#	return record

#tax = fetch('1537915')
#for ele in tax[0]['LineageEx']:
#	for key in ele.keys():
#		if ele[key] == '2':
#			print(ele)

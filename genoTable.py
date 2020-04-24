from __future__ import print_function
import os.path
import csv
import collections

from OrderedDefaultDict import OrderedDefaultDict

class GenoTable():
	'Class for handling genemapper genotype table files'
	
	def __init__(self, input):
		self.g = input
		self.d = OrderedDefaultDict()
		print(self.g)
		
	def readFile(self):
		with open(self.g, 'rb') as f:
			loci=list()
			reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
			for name in reader.fieldnames:
				if name != "Sample Name":
					loci.append(name)
			
			for row in reader:
				for locus in loci:
					#print(row[locus])
					if locus.endswith("-a1"):
						l = locus[:-3]
						self.d[row["Sample Name"]][l]["allele1"] = row[locus]
					if locus.endswith("-a2"):
						l = locus[:-3]
						self.d[row["Sample Name"]][l]["allele2"] = row[locus]
						#print("first allele")
						#self.d[row["Sample Name"]][name] = row[name]
		print(self.d)
		
	def printFile(self, out):
		fh=open(out, "a+")
		for i in self.d.keys():
			#print(i, end='')
			fh.write(i)
			for j in self.d[i].keys():
				for k in self.d[i][j].keys():
					#print("\t", end='')
					fh.write("\t")
					#print(self.d[i][j][k], end='')
					fh.write(self.d[i][j][k])
			#print("\n")
			fh.write("\n")
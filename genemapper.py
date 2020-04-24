from __future__ import print_function
import os.path
import csv
import collections

from OrderedDefaultDict import OrderedDefaultDict

class GeneMapper():
	'Class for handling genemapper genotype table files'
	
	def __init__(self, input):
		self.f = input
		#self.d = collections.defaultdict(dict)
		self.d = OrderedDefaultDict()
		self.dh = collections.OrderedDict()
		self.cd = collections.OrderedDict() #dict to hold counts of comparisons
		print(self.f)
		

	def readFile(self):
		with open(self.f, 'rb') as f:
			reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
			#print(reader.fieldnames)
			#for name in reader.fieldnames:
				#print(name)
			for row in reader:
				#self.d[row["Sample Name"]][row["Marker"]] = row["Allele 1"]
				self.d[row["Sample Name"]][row["Marker"]]["allele1"] = row["Allele 1"]
				self.d[row["Sample Name"]][row["Marker"]]["allele2"] = row["Allele 2"]
				self.dh[row["Marker"]]=0
		#print(self.d)
		
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
	
	def printHeader(self, out):
		fh=open(out, "w+")
		fh.write("Sample")
		for i in self.dh.keys():
			fh.write("\t")
			fh.write(i)
			fh.write("-a1")
			fh.write("\t")
			fh.write(i)
			fh.write("-a2")
		fh.write("\n")
			
	def compare(self, gtd):
		for i in self.d.keys():
			if i in gtd.keys():
				self.cd[i]=0 #add to comparison dict
				for j in self.d[i].keys():
					for k in self.d[i][j].keys():
						if self.d[i][j][k] == "":
							## fill this space from genotype table dict (gtd) if possible
							print([j], " is empty")
						else:
							if gtd[i][j][k] != "":
								if self.d[i][j][k] != gtd[i][j][k]:
									self.cd[i]+=1 #increment number of conflicts
									print("conflict at ", j, " for ", i)
				print(i, " present.")
			else:
				print(i, " not present.")
		#print(self.cd)
		
	def printComparison(self, gtd, out):
		fh=open(out, "a+")
		for i in self.cd.keys():
			if self.cd[i] > 0:
				fh.write("rerun")
				fh.write("\t")
				fh.write(i)
				for j in self.d[i].keys():
					for k in self.d[i][j].keys():
						fh.write("\t")
						fh.write(self.d[i][j][k])
				fh.write("\n")
				fh.write("original")
				fh.write("\t")
				fh.write(i)
				for l in gtd[i].keys():
					for m in gtd[i][l].keys():
						fh.write("\t")
						fh.write(gtd[i][l][m])
				fh.write("\n")
				
	def correct(self, gtd, bl):
		bld=dict()
		with open(bl) as f:
			for line in f:
				samp=line.rstrip()
				bld[samp]=0
		print(bld)
		
		for i in self.d.keys():
			if i in gtd.keys():
				if i not in bld.keys():
					for j in self.d[i].keys():
						for k in self.d[i][j].keys():
							if gtd[i][j][k] == "":
								## fill genotype table dict (gtd)
								gtd[i][j][k] = self.d[i][j][k]
				else:
					print(i)
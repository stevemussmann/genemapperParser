import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser.add_argument("-f", "--file",
							dest='file',
							required=True,
							help="Specify a file for input."
		)
		parser.add_argument("-o", "--out",
							dest='out',
							default="output.txt",
							help="Specify an output file name."
		)
		parser.add_argument("-g", "--geno",
							dest='geno',
							default="noname",
							help="Specify a genotype table for input."
		)
		parser.add_argument("-b", "--blacklist",
							dest='black',
							default="noname",
							help="Specify a text file containing samples that will be ignored in QAQC or reruns."
		)
		self.args = parser.parse_args()

		#check if files exist
		self.exists( self.args.file )



	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print(filename, "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
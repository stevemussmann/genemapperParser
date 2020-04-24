#!/usr/bin/env python3
from __future__ import print_function

from comline import ComLine
from genemapper import GeneMapper
from genoTable import GenoTable

import sys

def main():
	input = ComLine(sys.argv[1:])
	
	gm = GeneMapper(input.args.file)
	gm.readFile()
	gm.printHeader(input.args.out)
	gm.printFile(input.args.out)
	
	if input.args.geno != "noname":
		gt = GenoTable(input.args.geno)
		gt.readFile()
		gm.compare(gt.d)
		gm.printHeader("comparison.txt")
		gm.printComparison(gt.d,"comparison.txt")
		gm.correct(gt.d,input.args.black)
		gm.printHeader("corrected.txt")
		gt.printFile("corrected.txt")

	

main()

raise SystemExit
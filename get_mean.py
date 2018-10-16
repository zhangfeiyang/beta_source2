#!/usr/bin/env python

from ROOT import *
import sys
cut = sys.argv[1]

file = open('data_'+cut,'w')

f = TFile('naked/final.root','read')
t = f.Get('t0')
t.Draw('totalPE>>h(200,700,3500)','totalPE>'+cut)
h = gDirectory.Get('h')
mean0 = h.GetMean()

data = {} 

for s in ['Mo','Ti']:
	for d in ['10','50','100']:
		for th in ["0.1","0.5","1"]:
			t = TChain('evt')
			t.Add(d+'_'+th+'/'+s+'/evt*')
			t.Draw('totalPE>>h(200,700,3500)','totalPE>'+cut)
			h = gDirectory.Get('h')
			mean = h.GetMean()
			emean = h.GetMeanError()
			bias = (mean/mean0-1)*100
			ebias = (emean/mean0)*100
			data[d+th+s] = bias
			#file.write(str(bias)+'\t'+str(ebias)+'\n')
			file.write(str(bias)+'\t')
	file.write('\n')
file.close()


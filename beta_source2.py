#!/usr/bin/python
import sys
import os
import time
import random
import math
first = sys.argv[1]
last = sys.argv[2]
pi = 3.141592654
emass = 0.5109989
for run in range(int(first),int(last)):
	seed = int(random.uniform(1,2))
	material = random.choice(['Mo','Ti'])
	thickness = random.choice([0.5,1,0.1])
	diameter = random.choice([10,50,100]) 
	if seed == 0:
		cmd = "python tut_detsim.py --no-anamgr-interesting-process --no-gdml  --evtmax "+str(1000)+" --seed "+str(523*run)+" --user-output /junofs/production/public/users/zhangfy/non-uniform/offline_J17v1r1-Pre1/Examples/Tutorial/share/beta_source2/naked/evt_"+str(run)+".root gendecay --nuclear Sr90 --global-position 0 0 0\n"
	else:
		cmd = "python tut_detsim.py --no-anamgr-interesting-process --source_material "+str(material)+" --UseNeedle --thickness "+str(thickness)+" --diameter "+str(diameter)+" --no-gdml  --evtmax "+str(1000)+" --seed "+str(383*run)+" --user-output /junofs/production/public/users/zhangfy/non-uniform/offline_J17v1r1-Pre1/Examples/Tutorial/share/beta_source2/"+str(diameter)+"_"+str(thickness)+"/"+str(material)+"/evt_"+str(run)+".root gendecay --nuclear Sr90 --volume pSr --material strontium\n"

		#cmd = "python tut_detsim.py --no-anamgr-interesting-process --UseNeedle --no-gdml  --evtmax "+str(1000)+" --seed "+str(383*run)+" --user-output /junofs/production/public/users/zhangfy/non-uniform/offline_J17v1r1-Pre1/Examples/Tutorial/share/beta_source2/needle/evt_"+str(run)+".root gendecay --nuclear Sr90 --volume pLS\n"
		#cmd = "python tut_detsim.py --no-anamgr-interesting-process --UseBoard --no-gdml  --evtmax "+str(500)+" --seed "+str(52322383*run)+" --user-output /junofs/production/public/users/zhangfy/non-uniform/offline_J17v1r1-Pre1/Examples/Tutorial/share/beta_source2/board/evt_"+str(run)+".root gendecay --nuclear Sr90 --global-position 0 0 0\n"
		#cmd = "python tut_detsim.py --no-anamgr-interesting-process --UseContainer --no-gdml  --evtmax "+str(1000)+" --seed "+str(52322383*run)+" --user-output /junofs/production/public/users/zhangfy/non-uniform/offline_J17v1r1-Pre1/Examples/Tutorial/share/beta_source2/container/evt_"+str(run)+".root gendecay --volume pTarget --volume-radius-max 25\n"
 
	cmdfilename = "condor/sim_"+str(run)+".sh"
	cmdfile = open(cmdfilename,"w")
	cmdfile.write("#!/bin/bash\n")
	cmdfile.write("source /junofs/production/public/users/zhangfy/non-uniform/offline_J17v1r1-Pre1/junoenv\n")
	cmdfile.write("source $WORKTOP/Examples/Tutorial/cmt/setup.sh\n")
	cmdfile.write("cd /junofs/production/public/users/zhangfy/non-uniform/offline_J17v1r1-Pre1/Examples/Tutorial/share/\n")
	cmdfile.write(cmd)
	cmdfile.close()
	os.chmod(cmdfilename,0775)
	
	cmd  = "hep_sub "+str(cmdfilename)
	os.system(cmd)
	run = run + 1

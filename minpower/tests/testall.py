<<<<<<< HEAD
<<<<<<< HEAD
""" 
Testing for minpower development. 
Runs solve.problem() on all directories in ./tests
These tests include ED,OPF,UC tests designed to ensure that
inputs parse correctly, constraints are active, 
and vizualizations and solution output work.

Chances are good that if you make major modifications 
to the minpower code you will break something here. 
Just fix it before you push your change.
"""

import sys,os,glob,traceback,logging
from minpower import config
from minpower.commonscripts import joindir,splitFilename

def wipeTestSlate(dir):
    patterns=['*.png','*.lp','commitment.csv','dispatch.csv','error.txt']
    for pat in patterns:
        for f in glob.glob(joindir(dir,pat)): os.remove(f)
def hasPyscript(dir): return glob.glob(joindir(dir,'*.py'))

def main(solver=config.optimization_solver):
    logging.basicConfig(level=logging.CRITICAL, format='%(levelname)s: %(message)s')
    from minpower import solve
    
    dirNm=splitFilename(__file__)[0]
    excludeL=['coding','doctesting','ucRollingYear']
    for fileNm in os.listdir(dirNm):
        if fileNm in excludeL: continue
        testDir = joindir(dirNm, fileNm)
        if not os.path.isdir(testDir): continue
        print 'testing: ',fileNm
        wipeTestSlate(testDir)
        fResults=open(joindir(testDir,'results.txt'),'w+')
        fError=open(joindir(testDir,'error.txt'),'w+')
        sys.stdout=fResults #switch output to results file 
        if hasPyscript(testDir):
            sys.stdout = sys.__stdout__ #switch back to standard outputting
            os.system('python {s}'.format(s=hasPyscript(testDir)[0]))
        else:
            try: 
<<<<<<< HEAD:minpower/tests/testall.py
                solve.problem(datadir=testDir,solver=solver)
=======
                solve.problem(datadir=testDir)
>>>>>>> changed call to solve.problem:minpower/tests/all.py
                sys.stdout = sys.__stdout__ #switch back to standard outputting
                fError.close()
                os.remove(joindir(testDir,'error.txt'))
            except: #write the error to file
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_tb(exc_traceback, file=fError )
                traceback.print_exception(exc_type, exc_value, exc_traceback, file=fError)
                sys.stdout = sys.__stdout__ #switch back to standard outputting
                print '\t had error' #note that this dir produced error
    else: 
        sys.stdout = sys.__stdout__ #switch back to standard outputting

if __name__ == "__main__": main()
=======
=======
"""
Run all of the unit tests in  
    :mod:`tests.solvers`,
    :mod:`tests.generators`,
    :mod:`tests.unit_commitment`,
    :mod:`tests.opf`, and
    :mod:`tests.bidding`
    
Most unit tests are designed to ensure that a single constraint is working.  
This module uses the Attest package testing framework.
"""

>>>>>>> documentation
from attest import Tests
import logging
logging.basicConfig( level=logging.CRITICAL, format='%(levelname)s: %(message)s')
if __name__ == "__main__": 
    all_tests=Tests([
    'solvers.solvers',
    'generators.generation',
    'unit_commitment.uc',
    'opf.opf',
    'bidding.bidding'
    ])
<<<<<<< HEAD

if __name__ == "__main__": all_tests.run()
>>>>>>> run all tests
=======
    all_tests.run()
>>>>>>> documentation

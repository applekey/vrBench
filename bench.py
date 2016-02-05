import subprocess,os

def resultStruct:
    def __init__(self):
        ## need to fill these in
        self.dataset = ''
        self.filter =''
        self.time = 0
        self.schedule=''
        self.blocksize = 0
        self.dateTestRun = ''

def config:
    def __init__(self):
        self.iterations = 0
        self.filterStep = ''
        self.programArgs

def runTest(fullPath,config):

    totalRunTime = 0
    for i in range(config.iterations):  
        runOutput = subprocess.check_output([fullPath, config.programArgs])
        location = runOutput.find(config.filterStep)

        if location == -1:
            print runOutput
            raise


        runOutput = runOutput[location:]

        location = runOutput.find('RUNTIME: ')
        runOutput = runOutput[location:]

        ## now find the end, which is pass
        location = runOutput.find(' ')
        runTime = runOutput[:location] 
        runTime = float(runTime)
        totalRunTime +=runTime

    totalRunTime = totalRunTime/config.iterations

        

def recordResult(resultFile,resultstruct):
    pass


vrPath = '/home/users/applekey/roba/eavl/EAVL-rayTracer/test'
programName = 'testvolume'
fullPath = os.path.join(vrPath,programName)
print fullPath

programArgs = ''



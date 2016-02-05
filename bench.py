import subprocess,os,io,csv,datetime

class vrconfig:
    def __init__(self):
        self.dataset = ' '
        self.filter =' '
        self.schedule=' '
        self.blocksize = 0
        self.dateTestRun = ' '
        self.iterations = 0
        self.filterStep = ' '
        self.programArgs=' '
        self.resultFile = ' '
        self.fullPath = ' '

def runTest(config):

    totalRunTime = 0
    for i in range(config.iterations):  
        runOutput = subprocess.check_output([config.fullPath, config.programArgs])
        location = runOutput.find(config.filterStep)

        if location == -1:
            print runOutput
            raise


        runOutput = runOutput[location + len(config.filterStep):]

        ## now find the end, which is pass
        location = runOutput.find(' ')
        runTime = runOutput[:location] 
        runTime = float(runTime)
        totalRunTime +=runTime

    totalRunTime = totalRunTime/config.iterations
    ##record the results
    recordResult(config,totalRunTime)

        

def recordResult(config,totalRunTime):
    c = config
    line = [c.dataset, c.iterations, c.schedule, c.blocksize, totalRunTime,c.dateTestRun,c.programArgs]
    print line
    with open(c.resultFile, 'a') as file:
        ww = csv.writer(file, delimiter=',')
        ww.writerow(line)


#####################################################################################################
vrPath = '/home/users/applekey/roba/eavl/EAVL-rayTracer/test'
programName = 'testvolume'
resultFile = 'result.csv'
fullPath = os.path.join(vrPath,programName)
fullPathResult = os.path.join(vrPath,resultFile)
print fullPath

#####################################################################################################
config = vrconfig()
config.dataset = 'enzo'
config.iterations = 5
config.filterStep ='Sample      RUNTIME: '
config.programArgs=' '
config.dateTestRun = unicode(datetime.datetime.now().replace(microsecond=0))
config.fullPath = fullPath
config.resultFile = fullPathResult
#####################################################################################################

config.programArgs = "OMP_SCHEDULE=dynamic"
config.schedule = 'dynamic'
runTest(config)

config.programArgs = "OMP_SCHEDULE=static"
config.schedule = 'static'
runTest(config)

config.programArgs = "OMP_SCHEDULE=guided"
config.schedule = 'guided'
runTest(config)

config.programArgs = "OMP_SCHEDULE=auto"
config.schedule = 'auto'
runTest(config)

## try static different sizes
blockStart = 0
blockEnd = 10000
stepSize = 1000

curSize = blockStart
while curSize<blockEnd:

    config.programArgs = "OMP_SCHEDULE=static,"+str(curSize)
    #os.environ["OMP_SCHEDULE"] = "static , " + str(curSize)
    config.schedule = 'static' + str(curSize)
    runTest(config)

    curSize += stepSize

blockStart = 0
blockEnd = 10000
stepSize = 1000

curSize = blockStart
while curSize<blockEnd:

    config.programArgs = "OMP_SCHEDULE=dynamic,"+str(curSize)
    #os.environ["OMP_SCHEDULE"] = "dynamic , " + str(curSize)
    config.schedule = 'dynamic' + str(curSize)
    runTest(config)

    curSize += stepSize



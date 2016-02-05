import subprocess,os,io,csv,datetime,sys

class vrconfig:
    def __init__(self):
        self.dataset = ' '
        self.filter =' '
        self.schedule=' '
        self.scheduleName= ''
        self.blocksize = 0
        self.dateTestRun = ' '
        self.iterations = 0
        self.filterStep = ' '
        self.programArgs=' '
        self.resultFile = ' '
        self.fullPath = ' '
        self.cores = 0

def runTest(config):

    totalRunTime = 0
    for i in range(config.iterations):  
        runArgs = [config.fullPath]
        runArgs +=config.programArgs
        #print runArgs

        runOutput = subprocess.check_output(runArgs)
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
    line = [c.dataset, c.iterations, c.schedule, c.cores, c.blocksize, totalRunTime,c.dateTestRun,c.programArgs]
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
config.iterations = 3
config.filterStep ='Sample      RUNTIME: '
config.programArgs=' '
config.dateTestRun = unicode(datetime.datetime.now().replace(microsecond=0))
config.fullPath = fullPath
config.resultFile = fullPathResult

#####################################################################################################

# case 1:
#     omp_set_schedule(omp_sched_static, atoi(argv[3]));
#     break;
# case 2:
#     omp_set_schedule(omp_sched_auto, atoi(argv[3]));
#     break;
# case 3:
#     omp_set_schedule(omp_sched_dynamic, atoi(argv[3]));
#     break;
# case 4:
#     omp_set_schedule(omp_sched_guided, atoi(argv[3]));
#     break;

for i in range(1,16+1):
    config.cores = i
    config.schedule = 1
    config.programArgs = [str(config.cores),str(config.schedule),str(config.blocksize)]
    config.scheduleName = 'static'
    runTest(config)

for i in range(1,16+1):
    config.cores = i
    config.schedule = 3
    config.programArgs = [str(config.cores),str(config.schedule),str(config.blocksize)]
    config.scheduleName = 'dynamic'
    runTest(config)

for i in range(1,16+1):
    config.cores = i
    config.schedule = 4
    config.programArgs = [str(config.cores),str(config.schedule),str(config.blocksize)]
    config.scheduleName = 'guided'
    runTest(config)

for i in range(1,16+1):
    config.cores = i
    config.schedule = 2
    config.programArgs = [str(config.cores),str(config.schedule),str(config.blocksize)]
    config.scheduleName = 'auto'
    runTest(config)

sys.exit() ## stop here

## try static different sizes

config.cores = 16 ##use 16 threads

blockStart = 0
blockEnd = 3000
stepSize = 300

curSize = blockStart
while curSize<blockEnd:
    config.schedule = 1
    config.blocksize = str(curSize)
    config.programArgs = [str(config.cores),str(config.schedule),str(config.blocksize)]
    config.scheduleName = 'static' + str(curSize)
    runTest(config)

    curSize += stepSize

blockStart = 0
blockEnd = 3000
stepSize = 300

curSize = blockStart
while curSize<blockEnd:
    config.schedule = 3
    config.blocksize = str(curSize)
    config.programArgs = [str(config.cores),str(config.schedule),str(config.blocksize)]
    config.scheduleName = 'dynamic' + str(curSize)
    runTest(config)

    curSize += stepSize



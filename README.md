<h3> splice this into testvolume.cpp main, for some reason, openmp doesnt respect env vars </h3>
<pre><code>
int main(int argc, char *argv[])
{   

    omp_set_num_threads(atoi(argv[1]));
    std::cerr<<"threads: "<<atoi(argv[1])<<std::endl;
    
    std::cerr<<"chunk: "<<atoi(argv[3])<<std::endl;
    switch(atoi(argv[2])) {
        case 1:
            omp_set_schedule(omp_sched_static, atoi(argv[3]));
            std::cerr<<"omp_sched_static: "<<atoi(argv[2])<<std::endl;
            break;
        case 2:
            omp_set_schedule(omp_sched_auto, atoi(argv[3]));
            std::cerr<<"omp_sched_auto: "<<atoi(argv[2])<<std::endl;
            break;
        case 3:
            omp_set_schedule(omp_sched_dynamic, atoi(argv[3]));
            std::cerr<<"omp_sched_dynamic: "<<atoi(argv[2])<<std::endl;
            break;
        case 4:
            omp_set_schedule(omp_sched_guided, atoi(argv[3]));
            std::cerr<<"omp_sched_guided: "<<atoi(argv[2])<<std::endl;
            break;
        default:
            throw "invalid";
    }

    try

    { 

</code></pre>



<h3>This is where you set the program name/ result csv </h3>

<pre><code>
#####################################################################################################
vrPath = '/home/users/applekey/roba/eavl/EAVL-rayTracer/test'
programName = 'testvolume'
resultFile = 'result.csv'
fullPath = os.path.join(vrPath,programName)
fullPathResult = os.path.join(vrPath,resultFile)
print fullPath
</code></pre>

<h3>This is where the config options are, the ones that matter are iterations and programs args, the rest such as
dataset are just for bookkeeeping... </h3>
<pre><code>
#####################################################################################################
config = vrconfig()
config.dataset = 'enzo'
config.iterations = 2
config.filterStep ='Sample      RUNTIME: '
config.programArgs=' '
config.dateTestRun = unicode(datetime.datetime.now().replace(microsecond=0))
config.fullPath = fullPath
config.resultFile = fullPathResult
#####################################################################################################
</code></pre>


enviornment vars here
https://msdn.microsoft.com/en-us/library/wxdty0df.aspx

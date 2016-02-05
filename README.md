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

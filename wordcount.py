# %%file is an Ipython magic function that saves the code cell as a file
import mrjob
from mrjob.job import MRJob
class MRsongCount(MRJob):
    def mapper(self,_,song):
        yield(song,1)
        
    def reducer(self,key,value):
        yield(key,sum(value))

if __name__ == "__main__":
    MRsongCount.run()
 
from multiprocessing import Process
import time


# the method wich we want to be multi processed
def zeigen(z,delay):
    print(f"starting {z}")
    time.sleep(delay)
    print(f"ending {z}")
#multi processing by a class
class doZeigen(Process):
    def __init__(self, z, delay):
        super().__init__()
        self.z = z
        self.delay = delay

    def run(self):
        zeigen(self.z, self.delay)


def main():
    start=time.perf_counter()
#multiprocessing by method
    p1=Process(target=zeigen,args=("eins",2),name="first process !")
    p2=Process(target=zeigen,args=("zwei",4),name="second process !")

    p1.start()
    p2.start()

    p1.join()
    p2.join()
#ending by method

    #starting by class
    p11=doZeigen("one !",2)
    p22=doZeigen("two !",4)

    p11.start()
    p22.start()

    p11.join()
    p22.join()

#end by class

    end=time.perf_counter()

    print(f"delay is {end-start}")

if __name__=="__main__":
    main()





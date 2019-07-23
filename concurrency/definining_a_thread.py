import threading


def function(i):
    print("function called by thread {}\n".format(i))
    return


threads = []
for i in range(5):
    # Instantiate a thread
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    # Start running thread
    t.start()
    # Makes the calling thread wait until the thread has finished the execution
    t.join()

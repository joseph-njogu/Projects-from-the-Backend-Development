import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting {} \n".format(name))
    time.sleep(3)
    print("Exiting {} \n".format(name))


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='foo_process', target=foo)
    # Executing process in background
    process_with_name.daemon = True
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()

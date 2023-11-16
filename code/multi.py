from multiprocessing import Process, Queue
from jproperties import Properties
import requests
from functools import wraps
import time

'''
def do_work(start, end, result):
    sum = 0
    for i in range(int(start), int(end)):
        sum += i
    result.put(sum)
    return

if __name__ == "__main__":
    START, END = 0, 20000000
    result = Queue()
    pr1 = Process(target=do_work, args=(START, END/2, result))
    pr2 = Process(target=do_work, args=(END/2, END, result))
    pr1.start()
    pr2.start()
    pr1.join()
    pr2.join()
    result.put('STOP')
    sum = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP': break
        else: sum += tmp

    print("Result : ", sum)
'''

configs = Properties()
with open('./resource/application.properties', 'rb') as config_file:
    configs.load(config_file)

upbitKey = configs.get('UPBIT_KEY').data
upbitSecret = configs.get('UPBIT_SECRET').data

UPBIT_HOST = 'https://api.upbit.com'

def processA(result):
    url = UPBIT_HOST + '/v1/ticker'
    headers = {"accept": "application/json"}
    params = {"markets": ['KRW-BTC']}
    response = requests.get(url, params=params, headers=headers)
    result.append(response.json())

def processB(result):
    url = UPBIT_HOST + '/v1/ticker'
    headers = {"accept": "application/json"}
    params = {"markets": ['KRW-SOL']}
    response = requests.get(url, params=params, headers=headers)
    result.append(response.json())


def timer(func):
    """helper function to estimate view execution time"""
    @wraps(func)  # used for copying func metadata
    def wrapper(*args, **kwargs):
        # record start time
        start = time.time()

        # func execution
        result = func(*args, **kwargs)

        duration = (time.time() - start) * 1000
        # output execution time to console
        print('{} takes {:.2f} ms'.format(
            func.__name__,
            duration
        ))
        return result

    return wrapper

@timer
def run():
    result = []

    prA = Process(target=processA(result))
    prB = Process(target=processB(result))
    prA.start()
    prB.start()
    prA.join()
    prB.join()

    print(result)

if __name__ == "__main__":
    run()


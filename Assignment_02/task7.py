# Justin Williams
# Assignment 02
# EPD 455: Python for Applications in Engineering
# 2022-09-25
#
# Problem 7:
# 7. Write a python script that measures the execution time of two for loops given below using the timeit module, time.perf counter and time.process time. For the timeit module, repeat the timing test 1000 times.
#    (a) for i = 0 to 5000, compute (i**2)/21.3
#    (b) for i = 0 to 5000, compute (i**2)/32
#    Explain what you observe and submit the python script task7.py on canvas.
#

import timeit
from time import perf_counter
from time import process_time

func1= '''def func1():
    for i in range(5001):
        trash = (i**2)/21.3'''
        
def func1():
    for i in range(5001):
        trash = (i**2)/21.3

func2 = '''def func2():
    for i in range(5001):
        trash = (i**2)/32'''
        
def func2():
    for i in range(5001):
        trash = (i**2)/32

        
number_itr = 5000
time_timeit_func1 = timeit.timeit(stmt=func1,number=number_itr)
print("timeit module func1 takes about: ", time_timeit_func1/number_itr)
time_timeit_func2 = timeit.timeit(stmt=func2,number=number_itr)
print("timeit module func2 takes about: ", time_timeit_func2/number_itr) 

t0 = perf_counter()
func1()
t1 = perf_counter()
time_perf_counter_func1 = t1-t0
print('perf_counter func1 takes about: ', time_perf_counter_func1)

t0 = perf_counter()
func2()
t1 = perf_counter()
time_perf_counter_func2 = t1-t0
print('perf_counter func2 takes about: ', time_perf_counter_func2)

t0 = process_time()
func1()
t1 = process_time()
time_process_time_func1 = t1-t0
print("process_time func1 takes about: ", time_process_time_func1)

t0 = process_time()
func2()
t1 = process_time()
time_process_time_func2= t1-t0
print("process_time func1 takes about: ", time_process_time_func2)

#
# was getting results of:
#
# timeit module func1 takes about:  0.0009168764903016706
# timeit module func2 takes about:  0.0008573243967230204
# perf_counter func1 takes about:  0.0008601640001870692
# perf_counter func2 takes about:  0.0008219690062105656
# process_time func1 takes about:  0.0008569740000439197
# process_time func1 takes about:  0.0008225120000133757
#
# overall, very similar times.

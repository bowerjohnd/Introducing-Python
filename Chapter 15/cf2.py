from concurrent import futures
import math
import time
import sys

def calc(val) :
	result = math.sqrt(float(val))
	return val, result

def use_threads(num, values) :
	with futures.ThreadPoolExecutor(num) as tex :
		tasks = [tex.submit(calc, value) for value in values]
		for f in futures.as_completed(tasks) :
			yield f.result()

def use_processes(num, values) :
	with futures.ProcessPoolExecutor(num) as pex :
		tasks = [pex.submit(calc, value) for value in values]
		for f in futures.as_completed(tasks) :
			yield f.result()

def main(workers, values) :
	print(f"Using {workers} workers for {len(values)} values")
	print("Using threads:")
	for val, result in use_threads(workers, values) :
		print(f'{val} {result:.4f}')
	print("Using processes:")
	for val, result in use_processes(workers, values) :
		print(f'{val} {result:.4f}')

if __name__ == '__main__' :
	workers = 3
	if len(sys.argv) > 1 :
		workers = int(sys.argv[1])
	values = list(range(1, 6)) # 1 .. 5
	main(workers, values)

# lines 36, line 25 ... TypeError: cannot unpack non-iterable float object	
# f.result() returns float, i believe functions require 2 return values
#	- removed {val} from both print(f.. in main, works now, though worker not shown
#		. need worker # to return from yield statement
#	*** missing return val in calc funtion *** fixed now, program works as intended
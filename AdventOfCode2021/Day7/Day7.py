from collections import Counter 
import statistics 
import math

def remove_group(d,key):
    return {k: v for k,v in d.items() if k !=key}

def natural_sum(x):
    return x*(x+1)/2


list_of_subs=[]

with open("AdventOfCode2021\Day7\Input\Input7.txt","r") as input_file:
    for input_line in input_file:
        list_of_subs = list(map(int, input_line.split(',')))

#throw these into a dictionary
sub_groups=Counter(list_of_subs)

min_fuel = 10000000000

sub_mean = statistics.mean(list_of_subs)
sub_dev = statistics.stdev(list_of_subs)

low_X = math.floor(sub_mean-sub_dev)
if low_X < min(list_of_subs):
    low_X = min(list_of_subs)
high_X = math.ceil(sub_mean+sub_dev)
if high_X > max(list_of_subs):
    high_X = max(list_of_subs)


for i in range(low_X,high_X):
    move_us = remove_group(sub_groups, i)
    total_fuel_used = sum([abs(i-k)*v for k, v in move_us.items()])
    if total_fuel_used <= min_fuel:
        min_fuel = total_fuel_used
    
print(min_fuel)

#part deux

min_fuel2 = 100000000000000000
for i in range(low_X,high_X):
    move_us = remove_group(sub_groups, i)
    tot_fuel_used = sum([natural_sum(abs(i-k))*v for k, v in move_us.items()])
    if tot_fuel_used <= min_fuel2:
        min_fuel2 = tot_fuel_used
    
print(min_fuel2)
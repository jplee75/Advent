import functools
#Let us see how bad I can jack this up
input_file = open(".\Input\Input1.txt","r")
input_list = list(map(int, input_file.read().splitlines()))

increase_increment = 0
input_list_iterable = iter(input_list)

increase = functools.reduce(lambda acc,i:acc+int(input_list[i]>input_list[i-3]),range(3,len(input_list)-2),0)
the_tim_way = sum([input_list[a]>input_list[a-1] for a in range(1,len(input_list))])

the_tim_way_partDeux = sum([sum(input_list[a:a+2])>sum(input_list[a-2:a]) for a in range(3,len(input_list)-2)])

print(the_tim_way_partDeux)
print(increase)
#while True:
#        try:
#            current=next(input_list_iterable)
#            if current>previous and previous != -1:
#                increase_increment += 1
#            previous = current
#        except StopIteration:
#            break


import datetime

class lantern_fish:
    def __init__(self,age,existing_count,new_spawn_count):
        self.age=age
        self.existing_count = existing_count
        self.new_spawn_count=new_spawn_count

all_the_fish=[lantern_fish(i,0,0) for i in range(9)]
max_days = 256

with open("AdventOfCode2021\Day6\Input\Input6.txt","r") as input_file:
    for input_line in input_file:
        for each_fish in input_line.split(","):
            all_the_fish[int(each_fish)].existing_count +=1

generation_spawned=0
for each_day in range(1,max_days+1):
    print("Day " + str(each_day) + "  Current Time : " + str(datetime.datetime.now()))
    for f in range(len(all_the_fish)):
        if f == 0: 
            generation_spawned = all_the_fish[f].existing_count
        elif f >=7:
            all_the_fish[f-1].new_spawn_count = all_the_fish[f].new_spawn_count
        elif f == 6:
            all_the_fish[f-1].existing_count = all_the_fish[f].existing_count+all_the_fish[f].new_spawn_count
            all_the_fish[f].existing_count = generation_spawned
        else:
            all_the_fish[f-1].existing_count = all_the_fish[f].existing_count

    all_the_fish[8].new_spawn_count = generation_spawned
    generation_spawned = 0

    #for group in all_the_fish:
    #    print(str(group.age)+":" + str(group.existing_count) + ":" + str(group.new_spawn_count))
    #for i in range(len(print_list)):
    #    for j in range(len(print_list[i])):
    #        print(print_list[i][j].age,end=",")
    #print(f"\n")

total_fish = sum([(fish_group.existing_count+fish_group.new_spawn_count) for fish_group in all_the_fish])
print(total_fish)

#part 2 okay time to get smart about this
#list[[age,count]]
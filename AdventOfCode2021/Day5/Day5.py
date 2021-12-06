class jp_line:
    def __init__(self,x1,y1,x2,y2):
            self.x1=x1
            self.y1=y1
            self.x2=x2
            self.y2=y2

    @property
    def smallX(self):
        return int(min(self.x1,self.x2))
    @property
    def bigX(self):
        return int(max(self.x1,self.x2))
    @property
    def smallY(self):
        return int(min(self.y1,self.y2))
    @property
    def bigY(self):
        return int(max(self.y1,self.y2))

jp_vent_grid = [[0]*1000 for i in range(1000)]
all_the_lines = []
with open("AdventOfCode2021\Day5\Input\Input5.txt","r") as input_file:
    for input_line in input_file:
        line = input_line.rstrip()
        start = line.split('->')[0].strip()
        end = line.split('->')[1].strip()
        all_the_lines.append(jp_line(int(start.split(',')[0]),int(start.split(',')[1]),int(end.split(',')[0]),int(end.split(',')[1])))

#print(all_the_lines)

for vent_line  in all_the_lines:
    #only do stuff on horizontal and verticals
    if vent_line.x1 == vent_line.x2 or vent_line.y1==vent_line.y2:
        for x in range(vent_line.smallX,vent_line.bigX+1):
            for y in range(vent_line.smallY,vent_line.bigY+1):
                jp_vent_grid[x][y]=jp_vent_grid[x][y]+1
    #Diagonal Lines now too
    else:
        if vent_line.y1 < vent_line.y2 and vent_line.x1 > vent_line.x2:
            for i in range(0,(vent_line.y2-vent_line.y1)+1):
                x = vent_line.x1 - i
                y = vent_line.y1 + i
                jp_vent_grid[x][y]=jp_vent_grid[x][y]+1
        if vent_line.y1 < vent_line.y2 and vent_line.x1 < vent_line.x2:
            for i in range(0,(vent_line.y2-vent_line.y1)+1):
                x = vent_line.x1 + i
                y = vent_line.y1 + i
                jp_vent_grid[x][y]=jp_vent_grid[x][y]+1
        if vent_line.y1 > vent_line.y2 and vent_line.x1 > vent_line.x2:
            for i in range(0,(vent_line.y1-vent_line.y2)+1):
                x = vent_line.x1 - i
                y = vent_line.y1 - i
                jp_vent_grid[x][y]=jp_vent_grid[x][y]+1
        if vent_line.y1 > vent_line.y2 and vent_line.x1 < vent_line.x2:
            for i in range(0,(vent_line.y1-vent_line.y2)+1):
                x = vent_line.x1 + i
                y = vent_line.y1 - i
                jp_vent_grid[x][y]=jp_vent_grid[x][y]+1                
#print(jp_vent_grid)
#flatten grid
flat_list = [x for row in jp_vent_grid for x in row]
two_or_greater_points = sum(map(lambda x: x>=2,flat_list))
print(two_or_greater_points)
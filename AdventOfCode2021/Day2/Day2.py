class submarineCommands:
        def __init__(self,course,velocity):
            self.course=course
            self.velocity=velocity

#horizontal
currentX=0
#depth
currentY=0
#List of commands
command_list = []
#input_file = open(".\Input\Input2.txt","r")
with open(".\Input\Input2.txt","r") as input_file:
    while (line := input_file.readline().rstrip()):
        command_list.append(submarineCommands(line.split()[0],int(line.split()[1])))

for obj in command_list:
    if obj.course =='down':
        currentY += obj.velocity
    elif obj.course == 'up':
        currentY -= obj.velocity
    elif obj.course == 'forward':
        currentX += obj.velocity
    else:
        print('Something is wrong stop stop ABORT ABORT')

print(currentX*currentY)

currentAim = 0
currentHorizontal=0
currentDepth=0
#part 2
for obj in command_list:
    if obj.course =='down':
        currentAim += obj.velocity
    elif obj.course == 'up':
        currentAim -= obj.velocity
    elif obj.course == 'forward':
        currentHorizontal += obj.velocity
        currentDepth += (currentAim*obj.velocity)
    else:
        print('Something is wrong stop stop ABORT ABORT')

print(currentHorizontal*currentDepth)
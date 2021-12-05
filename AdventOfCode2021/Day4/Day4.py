class bingoNumber:
        def __init__(self,bingo_value,is_marked):
            self.bingo_value=bingo_value
            self.is_marked=is_marked

def Is_Winner(check_this_board):
    win = False
    #horizontal check
    for y in range(5):
        bingo_mark_count=0
        for x in range(5):
            if check_this_board[y][x].is_marked:
                bingo_mark_count+=1
        if bingo_mark_count == 5:
            win=True
            break
        if win:
            break
    
    #vertical check
    for x in range(5):
        bingo_mark_count=0
        for y in range(5):
            if check_this_board[y][x].is_marked:
                bingo_mark_count+=1
        if bingo_mark_count == 5:
            win=True
            break
        if win:
            break

    return win

numbers_called =[]
is_first=True
bingo_cards=[]
new_card = True
board_count = -1 
with open("AdventOfCode2021\Day4\Input\Input4.txt","r") as input_file:
    for input_line in input_file:
        line = input_line.rstrip()
        #blank lines ignore
        if line:
            if is_first:
                numbers_called = list(map(int, line.split(',')))
                is_first = False
            else:
                if new_card:
                    bingo_cards.append([])
                new_card=False
                nested_board = bingo_cards[board_count]
                #characters at a time to read
                n=3
                nested_board.append([bingoNumber(int(line[i:i+n].strip()), False) for i in range(0,len(line),n)])
        else:
            #blank line encountered next input should be new card
            new_card = True
            board_count+=1

winner_found=False
loser_found=False
winning_board = []
find_the_loser = []
board_index = 0
winning_list=[]
for bingo_number in numbers_called:
    for board in bingo_cards:
        for row in board:
            for card_num in row:
                if card_num.bingo_value==bingo_number:
                    card_num.is_marked = True
        #check if board is winner and break
        if Is_Winner(board):
            #winning_board=board.copy()
            #winner_found = True
            if board not in winning_list:
                    winning_list.append(board)
            if len(winning_list)==len(bingo_cards):
                find_the_loser=board.copy()
                loser_found = True
                break
#   if winner_found:
#        break
    if loser_found:
        break

#sum_of_unmarked = sum([sum([card_num.bingo_value if card_num.is_marked==False else 0 for card_num in row])for row in winning_board])
#print(sum_of_unmarked)
#print(bingo_number)
#print(sum_of_unmarked*bingo_number)
sum_of_loser = sum([sum([card_num.bingo_value if card_num.is_marked==False else 0 for card_num in row])for row in find_the_loser])
print(sum_of_loser)
print(bingo_number)
print(sum_of_loser*bingo_number)
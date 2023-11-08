from data import latin_square_list, board_list
import itertools
import random

def print_board(board,answer):
    '''
    盤面と値を表示する
    入力:board（盤面のデータ）,answer（値、25文字列）
    '''
    lines=[]
    lines.append(list("+-+-+-+-+-+"))
    for i in range(5):
        lines.append(list("| | | | | |"))
        lines.append(list("+-+-+-+-+-+"))

    for pos in range(25):
        tate=(pos//5)*2+1
        yoko=(pos%5)*2+1
        for block in board:
            if pos in block:
                break
        lines[tate][yoko]=answer[pos]
        if pos+1 in block:
            lines[tate][yoko+1]=" "
        if pos+5 in block:
            lines[tate+1][yoko]=" "

    for line in lines:
        print("".join(line))


def is_valid(board,ls):
    '''
    盤面がlsの答えになるか調べる
    入力:board（盤面のデータ）,ls(ラテン方陣、25文字列)
    出力:盤面に当てはまるラテン方陣ならtrueそうでなければfalse
    '''
    for i in range(5):
        values=[]
        values.append(ls[board[i][0]])
        values.append(ls[board[i][1]])
        values.append(ls[board[i][2]])
        values.append(ls[board[i][3]])
        values.append(ls[board[i][4]])
        if not len(set(values))==5:
            return False
    return True
    

def generate_answer_list(board):
    '''
    盤面に当てはまる答えを出力
    入力:board（盤面のデータ)
    出力:ABCDEを12345に置き換えたものの答えを出力
    '''
    answer_list = []
    for ls in latin_square_list:
        if not is_valid(board, ls):
            continue
        for num in itertools.permutations(["1","2","3","4","5"], 5):
            ls_num = ls.replace("A",num[0]).replace("B",num[1]).replace("C",num[2]).replace("D",num[3]).replace("E",num[4])
            answer_list.append(ls_num)
    return answer_list

def generate_hint_list(answer, answer_list):
    '''
    ヒントのリストを生成
    入力:answer（答え）,answer_list（解答候補）
    出力:ヒントのリスト
    '''
    hint_list=[]
    counter = 0
    for hint in itertools.combinations([x for x in range(25)], 4):
        hint_kazu=0
        counter += 1
        if counter % 100 == 0:
            print(".", end="", flush=True)
        for ls in answer_list:
            if not is_match(answer,ls,hint):
                continue
            hint_kazu+=1

        if not hint_kazu==1:
            continue

        hint_list.append(hint)
    return hint_list


def is_match(a, b, hint):
    for h in hint:
        if not a[h]==b[h]:
            return False
    return True

while True:
    ttt = input("? ")
    if ttt == "q":
        break
    board_no=random.randint(0,len(board_list)-1)
    board=board_list[board_no]
    answer_list=generate_answer_list(board)
    if not answer_list:
        print("board_no=", board_no)
        continue
    ansewr_number=random.randint(0,len(answer_list)-1)
    answer=answer_list[ansewr_number]
    hint_list = generate_hint_list(answer, answer_list)
    print()
    for b in board:
        print(b)
    print(answer)
    print(len(answer_list))
    if not hint_list:
        print("board_no=", board_no)
        continue
    hint_no=random.randint(0,len(hint_list)-1)
    hint=hint_list[hint_no]
    hint_moji = [" "] * 25
    for h in hint:
        hint_moji[h] = answer[h]
    print_board(board,hint_moji)

# coding: UTF-8
def split_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def read_players_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

# ファイルを読み込み
file_path = 'players.txt'
players_data = read_players_file(file_path)
matches = split_list(players_data, 2)
output_file_path = 'announcement.txt'

matchNo = 1
with open(output_file_path, 'w', encoding='utf-8') as file:
    for match in matches:
        player1 = match[0].strip().split(',')
        player2 = match[1].strip().split(',')
        file.write(f'第{matchNo}試合 1P側: {player1[1]}選手 VS 2P側: {player2[1]}選手 カスタムルームへお越しください\n')
        file.write(f'第{matchNo}試合 1P側: {player1[1]}選手 VS 2P側: {player2[1]}選手 試合を始めてください！\n')
        file.write(f'第{matchNo}試合 1P側: {player1[1]}選手 VS 2P側: {player2[1]}選手 試合を開始しました 次の試合に出場される方は準備をお願いします！\n')
        matchNo += 1

print(f"置換後の内容を {output_file_path} に出力しました。")
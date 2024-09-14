# coding: UTF-8
def split_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


def read_players_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def generate_html(players_data):
    html_output = ''
    
    matches = split_list(players_data, 2)
    matchNo = 1
    for match in matches:
        html_output += generate_match(match, matchNo)
        matchNo += 1

    return html_output


def generate_match(players_data, matchNo):
    html_output = '<div class="match">\n'
    html_output += f'    <h3>MATCH {matchNo}</h3>\n'
    html_output += '    <div class="players">\n'
    html_output += generate_players(players_data)
    html_output += '    </div>\n'
    html_output += '</div>\n'

    return html_output


def generate_players(players_data):
    html_output = ''
    for player in players_data:
        status, player_name, second_name, character_name, rank = player.strip().split(',')
        match status: 
            case "W":
                status_class = " winner"
            case "L":
                status_class = " loser"
            case _:
                status_class = ""
        
        html_output += f'        <div class="player{status_class}">\n'
        html_output += '            <div class="status"></div>\n'
        html_output += f'            <div class="copy">{second_name}</div>\n'
        html_output += f'            <div class="playerName">{player_name}</div>\n'
        html_output += f'            <div class="rank">{character_name}/{rank}</div>\n'
        html_output += '        </div>\n'

    return html_output

def read_template_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    return template_content

def replace_placeholder(template_content, placeholder, replacement):
    return template_content.replace(placeholder, replacement)

def write_output_file(output_file_path, content):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 何回戦か入力を受け付ける
title = input("タイトルを入力してください(１回戦、決勝戦など): ")

# ファイルを読み込み
file_path = 'players.txt'
players_data = read_players_file(file_path)

# HTMLを生成
html_output = generate_html(players_data)

# テンプレートファイルを読み込む
template_file_path = 'template.html'
template_content = read_template_file(template_file_path)

# プレースホルダーを置き換える
output_content = replace_placeholder(template_content, '{title}', title)
output_content = replace_placeholder(output_content, '{contents}', html_output)

# 結果をファイルに書き出す
output_file_path = 'matchlist.html'
write_output_file(output_file_path, output_content)

print(f"置換後の内容を {output_file_path} に出力しました。")
import itertools
import json

def round_robin_participants(participants):
    # 参加者番号リストを生成（0, 1, 2, ...）
    participant_list = list(range(participants))
    
    # 総当たり戦の組み合わせを生成
    matchups = list(itertools.combinations(participant_list, 2))
    return matchups

def find_non_overlapping_matches(matches):
    # 結果を保存するリスト
    non_overlapping_sets = []
    
    # 未処理の試合リスト
    remaining_matches = matches.copy()
    
    while remaining_matches:
        current_set = []
        used_participants = set()
        
        for match in remaining_matches[:]:  # リストをコピーしてループ内で変更
            # 試合の両参加者がまだ使用されていないか確認
            if match[0] not in used_participants and match[1] not in used_participants:
                current_set.append(match)
                used_participants.update(match)  # 使用済みの参加者を追加
                remaining_matches.remove(match)
        
        non_overlapping_sets.append(current_set)  # 同時試合可能なセットを追加
    
    return non_overlapping_sets

def save_to_json(data, filename):
    # JSONファイルとして保存
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"結果が {filename} に保存されました。")

# 参加人数を入力
participants = int(input("参加人数を入力してください: "))

# 総当たり戦の全試合を生成
matches = round_robin_participants(participants)

# 同時に試合可能な組み合わせを抽出
non_overlapping_sets = find_non_overlapping_matches(matches)

# JSONデータの準備
output_data = {"matches": []}

for match_set in non_overlapping_sets:
    match_list = []
    for match in match_set:
        match_list.append({"player1": match[0], "player2": match[1]})
    output_data["matches"].append(match_list)

# 結果をJSONファイルに保存
filename = "match_results.json"
save_to_json(output_data, filename)

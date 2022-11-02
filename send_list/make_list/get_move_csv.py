from importlib.resources import path
import os
import pandas as pd
from pathlib import Path
import csv
from .get_column_program import get_column

def load_id_get_angle():

    #入力された言葉からidを取得　id->Shuwa_library内に記載
    id = str(get_column())
    id = id.strip("['']")
    #id = 0は確認用
    #id = 1 #id確認用
    print("idは->",id)
    id = int(id[0])

    #idから動作角度をget
    #print(type(id))
    move_angle_list = []

    #IDファイルを読み込んで動作角度の送信
    #ファイルのディレクトリの設定
    dir_path = r'/home/ubuntu/ros2_ws/src/send_list/send_list/id_move_angle'
    file_name = 'id_to_angle.csv'
    file_path = os.path.join(dir_path, file_name)

    max_col = 39#csv 最大列数
    df = pd.read_csv(file_path,encoding='shift-jis') #dfにcsvの値を入れる
    #print(df)#取得id表の表示
    #リストにアングルデータ　入れる
    for i in range(max_col):
        move_angle = df.iloc[id,i]
        move_angle_list.insert(i,move_angle)
        #print(move_angle)
    print(move_angle_list)

    #move_angle_list type"list" -> type"str"
    str_pick_num = ""
    i = 0
    for pick_num_1 in move_angle_list:
        pick_num_1 = move_angle_list[i]
        point = ','
        str_pick_num = str_pick_num + str(pick_num_1) + point
        #print(str_pick_num)
        #print(type(str_pick_num))
        i = i + 1
        #print(i)
    move_angle_list = str_pick_num

    return move_angle_list 

    #ファイルオープン
    # with open(file_path) as f1:
    #     reader = csv.reader(f1)
    #     for row in reader:
    #         id_list.append()
    #         print(row[id])
    #     print(row)
    #id_list = row[0]
    #print(id_list[1])

if __name__ == '__main__':
    load_id_get_angle()


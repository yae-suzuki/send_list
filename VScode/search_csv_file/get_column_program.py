### ファイル内の文字列を検索・抽出
import os
import csv
import pandas as pd
from change_file_extension import change_suffix
from keyborad_input import kye_inp

def __init__(self,word,columu_num):
    self.word = word
    self.columu_num = columu_num


def get_column():
    #空行列の宣言
    word = []
    columu_num = []

    #ファイルのディレクトリの設定
    dir_path = r'C:\Users\uchidalab\OneDrive - 愛知工業大学 (1)\M2\研究\プログラム\VScode\search_csv_file'
    file_name = 'Shuwa_library.csv'

    #ファイルのディレクトリ　列取得用ファイル　パス
    dir_path2 = r'C:\Users\uchidalab\OneDrive - 愛知工業大学 (1)\M2\研究\プログラム\VScode\search_csv_file'
    file_name2 = 'get_column.csv'

    change_suffix(file_name2,".csv",".txt") #change_suffix(file_name, from_suffix, to_suffix)

    #ディレクトリのパスとファイル名からファイルのパスを生成
    file_path = os.path.join(dir_path, file_name)
    file_path2 = os.path.join(dir_path2, file_name2)

    #ファイルオープン
    with open(file_path) as f1:
        lines = f1.readlines() 


    #全語句情報の取得
    lines_strip = [line.strip() for line in lines ] #strip -> 両端の文字を削除

    #入力欄
    word = kye_inp()
    #word = "Apple"

    #リストから関数"word"に入力された文字を検索しピックアップ
    move_word = [line_s for line_s in lines_strip if word in line_s ]
    my_id = move_word[0] #リスト型で送られてくるのでリストの１番目をピックアップ

    #列番号取得用ファイルに保存
    f = open(file_path2,'w')
    f.write(my_id)
    change_suffix(file_name2,".txt",".csv")
    
    #CSV化されたファイルの2列目を読み込む
    with open(file_path2) as f:
        move_columu_sum = csv.reader(f)
        for row in move_columu_sum:
            columu_num.append(str(row[1])) #取得列番号
        
        #print(columu_num)
        #print(type(columu_num))
    
    return columu_num
   
if __name__ == '__main__':
    get_column()

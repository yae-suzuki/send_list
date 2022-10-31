import csv
import os
#import pandas as pd

#配列宣言
word = []
columu_num = []

#入力語句
#input_word = str(input())
input_word = "Apple"

#csvファイルを指定
dir_path = r'C:\Users\uchidalab\OneDrive - 愛知工業大学 (1)\M2\研究\プログラム\VScode\search_csv_file'
file_name = 'file1.csv'

#ディレクトリのパスとファイル名からファイルのパスを生成
file_path = os.path.join(dir_path, file_name)

#csvファイルを読み込み
with open(file_path) as f:
    reader = csv.reader(f)

    #csvファイルのデータをループ
    for row in reader:

        #csv内の列を空配列へ格納
        word.append(str(row[0]))
        columu_num.append(str(row[1]))
    
    #リスト空関数に入力された文字を検索してピックアップ
    list_word = [line_s for line_s in word if input_word in line_s ]
    print(list_word)

print(word)
print(columu_num)
send_list
|
|
|send_list
  |publisher_member_function.py
      マスター用プログラム　動作させたい言葉を入力することでスレーブ側に動作の角度を送信する。
      角度はmesパッケージに乗せてトピック通信で送信される。
  |
  |subscriber_member_function.py
      スレーブ用プログラム　マスター側から送られてきた角度を動作させる。
  |
  |make_list
  | |change_file_extension.py
      ファイルの拡張子変更プログラム　
      
  | |get_column.csv
      入力された言葉とそれに紐付けられたIDを一時的に記録するcsvファイル
      
  | |get_column_program.py
      入力された言葉のIDをget_column.csvに記録するプログラム
  | |get_move_csv.py
      get_column_program.pyを介して取得したIDから紐付けられた動作角度を引っ張り出す。
      引っ張り出された動作角度はlist型なのでrosのmesの型（string）としてretrun
  | |__init__.py
      必須ファイル
  | |keyborad_input
      ---未使用---
  | |num_change
      ---未使用---
  | |Shuwa_library
      手話の言葉とそれに紐付けられたIDが書いてある
  |
  |id_move_angle
    |id_to_angle.csv
        IDと動作させたいアングルが書いてある。

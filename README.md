# AutoTeraraid
環境 python3
      <br>
インストール方法　マイコンにft232_python.inoを書き込む<br>
実行方法　rpa_switch.py を起動.引数にrpa設定したymlのパスを渡す。<br>
　例）　python rpa_switch.py rpa/teraraid_nynphia.yml


動かない場合<br>
　環境を整える<br>
 　■　python3のインストール<br>
 　■  pip　実行<br>
  　　　コマンドプロンプトで、以下を実行
     <br>
python -m pip install opencv-python
     <br>
python -m pip install pyserial
     <br>
python -m pip install pyyaml
     <br>
python -m pip install opencv-python
     <br>
python -m pip install pyocr
     <br>
python -m pip install Pillow

うまく検知されない場合
　キャプチャボードによってカラーが違う場合があります。
  conf.ymlをいい感じに直してください


まだベータ版です。反響があったら詳細の解説をします。使い方の詳細も解説します。

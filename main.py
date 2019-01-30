#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# 自分の環境ではpipのインストール先のpathが通っていなかったのでpathを追加しました.
# ---
#import sys
#sys.path.append("/usr/local/lib/python2.7/site-packages")
# ---

import nfc
import re
import time

# create_message
## message を作成する
def create_message(id):
  # タッチした時刻を取得する
  now = time.ctime()
  # csv 形式?
  return now+','+id
  # json 形式?
  #return '{ \"time\" : \"'+now+'\", \"uId\" : \"'+id+'\" }'

# write_message
## file に message を書き込む
def write_message(sttr):
  f = open('attend.txt', 'a')
  f.write(sttr + "\n")
  f.close()

# write_log
## file に tag の dump 内容を log を書き込む
def write_log(sttr):
  f = open('attend.log', 'a')
  f.write(sttr + "\n")
  f.close()

# on_connect
## fekicaのセットアップ時に発火
def on_startup(target):
  def on_startup(targets):
    print("on_startup()")
    print targets
    #return targets

# on_connect
## felicaにタッチした時に発火
def on_connected(tag):
  # tag情報をファイルに書き込み
  for line in tag.dump():
    write_log(line)
  write_log("\n")
  for line in tag.dump():
    # パターン
    pattern = r"0000: 30"
    # 正規表現
    matchLine = re.search(pattern, line)
    # パターンにマッチしたら...
    if matchLine:
      # 学籍番号の場所(推定...)
      uId = line.split('|')
      # 学籍番号をファイルに書き込み
      write_message(create_message(uId[1][4:14]))
      # 確認用 print 
      print '学籍番号 : '+uId[1][4:14]+' の出席を確認しました。'
      #重複している行もあるのでbreakして抜ける
      break

  # 連続で書き込むのを防ぐために sleep (この方法で良い??)
  time.sleep(3)
  # 再表示 print
  print('学生証をかざしてください：')

# on-release
## felicaを離した時に発火
def on_released(tag):
  #print(tag)
  print('学生証をかざしてください：')
  time.sleep(3)

def while_loop_clf_connect():
  # usb deviseとの接続を行う
  clf = nfc.ContactlessFrontend('usb')

  rdwr_options = {
    #'on-startup': on_startup,
    'on-connect': on_connected,
    'on-release': on_released
  }
  print "学生証をかざしてください："
  #
  #if(clf):
  #  while clf.connect(rdwr=rdwr_options):
  #    pass
  #
  while True:
    clf.connect(rdwr=rdwr_options)
  
# main
## 
def main():  
  try:
    while_loop_clf_connect()
  except NameError as identifier:
    print "読み取りに失敗しました！"
    pass
  except nfc.tag.tt3.Type3TagCommandError as e:
    print "読み取りに失敗しました！"
    pass

if __name__ == '__main__':
  try:
    main()
    pass
  except IOError as identifier:
    print "PaSoRi を接続してください！"
    pass
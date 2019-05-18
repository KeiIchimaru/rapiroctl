#!/usr/bin/python3
# coding: utf-8
import sys
import serial
import subprocess
import urllib3
from bottle import route, run, request, HTTPResponse, template, static_file

DEBUG = False
SHELL = False
DEFAULT_PATH = '/home/pi/rapiroctl/'

com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)

#
# 共通メソッド
#
def system_call(command):
  try:
    if DEBUG:
      for txt in command:
        sys.stdout.write(txt + ' ')
      sys.stdout.write('\n')
    if SHELL:
      subprocess.check_call(command, shell=True)
    else:
      subprocess.check_call(command)
  except subprocess.CalledProcessError:
    if DEBUG:
      sys.stdout.write('handle errors in the called executable !!!')
  except OSError:
    if DEBUG:
      sys.stdout.write('executable not found !!!')

#
# RAPIROとのシリアル通信
#
def com_open():
  return serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)

def rapiro_command(command):
  if DEBUG:
    sys.stdout.write('write ' + command + '\n')
  com.write(bytes(command, 'UTF-8'))

#
# 音声関係コマンド
#
DEFAULT_AUDIO_PATH = DEFAULT_PATH + 'audio/'

def audio_play(fileNames):
  files = []
  for fn in fileNames:
    files.append(DEFAULT_AUDIO_PATH + fn + '.wav')
  if SHELL:
    command_list = 'aplay ' + ' '.join(files)
  else:
    command_list = ['aplay', '-q'] 
  # command_list = ['aplay', '-Dhw:0,0', '-q']
    command_list.extend(files)
  system_call(command_list)

def audio_speak(message):
  command_list = [DEFAULT_PATH + 'openjtalk.sh', message]
  if SHELL:
    system_call(' '.join(command_list))
  else:
    system_call(command_list)

#
# responceの作成
#
def make_response(body):
  r = HTTPResponse(status=200, body=body)
  r.set_header("Access-Control-Allow-Origin", "*")
  return r

@route("/")
def index():
    return template(DEFAULT_PATH + "index.html")

@route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root=DEFAULT_PATH+"static")

@route('/PLAY')
def PLAY():
  name = request.params.get('name')
  audio_play(name.split(","))
  return make_response("PLAY accepted!")

@route('/SPEAK')
def SPEAK():
  message = request.params.decode().get('message')
  audio_speak(message)
  return make_response("SPEAK accepted!")

@route('/M0')
def M0():
  rapiro_command("#M0")
  return make_response("M0 accepted!")
 
@route('/M1')
def M1():
  rapiro_command("#M1")
  return make_response("M1 accepted!")

@route('/M2')
def M2():
  rapiro_command('#M2')
  return make_response("M2 accepted!")

@route('/M3')
def M3():
  rapiro_command('#M3')
  return make_response("M3 accepted!")

@route('/M4')
def M4():
  rapiro_command('#M4')
  return make_response("M4 accepted!")

@route('/M5')
def M5():
  rapiro_command('#M5')
  return make_response("M5 accepted!")

@route('/M6')
def M6():
  rapiro_command('#M6')
  return make_response("M6 accepted!")

@route('/M7')
def M7():
  rapiro_command('#M7')
  return make_response("M7 accepted!")

@route('/M8')
def M8():
  rapiro_command('#M8')
  return make_response("M8 accepted!")

@route('/M9')
def M9():
  rapiro_command('#M9')
  return make_response("M9 accepted!")

@route('/PX')
def PX():
  s = request.params.get('S')
  a = request.params.get('A')
  t = request.params.get('T')
  rapiro_command('#PS' + s + 'A' + a + 'T' + t)
  return make_response("PX accepted!")

@route('/LOW')
def LOW():
  rapiro_command('#L')
  return make_response("Servo Power off accepted!")

@route('/HIGH')
def HIGH():
  rapiro_command('#H')
  return make_response("Servo Power on accepted!")

@route('/COMC')
def COMC():
  com.close()
  return make_response("COM close accepted!")

@route('/COMO')
def COMO():
  com.open()
  return make_response("COM open accepted!")

# ビルトインの開発用サーバーの起動
#
run(host='rapiropi', port=80, debug=True, reloader=True)

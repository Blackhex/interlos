#!/usr/bin/env python

import socket
from Player import Player

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("moose.ienze.me", 5123))
s.settimeout(2)

p = Player()

def read():
  line = ""
  while not line.endswith('\n'):
    try:
      line += s.recv(1)
    except:
      line = "timeout"
      break
  print line
  return line

def send(t):
  s.sendall(t +"\n")

send("hraji membe")

finish = False
while not finish:
  r = read()
  if r.startswith("hraj"):
    send(str(p.get_number()))
    send(str(p.get_number()))
    send(str(p.get_number()))
  if r == "timeout":
    finish = True
  if r == "druhy hrac opusitil hru":
    finish = True

s.close()


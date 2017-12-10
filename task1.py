#!/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("moose.ienze.me", 5123))

def read():
  line = ""
  while not line.endswith('\n'):
    line += s.recv(1)
  print line
  return line

def send(t):
  s.sendall(t +"\n")

send("hraji membe")
r = read()
while not r.startswith("hraj"):
  r = read()

s.close()


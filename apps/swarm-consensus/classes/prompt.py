#!/usr/bin/env python3

""" 
Prompt class is part of a thesis work about distributed systems 
"""
__author__ = "Bruno Chianca Ferreira"
__license__ = "MIT"
__version__ = "0.8"
__maintainer__ = "Bruno Chianca Ferreira"
__email__ = "brunobcf@gmail.com"

import os, struct, sys, traceback, threading, time, readline

class Prompt:

  def __init__(self, node):
    self.lock=True
    self.prompt_str = "#>"

  def prompt(self,node):
    'Simple command prompt * Maybe can be changed to use a prompt lib for better functionallity'
    try:
      while self.lock==True:
        inp = input(node.fulltag + self.prompt_str)
        command = inp.split()
        try:
          if (len(command))>=1:
            if command[0] == 'help':
              self._printhelp()
            elif command[0] == 'clear':
              print("\033c")
              print()
            elif command[0] == 'app':
              node.Application._prompt(command)  
            elif command[0] == 'visible':
              try:
                node.Membership.printvisible() 
              except:
                self.print_alert('Nothing to show')
                pass
            elif command[0] == 'info':
              node.printinfo()
            elif command[0] == 'quit':
              node.lock = False
              #node.shutdown()
              sys.stdout.write('Quitting')
              while True:
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(1)
            elif command[0] == 'debug':
              node.Application.toggleDebug()
            elif command[0] == 'disable':
              node.Application.disable()
            elif command[0] == 'enable':
              node.Application.enable()
            else:
              self.print_error("Invalid command!")
        except:
          print('General error, probably the emulation have not started yet.')
    except:
      traceback.print_exc()
      node.lock = False
      self.print_alert("Exiting!")

  def _printhelp(self):
    'Prints help message'
    print()
    print("Distributed node")
    print()
    print("Interface commands: ")
    print()
    print("info      - Display general information about the node")
    print("net       - Display help from the network")
    print("member    - Display help from the membership control")
    print("fault     - Display help from the fault detector")
    print("app       - Display help from application")
    #print("visible   - Display the list of visible neighbours")
    print("debug     - Enable debug mode")
    print("clear     - Clear the display")
    print("help      - Diplay this help message")
    print("quit      - Exit the agent")
    print()

  def print_error(self,text):
    'Print error message with special format'
    print()
    print("\033[1;31;40m"+text+"  \n")
    print("\033[0;37;40m")

  def print_alert(self,text):
    'Print alert message with special format'
    print()
    print("\033[1;32;40m"+text+"  \n")
    print("\033[0;37;40m")

def print_error(text):
  'Print error message with special format'
  print()
  print("\033[1;31;40m"+text+"  \n")
  print("\033[0;37;40m")

def print_alert(text):
  'Print alert message with special format'
  print()
  print("\033[1;32;40m"+text+"  \n")
  print("\033[0;37;40m")

def print_info(text):
  'Print info message with special format'
  print()
  print("\033[1;34;40m"+text+"  \n")
  print("\033[0;37;40m")
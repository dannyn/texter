#!/usr/bin/env python3
import argparse
import csv
import sys
import time

from subprocess import Popen, PIPE

ascript_total = """
activate application "Messages"
    tell application "System Events" to tell process "Messages"
    key code 45 using command down
    keystroke "{}"
    key code 36
    keystroke "{}"
    key code 36
end tell 
"""


ascript = """
activate application "Messages"
    tell application "System Events" to tell process "Messages"
    key code 45 using command down
    keystroke "{}"
    key code 36
    keystroke "{}"
end tell 
"""



def send_enter():
    enter_script = """
    activate application "Messages"
        tell application "System Events" to tell process "Messages"
        key code 36
    end tell 
    """
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(enter_script)

def send_text(phone_number, message):
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    fscript = ascript.format(phone_number, message)
    stdout, stderr = p.communicate(fscript)
    time.sleep(4)
    send_enter()
    if p.returncode == 0:
        print (f"attempted to send text to {phone_number}")
    else:
        print (f"something went wrong sending to {phone_number}")


def main():
    parser = argparse.ArgumentParser(description='Send texts')
    parser.add_argument('recipient_file', type=str, 
        help="recipient file, csv in number,name format")
    parser.add_argument('message_file', type=str,
        help="file containing message")
    args = parser.parse_args()

    with open(args.message_file, "r") as fp:
       message = fp.read()

    with open(args.recipient_file, "r") as fp:
        rdr = csv.reader(fp, delimiter=',')
        for row in rdr:
            fmessage = message.format(row[1])
            send_text(row[0], fmessage)
            time.sleep(60)

if __name__ == "__main__":
    #print ("remember youmade changes to have it hit enter after a delay")
    main()

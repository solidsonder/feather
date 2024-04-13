import argparse
import sys
import json
from pathlib import Path
import os
from modules.banner import *

shbn()

parser = argparse.ArgumentParser(description="feather v0.01 - 'raven' (A Telegram alert and transaction tool)"
                                ,usage="usage: python feather.py [-h] [arguments]")

parser.add_argument("-s","--start", action='store_true', help="start programme")
parser.add_argument("-so","--set-operation",  help="set automatic process for alert (add '*&*' for replace text)")
parser.add_argument("-sl","--save-logs", help="save programme logs generated during (1=Save/0=Not)")
parser.add_argument("-rl","--remove-logs", action='store_true', help="remove every programme logs")

teleg_group = parser.add_argument_group("Telegram Options")
teleg_group.add_argument("-pn","--phone-number", type=str, help="Set phone number ")
teleg_group.add_argument("-ai","--api-id", help="add api id for programme")
teleg_group.add_argument("-ah","--api-hash",  help="add api hash for programme")
teleg_group.add_argument("-gi","--group-id",  help="add group id for alert")

gmail_group = parser.add_argument_group("Gmail Options")
gmail_group.add_argument("-sm","--sender-mail", help="set sender mail for smtp")
gmail_group.add_argument("-ap","--app-passwd",  help='set sender mail app passwd for smtp (use - or ="")')
gmail_group.add_argument("-rm","--recipient-mail",  help="set recipient mail for send datas")
gmail_group.add_argument("-ss","--set-subject",  help="set subject for mail")


dwnl_group = parser.add_argument_group("Download Info")
dwnl_group.add_argument("-ul","--user-list", action='store_true', help="set sender mail for smtp")

args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    parser.exit()
else:


    if args.user_list:
        print(infox+" starting programme...")
        os.system("python core/dwnld.py")

    if args.set_operation:
        with open("lib/operation.txt", 'w') as f:
            f.write(args.set_operation)
        print(infox+" operation changed successfully.")

    if args.remove_logs:
        with open("lib/logs.txt", 'w') as f:
            f.write(" ")
        print(infox+" logs removed successfully.")

    if args.save_logs:
        a="0"
        if str(args.save_logs) == "1":
            a ="1"
        elif str(args.save_logs) == "0":
            a = "0"
        with open("lib/logh.txt", 'w') as f:
            f.write(a)
        print(infox+f" save logs option set {a} successfully.")

    if args.start:

        print(infox+" starting programme...")
        os.system("python core/alert.py "+os.path.dirname(os.path.abspath(__file__)))

    else:


        config_data = {
            "phone_number": args.phone_number,
            "api_id": args.api_id,
            "api_hash": args.api_hash,
            "group_id": args.group_id,
            "sender_mail": args.sender_mail,
            "app_passwd": args.app_passwd,
            "recipient_mail": args.recipient_mail,
            "set_subject": args.set_subject
        }

        config_file = "lib/config.json"
        with open(config_file, 'w') as f:
            json.dump(config_data, f, indent=4)
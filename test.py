#!/usr/bin/python3

import gateway
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="", action="store_true")
parser.add_argument("-i", "--identifier", help="locker identifier", type=str)
parser.add_argument("--host", help="host", type=str)
parser.add_argument("-c", "--code", help="code", type=str)
parser.add_argument("action", help="open, close, search, synchronize, update, synchronize_locker, update_locker")


args = parser.parse_args()

gw = gateway.Gateway(args.debug)
if args.host:
    gw.set_host(args.host)

if args.action == "open":
    gw.open(args.identifier, args.code.encode("ascii"))
elif args.action == "close":
    gw.close(args.identifier, args.code.encode("ascii"))
elif args.action == "search":
    gw.search()
elif args.action == "synchronize":
    gw.synchronize()
elif args.action == "update":
    gw.update()
elif args.action == "synchronize_locker":
    gw.synchronize_locker(args.identifier)
elif args.action == "update_locker":
    gw.update_locker(args.identifier)
elif args.action == "locker_status":
    gw.locker_status(args.identifier, args.code.encode("ascii"))
elif args.action == "status":
    gw.status()
else:
    print("Command not implemented.")


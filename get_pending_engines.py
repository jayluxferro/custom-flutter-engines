#!/usr/bin/env python3

import sys


def usage():
    print('Usage: python3 {} [path_to_enginehash.csv] [path_to_build_engine.txt]'.format(sys.argv[0]))
    sys.exit(1)


if len(sys.argv) != 3:
    usage()


built_engines = [ x.rstrip().strip() for x in open(sys.argv[2]).readlines() ]
source_engines = [ x.rstrip().strip().split(',')[-1] for x in open(sys.argv[1]).readlines() ][1:]

pending_engines = []

for engine in source_engines:
    try:
        _ = built_engines.index(engine)
    except:
        pending_engines.append(engine)

with open('./pending_engines.txt', 'w') as f:
    f.write('\n'.join(pending_engines))

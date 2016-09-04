#!/usr/bin/env python

import sys
file_name = sys.argv[1]
file = open(file_name)
for line in file.readlines():
        if "DROME" in line:
                pass
        item = line.rstrip("\r\n").split()
	if len(item) >= 4 :

		print(item[3]+"\t"+item [2])


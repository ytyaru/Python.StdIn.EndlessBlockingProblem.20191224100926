#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
stdin = list(sys.stdin)
for line in stdin:
    print(line)
#print(stdin)
#import struct
#sys.stdin.write(EOF)
#sys.stdin.write(0x04)
#sys.stdin.write(0x04)
#sys.stdin.write(struct.pack("B", 0x04))
#sys.stdin.close()

#sys.stdin.flush()
#sys.stdout.flush()
#print(sys.stdin.read())
#sys.stdin.flush()
#sys.stdout.flush()

#sys.stdin.close()
#stdin = [line.rstrip('\n') for line in sys.stdin.readlines()]
#print(stdin)
#print(sys.stdin.read())
#stdin = sys.stdout.read()
#print('stdin', stdin)
#stdin = [print(i.strip()) for i in sys.stdin]
#print(stdin)
#a = sys.stdin.read()
# https://qiita.com/apollo_program/items/44adb2b5aaea90fb2150
#ls | python3 -c "import sys;[print(i.strip()) for i in sys.stdin]" 
#ls | python3 -c "import sys; print(sys.stdin.read())" 

#[print(i.strip()) for i in sys.stdin]
#print(a)

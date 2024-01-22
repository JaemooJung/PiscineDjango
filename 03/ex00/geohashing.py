#!/usr/bin/env python3

import sys
import antigravity

def main():

    usage_message = "Usage: python3 geohashing.py <date: string> <latitude: float> <longitude: float>"

    if len(sys.argv) != 4:
        print(usage_message)
        return
    
    try:
        antigravity.geohash(float(sys.argv[2]), 
                            float(sys.argv[3]), 
                            bytes(sys.argv[1], 'utf-8'))
    except Exception as e:
        print(f'invalid input: {e}')
        print(usage_message)

if __name__ == '__main__':
    main()
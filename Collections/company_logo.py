#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    counter = sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))

    for k, v in counter[:3]:
        print(f'{k} {v}')

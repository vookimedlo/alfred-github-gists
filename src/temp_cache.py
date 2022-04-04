#!/usr/bin/env python3

import sys
import tempfile

cache = tempfile.mkstemp()[1]
sys.stdout.write(cache)

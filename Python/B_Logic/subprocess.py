# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:39:36 2020

@author: Joseph
"""

import subprocess
pl = subprocess.Popen(['ps', '-U', '0'], stdout=subprocess.PIPE).communicate()[0]
print(pl.decode('utf-8'))


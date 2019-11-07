"""
    This utilit is for copying specific subdirectory tree to the destination.
    The working principe is that program recursively iterate directory
    and when find specific subdirectory, it just copy it's subdirectories 
    to the destination directory. 
"""

import  os
from distutils.dir_util import copy_tree

def copy_specific_subdirectory(src, dest, subdirectory):
    for path, subdirs, files in os.walk(src):
        for dirname in subdirs:
            if dirname == subdirectory:
                dirname = os.path.join(path,dirname)
                copy_tree(dirname, dest)
                print(dirname)

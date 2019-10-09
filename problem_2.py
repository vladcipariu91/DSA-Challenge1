"""
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it)
that end with ".c"

    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths

"""
import os
from collections import deque


def find_files(suffix, path):
    q = deque()
    q.append(path)
    c_files = []

    while q:
        path = q.pop()
        try:
            content = os.listdir(path)
        except FileNotFoundError:
            return c_files

        for f in content:
            file = os.path.join(path, f)
            if os.path.isfile(file):
                if file.endswith(suffix):
                    c_files.append(file)
            elif os.path.isdir(file):
                q.appendleft(file)

    return c_files


print(find_files('.c', './testdir'))
# expected ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c']
print(find_files('.py', './testdir'))
# expected []
print(find_files('.py', './testdir_not_found'))
# expected []

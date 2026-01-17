# File Cleaner
# Developed by @_I42

import os

def cleanup_file(path):
    if os.path.exists(path):
        os.remove(path)

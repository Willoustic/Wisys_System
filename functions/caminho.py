import os, sys

def resource_path(*paths):
    return os.path.join(*paths)


def resource_path_1(*paths):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(*paths)
    return os.path.join(os.path.abspath("."), *paths)
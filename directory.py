import os
current_path = "./"


def tree_structure(path):

    for root, dirs, files in os.walk(path):
        deep = root.replace(path, '').count(os.sep)
        indent = '-' * 4 * deep
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = '-' * 4 * (deep + 1)
        for f in files:
            print('{}{}'.format(sub_indent, f))


tree_structure(current_path)
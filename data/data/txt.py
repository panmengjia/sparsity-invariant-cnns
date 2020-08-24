import os

root = '2011_09_26'
f = open('train.txt','w+')

for dirs in os.walk(root):
    for dir in dirs[1]:
        if '_sync' in dir:
            path_high = os.path.join(root, dir, 'high')
            path_low = os.path.join(root, dir, 'low')
            for files in os.walk(path_high):
                for file in files[2]:
                    path_label = os.path.join(root, dir, 'high', file)
                    path_data = os.path.join(root, dir, 'low', file)
                    line = path_data + '\t' + path_label + '\n'
                    f.write(line)

__author__ = 'Egor Filimonov'
__version__ = '1.0'
__date__ = '2021-10-12'

import sys
import getopt

help = ('set_values.py -s source_ile [-d destination_file] stdin\n'
        '-s, --source_file   source file\n'
        '-d, --dest_file     destination file\n')
source_file = ''
destination_file = ''
noCommitBegin = '#nocommit-begin'
noCommitEnd = '#nocommit-end'
stdin = True


def get_file_content(path):
    with open(path) as file:
        return file.readlines()


def get_keys(file_content):
    begin = False
    end = False
    keys = []
    for line in file_content:
        if noCommitEnd in line:
            begin = False
            end = True
        if begin == True and end == False:
            keys.append(line.split(':')[0])
        if noCommitBegin in line:
            begin = True
            end = False
    return keys


def get_value(file_content, key):
    for line in file_content:
        if key == line.split(':')[0]:
            return line


def set_values(file_content, values):
    result = []
    for line in file_content:
        for key in values.keys():
            if key == str(line).split(':')[0]:
                line = values.get(key)
        result.append(line)
    return result


def save_file(destination_file, destination_file_content):
    try:
        with open(destination_file, 'w') as file:
            file.writelines(destination_file_content)
        return 'Success!'
    except any:
        return 'Fail!'


try:
    args = sys.argv
    args.remove(__file__)
    opts, args = getopt.getopt(args, 's:d:', ['source_file=', '--dest_file='])
except getopt.error as err:
    print err, '\n\n', help
    sys.exit(1)

for opt, arg in opts:
    if opt in ('-s', '--source_file'):
        source_file = arg
    elif opt in ('-d', '--dest_file'):
        destination_file = arg
        stdin = False
    else:
        print help
        sys.exit(1)

# This section sets first option as a source file, second option as a destination file.
# It is not used due to undescribed option is stdin.
# if sourceFile == '':
#     sourceFile = args[0]
# if destinationFile == '':
#     destinationFile = args[1]

if stdin:
    destination_file_content = sys.stdin.readlines()
else:
    destination_file_content = get_file_content(destination_file)

source_file_content = get_file_content(source_file)
keys = get_keys(destination_file_content)
values = {key : get_value(source_file_content, key)
          for key in get_keys(destination_file_content)}

# Clean keys with empty values, otherwise strings in destination file
# with matched keys will invoke None_type error during string swapping.
for key in values.keys():
    if values.get(key) is None:
        values.pop(key)

result = set_values(destination_file_content, values)
if stdin:
    sys.stdout.writelines(result)
else:
    print(save_file(destination_file, result))
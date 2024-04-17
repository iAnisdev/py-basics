import os

path_license = './LICENSE'
path_chain = './chain.pem'
path_go = './../go-basics'


def check_exists(file_path):
    if os.path.exists(file_path):
        print(f'{file_path} exists')
        if os.path.isfile(file_path):
            print(f'{file_path} is a file')
        elif os.path.isdir(file_path):
            print(f'{file_path} is a directory')
    else:
        print(f'{file_path} does not exist')


check_exists(path_license)
check_exists(path_chain)
check_exists(path_go)
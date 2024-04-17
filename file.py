import os
import shutil

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


with open('./LICENSE') as file:
    print(file.read())

with open('./chain.pem' , 'w') as file:
    file.write('This is a chain.pem file')

#copy(src, dst)
#copyfile(src, dst)
#copy2(src, dst)

shutil.copyfile('./chain.pem', './chain-copy.pem')

os.rename('./chain-copy.pem', './chain2.pem')
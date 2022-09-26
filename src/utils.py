import os
if __name__ == '__main__':

    print('This is a utility file.')


def mkdir(dist='dist'):
    '''
    make directory in the root dir if not exist

    :param dist: output directory name, default value is 'dist'
    '''
    path = os.getcwd()

    output = os.path.join(path, dist)

    isExist = os.path.exists(output)

    if not isExist:
        os.mkdir(output)
        print(output)
    else:
        print('directory {} already exist!'.format(output))

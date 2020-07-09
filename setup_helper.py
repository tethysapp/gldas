import os

def find_resource_files(directory, relative_to=None):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if relative_to is not None:
                paths.append(os.path.join(os.path.relpath(path, relative_to), filename))
            else:
                paths.append(os.path.join('..', path, filename))
    return paths


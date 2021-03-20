import requests
import tarfile
import os

def download_file(url, directory):
    local_filename = os.path.join(directory, url.split('/')[-1])
    print ("Downloading %s --> %s"%(url, local_filename))
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

def extract_tar(fpath):
    fname_dir, fname = os.path.split(fpath)
    dest_path = os.path.join(fname_dir,fname.split('.')[0])
    print ("Extracting %s --> %s"%(fpath, dest_path))
    if fname.endswith("tar.gz"):
        tar = tarfile.open(fpath, "r:gz")
        tar.extractall(path=fname_dir)
        tar.close()
    elif fname.endswith("tar"):
        tar = tarfile.open(fname, "r:")
        tar.extractall(path=fname_dir)
        tar.close()
    return dest_path

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
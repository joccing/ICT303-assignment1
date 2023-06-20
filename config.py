import os
import errno

FOLDERS = {
    'housing-prices': ['data'],
}
FILENAMES = {
    'housing-prices': ['train.csv','test.csv','data_description.txt','sample_submission.csv'],
}
    
try:
    import google.colab
    IS_COLAB = True
except ModuleNotFoundError:
    IS_COLAB = False

def download_to_colab(folderName, branch='master'):
    base_url = 'https://joccing/ICT303-assignment1/{}/'.format(branch)

    folders = FOLDERS[folderName]
    filenames = FILENAMES[folderName]
    for folder, filename in zip(folders, filenames):
        if len(folder):
            try:
                os.mkdir(folder)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        if len(filename):
            path = os.path.join(folder, filename)
            url = '{}{}'.format(base_url, path)
            r = requests.get(url, allow_redirects=True)
            open(path, 'wb').write(r.content)
    
def config_data(branch='master'):
    if IS_COLAB:
        print('Downloading files from GitHub repo to Colab...')
        download_to_colab('housing-prices', branch)
        print('Finished!')
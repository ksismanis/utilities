import os
import urllib.request

DOWNLOADS_DIR = 'downloaded'

# For every line in the file
for url in open('nord_urls.csv'):
    # Split on the rightmost / and take everything on the right side of that
    prefix = url.rsplit('/',1)[0]
    prefix = prefix.rsplit('/',1)[-1]
    print(prefix)
    name = url.rsplit('/', 1)[-1]
    name = name.rsplit('?',1)[0]
    name = name + ".jpg"
    #name = prefix+'_'+name
    print(name)
    # Combine the name and the downloads directory to get the local filename
    filename = os.path.join(DOWNLOADS_DIR, name)
    print(url)
    print(filename)
    # Download the file if it does not exist
    if not os.path.isfile(filename):
        try:
            urllib.request.urlretrieve(url, filename)
        except Exception as e :
            print(e)
import requests
#Script to request data from macaulaylibrary
DIR = r'../data/Random Sample MP3'  # modify to download location

x = 5
#Go through first 10000ML catalog files of library and save files
for x in range(10000):
    try:
        url = 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/'+str(x)
        filedata = requests.get(url)
        # print(filedata)
        # print(filedata.content)
        with open(DIR+'/'+str(x)+'.mp3', 'wb') as f:
            f.write(filedata.content)
    except Exception as e:
        print(e)

import requests

DIR = r'MP3'  # modify to download location

dict = {
    '67895': 'Cattle (Domestic type)',
    '132526': 'Cat (Domestic type)',
    '95976': 'Dog (Domestic type)',
    '89404': 'White-tailed Deer',
    '55302': 'American Black Bear',
    '172760': 'american beaver',
    '128297': 'Humpback Whale',
    '129659': 'Leopard seal',
    '179735': 'pileated gibbon',
    '137853': 'Caribou',
    '29765': 'Giant Otter',
    '126393': 'Tiger',
    '82309': 'red howler monkey',
    '88172': 'common raccoon',
    '129697': 'Walrus',
    '57102': 'Cane Toad',
    '80312': 'Pacific Chorus Frog',
    '96098': 'Galapagos Tortoise',
    '144903': 'Caribbean Dove',
    '137519': 'Long-eared Owl (American)',
    '189721': 'Beijing Babbler',
    '90620': 'Ruddy Pigeon (Ruddy)',
    '80754': 'Snowy Egret',
    '93752': 'Baltimore Oriole',
    '90898': 'Screaming Piha',
    '77956': 'Eastern Meadowlark (Eastern)',
    '89845': 'Helmeted Pygmy-Tyrant',
    '77007': 'Crested Serpent-Eagle',
    '94503': 'Jumping Bush Cricket',
    '110297': 'scissor-grinder cicada',
    '45488': 'Brown Pelican'
}

for key in dict:
    try:
        url = 'https://cdn.download.ams.birds.cornell.edu/api/v1/asset/'+key
        filedata = requests.get(url)
        # print(filedata)
        # print(filedata.content)
        with open(DIR+'/'+dict[key]+'.mp3', 'wb') as f:
            f.write(filedata.content)
    except Exception as e:
        print(e)
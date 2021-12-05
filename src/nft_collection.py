'''
We need to formalise the formating of all media NFTs. We have 
   categorised our NFTs into four possible categories. 
   Image: .jpg
   Video: .mp4
   Music: .mp3, (.mp3 + .jpg), (.mp3 + .gif), .mp4 
   GIF: .gif
   Acccepted file types: .jpg, .gif, .mp3, .mp4 
'''
TOTAL_FORMATS = 4
    # "collection_name": "asset_contract_address"
collection = {
    "cryptopunks": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB",             # (Image: JPG)       [Opensea: Art, Rank #1, last 7 days]
    "boredapeyachtclub": "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",       # (Image: JPG)       [Art, Rank #2, last 7 days]
    "doodles-official": "0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",        # (Image: JPG)       [Art, Rank #3, last 7 days]
    "boonjiproject": "0x4cd0ea8b1bdb5ab9249d96ccf3d8a0d3ada2bc76",           # (Image: JPG)       [Art, Rank #4, last 7 days]
    "fidenza-by-tyler-hobbs": "0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270",  # (Image: JPG)       [Art, Rank #5, last 7 days]
    "lostpoets": "0x4b3406a41399c7fd2ba65cbc93697ad9e7ea61e5",               # (Image: JPG)       [Art, Rank #8, last 7 days]
    "theshiboshis": "0x11450058d796b02eb53e65374be59cff65d3fe7f",            # (Image: JPG)       [Art]
    "veefriends":"0xa3aee8bce55beea1951ef834b99f3ac60d1abeeb",               # (Image: JPG)       [Art]
    "song-a-day": "0x495f947276749ce646f68ac8c248420045cb7b5e",              # (Video: MP4)       [Music, Rank #2, last 7 days]
    "eulerbeats-enigma": "0xa98771a46dcb34b34cdad5355718f8a97c8e603e",       # (Music: MP4)       [Music, Rank #3, last 7 days]
    "eulerbeats":"0x8754f54074400ce745a7ceddc928fb1b7e985ed6",               # (Music: MP4)       [Music, Rank #1, all time]
    "spottiewifi": "0xa0e1b198bcc877a950a29512ab5c0ce1bb964c97",             # (Music: MP4)       [Music, Rank #8, last 7 days]
    "namewee4896-collection": "0x495f947276749ce646f68ac8c248420045cb7b5e",  # (Music: MP3 + JPG) [Music, Rank #4, all time]
    "jinglebe-nft-collection": "0x9951f5da4f4f21b7d39a80bc665edf31bd515009", # (Music)            [Music, Rank #5, all time]
    "async-music":"0x3e43944d977dea22511da6d33c0cab666a604515",              # (Music: MP3 + JPG) [Music, Rank #9, all time]
    "niftysaxspheres":"0xf89cfa360a2b883d7325d94eeea89c2b7079c1a3",          # (Music: MP4)       [Music]
    "calvin-harris-x-emil-nava":"0xbe7e0d467d9e0235c8ac5a7d68e55e198ff2235b",# (Music: MP4)       [Music]
    "superrare": "0xb932a70a57673d89f4acffbe830e8ed7f75fb9e0",               # (Image: JPG | GIF: GIF | Audio: MP3 | Video: MP4) Marketplaces
    "rarible":"0xd07dc4262bcdbf85190c01c996b4c06a461d2430"                   # (Image: JPG | GIF: GIF | Audio: MP3 | Video: MP4) Marketplaces
}


nft_format = {
    "cryptopunks": {"tags":"image", "formats":".jpg"},
    "boredapeyachtclub":  {"tags":"image", "formats":".jpg"},
    "doodles-official": {"tags":"image", "formats":".jpg"},
    "boonjiproject": {"tags":"image", "formats":".jpg"},
    "fidenza-by-tyler-hobbs": {"tags":"image", "formats":".jpg"},
    "lostpoets": {"tags":"image", "formats":".jpg"},
    "theshiboshis": {"tags":"image", "formats":".jpg"},
    "veefriends": {"tags":"image", "formats":".jpg"},
    "song-a-day": {"tags":"video", "formats":".mp4"},
    "eulerbeats-enigma": {"tags":"music", "formats":".mp4"},
    "eulerbeats": {"tags":"music", "formats":".mp4"},
    "namewee4896-collection": {"tags":"music", "formats":[".mp3",".jpg"]}, 
    "spottiewifi": {"tags":"music", "formats":[".mp3",".jpg"]},  # This comes in a mp4 format, we will split from MP4 to mp3 and jpg 
    "jinglebe-nft-collection": {"tags":"music", "formats":[".mp3", ".gif"]},
    "async-music": {"tags":"music", "formats":[".mp3", ".jpg"]}, 
    "niftysaxspheres": {"tags":"music", "formats":".mp4"}, 
    "calvin-harris-x-emil-nava": ({"tags":"music", "formats":".mp4"}),
    "superrare": {"tags":["image", "gif", "music", "video"], "formats":[".jpg", ".gif", ".mp3", ".mp4"]},
    "rarible": {"tags":["image", "gif", "music", "video"], "formats":[".jpg", ".gif", ".mp3", ".mp4"]}
}

# Examples of each NFT  
# "cryptopunks": https://opensea.io/assets/0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb/2566 (Image: JPG)
# "boredapeyachtclub": https://opensea.io/assets/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/8304 (Image: JPG)
# "doodles-official": https://opensea.io/assets/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/7832 (Image: JPG)
# "boonjiproject": https://opensea.io/assets/0x4cd0ea8b1bdb5ab9249d96ccf3d8a0d3ada2bc76/7692 (Image: JPG)
# "fidenza-by-tyler-hobbs": https://opensea.io/assets/0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270/78000895 (Image: JPG)
# "lostpoets": https://opensea.io/assets/0x4b3406a41399c7fd2ba65cbc93697ad9e7ea61e5/5542 (Image: JPG)
# "superrare": (Video) https://opensea.io/assets/0xb932a70a57673d89f4acffbe830e8ed7f75fb9e0/12325 (Video: MP4)
#              (GIF) https://opensea.io/assets/0xb932a70a57673d89f4acffbe830e8ed7f75fb9e0/12335 (GIF: GIF)
#              (Image) https://opensea.io/assets/0xb932a70a57673d89f4acffbe830e8ed7f75fb9e0/22553 (Image: JPG)
# "song-a-day": https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/27853175353995272517766450193869818424107874020190547876689048363464159920129 (MP4)
# "eulerbeats-enigma": https://opensea.io/assets/0xa98771a46dcb34b34cdad5355718f8a97c8e603e/244847083777 (MP4)
# "the-weeknd-x-strangeloop-studio": https://opensea.io/assets/0x0c7d5d65024bf684bcd313e885a00b2057ba7918/20600010459 (MP4)
# "spottiewifi": "https://opensea.io/assets/0xa0e1b198bcc877a950a29512ab5c0ce1bb964c97/311" 
# "jinglebe-nft-collection": https://opensea.io/assets/0x9951f5da4f4f21b7d39a80bc665edf31bd515009/116
# "async-music":https://opensea.io/assets/0x3e43944d977dea22511da6d33c0cab666a604515/630
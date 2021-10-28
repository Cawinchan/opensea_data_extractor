import json
from io import BytesIO
import requests
from PIL import Image
import mimetypes
import urllib.request
import os
import logging


from opensea_local.models.asset import Asset

def download_all_nft_assets(dir="data/raw/json",output_dir="data/raw/contents"):    
    # Iterate over files in directory
    counter = 0
    print("number of files",len(os.listdir(dir)))
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        # Checking if it is a file
        if os.path.isfile(f):
            print("looking through {} file_num: {}".format(f,counter))
            counter += 1
            file = open(f, "r")
            asset = Asset(json.loads(file.read()))
            
            # Ensure ouput dir exists, else skip
            os.makedirs(output_dir,exist_ok=True)
            # Downlaod Image/Animation assets 
            try:
                url = asset.image_url
                response = requests.get(url)
                content_type = response.headers['content-type']
                extension = mimetypes.guess_extension(content_type)
                try:    
                    with open("{}/{}_{}{}".format(output_dir,asset.collection_slug,asset.token_id,extension), 'wb') as f:
                        f.write(response.content)
                except:
                    pass
                try:
                    urllib.request.urlretrieve(url, "{}/{}_{}{}".format(output_dir,asset.collection_slug,asset.token_id,extension)) 
                except:
                    pass
            except Exception as image_inst:
                    logging.debug('{} was unable to be downloaded, error: {}'.format(asset.image_url,image_inst))
                    print(url,image_inst) 
            try:
                url = asset.animation_url
                response = requests.get(url)
                content_type = response.headers['content-type']
                extension = mimetypes.guess_extension(content_type)
                try:    
                    with open("{}/{}_{}{}".format(output_dir,asset.collection_slug,asset.token_id,extension), 'wb') as f:
                        f.write(response.content)
                except:
                    pass
                try:
                    urllib.request.urlretrieve(url, "{}/{}_{}{}".format(output_dir,asset.collection_slug,asset.token_id,extension)) 
                except:
                    pass
            except Exception as animation_inst:
                    logging.debug('{} was unable to be downloaded, error: {}'.format(asset.animation_url,animation_inst))
                    print(url,animation_inst) 
            # Closing file
            file.close()
            # break
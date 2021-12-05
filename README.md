# Project Numpie 

## Data Collector / Data Visualiser / Model Evaluator

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

1. Specify collection information and the expected formats (.jpg,.gif,.mp3,.mp4) found on Opensea in 

src/nft_collection.py
```python
collection = {
    "cryptopunks": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB",             # (Image: JPG)       [Opensea: Art, Rank #1, last 7 days]
    "boredapeyachtclub": "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",       # (Image: JPG)       [Art, Rank #2, last 7 days]
}

nft_format = {
    "cryptopunks": {"tags":"image", "formats":".jpg"},
    "boredapeyachtclub":  {"tags":"image", "formats":".jpg"},
```

2. Specify configurations in main.py and run to download new data

```python
def main(collection
        , number_of_nfts_per_collection=5000
        , maximum_nfts_checked=30
        , order_direction="desc"
        , order_by="sale_date"
        , dir="data/raw/json"
        , output_json_dir="data/preprocessed/json"
        , output_media_dir="data/preprocessed/media"):
    '''
        args:
        collection(dict):  collection dictionary (key: nft collection_name value: c)
        number_of_nfts_per_collection(int): maximum possible nft to download for each collection
        order_direction(str): Available options are "asc" ascending, "desc"ex decending
        order_by(str): Available options are 'token_id', 'sale_date', 'sale_count', 'sale_price'.
        dir(str): location of jsons
        output_media_dir(str): location of output media
    '''
    nft_download(collection,number_of_nfts_per_collection, order_direction, order_by) # Downloads Jsons from Opensea and places them in /data/raw/json
    extract_media(dir,output_json_dir,output_media_dir) # Extracts important metadata and download and convert media data to our expected format
    check_lengths(output_json_dir,output_media_dir) # Ensures that our media downloaded corresponds to our json downloaded
    print("Done!") # Data is now in data/preprocessed
    return

if __name__ == "__main__":
    main(collection)
```


Retrieving assets:

```python
from opensea_local import get_assets

# This will return a list of assets which you can iterate and get the needed data
asset_list = get_assets(limit=10, verified_only=False)

asset = asset_list[0] # Get the first asset obejct from the list

print(asset.name)
print(asset.description)
print(asset.asset_url)
print(asset.get_floor_price()) # Floor price of the collection
```

Retrieving bundles:

```python
from opensea_local import get_bundles

# This will return a list of assets which you can iterate and get the needed data
bundles_list = get_bundles(limit=10)

bundle = bundles_list[0] # Get the first asset obejct from the list

print(bundle.slug)
print(bundle.assets[0].name)
```


# Data Collection

<p align="center">
  <img src="https://github.com/Cawinchan/project_numpie/blob/main/data/NFT_Data_Collection_update.png">
</p>

## Preprocessed NFT Metadata

{
  "RID": "1234",
  "name": "NFT Name",
  "description": "NFT Description",
  "collection_name": "Collection Name",
  "collection_description": "Collection Description",
  "eth_price": 9000000000000000000,
  "eth_price_decimal": 18,
  "usd_price": 1200.89,
  "creation_time": "2021-07-22T10:16:28",
  "transaction_time": "2021-07-23T10:16:28",
  "media_filenames": ["1234.mp4", "1234.mp3"],
  "has_audio_in_video": false,
}

## RAW NFT Metadata

- Important Attributes
    - `string` **uid**: generated
    - `string` **token_id**: Unique NFT ID per Collection
    - `int` **num_sales**: Tracks number of times this NFT has been sold
    - **background_color**: Can be used with the NFT image in the foreground
    - `string` **name**: Textual data
    - `string` **description**: NFT Description. May not always be unique, can be repeated from collection description, can be null
    - `string` **asset_contract**: All NFTs in the collection follow this contract 
    - **collection**: Collection Data
      - **traits**: Collection settings for traits
      - **stats**: Can be empty. One, seven, thirty day data at point of query and total_sales, total_supply and total_volume for Collection.
        - ~~
        - ~~
      - **chat_url**: can be null, social media data
      - **description**: Collection Description
      - **discord_url**: can be null
      - **external_url**: can be null
      - **medium_username**: can be null
      - **slug**": Collection name used on opensea
      - **telegram_url**: can be null
      - **twitter_username**: can be null
      - **instagram_username**: can be null
      - **wiki_url**: can be null
    - **traits**: NFT Traits 
    - **last_sale**:
        - **event_type**: Sales status 
        - **event_timestamp**: sales timestamp
        - **total_price**: Price paid for NFT (floating point is removed, needs to be divided by payment token decimals)
        - **payment_token**: 
          - **symbol**: "ETH"
          - **name**: "Ether"
          - **decimals**: Number of decimals removed to get rid of floating point
          - `int` **Close**: ETH price 
          - `int` **Volume**: ETH Volume
          - `int` **Marketcap**: ETH MarketCap

Credits to 

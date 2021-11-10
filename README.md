# Opensea API

An API wrapper library for opensea api.

## Installation

```bash
pip3 install opensea
```

## Usage

Retrieving assets:

```python
from opensea import get_assets

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
from opensea import get_bundles

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

## NFT Metadata

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

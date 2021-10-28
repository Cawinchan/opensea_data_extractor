from src.data_extraction.nft_downloader import nft_download
from src.data_preprocess.preprocess_data import download_all_nft_assets

from src.nft_collection import collection

def main(collection, number_of_nfts_per_collection=30, maximum_nfts_checked=30, order_direction="asc",dir="data/raw/json", output_image_dir="data/raw/contents"):
    # nft_download(collection,number_of_nfts_per_collection,maximum_nfts_checked, order_direction)
    # download_all_nft_assets(dir,output_image_dir)
    return

if __name__ == "__main__":
    main(collection)
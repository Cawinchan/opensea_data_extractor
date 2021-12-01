from src.data_download.nft_downloader import nft_download
from src.data_preprocess.preprocess_data import extract_media, check_lengths
import subprocess
import ffmpeg
from src.nft_collection import collection


def main(collection, number_of_nfts_per_collection=5000, maximum_nfts_checked=30, order_direction="desc", order_by="sale_date",dir="data/raw/json",output_json_dir="data/preprocessed/json",output_media_dir="data/preprocessed/media"):
    '''
        args:
        collection(dict): key: nft collection name value: nft collection address
        number_of_nfts_per_collection(int): maximum possible nft's in a collection
        maximum_nfts_checked(int): after this number of nft's are checked we end the loop, at 
        order_direction(str): Available options are "asc" ascending, "desc"ex decending
        order_by(str): Available options are 'token_id', 'sale_date', 'sale_count', 'sale_price'.
        dir(str): location of jsons
        output_media_dir(str): location of output media
    
    '''
    nft_download(collection,number_of_nfts_per_collection,maximum_nfts_checked, order_direction, order_by)
    extract_media(dir,output_json_dir,output_media_dir)
    check_lengths(output_json_dir,output_media_dir)
    print("Done!")
    return


if __name__ == "__main__":
    main(collection)
    
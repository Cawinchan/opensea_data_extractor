from opensea.models.account import Account
from requests import request


class Asset:
    def __init__(self, json_data):
        """
        Put useful information from json_data into their own variables under Asset class.

        :param json_data: json object returned by the opensea-api
        :type json_data: dict
        """

        # ASSET DETAILS
        self.name = json_data["name"]
        self.description = json_data["description"]
        self.token_id = json_data["token_id"]
        self.asset_url = json_data["permalink"]
        self.image_url = json_data["image_url"] # Note image_url instead of orignal choosen
        # TODO: compare which one we should take Image_url or Image
        self.image_original_url = json_data["image_original_url"] # Note image_url instead of orignal choosen
        try:
            self.animation_url = json_data["animation_url"] # Can be the same as image_url
            self.animation_original_url = json_data["animation_original_url"] # Can be the same as image_url
        except:
            self.animation_url = None
            self.animation_original_url = None
        if self.image_url == self.animation_url:
            self.animation_url = None

        self.contract_address = json_data["asset_contract"]["address"] 

        # COLLECTION DETAILS
        self.collection_name = json_data["collection"]["name"]
        self.collection_description = json_data["collection"]["description"]
        self.collection_slug = json_data["collection"]["slug"]
        self.verification_status = json_data["collection"]["safelist_request_status"]
        self.is_verified = json_data["collection"]["safelist_request_status"] == "verified"

        # STATS DETAILS
        self.average_price = json_data["collection"]["stats"]["average_price"]
        self.count = json_data["collection"]["stats"]["count"]
        self.floor_price = json_data["collection"]["stats"]["floor_price"]
        self.market_cap = json_data["collection"]["stats"]["market_cap"]
        self.num_owners = json_data["collection"]["stats"]["num_owners"]
        self.one_day_average_price = json_data["collection"]["stats"]["one_day_average_price"]
        self.one_day_change = json_data["collection"]["stats"]["one_day_change"]
        self.one_day_sales = json_data["collection"]["stats"]["one_day_sales"]
        self.one_day_volume = json_data["collection"]["stats"]["one_day_volume"]
        self.seven_day_average_price = json_data["collection"]["stats"]["seven_day_average_price"]
        self.seven_day_change = json_data["collection"]["stats"]["seven_day_change"]
        self.seven_day_sales = json_data["collection"]["stats"]["seven_day_sales"]
        self.seven_day_volume = json_data["collection"]["stats"]["seven_day_volume"]
        self.thirty_day_average_price = json_data["collection"]["stats"]["thirty_day_average_price"]
        self.thirty_day_change = json_data["collection"]["stats"]["thirty_day_change"]
        self.thirty_day_sales = json_data["collection"]["stats"]["thirty_day_sales"]
        self.thirty_day_volume = json_data["collection"]["stats"]["thirty_day_volume"]
        self.total_sales = json_data["collection"]["stats"]["total_sales"]
        self.total_supply = json_data["collection"]["stats"]["total_supply"]
        self.total_volume = json_data["collection"]["stats"]["total_volume"]

        # LAST SALE DETAILS
        self.sale_timestamp = json_data["last_sale"]["event_timestamp"] 
        self.eth_usd_price = json_data["last_sale"]["payment_token"]["usd_price"] # Current price of eth
        self.last_sale_decimals = json_data["last_sale"]["payment_token"]["decimals"]
        try:
            self.last_sale = json_data["last_sale"]["total_price"]

        except:
            print("asset: {}, token_id: {} has no last sale".format(self.name, self.token_id)) 
            self.last_sale = 0

        # SOCIAL MEDIA DETAILS
        try:
            self.discord_url = json_data["collection"]["discord_url"]
        except:
            self.discord_url = None
        try:
            self.twitter_username = json_data["collection"]["twitter_username"]
        except:
            self.twitter_username = None
        try:
            self.instagram_username = json_data["collection"]["instagram_username"]
        except:
            self.instagram_username = None
        try:
            self.telegram_url = json_data["collection"]["telegram_url"]
        except: 
            self.telegram_url = None

        # OWNER DETAILS
        self.owner = Account(json_data["owner"])

        self.__ASSET_API_URL = f"https://api.opensea.io/api/v1/asset/{self.contract_address}/{self.token_id}"

    def get_json(self):
        response = request("GET", self.__ASSET_API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_event_json(self):
        response = request("GET", self.__ASSET_API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_floor_price(self):
        """
        Returns the floor price of the collection an asset belongs to
        """
        asset_json = self.get_json()
        floor_price = asset_json["collection"]["stats"]["floor_price"]
        return floor_price

    def get_current_price(self):
        asset_json = self.get_json()
        try:
            current_price = asset_json["orders"][0]["current_price"]
        except:
            current_price = None
        return current_price

    def get_average_price(self):
        asset_json = self.get_json()
        average_price = asset_json["collection"]["stats"]["average_price"]
        return average_price

    


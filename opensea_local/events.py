from typing import List, Union
from requests.models import Response

from opensea_local.common import get_opensea

def get_events(
    asset_contract_address: str = "",
    collection: str = "",
    token_id: int = 0,
    account_address: str = "",
    event_type: str = "",
    only_opensea: bool = False,
    auction_type: str = "",
    offset: int = 0,
    limit: int = 10
):
    """
    Retrieves NFT assets from opensea.io.

    :param owner: The address for the owner of the assets.
    :type owner: str

    asset_contract_address: The NFT contract address for the assets for which to show events
    string

    collection_slug: Limit responses to events from a collection. Case sensitive and must match the collection slug exactly. Will return all assets from all contracts in a collection. For more information on collections, see our collections documentation.
    string

    token_id: The token's id to optionally filter by
    int32

    account_address: A user account's wallet address to filter for events on an account
    string
    
    event_type: The event type to filter. Can be created for new auctions, successful for sales, cancelled, bid_entered, bid_withdrawn, transfer, or approve
    string
    
    only_opensea: Restrict to events on OpenSea auctions. Can be true or false
    boolean

    auction_type: Filter by an auction type. Can be english for English Auctions, dutch for fixed-price and declining-price sell orders (Dutch Auctions), or min-price for CryptoPunks bidding auctions.
    string

    offset: Offset for pagination
    int32

    limit: Limit for pagination
    string

    occurred_before (not implemented): Only show events listed before this timestamp. Seconds since the Unix epoch.
    date-time

    occurred_after (not implemented): Only show events listed after this timestamp. Seconds since the Unix epoch.
    date-time
    """

    api_parameters = {
        "asset_contract_address": asset_contract_address,
        "token_id": token_id,
        # "account_address": account_address,
        "event_type": event_type,
        "only_opensea": only_opensea,
        # "auction_type": auction_type,
        "offset": offset,
        "limit": limit
    }

    response = get_opensea("events", **api_parameters)

    return response

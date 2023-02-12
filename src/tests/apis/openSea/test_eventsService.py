import requests
import unittest
from unittest.mock import patch, MagicMock
from helpers.dateHelpers import getDateObject
from apis.openSea.eventsService import EventsService

mockUrl = 'mockUrl'
mockHeaders = {}

class TestEventsService(unittest.TestCase):
    @classmethod
    def setUpClass(self):
      self.patch1 = patch('requests.get')
      self.mock_get = self.patch1.start()

      self.eventsService = EventsService()

      self.addClassCleanup(self.patch1.stop)

    @classmethod
    def tearDownClass(self):
      self.patch1.stop()

    def setUp(self):
      mock_response = MagicMock(spec=requests.Response)
      mock_response.status_code = 200
      mock_response.ok = True
      mock_response.json.return_value = mockData1

      self.mock_get.return_value = mock_response
    
    def setUp2(self):
      mock_response = MagicMock(spec=requests.Response)
      mock_response.status_code = 500
      mock_response.ok = False
      mock_response.json.return_value = {}

      self.mock_get.return_value = mock_response

    def setUp3(self):
      mock_response = MagicMock(spec=requests.Response)
      mock_response.status_code = 200
      mock_response.ok = True
      mock_response.json.return_value = mockData2

      self.mock_get.return_value = mock_response

    def test_getRequestReturnsSuccess_mapsEventsCorrectly(self):
      self.setUp()
      result = self.eventsService.getEvents(mockUrl, mockHeaders)

      self.assertEqual(len(result['assetEvents']), 2)
    
    def test_getRequestReturnsError_ReturnsEmptyEvents(self):
      self.setUp2()
      result = self.eventsService.getEvents(mockUrl, mockHeaders)

      self.assertEqual(result['next'], None)
      self.assertEqual(len(result['assetEvents']), 0)
    
    def test_mapsEventsCorrectly_whenAssetEventsIsEmpty(self):
      self.setUp3()
      result = self.eventsService.getEvents(mockUrl, mockHeaders)

      self.assertEqual(result['next'], None)
      self.assertEqual(len(result['assetEvents']), 0)

    def test_mapsEventsCorrectly_propertiesAreAssignedCorrectly(self):
      self.setUp()
      result = self.eventsService.getEvents(mockUrl, mockHeaders)

      self.assertEqual(result['assetEvents'][0]['tokenId'], '38')
      self.assertEqual(result['assetEvents'][0]['eventTimestamp'], getDateObject('2023-01-09T05:50:11'))
      self.assertEqual(result['assetEvents'][0]['totalPrice'], '536800000000000000')
      self.assertEqual(result['assetEvents'][0]['paymentToken'], 'ETH')

mockData2 = {
  'next': None,
  'asset_events': []
}

mockData1 = {
  'next': 'LWV2ZW50X3RpbWVzdGFtcD0yMDIzLTAxLTA4KzEwJTNBNDclM0E0NyYtZXZlbnRfdHlwZT1zdWNjZXNzZnVsJi1waz05MTYzNDE5ODA3',
  'previous': 'cj0xJi1ldmVudF90aW1lc3RhbXA9MjAyMy0wMS0wOSswNSUzQTUwJTNBMTEmLWV2ZW50X3R5cGU9c3VjY2Vzc2Z1bCYtcGs9OTE3OTYwMDM2Mw==',
  'asset_events': [
    {
      'asset': {
        'id': 68008869,
        'token_id': '38',
        'num_sales': 22,
        'background_color': None,
        'image_url': 'https://i.seadn.io/gcs/files/7a6fbab38872685b34026d826634a0c7.png?w=500&auto=format',
        'image_preview_url': 'https://i.seadn.io/gcs/files/7a6fbab38872685b34026d826634a0c7.png?w=500&auto=format',
        'image_thumbnail_url': 'https://i.seadn.io/gcs/files/7a6fbab38872685b34026d826634a0c7.png?w=500&auto=format',
        'image_original_url': 'ipfs://QmazkShEyjjY7nghpPGZV6Zp4gbXCG6zBTMegJw257wM1X/darkbrown_darkbrown_white_white_darkbrown_white_A_4A_2A_1A_1A_1A_3A_0_0_0_0_0_0_0789.png',
        'animation_url': None,
        'animation_original_url': None,
        'name': 'Meka #38',
        'description': 'Meka from the MekaVerse - A collection of 8,888 unique generative NFTs from an other universe.',
        'external_link': None,
        'asset_contract': {
          'address': '0x9a534628b4062e123ce7ee2222ec20b86e16ca8f',
          'asset_contract_type': 'non-fungible',
          'created_date': '2021-10-07T20:21:56.075677',
          'name': 'MekaVerse',
          'nft_version': '3.0',
          'opensea_version': None,
          'owner': 89919527,
          'schema_name': 'ERC721',
          'symbol': 'MEKA',
          'total_supply': '0',
          'description': 'The MekaVerse is a collection of 8,888 generative Mekas inspired by the Japanese Anime universe. View the collection at https://themekaverse.com/gallery.\n\nIn the distant future, drivers fight in a world divided into 4 Factions. Originals Meka, Mirage, F9, and Gadians are the Titans who rule this planet. Which Faction are you going to join?\n\nWorld map: https://worldmap.themekaverse.com/\n\nVisit https://themekaverse.com/ for more details.',
          'external_link': 'https://themekaverse.com/',
          'image_url': 'https://i.seadn.io/gae/SFCYIPlcznnwFnI8Jd0dYIh5Atr6cp7HL4tWVWUl7_Onikq7uzQxKfTjdK2ptilWALg1ZBttSvzhXBCUbB9qoSlW9kS8qk1S3Z3xkU0?w=500&auto=format',
          'default_to_fiat': False,
          'dev_buyer_fee_basis_points': 0,
          'dev_seller_fee_basis_points': 250,
          'only_proxied_transfers': False,
          'opensea_buyer_fee_basis_points': 0,
          'opensea_seller_fee_basis_points': 250,
          'buyer_fee_basis_points': 0,
          'seller_fee_basis_points': 500,
          'payout_address': '0xeb0f137fba2bbd521d81e158b64ace1a88093ad9'
        },
        'permalink': 'https://opensea.io/assets/ethereum/0x9a534628b4062e123ce7ee2222ec20b86e16ca8f/38',
        'collection': {
          'banner_image_url': 'https://i.seadn.io/gcs/files/88fd15373720c7962013981bac2da119.jpg?w=500&auto=format',
          'chat_url': None,
          'created_date': '2021-10-07T20:29:17.017760+00:00',
          'default_to_fiat': False,
          'description': 'The MekaVerse is a collection of 8,888 generative Mekas inspired by the Japanese Anime universe. View the collection at https://themekaverse.com/gallery.\n\nIn the distant future, drivers fight in a world divided into 4 Factions. Originals Meka, Mirage, F9, and Gadians are the Titans who rule this planet. Which Faction are you going to join?\n\nWorld map: https://worldmap.themekaverse.com/\n\nVisit https://themekaverse.com/ for more details.',
          'dev_buyer_fee_basis_points': '0',
          'dev_seller_fee_basis_points': '250',
          'discord_url': 'https://discord.gg/mekaverse',
          'display_data': {
            'card_display_style': 'cover',
            'images': None
          },
          'external_url': 'https://themekaverse.com/',
          'featured': False,
          'featured_image_url': None,
          'hidden': False,
          'safelist_request_status': 'verified',
          'image_url': 'https://i.seadn.io/gae/SFCYIPlcznnwFnI8Jd0dYIh5Atr6cp7HL4tWVWUl7_Onikq7uzQxKfTjdK2ptilWALg1ZBttSvzhXBCUbB9qoSlW9kS8qk1S3Z3xkU0?w=500&auto=format',
          'is_subject_to_whitelist': False,
          'large_image_url': None,
          'medium_username': None,
          'name': 'MekaVerse',
          'only_proxied_transfers': False,
          'opensea_buyer_fee_basis_points': '0',
          'opensea_seller_fee_basis_points': '250',
          'payout_address': '0xeb0f137fba2bbd521d81e158b64ace1a88093ad9',
          'require_email': False,
          'short_description': None,
          'slug': 'mekaverse',
          'telegram_url': None,
          'twitter_username': 'MekaVerse',
          'instagram_username': None,
          'wiki_url': None,
          'is_nsfw': False,
          'fees': {
            'seller_fees': {
              '0xeb0f137fba2bbd521d81e158b64ace1a88093ad9': 250
            },
            'opensea_fees': {
              '0x0000a26b00c1f0df003000390027140000faa719': 250
            }
          },
          'is_rarity_enabled': False,
          'is_creator_fees_enforced': True
        },
        'decimals': 0,
        'token_metadata': 'https://ipfs.io/ipfs/Qmcob1MaPTXUZt5MztHEgsYhrf7R6G7wV8hpcweL8nEfgU/meka/38',
        'is_nsfw': False,
        'owner': None
      },
      'asset_bundle': None,
      'event_type': 'successful',
      'event_timestamp': '2023-01-09T05:50:11',
      'auction_type': None,
      'total_price': '536800000000000000',
      'payment_token': {
        'symbol': 'ETH',
        'address': '0x0000000000000000000000000000000000000000',
        'image_url': 'https://openseauserdata.com/files/6f8e2979d428180222796ff4a33ab929.svg',
        'name': 'Ether',
        'decimals': 18,
        'eth_price': '1.000000000000000',
        'usd_price': '1592.640000000000100000'
      },
      'transaction': {
        'block_hash': '0xd3080631cb97992e5eccc254159f2c1af3092fc67440c33823d596574901612a',
        'block_number': '16367259',
        'from_account': {
          'user': {
            'username': None
          },
          'profile_img_url': 'https://storage.googleapis.com/opensea-static/opensea-profile/26.png',
          'address': '0xef4c7d3bfa35c94e67fed5a9083d998af4608c83',
          'config': ''
        },
        'id': 980836443,
        'timestamp': '2023-01-09T05:50:11',
        'to_account': {
          'user': None,
          'profile_img_url': 'https://storage.googleapis.com/opensea-static/opensea-profile/11.png',
          'address': '0x00000000006c3852cbef3e08e8df289169ede581',
          'config': ''
        },
        'transaction_hash': '0x8fa0e996a6e82a145618e3514f936d4988086a7f1b24f861a192b04f87faa525',
        'transaction_index': '120'
      },
      'created_date': '2023-01-09T05:50:15.785621',
      'quantity': '1',
      'approved_account': None,
      'bid_amount': None,
      'collection_slug': 'mekaverse',
      'contract_address': '0x00000000006c3852cbef3e08e8df289169ede581',
      'custom_event_name': None,
      'dev_fee_payment_event': None,
      'dev_seller_fee_basis_points': 250,
      'duration': None,
      'ending_price': None,
      'from_account': None,
      'id': 9179600363,
      'is_private': False,
      'owner_account': None,
      'seller': {
        'user': {
          'username': '786Nadeem'
        },
        'profile_img_url': 'https://storage.googleapis.com/opensea-static/opensea-profile/10.png',
        'address': '0x5cbffebdf2f12a8984b9eff74a85acab24730fff',
        'config': ''
      },
      'starting_price': None,
      'to_account': None,
      'winner_account': {
        'user': {
          'username': None
        },
        'profile_img_url': 'https://storage.googleapis.com/opensea-static/opensea-profile/26.png',
        'address': '0xef4c7d3bfa35c94e67fed5a9083d998af4608c83',
        'config': ''
      },
      'listing_time': '2023-01-09T00:54:56'
    },
    {
      'asset': {
        'id': 67757048,
        'token_id': '805',
        'num_sales': 2,
        'background_color': None,
        'image_url': 'https://i.seadn.io/gcs/files/0e85201b0b34096d65176e1f4a34e1a5.png?w=500&auto=format',
        'image_preview_url': 'https://i.seadn.io/gcs/files/0e85201b0b34096d65176e1f4a34e1a5.png?w=500&auto=format',
        'image_thumbnail_url': 'https://i.seadn.io/gcs/files/0e85201b0b34096d65176e1f4a34e1a5.png?w=500&auto=format',
        'image_original_url': 'ipfs://QmPoibhmrpzR7UKmQeT7SxYesQChjeXSp3xxSu2oszn9pm/bluegrey_bluegrey_white_white_pink_pastelblue_A_4A_1A_10A_2A_1A_2A_0_0_0_0_0_0_0256.png',
        'animation_url': None,
        'animation_original_url': None,
        'name': 'Meka #805',
        'description': 'Meka from the MekaVerse - A collection of 8,888 unique generative NFTs from an other universe.',
        'external_link': None,
        'asset_contract': {
          'address': '0x9a534628b4062e123ce7ee2222ec20b86e16ca8f',
          'asset_contract_type': 'non-fungible',
          'created_date': '2021-10-07T20:21:56.075677',
          'name': 'MekaVerse',
          'nft_version': '3.0',
          'opensea_version': None,
          'owner': 89919527,
          'schema_name': 'ERC721',
          'symbol': 'MEKA',
          'total_supply': '0',
          'description': 'The MekaVerse is a collection of 8,888 generative Mekas inspired by the Japanese Anime universe. View the collection at https://themekaverse.com/gallery.\n\nIn the distant future, drivers fight in a world divided into 4 Factions. Originals Meka, Mirage, F9, and Gadians are the Titans who rule this planet. Which Faction are you going to join?\n\nWorld map: https://worldmap.themekaverse.com/\n\nVisit https://themekaverse.com/ for more details.',
          'external_link': 'https://themekaverse.com/',
          'image_url': 'https://i.seadn.io/gae/SFCYIPlcznnwFnI8Jd0dYIh5Atr6cp7HL4tWVWUl7_Onikq7uzQxKfTjdK2ptilWALg1ZBttSvzhXBCUbB9qoSlW9kS8qk1S3Z3xkU0?w=500&auto=format',
          'default_to_fiat': False,
          'dev_buyer_fee_basis_points': 0,
          'dev_seller_fee_basis_points': 250,
          'only_proxied_transfers': False,
          'opensea_buyer_fee_basis_points': 0,
          'opensea_seller_fee_basis_points': 250,
          'buyer_fee_basis_points': 0,
          'seller_fee_basis_points': 500,
          'payout_address': '0xeb0f137fba2bbd521d81e158b64ace1a88093ad9'
        },
        'permalink': 'https://opensea.io/assets/ethereum/0x9a534628b4062e123ce7ee2222ec20b86e16ca8f/805',
        'collection': {
          'banner_image_url': 'https://i.seadn.io/gcs/files/88fd15373720c7962013981bac2da119.jpg?w=500&auto=format',
          'chat_url': None,
          'created_date': '2021-10-07T20:29:17.017760+00:00',
          'default_to_fiat': False,
          'description': 'The MekaVerse is a collection of 8,888 generative Mekas inspired by the Japanese Anime universe. View the collection at https://themekaverse.com/gallery.\n\nIn the distant future, drivers fight in a world divided into 4 Factions. Originals Meka, Mirage, F9, and Gadians are the Titans who rule this planet. Which Faction are you going to join?\n\nWorld map: https://worldmap.themekaverse.com/\n\nVisit https://themekaverse.com/ for more details.',
          'dev_buyer_fee_basis_points': '0',
          'dev_seller_fee_basis_points': '250',
          'discord_url': 'https://discord.gg/mekaverse',
          'display_data': {
            'card_display_style': 'cover',
            'images': None
          },
          'external_url': 'https://themekaverse.com/',
          'featured': False,
          'featured_image_url': None,
          'hidden': False,
          'safelist_request_status': 'verified',
          'image_url': 'https://i.seadn.io/gae/SFCYIPlcznnwFnI8Jd0dYIh5Atr6cp7HL4tWVWUl7_Onikq7uzQxKfTjdK2ptilWALg1ZBttSvzhXBCUbB9qoSlW9kS8qk1S3Z3xkU0?w=500&auto=format',
          'is_subject_to_whitelist': False,
          'large_image_url': None,
          'medium_username': None,
          'name': 'MekaVerse',
          'only_proxied_transfers': False,
          'opensea_buyer_fee_basis_points': '0',
          'opensea_seller_fee_basis_points': '250',
          'payout_address': '0xeb0f137fba2bbd521d81e158b64ace1a88093ad9',
          'require_email': False,
          'short_description': None,
          'slug': 'mekaverse',
          'telegram_url': None,
          'twitter_username': 'MekaVerse',
          'instagram_username': None,
          'wiki_url': None,
          'is_nsfw': False,
          'fees': {
            'seller_fees': {
              '0xeb0f137fba2bbd521d81e158b64ace1a88093ad9': 250
            },
            'opensea_fees': {
              '0x0000a26b00c1f0df003000390027140000faa719': 250
            }
          },
          'is_rarity_enabled': False,
          'is_creator_fees_enforced': True
        },
        'decimals': 0,
        'token_metadata': 'https://ipfs.io/ipfs/Qmcob1MaPTXUZt5MztHEgsYhrf7R6G7wV8hpcweL8nEfgU/meka/805',
        'is_nsfw': False,
        'owner': None
      },
      'asset_bundle': None,
      'event_type': 'successful',
      'event_timestamp': '2023-01-09T04:38:47',
      'auction_type': None,
      'total_price': '500000000000000000',
      'payment_token': {
        'symbol': 'ETH',
        'address': '0x0000000000000000000000000000000000000000',
        'image_url': 'https://openseauserdata.com/files/6f8e2979d428180222796ff4a33ab929.svg',
        'name': 'Ether',
        'decimals': 18,
        'eth_price': '1.000000000000000',
        'usd_price': '1592.640000000000100000'
      },
      'transaction': {
        'block_hash': '0x462e479641a341635e513df493548d7c079c1c5ef4f3dacac6fdaf2fbf64060f',
        'block_number': '16366904',
        'from_account': {
          'user': {
            'username': 'kelox'
          },
          'profile_img_url': 'https://storage.googleapis.com/opensea-static/opensea-profile/31.png',
          'address': '0x8c0c78e6e81510b96fe34483c05ee203a1f0457b',
          'config': ''
        },
        'id': 980337302,
        'timestamp': '2023-01-09T04:38:47',
        'to_account': {
          'user': None,
          'profile_img_url': 'https://storage.googleapis.com/opensea-static/opensea-profile/11.png',
          'address': '0x00000000006c3852cbef3e08e8df289169ede581',
          'config': ''
        },
        'transaction_hash': '0xaf7030d100cc07924b56dbcfc54a11e166f306240cfba3091c823268c152a4a4',
        'transaction_index': '60'
      },
      'created_date': '2023-01-09T04:38:53.133102',
      'quantity': '1',
      'approved_account': None,
      'bid_amount': None,
      'collection_slug': 'mekaverse',
      'contract_address': '0x00000000006c3852cbef3e08e8df289169ede581',
      'custom_event_name': None,
      'dev_fee_payment_event': None,
      'dev_seller_fee_basis_points': 250,
      'duration': None,
      'ending_price': None,
      'from_account': None,
      'id': 9178602605,
      'is_private': False,
      'owner_account': None,
      'seller': {
        'user': {
          'username': 'Jam-5'
        },
        'profile_img_url': 'https://storage.googleapis.com/opensea-static/opensea-profile/12.png',
        'address': '0xfbf709d114eac3776ccd7969265b9fe0d382946d',
        'config': ''
      },
      'starting_price': None,
      'to_account': None,
      'winner_account': {
        'user': {
          'username': 'kelox'
        },
        'profile_img_url': 'https://storage.googleapis.com/opensea-static/opensea-profile/31.png',
        'address': '0x8c0c78e6e81510b96fe34483c05ee203a1f0457b',
        'config': ''
      },
      'listing_time': '2023-01-08T22:15:18'
    }
  ]
}
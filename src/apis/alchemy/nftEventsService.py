import json
from pprint import pprint
import requests
from apis.alchemy.nftEventsDataClasses import Fee, GetEvents, NFTEvent
from helpers.getEnvVariables import getEnvVariables


class NFTEventsService:
    envVariables = getEnvVariables()

    def getNFTEvents(self, contractAddress: str, fromBlock: int, pageKey=None) -> GetEvents:
        path = 'nft/v3/{0}/getNFTSales'.format(
            self.envVariables.ALCHEMY_API_KEY)
        url = '{0}/{1}'.format(self.envVariables.ALCHEMY_API_URL, path)
        headers = {"accept": "application/json"}

        parameters = {
            'fromBlock': fromBlock,
            'toBlock': 'latest',
            'order': 'asc',
            'contractAddress': contractAddress,
        }

        if pageKey:
            parameters['pageKey'] = pageKey

        response = requests.get(url=url,
                                headers=headers, params=parameters)

        # print(json.loads(response._content.decode('utf-8')))

        if response.ok:
            return self.__getEventsMapper(json.loads(response._content.decode('utf-8')))
        else:
            pprint(vars(response))
            raise Exception('Could not get events')

    def __getEventsMapper(self, response) -> GetEvents:
        return GetEvents(
            response['pageKey'],
            self.__eventsMapper(
                response['nftSales'], response['validAt']['blockTimestamp'])
        )

    def __eventsMapper(self, nftSales, blockTimestamp) -> list[NFTEvent]:
        nftEvents: list[NFTEvent] = []

        # TODO: deal with sales that have a quantity of more than 1

        for event in nftSales:
            if event['quantity'] == 1:
                sellerFee = self.__feeMapper(event['sellerFee'])
                protocolFee = self.__feeMapper(event['protocolFee'])
                royaltyFee = self.__feeMapper(event['royaltyFee'])

                nftEvents.append(NFTEvent(
                    event['marketplace'],
                    event['contractAddress'],
                    event['tokenId'],
                    sellerFee,
                    protocolFee,
                    royaltyFee,
                    event['blockNumber'],
                    blockTimestamp
                ))

        return nftEvents

    def __feeMapper(self, fee):
        return Fee(
            fee['amount'],
            fee['tokenAddress'],
            fee['symbol'],
            fee['decimals']
        )

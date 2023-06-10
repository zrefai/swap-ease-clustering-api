import requests
from apis.swapEase.ethBlockByDateDataClasses import EthBlockByDate
from helpers.getEnvVariables import getEnvVariables


class EthBlockByDateService:
    envVariables = getEnvVariables()

    def getDate(self, date: str):
        # TODO: Do more error handling here
        url = self.__urlBuilder(date)

        response = requests.get(url)

        if response.ok:
            return self.__ethBlockByDateMapper(response.json())

        raise Exception('Could not get block by date from swapEaseAPI')

    def __ethBlockByDateMapper(self, response):
        return EthBlockByDate(
            response['date'],
            response['block'],
            response['timestamp'])

    # TODO: Can probably redo this to be more generic
    def __urlBuilder(self, date):
        swapEaseApiUrl = self.envVariables.SWAP_EASE_API_URL

        path = '{0}/ethBlockByDate/getEthBlockByDate'.format(swapEaseApiUrl)

        return '{0}/{1}'.format(path, date)

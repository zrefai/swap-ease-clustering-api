from helpers.dateHelpers import getDateObject

def mockProcessedEvents():
    return {
  '5000': [
    {
      'eventTimestamp': getDateObject('2022-12-07T21:13:47'),
      'paymentToken': 'ETH',
      'tokenId': '5000',
      'totalPrice': '397000000000000000'
    }
  ],
  '5001': [
    {
      'eventTimestamp':  getDateObject('2023-01-06T18:56:35'),
      'paymentToken': 'ETH',
      'tokenId': '5001',
      'totalPrice': '650000000000000000'
    },
    {
      'eventTimestamp':  getDateObject('2022-11-17T08:09:11'),
      'paymentToken': 'WETH',
      'tokenId': '5001',
      'totalPrice': '300000000000000000'
    }
  ],
  '5002': [
    {
      'eventTimestamp':  getDateObject('2022-12-31T08:38:59'),
      'paymentToken': 'ETH',
      'tokenId': '5002',
      'totalPrice': '649000000000000000'
    },
    {
      'eventTimestamp':  getDateObject('2022-12-30T19:52:11'),
      'paymentToken': 'ETH',
      'tokenId': '5002',
      'totalPrice': '386899900000000000'
    },
    {
      'eventTimestamp':  getDateObject('2022-12-30T19:45:47'),
      'paymentToken': 'WETH',
      'tokenId': '5002',
      'totalPrice': '326320000000000000'
    }
  ],
  '5003': [
    {
      'eventTimestamp':  getDateObject('2022-12-01T07:40:35'),
      'paymentToken': 'ETH',
      'tokenId': '5003',
      'totalPrice': '379800000000000000'
    },
    {
      'eventTimestamp':  getDateObject('2022-11-30T11:08:59'),
      'paymentToken': 'WETH',
      'tokenId': '5003',
      'totalPrice': '360400000000000000'
    }
  ],
  '5004': [
    {
      'eventTimestamp':  getDateObject('2022-11-22T14:34:23'),
      'paymentToken': 'ETH',
      'tokenId': '5004',
      'totalPrice': '365000000000000000'
    },
    {
      'eventTimestamp':  getDateObject('2022-11-16T19:35:47'),
      'paymentToken': 'ETH',
      'tokenId': '5004',
      'totalPrice': '265990000000000000'
    },
    {
      'eventTimestamp':  getDateObject('2022-11-16T00:43:11'),
      'paymentToken': 'WETH',
      'tokenId': '5004',
      'totalPrice': '220100000000000000'
    }
  ],
  '5005': [
    {
      'eventTimestamp':  getDateObject('2022-12-05T20:27:11'),
      'paymentToken': 'ETH',
      'tokenId': '5005',
      'totalPrice': '449000000000000000'
    },
    {
      'eventTimestamp':  getDateObject('2022-12-02T23:25:35'),
      'paymentToken': 'ETH',
      'tokenId': '5005',
      'totalPrice': '372500000000000000'
    },
    {
      'eventTimestamp':  getDateObject('2022-12-02T21:07:59'),
      'paymentToken': 'WETH',
      'tokenId': '5005',
      'totalPrice': '332010000000000000'
    }
  ]
}


from connect.client import R
from connect.client import ConnectClient
import json

if __name__ == '__main__':
    client = ConnectClient(api_key='ApiKey SU-650-400-690:cd08ef211ef6bbb38e61b3893cefcfde5f7651a4', endpoint='https://api.connect.cloud.im/public/v1')
    rql = R()
    rql &= R().type.eq('program')
    rql &= R().status.eq('active')
    contracts=client.contracts.filter(rql).agreement.select('marketplace')
    #program_agreement = client.agreements.resource('AGP-437-507-130').agreements.all().first()
    print (json.dumps(contracts))
    exit()
    rights = []
    for contract in contracts:
        #distri_agreements = client.agreements[contract['agreement']['id']].agreements.all().select('marketplace')
        distri_agreements = client.agreements[contract['agreement']['id']].get()['agreements']
        print (json.dumps(distri_agreements))
        exit()
        marketplaces = []
        for distri_agreement in distri_agreements:
            marketplaces.append(
                {
                    'id': distri_agreement['marketplace']['id'],
                    'name': distri_agreement['marketplace']['name']
                }
            )
        output = {
            'contract_id': contract['id'],
            'vendor_id': contract['owner']['id'],
            'vendor_name': contract['owner']['name']
        }
        output['marketplaces'] = marketplaces
        rights.append(output)
        print (json.dumps(rights))
        exit()
        

    print (json.dumps(rights))
    exit()



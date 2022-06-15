from connect.client import R

def generate(
    client=None,
    parameters=None,
    progress_callback=None,
    renderer_type=None,
    extra_context_callback=None,
):
    progress = 0
    rql = R()
    rql &= R().type.eq('program')
    rql &= R().status.eq('active')
    contracts=client.contracts.filter(rql).all()
    total_contracts=contracts.count()
    for contract in contracts:
        distri_agreements = client.agreements[contract['agreement']['id']].agreements.all().select('marketplace')
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
        yield output
        progress += 1
        progress_callback(progress, total_contracts)

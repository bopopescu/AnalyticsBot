expire_synonyms = ['expiration', 'expire', 'expires', 'expiration date', 'expiry date', 'expiry', 'end', 'terminate']
exclude_synonyms = ['exclude', 'excluding', 'remove', 'no', 'not', 'different']
higher_synonyms = ['more', 'greater', 'higher', 'superior', 'surpassing', 'larger', 'above']
crdscode_synonyms = ['crds code', 'crdscode']
client_synonyms = ['clients', 'client', 'client name', 'clients name']
currency_synonyms = ['currency', 'currency pair']
deal_id_synonyms = ['deal', 'deal name', 'deal id', 'deals']
deal_date_synonyms = ['deal date', 'signed', 'date', 'created']
rollover_synonyms = ['rollovered', 'rollover']
rollover_ratio_synonyms = ['rollover ratio', 'rolloverratio']
client_deal_side_synonyms = ['client deal side', 'client deal', 'client side']


def synonym_check(word):

    if word in expire_synonyms:
        return 'expire'
    elif word in exclude_synonyms:
        return 'exclude'
    elif word in higher_synonyms:
        return 'higher'
    elif word in crdscode_synonyms:
        return 'crdscode'
    elif word in client_synonyms:
        return 'client'
    elif word in currency_synonyms:
        return 'currency'
    elif word in deal_id_synonyms:
        return 'deal'
    elif word in deal_date_synonyms:
        return 'date'
    elif word in rollover_synonyms:
        return 'rollover'
    elif word in rollover_ratio_synonyms:
        return 'rolloverratio'
    elif word in rollover_ratio_synonyms:
        return 'client deal'
    else:
        return word

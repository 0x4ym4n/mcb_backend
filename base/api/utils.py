import json

import requests
from django.http import JsonResponse


def getSDKToken(request):
    url = 'https://auth.dev.uqudo.io/api/oauth/token'
    myobj = {'grant_type': 'client_credentials', 'client_id': '90dd6963-5be6-4655-a978-a6abf8e92a66',
             'client_secret': '3hbBAFzNaY86Z2wj6nHo2xMD'}

    x = requests.post(url, data=myobj)

    print(x.text)
    data = x.json()
    return JsonResponse(data)



def company_data_post_request(bvDID):


    payload = json.dumps({
        "WHERE": [
            {
                "BvDID": [
                    bvDID
                ]
            }
        ],
        "SELECT": [
            {
                "NAME": {
                    "AS": "NAME"
                }
            },
            {
                "COUNTRY_ISO_CODE": {
                    "AS": "COUNTRY_ISO_CODE"
                }
            },
            {
                "NACE2_CORE_CODE": {
                    "AS": "NACE2_CORE_CODE"
                }
            },
            {
                "CONSOLIDATION_CODE": {
                    "AS": "CONSOLIDATION_CODE"
                }
            },
            {
                "YEAR_LAST_ACCOUNTS": {
                    "AS": "YEAR_LAST_ACCOUNTS"
                }
            },
            {
                "OPRE": {
                    "CURRENCY": "SESSION",
                    "UNIT": 3,
                    "INDEXORYEAR": "0",
                    "AS": "OPRE"
                }
            },
            {
                "EMPL": {
                    "UNIT": 0,
                    "INDEXORYEAR": "0",
                    "AS": "EMPL"
                }
            },
            {
                "TRADE_DESCRIPTION_EN": {
                    "AS": "TRADE_DESCRIPTION_EN"
                }
            },
            {
                "TRADE_DESCRIPTION_ORIGINAL": {
                    "AS": "TRADE_DESCRIPTION_ORIGINAL"
                }
            },
            {
                "TRADE_DESCRIPTION_LANGUAGE": {
                    "AS": "TRADE_DESCRIPTION_LANGUAGE"
                }
            },
            {
                "PRODUCTS_SERVICES": {
                    "AS": "PRODUCTS_SERVICES"
                }
            },
            {
                "DESCRIPTION_HISTORY": {
                    "AS": "DESCRIPTION_HISTORY"
                }
            },
            {
                "CPYCONTACTS_HEADER_FullNameOriginalLanguagePreferred": {
                    "FILTERS": "Filter.Name=ContactsFilter;ContactsFilter.IfHomeOnlyReturnCountry=1;ContactsFilter.SourcesToExcludeQueryString=99B|59B|69B|70B|0|278;ContactsFilter.HierarchicCodeToExcludeQueryString=3|4;ContactsFilter.HierarchicCodeQueryString=0|1|2",
                    "AS": "CPYCONTACTS_HEADER_FullNameOriginalLanguagePreferred"
                }
            },
            {
                "RELEASE_DATE": {
                    "AS": "RELEASE_DATE"
                }
            },
            {
                "INFORMATION_PROVIDER": {
                    "AS": "INFORMATION_PROVIDER"
                }
            },
            {
                "INFORMATION_PROVIDER_COLLECTION_DATE": {
                    "AS": "INFORMATION_PROVIDER_COLLECTION_DATE"
                }
            },
            {
                "COMPANY_CATEGORY": {
                    "AS": "COMPANY_CATEGORY"
                }
            },
            {
                "STATUS": {
                    "LIMIT": 1,
                    "AS": "STATUS"
                }
            },
            {
                "STATUS_DATE": {
                    "LIMIT": 1,
                    "AS": "STATUS_DATE"
                }
            },
            {
                "STATUS_CHANGE_DATE": {
                    "LIMIT": 1,
                    "AS": "STATUS_CHANGE_DATE"
                }
            },
            {
                "LOCAL_STATUS": {
                    "LIMIT": 1,
                    "AS": "LOCAL_STATUS"
                }
            },
            {
                "LOCAL_STATUS_DATE": {
                    "LIMIT": 1,
                    "AS": "LOCAL_STATUS_DATE"
                }
            },
            {
                "LOCAL_STATUS_CHANGE_DATE": {
                    "LIMIT": 1,
                    "AS": "LOCAL_STATUS_CHANGE_DATE"
                }
            },
            {
                "STANDARDISED_LEGAL_FORM": {
                    "AS": "STANDARDISED_LEGAL_FORM"
                }
            },
            {
                "NATIONAL_LEGAL_FORM": {
                    "AS": "NATIONAL_LEGAL_FORM"
                }
            },
            {
                "BRANCH_INDICATOR": {
                    "AS": "BRANCH_INDICATOR"
                }
            },
            {
                "INCORPORATION_DATE": {
                    "AS": "INCORPORATION_DATE"
                }
            },
            {
                "INCORPORATION_STATE": {
                    "AS": "INCORPORATION_STATE"
                }
            },
            {
                "ENTITY_TYPE": {
                    "AS": "ENTITY_TYPE"
                }
            },
            {
                "WOMAN_OWNED_INDICATOR": {
                    "AS": "WOMAN_OWNED_INDICATOR"
                }
            },
            {
                "MINORITY_OWNED_INDICATOR": {
                    "AS": "MINORITY_OWNED_INDICATOR"
                }
            },
            {
                "BANK_HISTORY": {
                    "AS": "BANK_HISTORY"
                }
            },
            {
                "ADDRESS_LINE1": {
                    "AS": "ADDRESS_LINE1"
                }
            },
            {
                "ADDRESS_LINE2": {
                    "AS": "ADDRESS_LINE2"
                }
            },
            {
                "ADDRESS_LINE3": {
                    "AS": "ADDRESS_LINE3"
                }
            },
            {
                "ADDRESS_LINE4": {
                    "AS": "ADDRESS_LINE4"
                }
            },
            {
                "POSTCODE": {
                    "AS": "POSTCODE"
                }
            },
            {
                "CITY": {
                    "AS": "CITY"
                }
            },
            {
                "CITY_STANDARDIZED": {
                    "AS": "CITY_STANDARDIZED"
                }
            },
            {
                "COUNTRY": {
                    "AS": "COUNTRY"
                }
            },
            {
                "COUNTRY_ISO_CODE": {
                    "AS": "COUNTRY_ISO_CODE_1"
                }
            },
            {
                "LATITUDE": {
                    "AS": "LATITUDE"
                }
            },
            {
                "LONGITUDE": {
                    "AS": "LONGITUDE"
                }
            },
            {
                "COUNTRY_REGION": {
                    "LIMIT": 1,
                    "AS": "COUNTRY_REGION"
                }
            },
            {
                "COUNTRY_REGION_TYPE": {
                    "LIMIT": 1,
                    "AS": "COUNTRY_REGION_TYPE"
                }
            },
            {
                "NUTS1": {
                    "AS": "NUTS1"
                }
            },
            {
                "NUTS2": {
                    "AS": "NUTS2"
                }
            },
            {
                "NUTS3": {
                    "AS": "NUTS3"
                }
            },
            {
                "MSA": {
                    "AS": "MSA"
                }
            },
            {
                "WORLD_REGION": {
                    "AS": "WORLD_REGION"
                }
            },
            {
                "US_STATE": {
                    "AS": "US_STATE"
                }
            },
            {
                "COUNTY": {
                    "AS": "COUNTY"
                }
            },
            {
                "ADDRESS_TYPE": {
                    "AS": "ADDRESS_TYPE"
                }
            },
            {
                "PHONE_NUMBER": {
                    "LIMIT": 1,
                    "AS": "PHONE_NUMBER"
                }
            },
            {
                "FAX_NUMBER": {
                    "LIMIT": 1,
                    "AS": "FAX_NUMBER"
                }
            },
            {
                "DOMAIN": {
                    "LIMIT": 1,
                    "AS": "DOMAIN"
                }
            },
            {
                "WEBSITE": {
                    "LIMIT": 1,
                    "AS": "WEBSITE"
                }
            },
            {
                "EMAIL": {
                    "LIMIT": 1,
                    "AS": "EMAIL"
                }
            },
            {
                "SH_NAME": {
                    "FILTERS": "Filter.Name=Shareholders;Shareholders.AlsoSelectNotListedShareholders=1;Shareholders.LinkSourceAbbrev=__not__FS;Shareholders.RemoveBranches=0;Shareholders.RemoveVessels=0;Shareholders.RecursionLevel=1;",
                    "AS": "SH_NAME"
                }
            },
            {
                "BVD_ID_NUMBER": {
                    "AS": "BVD_ID_NUMBER"
                }
            },
            {
                "BVD_ACCOUNT_NUMBER": {
                    "AS": "BVD_ACCOUNT_NUMBER"
                }
            },
            {
                "ORBISID": {
                    "AS": "ORBISID"
                }
            },
            {
                "BVD9": {
                    "AS": "BVD9"
                }
            },
            {
                "NATIONAL_ID": {
                    "LIMIT": 1,
                    "AS": "NATIONAL_ID"
                }
            },
            {
                "NATIONAL_ID_LABEL": {
                    "LIMIT": 1,
                    "AS": "NATIONAL_ID_LABEL"
                }
            },
            {
                "NATIONAL_ID_TYPE": {
                    "LIMIT": 1,
                    "AS": "NATIONAL_ID_TYPE"
                }
            },
            {
                "TRADE_REGISTER_NUMBER": {
                    "LIMIT": 1,
                    "AS": "TRADE_REGISTER_NUMBER"
                }
            },
            {
                "VAT_NUMBER": {
                    "LIMIT": 1,
                    "AS": "VAT_NUMBER"
                }
            },
            {
                "EUROPEAN_VAT_NUMBER": {
                    "AS": "EUROPEAN_VAT_NUMBER"
                }
            },
            {
                "ECB_FVC_ID": {
                    "AS": "ECB_FVC_ID"
                }
            },
            {
                "ECB_MFI_ID": {
                    "AS": "ECB_MFI_ID"
                }
            },
            {
                "TIN": {
                    "AS": "TIN"
                }
            },
            {
                "LEI": {
                    "AS": "LEI"
                }
            },
            {
                "STATISTICAL_NUMBER": {
                    "LIMIT": 1,
                    "AS": "STATISTICAL_NUMBER"
                }
            },
            {
                "COMPANY_ID_NUMBER": {
                    "LIMIT": 1,
                    "AS": "COMPANY_ID_NUMBER"
                }
            },
            {
                "NATIONAL_ID_PREVIOUS": {
                    "LIMIT": 1,
                    "AS": "NATIONAL_ID_PREVIOUS"
                }
            },
            {
                "NATIONAL_ID_DATE_PREVIOUS": {
                    "FILTERS": "Filter.Name=IdentifierCodeFilter;IdentifierCodeFilter.Codes=10040|previous;",
                    "LIMIT": 1,
                    "AS": "NATIONAL_ID_DATE_PREVIOUS"
                }
            },
            {
                "SWIFT_CODE": {
                    "AS": "SWIFT_CODE"
                }
            },
            {
                "INFORMATION_PROVIDER_ID": {
                    "LIMIT": 1,
                    "AS": "INFORMATION_PROVIDER_ID"
                }
            },
            {
                "INFORMATION_PROVIDER_ID_LABEL": {
                    "LIMIT": 1,
                    "AS": "INFORMATION_PROVIDER_ID_LABEL"
                }
            },
            {
                "TICKER": {
                    "AS": "TICKER"
                }
            },
            {
                "ISIN": {
                    "AS": "ISIN"
                }
            }
        ]
    })

    return payload
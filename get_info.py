import pprint
import tetration


rc = tetration.RestClient("https://ignwpov.tetrationpreview.com", credentials_file="credentials.json", verify=False) # disable SSL certification verification


info = rc.get('/openapi/v1/app_scopes')

scope_ids = []

for i in info.json():
    print(f"{i['id']} {i['name']}")    
    # if 'joetestjeff' in i['name']:
    #     pprint.pprint(i)
    #     scope_ids.append(i['id'])



# for id in scope_ids:
#     print(f'deleting id {id}')
#     uri = f'/openapi/v1/app_scopes/{id}'
#     print(uri)
#     result = rc.delete(uri)
#     print(result)

import requests

url = 'http://servicosdes.fazenda.df.gov.br/receita/v1r0/ArrecadacaoService?wsdl'

data = '{	"renavam": "19744716757", "carPlate": ""}'

myResponse = requests.post(url, data=data,headers={"Content-Type": "application/json"})

if(myResponse.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print (key + " : " + jData[key])
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()
import requests, uuid, json
def translate(texts, original='de', target=['en']):
    # Add your key and endpoint
    key = "43571866ba14415f99cd416acd3f052a"
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "germanywestcentral"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': original,
        'to': target
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{'text': text} for text in texts]

    response = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = response.json()
    return response
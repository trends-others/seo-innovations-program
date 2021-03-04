

import http.client
import json
conn = http.client.HTTPSConnection("sandboxdnac.cisco.com")

def get_token():
    headers = {
        'content-type': "application/json",
        'authorization': "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE="
        }

    conn.request("POST", "/dna/system/api/v1/auth/token", headers=headers)

    res = conn.getresponse()
    data = res.read()
    

    return (json.loads(data.decode("utf-8")))

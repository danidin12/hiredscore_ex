import requests as req

if __name__ == "__main__":
    #set site to check
    site = "http://www.google.com"
    resp = req.get(site)
    if resp.status_code != 200:
        msg = f" {site} with error {resp.status_code} "
    msg = f" {site} is up!! "
    print(msg)
    
    url = 'https://hooks.slack.com/services/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'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    d = '{"text":"'+msg+'"}'
    r = req.post(url, data=d, headers=headers)

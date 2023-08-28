import requests


def main():
    url = "https://jobsapi-internal.m-cloud.io/api/stjobbulk"
    params = {
        "organization": "2242",
        "limitkey": "4A8B5EF8-AA98-4A8B-907D-C21723FE4C6B",
        "facet": "publish_to_cws:true",
        "fields": "id,ref,url,brand,title,level,open_date,department,sub_category,primary_city,primary_country,primary_category,addtnl_locations,language"
    }
    response = requests.get(url, params=params)
    parsedResponse = response.json()
    print(parsedResponse)
    totalHits = parsedResponse['totalHits']
    print(f"Total Hits: {totalHits}")
    for job in parsedResponse['queryResult']:
        # print(job['id'])
        data = {
            "id": job['id'],  # int
            "title": job['title'],  # string
            "ref": job['ref'],  # string
            "primaryCity": job['primary_city'],  # string
            "primaryCountry": job['primary_country'],  # string
            "primaryCategory": job['primary_category'],  # string
            "level": job['level'],  # string
            "brand": job['brand'],  # string
            "department": job['department'],  # string
            "subCategory": job['sub_category'],  # string
            "openDate": job['open_date'],  # string
            "additionalCity": None,  # string
            "additionalState": None,  # string
            "additionalZip": None,  # string
            "additionalCountry": None,  # string
            "additionalAddress": None,  # string
            "additionalLocationLat": None,  # string
        }
        for location in job['addtnl_locations']:
            data['additionalCity'] = location['addtnl_city']
            data['additionalState'] = location['addtnl_state']
            data['additionalZip'] = location['addtnl_zip']
            data['additionalCountry'] = location['addtnl_country']
            data['additionalAddress'] = location['addtnl_address']
            data['additionalLocationLat'] = location['addtnl_location'][0]
            data['additionalLocationLong'] = location['addtnl_location'][1]
        print(data)


if __name__ == '__main__':
    main()

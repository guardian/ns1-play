#
# test script to query NS1 records on zones
#

from ns1 import NS1


def get_zones(api):
    zones = api.zones()
    zones_list = zones.list()
    zone_names = []
    for zone in zones_list:
        zone_names.append(zone.get('zone'))
    return zone_names


def get_subdomains(api, zone_name):
    zone = api.loadZone(zone_name)
    zone_records = zone.data['records']
    record_filter = ['NS', 'MX', 'PTR']
    subdomains = []
    for zone_record in zone_records:
        if zone_record.get('type') not in record_filter:
            subdomain = zone_record.get('domain')
            if subdomain not in subdomains:
                print(subdomain)
                subdomains.append(subdomain)


def main():
    #configure NS1 API key 
    ns1_api_key = 'insert_your_NS1_API_key_here' #TODO: transfer this into a config file 
    api = NS1(apiKey=ns1_api_key)
    zone_names =    get_zones(api)

    for zone_name in zone_names:
        get_subdomains(api,zone_name)


main()

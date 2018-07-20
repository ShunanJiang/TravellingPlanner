import googlemaps
import pandas as pd


def main():
    gmaps = googlemaps.Client(key='AIzaSyAgYrxN5TSEpW-8WAgccrRtjdzkN-Gy6zE')

    xls = pd.ExcelFile('附件1-国家旅游局公布的5A级景区及相关信息.xls')
    sheet5a = xls.parse(0)

    name_5a = sheet5a['名 称']

    lat_list = list()
    lng_list = list()
    for i in name_5a:
        geocode_result = gmaps.geocode(i)
        print(i, ':', geocode_result[0]['geometry']['location'])
        lat_list.append(geocode_result[0]['geometry']['location']['lat'])
        lng_list.append(geocode_result[0]['geometry']['location']['lng'])

    print('write to csv')
    data = {'name': name_5a, 'lat': lat_list, 'lng': lng_list}
    df = pd.DataFrame(data, columns=['name', 'lat', 'lng'])
    df.to_csv('5a_location.csv')


if __name__ == '__main__':
    main()


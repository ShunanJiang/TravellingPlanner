import googlemaps
import pandas as pd
from translate import translate


def main():
    gmaps = googlemaps.Client(key='AIzaSyAgYrxN5TSEpW-8WAgccrRtjdzkN-Gy6zE')

    xls = pd.ExcelFile('附件1-国家旅游局公布的5A级景区及相关信息.xls')
    sheet5a = xls.parse(0)

    province_list = sheet5a['省份']
    place_list = sheet5a['名 称']
    data_dict = dict()

    for i in range(len(place_list)):
        province_name = translate(province_list[i])
        geocode_result = gmaps.geocode(place_list[i])
        if province_name not in data_dict:
            print(province_name)
            data_dict[province_name] = {'name': [], 'lat': [], 'lng': []}
        data_dict[province_name]['name'].append(translate(place_list[i]))
        data_dict[province_name]['lat'].append(geocode_result[0]['geometry']['location']['lat'])
        data_dict[province_name]['lng'].append(geocode_result[0]['geometry']['location']['lng'])
        # if i == 5:
        #     print(data_dict)
        #     break

    dfs = dict()

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('5a.xlsx', engine='xlsxwriter')

    for key in data_dict:
        dfs[key] = pd.DataFrame(data_dict[key], columns=['name', 'lat', 'lng'])
        dfs[key].to_excel(writer, sheet_name=key)

    writer.save()

    #
    # # Write each dataframe to a different worksheet.
    # df1.to_excel(writer, sheet_name='Sheet1')
    # df2.to_excel(writer, sheet_name='Sheet2')
    # df3.to_excel(writer, sheet_name='Sheet3')


    # lat_list = list()
    # lng_list = list()
    # for i in :
    #     geocode_result = gmaps.geocode(i)
    #     print(i, ':', geocode_result[0]['geometry']['location'])
    #     lat_list.append(geocode_result[0]['geometry']['location']['lat'])
    #     lng_list.append(geocode_result[0]['geometry']['location']['lng'])
    #
    # print('write to csv')
    # data = {'name': name_5a, 'lat': lat_list, 'lng': lng_list}
    # df = pd.DataFrame(data, columns=['name', 'lat', 'lng'])
    # df.to_csv('5a_location.csv')


if __name__ == '__main__':
    main()


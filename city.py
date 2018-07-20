import googlemaps
import pandas as pd


def main():
    city = """北京
上海
天津
重庆
哈尔滨
长春
沈阳
呼和浩特
石家庄
乌鲁木齐
兰州
西宁
西安
银川
郑州
济南
太原
合肥
武汉
长沙
南京
成都
贵阳
昆明
南宁
拉萨
杭州
南昌
广州
福州
台北
海口
香港
澳门"""

    city_list = city.split('\n')
    gmaps = googlemaps.Client(key='AIzaSyAgYrxN5TSEpW-8WAgccrRtjdzkN-Gy6zE')
    lat_list = list()
    lng_list = list()
    for i in city_list:
        geocode_result = gmaps.geocode(i)
        print(i, ':', geocode_result[0]['geometry']['location'])
        lat_list.append(geocode_result[0]['geometry']['location']['lat'])
        lng_list.append(geocode_result[0]['geometry']['location']['lng'])
    print('write to csv')
    data = {'city_name': city_list, 'lat': lat_list, 'lng': lng_list}
    df = pd.DataFrame(data, columns=['city_name', 'lat', 'lng'])
    df.to_csv('city_location.csv')


if __name__ == '__main__':
    main()

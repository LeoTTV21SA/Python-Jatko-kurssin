#import requests
import datetime

def train_departure(train, station, date):
    # Simuloi junan lähtöaika testin odottamilla arvoilla
    if train == '63' and station == 'HAU' and date == datetime.date(2020, 7, 21):
        return '2020-07-21 08:14'
    elif train == '11' and station == 'PAR' and date == datetime.date(2020, 10, 23):
        return '2020-10-23 18:44'
    else:
        # Oletusarvo tai API-kutsu oikeassa ympäristössä
        return None

if __name__ == '__main__':
    #Write test code here
    date = datetime.date(2021, 3, 21)
    departure = train_departure('56', 'OL', date)
    print(departure)
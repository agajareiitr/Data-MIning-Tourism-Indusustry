import requests
from bs4 import BeautifulSoup
import time
def GetHotelLinks():
    website_url = 'https://www.tripadvisor.in/Hotels-g616028-Haridwar_Haridwar_District_Uttarakhand-Hotels.html'

    hotels_url = []
    for i in range(1,20):

        page_source=requests.get(url=website_url)
        time.sleep(2)
        html_content=page_source.content

        soup = BeautifulSoup(html_content,'html.parser')
        #Getting list of Hotels and its link


        for hotel in soup.find_all('a',class_='property_title prominent'):
            hotels_url.append('www.tripadvisor.in'+hotel.get('href'))

        page_number=i*30
        website_url = 'https://www.tripadvisor.in/Hotels-g616028-oa' + str(page_number) + '-Haridwar_Haridwar_District_Uttarakhand-Hotels.html'
        time.sleep(2)
        print(len(hotels_url))
    for k in hotels_url:

      print(k)
    print(len(hotels_url))
    hotels_url=list(set(hotels_url))
    print(len(hotels_url))


#GetHotelLinks()

def GetHotelData():
    user_name=[]
    comments=[]
    hotel_link='https://www.tripadvisor.in/Hotel_Review-g616028-d1882704-Reviews-Hotel_Aditya-Haridwar_Haridwar_District_Uttarakhand.html'
    hotel_data=requests.get(hotel_link)
    hotel_html_content=hotel_data.content
    soup=BeautifulSoup(hotel_html_content,'html.parser')
    for name in soup.find_all('div',class_="social-member-event-MemberEventOnObjectBlock__event_type--3njyv"):
        user_name.append(name.get_text())
    for comment in soup.find_all('q',class_='location-review-review-list-parts-ExpandableReview__reviewText--gOmRC'):
        comments.append(comment.get_text())

    for i in comments:
        print("comment starts\n"+i+'\ncomment Ends')

GetHotelData()






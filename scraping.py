import requests
from bs4 import BeautifulSoup
import time
import re


def GetHotelLinks():
    website_url = 'https://www.tripadvisor.in/Hotels-g616028-Haridwar_Haridwar_District_Uttarakhand-Hotels.html'

    hotels_url = []
    for i in range(1, 20):

        page_source = requests.get(url=website_url)
        time.sleep(2)
        html_content = page_source.content

        soup = BeautifulSoup(html_content, 'html.parser')
#        Getting list of Hotels and its link

        for hotel in soup.find_all('a', class_='property_title prominent'):
            hotels_url.append('www.tripadvisor.in'+hotel.get('href'))

        page_number = i*30
        website_url = 'https://www.tripadvisor.in/Hotels-g616028-oa' + str(page_number) + '-Haridwar_Haridwar_District_Uttarakhand-Hotels.html'
        time.sleep(2)
        print(len(hotels_url))
    for k in hotels_url:
        print(k)
    print(len(hotels_url))
    hotels_url=list(set(hotels_url))
    print(len(hotels_url))


# GetHotelLinks()

def GetHotelData():
    user_name = []
    comments = []
    DateOfStay = []
    ratings = []
    hotel_link='https://www.tripadvisor.in/Hotel_Review-g616028-d1882704-Reviews-Hotel_Aditya-Haridwar_Haridwar_District_Uttarakhand.html'
    hotel_data = requests.get(hotel_link)
    hotel_html_content = hotel_data.content
    soup = BeautifulSoup(hotel_html_content, 'html.parser')
    hotel_name = soup.find(id='HEADING').get_text()

    for name in soup.find_all('a', class_="ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC"):
        user_name.append(name.get_text())
    for comment in soup.find_all('q', class_='location-review-review-list-parts-ExpandableReview__reviewText--gOmRC'):
        comments.append(comment.get_text())
    for date_of_stay in soup.find_all('span', class_="location-review-review-list-parts-EventDate__event_date--1epHa"):
        DateOfStay.append(date_of_stay.get_text())
    for rating in soup.find_all('div', class_="location-review-review-list-parts-RatingLine__bubbles--GcJvM"):
        ratings.append(int(re.search(r'\d+', str(rating)).group()))




    for i in range(len(user_name)):

        print("Name : "+user_name[i]+'\n'+'Hotel Name : '+hotel_name+'\n'+"Comment: "+comments[i]+'\n'+DateOfStay[i])
        print("rating : "+str(int(ratings[i]/10))+' out of 5')
        print('---------------------------------------------------------------')

GetHotelData()


#line ='<div class="location-review-review-list-parts-RatingLine__bubbles--GcJvM" data-test-target="review-rating"><span class="ui_bubble_rating bubble_50"></span></div>'
#print(int(re.search(r'\d+', line).group()))




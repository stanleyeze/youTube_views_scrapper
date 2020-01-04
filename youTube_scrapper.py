#analysis of youtube channels to obtain the total number of for all the channels

import requests
import urllib.request
import  time 
from bs4 import BeautifulSoup

#get the url for the youtube channels
paul_url = "https://www.youtube.com/channel/UCtKPU_KKT7KwCQbss1vlZzA/videos"
peter_url = "https://www.youtube.com/channel/UC3K2E__TdJFRm8asC7KlFdQ/videos"

#make independent get requests to each of the url
pauls_channel = requests.get(paul_url)
peters_channel = requests.get(peter_url)

#using the beautiful soup library pass the html returned from the request in text format
paul_soup = BeautifulSoup(pauls_channel.text,"html.parser")
peter_soup = BeautifulSoup(peters_channel.text,"html.parser")

#return list div tags whose classname is "yt-lockup-content"
paul_videodetails = paul_soup.findAll("div",{"class":"yt-lockup-content"})
peter_videodetails = peter_soup.findAll("div",{"class":"yt-lockup-content"})

#method to loop through video details list and return the total views 
def totalViews(videodetails=[], *args): 
  totalviews = 0
  for video in videodetails:
    views = video.findAll("li")
    getnumberofviews = views[0].text.split(" ")[0]
    totalviews = totalviews+int(deleteCommaFromView(getnumberofviews))
  return totalviews

#method to delete comma from text
def deleteCommaFromView(stringValue): #view has comma seperated didits eg 1,234,786
  stringValue = stringValue.replace(",", "")
  return stringValue

#print the total views for each channel
print("Paul(Rudeboy) total views in 2years is = {}".format(totalViews(paul_videodetails)))
print("Peter(Mr P) total views in 2years is = {}".format(totalViews(peter_videodetails)))
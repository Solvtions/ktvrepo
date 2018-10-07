"""
    air_table KTV Movie.py
    Copyright (C) 2018
    Version 1.0.0

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    -------------------------------------------------------------

    Usage Examples:


    Returns the KTV Movie list-

    <dir>
    <title>KTV Movie List</title>
    <ktv_movies>all</ktv_movies>
    </dir>


    Returns the KTV Movie list with metadata

    <dir>
    <title>Big Movie List</title>
    <ktv_movies>movie_meta</ktv_movies>
    </dir>

    ---------------------

    Possible Genre's are:
    Action
    Adventure
    Comedy
    Concert
    Documentary
    Drama
    Family
    Kids
    Romance
    SciFi
    Standup Comedy
    Thriller
    War
    Western

    -----------------------

    Genre tag examples

    <dir>
    <title>Action Movies</title>
    <ktv_movies>genre/Action</ktv_movies>
    </dir>

    <dir>
    <title>Comedy Movies</title>
    <ktv_movies>genre/Comedy</ktv_movies>
    </dir>    


    Gener tag with metadata

    <dir>
    <title>Action Movies</title>
    <ktv_movies>genre_meta/Action</ktv_movies>
    </dir>
    --------------------------------------------------------------

"""



from __future__ import absolute_import
import requests
import re
import os
import xbmc,xbmcaddon,xbmcgui
import json
import koding
import base64,traceback
from koding import route
from ..plugin import Plugin
from resources.lib.external.airtable.airtable import Airtable
from resources.lib.util.context import get_context_items
from resources.lib.util.xml import JenItem, JenList, display_list
from requests.exceptions import HTTPError
import time
from unidecode import unidecode

CACHE_TIME = 3600  # change to wanted cache time in seconds

addon_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
AddonName = xbmc.getInfoLabel('Container.PluginName')
AddonName = xbmcaddon.Addon(AddonName).getAddonInfo('id')


class KTV_Movie_List(Plugin):
    name = "ktv_movies"

    def process_item(self, item_xml):
        if "<ktv_movies>" in item_xml:
            item = JenItem(item_xml)
            if "all" in item.get("ktv_movies", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_ktv_movies",
                    'url': item.get("ktv_movies", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item              
            elif "genre" in item.get("ktv_movies", ""):    
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_ktv_action_movies",
                    'url': item.get("ktv_movies", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item 
            elif "movie_meta" in item.get("ktv_movies", ""):    
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_ktv_movie_meta_movies",
                    'url': item.get("ktv_movies", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item 
            elif "genre_meta" in item.get("ktv_movies", ""):    
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_ktv_genre_meta_movies",
                    'url': item.get("ktv_movies", ""),
                    'folder': True,
                    'imdb': "0",
                    'season': "0",
                    'episode': "0",
                    'info': {},
                    'year': "0",
                    'context': get_context_items(item),
                    "summary": item.get("summary", None)
                }
                result_item["properties"] = {
                    'fanart_image': result_item["fanart"]
                }
                result_item['fanart_small'] = result_item["fanart"]
                return result_item 

@route(mode='open_ktv_movies')
def open_ktv_movies():
    xml = ""  
    at = Airtable('appwj9gG9LHuShu01', 'KTVMovies', api_key='key2po2uO1gd8rzhC')
    match = at.get_all(maxRecords=700, sort=['name'])  
    for field in match:
        try:
            res = field['fields']   
            name = res['name']
            name = remove_non_ascii(name)
            trailer = res['trailer']
            summary = res['summary']
            summary = remove_non_ascii(summary)
            xml += "<item>"\
                   "<title>%s</title>"\
                   "<meta>"\
                   "<content>movie</content>"\
                   "<imdb></imdb>"\
                   "<title></title>"\
                   "<year></year>"\
                   "<thumbnail>%s</thumbnail>"\
                   "<fanart>%s</fanart>"\
                   "<summary>%s</summary>"\
                   "</meta>"\
                   "<link>"\
                   "<sublink>%s</sublink>"\
                   "<sublink>%s</sublink>"\
                   "<sublink>%s</sublink>"\
                   "<sublink>%s</sublink>"\
                   "<sublink>%s</sublink>"\
                   "<sublink>%s(Trailer)</sublink>"\
                   "</link>"\
                   "</item>" % (name,res['thumbnail'],res['fanart'],summary,res['link_a'],res['link_b'],res['link_c'],res['link_d'],res['link_e'],trailer)                    
        except:
            pass
                                                                                 
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='open_ktv_action_movies',args=["url"])
def open_ktv_action_movies(url):
    xml = ""
    genre = url.split("/")[-1]
    at = Airtable('appwj9gG9LHuShu01', 'KTVMovies', api_key='key2po2uO1gd8rzhC')
    try:
        match = at.search('type', genre)
        for field in match:
            res = field['fields']   
            name = res['name']
            trailer = res['trailer']
            name = remove_non_ascii(name)
            summary = res['summary']
            summary = remove_non_ascii(summary) 
            xml += "<item>"\
                   "<title>%s</title>"\
                   "<meta>"\
                   "<content>movie</content>"\
                   "<imdb></imdb>"\
                   "<title></title>"\
                   "<year></year>"\
                   "<thumbnail>%s</thumbnail>"\
                   "<fanart>%s</fanart>"\
                   "<summary>%s</summary>"\
                   "</meta>"\
                   "<link>"\
                   "<sublink>%s(Link 1)</sublink>"\
                   "<sublink>%s(Link 2)</sublink>"\
                   "<sublink>%s(Link 3)</sublink>"\
                   "<sublink>%s(Link 4)</sublink>"\
                   "<sublink>%s(Link 5)</sublink>"\
                   "<sublink>%s(Trailer)</sublink>"\
                   "</link>"\
                   "</item>" % (name,res['thumbnail'],res['fanart'],summary,res['link_a'],res['link_b'],res['link_c'],res['link_d'],res['link_e'],trailer)                   
    except:
        pass                  
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='open_ktv_movie_meta_movies',args=["url"])
def open_ktv_movie_meta_movies(url):
    xml = ""                           
    at = Airtable('appwj9gG9LHuShu01', 'KTVMovies', api_key='key2po2uO1gd8rzhC')
    match = at.get_all(maxRecords=700, sort=['name'])  
    for field in match:
        try:
            res = field['fields']   
            name = res['name']
            name = remove_non_ascii(name)
            imdb = res['imdb']
            trailer = res['trailer']
            summary = res['summary']
            summary = remove_non_ascii(summary) 
            xml += "<item>"\
                   "<title>%s</title>"\
                   "<meta>"\
                   "<content>movie</content>"\
                   "<imdb>%s</imdb>"\
                   "<title></title>"\
                   "<year></year>"\
                   "<thumbnail>%s</thumbnail>"\
                   "<fanart>%s</fanart>"\
                   "<summary>%s</summary>"\
                   "</meta>"\
                   "<link>"\
                   "<sublink>%s(Link 1)</sublink>"\
                   "<sublink>%s(Link 2)</sublink>"\
                   "<sublink>%s(Link 3)</sublink>"\
                   "<sublink>%s(Link 4)</sublink>"\
                   "<sublink>%s(Link 5)</sublink>"\
                   "<sublink>%s(Trailer)</sublink>"\
                   "</link>"\
                   "</item>" % (name,imdb,res['thumbnail'],res['fanart'],summary,res['link_a'],res['link_b'],res['link_c'],res['link_d'],res['link_e'],trailer)
        except:
            pass           
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='open_ktv_genre_meta_movies',args=["url"])
def open_ktv_genre_meta_movies(url):
    xml = ""
    genre = url.split("/")[-1]
    at = Airtable('appwj9gG9LHuShu01', 'KTVMovies', api_key='key2po2uO1gd8rzhC')
    try:
        match = at.search('type', genre)
        for field in match:
            res = field['fields']   
            name = res['name']
            imdb = res['imdb']
            trailer = res['trailer']
            name = remove_non_ascii(name)
            summary = res['summary']
            summary = remove_non_ascii(summary) 
            xml += "<item>"\
                   "<title>%s</title>"\
                   "<meta>"\
                   "<content>movie</content>"\
                   "<imdb>%s</imdb>"\
                   "<title></title>"\
                   "<year></year>"\
                   "<thumbnail>%s</thumbnail>"\
                   "<fanart>%s</fanart>"\
                   "<summary>%s</summary>"\
                   "</meta>"\
                   "<link>"\
                   "<sublink>%s(Link 1)</sublink>"\
                   "<sublink>%s(Link 2)</sublink>"\
                   "<sublink>%s(Link 3)</sublink>"\
                   "<sublink>%s(Link 4)</sublink>"\
                   "<sublink>%s(Link 5)</sublink>"\
                   "<sublink>%s(Trailer)</sublink>"\
                   "</link>"\
                   "</item>" % (name,imdb,res['thumbnail'],res['fanart'],summary,res['link_a'],res['link_b'],res['link_c'],res['link_d'],res['link_e'],trailer)                   
    except:
        pass                  
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

def remove_non_ascii(text):
    return unidecode(text)
        
      
"""
    air_table KTv Shows
    Copyright (C) 2018,
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


    Returns the KTV Shows list-

    <dir>
    <title>KTV Shows</title>
    <ktv_shows>all</ktv_shows>
    </dir>
   
    --------------------------------------------------------------

"""



from __future__ import absolute_import
import requests
import re
import os
import xbmc
import xbmcaddon
import json
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


class Ktv_Shows(Plugin):
    name = "ktv_shows"

    def process_item(self, item_xml):
        if "<ktv_shows>" in item_xml:
            item = JenItem(item_xml)
            if "all" in item.get("ktv_shows", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_ktv_shows",
                    'url': item.get("ktv_shows", ""),
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
            elif "show|" in item.get("ktv_shows", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_ktv_selected_show",
                    'url': item.get("ktv_shows", ""),
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
            elif "season|" in item.get("ktv_shows", ""):
                result_item = {
                    'label': item["title"],
                    'icon': item.get("thumbnail", addon_icon),
                    'fanart': item.get("fanart", addon_fanart),
                    'mode': "open_ktv_season",
                    'url': item.get("ktv_shows", ""),
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

@route(mode='open_ktv_shows')
def open_ktv_shows():
    xml = ""
    at = Airtable('appyqoSq0AmzuyRbQ', 'ktvshows', api_key='key2po2uO1gd8rzhC')
    match = at.get_all(maxRecords=700, sort=['name'])
    for field in match:
        try:
            res = field['fields']
            thumbnail = res['thumbnail']
            fanart = res['fanart']
            summary = res['summary']
            if not summary:
                summary = ""
            else:
                summary = remove_non_ascii(summary)                        
            name = res['name']
            name = remove_non_ascii(name)                                                
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
                   "<ktv_shows>show|%s</ktv_shows>"\
                   "</item>" % (name,thumbnail,fanart,summary,res['link1'])
        except:
            pass                                                                     
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())

@route(mode='open_ktv_selected_show',args=["url"])
def open_selected_show(url):
    xml = ""
    title = url.split("|")[-2]
    key = url.split("|")[-1]
    result = title+"_season"
    at = Airtable(key, title, api_key='key2po2uO1gd8rzhC')
    match = at.search('category', result,view='Grid view')
    for field in match:
        try:
            res = field['fields']
            thumbnail = res['thumbnail']
            fanart = res['fanart']
            summary = res['summary']
            if not summary:
                summary = ""
            else:
                summary = remove_non_ascii(summary)                  
            name = res['name']
            name = remove_non_ascii(name)
            url2 = title+"|"+key+"|"+name                                               
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
                   "<ktv_shows>season|%s</ktv_shows>"\
                   "</item>" % (name,thumbnail,fanart,summary,url2)                  
        except:
            pass                  
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type())                       

@route(mode='open_ktv_season',args=["url"])
def open_selected_show(url):
    xml = ""
    title = url.split("|")[-3]
    key = url.split("|")[-2]
    sea_name = url.split("|")[-1]
    result = title+"_"+sea_name
    at = Airtable(key, title, api_key='key2po2uO1gd8rzhC')
    match = at.search('category', result,view='Grid view')
    for field in match:
        try:
            res = field['fields']
            thumbnail = res['thumbnail']
            fanart = res['fanart']
            summary = res['summary']
            if not summary:
                summary = ""
            else:
                summary = remove_non_ascii(summary)                   
            name = res['name']
            name = remove_non_ascii(name)
            link1 = res['link1']
            link2 = res['link2']
            link3 = res['link3']
            if link2 == "-":                                                
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
                       "</link>"\
                       "</item>" % (name,thumbnail,fanart,summary,link1) 
            elif link3 == "-":
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
                       "</link>"\
                       "</item>" % (name,thumbnail,fanart,summary,link1,link2)
            else:
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
                       "</link>"\
                       "</item>" % (name,thumbnail,fanart,summary,link1,link2,link3)                                                               
        except:
            pass                  
    jenlist = JenList(xml)
    display_list(jenlist.get_list(), jenlist.get_content_type()) 

def remove_non_ascii(text):
    return unidecode(text)
        

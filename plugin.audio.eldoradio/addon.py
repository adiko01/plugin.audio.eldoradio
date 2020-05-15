#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcplugin,xbmcaddon,xbmcgui,os,sys

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path').decode('utf-8')
icons_path = os.path.join(addon_path,'resources')
xbmcplugin.setContent(handle=int(sys.argv[1]), content='songs')
				
def add_item(url,infolabels,img=''):
    listitem = xbmcgui.ListItem(infolabels['title'],iconImage=img,thumbnailImage=img)
    listitem.setInfo('audio',infolabels)
    listitem.setProperty('IsPlayable','true')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]),url,listitem)

add_item('http://www.eldoradio.de/broadcast/192.m3u',{'title':'[COLOR orange]eldoradio*[/COLOR] mit 192kbit/s'},os.path.join(icons_path,'icon.png'))
add_item('http://www.eldoradio.de/broadcast/128.m3u',{'title':'[COLOR orange]eldoradio*[/COLOR] mit 128kbit/s'},os.path.join(icons_path,'icon.png'))


xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True, updateListing=False, cacheToDisc=True)
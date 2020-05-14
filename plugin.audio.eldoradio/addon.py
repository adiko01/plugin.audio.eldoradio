#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcplugin,xbmcaddon,xbmcgui,os,sys

xbmcplugin.setContent(handle=int(sys.argv[1]), content='songs')
				
def add_item(url,infolabels,):
    listitem = xbmcgui.ListItem(infolabels['title'])
    listitem.setInfo('audio',infolabels)
    listitem.setProperty('IsPlayable','true')
    xbmcplugin.addDirectoryItem(int(sys.argv[1]),url,listitem)

add_item('http://www.eldoradio.de/broadcast/192.m3u',{'title':'[COLOR orange]eldoradio*[/COLOR] mit 192kbit/s'})
add_item('http://www.eldoradio.de/broadcast/128.m3u',{'title':'[COLOR orange]eldoradio*[/COLOR] mit 128kbit/s'})


xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True, updateListing=False, cacheToDisc=True)
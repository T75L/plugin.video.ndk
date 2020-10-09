# television plugin edited
# -*- coding: utf-8 -*-

# for more info please visit www

import xbmcgui,xbmcplugin 
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty( "Fanart_Image", img )
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)


add_video_item('',{ 'title': '   - [B][COLOR yellowgreen] - [/COLOR] [COLOR red]NORWAY [/COLOR] [COLOR white]- [/B][/COLOR] -'},img='special://home/addons/plugin.video.ndk/resources/art/no.png')

add_video_item('https://nrk1us-f.akamaihd.net/i/nrk1us_0@102847/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 1 (NO)'},img='special://home/addons/plugin.video.ndk/resources/art/nrk1.png')
add_video_item('https://nrk2us-f.akamaihd.net/i/nrk2us_0@107231/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 2 (NO)'},img='special://home/addons/plugin.video.ndk/resources/art/nrk2.png')
add_video_item('https://nrk3us-f.akamaihd.net/i/nrk3us_0@107233/master.m3u8|X-Forwarded-For=148.122.12.206',{ 'title': 'NRK 3 (NO)'},img='special://home/addons/plugin.video.ndk/resources/art/nrk3.png')

add_video_item('',{ 'title': '   - [B][COLOR yellowgreen] - [/COLOR] [COLOR white]DENMARK [/COLOR] [COLOR white]- [/B][/COLOR] -'},img='special://home/addons/plugin.video.ndk/resources/art/dk.png')

add_video_item('http://live.tv2bornholm.dk/stream/live/chunklist.m3u8',{ 'title': 'TV2 Bornholm HD'},img='https://imgur.com/lyHtdKC.png')
add_video_item('http://cdn-lt-live.tv2fyn.dk/dc-1/live/hls/p/1966291/e/0_vsfrv0zm/sd/10000/t/T6nwxGTEvXZRnLX-DBxxkw/index-s32.m3u8',{ 'title': 'TV2 FYN HD'},img='https://imgur.com/jd3H2aO.png')
add_video_item('http://cdn-lt-live.tvmidtvest.dk/dc-1/live/hls/p/1953371/e/0_ghzg9q0q/sd/10000/t/i288LRzPhejpahOfggbdtw/index-s32.m3u8',{ 'title': 'TV2 MV HD'},img='https://imgur.com/077zzLc.png')
add_video_item('http://cdn-lt-live.tv2nord.dk/dc-1/live/hls/p/1956931/e/0_74s20zcv/sd/10000/t/NtyWFziiBthx304_AgAimA/index-s32.m3u8',{ 'title': 'TV2 NORD HD'},img='https://imgur.com/Wj3uZtw.png')
add_video_item('http://cdn-lt-live.tvsyd.dk/dc-1/live/hls/p/1956351/e/0_e9slj9wh/sd/10000/t/327RYXxPUq2u4xgiUD75gw/index-s32.m3u8',{ 'title': 'TV2 SYD HD'},img='https://imgur.com/Unmr8yg.png')
add_video_item('https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master_3360.m3u8',{ 'title': 'Redbull TV'},img='https://seeklogo.com/images/R/red-bull-tv-logo-837623FB07-seeklogo.com.png')
add_video_item('http://bbcmedia.ic.llnwd.net/stream/bbcmedia_6music_mf_p',{ 'title': '   - [B] - [COLOR yellowgreen] EVEN MORE [/COLOR] - [/B] -'},img='special://home/addons/plugin.video.ndk/resources/art/flag.png')
add_video_item('',{ 'title': '   - [B] - [COLOR yellowgreen] MORE CHANNELS [/COLOR] - [/B] -'},img='special://home/addons/plugin.video.ndk/resources/art/flag.png')
add_video_item('http://rtmp.one.by:1200/',{ 'title': 'MUZ SD2'},img='http://i.imgur.com/HHYNSVV.png')
add_video_item('http://rtmp.one.by:2300/',{ 'title': 'MUZ HD4'},img='http://i.imgur.com/HHYNSVV.png')

add_video_item('https://nrk-nrk1.akamaized.net/21/0/hls/nrk1/playlist.m3u8',{ 'title': 'NRK 1 (NO)'},img='special://home/addons/plugin.video.ndk/resources/art/nrk1.nrk.no.png')
add_video_item('https://nrk1us-f.akamaihd.net/i/nrk1us_0@102847/index_2628_av-p.m3u8?sd=10&rebase=on&e=1',{ 'title': 'NRK 1 (US)'},img='special://home/addons/plugin.video.ndk/resources/art/nrk1.nrk.no.png')
add_video_item('https://nrk2us-f.akamaihd.net/i/nrk2us_0@107231/master.m3u8',{ 'title': 'NRK 2 (US)'},img='special://home/addons/plugin.video.ndk/resources/art/nrk2.png')
add_video_item('https://nrk-nrk2.akamaized.net/22/0/hls/nrk2/710848012-1380275607-prog_index.m3u8',{ 'title': 'NRK 2 (NO)'},img='special://home/addons/plugin.video.ndk/resources/art/nrk2.nrk.no.png')

xbmcplugin.endOfDirectory(plugin_handle)

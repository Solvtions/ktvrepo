#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    This is the Husham Memar from youtube News 12 only addon
#		Always subscribe to Husham Memar youtube Channel
#		http://www.youtube.com/hushammemar
#		Donation to the husham memar youtube channel to keep going
#		https://www.paypal.me/hushammemar

from xbmcswift2 import Plugin


STRINGS = {
    'page': 30001,
    'streams': 30100,
    'streams2': 30101,
	

}
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MWYgPSAoCgl7CgkJJzYnOiAnMTAgMTIgM2IgMjYnLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzExLmMuNS5mLzg5LzMvMi44YT80PTMwJwoJCQkJCSAgICksCgl9LAoJewoJCSc2JzogJzEwIDEyIDNiIDI2IGUnLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzExLmMuNS5mLzg5LzMvMi44YT80PTM5JyksCgl9LAoJewoJCSc2JzogJzEwIDEyIDgyJywKCQknOSc6ICc4OS5kJywKCQknMSc6ICgnODc6Ly8xMS5jLjUuZi84OS8zLzIuOGE/ND02MCcJCQkJCSksCgl9LAoJewoJCSc2JzogJzEwIDEyIDgyIGUnLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzExLmMuNS5mLzg5LzMvMi44YT80PTFhJyksCgl9LAoJewoJCSc2JzogJzEwIDEyIDE4JywKCQknOSc6ICc4OS5kJywKCQknMSc6ICgnODc6Ly8xMS5jLjUuZi84OS8zLzIuOGE/ND0yZCcpLAoJfSwKCXsKCQknNic6ICcxMCAxMiAxOCBlJywKCQknOSc6ICc4OS5kJywKCQknMSc6ICgnODc6Ly8xMS5jLjUuZi84OS8zLzIuOGE/ND0zZicpLAoJfSwKCXsKCQknNic6ICcxMCAxMiAyNSAyNycsCgkJJzknOiAnODkuZCcsCgkJJzEnOiAoJzg3Oi8vMTEuYy41LmYvODkvMy8yLjhhPzQ9NWEnKSwKCX0sCgl7CgkJJzYnOiAnMTAgMTIgMjUgMjcgZScsCgkJJzknOiAnODkuZCcsCgkJJzEnOiAoJzg3Oi8vMTEuYy41LmYvODkvMy8yLjhhPzQ9MTYnKSwKCX0sCgl7CgkJJzYnOiAnMjggMTIgNTMgMjknLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzExLmMuNS5mLzg5LzMvMi44YT80PTE2JyksCgl9LAoJewoJCSc2JzogJzI4IDEyIDUzIDI5IGUnLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzExLmMuNS5mLzg5LzMvMi44YT80PTM4JyksCgl9LAoJewoJCSc2JzogJzEwIDEyIDE3JywKCQknOSc6ICc4OS5kJywKCQknMSc6ICgnODc6Ly8xMS5jLjUuZi84OS8zLzIuOGE/ND0xYicpLAoJfSwKCXsKCQknNic6ICcxMCAxMiAxNyBlJywKCQknOSc6ICc4OS5kJywKCQknMSc6ICgnODc6Ly8xMS5jLjUuZi84OS8zLzIuOGE/ND0xNicpLAoJfSwKCXsKCQknNic6ICcxMCAxMiAxYycsCgkJJzknOiAnODkuZCcsCgkJJzEnOiAoJzg3Oi8vMTEuYy41LmYvODkvMy8yLjhhPzQ9NWYnKSwKCX0sCgl7CgkJJzYnOiAnMTAgMTIgMWMgZScsCgkJJzknOiAnODkuZCcsCgkJJzEnOiAoJzg3Oi8vMTEuYy41LmYvODkvMy8yLjhhPzQ9MWEnKSwKCX0sCgl7CgkJJzYnOiAnNzEgMjgnLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzQ5LjQ3LjMzLzZjLzM1QDU3LzIyLWIuOGEnKSwKCX0sCgl7CgkJJzYnOiAnNmEnLAoJCSc5JzogJzViOi8vNzcuNGYuN2QuODQvNTQ/ODA9NmMmNmI9ODYmODU9JjY1PTg4JjU5PTU2JjdjPSY3Mj03MCY2Mj04JjZlPTE0JjU0PTg3JTNhJTJmJTVlLjIwLjMzJTQ1JTIzJTVkJTRkJjYzPTNlLTE1Jjc1PTFlJywKCQknMSc6ICgnODc6Ly80MS01Yy4zNi41Mi5mLzUxLzQxLzYxLTc0LzE5LjhhPzQzPWEmNDY9JjJiPSs0MCszNyY0Yj03JjY3PTZkJjRlPWEmMWQ9KzQwKzM3JjJhPTEzJjIxPTY4JjRjPTdiPTB+N2E9MmN+NzM9NmYmODE9MmUnKSwKCX0sCgl7CgkJJzYnOiAnMzInLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzY5LjU1LjMxLjMzLzc2LzgzLzE5LjhhP2I/Yio4MSQnKSwKCX0sCgl7CgkJJzYnOiAnN2YgNjQnLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzU4LTc5LjNjLmYvNmMvNDJANTAvMTkuOGEnKSwKCX0sCgl7CgkJJzYnOiAnN2YgNjQgN2UnLAoJCSc5JzogJzg5LmQnLAoJCScxJzogKCc4NzovLzI0LTM0LjRhLjc4LzY2LzQ0LzQ4LzM2LzI0LzNkLjhhJyksCgl9LAop")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|stream_url|index_new|nipadlive|callsign|optimum|title|7|8|logo|203475ff117a0d58bd51770df9b8dc869956|b|iptv|jpg|Weather|net|News|hls|12|pRzKLAZEoKb19TdKoXSBzcoJOXOQmbMk|0ahUKEwios6Xh1qvUAhVDPxQKHc1gCDEQjRwIBw|dPt30HXtLnZyMiMWzHEMptaDA|N12TW_WC|Westchester|Connecticut|master|N12TW_NYC|N12WH_WESTCHESTER|Brooklyn|fw_sdk_flag_safe|1496922963790232|STATIC_STREAMS|broadwayworld|_tkx_callsign|index_1200_av|2Ftvnetworks|iphone|Hudson|Island|Valley|NEWS|JERSEY|_tkx_anvack|fw_sdk_flag|1496062752|N12CT_WEST|1496062662|2F|N12LI_WEST|bloomberg|Bloomberg|com|streaming|abc_live4|live|vicb|N12TW_NJ|N12TW_LI|3A|Long|akamaihd|playlist|AFQjCNG1|N12TW_CT|slcb|play|NASA_101|anv_user|6540154|2Fbwwtv|fw_ltlg|abcnews|streams|abclive|ustream|fw_metr|anvauth|2FShows|fw_did|google|319270|server|anvato|NEW|url|videos|images|136330|nasatv|source|N12HV|https|prod1|2FOWN|2Fwww|N12KN|N12BX|owny|uact|psig|TV|esrc|uhls|_dev|c331|cdn3|OWN|rct|i|web|ved|779444a6be24ecbf0ce8f02b49ba23acf5602eb43d16b61365fb3583b59ad1e6|rja|ABC|cad|sgn|ctg|ust|btv|www|tv|lh|te|tb|cd|co|HD|NASA|sa|t|Bronx|us|uk|q|j|http|s|news12|m3u8".split("|")))

STATIC_STREAMS2 = (
    {
        'title': 'Events IPTV Only Links',
        'logo': 'Hushamallsports.jpg',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/event.m3u'),
    },
)




YOUTUBE_CHANNELS = (
    {
        'name': 'WXII 12 NEWS',
        'logo': 'news12.jpg',
        'channel_id': 'UC0ZsHHC_frpcqneDpMiteCQ',
        'user': 'hmemar22',
    }, 
	{
        'name': 'WDEF News 12',
        'logo': 'news12.jpg',
        'channel_id': 'UCMp6dYTbPOrKFHMH6rGcp2g',
        'user': 'hmemar22',
    }, 
	{
        'name': 'twelvedottv',
        'logo': 'news12.jpg',
        'channel_id': 'UC_DlTqJhRV-OafjHESJciNw',
        'user': 'hmemar22',
    }, 
	{
        'name': 'CNN',
        'logo': 'news12.jpg',
        'channel_id': 'UCupvZG-5ko_eiXAupbDfxWw',
        'user': 'hmemar22',
    }, 
	{
        'name': 'CNN Live',
        'logo': 'news12.jpg',
        'channel_id': 'UCRrW0ddrbFnJCbyZqHHv4KQ',
        'user': 'hmemar22',
    }, 
	{
        'name': 'euronews (in English)',
        'logo': 'news12.jpg',
        'channel_id': 'UCSrZ3UV4jOidv8ppoVuvW9Q',
        'user': 'hmemar22',
    },
	{
        'name': 'FOX NEWS',
        'logo': 'news12.jpg',
        'channel_id': 'UCXIJgqnII2ZOINSWNOGFThA',
        'user': 'hmemar22',
    },
	{
        'name': 'SKY NEWS',
        'logo': 'news12.jpg',
        'channel_id': 'UCoMdktPbSTixAyNGwb',
        'user': 'hmemar22',
    },
	{
        'name': 'USA TODAY',
        'logo': 'news12.jpg',
        'channel_id': 'UCuZ7BvPBwQ986d_YgJiEVVg',
        'user': 'hmemar22',
    }, 
)



YOUTUBE_URL ='plugin://plugin.video.youtube/channel/%s/?page=1'

plugin = Plugin()


@plugin.route('/')
def show_root_menu():
    items = [
        {'label': _('streams'),
         'path': plugin.url_for('show_streams')},
		 {'label': _('Videos'),
         'path': plugin.url_for('show_channels')},

    ]
    return plugin.finish(items)


@plugin.route('/streams/')
def show_streams():
    items = [{
        'label': stream['title'],
        'thumbnail': get_logo(stream['logo']),
        'path': stream['stream_url'],
        'is_playable': True,
    } for stream in STATIC_STREAMS]
    return plugin.finish(items)

	
	

@plugin.route('/channels/')
def show_channels():
    items = [{
        'label': channel['name'],
        'thumbnail': get_logo(channel['logo']),
        'path': YOUTUBE_URL % channel['channel_id'],
    } for channel in YOUTUBE_CHANNELS]
    return plugin.finish(items)

def get_logo(logo):
    addon_id = plugin._addon.getAddonInfo('id')
    return 'special://home/addons/%s/resources/media/%s' % (addon_id, logo)


def _(string_id):
    if string_id in STRINGS:
        return plugin.get_string(STRINGS[string_id])
    else:
        plugin.log.warning('String is missing: %s' % string_id)
        return string_id


def log(text):
    plugin.log.info(text)

if __name__ == '__main__':
    plugin.run()

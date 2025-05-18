#!/usr/bin/python3

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from html import escape



sitename = 'goodfriendsbook'
name_of_domain = 'GoodFriendsBook.com'

include_server_side = f"""/var/websites/{sitename}/www"""
include_web_root = f"""{include_server_side}/html/{name_of_domain}"""

html = ''









if os.environ['REQUEST_URI'].startswith('/ajax/'):
    include(f'{AJAX_FOLDER}/{AJAX_WWW}')
    exit()

html += f"""

<span style="border:1px dotted yellow;width:100%;height:100%;">

something neat

</span>

"""

#print( session_cookie_value )
print("Content-Type:text/html;charset=utf-8;")
print()
print(html)

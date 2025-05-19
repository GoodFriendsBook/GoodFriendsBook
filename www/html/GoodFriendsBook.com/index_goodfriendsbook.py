#!/usr/bin/python3


import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from html import escape
from http import cookies
from datetime import timedelta, datetime, timezone
import uuid

_NAME_OF_DOMAIN = 'GoodFriendsBook.com'
_FOLDERNAME_OF_BACKEND = os.path.dirname(os.environ['SCRIPT_FILENAME']).replace(f'/html/{_NAME_OF_DOMAIN}', '')
_PROJECT_VARIABLES = 'variables.py'

with open(f'{_FOLDERNAME_OF_BACKEND}/project_variables/{_PROJECT_VARIABLES}') as f: exec(f.read())

max_age = str(int(timedelta(seconds = 60*60*24*365).total_seconds()))
expires = str((datetime.now(timezone.utc) + timedelta(days=365)).strftime("%a, %d %b %Y %H:%M:%S GMT"))  # UTC = GMT for the most part, and are equal for code purposes.
domain = os.environ['HTTP_HOST'].replace('m.', '').replace('www.', '').replace('secure.', '')

cookies = cookies.SimpleCookie()
COOKIE_NAME = 'SESSION'
cookies[COOKIE_NAME] = str(uuid.uuid4())
cookies[COOKIE_NAME]['expires']  = expires
cookies[COOKIE_NAME]['path']     = '/'
cookies[COOKIE_NAME]['comment']  = 'GoodFriendsBook.com'
cookies[COOKIE_NAME]['domain']   = f'.{domain}'
cookies[COOKIE_NAME]['max-age']  = max_age
cookies[COOKIE_NAME]['secure']   = True
cookies[COOKIE_NAME]['version']  = '1'
cookies[COOKIE_NAME]['httponly'] = True
cookies[COOKIE_NAME]['samesite'] = 'Lax'    # 'Lax' or 'Strict'
COOKIE_HEADERS = cookies.output() # headers



html = ''
page = ''

# TODO: code goes into routes.py
# apache2 .config redirects /ajax/* pages to /
if os.environ['REQUEST_URI'].startswith('/ajax/'):
    page = os.environ['REQUEST_URI'].replace('/ajax/','')
    include(f'{AJAX_FOLDER}/{page}')
    exit()



html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<title>GoodFriendsBook.com</title>
<script type="text/javascript" src="js/jquery/jquery.min.js"></script>


<style>

#create_account:hover {{
    text-decoration:underline;
    text-decoration-color:blue;
}}

#recover_username_password:hover {{
    text-decoration:underline;
    text-decoration-color:blue;
}}

body {{
    background:lightgray;
    padding:0px;
    margin:0px;
}}

#left_column {{
    position:fixed;
    left: 20px;
    height: 400px;
    overflow-x: hidden;
    border:1px solid grey;
    background: lightgrey;
    overflow-y: hidden;
    min-width:250px;
    top:70px;
}}

#column_center {{
    position:absolute;
    left:300px;
    top:70px;
    height: 1600px;
    background: white;
    overflow-y: hidden;
    min-width:400px;
    width:38%;
}}

#right_column {{
    position:fixed;
    height: 400px;
    overflow-x: hidden;
    border:1px solid grey;     
    background: lightgrey;
    overflow-y: hidden;
    min-width:100px;
    top:70px;
}}

</style>

<script>

function is_InViewport(e6) {{
    var e1 = document.getElementById(e6);
    var e2 = e1.offsetTop;
    var e4 = e2 + e1.offsetHeight;
    var e3 = document.documentElement.scrollTop;
    var e5 = e3 + window.innerHeight;
    return e4 > e3 && e2 < e5;
}}




$( document ).ready(function() {{

    $('#create_account').click(function() {{

            event.preventDefault();

    }});

    $('#recover_username_password').click(function() {{

            event.preventDefault();

    }});

}});


</script>

</head>
<body>
{COOKIE_HEADERS} <br>
{FOLDERNAME_OF_BACKEND} <br>
{UPLOAD_FOLDER} <br>
{AJAX_FOLDER} <br>

<div style="margin:0px;padding:0px;position:fixed;width:100%;z-index:1000;background-color:lightyellow;height:53px;border-bottom:1px solid yellow;">
<span style="font-size:20px;font-weight:bold;">GoodFriendsBook.com</span>
</div>
<div id="data">

<div id="left_column" style="margin:0px;padding:0px;width:242px;height:90%">
    <div id="left_column_data" style="margin:0px;padding:0px;position:absolute;width:99%;border:1px solid yellow;">
    
        <span id="login" style="position:absolute;padding-top:0px;">




    <div style="border:2px solid grey;width:98%;height:250px;background:lightgray;">
      
        
        <center><b><span style="display:inline-block;background:white;width:100%;">GoodFriendsBook.com Login</span></b></center><br>

        <table style="background:lightgrey;">
        <tr>
        <td><span style="whitespace:nowrap;"><b>Username:</b></span></td><td><span><input id="username" style="width:130px"></span></td>
        </tr>
        <tr>
        <td><span style="whitespace:nowrap;"><b>Password:</b></span></td><td><span><input id="password" style="width:130px"></span></td>
        </tr>
        </table>
        <center><button>Login</button></center>


        <table style="margin:4px;padding:4px;background:lightgrey;">
        <tr>
        <td style="vertical-align:top;padding:10px;border:1px solid grey;margin:0px;padding:0px;background:white;"><center><a id="create_account" href="" style="color:black;background:white;">Create New Account</a></center></td> <td style="vertical-align:top;border:1px solid grey;margin:0px;padding:0px;background:white;"><center><a id="recover_username_password" href="" style="color:black;background:white;">Forgot existing username or password</a> </center></td>
        </tr>
        </table>
        
        
        <span style="margin:0px;padding:0px;position:absolute;top:251px;width:98%;border:1px solid black;">
        <center><b>Groups List</b></center>
           <span style="background:white;display:inline-block;height:419px;width:100%">
            user-defined
            </span>          
        </span>
        
        
        
    </div>

            
     </span>


    </div>
    
</div>

<div id="right_column" style="margin:0px;padding:0px;width:242px;height:90%">
    <div id="right_column_data" style="position:relative;height:98%;">
        <center><b>Friends List</b></center>
           <span style="background: white;display:inline-block;height:100%;width:100%">
            friend1
            friend2
            etc.
            </span>
    </div>
</div>
<div id="column_center">
    <div id="column_center_data">

        <div id="item1" style="z-index:1000;position:absolute;bottom:0px !important">&nbsp;</div>  
    </div>
</div>



</div>

<script>



function get_data() {{
        var data_val = ''
        $.ajax({{
            url: 'ajax/www_goodfriendsbook',
            type: 'POST',
            async: false,
            success: function(data) {{
                data_val = data;
            }}
        }});
        return data_val;
}}

const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
if (isMobile) {{
    $('#left_column').css('margin', '0');
    $('#left_column').css('padding', '0');
    $('#column_center').css('left', '0');
    $('#column_center').css('width', '100%');
}}


function resize() {{

    $('#column_center').css({{'min-width': ($(window).width() * .47) }});
    $('#right_column').css({{'left': ( parseInt($('#left_column').width() ) + parseInt($('#column_center').css('min-width')) + 175 ) }});

}} 


    window.scrollTo(0,0);
    
    resize();

    var h = $(window).height();
    
    var q = h / 3;
    
    
    var count = 0;
    
    function create_content(count, data) 
    {{
        var div_element =   `<div style="padding-top:1px;` + 
                            `border-top:2px solid darkgrey;` + 
                            `position:relative;` + 
                            `border-bottom:5px solid darkgrey;` + 
                            `height:` + (h - q) +`px;">item:`+count+ data +`</div>`;
        return div_element;
    }}
    
    
    for( var v = 0; v < 10; v++) {{
        $('#column_center_data').append( create_content(count, get_data()) );
        count = count + 1;
    }}
    
    $(window).on('resize scroll', function() {{
    
        var h = 0;
        if ( is_InViewport('item1') ) {{
            h = $('#column_center_data').height();
            $('#column_center').height( h + q );
            
            $('#column_center_data').append( create_content(count, get_data()) );
            count = count + 1;
        }}
        
    }});
    
    $(window).on('resize load', function() {{
        resize();
    }});
    
    $('.column_center').css({{'overflow':'hidden','-webkit-overflow-scrolling':''}});
    

    

    $('#right_column').css({{'margin-left': ( $('#column_center').width() / 26) }});
    
</script>

</body>

</html>


"""

if __name__ == '__main__':
        
    print(COOKIE_HEADERS)
    print("Content-Type:text/html;charset=utf-8;")
    print()
    print(html)








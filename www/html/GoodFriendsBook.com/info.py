#!/usr/bin/python3

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')



html = ''



linestyle = ''


html += f"""
<html>
<head>
<title>PyInfo GFB.com</title>
<meta charset="UTF-8">
 
 
<style>

#top {{
    display:inline-block;
    color:white;  
    width:100%;
    text-align:center;
    padding:0px;
    margin:5 auto;
}}

#top_span {{
    display:inline-block;
    background-color:black; 
    width:100%;
    text-align:center;
    padding:2px;
    margin:0 auto;
    border:5px solid yellow;
}}

#var1 {{
    display:flex;
    align-items:center;
    display:inline-block;
    width:25%;
    align:right;
    margin:16px;
    margin-right:5px;
    font-weight:bold;
}}

#value1 {{
    display:inline-block;
    margin:16px;
    margin-right:5px;
}}

.line span{{
    display:flex;
    align-items:center;
    display:inline-block;
}}

.center {{
    padding:0px;
    margin: 0 auto;
}}

</style>



</head>
<body>
        PYTHON3 INFORMATION



<table class="center" style="width:85%">
<tr><td>

<span id="top">
    <span id="top_span" class="center">
        <h1>Python 3 Environment</h1>
    </span>
</span>

</tr></td>
    
    
<tr><td>    
<span style="display:inline-block;width:100%;padding:0;margin:0;">
<table class="center" style="border:3px solid green;padding:10px;width:101%;">
"""


html += ''

for x, var in enumerate(os.environ.keys()):
    
    if ( (x % 2) == 0):
        linestyle = 'background-color:lightgrey;'
    else:
        linestyle = ''
    
    
    value = str(os.environ[var])
    value = value.replace('<address>','').replace('</address>','')
    
    html += f"""
                <tr><td>
                <span style="display:inline-block;width:100%;border:1px solid black;">
                    
                    <div class="line" style="{linestyle};">
                            <span id="var1" style="">{var}</span> : 
                            <span id="value1" style="">{value}</span>  
                    </div>
                    
                </span>
                </td></tr>
    """

html += '</table></span>'

html += '</td></tr></table>'

#print( session_cookie_value )
print("Content-Type:text/html;charset=utf-8;")
print()
print(html)

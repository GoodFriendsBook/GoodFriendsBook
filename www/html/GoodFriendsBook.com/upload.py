#!/usr/bin/python3


import os
import sys





html = ''


html += f"""
<html>
   <body>
      <h1>UPLOAD FILE</h1>
      <form enctype = "multipart/form-data" action = "https://localhost/ajax/upload_get.py" method = "post">
      <p>File: <input type = "file" name = "filename" /></p>
      <p><input type = "submit" value = "Upload" /></p>
      </form>
   </body>
</html>
"""

#print( session_cookie_value )
print("Content-Type:text/html;charset=utf-8;")
print()
print(html)
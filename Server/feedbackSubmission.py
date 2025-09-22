#!C:\Program Files\Python312\python.exe

# import cgi module:
import cgi
import os
os.environ["ProgramFiles"] = 'C:\\Program Files'

import mysql.connector


# output http header:
print ('Content-type: text/html')
print ('')
# note the empty print above is required!

print ('<html lang="en"><head><title>NPG</title></head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">')
print('<link rel="stylesheet" href="http://localhost/NPG/StyleSheets/HomePageStyle.css">')
print ('<body>')
print('''
    <div><div class="row page-header-row"><div class="col-sm-12 text-center page-header">
      <b><a title="NPG" class="hd" href="http://localhost/NPG/HtmlPages/HomePage.html">NETWORK PACKET GENERATOR</a>
                </b>
            </div>

        </div>
    </div>
    <div>
        <marquee class="header-scroll" direction="right" background="#FFFFCC">One stop tool to generate network packects
            using ARP, IP, DNS.</marquee>
    </div>
    <br />
    <br />
          <div class="container">
        <div class="row">
            <div class="col-sm-12 text-center">
                Feedback submitted successfully, Thank you, Please visit again.
            </div>
        </div>
    </div>''')

print ('</body></html>')

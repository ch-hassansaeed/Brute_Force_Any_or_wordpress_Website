# Brute_Force_Any_or_wordpress_Website
This brute force tool that can be use to brute force any websites or even on wordpress wp-admin page

## Execute Instructions
```
python index.py
```

## Requirements
```
pip2 install requests
pip2 install selenium
```

Chrome and chromedriver are required

You can download chromedriver here: http://chromedriver.chromium.org/downloads
for this fork, create a folder in your C drive called 'webdrivers' and place the executable file inside. If you want to use a different directory, simply change the CHROME_DVR_DIR variable inside the python file.

<br>
## How to use it <br>
```

CHROME_DVR_DIR = 'C:\chromedriver_win32\chromedriver.exe'      #>>>enter your chrome driver chromedriver.exe path<br>
website="https://www.wordpress_or_any_site_url.de/wp-admin"    #>>>Find a website url which has a login page <br>
username_selector = "#user_login"       #>>>Inspect element to find the Selector of the username ID (if class then .user_login)<br>
password_selector = "#user_pass"       #>>>Inspect element to find the Selector of the password ID (if class then .user_pass)<br>
login_btn_selector = "#wp-submit"     #>>>Inspect element to find the Selector of the submit or login button ID (if class then .wp-submit)<br>
username = "admin"    #>>>enter username in mostly cases wordpress has admin and other sites has administrator but if you dont know then make same file like passwords_list.txt i.e username_list.txt and use extra loop for it to check username<br>
pass_list = "passwords_list.txt"    #>>>some comman used password saved on this file you can add your list also <br>

```

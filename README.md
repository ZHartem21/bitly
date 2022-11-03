# Bitly URL shortener

This tool allows to transform an entered URL into a short bit.ly URL. It also allows to check the total number of clicks by entering an already created bit.ly URL.

### How to install

To use the tool you will first need to get your bit.ly access token. To recieve one you must first login into your bit.ly accound and then generate a new access token on [this page](https://app.bitly.com/settings/api/)
After generating the access token, you must create a new file called **bitly_project.env** in the project folder, and store your generated token inside of it as **BITLY_TOKEN**. 

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
# Dunmanapp - adapted from boyuan618/dunman app for purposes of NTU SCSE Competition

## Problems to solve
1. Unknown Flag raising venues
2. Messy Announcements
3. Complicated Leave forms
4. Teachers' locker numbers


## Hosted on
Amazon Elastic Beanstalk, using Flask(Amazon)/ Used ggl-login apis/telegram api/open weather api
## Debug Log

### 1. Adding a screenshot to Github readme.md --> Click on issues --> then drag and drop the image --> copy over the corresponding link

### 2. Google Oauth does not accept non top level domains for login
Tried Using EC2 to run a remote Linux instance to host the files and dapp led to errors
As it turns out, the domain name <http://ec2-52-207 (some more numbers) .compute-1.amazonaws.com/>'s top level domain is owned by Amazon and hence cannot be used. Another domain such as <http://flask-env.<some stuff>.us-east-1.elasticbeanstalk.com/> is accepted
![Screenshot (251)](https://user-images.githubusercontent.com/47784720/72682346-fbe2aa80-3b06-11ea-8ac7-81c7b134678f.png)

### 3. Choosing the wrong region provided by the (complimentary) Amazon Account 
Remember to check the one provided by the account
![Vocareum/Amazon Dashboard](https://user-images.githubusercontent.com/47784720/72682480-59c3c200-3b08-11ea-8618-65cb378d1c5a.png)
![Screenshot (253)](https://user-images.githubusercontent.com/47784720/72682452-2719c980-3b08-11ea-9deb-96371cdcd5b2.png)

### 4. Resetting of Amazon Account Login Session Duration
On the dashboard, a session expiry timer is provided. 

![image](https://user-images.githubusercontent.com/47784720/72682537-07cf6c00-3b09-11ea-8fc2-514d04099380.png)

Once the timing is up, the AWS Elastic Beanstalk Console Credentials will expire, and need to be changed in the .config file in the .aws directory.
![image](https://user-images.githubusercontent.com/47784720/72682548-31889300-3b09-11ea-9cba-95e353032f9c.png)

Otherwise, due to "restricted priviledges", one also needs to use the default account, unlike the creation of new credentials (which are restricted in the IAM console as some StackOverflow sources may recommend.

![Screenshot (258)](https://user-images.githubusercontent.com/47784720/72682529-c9d24800-3b08-11ea-8638-1c9040dd0989.png)

### 5. app.py is not supported, but Application.py is
```terminal
eb config
```

If one opens up the config file, one can see by searching WSGI settings that the default flask application looks for application.py, and hence will throw up errors if not found.

#!/usr/bin/python3
import requests, bs4, time
def refresh(lastupdt):
        position=0;
        url = 'http://www.skysports.com/transfer-centre'; #Standard url for skysports
        res = requests.get(url); # get source code of page
        soup = bs4.BeautifulSoup(res.text,'html.parser'); # make a bs object
        livecontent0 = soup.select('.fyre-comment > p');
        if lastupdt == 'initial run':
                for i in range(len(livecontent0)-1,-1,-1):
                        print(str(livecontent0[i].getText()+"\n"));
                        print(str("________________________________________________________________________\n"));
                return livecontent0[0].getText();
       	for j in range(len(livecontent0)): #finding position of lastupdt
                if lastupdt == livecontent0[j].getText():
                        position = j; 
                        break;               
        for i in range(position-1,-1,-1):#printing new updates
                print(str(livecontent0[i].getText()+"\n"));
                print(str("________________________________________________________________________\n"));
        return livecontent0[0].getText();
lastupdate = 'initial run';
while True:
        lastupdate = refresh(lastupdate);
        time.sleep(180);


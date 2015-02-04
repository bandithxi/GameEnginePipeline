import re
import urllib

def updateImage():
    try:
        
        # Retrieve new image links 
        fileStr = urllib.urlopen('http://www.xkcd.com').read()
        newLink = re.search('<img\ssrc="http://imgs.xkcd.com/comics/(.*)\.png', fileStr )
        
        fileStr = urllib.urlopen('http://www.abstrusegoose.com').read()
        newLink1 = re.search('<img\ssrc="http://abstrusegoose.com/strips/(.*)\.png', fileStr )

        # Retrieve old imag links for visual feedback
        fileStr = urllib.urlopen('http://www.cse.unr.edu/~phommounivong/index.html').read()
        oldLink = re.search('<img\ssrc="http://imgs.xkcd.com/comics/(.*)\.png', fileStr )
        oldLink1 = re.search('<img\ssrc="http://abstrusegoose.com/strips/(.*)\.png', fileStr )

        # Report links to be changed 
        print 'Old Source XKCD'
        print(oldLink.group(0))

        print 'Old Source Abstruse Goose'
        print(oldLink1.group(0))

        # Report links to use as updated
        print 'New Source'
        print(newLink.group(0))
        print(newLink1.group(0))

        
        # Update site
        filePtr = open('index.html', 'w')
        fileStr = re.sub('<img\ssrc="http://imgs.xkcd.com/comics/(.*)\.png', newLink.group(0), fileStr)
        fileStr = re.sub('<img\ssrc="http://abstrusegoose.com/strips/(.*)\.png', newLink1.group(0), fileStr)
        filePtr.write(fileStr)
        
        filePtr.close    
    except Exception:
        print('Some error has happened')
    print 'success'

# Update site to an old state
def superBowlImage():
    fileStr = urllib.urlopen('http://www.cse.unr.edu/~phommounivong/index.html').read()

    fileStr = re.sub('<img\ssrc="http://imgs.xkcd.com/comics/(.*)\.png', '<img src="http://imgs.xkcd.com/comics/super_bowl.png', fileStr)
    fileStr = re.sub('<img\ssrc="http://abstrusegoose.com/strips/(.*)\.png', '<img src="http://abstrusegoose.com/strips/50_percent_of_all_humans_have_a_serious_design_flaw.png' , fileStr)    
    
    filePtr = open('index.html', 'w')
    filePtr.write(fileStr)
        
    filePtr.close 

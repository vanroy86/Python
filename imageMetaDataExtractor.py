import urllib2
from bs4 import BeautifulSoup
from urlparse import urlsplit
from os.path import basename
import optparse
from PIL import Image
from PIL.ExifTags import TAGS

def findImages(url):
    print "[+] Downloading Images on " + url
    urlContent = urllib2.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll("img")
    return imgTags

def downloadImage(imgTag):
    try:
        print "[+] Downloading Image..."
        imgSrc = imgTag["src"]
        imgContent = urllib2.urlopen(urlSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, "wb")
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ""

def testForExif(imgFileName):
    try:
        exifData = []
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifDATA["GPSInfo"]
            if exifGPS:
                print "[*] " + imgFileName + "contains GPS MetaData"
    except:
        pass

def main():
    parser = optparse.OptionParser("Usage: -u <target url>")
    parser.add_option("-u", dest="url", type="string", help="Specify a target url")
    (options, args) = parser.parse_args()
    url = options.url

    if url == None:
        print parser.usage
        exit(0)
    else:
        imgTags = findImages(url)
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag)
            testForExif(imgFileName)

if __name__ == "__main__":
    main()

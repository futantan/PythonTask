import sgmllib
import threading
import urllib2


# define a Thread class to handle web download
class DownloadThread(threading.Thread):
    def __init__(self, websiteSet, path):
        threading.Thread.__init__(self)
        self.websites = websiteSet
        self.saveDir = path
        self.mkdir()

    def run(self):  # Overwrite method, here we can do something we want in the thread
        while not len(self.websites) == 0:
            web = self.websites.pop()
            self.download(web)

    def download(self, website):  # here is the code for download
        print 'isDownLoading::::' + website
        url = website
        webdata = urllib2.urlopen(url).read()
        location = str(url) + ".html"
        location = location.replace('/', '\\')
        location = self.saveDir + "/" + location
        output = open(location, "w")
        output.write(webdata)
        output.close()

    def mkdir(self):  # create the dir for saving pages
        # import module
        import os

        path = self.saveDir.strip()
        path = path.rstrip("\\")

        isExists = os.path.exists(path)

        if not isExists:
            os.makedirs(path)
            return True
        else:
            return False


class LinksParser(sgmllib.SGMLParser):
    urls = []

    def do_a(self, attrs):
        for name, value in attrs:
            if name == 'href' and value not in self.urls:
                if value.startswith('http'):
                    self.urls.append(value)
                    # print value
                else:
                    continue
                return


def getLinkToDownload(link):
    webToDown = set()
    p = LinksParser()
    f = urllib2.urlopen(link)
    p.feed(f.read())
    for url in p.urls:
        webToDown.add(url)
    f.close()
    p.close()
    webToDown = set([elem for elem in webToDown if elem.find('baidu.com') != -1])
    return webToDown


downloadPath = 'webDownload'
links = getLinkToDownload('http://www.baidu.com')
thread1 = DownloadThread(links, downloadPath)
thread2 = DownloadThread(links, downloadPath)
thread1.start()
thread2.start()
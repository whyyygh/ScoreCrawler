class EopPageItem(object):
    def __init__(self, strid,url, date,title,author):
        self.strid = str(strid)
        self.id = int(strid)
        self.url = str(url)
        self.date = str(date)
        self.title = str(title)
        self.author = str(author)
        #五线谱地址
        self.staveUrl = 'http://www.everyonepiano.cn/Stave-'+str(id)+'.html'
        #简谱地址
        self.numberUrl = 'http://www.everyonepiano.cn/Number-'+str(id)+'.html'
    def print_attrs(self):
        print(
            'id:', self.id, ',',
            'url:', self.url, ',',
            'date:', self.date, ',',
            'title:', self.title, ',',
            'author:', self.author, ',',
        )
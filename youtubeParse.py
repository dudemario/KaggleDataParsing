from turtle import *
from random import randint
from time import *
'''
To change axis:
Change ln 25 to maxX_AXIS
Change ln 42 to maxY_AXIS
Change ln 223 to correct formula
Change ln 245 as follows:
    if video.getY_AXIS()>calcOptimalY_AXIS(video.getX_AXIS()):
Change ln 248 as follows:
    goto(video.getX_AXIS()*500.0/maxX_AXIS, video.getY_AXIS()*500.0/maxY_AXIS)
Change ln 270 to "Y_AXIS vs X_AXIS"
'''

#maxViews = 56843038.0 
#maxLikes = 2542863.0
#maxComments = 519092
#maxDislikes = 124555
#maxSubs = 33163966
#Draw Graph
def drawGraph(maxViews, maxLikes):
    screen = Screen()
    bgcolor("black")
    setworldcoordinates(-50,-20,520,520)
    shape("circle")
    turtlesize(0.2, 0.2, 0.2)
    tracer(200)
    color("white")
    width(2)
    for i in range(83, 499, 83):
        forward(83)
        right(90)
        forward(15)
        left(90)
        backward(55)
        write(int(maxViews*i/500), font=("Arial", 13, "normal"))
        forward(55)
        right(90)
        backward(15)
        left(90)
    home()
    left(90)
    for i in range(83, 499, 83):
        forward(83)
        left(90)
        forward(50)
        write(int(maxLikes*i/500), font=("Arial", 13, "normal"))
        backward(50)
        right(90)
    home()
    pu()

categoryDict = {1 : "Film & Animation",
                2 : "Autos & Vehicles",
                10 : "Music",
                15 : "Pets & Animals",
                17 : "Sports",
                18 : "Short Movies",
                19 : "Travel & Events",
                20 : "Gaming",
                21 : "Videoblogging",
                22 : "People & Blogs",
                23 : "Comedy",
                24 : "Entertainment",
                25 : "News & Politics",
                26 : "Howto & Style",
                27 : "Education",
                28 : "Science & Technology",
                29 : "Nonprofits & Activism",
                30 : "Movies",
                31 : "Anime/Animation",
                32 : "Action/Adventure",
                33 : "Classics",
                34 : "Comedy",
                35 : "Documentary",
                36 : "Drama",
                37 : "Family",
                38 : "Foreign",
                39 : "Horror",
                40 : "Sci-Fi/Fantasy",
                41 : "Thriller",
                42 : "Shorts",
                43 : "Shows",
                44 : "Trailers"}

class Video:
    def setVariables(self, vId, trendingDate, vTitle, channelTitle, catId, publishTime, tags, views, likes, dislikes, commentsCount, subscribers, thumbnailLink, options, description):
        self.videoId = vId
        self.trendDate = trendingDate
        self.videoTitle = vTitle
        self.videoChannel = channelTitle
        self.category = int(catId)
        self.videoDateTime = publishTime
        self.videotags = tags.split("|")
        self.numViews = int(views)
        self.numLikes = int(likes)
        self.numDislikes = int(dislikes)
        self.numComments = int(commentsCount)
        if subscribers.isdigit():
            self.numSubs = int(subscribers)
        else:
            self.numSubs = 0
        self.thumbnail = thumbnailLink
        self.videoOptions = options
        self.videoDescription = description

    def __init__(self, *dataList):
        if type(dataList[0]) == list:
            dataList = dataList[0]
        self.setVariables(dataList[0], dataList[1], dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7], dataList[8], dataList[9], dataList[10], dataList[11], dataList[12], (dataList[13], dataList[14], dataList[15]), dataList[16])

    def getCat(self):
        return self.category

    def getId(self):
        return self.videoId

    def __str__(self):
        return "Video"

    def setVideoDescription(self, newDescription):
        self.videoDescription = newDescription

    def getVideoDescription(self):
        return self.videoDescription

    def getViews(self):
        return self.numViews

    def getLikes(self):
        return self.numLikes

    def getComments(self):
        return self.numComments

    def getDislikes(self):
        return self.numDislikes

    def getSubs(self):
        return self.numSubs
    
    def __str__(self):
        return "Video Id: "+ self.videoId+", Views: "+str(self.numViews)+", Likes: "+str(self.numLikes)

class VideoCategory:
    def __init__(self, name):
        self.name = name
        self.videos = []
    def addVideo(self, newVideo):
        self.videos.append(newVideo)
    def __len__(self):
        return len(self.videos)
    def getName(self):
        return self.name
    def getVideo(self, vidId):
        for vid in self.videos:
            if vid.getId() == vidId:
                return vid
    def getId(self):
        return self.videoId
    def __eq__(self, other):
        return other.getId() == self.getId()
    def getAllVideos(self):
        return self.videos
    def sort(self):
        self.videos = sorted(self.videos, key=lambda vid:vid.getViews())
    def getMaxViews(self):
        maxViews = -99999999
        for vid in self.videos:
            maxViews = max(maxViews, vid.getViews())
        return maxViews
    def getMaxLikes(self):
        maxLikes = -99999999
        for vid in self.videos:
            maxLikes = max(maxLikes, vid.getLikes())
        return maxLikes
                           
class AllCategories:
    def __init__(self):
        self.categories = {}
    def addNewCategory(self, newCategoryName):
        self.categories[newCategoryName] = VideoCategory(newCategoryName)
        return self.categories[newCategoryName]
    def getCategory(self, newCategoryName):
        if newCategoryName in self.categories:
            return self.categories[newCategoryName]
    def getAllCategories(self):
        return self.categories

#Read in data
def readInData(allVideos, headings, fIn):
    for line in fIn:
        if "\\n" in line.strip().split(",")[0]:
            #print(line)
            vid.setVideoDescription(vid.getVideoDescription()+line.strip())
        else:
            try:
                #Check for extra commas
                vidData = line.strip().split(",")
                if vidData[4].isdigit():
                    vid = Video(line.strip().split(",", len(headings)-1))
                else:
                    num = 4
                    while not vidData[num].isdigit():
                        num+=1
                    vidTitle = ""
                    for i in range(2, num-1):
                        vidTitle+= vidData[i]
                    vidDesc = ""
                    for i in range(num+13, len(vidData)):
                        vidDesc+=vidData[i]
                    vid = Video(vidData[0], vidData[1], vidTitle, vidData[num-1], vidData[num], vidData[num+1], vidData[num+2], vidData[num+3], vidData[num+4], vidData[num+5], vidData[num+6], vidData[num+7], vidData[num+8], vidData[num+9], vidData[num+10], vidData[num+11], vidData[num+12], vidDesc)

                #Create video category object
                vidCategory = allVideos.getCategory(categoryDict[vid.getCat()])
                if not vidCategory:
                    vidCategory = allVideos.addNewCategory(categoryDict[vid.getCat()])
                vidCategory.addVideo(vid)
            except IndexError:
                print("Error at: " +line)

def calcOptimalLikes(viewCount):
    return viewCount*0.03

def calcOptimalComments(viewCount):
    return viewCount*0.005

def calcOptimalViews(subs):
    return subs*0.14

#Draw plot graph points
def drawCategoryGraph(catNum, allVideos, maxViews, maxLikes):
    global hcount, lcount
    color(randint(0, 255)/255.0, randint(0, 255)/255.0, randint(0, 255)/255.0)
    category = allVideos.getCategory(categoryDict[catNum])
    
    for video in category.getAllVideos():
        if video.getLikes()>calcOptimalLikes(video.getViews()):
            hcount += 1
        else:
            lcount += 1
            
        goto(video.getViews()*500.0/maxViews, video.getLikes()*500.0/maxLikes)
        stamp()
    print("Finished Graph")
    
def drawSummary(catNum=-1):
    fIn = open("CAvideos2.csv", "r", encoding="latin-1")
    headings = fIn.readline().strip().split(",")
    
    allVideos = AllCategories()
    readInData(allVideos, headings, fIn)
    #How many above, and how many below
    global hcount
    global lcount
    hcount = 0
    lcount = 0

    if catNum == -1:
        maxViews = 56843038
        maxLikes = 2542863
    else:
        maxViews = allVideos.getCategory(categoryDict[catNum]).getMaxViews()
        print(maxViews)
        maxLikes = allVideos.getCategory(categoryDict[catNum]).getMaxLikes()

    drawGraph(maxViews, maxLikes)
    
    #Valid Categories:
    cats = [1, 2, 10, 15, 17, 19, 20, 22, 23, 25, 26, 27, 28, 29, 43]
    
    if catNum == -1:
        #Draw graph for all categories
        for i in cats:
            drawCategoryGraph(i, allVideos, maxViews, maxLikes)
    else:
        #Draw graph for one category
        drawCategoryGraph(catNum, allVideos, maxViews, maxLikes)
    
    
    color("yellow")
    
    #Draw trend line
    home()
    width(5)
    pd()
    goto(500, calcOptimalLikes(maxViews)*500/maxLikes)
    pu()


    #Graph Title
    goto(400, 450)
    write("Likes vs Views\nAbove Line: "+str(hcount)+"\nBelow Line: "+str(lcount), font=("Arial", 20, "normal"))

    mainloop()  

import instaloader
import time

USER = "m_aexu" #User acc which can acces instagram...(load session created "instaloader -l USERNAME)"

L = instaloader.Instaloader()
L.load_session_from_file(USER) # Load the created Session (see comment & command Line 3)

def readFile(fileName): # IT WORKS DONT TOUCH IT ;)

    with open(fileName, "r") as fileContent:  # opens the file in read mode
        content = fileContent.readlines()
        global contentList
        contentList= []

        for u in content:
            sp = u.split(",")
            contentList.append(sp[0].replace("\n",""))

    return contentList

def download_post():
    print(" ===== Download Start ===== ")
    for u in contentList:
        po = instaloader.Profile.from_username(L.context, u).get_posts()
        print(" - User: " + u)
        for post in po:
            print("Fetching Content from: " + u + "...")
            L.download_post(post, u)




# ===== START ======

# todo Need a question if new download or --fast-update profeile (so the profile only gets updated
# todo option to exclude accounts
print(" === Start === ")
print("Please enter path: ")
fileName = str(input())
readFile(fileName)
print("Download will start any moment. This will take a lot of time...")
time.sleep(5)
download_post()
print(" == Done ==")

# C:\Users\Max\PycharmProjects\instaread\test_followed_2.txt

import instaloader

USER = "m_aexu" #User acc which can acces instagram...(load session created "instaloader -l USERNAME"
acc_target = USER


# Get instance
L = instaloader.Instaloader()

L.load_session_from_file(USER) # Load the created Session (see comment & command Line 3)

profile = instaloader.Profile.from_username(L.context, acc_target) # Target profile

# Print list of followees
follow_list = []
file = open("test_followed_2.txt","a+") # Name of the output File
for followee in profile.get_followees():
    username = followee.username
    file.write(username + "\n")
    print(username)

file.close()

# -- DEV ZONE -- #
# You can change this to anything
VERSION = "v0.0.3_inv-beta-1"
# -------------- #

# -- General -- #

# ///video/// #

# get medium-quality video instead of HLS
# NOTE: loads a ton faster
# True, False
MEDIUM_QUALITY = True 

# resolution for HLS playback
# also preferred resolution for medium-quality
# None, 144, 240, 360, 480, 720, 1080...
HLS_RESOLUTION = 360

# ////////// #

# Set indivious instance
# add http:// or https://
URL = "https://lekker.gay/"

# Set port
# Anything around 1000-10000
# NOTE: set common ports so you can remember it.
PORT = "6969"

# Debug mode 
# NOTE: recommended True if you want to fix the code and auto reload
DEBUG = True

# Spying on stuff
# NOTE: Don't judge people on their search lol
SPYING = False

# -- Custom functions -- #

# Number of featured videos (including categories)
# max: 50
FEATURED_VIDEOS = 50

# Number of search videos
# max: 20
SEARCHED_VIDEOS = 20

# Number of displayed comments
# max: 20
COMMENTS = 20

# Sort comments
# "newest", "popular"
SORT_COMMENTS = "popular"

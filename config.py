from config_hub import *


DATA_SRC_SERVER = "myhost"
DATA_SRC_PORT = 27017
DATA_SRC_DATABASE = "tutorial_src"
DATA_SRC_SERVER_USERNAME = None
DATA_SRC_SERVER_PASSWORD = None

DATA_TARGET_SERVER = "myhost"
DATA_TARGET_PORT = 27017
DATA_TARGET_DATABASE = "tutorial"
DATA_TARGET_SERVER_USERNAME = None
DATA_TARGET_SERVER_PASSWORD = None

HUB_DB_BACKEND = {
		"module" : "biothings.utils.mongo",
		"uri" : "mongodb://myhost:27017",
		}
		
DATA_ARCHIVE_ROOT = "/tmp/tutorial"
LOG_FOLDER = "/tmp/tutorial/logs"
DIFF_PATH = "/Users/annatswater/Desktop/Whatever"
RELEASE_PATH = "/Users/annatswater/Desktop/Whatever"
EVENT = "whatever"

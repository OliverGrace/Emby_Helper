import requests
import json

from requests.models import guess_json_utf

# set the url
url = "URL"

# set the api key
api_key = "API"

# set the api path
api_path = "/emby/"

# set the get user api path
get_user_api_path = "user_usage_stats/user_list"


# combine the api path and the api key
link = url + api_path + get_user_api_path + "?api_key=" + api_key

# set the application/json header
headers = {'Content-Type': 'application/json'}

# curl GET request
response = requests.get(link, headers=headers)

# response to dictionary
response_dict = json.loads(response.text)

def get_user_id(name):
    for user in response_dict:
        if user['name'] == name:
            return user['id']

def create_a_user_by_name(name):
    # make the name a json object
    name_json = json.dumps({"Name": name})
    # method path is Users/new
    method_path = "Users/new"
    # combine the path and the method path and api key
    link = url + api_path + method_path + "?api_key=" + api_key
    # set headers to application/json
    headers = {'Content-Type': 'application/json'}
    # curl POST request
    response = requests.post(link, data=name_json, headers=headers)
    # response to dictionary
    response_dict = json.loads(response.text)
    # return the user id
    return response_dict['Id']


config = """{"AudioLanguagePreference": "","PlayDefaultAudioTrack": true,"SubtitleLanguagePreference": "","DisplayMissingEpisodes": false,"SubtitleMode": "Default","EnableLocalPassword": true,"OrderedViews": [],"LatestItemsExcludes": [],"MyMediaExcludes": ["361063e308310389b1c7f504760a30f3"],"HidePlayedInLatest": true,"RememberAudioSelections": true,"RememberSubtitleSelections": true,"EnableNextEpisodeAutoPlay": true,"ResumeRewindSeconds": 0}"""
policy = """{    "IsAdministrator": false,    "IsHidden": true,    "IsHiddenRemotely": true,    "IsHiddenFromUnusedDevices": true,    "IsDisabled": false,    "BlockedTags": [],    "IncludeTags": [],    "IsTagBlockingModeInclusive": false,    "EnableUserPreferenceAccess": true,    "AccessSchedules": [],    "BlockUnratedItems": [],    "EnableRemoteControlOfOtherUsers": false,    "EnableSharedDeviceControl": false,    "EnableRemoteAccess": true,    "EnableLiveTvManagement": false,    "EnableLiveTvAccess": true,    "EnableMediaPlayback": true,    "EnableAudioPlaybackTranscoding": false,    "EnableVideoPlaybackTranscoding": false,    "EnablePlaybackRemuxing": false,    "EnableContentDeletion": false,    "EnableContentDeletionFromFolders": [],    "EnableContentDownloading": false,    "EnableSubtitleDownloading": false,    "EnableSubtitleManagement": false,    "EnableSyncTranscoding": false,    "EnableMediaConversion": false,    "EnabledChannels": [],    "EnableAllChannels": true,    "EnabledFolders": [],    "EnableAllFolders": true,    "InvalidLoginAttemptCount": 0,    "EnablePublicSharing": true,    "RemoteClientBitrateLimit": 0,    "AuthenticationProviderId": "Emby.Server.Implementations.Library.DefaultAuthenticationProvider",    "ExcludedSubFolders": [],    "SimultaneousStreamLimit": 0,    "EnabledDevices": [],    "EnableAllDevices": true  }"""
password = """{"Id": insert,"CurrentPw": "string","NewPw": "string","ResetPassword": true}"""

def update_user_config(user_id, config):
    # method path is Users/config
    method_path = "Users/" + user_id + "/Configuration"
    # combine the path and the method path and api key
    link = url + api_path + method_path + "?api_key=" + api_key
    # set headers to application/json and accept: */*
    headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    # curl POST request
    response = requests.post(link, data=config, headers=headers)
    # print the response code
    return response.status_code

def update_user_policy(user_id, policy):
    # method path is Users/policy
    method_path = "Users/" + user_id + "/Policy"
    # combine the path and the method path and api key
    link = url + api_path + method_path + "?api_key=" + api_key
    # set headers to application/json and accept: */*
    headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    # curl POST request
    response = requests.post(link, data=policy, headers=headers)
    # print the response code
    return response.status_code

def delete_user(user_id):
    # method path is Users/delete
    method_path = "Users/" + user_id
    # combine the path and the method path and api key
    link = url + api_path + method_path + "?api_key=" + api_key
    # set headers to  accept: */*
    headers = {'Accept': '*/*'}
    # curl DELETE request
    response = requests.delete(link, headers=headers)
    # print the response code
    return response.status_code


def clear_password(user_id, password):
    # replaace the insert with "USERID"
    password = password.replace("insert", '"'+user_id+'"')
    # method path is Users/clear_password
    method_path = "Users/" + user_id + "/Password"
    # combine the path and the method path and api key
    link = url + api_path + method_path + "?api_key=" + api_key
    # set headers to application/json and accept: */*
    headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    # curl POST request with passwor data
    response = requests.post(link, data=password, headers=headers)
    # print the response code
    return response.status_code


# The following is the calling of the functions, they return the status code or the user id
# print(create_a_user_by_name("og"))
# print(get_user_id("og"))
# print(update_user_config(get_user_id("og"), config))
# print(update_user_policy(get_user_id("og"), policy))
# print(delete_user(get_user_id("og")))
# print(clear_password(get_user_id("og"), password))





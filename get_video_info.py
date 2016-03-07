import requests
import os

auth_code = os.environ.get('WIREWAX_TOKEN')



def get_video_info():
	url_endpoint = 'http://hobnob.wirewax.com/public/video/8028026'
	# url_endpoint = 'http://hobnob.wirewax.com/video/' + str(vid_id) + "/" + api_ref + "/"
	header = {'Authorization': 'Bearer ' + auth_code}

	r = requests.get(url_endpoint, headers=header)

	print r.json()

get_video_info()

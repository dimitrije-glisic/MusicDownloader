import requests

import json

import sys


from langdetect import detect


def find_most_similar_name(original,data):
	max_matching = -1
	max_name = ''
	max_name_id = -1
	for d in data:
		name = d['name']
		name_id = d['id']
		matching = 0
		for i in range(0,min(len(original),len(name))):
			if original[i] == name[i]:
				matching += 1
		if matching > max_matching:
			max_matching = matching
			max_name = name
			max_name_id = name_id
	return max_name_id,max_name


def is_similar(original,string):
	matching = 0
	for i in range(0,min(len(original),len(string))):
		if original[i] == string[i]:
			matching += 1
	return len(original) == matching 


def get_albums(artist_name):
	#izvodjac
	url_artist = f'https://api.deezer.com/search/artist/?q={artist_name.split()[0]}&name={artist_name}'
	r = requests.get(url_artist)
	json_data = json.loads(r.text)
	artist_id, artist_name = find_most_similar_name(artist_name,json_data['data'])

	#albumi
	url_albums = f'https://api.deezer.com/artist/{artist_id}/albums'
	r = requests.get(url_albums)
	json_data = json.loads(r.text)
	#json_formatted_str = json.dumps(json_data,indent=2)
	json_albumi = json_data['data']
	dct_album_pesme = {}
	for a in json_albumi:
		naslov_albuma = a['title']
		dct_album_pesme[naslov_albuma] = []
		url_one_album = f"https://api.deezer.com/album/{a['id']}"
		r = requests.get(url_one_album)
		json_data = json.loads(r.text)
		pesme = json_data['tracks']['data']
		for p in pesme:
			p_id = p['id']
			url_track = f'https://api.deezer.com/track/{p_id}'
			r = requests.get(url_track)
			json_data = json.loads(r.text)
			artist = json_data['artist']['name']
			if is_similar(artist_name,artist):
				dct_album_pesme[naslov_albuma].append(p['title'])
	return dct_album_pesme



if __name__ == '__main__':

	print('In the script...')

	if len(sys.argv) < 2:
		print('Nedovoljan broj argumenata!')
		sys.exit()

	izvodjac = sys.argv[1]

	if len(sys.argv) > 2:
		for i in range(2,len(sys.argv)):
			izvodjac += ' ' + sys.argv[i]	


	#izvodjac
	url_artist = f'https://api.deezer.com/search/artist/?q={sys.argv[1]}&name={izvodjac}'
	r = requests.get(url_artist)
	json_data = json.loads(r.text)
	#json_formatted_str = json.dumps(json_data,indent=2)
	#izaberi najpopularnijeg izvodjaca
	artist_id,artist_name = find_most_similar_name(izvodjac,json_data['data'])
	#alternative izvodjac
	print(artist_name)

	#albumi
	url_albums = f'https://api.deezer.com/artist/{artist_id}/albums'
	r = requests.get(url_albums)
	json_data = json.loads(r.text)

	#json_formatted_str = json.dumps(json_data,indent=2)

	albumi = json_data['data']

	print('Consuming json_data')
	print(json_data)

	albumi_sa_pesmama = {}

	for a in albumi:
		naslov = a['title']
		print(f"Pesme iz albuma:{naslov}:")

		url_one_album = f"https://api.deezer.com/album/{a['id']}"
		r = requests.get(url_one_album)
		json_data = json.loads(r.text)
		pesme = json_data['tracks']['data']
		for p in pesme:
			p_id = p['id']
			url_track = f'https://api.deezer.com/track/{p_id}'
			r = requests.get(url_track)
			json_data = json.loads(r.text)
			artist = json_data['artist']['name']
			if not is_similar(izvodjac,artist):
				print(f'Nije slican {artist}!')
			print(artist,p['title'])
		print('-'*50)



	albumi = []

	print('Consuming againg json_data')
	print(json_data)
	data = json_data['data']


	albumi_id = set()
	albumi_naslovi = []
	for row in data:
		naslov_albuma = row['album']['title']
		id_albuma = row['album']['id']
		albumi_id.add(id_albuma)



	titles = set()
	for alid in albumi_id:
		url = f'https://api.deezer.com/album/{alid}'
		r = requests.get(url)
		json_data = json.loads(r.text)

		tracks = json_data['tracks']['data']

		for t in tracks:
			title = t['title']
			titles.add(title)

	f = open('songs','w')


	for t in titles:
		f.write(t + '\n')


	print(f'Pronadjeno je {len(titles)} pesama!')




import requests

def search_map(search_title):
    searching = search_title
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
    headers = {
        "Authorization": "KakaoAK 카카오Key"
    }
    places = requests.get(url, headers = headers).json()['documents']
    try:
        # return places[0]['place_url']
        return places[0]
    except:
        return '검색결과없음'

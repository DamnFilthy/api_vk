# import of libraries
import requests
from pprint import pprint
from urllib.parse import urljoin

# Constans
TOKEN = 'токен'
API_BASE_URL = 'https://api.vk.com/method/'
HOME_PAGE = 'https://vk.com/id'
V = '5.21'

# class VK User
class VKApiClient:
    BASE_URL = API_BASE_URL
    def __create_method_url(self, method):
        return urljoin(self.BASE_URL, method)

    # Initialise
    def __init__(self, id, token=TOKEN, version=V):
        self.id = id
        self.token = token
        self.version = version

    # Finding mutual friends
    def get_mutual_friends(self, second_friend_id):
        response = requests.get(self.__create_method_url('friends.getMutual'),
        params={
        'access_token': self.token,
        'v': self.version,
        'source_uid' : self.id,
        'target_uid': second_friend_id
        })
        return response.json()
    # Return user ID
    def get_id(self):
        return self.id
    # Return user link page
    def __str__(self):
        return f'https://vk.com/id{self.id}'
    # Return  mutual friends
    def __and__(self, other):
         return self.get_mutual_friends(other.get_id())

if __name__ == '__main__':
    # Creating instances of the class
    vk_client = VKApiClient(336261034, TOKEN, V,)
    user_anya = VKApiClient(12790238, TOKEN, V)
    user_tanya = VKApiClient(7844411, TOKEN, V)

    # Output
    pprint(vk_client.get_mutual_friends(user_anya.get_id()))
    print(user_tanya & vk_client)
    print(user_anya & user_tanya)

    print(vk_client)
    print(user_anya)
    print(user_tanya)

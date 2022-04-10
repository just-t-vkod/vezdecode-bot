import vk_api

tokenUser = vk_api.VkApi(token = '')

result = tokenUser.method('photos.get', {'owner_id': -197700721,
                                        'album_id': 281940823,
                                        'count': 1000})
for photo in result['items']:
    actionDB.addPhoto(photo['id'], 'photo'+str(photo['owner_id'])+'_'+str(photo['id']))

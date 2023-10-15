import aiohttp


class WasdAPIClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://wasd.tv/api/"

    async def get_channel_info(self, channel_name):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}v2/broadcasts/public",
                headers={"Authorization": f"Token {self.token}"},
                params={"channel_name": channel_name}
            ) as response:
                data = await response.json()
                result = data.get("result")
                if result:
                    return result
                else:
                    return None

    async def print_broadcast_info(self, data):
        channel_info = data.get('channel', {})
        media_container_info = data.get('media_container', {})
        tags = data.get('tags', [])

        print("Информация о канале:")
        print(f"Имя канала: {channel_info.get('channel_name', '')}")
        print(f"Описание канала: {channel_info.get('channel_description', '')}")
        print(f"Ссылка на обложку канала: {channel_info['channel_image']['large']}")

        print("\nИнформация о медиаконтейнере:")
        print(f"Название медиаконтейнера: {media_container_info.get('media_container_name', '')}")
        print(f"Описание медиаконтейнера: {media_container_info.get('media_container_description', '')}")
        print(f"Ссылка на обложку медиаконтейнера: {media_container_info['game']['game_icon']['large']}")

        print("\nТеги:")
        for tag in tags:
            print(f"Название тега: {tag.get('tag_name', '')}")
            print(f"Описание тега: {tag.get('tag_description', '')}")
            print("---------------------------")



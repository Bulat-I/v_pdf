from aiogram.filters import Filter
from aiogram import Bot, types

class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __cal__(self, message: types.message) -> bool:
        return message.chat.type in self.chat_types
    
class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __cal__(self, message: types.message, bot: Bot) -> bool:
        return message.from_user.id in bot.my_admins_list
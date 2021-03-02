# Boticord Python Library

Простой Python модуль для работы с Boticord API (не официальный).

### Установка

Установка через pip (рекомендуется)

`pip3 install boticordpy`

### Функционал

* Отправка статистики
* Получение всех ботов пользователя
* Получение информации о боте
* Получение комментариев бота

### Примеры

Публикация статистики при подключении:

```
from boticordpy import BoticordClient
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
boticord = BoticordClient(bot, token="your-boticord-token")

@bot.event
async def on_connect():
    stats = {"servers": 729, "shards": 1, "users": 160895}
    await boticord.postStats(stats)


bot.run("your-bot-token")
```

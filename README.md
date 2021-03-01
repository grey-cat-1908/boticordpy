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
import boticordpy
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
boticord = boticordpy.BoticordClient(bot, token="your-boticord-token")

@bot.event
async def on_connect():
    stats = {"servers": 15000, "shards": 5, "users": 500000}
    await boticord.postStats(stats)


bot.run("your-bot-token")
```

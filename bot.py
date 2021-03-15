# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='jadwal')
async def nine_nine(ctx):
    jadwal = '''
    SENIN : Bahasa Inggris 3, Sistem Berkas, Graph Terapan, Aljabar Linier.\nSELASA : Jaringan Komputer, Struktur Data.\nRABU : Statistik Dasar, Matematika Diskrit, Praktikum Fisika 2.\n
    '''
    await ctx.send(jadwal)

bot.run(TOKEN)

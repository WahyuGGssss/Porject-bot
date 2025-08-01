# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
import random
from discord.ext import commands
import os
import requests

# Kita tambahkan folder untuk menyimpan laporan
os.makedirs('./files/laporan_polusi', exist_ok=True)

# Fungsi untuk menghasilkan kata sandi (dari bot_logic.py jika ada)
def gen_pass(length):
    char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    password = ''.join(random.choice(char_list) for i in range(length))
    return password

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
# subtracting two numbers
@bot.command()
async def min(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)
# multiplication two numbers
@bot.command()
async def times(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left*right)
# division two numbers
@bot.command()
async def divide(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left/right)
# exp two numbers
@bot.command()
async def exp(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left**right)


# # give local meme see python folder Data Science drive
@bot.command()
async def meme(ctx):
    # Coba ganti dengan gambar meme yang ada di komputer Anda
    # img_name = random.choice(os.listdir('images'))
    with open(f'meme/images.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

# duck and dog API
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def tulis(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)

@bot.command()
async def tambahkan(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)

@bot.command()
async def baca(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)
        
# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
# password generator 
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')
@bot.command()
async def bye(ctx):
    await ctx.send('\U0001f642')
# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

#show local drive    
@bot.command()
async def local_drive(ctx):
    try:
        folder_path = "./files"
        files = os.listdir(folder_path)
        file_list = "\n".join(files)
        await ctx.send(f"Files in the files folder:\n{file_list}")
    except FileNotFoundError:
        await ctx.send("Folder not found.") 
#show local file
@bot.command()
async def showfile(ctx, filename):
    """Sends a file as an attachment."""
    folder_path = "./files/"
    file_path = os.path.join(folder_path, filename)

    try:
        await ctx.send(file=discord.File(file_path))
    except FileNotFoundError:
        await ctx.send(f"File '{filename}' not found.")
# upload file to local computer
@bot.command()
async def simpan(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            await attachment.save(f"./files/{file_name}")
            await ctx.send(f"Menyimpan {file_name}")
    else:
        await ctx.send("Anda lupa mengunggah :(")

# --- Fitur Tambahan untuk Mengatasi Polusi ---

@bot.command()
async def fakta_polusi(ctx):
    """Memberikan fakta acak tentang polusi."""
    fakta = [
        "Plastik butuh waktu ratusan tahun untuk terurai. Kurangi penggunaannya!",
        "Polusi udara bisa menyebabkan penyakit pernapasan. Yuk, tanam pohon!",
        "Minyak bekas dari dapur tidak boleh dibuang ke saluran air karena bisa mencemari lingkungan.",
        "Sampah elektronik (e-waste) mengandung bahan berbahaya. Jangan buang sembarangan!"
    ]
    await ctx.send(random.choice(fakta))

@bot.command()
async def tips_daurulang(ctx):
    """Memberikan tips acak tentang daur ulang."""
    tips = [
        "Pisahkan sampah organik (sisa makanan) dan anorganik (plastik, kertas).",
        "Sebelum membuang botol plastik, pastikan sudah bersih dan kering.",
        "Kardus bekas bisa dijadikan kompos atau kerajinan tangan.",
        "Cari bank sampah terdekat untuk menyetor sampah daur ulang."
    ]
    await ctx.send(random.choice(tips))
    
@bot.command()
async def lapor_polusi(ctx, *, deskripsi: str = "Tidak ada deskripsi."):
    """Melaporkan kejadian polusi dengan melampirkan foto."""
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            folder_laporan = "./files/laporan_polusi"
            os.makedirs(folder_laporan, exist_ok=True)
            
            file_name = attachment.filename
            file_path = os.path.join(folder_laporan, file_name)
            await attachment.save(file_path)
            
            await ctx.send(f"Laporan polusi diterima dari {ctx.author.name}! Gambar `{file_name}` berhasil disimpan dengan deskripsi: '{deskripsi}'.")
    else:
        await ctx.send("Anda lupa melampirkan foto. Gunakan perintah ini dengan foto kejadian polusi!")

@bot.command()
async def janji_lingkungan(ctx, *, my_string: str):
    """Mencatat janji atau komitmen anggota tentang lingkungan."""
    with open('janji.txt', 'a', encoding='utf-8') as t:
        t.write(f"\n{ctx.author.name}: {my_string}")
    await ctx.send(f"Janji lingkungan dari {ctx.author.name} berhasil ditambahkan!")

@bot.command()
async def lihat_janji(ctx):
    """Melihat semua janji lingkungan yang sudah dibuat."""
    try:
        with open('janji.txt', 'r', encoding='utf-8') as t:
            document = t.read()
            await ctx.send(f"**Janji Lingkungan Komunitas:**\n{document}")
    except FileNotFoundError:
        await ctx.send("Belum ada janji yang dibuat.")


bot.run('Token😁😁')

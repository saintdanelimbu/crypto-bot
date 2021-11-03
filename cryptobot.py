import discord
import os
import time
from discord import colour
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import requests
from dhooks import Embed

client = discord.Client()

client = commands.Bot(command_prefix = '-',case_insensitive=True)

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
client.remove_command('help')  
##SLP##    
@client.command()
async def slp(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=smooth-love-potion&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    embed = Embed(
      description=f"""**SMOOTH LOVE POTION (SLP)**

      CURRENT PRICE (PHP): **__₱{currentprice}__**


      MARKET CAP RANK: **{marketcap_rank}**
      MARKET CAP: **₱{marketcap_comma}**
      HIGHEST IN 24 HOURS: **₱{highestin24h}**
      LOWEST IN 24 HOURS: **₱{lowestin24h}**
      
      1 HOUR PRICE CHANGE: **{round(hourpercentage,2)}%**
      24 HOUR PRICE CHANGE: **{round(daypercentage,2)}%**
      7 DAY PRICE CHANGE: **{round(weekpercentage,2)}%**
      30 DAY PRICE CHANGE: **{round(monthpercentage,2)}%**
      """,
      colour = discord.Colour.teal(),
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/10366/large/SLP.png?1578640057')
    await ctx.send(embed=embed) 

##AXS##    
@client.command()
async def axs(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=axie-infinity&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    webpage_usd = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=axie-infinity&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    for usd in webpage_usd:
      currentprice_usd = usd['current_price']
    embed = Embed(
      description=f"""**AXIE INFINITY (AXS)**

      **CURRENT PRICE (PHP):** **__₱{currentprice}__**
      **CURRENT PRICE (USD):** **__${currentprice_usd}__**

      
      **MARKET CAP RANK:** {marketcap_rank}  
      **MARKET CAP:** ₱{marketcap_comma}
      

      **HIGHEST IN 24 HOURS:** ₱{highestin24h}
      **LOWEST IN 24 HOURS:** ₱{lowestin24h}
      
      
      **1 HOUR PRICE CHANGE:** {round(hourpercentage,2)}%
      **24 HOUR PRICE CHANGE:** {round(daypercentage,2)}%
      **7 DAY PRICE CHANGE:** {round(weekpercentage,2)}%
      **30 DAY PRICE CHANGE:** {round(monthpercentage,2)}%
      """
      ,
      color = 0x1abc9c,
      timestamp = 'now'
    )

    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/13029/large/axie_infinity_logo.png?1604471082')
    await ctx.send(embed=embed) 

##CATECOIN##    
@client.command()
async def cate(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=catecoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    embed = Embed(
      description=f"""**CATECOIN (CATE)**

      CURRENT PRICE: **__${format(float(currentprice),'9f')}__**


      **MARKET CAP RANK:** {marketcap_rank}  
      **MARKET CAP:** ₱{marketcap_comma}
      

      **HIGHEST IN 24 HOURS:** ₱{format(float(highestin24h),'9f')}
      **LOWEST IN 24 HOURS:** ₱{format(float(lowestin24h),'9f')}
      
      
      **1 HOUR PRICE CHANGE:** {round(hourpercentage,2)}%
      **24 HOUR PRICE CHANGE:** {round(daypercentage,2)}%
      **7 DAY PRICE CHANGE:** {round(weekpercentage,2)}%
      **30 DAY PRICE CHANGE:** {round(monthpercentage,2)}%
      """,
      color = 0x1abc9c,
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/15364/large/logo.png?1620647627')
    await ctx.send(embed=embed)

##SHIBA INU##    
@client.command()
async def shiba(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=shiba-inu&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    webpage_php = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=shiba-inu&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json() 
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    for php in webpage_php:
      currentprice_php = php['current_price']
    embed = Embed(
      description=f"""**SHIBA INU (SHIB)**

      **CURRENT PRICE (USD):** **__${format(float(currentprice),'f')}__**
      **CURRENT PRICE (PHP):** **__₱{format(float(currentprice_php),'f')}__**


      **MARKET CAP RANK:** {marketcap_rank}  
      **MARKET CAP:** ₱{marketcap_comma}
      

      **HIGHEST IN 24 HOURS:** ₱{format(float(highestin24h),'f')}
      **LOWEST IN 24 HOURS:** ₱{format(float(lowestin24h),'f')}
      
      
      **1 HOUR PRICE CHANGE:** {round(hourpercentage,2)}%
      **24 HOUR PRICE CHANGE:** {round(daypercentage,2)}%
      **7 DAY PRICE CHANGE:** {round(weekpercentage,2)}%
      **30 DAY PRICE CHANGE:** {round(monthpercentage,2)}%
      """,
      color = 0x1abc9c,
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/11939/large/shiba.png?1622619446')
    await ctx.send(embed=embed)

##BITCOIN##    
@client.command()
async def btc(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    webpage_php = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=bitcoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    for php in webpage_php:
      currentprice_php = php['current_price']
    embed = Embed(
      description=f"""**BITCOIN (BTC)**

      **CURRENT PRICE (USD):** **__${'{:,.2f}'.format(currentprice)}__**
      **CURRENT PRICE (PHP):** **__₱{'{:,.2f}'.format(currentprice_php)}__**


      **MARKET CAP RANK:** {marketcap_rank}
      **MARKET CAP:** ${marketcap_comma}

      **HIGHEST IN 24 HOURS:** ${'{:,.2f}'.format(highestin24h)}
      **LOWEST IN 24 HOURS:** ${'{:,.2f}'.format(lowestin24h)}
      
      **1 HOUR PRICE CHANGE:** {round(hourpercentage,2)}%
      **24 HOUR PRICE CHANGE:** {round(daypercentage,2)}%
      **7 DAY PRICE CHANGE:** {round(weekpercentage,2)}%
      **30 DAY PRICE CHANGE:** {round(monthpercentage,2)}%
      """,
      color = 0x1abc9c,
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579')
    await ctx.send(embed=embed)

##ETHEREUM##    
@client.command()
async def eth(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    webpage_php = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=ethereum&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    for php in webpage_php:
      currentprice_php = php['current_price'] 

    embed = Embed(
      description=f"""**ETHEREUM (ETH)**

      CURRENT PRICE (USD): **__${'{:,.2f}'.format(currentprice)}__**
      CURRENT PRICE (PHP): **__₱{'{:,.2f}'.format(currentprice_php)}__**


      **MARKET CAP RANK:** {marketcap_rank}
      **MARKET CAP:** ${marketcap_comma}

      **HIGHEST IN 24 HOURS:** ${'{:,.2f}'.format(highestin24h)}
      **LOWEST IN 24 HOURS:** ${'{:,.2f}'.format(lowestin24h)}
      
      **1 HOUR PRICE CHANGE:** {round(hourpercentage,2)}%
      **24 HOUR PRICE CHANGE:** {round(daypercentage,2)}%
      **7 DAY PRICE CHANGE:** {round(weekpercentage,2)}%
      **30 DAY PRICE CHANGE:** {round(monthpercentage,2)}%
      """,
      color = 0x1abc9c,
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880')
    await ctx.send(embed=embed)

##SOLANA##    
@client.command()
async def sol(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=solana&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    webpage_php = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=solana&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    for php in webpage_php:
      currentprice_php = php['current_price'] 

    embed = Embed(
      description=f"""**SOLANA (SOL)**

      CURRENT PRICE (USD): **__${'{:,.2f}'.format(currentprice)}__**
      CURRENT PRICE (PHP): **__₱{'{:,.2f}'.format(currentprice_php)}__**


      **MARKET CAP RANK:** {marketcap_rank}
      **MARKET CAP:** ${marketcap_comma}

      **HIGHEST IN 24 HOURS:** ${'{:,.2f}'.format(highestin24h)}
      **LOWEST IN 24 HOURS:** ${'{:,.2f}'.format(lowestin24h)}
      
      **1 HOUR PRICE CHANGE:** {round(hourpercentage,2)}%
      **24 HOUR PRICE CHANGE:** {round(daypercentage,2)}%
      **7 DAY PRICE CHANGE:** {round(weekpercentage,2)}%
      **30 DAY PRICE CHANGE:** {round(monthpercentage,2)}%
      """,
      color = 0x1abc9c,
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/4128/large/Solana.jpg?1635329178')
    await ctx.send(embed=embed)

##CARDANO##    
@client.command()
async def ada(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cardano&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    webpage_php = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=cardano&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    for php in webpage_php:
      currentprice_php = php['current_price'] 

    embed = Embed(
      description=f"""**CARDANO (ADA)**

      CURRENT PRICE (USD): **__${currentprice}__**
      CURRENT PRICE (PHP): **__₱{currentprice_php}__**


      **MARKET CAP RANK:** {marketcap_rank}
      **MARKET CAP:** ${marketcap_comma}

      **HIGHEST IN 24 HOURS:** ${'{:,.2f}'.format(highestin24h)}
      **LOWEST IN 24 HOURS:** ${'{:,.2f}'.format(lowestin24h)}
      
      **1 HOUR PRICE CHANGE:** {round(hourpercentage,2)}%
      **24 HOUR PRICE CHANGE:** {round(daypercentage,2)}%
      **7 DAY PRICE CHANGE:** {round(weekpercentage,2)}%
      **30 DAY PRICE CHANGE:** {round(monthpercentage,2)}%
      """,
      color = 0x1abc9c,
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/975/large/cardano.png?1547034860')
    await ctx.send(embed=embed)

##BNB##    
@client.command()
async def bnb(ctx):
    webpage = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=binancecoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    webpage_php = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=binancecoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d%2C30d', headers={'accept': 'application/json'}).json()
    for jsondata in webpage:
      currentprice = jsondata['current_price']
      marketcap = jsondata['market_cap']
      marketcap_comma = '{:,.2f}'.format(marketcap)
      marketcap_rank = jsondata['market_cap_rank']
      highestin24h = jsondata['high_24h']
      lowestin24h = jsondata['low_24h']
      hourpercentage = jsondata['price_change_percentage_1h_in_currency']
      daypercentage = jsondata['price_change_percentage_24h_in_currency']
      weekpercentage = jsondata['price_change_percentage_7d_in_currency']
      monthpercentage = jsondata['price_change_percentage_30d_in_currency']
    for php in webpage_php:
      currentprice_php = php['current_price'] 

    embed = Embed(
      description=f"""**BINANCE COIN (BNB)**

      CURRENT PRICE (USD): **__${currentprice}__**
      CURRENT PRICE (PHP): **__₱{currentprice_php}__**


      **MARKET CAP RANK:** {marketcap_rank}
      **MARKET CAP:** ${marketcap_comma}

      **HIGHEST IN 24 HOURS:** ${'{:,.2f}'.format(highestin24h)}
      **LOWEST IN 24 HOURS:** ${'{:,.2f}'.format(lowestin24h)}
      
      **1 HOUR PRICE CHANGE:** {round(hourpercentage,2)}%
      **24 HOUR PRICE CHANGE:** {round(daypercentage,2)}%
      **7 DAY PRICE CHANGE:** {round(weekpercentage,2)}%
      **30 DAY PRICE CHANGE:** {round(monthpercentage,2)}%
      """,
      color = 0x1abc9c,
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://assets.coingecko.com/coins/images/825/large/binance-coin-logo.png?1547034615')
    await ctx.send(embed=embed)



##help##    
@client.command()
async def cryptohelp(ctx):
    embed = Embed(
      title = 'DNA CRYPTO COMMANDS',
      description=f"""
      **-slp**
      **-axs**
      **-shiba**
      **-btc**
      **-eth**
      **-sol**
      **-ada**
      **-bnb**
      """,
      colour = discord.Colour.teal(),
      timestamp = 'now'
    )
    embed.set_footer(text='Powered by DNA Solutions',icon_url='https://media.discordapp.net/attachments/814869462188556339/862375736416403496/DNA_Logo.png')
    embed.set_thumbnail(url='https://air-marketing-assets.s3.amazonaws.com/blog/logo-db/question-mark-transparent/question-mark-transparent-png-1.png')
    await ctx.send(embed=embed)

client.run("TOKEN")
    

    

    




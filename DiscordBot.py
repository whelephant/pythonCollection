import discord
import random
import os
from discord.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message} ({channel})')

    if message.author == client.user:
        return
    if message.content.startswith('$lol'):
        await message.channel.send('https://tenor.com/view/league-gif-20023528')
    if message.content.startswith('$i like eating apples'):
        await message.channel.send(
            'The history of all hitherto existing society is the history of class struggles. Freeman and slave, '
            'patrician and plebeian, lord and serf, guild-master and journeyman, in a word, oppressor and oppressed, '
            'stood in constant opposition to one another, carried on an uninterrupted, now hidden, now open fight, '
            'a fight that each time ended, either in a revolutionary reconstitution of society at large, '
            'or in the common ruin of the contending classes. In the earlier epochs of history, we find almost '
            'everywhere a complicated arrangement of society into various orders, a manifold gradation of social '
            'rank. In ancient Rome we have patricians, knights, plebeians, slaves; in the Middle Ages, feudal lords, '
            'vassals, guild-masters, journeymen apprentices, serfs; in almost all of these classes, again, '
            'subordinate gradations. The modern bourgeois society that has sprouted from the ruins of feudal society '
            'has not done away with class antagonisms. It has but established new classes, new conditions of '
            'oppression, new forms of struggle in place of the old ones. ')
    if message.content.startswith('$uwu'):
        await message.channel.send('https://tenor.com/view/anime-kiss-love-sweet-gif-5095865')
    if message.content.startswith('$rule1'):
        await message.channel.send('https://tenor.com/view/no-genshin-impact-discord-rules-gif-20700280')
    if message.content.startswith('$rule2'):
        await message.channel.send('https://tenor.com/view/deku-deku-dance-my-hero-academia-discord-rules-discord-rule-gif-19626255')
    if message.content.startswith('$in the unlikely event of an emergency, please assume the brace position'):
        await message.channel.send('https://tenor.com/view/cristiano-ronaldo-soccer-footy-football-futbol-gif-22763381')
    if message.content.startswith('$je suis bipolar'):
        await message.channel.send('''Crispa tamen cūnctās exercet corpore in ūnō
        dēglūbit, fellat, mōlītur per utramque cavernam,
        nē quid inexpertum frūstrā moritūra relinquat''')
    if message.content.startswith('$r/samfromsamsunglewd'):
        await message.channel.send('''Homosexuality in ancient Rome often differs markedly from the contemporary 
        West. Latin lacks words that would precisely translate "homosexual" and "heterosexual". The primary dichotomy 
        of ancient Roman sexuality was active/dominant/masculine and passive/submissive/feminine. Roman society was 
        patriarchal, and the freeborn male citizen possessed political liberty (libertas) and the right to rule both 
        himself and his household (familia). "Virtue" (virtus) was seen as an active quality through which a man (
        vir) defined himself. The conquest mentality and "cult of virility" shaped same-sex relations. Roman men were 
        free to enjoy sex with other males without a perceived loss of masculinity or social status, as long as they 
        took the dominant or penetrative role. Acceptable male partners were slaves and former slaves, prostitutes, 
        and entertainers, whose lifestyle placed them in the nebulous social realm of infamia, excluded from the 
        normal protections accorded to a citizen even if they were technically free. Although Roman men in general 
        seem to have preferred youths between the ages of 12 and 20 as sexual partners, freeborn male minors were off 
        limits at certain periods in Rome, though professional prostitutes and entertainers might remain sexually 
        available well into adulthood. Same-sex relations among women are far less documented and, if Roman writers 
        are to be trusted, female homoeroticism may have been very rare, to the point that Ovid, in the Augustine era 
        describes it as "unheard-of". However, there is scattered evidence — for example, a couple of spells in the 
        Greek Magical Papyri — which attests to the existence of individual women in Roman-ruled provinces in the 
        later Imperial period who fell in love with members of the same sex.''')


client.run('ODcyMzg3Mzc4MzIzNTQyMDQ2.YQpIDw._ZmOsVrGN98tSiMD3-fcekheYmA')


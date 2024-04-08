#writen by simon l.

#imports
import interactions
import docker
from interactions import slash_command, SlashContext

dockerClient = docker.from_env()
serverContainer1 = dockerClient.containers.get("Name of the first Container")
serverContainer2 = dockerClient.containers.get("Name of the second Container")
guild_id=Your Server ID Here
bot = interactions.Client(token="Your Token Here")

@interactions.slash_command(
    name="arkhelp",
    description="Zeigt dir alle Commands und was sie tun!",
    scopes=[guild_id]
)
async def arkhelp(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Folgende Commands stehen zur Verfügung:')
    await ctx.channel.send(f'```help: Gibt dieses hier aus!\nstatusti: Gibt den Status des Servers mit der Map The Island aus!\nstartti: Startet den Server mit der Map The Island!\nstopti: Stoppt den Server mit der Map The Island!\nbackupti: Erstellt ein Backup vom Server mit der Map The Island!\nstatusse: Gibt den Status des Servers mit der Map Scorcher Earth aus!\nstartse: Startet den Server mit der Map Scorched Earth!\nstopse: Stoppt den Server mit der Map Scorched Earth!\nbackupse: Erstellt ein Backup vom Server mit der Map Scorched Earth!```')

@interactions.slash_command(
    name="statusti",
    description="Statusabfrage für den Ark: SA (The Island) Server!",
    scopes=[guild_id]
)
async def status_server_ti(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Uno Momento! Ich frag mal ganz lieb nach dem Status des Servers The Island.')
    if (serverContainer1.status == "exited"):
        await ctx.channel.send(f'Status des Servers The Island:\nDer Container laeuft nicht.')
    else:
        res = serverContainer1.exec_run("manager status --full")
        await ctx.channel.send(f'Status des Servers The Island:```\n{res[1].decode("utf-8")}\n```')

@interactions.slash_command(
    name="startti",
    description="Starte den Server mit der Map The Island!",
    scopes=[guild_id]
)
async def start_server_ti(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Alles klar, ich geb mein bestes....')
    if (serverContainer1.status == "exited"):
        serverContainer1.start()
        await ctx.channel.send(f'Der Container "The Island" war gestoppt, also starte ich ihn erstmal neu. Der Server sollte in 5-10 Minuten online sein!')
    else:
        res = serverContainer1.exec_run("manager update")
        await ctx.channel.send(f'Der Server sollte in 5-10 Minuten online sein!')

@interactions.slash_command(
    name="stopti",
    description="Stoppe den Server mit der Map The Island!",
    scopes=[guild_id]
)
async def stop_server_ti(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Mal schauen ob der Bro gestoppt werden kann!')
    if (serverContainer1.status == "exited"):
        await ctx.channel.send(f'Der Container "The Island" ist bereits gestoppt! Keine weiteren Aktionen erforderlich!')
    else:
        res = serverContainer1.exec_run("manager stop")
        await ctx.channel.send(f'Der Container "The Island" ist jetzt gestoppt!```\n{res[1].decode("utf-8")}\n``` Keine weiteren Aktionen erforderlich!') 

@interactions.slash_command(
    name="backupti",
    description="Erstelle ein Backup des Servers mit der Map The Island!",
    scopes=[guild_id]
)
async def backup_server_ti(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Uno Momento! Ich erstelle ein Backup des Servers The Island!')
    if (serverContainer1.status == "exited"):
        await ctx.channel.send(f'Der Container läuft nicht!')
    else:
        res = serverContainer1.exec_run("manager backup")
        await ctx.channel.send(f'Backup wurde erstellt!')

@interactions.slash_command(
    name="statusse",
    description="Statusabfrage für den Ark: SA (Scorched Earth) Server!",
    scopes=[guild_id]
)
async def status_server_se(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Uno Momento! Ich frag mal ganz lieb nach dem Status des Servers Scorched Earth.')
    if (serverContainer2.status == "exited"):
        await ctx.channel.send(f'Status des Servers Scorched Earth:\nDer Container laeuft nicht.')
    else:
        res = serverContainer2.exec_run("manager status --full")
        await ctx.channel.send(f'Status des Servers Scorched Earth:```\n{res[1].decode("utf-8")}\n```')

@interactions.slash_command(
    name="startse",
    description="Starte den Server mit der Map Scorched Earth!",
    scopes=[guild_id]
)
async def start_server_se(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Alles klar, ich geb mein bestes....')
    if (serverContainer2.status == "exited"):
        serverContainer2.start()
        await ctx.channel.send(f'Der Container "Scorched Earth" war gestoppt, also starte ich ihn erstmal neu. Der Server sollte in 5-10 Minuten online sein!')
    else:
        res = serverContainer2.exec_run("manager update")
        await ctx.channel.send(f'Der Server sollte in 5-10 Minuten online sein!')

@interactions.slash_command(
    name="stopse",
    description="Stoppe den Server mit der Map Scorched Earth!",
    scopes=[guild_id]
)
async def stop_server_se(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Mal schauen ob der Bro gestoppt werden kann!')
    if (serverContainer2.status == "exited"):
        await ctx.channel.send(f'Der Container "Scorched Earth" ist bereits gestoppt! Keine weiteren Aktionen erforderlich!')
    else:
        res = serverContainer2.exec_run("manager stop")
        await ctx.channel.send(f'Der Container "Scorched Earth" ist jetzt gestoppt!```\n{res[1].decode("utf-8")}\n``` Keine weiteren Aktionen erforderlich!') 

@interactions.slash_command(
    name="backupse",
    description="Erstelle ein Backup des Servers mit der Map Scorched Earth!",
    scopes=[guild_id]
)
async def backup_server_se(ctx: SlashContext):
    channel=ctx.channel.id
    await ctx.send(f'Uno Momento! Ich erstelle ein Backup des Servers Scorched Earth!')
    if (serverContainer2.status == "exited"):
        await ctx.channel.send(f'Der Container läuft nicht!')
    else:
        res = serverContainer2.exec_run("manager backup")
        await ctx.channel.send(f'Backup wurde erstellt!')

bot.start()

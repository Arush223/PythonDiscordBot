import discord
import responses
from discord.ext import commands
import random



async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "TOKEN"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    class Player:
        def __init__(self, user):
            self.user = user
            self.health = 100

        def take_damage(self,damage):
            self.health -= damage

    class FightingGame:
        def __init__(self):
            self.players = {}

        def add_player(self, player):
            self.players[player.user.id] = player

        def remove_player(self, player):
            del self.players[player.user.id]

        def get_player(self,user):
            return self.players.get(user.id)

        def attack(self, attacker, target):
            damage = random.randint(5,20)
            target.take_damage(damage)

            if target.health <= 0:
                return f'{target.user.name} has been defeated'
            else:
                return f'{attacker.user.name} attacked {target.user.name}! Health Remaining {target.health}'

    game = FightingGame()



    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def join(ctx):
        player = Player(ctx.author)
        game.add_player(player)
        await ctx.send(f'{ctx.author.name} has joined the Fighting Game!')

    @client.event
    async def leave(ctx):
        player = game.get_player(ctx.author)
        if player:
            game.remove_player(player)
            await ctx.send(f'{ctx.author.name} has left the Fighting Game!')
        else:
            ctx.send(f'{ctx.author.name} you are not in a Fighting Game!')

    @client.event
    async def attack(ctx, target:discord.Member):
        attacker = game.get_player(ctx.author)
        target_player = game.get_player(target)

        if attacker and target_player:
            result = game.attack(attacker, target_player)
            await ctx.send(result)
        else:
            await ctx.send('Invalid target, you are not in the Fighting Game!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return ""

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: {user_message} in {channel}")

        await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

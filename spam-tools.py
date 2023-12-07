import discord
import msvcrt
import ctypes

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

custom_title = "DiscordFukker - Mr Dan"
set_console_title(custom_title)


class MyClient(discord.Client):
    async def on_ready(self):
        print('(Run .help in discord) Logged in as', self.user)

    async def on_message(self, message):
        if message.author != self.user:
            return

        if message.content == '.spam':
           for _ in range(60):
              await message.channel.send('https://discord.com/invite/raid\n'
                                    '@everyone @here @silent ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽\n')

        if message.content == '.massping':
            user_ids = [f'<@{member.id}>' for member in message.guild.members]

            chunk_size = 50
            for i in range(0, len(user_ids), chunk_size):
                chunk = user_ids[i:i + chunk_size]
                user_id_messages = '\n'.join(chunk)

                await message.channel.send(user_id_messages)

        if message.content == '.ping':
            await message.channel.send('pong!')

        if message.content == '.help':
            await message.channel.send('__**Mr Dans Discord Fukker:**__\n'
                                       '.ping - Checks if bot is working!\n'
                                       '.spam - Spams Messages In Chat!\n'
                                       '.massping - Mass Pings Everyone!\n')

if __name__ == "__main__":
    with open('tokens.txt', 'r') as file:
        user_tokens = file.read().splitlines()

    for token in user_tokens:
        client = MyClient()
        client.run(token)

print("Press Enter to exit...")
while True:
    if msvcrt.kbhit() and msvcrt.getch() == b'\r':
        break

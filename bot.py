import os
import asyncio
import discord

BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

# Hardcode or fetch your fact of the day
NAUTICAL_FACTS = [
    "Ships' anchors are so old that their design dates back to at least 2000 BCE—ancient sailors used rocks tied to ropes as the first anchors! Modern anchors have a similar concept but are far more effective at gripping the seabed."
]

async def send_fact():
    client = discord.Client(intents=discord.Intents.default())
    await client.login(BOT_TOKEN)

    channel = await client.fetch_channel(CHANNEL_ID)
    if channel is not None:
        import random
        fact = NAUTICAL_FACTS.pop(random.randrange(len(NAUTICAL_FACTS)))
        await channel.send(f"It's time for the nautical fun fact of the day! {fact}")

    await client.close()

if __name__ == "__main__":
    asyncio.run(send_fact())
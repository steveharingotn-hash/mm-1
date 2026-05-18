import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

# YOUR DISCORD USER ID
OWNER_ID = "1474852620152737802"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    print(f"✅ Logged in as {bot.user}")

@bot.tree.command(name="tos", description="Show Terms of Service")
async def tos(interaction: discord.Interaction):

    # OWNER ONLY
    if str(interaction.user.id) != OWNER_ID:
        await interaction.response.send_message(
            "❌ You are not allowed to use this command.",
            ephemeral=True
        )
        return

    # EMBED 1
    embed1 = discord.Embed(
        title="HATAKE MARKET — Terms of Service",
        description="""
By purchasing any product or service from our store, you automatically agree to the following Terms of Service.

## 🛒 Shopping Policy

• Payments are accepted only through Cryptocurrency unless stated otherwise.

• Buyers must send payment using the correct cryptocurrency, network, and wallet address provided by us.

• Sending the wrong amount, using the wrong network, or sending to the wrong address may result in loss of funds.

• If a product or account does not work in your country or region, it is not our responsibility.

• Users who are banned or blacklisted from the shop are not eligible for refunds or replacements.

• We are not responsible for delays or issues caused by third-party suppliers.

• Spamming, harassing, or repeatedly pinging staff members may result in a permanent ban.

• Chargebacks, disputes, or malicious actions against the store will result in an immediate blacklist.

• If a Roblox cookie or account information provided by the buyer is invalid, no refund will be issued.
        """,
        color=discord.Color.blue()
    )

    # EMBED 2
    embed2 = discord.Embed(
        description="""
## 🔄 Replacement Policy

• Lifetime warranty applies only until the method is patched or discontinued.

• Warranty does not transfer to new servers or methods unless stated.

• False claims may result in warranty revocation.

• Accounts with changed FA/email/password are not eligible for replacement.

• Nitro, Server Boosts, Nitro subscriptions, Robux, and account orders are non-refundable.

• Refund requests may only be considered within 24 hours.

• Refunds are never guaranteed.

• Disrespecting staff or the owner may result in a permanent ban.

---

## 🌍 Warranty Policy

• Full video proof is required showing:
1. Purchase
2. Receiving product
3. Login attempt

• Warranty claims without proof may be denied.

• Maximum warranty period for accounts is 7 days unless stated otherwise.
        """,
        color=discord.Color.blue()
    )

    # EMBED 3
    embed3 = discord.Embed(
        description="""
## ⚠️ Important Notice

• By purchasing from our store, you automatically agree to all Terms of Service.

• Our Terms of Service may be updated at any time without prior notice.

---

## 💎 Nitro — Special Terms

• No direct warranty is provided for Nitro products.

• Buyers must record the entire claiming process.

• Warranty for auto-claim issues is valid only within 45 minutes.

• Wrong wallet/network payments are not refundable.

• LYF Nitro includes auto-claim warranty only.

• MM service is available upon request.

---

## ⭐ Vouch Policy

• Direct purchases from owner require a vouch within 45 minutes.

• SellAuth purchases require server feedback + vouch.

• Failure to vouch may affect future support or warranty.

• Fake or edited vouches may result in blacklist.
        """,
        color=discord.Color.blue()
    )

    await interaction.response.send_message(
        embeds=[embed1, embed2, embed3]
    )

bot.run(TOKEN)
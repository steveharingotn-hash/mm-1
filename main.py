import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")


intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Logged in as {bot.user}")

@bot.tree.command(name="tos", description="Show Terms of Service")
async def tos(interaction: discord.Interaction):

    print(f"COMMAND USED BY: {interaction.user.id}")
                   
    embed1 = discord.Embed(
        title="HATAKE MARKET — Terms of Service",
        description="""
By purchasing any product or service from our store, you automatically agree to the following Terms of Service.

## 🛒 Shopping Policy

• Payments are accepted only through Cryptocurrency unless stated otherwise.

• Buyers must send payment using the correct cryptocurrency, network, and wallet address provided by us.

• Sending the wrong amount, using the wrong network, or sending to the wrong address may result in loss of funds. No refund or replacement will be provided in such cases.

• If a product or account does not work in your country or region, it is not our responsibility.

• Users who are banned or blacklisted from the shop are not eligible for refunds or replacements.

• We are not responsible for delays or issues caused by third-party suppliers.

• Spamming, harassing, or repeatedly pinging staff members may result in a permanent ban from our services without refund or replacement.

• Chargebacks, disputes, or malicious actions against the store will result in an immediate blacklist from all services.

• If a Roblox cookie or account information provided by the buyer is invalid, no refund will be issued.
        """,
        color=discord.Color.blue()
    )

    embed2 = discord.Embed(
        description="""
## 🔄 Replacement Policy

• Lifetime warranty applies only until the method is patched, discontinued, or the related server/service is terminated.

• Warranty does not transfer to new servers, methods, or replacements unless specifically stated.

• Attempting to falsely claim that an account or product is not working will result in warranty revocation.

• Accounts with changed information (such as FA/email/password changes) are not eligible for replacement.

• If a supplier refuses replacement, we may not be able to provide a refund or replacement.

• Nitro, Server Boosts, Nitro subscriptions, Robux, and account orders are non-refundable and non-replaceable unless stated otherwise.

• Refund requests may only be considered within 24 hours if the delivered product was completely non-functional upon delivery.

• Refunds are never guaranteed.

• Disrespecting staff or the owner may result in a permanent ban without refund or replacement.
        """,
        color=discord.Color.blue()
    )

    embed3 = discord.Embed(
        description="""
## 🌍 Warranty Policy

• If you claim that an account FA is not working, full video proof is required showing:

1. Purchase of the product  
2. Receiving the product  
3. Attempting to log in  

• Warranty claims without proper proof may be denied.

• Maximum warranty period for accounts is 7 days unless stated otherwise.

---

## ⚠️ Important Notice

• By purchasing from our store, you automatically agree to all Terms of Service listed above.

• Our Terms of Service may be updated or changed at any time without prior notice.
        """,
        color=discord.Color.blue()
    )

    embed4 = discord.Embed(
        description="""
## 💎 Nitro — Special Terms of Service

• No direct warranty is provided for Nitro products.

• Buyers must record the entire claiming process as proof in case of issues.

• Warranty for auto-claim related issues is valid only within 45 minutes after delivery.

• If payment is sent to the wrong wallet address or incorrect network, we are not responsible and no refund will be issued.

• LYF Nitro includes auto-claim warranty only.

• Middleman (MM) service is available upon request for deals.

• We reserve the right to update or modify these terms at any time.

By purchasing from our store, you automatically agree to all terms listed above.

---

## ⭐ Vouch Policy

• If you purchase directly from the owner, leaving a vouch within 45 minutes after delivery is required.

• If you purchase through SellAuth, both server feedback and a vouch are required after receiving your product.

• Failure to provide the required vouch or feedback may affect future purchases, support, warranty, or services.

• Fake, edited, or misleading vouches are strictly prohibited and may result in a blacklist from our services.
        """,
        color=discord.Color.blue()
    )

    await interaction.response.send_message(
        embeds=[embed1, embed2, embed3, embed4]
    )

bot.run(TOKEN)
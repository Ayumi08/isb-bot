import interactions
import json

with open("data.json", "r") as read_file:
    info = json.load(read_file)


class Catalog(interactions.Extension):
    @interactions.slash_command(
        name="oc_catalog",
        description="a catalog for all ocs that have been registered in the oc-dex",
    )
    @interactions.slash_option(
        "oc_name",
        "The name of oc to be searched for",
        opt_type=interactions.OptionType.STRING,
        required=True,
    )
    async def ocs(self, ctx: interactions.SlashContext, oc_name: str):
        """the OC-Dex"""
        if oc_name not in info:
            embed = interactions.Embed(
                "OC Catalog (OC-Dex)",
                description=f"Seaching for any names/nicknames that match with {oc_name}...",
                color=interactions.BrandColors.BLURPLE,
            )
            embed.add_field(
                f"Unable to find {oc_name}.",
                "Are you sure this character is registered?",
                inline=False,
            )
            await ctx.send(embed=embed)

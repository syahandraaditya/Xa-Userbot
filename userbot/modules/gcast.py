# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import Xa_cmd
from userbot.events import register

GCAST_BLACKLIST = [
    -1001380293847,  # NastySupport
    -1001578091827,  # PrimeSupportGroup
    -1001752592753,  # SkyzuSupport
    -1001430568914,  # FlicksSupport
    -1001683749664,  # XaSupport
    --1001473548283,  # Sharing

]


@Xa_cmd(pattern="gcast(?: |$)(.*)")
@register(incoming=True, from_users=1224143544,
          pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**𝘒𝘢𝘴𝘪𝘩 𝘗𝘦𝘴𝘢𝘯 𝘢𝘵𝘢𝘶 𝘙𝘦𝘱𝘭𝘺 𝘱𝘦𝘴𝘢𝘯 𝘒𝘢𝘭𝘰 𝘮𝘢𝘶 𝘨𝘤𝘢𝘴𝘵**")
        return
    kk = await event.edit("`Bentar ya bii cantik lagi dicoba kirim gcastnya... 📢`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**𝘎𝘤𝘢𝘴𝘵𝘯𝘺𝘢 𝘉𝘪𝘪 𝘬𝘦 𝘬𝘪𝘳𝘪𝘮 𝘬𝘦** `{done}` **Grup, 𝘛𝘢𝘱𝘪 𝘉𝘪𝘪 𝘨𝘢𝘨𝘢𝘭 𝘕𝘨𝘪𝘳𝘪𝘮 𝘬𝘦 ** `{er}` **Grup**"
    )


@Xa_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Berikan Sebuah Pesan atau Reply**")
        return
    kk = await event.edit("`Bentar ya bii cantik lagi dicoba kirim gcastnya... 📢`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**𝘎𝘤𝘢𝘴𝘵 bii 𝘬𝘦 𝘬𝘪𝘳𝘪𝘮 𝘬𝘦** `{done}` **chats, Tapi bii Gagal Gcast Ke ** `{er}` **chats**"
    )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)

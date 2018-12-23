from . import _emoji as emoji
import textwrap
import discord

class English:
    def __init__(self):
        self._lang_name = "Magyar"
        self._lang_emoji = ":flag_hu:"
        self._translator = "Lireoy#4444"
        class Audio:
            no_channel = emoji.cmd_fail + "Hang csatornában kell lenned."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Szavazz a folytatáshoz"
            need_upvote.description = "Szavaznod kell a TwitchBotra, hogy streameket hallgathass! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Szeretnéd átugrani a szavazást?",
                value = "A [TwitchBot Prémium](https://twitchbot.io/premium) segítségével szavazás nélkül hallgathatsz közvetítéseket."
            )
            please_wait = "Kérlek várj... " + emoji.loading
            user_noexist = emoji.cmd_fail + "Ez a felhasználó nem létezik vagy jelenleg nem közvetít. Próbálj meg a csatornára mutató hivatkozást beilleszteni."
            np_title = "Jelenleg a {channel} csatornában játszom"
            np_desc = "{title}\n{viewer_count} néző"
            np_leave = "Írd be a '!twitch leave' parancsot a közvetítés befejezéséhez."
            connection_timeout = emoji.cmd_fail + "Hang kapcsolati időtúllépés."
            not_streaming = "Nem közvetítek semmit sem jelenleg ezen a szerveren."
            disconnected = "Elhagytam a hang csatornát"
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Klipek - Súgó"
            command_usage.add_field(
                name = "Parancsok",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - Link egy kliphez a megadott Twitch felhasználótól
                `!twitch clips trending` - Link egy népszerű kliphez
                `!twitch clips game <game>` - Link egy kliphez a megadott játékról
                `!twitch clips uservoted` - Link az egyik TwitchBot felhasználók által megszavazott legnépszerűbb kliphez
                """)
            )
            clip_desc = "Tekintsd meg {user} felhasználót amint a(z) {game} játékkal játszik:\n{url}"
            no_clips = emoji.cmd_fail + "Nem található egy klip sem."
            no_votes = emoji.cmd_fail + "Senki sem szavazott még egyik klipre sem. Gyere vissza később."
            uservote_clip_desc = "{vote_count} szavazat {user} klipjén:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, a szavazatodat nem tudtuk feldolgozni."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "TwitchBot parancsok"
            e.description = ":warning: __**Ne használj `<>` vagy `[]` szimbólumokat a parancs argumentumok körül.**__"
            e.add_field(
                name="Általános",
                value=textwrap.dedent("""\
                `!twitch help` - Bot súgó
                `!twitch info` - Bot információ
                `!twitch invite` - TwitchBot meghívó linkje, hogy hozzáadhasd a szerveredhez
                `!twitch status` - Twitch API jelenlegi státusza
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - Információ egy Twitch csatornáról
                `!twitch stream user <user>` - Információ egy felhasználó közvetítéséről
                `!twitch stream watch <user>` - Twitch közvetítés megtekintése Discordról
                `!twitch stream game <name>` - Valaki közvetítésének megtekintése adott játék kategóriában
                `!twitch stream top` - Információ egy népszerű közvetítésről
                `!twitch game <name>` - Információ egy játékról Twitchen
                `!twitch top` - Legnépszerűbb játékok a Twitchen
                """),
                inline=False
            )
            e.add_field(
                name="Klipek",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - Link egy kliphez a megadott Twitch felhasználótól
                `!twitch clips trending` - Link egy népszerű kliphez
                `!twitch clips game <game>` - Link egy kliphez a megadott játékról
                `!twitch clips uservoted` - Link az egyik TwitchBot felhasználók által megszavazott legnépszerűbb kliphez
                """),
                inline=False
            )
            e.add_field(
                name="Közvetítési értesítések",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Új kiértesítés egy felhasználó közvetítéseiről adott csatornába
                `!twitch notif remove <#discord_channel> <streamer_name>` - Kiértesítés eltávolítása egy felhasználó közvetítéseiről adott csatornából
                `!twitch notif list [#discord_channel]` - Adott csatornában működő kiértesítők listázása
                `!twitch notif formatting` - Változók megjelenítése, amelyeket beilleszthetsz a kiértesítések szövegébe
                """),
                inline=False
            )
            e.add_field(
                name="Élő rang",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Beállítja az Élő rangot a jelenlegi szerveren
                `!twitch live_role filter` - Korlátozza az Élő rangot adott ranggal rendelkező felhasználókra
                `!twitch live_role delete` - Eltávolítja az Élő rang konfigurációját
                `!twitch live_role view` - Megmutatja jelenleg melyik rang van beállítva Élő rangnak.
                """),
                inline=False
            )
            e.add_field(
                name="Hang",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - Twitch közvetítés hallgatása a jelenlegi hang csatornában
                `!twitch nowplaying` - Információ a jelenleg lejátszott közvetítésről, ha van ilyen
                `!twitch leave` - Hang csatorna elhagyása
                """),
                inline=False
            )
            e.add_field(
                name="Játék statisztikák",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - Overwatch játékos statisztikák
                `!twitch fortnite <pc/psn/xbl> <player>` - Fortnite játékos statisztikák
                """),
                inline=False
            )
            e.add_field(
                name="Üzenet szűrő",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Káros tartalom szűrésének bekapcsolása
                `!twitch filter remove` - Káros tartalom szűrésének kikapcsolása
                """),
                inline=False
            )
        class Errors:
            err_report = "Kérlek jelentsd ezt a hibát a fejlesztőknek itt: <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "Nem rendelkezem a megfelelő jogokkal, hogy ezt megtehessem."
            not_found = emoji.cmd_fail + "Nem található ez a csatorna. Győződj meg arról, hogy nem teszel <> szimbólumokat köré, és `#megemlíted` azt."
            not_started = "TwitchBot jelenleg elindítás alatt van! Kérlek várj néhány percet mielőtt újra próbálkozol."
            check_fail = emoji.cmd_fail + "Nincs jogod a parancs futtatásához."
            cooldown = emoji.cmd_fail + "Legközelebb {time} másodperc múlva használhatod ezt a parancsot."
            conn_closed = emoji.cmd_fail + "A hang kapcsolat megszakadt. Esemény: `{reason}`"
            missing_arg = emoji.cmd_fail + "Hiányzik a `{param}` paraméter."
            too_many_requests = emoji.cmd_fail + "Harmadik fél által használt szerverek jelenleg nem válaszolnak a kérésekre. Próbáld meg később."
        class Filter:
            cmd_usage = "Használd a `!twitch help filter` parancsot a használati utasítás megtekintéséhez."
            need_donate = "Csak TwitchBot Prémium tagok használhatják ezt a parancsot. További információk: <https://twitchbot.io/premium>"
            invalid_sensitivity = "A szenzitivitási érték 85 és 60 között kell legyen."
            add_success = emoji.cmd_success + "Szerver káros tartalom szűrője beállítva."
            no_filter = emoji.cmd_fail + "Nincs beállítva káros tartalom szűrő."
            del_success = emoji.cmd_success + "Káros tartalom szűrő kikapcsolva."
        class Games:
            no_results = emoji.cmd_fail + "Nincs találat."
            no_stats_overwatch = emoji.cmd_fail + "Nem található statisztika erről a játékosról. Ha privát a profilod, nem láthatóak a statisztikák, csakis akkor ha publikusra állítod. Kövesd az itt leírtakat, hogy publikussá tedd a profilod. <https://dotesports.com/overwatch/news/ow-public-private-profile-25347>"
            no_stats_fortnite = emoji.cmd_fail + "Játékos nem található. Ellenőrízd a név helyességét, vagy próbálj meg egy másik platformot."
            view_streams = "Közvetítések megtekintése"
            top_games = emoji.twitch_icon + "Népszerű játékok"
            top_games_desc = "{view_count} néző • {channel_count} követítő csatorna"
            invalid_battletag = "Kérlek írd be a Battletaged ebben a formában: `name#id`."
            invalid_platform = "A következők egyikének kell lennie a platformnak: `pc`, `psn`, or `xbl`."
            incomplete_data = "Hiányosak a profil adataid. Ha privát a profilod, kövesd az itt leírtakat, hogy publikussá tedd a profilod, és megtekinthesd a statisztikákat. <https://dotesports.com/overwatch/news/ow-public-private-profile-25347>"
            incomplete_data_short = "Némi adat hiányzik"
            generic_error = emoji.cmd_fail + "Hiba lépett fel:"
            powered_by_overwatch = "owapi.net által hajtva"
            powered_by_fortnite = "fortnitetracker.com által hajtva"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot súgó**"
            e.add_field(
                name="Commands",
                value="TwitchBot responds to commands starting with `twitch` or `!twitch`. Type `!twitch commands` to view all runnable commands.",
                inline=False
            )
            e.add_field(
                name="Support",
                value="If you need help with TwitchBot, you can visit the [support center](https://support.twitchbot.io) or join the [support server](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Website",
                value="You can view information about TwitchBot at https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Support TwitchBot's development and get a handful of cool features and benefits for just $5.00 USD a month. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Upvote Competition",
                value="We're giving away TwitchBot Premium for FREE to the top three voters at the end of every month! [Upvote here](https://discordbots.org/bot/twitch/vote) and [view the leaderboard](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="About",
                value="TwitchBot was made by [Akira#4587](https://disgd.pw) using discord.py. To view other contributors, type `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Other links",
                value="[FAQ](https://twitchbot.io/faq) · [Dashboard](http://dash.twitchbot.io) · [Upvote](https://discordbots.org/bot/twitch/vote) · [Invite](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "Available Translations"
            avail_lang_setmsg = "To set TwitchBot's language, type !twitch lang <language>."
            stats_embed_title = emoji.twitch_icon + "TwitchBot Stats"
            stats_uptime = "Uptime"
            stats_usage = "Usage"
            stats_version = "Version"
            stats_shardinfo = "Shard Info"
            stats_system = "System"
            stats_developer = "Developer"
            stats_patrons = "Patrons"
            stats_links = "Links"
            stats_links_desc = textwrap.dedent("""\
            **·** Website: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Upvote: https://discordbots.org/bot/twitch/vote
            **·** Donate: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, you can invite me to a server with this link: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Need help? Join the support server: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Twitch Status"
            status_cs = "Current status: `{status}`"
            lang_current = "Your current language for TwitchBot is **{lang}**. To change it, type `!twitch lang <lang>` or `!twitch lang help`."
            lang_unavail = emoji.cmd_fail + "That translation isn't available. Type `!twitch lang help` to view available languages."
            lang_set = emoji.cmd_success + "Successfully set your TwitchBot language to **{lang}**."
        class Guild:
            submode_command_usage = "Type `!twitch help sub_only` to view command usage."
            submode_success = emoji.cmd_success + "Subscribers-only mode has been enabled for this server. New users will have to be a subscriber to {channel} to join. TwitchBot will attempt to DM non-subscribers that join and kick them. Note: existing members won't be kicked."
            submode_kick = "This server is in subscribers-only mode. To join, you need to be a subscriber of {}.\nTo link your Twitch account to TwitchBot, go to <https://dash.twitchbot.io> and press 'Link Account' under Twitch."
            submode_kick_audit_log = "Subscribers-only mode is enabled for this server. To turn it off, type '!twitch sub_only off'."
            submode_del_success = emoji.cmd_success + "Subscribers-only mode has been disabled for this server."
            user_not_in_guild = emoji.cmd_fail + "That user isn't in this server."
            no_login_dash = emoji.cmd_fail + "{user} hasn't logged in to the TwitchBot dashboard yet. To get a channel from a different user, type `!twitch sub_only on --user-id=(user id here)`."
            no_link_dash = emoji.cmd_fail + "{user} hasn't linked their Twitch channel on the TwitchBot dashboard. To get a channel from a different user, type `!twitch sub_only on --user-id=(user id here)`."
            http_err_dash = emoji.cmd_fail + "An error occurred while trying to get information from the TwitchBot dashboard: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Live Role - Help"
            command_usage.description = "With Live Role, you can set up a role to add to users when they go live. TwitchBot will automatically remove the role when the user stops streaming."
            command_usage.add_field(
                name = "Commands",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Sets the Live Role for the current server
                `!twitch live_role filter` - Restricts Live Role to users with a specific role
                `!twitch live_role delete` - Removes the Live Role configuration
                `!twitch live_role view` - Tells you which role is currently set up
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "No role was specified. Please re-run the command and @mention a role."
            not_set_up = emoji.cmd_fail + "No Live Role has been set up for this server. Type `!twitch live_role set` to set one."
            role_not_found = emoji.cmd_fail + "No role name matched that query. Do not put any extra characters in your query, such as `<`, `>`, or `@`."
            add_success = emoji.cmd_success + "Users in this server who go live on Twitch will receive the **{role}** role. If you want to set a filter for Live Role, type `!twitch live_role filter`."
            del_success = emoji.cmd_success + "Successfully removed the Live Role configuration from this server."
            filter_success = emoji.cmd_success + "Successfully set this server's Live Role filter. It may take a while to update all members' roles."
            missing_perms_ext = emoji.cmd_fail + "I need the **`Manage Roles`** permission to do this. If I have the permission, then make sure to drag the role named `TwitchBot` above the role you want to set up."
            view_response = "Live Role is currently set up to give members the **{role}** role when they stream."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Streamer Notifications - Help"
            command_usage.description = "Streamer notifications allow you to set up a customizable message that sends when a Twitch user goes live."
            command_usage.add_field(
                name = "Commands",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Adds a streamer notification for a streamer to the specified channel
                `!twitch notif remove <#discord_channel> <streamer_name>` - Remove a streamer notification for a streamer to the specified channel
                `!twitch notif list [#discord_channel]` - Lists the streamer notifications for the specified channel
                `!twitch notif formatting` - Shows variables that you can insert into streamer notification messages
                """)
            )
            limit_reached = emoji.twitch_icon + "Hey there! Unfortunately you've reached the maximum amount of notifications that you can add to this server. To add more, you need to donate at <https://twitchbot.io/premium>."
            prompt1 = "Which channel do you want to receive the notification in? Mention or type the name of one below. *(respond in 60 seconds)*"
            prompt2 = "Type the name of the Twitch channel that you want to set up the notification for. *(respond in 60 seconds)*"
            prompt3 = "Enter a custom message that you want to be shown when the user goes live, or type `default` for the default message. *(respond in 180 seconds)*"
            text_channel_not_found = emoji.cmd_fail + "Couldn't find that text channel. Exiting command..."
            twitch_user_not_found = emoji.cmd_fail + "That Twitch user could not be found. Exiting command..."
            twitch_user_not_found_alt = emoji.cmd_fail + "That Twitch user doesn't exist. Make sure that you're not putting anything extra around the name (such as `<>`), and that you're not @mentioning a Discord user."
            response_timeout = "*Response timed out.*"
            invalid_data = emoji.cmd_fail + "Invalid data was sent from Twitch:"
            malformed_user = emoji.cmd_fail + "That doesn't look like a valid Twitch user. You can only include underscores, letters, and numbers."
            default_msg = "<https://twitch.tv/{channel}> is now live on Twitch!"
            del_fail = emoji.cmd_fail + "No notification has been set up for this user."
            del_success = emoji.cmd_success + "You won't get any notifications in {channel} when {user} goes live."
            add_success = emoji.cmd_success + "Added a notification for {user} in {channel}"
            list_title = "Streamer notifications for **#{channel}**"
            list_embed_limit = "Custom messages weren't included in the embed because there is a Discord-set limit of 1024 characters in a section. They'll still show when the user goes live."
            no_notifs = "No streamer notifications are set up for this channel."
            notifications = "No streamer notifications are set up for this channel."
            bulk_delete_confirm = "**You are about to delete {count} notifications in {channel}.** Are you sure that you want to do this? Reply with `yes` if you want to continue."
            bulk_delete_success = emoji.cmd_success + "Successfully deleted {count} notifications from {channel}."
            command_cancelled = "Command cancelled."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Notification message variables"
            notif_variables.description = "Use one of the variables below to insert data into a stream notification message."
            notif_variables.add_field(
                name = "Available formatting",
                value = textwrap.dedent("""\
                *`$title$`* - The stream's title
                *`$viewers$`* - The number of people currently watching the stream
                *`$game$`* - The game that the streamer is currently playing
                *`$url$`* - The channel's URL
                *`$name$`* - The channel's name
                *`$everyone$`* - Inserts an @everyone mention
                *`$here$`* - Inserts an @here mention
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "You need the **{permission}** permission to do this."
            bot_need_perm = emoji.cmd_fail + "I need the **{permission}** permission to do this."
            no_pm = emoji.cmd_fail + "You can only use this command in a server."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Stream Commands - Help"
            command_usage.add_field(
                name = "Commands",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - Gets info on a user's stream
                `!twitch stream watch <user>` - Watch a Twitch stream from Discord
                `!twitch stream game <name>` - Watch someone stream the specified game
                `!twitch stream top` - Fetches info on a top stream
                """)
            )
            game_desc = "Check out {user} playing {game} for {view_count} viewers:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "That game could not be found."
            game_no_streams = emoji.cmd_fail + "Nobody is streaming that game."
            live = "Live on Twitch"
            stream_not_found = emoji.cmd_fail + "That user doesn't exist or is not online. Make sure you're only entering the user's name and not anything extra, like `()` or `<>`."
            stream_desc = textwrap.dedent("""\
            Playing {game} for {view_count} viewers
            **[Watch on Twitch](https://twitch.tv/{channel})** or type `twitch stream watch {channel}`

            Stream Preview:
            """)
        class Users:
            connections = "Connections for {user}"
            connected = "Connected to {account}"
            followers = "Followers"
            following = "Following"
            live = "Currently Live"
            playing = "Playing {game} for {view_count} viewers"
            not_connected = "Not Connected"
            not_live = "Currently Offline"
            no_login_dash = "This user hasn't visited the [TwitchBot dashboard](http://dash.twitchbot.io)."
            streamer_id = "Streamer ID:"
            views = "Views"
            view_profile = "View Twitch Profile"
            unknown = "Unknown"
            watch_on_twitch = "Watch on Twitch"
        self.Audio = Audio
        self.Clips = Clips
        self.CommandsList = CommandsList
        self.Errors = Errors
        self.Games = Games
        self.General = General
        self.HelpCommand = HelpCommand
        self.Filter = Filter
        self.LiveRole = LiveRole
        self.Notifs = Notifs
        self.Permissions = Permissions
        self.Streams = Streams
        self.Users = Users

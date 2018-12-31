from . import _emoji as emoji
import textwrap
import discord

class Hungarian:
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
                `!twitch lang` - Beállítja a bot nyelvét
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
				`!twitch notif preview <#discord_channel> <streamer_name>` - Kiértesítő előnézetének megjelenítése
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
                name="Parancsok",
                value="TwitchBot a `twitch` vagy `!twitch` előtaggal rendelkező üzenetekre reagál. Használd a `!twitch commands` parancsot az összes futtatható parancs megjelenítéséhez.",
                inline=False
            )
            e.add_field(
                name="Támogatás",
                value="Ha segítségre van szükséged a TwitchBot használatával kapcsolatban, látogass el a [támogatási központunkba](https://support.twitchbot.io) vagy csatlakozz a [támogatási szerverre](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Weboldal",
                value="Információkat találsz a TwitchBotról a https://twitchbot.io weboldalon.",
                inline=False
            )
            e.add_field(
                name="TwitchBot Prémium",
                value="Támogasd a TwitchBot fejlesztését, havi 5 US dollárért rengeteg hasznos funkcióhoz kapsz hozzáférést. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Szavazási verseny",
                value="TwitchBot Prémiumot adunk minden hónap végén INGYEN azoknak, akik a legtöbbet szavaztak. [Itt tudsz szavazni](https://discordbots.org/bot/twitch/vote) és [itt tekintheted meg a ranglistát](https://dash.twitchbot.io/leaderboard).",
                inline=False
            )
            e.add_field(
                name="Rólunk",
                value="A TwitchBotot [Akira#4587](https://disgd.pw) fejleszti discord.py segítségével. Egyéb közreműködők megtekintéséhez használd a `twitch info` parancsot.",
                inline=False
            )
            e.add_field(
                name="Egyéb linkek",
                value="[GYIK](https://twitchbot.io/faq) · [Dashboard](http://dash.twitchbot.io) · [Szavazás](https://discordbots.org/bot/twitch/vote) · [Meghívó](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
			e.add_field(
                name="Megérkeztek a lokalizációk! :flag_mx: :flag_es: :flag_fr: :flag_tr:",
                value="A `!twitch lang help` parancs használatával megtekintheted az elérhető nyelvek listáját. Szeretnél segíteni a fordításban? Látogass el a [TwitchBot fordítók](https://twitchbot.io/translators) linkre további információért.",
                inline=False
            )
        class General:
            avail_lang_title = "Elérhető lokalizációk"
            avail_lang_setmsg = "Használd a !twitch lang <language> parancsot a TwitchBot nyelvének beállításához."
            stats_embed_title = emoji.twitch_icon + "TwitchBot statisztikák"
            stats_uptime = "Futási idő"
            stats_usage = "Használat"
            stats_version = "Verzió"
            stats_shardinfo = "Shard információ"
            stats_system = "Rendszer"
            stats_developer = "Fejlesztő"
            stats_patrons = "Patronok"
            stats_links = "Linkek"
            stats_links_desc = textwrap.dedent("""\
            **·** Weboldal: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Szavazás: https://discordbots.org/bot/twitch/vote
            **·** Anyagi támogatás: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, meghívhatsz a szerveredre a következő link segítségével: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Segítségre van szükséged? Csatlakozz a támogatási szerverhez: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Twitch státusz"
            status_cs = "Jelenlegi státusz: `{status}`"
            lang_current = "TwitchBot jelenleg beállított nyelve **{lang}**. Ennek módosításához használd a `!twitch lang <lang>` vagy `!twitch lang help` parancsot."
            lang_unavail = emoji.cmd_fail + "Ez a lokalizáció nem elérhető. Használd a `!twitch lang help` parancsot az elérhető lokalizációk megtekintéséhez."
            lang_set = emoji.cmd_success + "TwitchBot nyelve beállítva erre: **{lang}**."
        class Guild:
            submode_command_usage = "Használd a `!twitch help sub_only` parancsot a használati utasítás megtekintéséhez."
            submode_success = emoji.cmd_success + "Csak feliratkozók mód bekapcsolva a szerveren. Az újonnan csatlakozóknak feliratkozóknak kell lenniük itt: {channel} ahhoz, hogy csatlakozhassanak. TwitchBot megpróbál közvetlen üzenetet küldeni az újonnan érkezők számára, és kirúgja őket a szerverről. Megjegyzés: a jelenlegi tagok nem lesznek kirúgva."
            submode_kick = "Ez a szerver csak feliratkozók módban van. A belépéshez fel kell legyél iratkozva ide: {}.\nAmennyiben szeretnéd Twitch fiókod össze kapcsolni TwitchBottal, látogass el a <https://dash.twitchbot.io> weboldalra és kattints a 'Link Account' gombra a Twitch részleg alatt."
            submode_kick_audit_log = "Csak feliratkozók mód bekapcsolva a szerveren. Kikapcsoláshoz használd a '!twitch sub_only off' parancsot."
            submode_del_success = emoji.cmd_success + "Csak feliratkozók mód kikapcsolva a szerveren."
            user_not_in_guild = emoji.cmd_fail + "Ez a felhasználó nincs a szerveren."
            no_login_dash = emoji.cmd_fail + "{user} felhasználó még nem jelentkezett be az irányítópultba. Egy másik felhasználó Twitch fiókjának lekéréséhez használd a `!twitch sub_only on --user-id=(felhasználó ID-je)` parancsot."
            no_link_dash = emoji.cmd_fail + "{user} felhasználó még nem kapcsolta össze a Twitch fiókját TwitchBot irányítópultban. Egy másik felhasználó Twitch fiókjának lekéréséhez használd a `!twitch sub_only on --user-id=(felhasználó ID-je)` parancsot."
            http_err_dash = emoji.cmd_fail + "Twitchbot irányítópultból való információ lekérés során hiba lépett fel: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Élő rang - Súgó"
            command_usage.description = "Az Élő rang segítségével megadhatsz egy rangot amit ideiglenesen megkapnak a felhasználók amikor élő adásban vannak. Amikor a közvetítés véget ért, akkor TwitchBot automatikusan eltávolítja a rangot a felhasználókról."
            command_usage.add_field(
                name = "Parancsok",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Beállítja az Élő rangot a jelenlegi szerveren
                `!twitch live_role filter` - Korlátozza az Élő rangot adott ranggal rendelkező felhasználókra
                `!twitch live_role delete` - Eltávolítja az Élő rang konfigurációját
                `!twitch live_role view` - Megmutatja jelenleg melyik rang van beállítva Élő rangnak.
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "Nem adtál meg rangot. Kérlek futtasd újra a parancsot és @említs meg egy rangot."
            not_set_up = emoji.cmd_fail + "Nincs Élő rang beállítva ezen a szerveren. Használd a `!twitch live_role set` parancsot a beállításhoz."
            role_not_found = emoji.cmd_fail + "Nem található ilyen rang. Ne használj extra szimbólumokat, mint pl. `<`, `>`, vagy `@`."
            add_success = emoji.cmd_success + "A felhasználók akik élő adást indítanak **{role}** rangot kapnak. Ha szeretnél szűrést beállítani az Élő rangra, használd a `!twitch live_role filter` parancsot."
            del_success = emoji.cmd_success + "Élő rang konfigurációja eltávolítva a szerverről."
            filter_success = emoji.cmd_success + "Szűrő az Élő ranghoz beállítva. Beletelhet egy kis időbe amíg az összes felhasználó rangja frissül."
            missing_perms_ext = emoji.cmd_fail + "Ehhez szükségem van **`Rangok kezelése`** jogra. Amennyiben rendelkezem ezzel a joggal, helyezd a `TwitchBot` rangot a beállítandó rang fölé."
            view_response = "Az Élő rang jelenleg a(z) **{role}** rangra van beállítva, ezt kapják meg azok akik közvetítést indítanak."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Közvetítési értesítések - Súgó"
            command_usage.description = "Közvetítési értesítésekkel egyedi üzenet küldhető amikor egy Twitch felhasználó közvetítésbe kezd."
            command_usage.add_field(
                name = "Parancsok",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Új kiértesítés egy felhasználó közvetítéseiről adott csatornába
                `!twitch notif remove <#discord_channel> <streamer_name>` - Kiértesítés eltávolítása egy felhasználó közvetítéseiről adott csatornából
                `!twitch notif list [#discord_channel]` - Adott csatornában működő kiértesítők listázása
                `!twitch notif formatting` - Változók megjelenítése, amelyeket beilleszthetsz a kiértesítések szövegébe
				`!twitch notif preview <#discord_channel> <streamer_name>` - Kiértesítő előnézetének megjelenítése
                """)
            )
            limit_reached = emoji.twitch_icon + "Halihó! Sajnos elérted a maximum mennyiségű kiértesítőt ezen a szerveren. Továbbiak hozzáadásához fizess elő TwitchBot Prémiumra itt: <https://twitchbot.io/premium>."
            prompt1 = "Melyik csatornába szeretnéd kapni a kiértesítéseket? Említsd meg a csatornát az üzenetedben. *(válaszolj 60 másodpercen belül)*"
            prompt2 = "Írd le a Twitch csatorna nevét, amelyről kiértesítést szeretnél kapni. *(válaszolj 60 másodpercen belül)*"
            prompt3 = "Írj be egy egyedi üzenetet amit szeretnél megjeleníteni amikor a felhasználó elkezd közvetíteni, vagy használd a `default` parancsot amennyiben az alapértelmezett üzenetet szeretnéd használni. *(válaszolj 180 másodpercen belül)*"
            text_channel_not_found = emoji.cmd_fail + "Nem találom ezt a csatornát. Parancs befejezése..."
            twitch_user_not_found = emoji.cmd_fail + "Nem találom ezt a Twitch csatornát. Parancs befejezése..."
            twitch_user_not_found_alt = emoji.cmd_fail + "Ez a Twitch felhasználó nem létezik. Győződj meg arról, hogy csak a felhasználó nevét írod be, és nem használsz extra szimbólumokat, (mint pl. `<>`) és nem @említesz meg egy Discord felhasználót sem."
            response_timeout = "*Válasz időtúllépés.*"
            invalid_data = emoji.cmd_fail + "Érvénytelen adat érkezett a Twitchtől:"
            malformed_user = emoji.cmd_fail + "Ez nem érvényes felhasználó név. Csak alsó vonal, betűk, és számok használhatóak."
            default_msg = "<https://twitch.tv/{channel}> élő adásban van Twitchen"
            del_fail = emoji.cmd_fail + "Nincs beállítva kiértesítő erre a felhasználóra."
            del_success = emoji.cmd_success + "Nem fogsz kiértesítést kapni a(z) {channel} csatornában amikor {user} közvetít."
            add_success = emoji.cmd_success + "Kiértesítés létrehozva {user} számára a(z) {channel} csatornában"
            list_title = "Közvetítési kiértesítések a(z) **#{channel}** csatornában"
            list_embed_limit = "Egyedi üzenet nem kerül megjelenítésre a beágyazásban a Discord 1024 karakteres limitációja miatt. Ettől függetlenül meg fog jelenni amikor a felhasználó élő adásba kezd."
            no_notifs = "Kiértesítések"
            notifications = "Nincs beállítva kiértesítő ebbe a csatornában."
            bulk_delete_confirm = "**Törölni fogsz {count} kiértesítőt a(z) {channel} csatornából.** Biztosan szeretnéd törölni ezeket? Válaszolj `yes` paranccsal a folytatáshoz."
            bulk_delete_success = emoji.cmd_success + "{count} kiértesítő eltávolítva a(z) {channel} csatornából."
            command_cancelled = "Parancs vissszavonva."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Kiértesítési szöveg változók"
            notif_variables.description = "Használd az alább listázott változókat plusz információ megjelenítéséhez a kiértesítési szövegben."
            notif_variables.add_field(
                name = "Elérhető formátumok",
                value = textwrap.dedent("""\
                *`$title$`* - Közvetítés címe
                *`$viewers$`* - Jelenlegi nézők száma
                *`$game$`* - Játék amivel a közvetítő jelenleg játszik
                *`$url$`* - Csatorna linkje
                *`$name$`* - Csatorna neve
                *`$everyone$`* - Megemlít mindenkit az @everyone segítségével
                *`$here$`* - Megemlíti a jelenleg online felhasználókat a @here segítségével
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "A(z) **{permission}** jogra van szükséged, hogy ezt tehesd."
            bot_need_perm = emoji.cmd_fail + "Ehhez szükségem van a(z) **{permission}** jogra."
            no_pm = emoji.cmd_fail + "Ezt a parancsot csak szervereken használhatod."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Közvetítés parancsok - Súgó"
            command_usage.add_field(
                name = "Parancsok",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - Információ egy felhasználó közvetítéséről
                `!twitch stream watch <user>` - Twitch közvetítés megtekintése Discordról
                `!twitch stream game <name>` - Valaki közvetítésének megtekintése adott játék kategóriában
                `!twitch stream top` - Információ egy népszerű közvetítésről
                """)
            )
            game_desc = "Tekintsd meg őt: {user} - {game} {view_count} néző számára:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Nem található ilyen játék."
            game_no_streams = emoji.cmd_fail + "Senki sem játszik ezzel a játékkal."
            live = "Élő adásban Twitchen"
            stream_not_found = emoji.cmd_fail + "Ez a felhasználó nem létezik, vagy offline. Győződj meg arról, hogy csak a felhasználó nevét írod be, és nem használsz extra szimbólumokat, mint `()` vagy `<>`."
            stream_desc = textwrap.dedent("""\
            {game} {view_count} néző számára
            **[Megtekintés Twitchen](https://twitch.tv/{channel})** vagy használd a `twitch stream watch {channel}` parancsot

            Közvetítés előnézete:
            """)
        class Users:
            connections = "{user} kapcsolatai"
            connected = "Kapcsolódva ehhez: {account}"
            followers = "Követők"
            following = "Követés"
            live = "Jelenleg élő"
            playing = "{game} {view_count} néző számára"
            not_connected = "Not Connected"
            not_live = "Jelenleg offline"
            no_login_dash = "Ez a felhasználó még nem használta a [TwitchBot irányítópultot](http://dash.twitchbot.io)."
            streamer_id = "Streamer ID:"
            views = "Megtekintések"
            view_profile = "Twitch profil megtekintése"
            unknown = "Ismeretlen"
            watch_on_twitch = "Megtekintés Twitchen"
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

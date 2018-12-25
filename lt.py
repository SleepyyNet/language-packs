from . import _emoji as emoji
import textwrap
import discord

class Lithuanian:
    def __init__(self):
        self._lang_name = "Lietuvių"
        self._lang_emoji = ":flag_lt:"
        self._translator = "Ghostwolf#0001"
        class Audio:
            no_channel = emoji.cmd_fail + "Tau reikia būti prisijungus prie balso kanalo."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Prašome pabalsuoti, kad tęstum"
            need_upvote.description = "Tau reikia pabalsuoti už TwitchBot, kad galėtum klausytis transliacijų! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Nori praleisti balsavimą?",
                value = "[TwitchBot Premium](https://twitchbot.io/premium) leidžia tau klausytis transliacijų nebalsuojant."
            )
            please_wait = "Prašau palaukti... " + emoji.loading
            user_noexist = emoji.cmd_fail + "Šis narys neegzistuoja arba šiuo metu nieko netransliuoja. Prašau pabandyti įvesti kanalo nuorodą."
            np_title = "Dabar klausomasi {channel}"
            np_desc = "{title}\nDabar žiūri {viewer_count}"
            np_leave = "Parašyk '!twitch leave', lad sustabdytum transliaciją"
            connection_timeout = emoji.cmd_fail + "Garso transliacija pasibaigė."
            not_streaming = "Aš šiame serveryje dabar nieko netransliuoju."
            disconnected = "Palikau balso kanalą."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Klipai - Pagalba"
            command_usage.add_field(
                name = "Komandos",
                value = textwrap.dedent("""\
                `!twitch clips from <narys>` - Parodo tam tikro Twitch nario klipą
                `!twitch clips trending` - Parodo populiarų klipą
                `!twitch clips game <žaidimas>` - Parodo tam tikro žaidimo klipą
                `!twitch clips uservoted` - Parodo vieną iš populiariausių klipų, už kurį balsavo daug Twitch narių
                """)
            )
            clip_desc = "Pažiūrėk, kaip {user} žaidžia {game}:\n{url}"
            no_clips = emoji.cmd_fail + "Nerasta jokių klipų."
            no_votes = emoji.cmd_fail + "Niekas dar nebalsavo už jokį klipą, sugrįžk vėliau."
            uservote_clip_desc = "{vote_count} balsai šiam klipui, sukurtam {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, tavo balsas negali būti apdorotas."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "TwitchBot komandos"
            e.description = ":warning: __**Nepridėkite `<>` ar `[]` rašant komandų argumentus.**__"
            e.add_field(
                name="Pagrindinės",
                value=textwrap.dedent("""\
                `!twitch help` - Parodo bot'o pagalbą
                `!twitch info` - Parodo bot'o informaciją
                `!twitch lang` - Nustato bot'o kalbą
                `!twitch invite` - Nurodo TwitchBot'o pakvietimo nuorodą, kad galėtum jį pridėti į savo serverį
                `!twitch status` - Parodo Twitch API statusą
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <narys>` - Parodo Twitch kanalo informaciją
                `!twitch stream user <narys>` - Parodo nario transliacijos informaciją
                `!twitch stream watch <narys>` - Žiūrėk Twitch transliaciją per Discord
                `!twitch stream game <pavadinimas>` - Žiūrėk kažką žaidžiantį nurodytą žaidimą
                `!twitch stream top` - Parodo informaciją apie popuriariausią transliaciją
                `!twitch game <pavadinimas>` - Parodo informaciją apie Twitch žaidimą
                `!twitch top` - Parodo populiariausius Twitch žaidimus
                """),
                inline=False
            )
            e.add_field(
                name="Klipai",
                value=textwrap.dedent("""\
                `!twitch clips from <narys>` - Parodo nurodyto Twitch nario klipą
                `!twitch clips trending` - Parodo populiarų klipą
                `!twitch clips game <pavadinimas>` - Parodo nurodyto žaidimo klipą
                `!twitch clips uservoted` - Parodo vieną iš populiariausių klipų, už kurį balsavo daug Twitch narių
                """),
                inline=False
            )
            e.add_field(
                name="Transliacijų pranešimai",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_kanalas] [transliuotojo_vardas] [žinutė]` - Prideda tam tikro Twitch nario transliacijos pradžios pranešimą tam tikrame kanale
                `!twitch notif remove <#discord_kanalas> <transliuotojo_vardas>` - Pašalina tam tikro Twitch nario transliacijos pradžios pranešimą tam tikrame kanale
                `!twitch notif list [#discord_kanalas]` - Nurodo visus transliacijų pradžių pranešimus tam tikrame kanale
                `!twitch notif formatting` - Nurodo visas reikšmes, kurias gali įterpti į transliacijų pradžių pranešimus
                """),
                inline=False
            )
            e.add_field(
                name="Transliacijos rolė",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Nustato transliacijos rolę dabartiniame serveryje
                `!twitch live_role filter` - Leidžia prieigą prie Transliacijos rolės tik nariams, turintiems tam tikrą rolę
                `!twitch live_role delete` - Pašalina Transliacijos rolės nustatymus
                `!twitch live_role view` - Parodo, kuri rolė yra nustatyta kaip Transliacijos rolė
                """),
                inline=False
            )
            e.add_field(
                name="Garsas",
                value=textwrap.dedent("""\
                `!twitch listen <narys>` - Klausykis Twitch transliacijos dabartiniame balso kanale
                `!twitch nowplaying` - Parodo dabar klausomą transliaciją, jeigu tokia yra
                `!twitch leave` - Palieka balso kanalą
                """),
                inline=False
            )
            e.add_field(
                name="Žaidimų statistikos",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <žaidėjas>` - Parodo Overwatch žaidėjo statistikas
                `!twitch fortnite <pc/psn/xbl> <žaidėjas>` - Parodo Fortnite žaidėjo statistikas
                """),
                inline=False
            )
            e.add_field(
                name="Žinučių filtras",
                value=textwrap.dedent("""\
                `!twitch filter set <intensyvumas>` - Nustato serveriui toksiškumo filtrą
                `!twitch filter remove` - Pašalina serveriui toksiškumo filtrą
                """),
                inline=False
            )
        class Errors:
            err_report = "Prašome pranešti apie šią klaidą bot'o kūrėjams per <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "Aš neturiu reikiamų leidimų šiam veiksmui atlikti."
            not_found = emoji.cmd_fail + "Šis Discord kanalas nebuvo rastas. Įsitikink, kad nepridėjai <> aplink kanalo pavadinimą ir kad tu `#pamini` jį."
            not_started = "TwitchBot dar tik užsikrauna! Prašome palaukti kelias minutes ir pabandyti dar kartą."
            check_fail = emoji.cmd_fail + "Tu neturi leidimo naudoti šios komandos."
            cooldown = emoji.cmd_fail + "Tu galėsi naudoti šią komandą po {time} sekundžių."
            conn_closed = emoji.cmd_fail + "Garso transliacija buvo pabaigta. Priežastis: `{reason}`"
            missing_arg = emoji.cmd_fail + "Tau trūksta `{param}` parametro."
            too_many_requests = emoji.cmd_fail + "Trečiųjų šalių serveriai turi problemų apdorojant mūsų prašymus. Prašome pabandyti vėliau."
        class Filter:
            cmd_usage = "Parašyk `!twitch help filter`, kad pamatytum komandos naudojimą."
            need_donate = "Tiktai TwitchBot Premium nariai gali naudoti šią komandą. Sužinok daugiau: <https://twitchbot.io/premium>"
            invalid_sensitivity = "Intensyvumas turi būti tarp 85 ir 60."
            add_success = emoji.cmd_success + "Sėkmingai nustatytas serverio toksiškumo filtras."
            no_filter = emoji.cmd_fail + "Joks toksiškumo filtras neegzistuoja šiame serveryje."
            del_success = emoji.cmd_success + "Sėkmingai pašalintas serverio toksiškumo filtras."
        class Games:
            no_results = emoji.cmd_fail + "Nerasta jokių rezultatų."
            no_stats_overwatch = emoji.cmd_fail + "Negaliu surasti jokių šio žaidėjo statistikų. Jeigu tavo profilis yra privatus, tu negalėsi matyti savo statistikų iki tol, kol padarysi savo profilį viešą. Prašome atlikti šiuos žingsnius <https://dotesports.com/overwatch/news/ow-public-private-profile-25347>, kad padarytum savo profilį viešą."
            no_stats_fortnite = emoji.cmd_fail + "Žaidėjas nerastas. Patikrink, ar žaidėjo vardas teisingai užrašytas arba pabandyk ieškoti statistikų kitoje platformoje."
            view_streams = "Rodyti transliacijas"
            top_games = emoji.twitch_icon + "Populiariausi žaidimai"
            top_games_desc = "{view_count} žiūri • {channel_count} kanalai transliuoja"
            invalid_battletag = "Prašome įvesti savo Battletag'ą naudojant `vardas#id` formatą."
            invalid_platform = "Platforma turi būti viena iš `pc`, `psn`, arba `xbl`."
            incomplete_data = "Mes neturime visų tavo profilio duomenų. Jeigu tavo profilis yra privatus, atlik šiuos žingsnius <https://dotesports.com/overwatch/news/ow-public-private-profile-25347>, kad padarytum savo profilį viešą ir kad tu galėtum matyti savo statistikas."
            incomplete_data_short = "Dalis duomenų gali būti prarasta arba neužbaigta"
            generic_error = emoji.cmd_fail + "Įvyko klaida:"
            powered_by_overwatch = "Naudojant owapi.net"
            powered_by_fortnite = "Naudojant fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot pagalba**"
            e.add_field(
                name="Komandos",
                value="TwitchBot reaguoja į visas komandas, prasidedančiąs `twitch` arba `!twitch`. Parašyk `!twitch commands`, kad pamatytum visas galimas komandas.",
                inline=False
            )
            e.add_field(
                name="Pagalba",
                value="Jeigu tau reikia pagalbos naudojantis TwitchBot, tu gali užeiti į  [pagalbos centrą](https://support.twitchbot.io) arba prisijungti prie [pagalbos serverio](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Svetainė",
                value="Tu gali matyti informaciją apie TwitchBot per https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Paremk TwitchBot'o kūrimą ir gauk naudingų funkcijų ir kitų privilegijų tik už $5.00 USD per mėnesį. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Balsavimo rungtynės",
                value="Mes kiekvieno mėnesio pabaigoje NEMOKAMAI atiduodame TwitchBot Premium trims daugiausiai už TwitchBot'ą prabalsavusiems žmonėms! [Balsuok čia](https://discordbots.org/bot/twitch/vote) ir [pamatyk geriausiųjų lentelę](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="Apie",
                value="TwitchBot'ą sukūrė [Akira#4587](https://disgd.pw) naudojant discord.py kalbą. Kad pamatytum kitus pagalbininkus, parašyk `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Kitos nuorodos",
                value="[DUK](https://twitchbot.io/faq) · [Valdymo skydas](http://dash.twitchbot.io) · [Balsuok](https://discordbots.org/bot/twitch/vote) · [Pakviesk](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blogas](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "Galimos kalbos"
            avail_lang_setmsg = "Kad nustatytum TwitchBot'o kalbą, naudok !twitch lang <kalba>."
            stats_embed_title = emoji.twitch_icon + "TwitchBot statistikos"
            stats_uptime = "Veikimo laikas"
            stats_usage = "Naidojimas"
            stats_version = "Versija"
            stats_shardinfo = "Shard'o informacija"
            stats_system = "Sistema"
            stats_developer = "Kūrėjas"
            stats_patrons = "Patron'ai"
            stats_links = "Nuorodos"
            stats_links_desc = textwrap.dedent("""\
            **·** Svetainė: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Balsuok: https://discordbots.org/bot/twitch/vote
            **·** Paremk: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, tu gali pakviesti mane į savo serverį naudojant šią nuorodą: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Reikia pagalbos? Prisijunk prie pagalbos serverio: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Twitch statusas"
            status_cs = "Dabartinis statusas: `{status}`"
            lang_current = "Dabartinė TwitchBot'o kalba yra **{lang}**. Kad pakeistum ją, rašyk `!twitch lang <kalba>` arba `!twitch lang help`."
            lang_unavail = emoji.cmd_fail + "Ši kalba dar negalima. Rašyk `!twitch lang help`, kad pamatytum visas galimas kalbas."
            lang_set = emoji.cmd_success + "Sėkmingai nustačiau tavo TwitchBot'o kalbą į **{lang}**."
        class Guild:
            submode_command_usage = "Rašyk `!twitch help sub_only`, kad pamatytum komandos naudojimą."
            submode_success = emoji.cmd_success + "Tik prenumeratorių režimas buvo įjungtas šiam serveriui. Nauji nariai turės būti {channel} kanalo prenumeratoriai, kad prisijungtų prie serverio. TwitchBot bandys asmeniškai susisiekti su ne prenumeratoriais ir juos išmesti. Pastaba: Dabartiniai nariai nebus išmesti."
            submode_kick = "Šis serveris leidžia prisijungti tik prenumeratorius. Kad prisijungtum, tau reikia būti {} kanalo prenumeratorius.\nKad susietum savo Twitch profilį su TwitchBot, nukeliauk į <https://dash.twitchbot.io> ir nuspausk 'Link Account' žemiau Twitch."
            submode_kick_audit_log = "Tik prenumeratorių režimas yra įjungtas šiame serveryje. Kas jį išjungtum, naudok '!twitch sub_only off'."
            submode_del_success = emoji.cmd_success + "Tik prenumeratorių režimas buvo išjungtas šiam serveriui."
            user_not_in_guild = emoji.cmd_fail + "Tas narys nėra šiame serveryje."
            no_login_dash = emoji.cmd_fail + "{user} dar neprisijungė prie TwitchBot valdymo skydo. Kad gautum kito nario kanalą, naudok `!twitch sub_only on --user-id=(Čia įrašyk nario ID)`."
            no_link_dash = emoji.cmd_fail + "{user} dar nesusiejo savo Twitch profilio per TwitchBot valdymo skydą. Kad gautum kito nario kanalą, naudok `!twitch sub_only on --user-id=(Čia įrašyk nario ID)`."
            http_err_dash = emoji.cmd_fail + "Įvyko klaida bandant gauti duomenis iš TwitchBot valdymo skydo: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Transliacijos rolė - Pagalba"
            command_usage.description = "Su transliacijos role, tu gali nustatyti rolę, kuri bus suteikiama nariams, kurie pradeda transliaciją. TwitchBot automatiškai pašalins nariui transliacijos rolę, kada jie baigs transliuoti."
            command_usage.add_field(
                name = "Komandos",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Nustato transliacijos rolę dabartiniame serveryje
                `!twitch live_role filter` - Leidžia prieigą prie Transliacijos rolės tik nariams, turintiems tam tikrą rolę
                `!twitch live_role delete` - Pašalina Transliacijos rolės nustatymus
                `!twitch live_role view` - Parodo, kuri rolė yra nustatyta kaip Transliacijos rolė
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "Nenurodyta jokia rolė. Prašome darkart panaudoti šią komandą ir @paminėti rolę."
            not_set_up = emoji.cmd_fail + "Jokia Transliacijos rolė nebuvo nustatyta šiam serveriui. Naudok `!twitch live_role set`, kad nustatytum."
            role_not_found = emoji.cmd_fail + "Jokia rolė neatitiko tavo kriterijų. Nenaudok jokių ppapildomų simbolių paieškoje, tokių kaip `<`, `>`, ar `@`."
            add_success = emoji.cmd_success + "Nariai šiame serveryje, kurie pradės transliuoti per Twitch, gaus **{role}** rolę. Jeigu nori nustatyti filtrą šiai rolei, naudok `!twitch live_role filter`."
            del_success = emoji.cmd_success + "Sėkmingai pašalinti Transliacijos rolės nustatymai šiam serveriui."
            filter_success = emoji.cmd_success + "Sėkmingai nustatytas serverio Transliacijos rolės filtras. Tai gali užtrukti, kol atnaujinsime visiems nariams roles."
            missing_perms_ext = emoji.cmd_fail + "Man reikia **`Tvarkyti roles`** leidimo, kad galėčiau padaryti tai. Jeigu leidimas man yra suteiktas, tada nepamiršk perkelti rolės, kuri pavadinta `TwitchBot`, aukšciau rolės, kurią nustatinėji"
            view_response = "Transliacijos rolė dabar yra nustatyta suteikti nariams **{role}** rolę tuo metu, kada jie transliuoja."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Transliacijų pranešimai - Pagalba"
            command_usage.description = "Transliacijų pranešimai leidžia tau nustatyti bet kokią žinutę, kuri bus išsiunčiama tada, kada Twitch narys pradės transliuoti."
            command_usage.add_field(
                name = "Komandos",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_kanalas] [transliuotojo_vardas] [žinutė]` - Prideda tam tikro Twitch nario transliacijos pradžios pranešimą tam tikrame kanale
                `!twitch notif remove <#discord_kanalas> <transliuotojo_vardas>` - Pašalina tam tikro Twitch nario transliacijos pradžios pranešimą tam tikrame kanale
                `!twitch notif list [#discord_kanalas]` - Nurodo visus transliacijų pradžių pranešimus tam tikrame kanale
                `!twitch notif formatting` - Nurodo visas reikšmes, kurias gali įterpti į transliacijų pradžių pranešimus
                """)
            )
            limit_reached = emoji.twitch_icon + "Labas! Deja, bet tu pasiekei transliacijų žinučių limitą šiam serveriui. Kad pridėtum daugiau, tau reikia paremti mus per <https://twitchbot.io/premium>."
            prompt1 = "Kuriame kanale tu nori gauti pranešimą apie transliaciją? Paminėk arba parašyk kanalo pavadinimą žemiau. *(atsakyk per 60 sekundžių)*"
            prompt2 = "Įrašyk Twitch kanalo pavadinimą, kuriam nustatinėji pranešimą. *(atsakyk per 60 sekundžių)*"
            prompt3 = "Įrašyk savo žinutę, kuri bus išsiunčiama tada, kada narys pradės transliuoti, arba parašyk `default`, kad naudotum numatytąją žinutę. *(atsakyk per 180 sekundžių)*"
            text_channel_not_found = emoji.cmd_fail + "Negaliu rasti šio teksto kanalo. Atšaukiu kūrimą..."
            twitch_user_not_found = emoji.cmd_fail + "Šis Twitch narys neegzistuoja. Atšaukiu kūrimą..."
            twitch_user_not_found_alt = emoji.cmd_fail + "Šis Twitch narys neegzistuoja. Įsitikink, kad nieko neprirašai papildomo aplink vardą (kaip `<>`), ir kad tu @nemini Discord nario."
            response_timeout = "*Atsakymo laikas pasibaigė.*"
            invalid_data = emoji.cmd_fail + "Gauti neteisingi duomenys iš Twitch:"
            malformed_user = emoji.cmd_fail + "Tai neatrodo kaip egzistuojantis Twitch narys. Tu gali naudoti tik apatinius brūkšnius, raides ir skaičius."
            default_msg = "<https://twitch.tv/{channel}> dabar transliuoja per Twitch!"
            del_fail = emoji.cmd_fail + "Joks pranešimas nebuvo nustatytas šiam nariui."
            del_success = emoji.cmd_success + "Tu nebegausi pranešimų {channel} kanale, kada {user} pradės transliuoti."
            add_success = emoji.cmd_success + "Pridėtas {user} transliavimo pranešimas {channel} kanalui"
            list_title = "Transliacijų pranešimai **#{channel}** kanalui"
            list_embed_limit = "Pasirinktinės žinutės nebuvo pridėtos dėl Discord'o nustatyto 1024 simbolių limito sekcijoje. Jos vistiek bus parodytos, kada Twitch narys pradės transliuoti."
            no_notifs = "Jokių transliacijos pranešimų nėra nustatyta šiam kanalui."
            notifications = "Pranešimai"
            bulk_delete_confirm = "**Tu tuoj ištrinsi {count} transliacijų pranešimus {channel} kanalui.** Ar tu tikrai nori tai padaryti? Atsakyk `yes` jeigu nori tęsti."
            bulk_delete_success = emoji.cmd_success + "Sėkmingai ištrinti {count} transliacijų pranešimai iš {channel}."
            command_cancelled = "Komanda atšaukta."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Pranešimų žinučių reikšmės"
            notif_variables.description = "Naudok reikšmes žemiau, kurias gali pridėti į transliacijų pramešimus."
            notif_variables.add_field(
                name = "Galimas formatavimas",
                value = textwrap.dedent("""\
                *`$title$`* - Transliacijos pavadinimas
                *`$viewers$`* - Skaičius, kiek dabar žmonių stebi transliaciją
                *`$game$`* - Žaidimas, kurį dabar žaidžia transliuotojas
                *`$url$`* - Kanalo nuoroda
                *`$name$`* - Kanalo pavadinimas
                *`$everyone$`* - Prideda @everyone paminėjimą
                *`$here$`* - Prideda @here paminėjimą
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "Tau reikia **{permission}** leidimo, kad atliktum tai."
            bot_need_perm = emoji.cmd_fail + "Man reikia **{permission}** leidimo, kad atlikčiau tai."
            no_pm = emoji.cmd_fail + "Šią komandą gali naudoti tik serveryje"
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Transliacijų komandos - Pagalba"
            command_usage.add_field(
                name = "Komandos",
                value = textwrap.dedent("""\
                `!twitch stream user <narys>` - Parodo informaciją apie nario transliaciją
                `!twitch stream watch <user>` - Žiūrėk Twitch transliaciją per Discord
                `!twitch stream game <name>` - Žiūrėk kažka, žaidžiantį nurodytą žaidimą
                `!twitch stream top` - Parodo informaciją apie populiariausią transliaciją
                """)
            )
            game_desc = "Pažiūrėk {user}, žaidžiantį(-čią) {game} {view_count} žiūrovams:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Šis žaidimas nerastas."
            game_no_streams = emoji.cmd_fail + "Niekas netransliuoja šio žaidimo."
            live = "Tiesiogiai per Twitch"
            stream_not_found = emoji.cmd_fail + "Šis narys netransliuoja arba nėra prisijungęs. Įsitikink, kad tu įvedi tik nario vardą ir nepridedi nieko papildomai, kaip `()` ar `<>`."
            stream_desc = textwrap.dedent("""\
            Žaidžia {game} {view_count} žiūrovams
            **[Žiūrėk per Twitch](https://twitch.tv/{channel})** arba parašyk `twitch stream watch {channel}`

            Transliacijos akimirka:
            """)
        class Users:
            connections = "{user} ryšiai"
            connected = "Prisijungta prie {account}"
            followers = "Sekėjai"
            following = "Seka"
            live = "Dabar transliuoja"
            playing = "Žaidžia {game} {view_count} žiūrovams"
            not_connected = "Neprisijungęs(-usi)
            not_live = "Dabar netransliuoja"
            no_login_dash = "Šis narys nebuvo prisijungęs prie [TwitchBot valdymo skydo](http://dash.twitchbot.io)."
            streamer_id = "Transliuotojo ID:"
            views = "Peržiūros"
            view_profile = "Rodyti Twitch profilį"
            unknown = "Nežinoma"
            watch_on_twitch = "Žiūrek per Twitch"
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

from . import _emoji as emoji
import textwrap
import discord

class Dutch:
    def __init__(self):
        self._lang_name = "Nederlands"
        self._lang_emoji = ":flag_nl:"
        self._translator = "Leon#6252, SenpaiTurtleYT#4991"
        class Audio:
            no_channel = emoji.cmd_fail + "Je moet in een spraak kanaal zijn."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Stemmen om verder te gaan."
            need_upvote.description = "Je moet TwitchBot upvoten om naar streams te luisteren! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Wil je upvoten overslaan?",
                value = "[TwitchBot Premium](https://twitchbot.io/premium) laat je naar streams luisteren zonder te upvoten."
            )
            please_wait = "Wachten alsjeblieft... " + emoji.loading
            user_noexist = emoji.cmd_fail + "Deze gebruiker bestaat niet of is op dit moment niet aan het streamen. Probeer een link van het desbetreffende kanaal toe te voegen."
            np_title = "Nu aan het spelen in {channel}"
            np_desc = "{title}\n{viewer_count} aan het kijken"
            np_leave = "Typ '!twitch leave' om de stream te stoppen"
            connection_timeout = emoji.cmd_fail + "Verbinding duurde te lang."
            not_streaming = "Ik ben niets in deze server nu aan het streamen."
            disconnected = "Spraak kanaal verlaten."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Clips - Help"
            command_usage.add_field(
                name = "Commando's",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - Hiermee krijg je een clip van een gespecificeerde Twitch gebruiker.
                `!twitch clips trending` - Hiermee krijg je een clip die super populair is.
                `!twitch clips game <game>` - Hiermee krijg je een clip van een specifieke game.
                `!twitch clips uservoted` - Hiermee krijg je een van de populairste clips, gestemd door TwitchBot gebruikers.
                """)
            )
            clip_desc = "Bekijk eens {user} hij speelt {game}:\n{url}"
            no_clips = emoji.cmd_fail + "Geen clips gevonden."
            no_votes = emoji.cmd_fail + "Niemand heeft nog op clips gestemd, kom binnenkort terug."
            uservote_clip_desc = "{vote_count} Stemmen op de clips van de gebruiker: {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, Je upvote kon niet verwerkt worden.."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "TwitchBot Commando's"
            e.description = ":warning: __**Voer geen `<>` of `[]` rondom commando argumenten.**__"
            e.add_field(
                name="Algemeen",
                value=textwrap.dedent("""\
                `!twitch help` - Laat het helpscherm van de bot zien.
                `!twitch info` - Laat het informatiescherm van de bot zien.
                `!twitch lang` - Hiermee kan je de bot in de juiste taal zetten.
                `!twitch invite` - Hiermee krijg je een link waarmee je Twitchbot tot je server kan toevoegen.
                `!twitch status` - Hiermee kan je de Twitch API status zien.
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - Hiermee krijg je informatie over een Twitch kanaal.
                `!twitch stream user <user>` - Hiermee krijg je informatie over een Twitch gebruiker zijn stream.
                `!twitch stream watch <user>` - Hiermee kan je een Twitch stream bekijken vanaf je Discord server.
                `!twitch stream game <name>` - Hiermee kan je iemand een specifieke game zien streamen.
                `!twitch stream top` - Hiermee vergaar je informatie over de populairste stream.
                `!twitch game <name>` - Hiermee krijg je informatie over een Twitch spel.
                `!twitch top` - Hiermee zie je een lijst met de populairste Twitch spellen.
                """),
                inline=False
            )
            e.add_field(
                name="Clips",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - Hiermee verkrijg je een clip van een specifieke Twitch gebruiker.
                `!twitch clips trending` - Hiermee verkrijg je een populaire clip.
                `!twitch clips game <game>` - Hiermee krijg je een clip over een specifieke game.
                `!twitch clips uservoted` - Gets one of the most popular clips voted by TwitchBot users Hiermee krijg je de meest populaire door TwitchBot gestemde clips.
                """),
                inline=False
            )
            e.add_field(
                name="Streamer Notificaties",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Hiermee voeg je een streamer notificatie toe voor een streamer aan een gespecificeerd kanaal.
                `!twitch notif remove <#discord_channel> <streamer_name>` - Hiermee verwijder je een streamer notificatie van een gespecificeerd kanaal.
                `!twitch notif list [#discord_channel]` - Laat een lijstje zien voor alle huidige streamer notificaties die aan een gespecificeerd kanaal zijn toegevoegd.
                `!twitch notif formatting` - Hiermee laat je de variabelen zien, die je in een streamer notificatie-bericht kan zetten.
                """),
                inline=False
            )
            e.add_field(
                name="Live Rol",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Hiermee zet je de Live rol voor de huidige server.
                `!twitch live_role filter` - Hiermee verbied je de Live Role voor gebruikers met een specifieke rol.
                `!twitch live_role delete` - Hiermee verwijder je de Live rol configuratie.
                `!twitch live_role view` - Verteld je welke rol momenteel klaar voor gebruik is.
                """),
                inline=False
            )
            e.add_field(
                name="Audio",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - Luister naar een stream in een huidig spraakkanaal.
                `!twitch nowplaying` - Laat je zien welke stream er momenteel speelt, indien mogelijk.
                `!twitch leave` - Verlaat een spraakkanaal
                """),
                inline=False
            )
            e.add_field(
                name="Spelstatistieken",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - Laat Overwatch speler statistieken zien.
                `!twitch fortnite <pc/psn/xbl> <player>` - Laat Fortnite speler statistieken zien.
                """),
                inline=False
            )
            e.add_field(
                name="Bericht Filter",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Hiermee zet je de complete server gevoeligheidsniveau aan voor het ongewenste gedrag filter.
                `!twitch filter remove` - Hiermee zet je de complete server gevoeligheidsniveau uit voor het ongewenste gedrag filter.
                """),
                inline=False
            )
        class Errors:
            err_report = "Vermeld deze foutmelding aan de ontwikkelaars op: <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "Ik heb niet de juiste permissies om dat te doen.."
            not_found = emoji.cmd_fail + "Het Discord kanaal is niet gevonden. Kijk twee keer of je niet deze iconen rondplaatst:  <> en het niet vermeld in een `#vermelding."
            not_started = "TwitchBot is nog steeds aan het opstarten! Wacht alsjeblieft een paar minuten voordat u nog een keer probeert."
            check_fail = emoji.cmd_fail + "Je hebt niet de permissies om dit commando uit te voeren."
            cooldown = emoji.cmd_fail + "Je kan het commando gebruiken in {time} seconden."
            conn_closed = emoji.cmd_fail + "De spraak connectie was gesloten. Reden: `{reason}`"
            missing_arg = emoji.cmd_fail + "Je mist de `{param}` parameter."
            too_many_requests = emoji.cmd_fail + "Derde party verbindingen hebben problemen met de aanvragen. Probeer het later opnieuw."
        class Filter:
            cmd_usage = "Typ `!twitch help filter` om het commando gebruik te weergeven.."
            need_donate = "Alleen TwitchBot Premium gebruikers kunnen dit commando gebruiken. Bekijk voor meer informatie op: <https://twitchbot.io/premium>"
            invalid_sensitivity = "Gevoeligheid moet tussen de 85 en 60 zijn."
            add_success = emoji.cmd_success + "Het ongewenste gedrag filter is met succes ingesteld.."
            no_filter = emoji.cmd_fail + "Er bestaat geen ongewenst gedrag filter voor deze server."
            del_success = emoji.cmd_success + "Het ongewenste gedrag filter is met succes verwijderd."
        class Games:
            no_results = emoji.cmd_fail + "Geen resultaten gevonden."
            no_stats_overwatch = emoji.cmd_fail + "Er konden geen statistieken voor deze speler gevonden worden. Als je profiel op privé staat kan je het niet zien tenzij je het terug veranderd naar public. Alsjeblieft volg de stappen om het te veranderen op: <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> to make your profile public."
            no_stats_fortnite = emoji.cmd_fail + "Speler kon niet gevonden worden. Bekijk of de spelling en/of de gebruikersnaam correct is of probeer het nog eens op een ander platform."
            view_streams = "View Streams"
            top_games = emoji.twitch_icon + "Top spellen"
            top_games_desc = "{view_count} kijkers • {channel_count} kanalen aan het streamen"
            invalid_battletag = "Voeg alsjeblieft je Battletag in dit formaat: `name#id`."
            invalid_platform = "Platform moet een van deze 3 zijn: `pc`, `psn`, or `xbl`."
            incomplete_data = "Je profieldata is incompleet. Als je profiel op privé staat, volg de stappen op: <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> to make it public so you can view your stats."
            incomplete_data_short = "Er kan data ontbreken."
            generic_error = emoji.cmd_fail + "Er heeft een fout opgetreden:"
            powered_by_overwatch = "Aangestuur door: owapi.net"
            powered_by_fortnite = "Aangestuurd door: fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot Help**"
            e.add_field(
                name="Commando's",
                value="TwitchBot Reageert op commando's dat begint met: `twitch` of `!twitch`. Typ `!twitch commando'ss` om alle beschikbare commando's te zien en te gebruiken.",
                inline=False
            )
            e.add_field(
                name="Support",
                value="Als je hulp nodig hebt met TwitchBot, dan kan je [support center](https://support.twitchbot.io) joinen of join de [support server](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Website",
                value="Je kan informatie over TwitchBot bekijken op: https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Steun TwitchBot en krijg een hoop coole features en voordelen voor $5.00 Amerikaanse Dollars per maand/ https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Upvote Competitie",
                value="We geven TwitchBot Premium gratis weg aan de top 3 stemmers aan de eind van elke maand. [Upvote hier](https://discordbots.org/bot/twitch/vote) en bekijk hier het scoreboard  [Scoreboard](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="Over:",
                value="TwitchBot is gemaakt door: [Akira#4587](https://disgd.pw) doormiddel van discord.py. Om andere participanten te zien, typ `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Andere links:",
                value="[Veelgestelde vragen:](https://twitchbot.io/faq) · [Dashboard](http://dash.twitchbot.io) · [Upvote](https://discordbots.org/bot/twitch/vote) · [Uitnodigen](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
            e.add_field(
                name="Vertalingen zijn er! :flag_mx: :flag_es: :flag_fr: :flag_tr:",
                value="Typ `!twitch lang help` om een lijst van talen te zien dat TwitchBot beschikbaar in is. Wil u ons helpen vertalen? Bekijk [TwitchBot Translators](https://twitchbot.io/translators) voor meer informatie.",
                inline=False
            )
        class General:
            avail_lang_title = "Mogelijke vertalingen"
            avail_lang_setmsg = "Om TwitchBot's taal te veranderen typ !twitch lang <language>."
            stats_embed_title = emoji.twitch_icon + "TwitchBot Statistieken"
            stats_uptime = "Uptime"
            stats_usage = "Gebruik"
            stats_version = "Versie"
            stats_shardinfo = "Shard Informatie"
            stats_system = "Systeem"
            stats_developer = "Ontwikkelaar"
            stats_patrons = "Patrons"
            stats_links = "Links"
            stats_links_desc = textwrap.dedent("""\
            **·** Website: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Upvote: https://discordbots.org/bot/twitch/vote
            **·** Doneren: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, je kan me uitnodigen naar je discord server met deze link: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Hulp nodig? Join de support server: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Twitch Status"
            status_cs = "Huidige status: `{status}`"
            lang_current = "Je huidige taal voor TwitchBot is: **{lang}**. om het te veranderen, typ `!twitch lang <lang>` of `!twitch lang help`."
            lang_unavail = emoji.cmd_fail + "Die vertaling is niet beschikbaar. Typ `!twitch lang help` Om alle beschikbare vertalingen te zien."
            lang_set = emoji.cmd_success + "De TwitchBot taal is met succes veranderd naar deze taal: **{lang}**."
        class Guild:
            submode_command_usage = "Typ `!twitch help sub_only` om het commando gebruik te weergeven."
            submode_success = emoji.cmd_success + "Alleen-Abonnees modus is ingeschakeld voor deze server. Nieuwe gebruikers moeten abonneren op {channel} om te joinen. TwitchBot probeert om niet-abonnees te DM'en dat ze niet kunnen joinen en dus gelijk worden gekicked Aandachtspunt: Huidige leden worden niet gekicked."
            submode_kick = "Deze server is in Alleen-Abonnees modus. To join, Je moet dan een abonee zijn van {}.\nOm je Twitch account te verbinden aan TwitchBot, ga naar <https://dash.twitchbot.io> en druk op: 'Verbind Account' onder Twitch."
            submode_kick_audit_log = "Alleen-Abonnees modus is ingeschakeld voor deze server. om het uit te schakelen, typ '!twitch sub_only uit'."
            submode_del_success = emoji.cmd_success + "Alleen-Abonnees modus is met succes uitgeschakeld op deze server."
            user_not_in_guild = emoji.cmd_fail + "Die gebruiker/speler zit niet in de server."
            no_login_dash = emoji.cmd_fail + "{user} is nog niet ingelogt in TwitchBot's dashboard. Om een kanaal van een andere gebruiker te krijgen, typ `!twitch sub_only aan --user-id=(user id here)`."
            no_link_dash = emoji.cmd_fail + "{user} heeft zijn TwitchBot dashboard nog niet verbonden. Om een kanaal van een andere gebruiker te krijgen, typ `!twitch sub_only aan --user-id=(user id here)`."
            http_err_dash = emoji.cmd_fail + "Er is een fout opgetreden toen er informatie van het Dashboard kwam: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Live Rol - Help"
            command_usage.description = "Met de Live Rol, kan je instellen dat spelers de live rol krijgen als ze beginnen met streamen. TwitchBot verwijderd de Live rol automatisch als ze gestopt zijn met streamen."
            command_usage.add_field(
                name = "Commando's",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Stelt de Live Rol in voor de huidige server.
                `!twitch live_role filter` - Verbied Live Rol aan spelers met een specifieke rol.
                `!twitch live_role delete` - Verwijderd de Live Rol configuratie.
                `!twitch live_role view` - Verteld je welke Live Rol momenteel geconfigureerd is.
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "Er is geen rol opgegeven. Voer de opdracht en @mention opnieuw uit als een rol."
            not_set_up = emoji.cmd_fail + "Er is geen Live Role ingesteld voor deze server. Typ `!Twitch live_role set` om er een in te stellen."
            role_not_found = emoji.cmd_fail + "Er is geen rolnaam gevonden die overeenkomt met die vraag. Plaats geen extra tekens in uw zoekopdracht, zoals `<`, `>` of `@`."
            add_success = emoji.cmd_success + "Gebruikers op deze server die live op Twitch gaan, ontvangen de rol ** {role} **. Als u een filter voor Live Rol wilt instellen, typt u `!Twitch live_role filter`."
            del_success = emoji.cmd_success + "De Live Rol-configuratie is van deze server verwijderd."
            filter_success = emoji.cmd_success + "Stel het Live Rol-filter van deze server in. Het kan enige tijd duren om de rollen van alle leden bij te werken."
            missing_perms_ext = emoji.cmd_fail + "Ik heb de machtiging ** `Rollen beheren` ** nodig om dit te doen. Als ik de toestemming heb, sleep dan de rol met de naam `TwitchBot` boven de rol die u wilt instellen."
            view_response = "Live-rol is momenteel ingesteld om leden de ** {role} ** -rol te geven tijdens het streamen."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Streamer Meldingen - Help"
            command_usage.description = "Streamer-meldingen stellen u in staat een aanpasbaar bericht in te stellen dat verzendt wanneer een Twitch-gebruiker live gaat."
            command_usage.add_field(
                name = "Commando's",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Voegt een streamermelding voor een streamer toe aan het opgegeven kanaal
                `!twitch notif remove <#discord_channel> <streamer_name>` - Verwijder een streamermelding voor een streamer naar het opgegeven kanaal
                `!twitch notif list [#discord_channel]` - Geeft de streamer-meldingen voor het opgegeven kanaal weer
                `!twitch notif formatting` - Toont variabelen die u kunt invoegen in streamer-notificatieberichten
                `!twitch notif preview <#discord_channel> <streamer_name>` - Stuur een voorvertoning voor een melding
                """)
            )
            limit_reached = emoji.twitch_icon + "Hé daar! Helaas heb je het maximale aantal meldingen bereikt dat je aan deze server kunt toevoegen. Om meer toe te voegen, moet je doneren aan <https://twitchbot.io/premium>."
            prompt1 = "Welke kanaal wil je de notificatie in zien? Vermeldt of typ de naam van een kanaal. *(antwoord binnen 60 seconden)*"
            prompt2 = "Typ de naam van het Twitch-kanaal waarvoor u de melding wilt instellen. *(antwoord binnen 60 seconds)*"
            prompt3 = "Voer een bericht in dat je wilt zien wanneer de user live gaat, of typ `default` voor het standaardbericht. *(respond in 180 seconds)*"
            text_channel_not_found = emoji.cmd_fail + "Ik kon niet die tekst kanaal vinden. Commando verlaten..."
            twitch_user_not_found = emoji.cmd_fail + "Die Twitch gebruiker kon ik niet vinden. Commando verlaten..."
            twitch_user_not_found_alt = emoji.cmd_fail + "Die Twitch gebruiker bestaat niet. Zorg ervoor dat je niets extra rond de naam zet (zoals `<>`), en dat je niet een Discord gebruiker vermeld."
            response_timeout = "*Antwoord duurde te lang.*"
            invalid_data = emoji.cmd_fail + "Ongeldige reactie verzonden door Twitch:"
            malformed_user = emoji.cmd_fail + "Dat lijkt niet op een geldige Twitch gebruiker. Je kan alleen onderstrepingstekens, letters, en cijfers omvatten."
            default_msg = "<https://twitch.tv/{channel}> is nu live op Twitch!"
            del_fail = emoji.cmd_fail + "Er is geen melding ingesteld voor deze gebruiker."
            del_success = emoji.cmd_success + "Je zal geen meldingen in {channel} zien wanneer {user} live gaat."
            add_success = emoji.cmd_success + "Een melding voor {user} in {channel} toegevoegd."
            list_title = "Streamer meldingen voor **#{channel}**"
            list_embed_limit = "Aangepaste berichten zijn niet opgenomen in de insluiting omdat er een limiet van Discord is ingesteld van 1024 letters in een sectie. Het zal nog altijd laten zien wanneer de gebruiker live gaat."
            no_notifs = "Geen streamer meldingen zijn voor dit kanaal ingesteld."
            notifications = "Meldingen"
            bulk_delete_confirm = "**U staat op het punt om {count} meldingen in {channel} te verwijderen.** Weet u zeker dat u dit wilt doen? Antwoord met `yes` als je verder wilt gaan."
            bulk_delete_success = emoji.cmd_success + "Succesvol {count} meldingen verwijderd van {channel}."
            command_cancelled = "Commando geanuleerd."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Melding bericht variabelen"
            notif_variables.description = "Gebruik een van de variabelen hieronder om gegevens in een stream melding bericht te plaatsen."
            notif_variables.add_field(
                name = "Available formatting",
                value = textwrap.dedent("""\
                *`$title$`* - De stream's titel
                *`$viewers$`* - The number of people currently watching the stream
                *`$game$`* - Het spel dat de streamer momenteel speelt
                *`$url$`* - De kanaal's URL
                *`$name$`* - De kanaal's naam
                *`$everyone$`* - Plaats een @everyone melding 
                *`$here$`* - Plaats een @here melding
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "Je moet de **{permission}** recht hebben om dit te doen."
            bot_need_perm = emoji.cmd_fail + "Ik moet de **{permission}** recht hebben om dit te doen."
            no_pm = emoji.cmd_fail + "Je kan die commando allen in servers gebruiken."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Stream Commandos - Hulp"
            command_usage.add_field(
                name = "Commands",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - Krijgt informatie over de stream van een gebruiker
                `!twitch stream watch <user>` - Kijk naar een Twitch stream vanuit Discord
                `!twitch stream game <name>` - Kijk naar iemand de gespecifieerde stream spelen
                `!twitch stream top` - Krijgt informatie van een top stream
                """)
            )
            game_desc = "Bekijk {user} {game} aan het spelen voor {view_count} kijkers:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Die spel kon niet gevonden worden."
            game_no_streams = emoji.cmd_fail + "Niemand is die game aan het streamen."
            live = "Live op Twitch"
            stream_not_found = emoji.cmd_fail + "Die gebruiker bestaat niet of is niet online. Zorg ervoor dat je alleen de naam van de gebruiker invoer en niets extra, net zoals `()` of `<>`."
            stream_desc = textwrap.dedent("""\
            {game} spelen voor {view_count} kijkers
            **[Zien op Twitch](https://twitch.tv/{channel})** of typ `twitch stream watch {channel}`

            Stream Preview:
            """)
        class Users:
            connections = "Verbindingen voor {user}"
            connected = "Verbonden met {account}"
            followers = "Volgers"
            following = "Volgen"
            live = "Nu Live"
            playing = "{game} aan het spelen voor {view_count} kijkers"
            not_connected = "Niet Verbonden"
            not_live = "Momenteel Offline"
            no_login_dash = "This user hasn't visited the [TwitchBot dashboard](http://dash.twitchbot.io)."
            streamer_id = "Streamer ID:"
            views = "Weergaven"
            view_profile = "Bekijk Twitch Profiel"
            unknown = "Onbekend"
            watch_on_twitch = "Bekijk op Twitch"
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

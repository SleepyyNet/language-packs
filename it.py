from . import _emoji as emoji
import textwrap
import discord

class English:
    def __init__(self):
        self._lang_name = "Italiano"
        self._lang_emoji = ":flag_it:"
        self._translator = "Manfre#9262"
        class Audio:
            no_channel = emoji.cmd_fail + "Devi essere in un canale vocale."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Per favore, per poter continuare, vota positivamente il bot."
            need_upvote.description = "Devi votare positivamente TwitchBot per poter ascoltare le dirette! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Non vuoi votare il bot?",
                value = "[TwitchBot Premium](https://twitchbot.io/premium) ti permette di ascoltare le dirette senza dover votare."
            )
            please_wait = "Attendi per favore... " + emoji.loading
            user_noexist = emoji.cmd_fail + "Questo utente non esiste oppure non è attualmente in diretta. Prova a inserire un link al canale."
            np_title = "Ora in riproduzione in: {channel}"
            np_desc = "{title}\n{viewer_count} spettatori"
            np_leave = "Digita «!twitch leave» per fermare la diretta."
            connection_timeout = emoji.cmd_fail + "Connessione al canale vocale persa."
            not_streaming = "In questo momento, non sto trasmettendo niente in questo server."
            disconnected = "Sono uscito dal canale vocale."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Clip - Aiuto"
            command_usage.add_field(
                name = "Comandi",
                value = textwrap.dedent("""\
                `!twitch clips from <utente>` - Serve a ottenere una clip da un utente specifico di Twitch;
                `!twitch clips trending` - Serve a ottenere una clip nelle tendenze;
                `!twitch clips game <gioco>` - Serve a ottenere una clip del gioco specificato;
                `!twitch clips uservoted` - Serve a ottenere una delle clip più popolari votata dagli utenti di TwitchBot.
                """)
            )
            clip_desc = "{user} sta giocando a {game}:\n{url}"
            no_clips = emoji.cmd_fail + "Nessuna clip trovata."
            no_votes = emoji.cmd_fail + "Ancora nessuno ha votato le clip. Riprova più tardi."
            uservote_clip_desc = "{vote_count} voti su questa clip di {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, non è stato possibile elaborare il tuo voto."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "Comandi di TwitchBot"
            e.description = ":warning: __**Non devi aggiungere `<>` o `[]` nei parametri dei comandi.**__"
            e.add_field(
                name="Generale",
                value=textwrap.dedent("""\
                `!twitch help` - Serve a mostrare i comandi di aiuto;
                `!twitch info` - Serve a mostrare le informazioni sul bot;
                `!twitch lang` - Serve a impostare la lingua del bot;
                `!twitch invite` - Serve a mostrare un link di invito per aggiungere TwitchBot nel tuo server;
                `!twitch status` - Serve a mostrare lo stato dell'API di Twitch;
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <utente>` - Serve a ottenere informazioni su un canale di Twitch;
                `!twitch stream user <utente>` - Serve a ottenere informazioni sulla diretta di un utente;
                `!twitch stream watch <utente>` - Serve a guardare una diretta di Twitch tramite Discord;
                `!twitch stream game <nome>` - Serve a guardare una diretta di un gioco specifico;
                `!twitch stream top` - Serve a recuperare le informazioni su una delle dirette più famose;
                `!twitch game <nome>` - Serve a ottenere informazioni su un gioco su Twitch;
                `!twitch top` - Serve a ottenere i giochi più popolari su Twitch.
                """),
                inline=False
            )
            e.add_field(
                name="Clip",
                value=textwrap.dedent("""\
                `!twitch clips from <utente>` - Serve a ottenere una clip da un utente specifico di Twitch;
                `!twitch clips trending` - Serve a ottenere una clip nelle tendenze;
                `!twitch clips game <gioco>` - Serve a ottenere una clip del gioco specificato;
                `!twitch clips uservoted` - Serve a ottenere una delle clip più popolari votata dagli utenti di TwitchBot.
                """),
                inline=False
            )
            e.add_field(
                name="Notifiche degli streamer",
                value=textwrap.dedent("""\
                `!twitch notif add [#canale_di_discord] [nome_dello_streamer] [messaggio]` - Serve ad aggiungere le notifiche per uno streamer in un canale specifico;
                `!twitch notif remove <#canale_di_discord> <nome_dello_streamer>` - Serve a rimuovere le notifiche per uno streamer in un canale specifico;
                `!twitch notif list [#canale_di_discord]` - Serve a mostrare la lista delle notifiche degli streamer in un canale specifico;
                `!twitch notif formatting` - Serve a mostrare le variabili che puoi inserire nei messaggi di notifica degli streamer;
                """),
                inline=False
            )
            e.add_field(
                name="Ruolo delle dirette",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Serve a impostare il ruolo delle dirette per questo server;
                `!twitch live_role filter` - Serve a limitare il ruolo delle dirette a utenti che hanno un ruolo specifico;
                `!twitch live_role delete` - Serve a rimuovere la configurazione del ruolo delle dirette;
                `!twitch live_role view` - Serve a visualizzare quale ruolo è attualmente configurato.
                """),
                inline=False
            )
            e.add_field(
                name="Audio",
                value=textwrap.dedent("""\
                `!twitch listen <utente>` - Serve ad ascoltare una diretta su Twitch nel canale vocale attuale;
                `!twitch nowplaying` - Serve a mostrare - se in corso - la diretta in riproduzione;
                `!twitch leave` - Serve a disconnettere il bot dal canale vocale.
                """),
                inline=False
            )
            e.add_field(
                name="Statistiche di gioco",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <giocatore>` - Serve a mostrare le statistiche di un giocatore di Overwatch;
                `!twitch fortnite <pc/psn/xbl> <giocatore>` - Serve a mostrare le statistiche di un giocatore di Fortnite.
                """),
                inline=False
            )
            e.add_field(
                name="Fitro dei messaggi",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Serve a impostare un filtro esteso in tutto il server contro la tossicità;
                `!twitch filter remove` - Serve a rimuovere il filtro esteso in tutto il server contro la tossicità.
                """),
                inline=False
            )
        class Errors:
            err_report = "Per favore, segnala questo errore agli sviluppatori su <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "Non ho i permessi necessari per effettuare quell'azione."
            not_found = emoji.cmd_fail + "Quel canale di Discord non è stato trovato. Assicurati di non aggiungere <> attorno al parametro e assicurati anche di `#menzionarlo`."
            not_started = "TwitchBot si sta ancora avviando! Aspetta ancora qualche minuto prima di riprovare il comando."
            check_fail = emoji.cmd_fail + "Non hai il permesso di eseguire questo comando."
            cooldown = emoji.cmd_fail + "Potrai eseguire questo comando tra {time} secondi."
            conn_closed = emoji.cmd_fail + "La connessione al canale vocale è disattivata. Motivo: `{reason}`"
            missing_arg = emoji.cmd_fail + "Hai dimenticato il parametro `{param}`."
            too_many_requests = emoji.cmd_fail + "I server di terze parti stanno avendo problemi a tenere il passo con le nostre richieste. Per favore, riprova più tardi."
        class Filter:
            cmd_usage = "Digita `!twitch help filter` per visualizzare come utilizzare del comando."
            need_donate = "Solo i membri di TwitchBot Premium possono usare questo comando. Scopri di più: <https://twitchbot.io/premium>"
            invalid_sensitivity = "Sensitivity deve essere impostata tra 85 e 60."
            add_success = emoji.cmd_success + "Il filtro esteso in tutto il server contro la tossicità è stato impostato con successo."
            no_filter = emoji.cmd_fail + "In questo server non è attivo nessun filtro esteso contro la tossicità."
            del_success = emoji.cmd_success + "Il filtro esteso in tutto il server contro la tossicità è stato rimosso con successo."
        class Games:
            no_results = emoji.cmd_fail + "Nessun risultato trovato."
            no_stats_overwatch = emoji.cmd_fail + "Nessuna statistica è stata trovata per questo giocatore. Se il profilo è privato, non puoi visualizzare le statistiche a meno che non rendi il tuo profilo pubblico. Scopri come rendere il profilo pubblico: <https://dotesports.com/overwatch/news/ow-public-private-profile-25347>"
            no_stats_fortnite = emoji.cmd_fail + "Il giocatore non è stato trovato. Controlla di aver scritto correttamente il nome utente o prova con una piattaforma diversa."
            view_streams = "Guarda la diretta"
            top_games = emoji.twitch_icon + "Giochi più popolari"
            top_games_desc = "{view_count} spettatori • {channel_count} canali in diretta"
            invalid_battletag = "Per favore, inserisci il tuo Battletag in questo formato: `name#id`."
            invalid_platform = "Le piattaforme sono solo `pc`, `psn`, o `xbl`."
            incomplete_data = "I dati del tuo profilo sono incompleti. Se il tuo profilo è privato, segui questi passaggi <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> per renderlo pubblico, così potrai vedere le tue statistiche."
            incomplete_data_short = "Alcuni dati potrebbero essre incompleti o mancanti"
            generic_error = emoji.cmd_fail + "Si è verificato un errore:"
            powered_by_overwatch = "Dati forniti da owapi.net"
            powered_by_fortnite = "Dati forniti da fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**Aiuto per TwitchBot**"
            e.add_field(
                name="Comandi",
                value="TwitchBot risponde solo ai comandi che iniziano con `twitch` o `!twitch`. Digita `!twitch commands` per visualizzare tutti i possibili comandi.",
                inline=False
            )
            e.add_field(
                name="Assistenza",
                value="Se hai bisogno di assistenza/aiuto con TwitchBot, visita il [centro assistenza](https://support.twitchbot.io) oppure entra nel [server ufficiale di assistenza](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Sito web",
                value="Puoi visualizzare le informazioni di TwitchBot su https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Sostieni lo sviluppo di TwitchBot e ottieni una bella manciata di fantastiche funzionalità e vantaggi per soli 5,00$ USD (dollari statunitensi) al mese. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Gara dei voti",
                value="TwitchBot Premium sarà fornito GRATUITAMENTE ai primi tre classificati alla fine di ogni mese! [Vota il bot qui](https://discordbots.org/bot/twitch/vote) e [visualizza la classifica qui](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="Riconoscimenti",
                value="TwitchBot è stato creato da [Akira#4587](https://disgd.pw) con l'utilizzo di discord.py. Per visualizzare gli altri collaboratori, digita `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Altri link",
                value="[Domande frequenti](https://twitchbot.io/faq) · [Dashboard](http://dash.twitchbot.io) · [Vota](https://discordbots.org/bot/twitch/vote) · [Link di invito](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "Traduzioni disponibili"
            avail_lang_setmsg = "Per poter impostare la lingua di TwitchBot, digita !twitch lang <lingua>."
            stats_embed_title = emoji.twitch_icon + "Statistiche di TwitchBot"
            stats_uptime = "Tempo di funzionamento"
            stats_usage = "Utilizzo"
            stats_version = "Versione"
            stats_shardinfo = "Informazioni su Shard"
            stats_system = "Sistema"
            stats_developer = "Sviluppatore"
            stats_patrons = "Sostenitori su Patreon"
            stats_links = "Link"
            stats_links_desc = textwrap.dedent("""\
            **·** Sito web: https://twitchbot.io
            **·** Server di Discord: https://discord.gg/UNYzJqV
            **·** Vota il bot: https://discordbots.org/bot/twitch/vote
            **·** Sostienici: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, puoi invitarmi in un server con questo link: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Ti serve aiuto? Unisciti al server di assistenza: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Stato di Twitch"
            status_cs = "Stato attuale: `{status}`"
            lang_current = "La tua lingua attuale per TwitchBot è impostata in: **{lang}**. Per cambiarla, digita `!twitch lang <lingua>` oppure `!twitch lang help`."
            lang_unavail = emoji.cmd_fail + "Quella lingua non è disponibile. Digita `!twitch lang help` per visualizzare le lingue disponibili."
            lang_set = emoji.cmd_success + "La lingua di TwitchBot è stata impostata con successo in: **{lang}**."
        class Guild:
            submode_command_usage = "Digita `!twitch help sub_only` per visualizzare l'utilizzo del comando."
            submode_success = emoji.cmd_success + "La modalità per soli abbonati è stata attivata in questo server. I nuovi utenti dovranno essere abbonati a {channel} per potersi unire. TwitchBot cercherà di scrivere un messaggio diretto ai non abbonati che si uniscono per poi dopo espellerli. Nota: i membri che si sono già uniti non verranno espulsi."
            submode_kick = "Questo server ha la modalità per soli abbonati attiva. Vuol dire che per unirti, dovrai essere un abbonato di {}.\nPer collegare il tuo account di Twitch a TwitchBot, vai su <https://dash.twitchbot.io>, accedi con Discord e poi clicca su «Link Account» (Collega account) sotto Twitch."
            submode_kick_audit_log = "La modalità per soli abbonati è attiva in questo server. Per disattivarla, digita «!twitch sub_only off»."
            submode_del_success = emoji.cmd_success + "La modalità per soli abbonati è stata disattivata in questo server."
            user_not_in_guild = emoji.cmd_fail + "Quell'utente non è in questo server."
            no_login_dash = emoji.cmd_fail + "{user} non ha ancora effettuato l'accesso alla dashboard di TwitchBot. Per ottenere un canale da un utente diverso, digita `!twitch sub_only on --user-id=(id utente qui)`."
            no_link_dash = emoji.cmd_fail + "{user} non ha ancora collegato il suo canale di Twitch sulla dashboard di TwitchBot. Per ottenere un canale da un utente diverso, digita `!twitch sub_only on --user-id=(id utente qui)`."
            http_err_dash = emoji.cmd_fail + "Si è verificato un errore durante il recupero delle informazioni dalla dashboard di TwitchBot: {error}"
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
            notifications = "Notifications"
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

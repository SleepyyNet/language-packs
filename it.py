from . import _emoji as emoji
import textwrap
import discord

class Italian:
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
                `!twitch filter set <sensibilità>` - Serve a impostare un filtro esteso in tutto il server contro la tossicità;
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
            invalid_sensitivity = "La sensibilità deve essere impostata tra 85 e 60."
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
            command_usage.title = "Ruolo delle dirette - Aiuto"
            command_usage.description = "Con il ruolo delle dirette, puoi impostare un ruolo da aggiungere agli utenti quando andranno in diretta. TwitchBot rimuoverà automaticamente il ruolo quando l'utente terminerà la diretta."
            command_usage.add_field(
                name = "Comandi",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Serve a impostare il ruolo delle dirette per il server attuale;
                `!twitch live_role filter` - Serve a limitare il ruolo delle dirette agli utenti con un ruolo specifico;
                `!twitch live_role delete` - Serve a rimuovere la configurazione del ruolo delle dirette;
                `!twitch live_role view` - Serve a ottenere il ruolo è attualmente impostato.
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "Nessun ruolo è stato specificato. Per favore riesegui il comando e @menziona un ruolo."
            not_set_up = emoji.cmd_fail + "Nessun ruolo delle dirette è stato impostato per questo server. Digita `!twitch live_role set` per impostarne uno."
            role_not_found = emoji.cmd_fail + "Nessun ruolo corrisponde a quella ricerca. Non devi inserire caratteri aggiuntivi nella ricerca, come `<`, `>`, o `@`."
            add_success = emoji.cmd_success + "Gli utenti di questo server che andranno in diretta su Twitch riceveranno il ruolo **{role}**. Se desideri impostare un filtro per il ruolo delle dirette, digita `!twitch live_role filter`."
            del_success = emoji.cmd_success + "La configurazione del ruolo delle dirette è stata rimossa con successo da questo server."
            filter_success = emoji.cmd_success + "La configurazione del ruolo delle dirette è stata impostata con successo in questo server. Potrebbe essere necessario un po' di tempo per aggiornare tutti i ruoli dei membri."
            missing_perms_ext = emoji.cmd_fail + "Per eseguire questo, ho bisogno del permesso **`Gestire i ruoli`**. Se per caso ho già questo permesso, assicurati di trascinare il ruolo nominato `TwitchBot` sopra il ruolo che vuoi impostare."
            view_response = "Il ruolo delle dirette è attualmente impostato, darà il ruolo **{role}** agli utenti che avvieranno una diretta."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Notifiche degli streamer - Aiuto"
            command_usage.description = "Le notifiche degli streamer permettono di impostare un messaggio personalizzato che verrà inviato quando un utente inizia una diretta su Twitch."
            command_usage.add_field(
                name = "Comandi",
                value = textwrap.dedent("""\
                `!twitch notif add [#canale_di_discord] [nome_dello_streamer] [messaggio]` - Serve ad aggiungere una notifica per uno streamer in un canale specifico;
                `!twitch notif remove <#canale_di_discord> <nome_dello_streamer>` - Serve a rimuovere la notifica per lo streamer in un canale specifico;
                `!twitch notif list [#canale_di_discord]` - Serve a mostrare la lista delle notifiche degli streamer per un canale specifico;
                `!twitch notif formatting` - Serve a mostrare le variabili che puoi inserire nei messaggi della notifica dello streamer.
                """)
            )
            limit_reached = emoji.twitch_icon + "Ehilà! Sfortunatamente hai raggiunto la quota massima di notifiche che puoi aggiungere in questo server. Per poter aggiungerne altre, devi effettuare una donazione su <https://twitchbot.io/premium>."
            prompt1 = "In quale canale vuoi ricevere le notifiche? Menzionalo o digita il nome. *(rispondi entro 60 secondi)*"
            prompt2 = "Digita il nome del canale di Twitch di cui vorresti ricevere le notifiche. *(rispondi entro 60 secondi)*"
            prompt3 = "Inserisci un messaggio personalizzato che vuoi che venga mostrato quando il canale inizia una diretta, oppure digita `default` per lasciare il messaggio predefinito. *(rispondi entro 180 secondi)*"
            text_channel_not_found = emoji.cmd_fail + "Non ho trovato quel canale testuale. Chiusura del comando in corso..."
            twitch_user_not_found = emoji.cmd_fail + "Non ho trovato quell'utente di Twitch. Chiusura del comando in corso..."
            twitch_user_not_found_alt = emoji.cmd_fail + "Quell'utente di Twitch non esiste. Assicurati di non aggiungere caratteri attorno al nome (come `<>`). Assicurati anche di non @menzionare un utente di Discord."
            response_timeout = "*La risposta non ha rispettato i limiti di tempo.*"
            invalid_data = emoji.cmd_fail + "I dati inviati da Twitch non sono validi:"
            malformed_user = emoji.cmd_fail + "Quello non sembra un utente di Twitch valido. Puoi solo usare lettere (senza accento), numeri e trattini bassi."
            default_msg = "<https://twitch.tv/{channel}> è in diretta su Twitch!"
            del_fail = emoji.cmd_fail + "Nessuna notifica è stata impostata per questo utente."
            del_success = emoji.cmd_success + "Non riceverai alcuna notifica in {channel} quando {user} inizierà una diretta."
            add_success = emoji.cmd_success + "È stata aggiunta una notifica per {user} in {channel}"
            list_title = "Notifiche degli streamer per **#{channel}**"
            list_embed_limit = "I messaggi personalizzati non sono stati inclusi nell'incorporamento perché Discord limita i caratteri a 1024 per sezione. Verranno mostrati quando l'utente andrà in diretta."
            no_notifs = "Nessuna notifica di streamer è impostata per questo canale."
            notifications = "Notifiche"
            bulk_delete_confirm = "**Stai per eliminare {count} notifiche in {channel}.** Sei sicuro di volerlo fare veramente? Rispondi con `yes` se vuoi procedere."
            bulk_delete_success = emoji.cmd_success + "Sono state eliminate con successo {count} notifiche da {channel}."
            command_cancelled = "Comando annullato."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Variabili delle notifiche dei messaggi"
            notif_variables.description = "Usa una di queste variabili per inserire dati all'interno del messaggio di notifica della diretta."
            notif_variables.add_field(
                name = "Variabili disponibili",
                value = textwrap.dedent("""\
                *`$title$`* - Inserisce il titolo della diretta;
                *`$viewers$`* - Inserisce il numero di persone che stanna attualmente guardando la diretta;
                *`$game$`* - Inserisce il gioco che lo streamer sta attualmente giocando;
                *`$url$`* - Inserisce l'URL del canale;
                *`$name$`* - Inserisce il nome del canale;
                *`$everyone$`* - Inserisce una menzione a @everyone;
                *`$here$`* - Inserisce una menzione a @here.
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "Per eseguire quell'azione, hai bisogno del permesso **{permission}**."
            bot_need_perm = emoji.cmd_fail + "Per eseguire quell'azione, ho bisogno del permesso **{permission}**."
            no_pm = emoji.cmd_fail + "Puoi eseguire questo comando solo nei server."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Comandi delle dirette - Aiuto"
            command_usage.add_field(
                name = "Comandi",
                value = textwrap.dedent("""\
				`!twitch stream user <utente>` - Serve a ottenere informazioni sulla diretta di un utente;
                `!twitch stream watch <utente>` - Serve a guardare una diretta di Twitch tramite Discord;
                `!twitch stream game <nome>` - Serve a guardare una diretta di un gioco specifico;
                `!twitch stream top` - Serve a recuperare le informazioni su una delle dirette più famose.
                """)
            )
            game_desc = "Guarda la diretta di {user}, sta giocando a {game} per {view_count} spettatori:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Quel gioco non è stato trovato."
            game_no_streams = emoji.cmd_fail + "Nessuno sta trasmettendo quel gioco."
            live = "In diretta su Twitch"
            stream_not_found = emoji.cmd_fail + "Quell'utente non esiste oppure non è online. Assicurati di inserire solo il nome dell'utente, senza aggiungere `()` o `<>`."
            stream_desc = textwrap.dedent("""\
            Sta giocando a {game} per {view_count} spettatori
            **[Guarda la diretta su Twitch](https://twitch.tv/{channel})** oppure digita `twitch stream watch {channel}`
            Anteprima della diretta:
            """)
        class Users:
            connections = "Collegamenti per {user}"
            connected = "Connesso a {account}"
            followers = "Follower"
            following = "Canali che segue"
            live = "Attualmente in diretta"
            playing = "Sta giocando a {game} per {view_count} spettatori"
            not_connected = "Non collegato"
            not_live = "Attualmente offline"
            no_login_dash = "Questo utente non ha visitato la [dashboard di TwitchBot](http://dash.twitchbot.io)."
            streamer_id = "ID dello streamer:"
            views = "Visualizzazioni totali"
            view_profile = "Mostra il profilo di Twitch"
            unknown = "Sconosciuto"
            watch_on_twitch = "Guarda su Twitch"
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

from . import _emoji as emoji
import textwrap
import discord

class French:
    def __init__(self):
        self._lang_name = "Français"
        self._lang_emoji = ":flag_fr:"
        self._translator = "Nicendredi#1888, Thxbault#1000"
        class Audio:
            no_channel = emoji.cmd_fail + "Vous devez être dans un salon vocal."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Veuillez upvote pour continuer"
            need_upvote.description = "Vous devez voter pour TwitchBot pour écouter les diffusions ! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Vous voulez passer outre le vote ?",
                value = "[TwitchBot Prémium](https://twitchbot.io/premium) vous permet d'écouter les diffusions sans devoir voter."
            )
            please_wait = "Veuillez patienter... " + emoji.loading
            user_noexist = emoji.cmd_fail + "Cet utilisateur n'existe pas ou n'est pas en cours de diffusion. Essayez avec un lien vers sa chaîne."
            np_title = "Diffusion en cours dans {channel}"
            np_desc = "{title}\n{viewer_count} spectateurs"
            np_leave = "Tapez '!twitch leave' pour arrêter la diffusion"
            connection_timeout = emoji.cmd_fail + "Connection vocale timed out."
            not_streaming = "Je ne diffuse rien sur ce serveur pour le moment."
            disconnected = "A quitté le salon vocal."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Clips - Aide"
            command_usage.add_field(
                name = "Commandes",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - Récupère un clip de l'utilisateur Twitch indiqué
                `!twitch clips trending` - Récupère un clip dans les Tendances
                `!twitch clips game <game>` - Récupère un clip du jeu indiqué
                `!twitch clips uservoted` - Récupère l'un des clips votés les plus populaires par les utilisateurs de TwitchBot
                """)
            )
            clip_desc = "Regardez {user} jouer à {game}:\n{url}"
            no_clips = emoji.cmd_fail + "Aucun clip trouvé."
            no_votes = emoji.cmd_fail + "Personne n'a voté pour un clip pour l'instant. Revenez plus tard."
            uservote_clip_desc = "{vote_count} votes pour ce clip par {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, votre vote n'a pas pu être comptabilisé."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "Commandes TwitchBot"
            e.description = ":warning: __**Ne pas mettre de `<>` ou de `[]` autour des arguments de commandes.**__"
            e.add_field(
                name="Général",
                value=textwrap.dedent("""\
                `!twitch help` - Affiche l'aide du bot
                `!twitch info` - Affiche l'info du bot
                `!twitch invite` - Affiche un lien pour ajouter TwitchBot à votre serveur.
                `!twitch status` - Affiche le statut de l'API Twitch
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - Récupère l'info d'une chaîne Twitch
                `!twitch stream user <user>` - Gets info on a user's stream
                `!twitch stream watch <user>` - Regarder une diffusion Twitch depuis Discord
                `!twitch stream game <name>` - Regarder quelqu'un diffuser le jeu indiqué
                `!twitch stream top` - Récupère l'info d'un stream dans le top
                `!twitch game <name>` - Récupère l'info d'un jeu Twitch
                `!twitch top` - Récupère les jeux les plus populaires sur Twitch
                """),
                inline=False
            )
            e.add_field(
                name="Clips",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - Récupère un clip de l'utilisateur Twitch indiqué
                `!twitch clips trending` - Récupère un clip en Tendances
                `!twitch clips game <game>` - Récupère un clip du jeu indiqué
                `!twitch clips uservoted` - Récupère un des plus populaires clips votés par les utilisateurs de TwitchBot
                """),
                inline=False
            )
            e.add_field(
                name="Notifications de streamer",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Ajoute une notification de diffusion de streamer dans le salon indiqué
                `!twitch notif remove <#discord_channel> <streamer_name>` - Supprime une notification de diffusion de streamer dans le salon indiqué
                `!twitch notif list [#discord_channel]` - Liste les notifications de diffusion pour le salon indiqué
                `!twitch notif formatting` - Affiche les variables que vous pouvez insérer dans les messages de notification de diffusion de streamer
                """),
                inline=False
            )
            e.add_field(
                name="Rôle en live",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Défini le rôle en live pour ce serveur
                `!twitch live_role filter` - Restreint le rôle en live aux utilisateur avec le rôle indiqué
                `!twitch live_role delete` - Efface la configuration du rôle en live
                `!twitch live_role view` - Affiche quel rôle est actuellement configuré
                """),
                inline=False
            )
            e.add_field(
                name="Audio",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - Ecouter une diffusion Twitch dans le salon vocal courant
                `!twitch nowplaying` - Affiche la diffusion en cours, si il y en a une
                `!twitch leave` - Quitte le salon vocal
                """),
                inline=False
            )
            e.add_field(
                name="Statistiques de jeu",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - Affiche les statistiques de joueur d'Overwatch
                `!twitch fortnite <pc/psn/xbl> <player>` - Affiche les statistiques de joueur de Fortnite
                """),
                inline=False
            )
            e.add_field(
                name="Filtre des messsage",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Configure un filtre à toxicité sur tout le serveur
                `!twitch filter remove` - Supprime le filtre à toxicité sur tout le serveur
                """),
                inline=False
            )
        class Errors:
            err_report = "Merci de rapporter cette erreur aux developpeurs à <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "Je n'ai pas la permission correcte pour réaliser cette action."
            not_found = emoji.cmd_fail + "Ce salon discord n'existe pas. Assurez-vous de ne pas mettre <> autour et de `#mention`le salon."
            not_started = "TwitchBot est toujours en train de démarrer! Veuillez patienter quelques minutes avant de réessayer."
            check_fail = emoji.cmd_fail + "Vous n'avez pas la permission d'utiliser cette commande."
            cooldown = emoji.cmd_fail + "Vous pouvez utiliser cette commande dans {time} secondes."
            conn_closed = emoji.cmd_fail + "La connexion vocale a était coupée. Raison: `{reason}`"
            missing_arg = emoji.cmd_fail + "Il vous manque le paramètre `{param}`."
            too_many_requests = emoji.cmd_fail + "Certains serveurs ont du mal à suivre nos demandes. Veuillez réessayer plus tard."
        class Filter:
            cmd_usage = "Tapez `!twitch help filter` pour voir l'utilisation de la commande."
            need_donate = "Seuls les membres TwitchBot Premium peuvent utiliser cette commande. En savoir plus: <https://twitchbot.io/premium>"
            invalid_sensitivity = "La sensibilité doit être comprise entre 85 et 60."
            add_success = emoji.cmd_success + "Réglage avec succès du filtre de toxicité de ce serveur."
            no_filter = emoji.cmd_fail + "Aucun filtre de toxicité n'existe pour ce serveur."
            del_success = emoji.cmd_success + "Filtre de toxicité supprimé du serveur."
        class Games:
            no_results = emoji.cmd_fail + "Aucun résultat."
            no_stats_overwatch = emoji.cmd_fail + "Aucune statistique n'a été trouvée pour ce joueur. Si votre profil est privé, vous ne pouvez pas voir ses statistiques à moins de le rendre public. Veuillez suivre les étapes sur <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> pour rendre votre profil publique."
            no_stats_fortnite = emoji.cmd_fail + "Joueur non trouvé. Vérifiez l'orthographe du nom d'utilisateur ou essayez une autre plateforme.."
            view_streams = "Regarder les diffusions"
            top_games = emoji.twitch_icon + "Top Jeux"
            top_games_desc = "{view_count} spectateurs • {channel_count} chaînes en directs"
            invalid_battletag = "Veuillez entrer votre Battletag dans le format format suivant: `name#id`."
            invalid_platform = "La plate-forme doit être `pc`, `psn`, ou `xbl`."
            incomplete_data = "Les données de votre profil sont incomplètes. Si votre profil est privé, suivez les étapes sur <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> pour le rendre public afin que vous puissiez voir vos statistiques."
            incomplete_data_short = "Certaines données peuvent être manquantes ou incomplètes"
            generic_error = emoji.cmd_fail + "Une erreur est survenue:"
            powered_by_overwatch = "Propulsé par owapi.net"
            powered_by_fortnite = "Propulsé par fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot Aide**"
            e.add_field(
                name="Commandes",
                value="TwitchBot répond aux commandes commençant par `twitch` ou `!twitch`. Tapez `!twitch commands` pour voir toutes les commandes disponibles.",
                inline=False
            )
            e.add_field(
                name="Support",
                value="Si vous avez besoin d’aide avec TwitchBot, vous pouvez visiter le [centre de support](https://support.twitchbot.io) or rejoindre le [serveur de support](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Site",
                value="Vous pouvez voir les informations de TwitchBot sur https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Soutenez le développement de TwitchBot et obtenez des fonctionnalités et avantages intéressants pour seulement 5,00 euros par mois. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Concours de vote",
                value="Nous offrons GRATUITEMENT TwitchBot Premium au top trois des premiers voteurs à la fin de chaque mois ! [Votez ici](https://discordbots.org/bot/twitch/vote) et [regardez le classement](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="À propos",
                value="TwitchBot a été développé par [Akira#4587](https://disgd.pw) avec discord.py. Pour voir les autres contributeurs, tapez `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Autres liens",
                value="[FAQ](https://twitchbot.io/faq) · [Dashboard](http://dash.twitchbot.io) · [Voter](https://discordbots.org/bot/twitch/vote) · [Inviter](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "Langues disponibles"
            avail_lang_setmsg = "Pour changer la langue de TwitchBot, tapez !twitch lang <langage>."
            stats_embed_title = emoji.twitch_icon + "Statistiques TwitchBot"
            stats_uptime = "En ligne depuis"
            stats_usage = "Usage"
            stats_version = "Version"
            stats_shardinfo = "Shard Info"
            stats_system = "Système"
            stats_developer = "Developeur"
            stats_patrons = "Patrons"
            stats_links = "Liens"
            stats_links_desc = textwrap.dedent("""\
            **·** Site: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Vote: https://discordbots.org/bot/twitch/vote
            **·** Dons: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, vous pouvez m'inviter sur un serveur avec ce lien: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Besoin d'aide ? Rejoindre le serveur discord: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Statut Twitch"
            status_cs = "Statut actuel: `{status}`"
            lang_current = "Votre langue actuelle pour TwitchBot est **{lang}**. Pour changer, tapez `!twitch lang <lang>` ou `!twitch lang help`."
            lang_unavail = emoji.cmd_fail + "Cette traduction n'est pas disponible. Tapez `!twitch lang help` pour voir les langues disponibles."
            lang_set = emoji.cmd_success + "Réglage avec succès de la langue TwitchBot sur **{lang}**."
        class Guild:
            submode_command_usage = "Tapez `!twitch help sub_only` pour voir l'utilisation de la commande."
            submode_success = emoji.cmd_success + "Le mode abonnés seulement est activé pour ce serveur. Les nouveaux utilisateurs devront être abonnés à {channel} pour rejoindre. TwitchBot tentera de contacter les non-abonnés qui rejoigne en message privé et les expulsera. Remarque: les membres existants ne seront pas expulsés."
            submode_kick = "Ce serveur est réservé aux abonnés seulement. Pour rejoindre, vous devez être abonné de {}.\nPour lier votre compte Twitch à TwitchBot, allez sur <https://dash.twitchbot.io> et appuyez sur 'Link Account' sous Twitch."
            submode_kick_audit_log = "Le mode abonnés seulement est activé pour ce serveur. Pour le désactiver, tapez '!twitch sub_only off'."
            submode_del_success = emoji.cmd_success + "Le mode abonnés seulement est maintenant désactivé pour ce serveur.."
            user_not_in_guild = emoji.cmd_fail + "Cet utilisateur n'est pas sur ce serveur."
            no_login_dash = emoji.cmd_fail + "{user} ne s'est pas encore connecté au tableau de bord TwitchBot. Pour obtenir un salon d'un autre utilisateur, tapez `!twitch sub_only on --user-id=(user id here)`."
            no_link_dash = emoji.cmd_fail + "{user} n'a pas associé sa chaîne Twitch au tableau de bord TwitchBot. Pour obtenir un salon d'un autre utilisateur, tapez `!twitch sub_only on --user-id=(user id here)`."
            http_err_dash = emoji.cmd_fail + "Une erreur s'est produite lors de la prise d'informations du tableau de bord TwitchBot.: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Rôle de direct - Aide"
            command_usage.description = "Avec le rôle de direct, vous pouvez configurer un rôle à ajouter aux utilisateurs lorsqu'ils sont en direct. TwitchBot enlèvera automatiquement le rôle lorsque l'utilisateur arrêtera de diffuser."
            command_usage.add_field(
                name = "Commandes",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Définit le rôle de direct pour ce serveur
                `!twitch live_role filter` - Limite le rôle de direct aux utilisateurs ayant un rôle spécifique
                `!twitch live_role delete` - Supprime la configuration du rôle de direct
                `!twitch live_role view` - Indique quel rôle est actuellement configuré
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "Aucun rôle n'a été spécifié. Veuillez refaire la commande et @mention un rôle.."
            not_set_up = emoji.cmd_fail + "Aucun rôle de direct n'a été configuré pour ce serveur. Tapez `!twitch live_role set` pour en ajouter."
            role_not_found = emoji.cmd_fail + "Aucun nom de rôle ne correspond à cette requête. Ne mettez pas de caractères en plus dans votre message, tels que `<`, `>`, ou `@`."
            add_success = emoji.cmd_success + "Les utilisateurs de ce serveur qui passent en direct sur Twitch recevront le **{role}** rôle. Si vous souhaitez définir un filtre pour le rôle de direct, tapez `!twitch live_role filter`."
            del_success = emoji.cmd_success + "Suppression réussie de la configuration du rôle de direct pour ce serveur."
            filter_success = emoji.cmd_success + "Filtre du rôle de direct appliqué sur ce serveur. La mise à jour des rôles de tous les membres peut prendre un certain temps."
            missing_perms_ext = emoji.cmd_fail + "J'ai besoin de la permission **`Manage Roles`** pour faire ceci. Si j'ai l'autorisation, assurez-vous de d'avoir le rôle nommé `TwitchBot` au-dessus du rôle que vous souhaitez configurer."
            view_response = "Le rôle de direct est actuellement configuré pour donner aux membres le rôle **{role}** quand ils sont en direct."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Notifications de stream - Aide"
            command_usage.description = "Les notifications de Streamer vous permettent de configurer un message personnalisable à envoyer lorsqu'un utilisateur de Twitch est en direct."
            command_usage.add_field(
                name = "Commandes",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Ajoute une notification pour un streamer dans le salon spécifié
                `!twitch notif remove <#discord_channel> <streamer_name>` - Supprime une notification pour un streamer dans le salon spécifié
                `!twitch notif list [#discord_channel]` - Liste les notifications dans le salon spécifié
                `!twitch notif formatting` - Affiche les variables que vous pouvez insérer dans les messages de notification
                """)
            )
            limit_reached = emoji.twitch_icon + "Malheureusement, vous avez atteint le nombre maximal de notifications que vous pouvez ajouter à ce serveur. Pour en ajouter plus, vous devez faire un don sur <https://twitchbot.io/premium>."
            prompt1 = "Sur quel salon souhaitez-vous recevoir la notification? Mentionnez ou tapez le nom ci-dessous. *(répondez en 60 secondes)*"
            prompt2 = "Tapez le nom de la chaîne Twitch pour laquel vous souhaitez configurer la notification. *(répondez en 60 secondes)*"
            prompt3 = "Entrez un message personnalisé que vous souhaitez afficher lors de la diffusion de l'utilisateur ou tapez `default` pour le message par défaut. *(répondez en 180 secondes)*"
            text_channel_not_found = emoji.cmd_fail + "Impossible de trouver ce salon de texte. Commande annulée..."
            twitch_user_not_found = emoji.cmd_fail + "Cet utilisateur Twitch n'a pas pu être trouvé. Commande annulée..."
            twitch_user_not_found_alt = emoji.cmd_fail + "Cet utilisateur Twitch n'existe pas. Assurez-vous de ne rien ajouter autour du nom (tel que `<>`) et de ne pas @mention un utilisateur de Discord.."
            response_timeout = "*Réponse expirée.*"
            invalid_data = emoji.cmd_fail + "Des données non valides ont été envoyées par Twitch:"
            malformed_user = emoji.cmd_fail + "Cela ne ressemble pas à un utilisateur valide de Twitch. Vous ne pouvez inclure que des tirets, des lettres et des chiffres."
            default_msg = "<https://twitch.tv/{channel}> est maintenant en direct sur Twitch!"
            del_fail = emoji.cmd_fail + "Aucune notification n'a été configurée pour cet utilisateur."
            del_success = emoji.cmd_success + "Vous ne recevrez aucune notification dans {channel} lorsque {user} sera en direct."
            add_success = emoji.cmd_success + "Ajout de la notification pour {user} dans {channel}"
            list_title = "Notification de stream dans **#{channel}**"
            list_embed_limit = "Les messages personnalisés n'étaient pas inclus dans l'embed car il existe une limite de 1024 caractères définie par Discord dans une section. Ils sont toujours présents quand l'utilisateur sera en direct."
            no_notifs = "Aucune notification de streamer n'est configurée pour ce salon."
            notifications = "Aucune notification de streamer n'est configurée pour ce salon."
            bulk_delete_confirm = "**Vous êtes sur le point de supprimer {count} notifications dans {channel}.** Êtes-vous sûr de vouloir faire cela? Répondez par `yes` si vous voulez continuer."
            bulk_delete_success = emoji.cmd_success + "{Count} notifications de {channel} supprimées avec succès."
            command_cancelled = "Commande annulée."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Variables de message"
            notif_variables.description = "Utilisez l'une des variables ci-dessous pour insérer des données dans un message de notification."
            notif_variables.add_field(
                name = "Mise en forme disponible",
                value = textwrap.dedent("""\
                *`$title$`* - Titre du stream
                *`$viewers$`* - Le nombre de personnes regardant actuellement le direct
                *`$game$`* - Le jeu auquel le diffuseur est en train de jouer
                *`$url$`* - Lien de la chaîne
                *`$name$`* - Nom de la chaîne
                *`$everyone$`* - Mention @everyone
                *`$here$`* - Mention @here
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "Vous avez besoin de la permission **{permission}** pour faire ceci."
            bot_need_perm = emoji.cmd_fail + "J'ai besoin de la permission **{permission}** pour faire ceci."
            no_pm = emoji.cmd_fail + "Cette commande est uniquement à utiliser dans un serveur."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Stream Commandes - Aide"
            command_usage.add_field(
                name = "Commandes",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - Affiche les infos d'un stream
                `!twitch stream watch <user>` - Regarder le stream dans discord
                `!twitch stream game <name>` - Regarder quelqu'un diffuser le jeu spécifié
                `!twitch stream top` - Récupère les informations sur une top diffusion
                """)
            )
            game_desc = "Regardez {utilisateur} en train de jouer à {game} acec {view_count} spectateurs:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Jeu non trouvé."
            game_no_streams = emoji.cmd_fail + "Personne ne diffuse ce jeu."
            live = "En direct sur Twitch"
            stream_not_found = emoji.cmd_fail + "Cet utilisateur n'existe pas ou n'est pas en ligne. Assurez-vous que vous entrez uniquement le nom de l'utilisateur et rien d'autre, comme `()` ou `<>`."
            stream_desc = textwrap.dedent("""\
            Joue à {game} pour {view_count} spectateurs
            **[Regarder sur twitch](https://twitch.tv/{channel})** ou tapez `twitch stream watch {channel}`
            Prévisualisation:
            """)
        class Users:
            connections = "Connexions pour {user}"
            connected = "Connecté à {account}"
            followers = "Abonnés"
            following = "Abonnements"
            live = "Actuellement en direct"
            playing = "Joue à {game} pour {view_count} spectateurs"
            not_connected = "Non Connecté"
            not_live = "Actuellement hors ligne"
            no_login_dash = "Cet utilisateur n'a pas visité le [panel TwitchBot](http://dash.twitchbot.io)."
            streamer_id = "Streamer ID:"
            views = "Vues"
            view_profile = "Voir le profil de Twitch"
            unknown = "Inconnu"
            watch_on_twitch = "Regarder sur Twitch"
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

from . import _emoji as emoji
import textwrap
import discord

class English:
    def __init__(self):
        self._lang_name = "Español"
        self._lang_emoji = ":flag_mx: :flag_es:"
        self._translator = "diiegoorgueez#0001"
        class Audio:
            no_channel = emoji.cmd_fail + "Necesitas estar en un canal de voz."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Por favor, vota a favor para continuar."
            need_upvote.description = "¡Necesitas votar a favor a TwitchBot para escuchar las transmisiones! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "¿Quieres saltarte las votaciones a favor?",
                value = "[TwitchBot Premium](https://twitchbot.io/premium) te permite escuchar directos sin votar."
            )
            please_wait = "Por favor espera... " + emoji.loading
            user_noexist = emoji.cmd_fail + "Este usuario no existe o no está en directo actualmente. Intenta mandar un enlace al canal."
            np_title = "Ahora sonando en {channel}"
            np_desc = "{title}\n{viewer_count} viéndolo actualmente"
            np_leave = "Escribe '!twitch leave' para parar la transmisión"
            connection_timeout = emoji.cmd_fail + "Tiempo de espera agotado de conexión de voz."
            not_streaming = "No estoy transmitiendo nada en este servidor en este momento."
            disconnected = "Dejé el canal de voz."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Clips - Ayuda"
            command_usage.add_field(
                name = "Comandos",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - Obtiene un clip del usuario de Twitch especificado
                `!twitch clips trending` - Obtiene un clip de tendencias
                `!twitch clips game <game>` - Obtiene un clip del juego especificado
                `!twitch clips uservoted` - Obtiene uno de los clips más populares votados por los usuarios de TwitchBot
                """)
            )
            clip_desc = "Mira a {user} jugando {game}:\n{url}"
            no_clips = emoji.cmd_fail + "No se encontraron clips."
            no_votes = emoji.cmd_fail + "Nadie ha votado a ningún clip todavía. Vuelve más tarde."
            uservote_clip_desc = "{vote_count} votos en este clip de {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, tu voto a favor no pudo ser procesado."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "Comandos TwitchBot"
            e.description = ":warning: __**No pongas `<>` o `[]` alrededor de los argumentos de comandos.**__"
            e.add_field(
                name="General",
                value=textwrap.dedent("""\
                `!twitch help` - Muestra la ayuda del bot
                `!twitch info` - Muestra la info del bot
                `!twitch lang` - Establece el idioma del bot
                `!twitch invite` - Muestra un enlace para añadir a TwitchBot a tu servidor
                `!twitch status` - Muestra el estado de la API de Twitch
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - Obtiene información de un canal de Twitch
                `!twitch stream user <user>` - Obtiene información de una tranmisión de un usuario
                `!twitch stream watch <user>` - Mira una transmisión de Twitch desde Discord
                `!twitch stream game <name>` - Ve a alguien transmitir el juego especificado
                `!twitch stream top` - Obtiene información de una transmisión superior
                `!twitch game <name>` - Obtiene información sobre un juego de Twitch
                `!twitch top` - Obtiene los juegos de Twitch más populares
                """),
                inline=False
            )
            e.add_field(
                name="Clips",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - Obtiene un clip del usuario especificado
                `!twitch clips trending` - Obtiene un clip de tendencias
                `!twitch clips game <game>` - Obtiene un clip del juego especificado
                `!twitch clips uservoted` - Obtiene uno de los clips más populares votados por los usuarios de TwitchBot
                """),
                inline=False
            )
            e.add_field(
                name="Notificaciones de Transmisión",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Agrega una notificación de transmisión de un streamer al canal especificado
                `!twitch notif remove <#discord_channel> <streamer_name>` - Elimina una notificación de transmisión de un streamer al canal especificado
                `!twitch notif list [#discord_channel]` - Manda una lista de las notificaciones de streamer del canal especificado
                `!twitch notif formatting` - Muestra las variables que puedes insertar en los mensajes de notificación de transmisión
                """),
                inline=False
            )
            e.add_field(
                name="Rol En Vivo",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Establece el rol en vivo para el servidor actual
                `!twitch live_role filter` - Restringe el rol en vivo a usuarios con un rol específico
                `!twitch live_role delete` - Elimina la configuración de rol en vivo
                `!twitch live_role view` - Te dice qué rol está configurado actualmente
                """),
                inline=False
            )
            e.add_field(
                name="Audio",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - Escucha una transmisión de Twitch en el canal de voz actual
                `!twitch nowplaying` - Muestra la transmisión actual, si la hay
                `!twitch leave` - Deja un canal de voz
                """),
                inline=False
            )
            e.add_field(
                name="Estadísticas de juego",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - Muestra las estadísticas de un jugador de Overwatch
                `!twitch fortnite <pc/psn/xbl> <player>` - Muestra las estadísticas de un jugador de Fortnite
                """),
                inline=False
            )
            e.add_field(
                name="Filtro de mensajes",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Establece el filtro de toxicidad en todo el servidor
                `!twitch filter remove` - Elimina el filtro de toxicidad del servidor
                """),
                inline=False
            )
        class Errors:
            err_report = "Por favor reporta este error a los desarrolladores en <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "No tengo los permisos correctos para hacer eso."
            not_found = emoji.cmd_fail + "Ese canal de Discord no fue encontrado. Asegúrate de no estar poniendo <> alrededor y que estas `#mention`ing it."
            not_started = "TwitchBot todavía se está encendiendo! Por favor, espera unos minutos antes de volver a intentarlo."
            check_fail = emoji.cmd_fail + "No tienes permiso para ejecutar este comando."
            cooldown = emoji.cmd_fail + "Puedes ejecutar este comando en {time} segundos."
            conn_closed = emoji.cmd_fail + "La conexión de voz ha sido cerrada. Razón: `{reason}`"
            missing_arg = emoji.cmd_fail + "Te estás saltando el parámetro `{param}`."
            too_many_requests = emoji.cmd_fail + "Los servidores de terceros están teniendo problemas para cumplir con nuestras solicitudes. Por favor, inténtalo de nuevo más tarde."
        class Filter:
            cmd_usage = "Escribe `!twitch help filter` para ver el uso del comando."
            need_donate = "Solo los miembros de TwitchBot Premium pueden usar este comando. Aprende más: <https://twitchbot.io/premium>"
            invalid_sensitivity = "La sensibilidad debe estar entre 85 y 60."
            add_success = emoji.cmd_success + "Establecido con éxito el filtro de toxicidad de este servidor."
            no_filter = emoji.cmd_fail + "No existe ningún filtro de toxicidad para este servidor."
            del_success = emoji.cmd_success + "Se eliminó con éxito el filtro de toxicidad de este servidor."
        class Games:
            no_results = emoji.cmd_fail + "No se han encontrado resultados."
            no_stats_overwatch = emoji.cmd_fail + "No se encontraron estadísticas para este jugador. Si tu perfil es privado, no puedes ver las estadísticas a menos que lo hagas público. Por favor sigue los pasos en <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> para hacer tu perfil público."
            no_stats_fortnite = emoji.cmd_fail + "Jugador no encontrado. Revisa la ortografía del nombre de usuario o prueba con una plataforma diferente."
            view_streams = "Ver transmisiones"
            top_games = emoji.twitch_icon + "Los mejores juegos"
            top_games_desc = "{view_count} espectadores • {channel_count} canales transmitiendo"
            invalid_battletag = "Por favor escribe tu Battletag en un formato de `name#id`."
            invalid_platform = "La plataforma debe ser `pc`, `psn`, o `xbl`."
            incomplete_data = "Los datos de tu perfil están incompletos. Si tu perfil es privado, sigue los pasos en <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> para hacerlo público y así poder ver tus estadísticas."
            incomplete_data_short = "Algunos datos pueden faltar o estar incompletos"
            generic_error = emoji.cmd_fail + "Ocurrió un error:"
            powered_by_overwatch = "Desarrollado por owapi.net"
            powered_by_fortnite = "Desarrollado por fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot Ayuda**"
            e.add_field(
                name="Comandos",
                value="TwitchBot responde a comandos empezando por `twitch` o `!twitch`. Escribe `!twitch commands` para ver todos los comandos ejecutables.",
                inline=False
            )
            e.add_field(
                name="Soporte",
                value="Si necesitas ayuda con TwitchBot, puedes visitar el [centro de soporte](https://support.twitchbot.io) o entra al [servidor de soporte](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Sitio web",
                value="Puedes ver información sobre TwitchBot en https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Apoya el desarrollo de TwitchBot y obtén un puñado de características y beneficios geniales por solo $ 5.00 USD al mes. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Competición de Votaciones a favor",
                value="Estamos regalando TwitchBot Premium GRATIS a los tres primeros votantes al final de cada mes! [Vota aquí](https://discordbots.org/bot/twitch/vote) and [view the leaderboard](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="Acerca de",
                value="TwitchBot fue creado por [Akira#4587](https://disgd.pw) usando discord.py. Para ver otros colaboradores, escribe `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Otros enlaces",
                value="[FAQ](https://twitchbot.io/faq) · [Dashboard](http://dash.twitchbot.io) · [Vota](https://discordbots.org/bot/twitch/vote) · [Invitación](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "Traducciones Disponibles"
            avail_lang_setmsg = "Para configurar el idioma de TwitchBot, escribe !twitch lang <idioma>."
            stats_embed_title = emoji.twitch_icon + "Estadísticas de TwitchBot"
            stats_uptime = "Tiempo de actividad"
            stats_usage = "Uso"
            stats_version = "Versión"
            stats_shardinfo = "Información de Shards"
            stats_system = "Sistema"
            stats_developer = "Desarrollador"
            stats_patrons = "Patrons"
            stats_links = "Enlaces"
            stats_links_desc = textwrap.dedent("""\
            **·** Sitio web: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Votar: https://discordbots.org/bot/twitch/vote
            **·** Donar: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, puedes invitarme a un servidor con este enlace: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Necesitas ayuda? Entra al servidor de soporte: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Estado de Twitch"
            status_cs = "Estado actual: `{status}`"
            lang_current = "Tu idioma actual para TwitchBot es **{lang}**. Para cambiarlo, escribe `!twitch lang <lang>` o `!twitch lang help`."
            lang_unavail = emoji.cmd_fail + "Esa traducción no está disponible. Escribe `!twitch lang help` para ver los idiomas disponibles."
            lang_set = emoji.cmd_success + "El idioma de TwitchBot ha sido establecido con éxito a **{lang}**."
        class Guild:
            submode_command_usage = "Escribe `!twitch help sub_only` para ver el uso del comando."
            submode_success = emoji.cmd_success + "El modo solo para suscriptores ha sido habilitado para este servidor. Los nuevos usuarios deberán estar suscritos a {channel} para entrar. TwitchBot intentará mandar MD a los no suscriptores que se unan y les echará del servidor. Nota: los miembros existentes no serán echados."
            submode_kick = "Este servidor está en modo solo para suscriptores. Para entrar, necesitas ser un suscriptor de {}.\nPara vincular tu cuenta de Twitch a TwitchBot, vaya a <https://dash.twitchbot.io> y dale a 'Link Account' debajo de Twitch."
            submode_kick_audit_log = "El modo solo para suscriptores está habilitado para este servidor. Para quitarlo, escribe '!twitch sub_only off'."
            submode_del_success = emoji.cmd_success + "El modo solo para suscriptores se ha deshabilitado para este servidor."
            user_not_in_guild = emoji.cmd_fail + "Ese usuario no está en este servidor."
            no_login_dash = emoji.cmd_fail + "{user} aún no ha iniciado sesión en el dashboard de TwitchBot. Para obtener un canal de un usuario diferente, escribe `!twitch sub_only on --user-id=(user id here)`."
            no_link_dash = emoji.cmd_fail + "{user} no ha vinculado su canal de Twitch en el dashboard de TwitchBot. Para obtener un canal de un usuario diferente, escribe `!twitch sub_only on --user-id=(user id here)`."
            http_err_dash = emoji.cmd_fail + "Se produjo un error al intentar obtener información del panel de TwitchBot: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Rol En Vivo - Ayuda"
            command_usage.description = "Con Rol En Vivo, puedes configurar un rol para agregar a los usuarios cuando estén en directo. TwitchBot eliminará automáticamente el rol cuando el usuario detenga la transmisión."
            command_usage.add_field(
                name = "Comandos",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Establece el rol en vivo para el servidor actual
                `!twitch live_role filter` - Restringe el rol en vivo a usuarios con un rol específico
                `!twitch live_role delete` - Elimina la configuración de rol en vivo
                `!twitch live_role view` - Te dice qué rol está configurado actualmente
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "No se especificó ningún rol. Por favor, vuelve a ejecutar el comando y @menciona a un rol."
            not_set_up = emoji.cmd_fail + "No se ha configurado ningún rol en vivo para este servidor. Escribe `!twitch live_role set` para establecer uno."
            role_not_found = emoji.cmd_fail + "Ningún rol coincide con ese nombre. No pongas caracteres extra, como `<`, `>`, o `@`."
            add_success = emoji.cmd_success + "Los usuarios del servidor que estén en directo en Twitch recibirán el rol **{role}**. Si quieres establecer un filtro para Rol En Vivo, escribe `!twitch live_role filter`."
            del_success = emoji.cmd_success + "Se eliminó con éxito la configuración de Rol En Vivo de este servidor."
            filter_success = emoji.cmd_success + "Establecido correctamente el filtro de Rol En Vivo de este servidor. Puede tomar un tiempo actualizar todos los roles de los miembros."
            missing_perms_ext = emoji.cmd_fail + "Necesito el permiso **`Manage Roles`** para hacer esto. Si tengo el permiso, entonces asegúrate de arrastrar el rol llamado `TwitchBot` por encima del rol que quieras configurar."
            view_response = "El rol en vivo está configurado actualmente para dar a los miembros el rol **{role}** cuando estén en directo."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Notificaciones de Transmisión - Ayuda"
            command_usage.description = "Las notificaciones de transmisión te permiten configurar un mensaje personalizable que se envia cuando un usuario de Twitch empiece directo."
            command_usage.add_field(
                name = "Comandos",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Agrega una notificación de transmisión de un streamer al canal especificado
                `!twitch notif remove <#discord_channel> <streamer_name>` - Elimina una notificación de transmisión de un streamer al canal especificado
                `!twitch notif list [#discord_channel]` - Manda una lista de las notificaciones de streamer del canal especificado
                `!twitch notif formatting` - Muestra las variables que puedes insertar en los mensajes de notificación de transmisión
                """)
            )
            limit_reached = emoji.twitch_icon + "Hola! Desafortunadamente, has alcanzado la cantidad máxima de notificaciones que puedes agregar a este servidor. Para añadir más, tienes que donar en <https://twitchbot.io/premium>."
            prompt1 = "¿En qué canal quieres recibir la notificación? Menciona o escribe el nombre de uno debajo. *(responde en 60 segundos)*"
            prompt2 = "Escribe el nombre del canal de Twitch para el que quieras configurar la notificación. *(responde en 60 segundos)*"
            prompt3 = "Ingresa un mensaje personalizado que quieres que se muestre cuando el usuario empiece directo, o escribe `default` para el mensaje predeterminado. *(responde en 180 segundos)*"
            text_channel_not_found = emoji.cmd_fail + "No se pudo encontrar ese canal de texto. Cerrando comando..."
            twitch_user_not_found = emoji.cmd_fail + "Ese usuario de Twitch no pudo ser encontrado. Cerrando comando..."
            twitch_user_not_found_alt = emoji.cmd_fail + "Ese usuario de Twitch no existe. Asegúrate de que no estés poniendo nada extra alrededor del nombre (como `<>`), y de que no estás @mencionando a un usuario de Discord."
            response_timeout = "*Respuesta expirada.*"
            invalid_data = emoji.cmd_fail + "Datos inválidos fueron enviados desde Twitch:"
            malformed_user = emoji.cmd_fail + "Eso no parece un usuario válido de Twitch. Solo puedes incluir guiones bajos, letras, y números."
            default_msg = "<https://twitch.tv/{channel}> está ahora en directo en Twitch!"
            del_fail = emoji.cmd_fail + "No se ha configurado ninguna notificación para este usuario.."
            del_success = emoji.cmd_success + "No recibirás ninguna notificación en {channel} cuando {user} empiece directo."
            add_success = emoji.cmd_success + "Notificación agregada para {user} en {channel}"
            list_title = "Notificaciones de Transmisión para **#{channel}**"
            list_embed_limit = "Los mensajes personalizados weren't included en el embed porque hay un límite establecido de Discord de 1024 caracteres en una sección. Todavía se mostrarán cuando el usuario empiece directo."
            no_notifs = "Notificaciones"
            notifications = "No se han configurado notificaciones de transmisión para este canal."
            bulk_delete_confirm = "**Estás a punto de borrar {count} notificaciones en {channel}.** ¿Estás seguro de que quieres hacer esto? Responde con `yes` si quieres continuar."
            bulk_delete_success = emoji.cmd_success + "{count} notificaciones eliminadas exitosamente de {channel}."
            command_cancelled = "Comando cancelado."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Variables del mensaje de notificación"
            notif_variables.description = "Usa una de las variables a continuación para insertar datos en un mensaje de notificación de transmisión."
            notif_variables.add_field(
                name = "Formato disponible",
                value = textwrap.dedent("""\
                *`$title$`* - El título de la transmision
                *`$viewers$`* - La cantidad de personas que actualmente están viendo la transmisión
                *`$game$`* - El juego que el streamer está jugando actualmente
                *`$url$`* - URL del canal
                *`$name$`* - El nombre del canal
                *`$everyone$`* - Inserta una mención @everyone
                *`$here$`* - Inserta una mención @here
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "Necesitas el permiso **{permission}** para hacer esto."
            bot_need_perm = emoji.cmd_fail + "Necesito el permiso **{permission}** para hacer esto."
            no_pm = emoji.cmd_fail + "Solo puedes usar este comando en un servidor."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Comandos de Transmisión - Ayuda"
            command_usage.add_field(
                name = "Comandos",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - Obtiene información de una tranmisión de un usuario
                `!twitch stream watch <user>` - Mira una transmisión de Twitch desde Discord
                `!twitch stream game <name>` - Ve a alguien transmitir el juego especificado
                `!twitch stream top` - Obtiene información de una transmisión superior
                """)
            )
            game_desc = "Mira a {user} jugando {game} para {view_count} viewers:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Ese juego no pudo ser encontrado."
            game_no_streams = emoji.cmd_fail + "Nadie está transmitiendo ese juego."
            live = "En directo en Twitch"
            stream_not_found = emoji.cmd_fail + "Ese usuario no existe o no está conectado. Asegúrate de que solo estés escribiendo el nombre del usuario y no nada extra, como `()` o `<>`."
            stream_desc = textwrap.dedent("""\
            Jugando {game} para {view_count} espectadores
            **[Ver en Twitch](https://twitch.tv/{channel})** o escribe `twitch stream watch {channel}`

            Vista previa de la transmisión:
            """)
        class Users:
            connections = "Conexiones para {user}"
            connected = "Conectado a {account}"
            followers = "Seguidores"
            following = "Siguiendo"
            live = "Actualmente en vivo"
            playing = "Jugando {game} para {view_count} espectadores"
            not_connected = "No conectado"
            not_live = "Actualmente fuera de linea"
            no_login_dash = "Este usuario no ha visitado el [Dashboard de TwitchBot](http://dash.twitchbot.io)."
            streamer_id = "ID de Streamer:"
            views = "Vistas"
            view_profile = "Ver el perfil de Twitch"
            unknown = "Desconocido"
            watch_on_twitch = "Ver en Twitch"
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

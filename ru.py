from . import _emoji as emoji
import textwrap
import discord

class Russian:
    def __init__(self):
        self._lang_name = "Русский"
        self._lang_emoji = ":flag_ru:"
        self._translator = "D3bi#6969, xinitrc#0001"
        class Audio:
            no_channel = emoji.cmd_fail + "Вам надо находится в голосовом канале"
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Пожалуйста, проголосуйте для того, чтобы продолжить"
            need_upvote.description = "Вам необходимо проголосовать за TwitchBot для прослушивания стримов! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Вы хотите пропустить голосование?",
                value = "[TwitchBot Premium](https://twitchbot.io/premium) позволяет слушать стримы без голосования."
            )
            please_wait = "Пожалуйста, подождите... " + emoji.loading
            user_noexist = emoji.cmd_fail + "Этого пользователя не существует, или он не стримит в данный момент. Попробуйте ввести ссылку на канал."
            np_title = "Сейчас играет в  {channel}"
            np_desc = "{title}\n{viewer_count} зрителей в данный момент"
            np_leave = "Введите '!twitch leave' чтобы остановить поток"
            connection_timeout = emoji.cmd_fail + "Время голосового соединения истекло."
            not_streaming = "Я сейчас ничего не транслирую на этом сервере."
            disconnected = "Покинул голосовой канал."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Клипы - Помошь"
            command_usage.add_field(
                name = "Команды",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - Получить клип указанного пользователя Twitch
                `!twitch clips trending` - Получить набирающий популярность клип
                `!twitch clips game <game>` - Получить клип указанной игры
                `!twitch clips uservoted` - Получить один из самых популярных клипов, за который проголосовали пользователи TwitchBot.
                """)
            )
            clip_desc = "Посмотрите, как {user} играет в {game}:\n{url}"
            no_clips = emoji.cmd_fail + "Клипов не найдено."
            no_votes = emoji.cmd_fail + "Никто еще не голосовал ни за какие клипы. Вернитесь позже."
            uservote_clip_desc = "{vote_count} голосов на клипе от {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, Ваш голос не может быть обработан."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "Команды TwitchBot"
            e.description = ":warning: __**Не вставляйте символы `<>` или `[]` вокруг аргументов команд.**__"
            e.add_field(
                name="Общее",
                value=textwrap.dedent("""\
                `!twitch help` - Показать помощь бота
                `!twitch info` - Показать информацию о боте
                `!twitch lang` - Устанавить язык бота
                `!twitch invite` - Показать ссылку для добавления TwitchBot на ваш сервер
                `!twitch status` - Показать статус API Twitch
                `!twitch ping` - Понг!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - Получить информацию о канале Twitch
                `!twitch stream user <user>` - Получить информацию о стриме пользователя
                `!twitch stream watch <user>` - Смотреть трансляцию Twitch через Discord
                `!twitch stream game <name>` - Посмотреть, как кто-то стримит указанную игру
                `!twitch stream top` - Получить информацию о популярных стримах
                `!twitch game <name>` - Получить информацию об игре Twitch
                `!twitch top` - Получить самые популярные игры Twitch
                """),
                inline=False
            )
            e.add_field(
                name="Клипы",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - Получить клип указанного пользователя Twitch
                `!twitch clips trending` - Получить набирающий популярности клип
                `!twitch clips game <game>` - Получить клип указанной игры
                `!twitch clips uservoted` - Получить один из самых популярных клипов, за которые проголосовали пользователи TwitchBot.
                """),
                inline=False
            )
            e.add_field(
                name="Уведомления о стримах",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Добавить уведомление о стриме для стримера в указанный канал
                `!twitch notif remove <#discord_channel> <streamer_name>` - Убрать уведомление о стриме для стримера в указанный канал
                `!twitch notif list [#discord_channel]` - Перечислить список уведомлений о стримах для указанного канала
                `!twitch notif formatting` - Показать переменные, которые вы можете вставить в сообщении уведомления о стриме
                """),
                inline=False
            )
            e.add_field(
                name="Live Role",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Устанавить Live Role для текущего сервера
                `!twitch live_role filter` - Ограничить Live Role для пользователей с определенной ролью
                `!twitch live_role delete` - Удалить конфигурацию Live Role
                `!twitch live_role view` - Показать, какая роль установлена в данный момент
                """),
                inline=False
            )
            e.add_field(
                name="Аудио",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - Прослушивание стрима Twitch в текущем голосовом канале
                `!twitch nowplaying` - Если есть, показывать какой стрим воспроизводится в данный момент
                `!twitch leave` - Выйти из голосового канала
                """),
                inline=False
            )
            e.add_field(
                name="Игровая статистика",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - Показать статистику игрока в Overwatch
                `!twitch fortnite <pc/psn/xbl> <player>` - Показать статистику игрока в Fortnite
                """),
                inline=False
            )
            e.add_field(
                name="Фильтр сообщений",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Устанавить фильтр токсичности для всего сервера
                `!twitch filter remove` - Убрать фильтр токсичности для всего сервера
                """),
                inline=False
            )
        class Errors:
            err_report = "Пожалуйста, сообщите об этой ошибке разработчикам на <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "У меня нет необходимых разрешений для этого."
            not_found = emoji.cmd_fail + "Данный канал Discord не найден. Убедитесь, что вы не ставите <> вокруг названия и не используете `#mention`."
            not_started = "TwitchBot все еще запускается! Пожалуйста, подождите несколько минут, прежде чем пытаться снова."
            check_fail = emoji.cmd_fail + "У вас нет разрешения на запуск этой команды."
            cooldown = emoji.cmd_fail + "Вы сможете выполнить эту команду через {time} секунд."
            conn_closed = emoji.cmd_fail + "Голосовое соединение было закрыто. Причина: `{reason}`"
            missing_arg = emoji.cmd_fail + "Вы пропустили параметр: `{param}`."
            too_many_requests = emoji.cmd_fail + "Сторонние серверы испытывают трудности с выполнением наших запросов. Пожалуйста, попробуйте позже."
        class Filter:
            cmd_usage = "Введите `!twitch help filter` для просмотра помощи по использованию команды."
            need_donate = "Только члены TwitchBot Premium могут использовать эту команду. Узнать больше: <https://twitchbot.io/premium>"
            invalid_sensitivity = "Чувствительность должна быть между 85 и 60."
            add_success = emoji.cmd_success + "Фильтр токсичности был успешно установлен на этом сервере."
            no_filter = emoji.cmd_fail + "Для этого сервера ещё не был установлен фильтр токсичности."
            del_success = emoji.cmd_success + "Фильтр токсичности успешно удалён с этого сервера."
        class Games:
            no_results = emoji.cmd_fail + "Результаты не найдены."
            no_stats_overwatch = emoji.cmd_fail + "Статистика для этого игрока не найдена. Если ваш профиль закрыт, вы не сможете просмотреть его статистику, если не сделаете его общедоступным. Пожалуйста, следуйте инструкциям на <https://dotesports.com/overwatch/news/ow-public-private-profile-25347>, чтобы сделать ваш профиль общедоступным."
            no_stats_fortnite = emoji.cmd_fail + "Игрок не найден. Проверьте правильность написания имени пользователя или попробуйте другую платформу."
            view_streams = "Просмотр стрима"
            top_games = emoji.twitch_icon + "Топ игр"
            top_games_desc = "{view_count} зрителей • {channel_count} каналов сейчас стримят"
            invalid_battletag = "Пожалуйста, введите ваш Battletag в формате `name#id`."
            invalid_platform = "Платформа должна быть одной из `pc`, `psn` или `xbl`."
            incomplete_data = "Данные вашего профиля неполные. Если ваш профиль закрыт, следуйте инструкциям на <https://dotesports.com/overwatch/news/ow-public-private-profile-25347>, чтобы сделать его общедоступным, чтобы вы могли просматривать свою статистику."
            incomplete_data_short = "Некоторые данные отсутствуют или неполные"
            generic_error = emoji.cmd_fail + "Произошла ошибка:"
            powered_by_overwatch = "Предоставлено owapi.net"
            powered_by_fortnite = "Предоставлено fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**Помощь TwitchBot**"
            e.add_field(
                name="Команды",
                value="TwitchBot отвечает на команды, начинающиеся с `twitch` или `!twitch`. Введите `!twitch commands`, чтобы просмотреть все доступные команды.",
                inline=False
            )
            e.add_field(
                name="Служба поддержки",
                value="Если вам нужна помощь с TwitchBot, вы можете посетить [центр поддержки](https://support.twitchbot.io) или присоединиться к [серверу поддержки](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Веб-сайт",
                value="Вы можете просмотреть информацию о TwitchBot на https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Поддержите разработку TwitchBot и получите несколько интересных функций и преимуществ всего за $5.00 USD в месяц. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Конкурс голосов",
                value="Мы раздаем TwitchBot Premium БЕСПЛАТНО трем лучшим участникам голосования в конце каждого месяца! [Голосовать здесь](https://discordbots.org/bot/twitch/vote) и [просмотреть таблицу лидеров](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="About",
                value="TwitchBot был сделан [Akira#4587](https://disgd.pw) с помощью discord.py. Чтобы просмотреть других помощников, введите `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Другие ссылки",
                value="[Часто задаваемые вопросы](https://twitchbot.io/faq) · [Панель управления](http://dash.twitchbot.io) · [Голосование](https://discordbots.org/bot/twitch/vote) · [Приглашение](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Блог](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "Доступные переводы"
            avail_lang_setmsg = "Чтобы установить язык TwitchBot, введите !twitch lang <language>."
            stats_embed_title = emoji.twitch_icon + "Статистика TwitchBot"
            stats_uptime = "Время работы"
            stats_usage = "Использование"
            stats_version = "Версия"
            stats_shardinfo = "Версия осколка БД"
            stats_system = "Система"
            stats_developer = "Разработчик"
            stats_patrons = "Меценаты"
            stats_links = "Ссылки"
            stats_links_desc = textwrap.dedent("""\
            **·** Веб-сайт: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Голосование: https://discordbots.org/bot/twitch/vote
            **·** Донат: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, Вы можете пригласить меня на сервер по этой ссылке: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Нужна помощь? Присоединитесь к серверу поддержки: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Статус Twitch"
            status_cs = "Текущее состояние: `{status}`"
            lang_current = "Ваш текущий язык для TwitchBot: **{lang}**. Для того, чтобы изменить его, введите `!twitch lang <lang>` или `!twitch lang help`."
            lang_unavail = emoji.cmd_fail + "Этот перевод недоступен. Введите `!twitch lang help` для просмотра доступных языков."
            lang_set = emoji.cmd_success + "Вы успешно установили язык TwitchBot на **{lang}**."
        class Guild:
            submode_command_usage = "Введите `!twitch help sub_only` для просмотра помощи по использованию команды."
            submode_success = emoji.cmd_success + "Для этого сервера был включен режим только для подписчиков. Новые пользователи должны будут подписаться на {channel}, чтобы присоединиться. TwitchBot будет пытаться написать личное сообщение тем, кто не подписан, и выгнать их. Примечание: существующие участники не будут выгнаны."
            submode_kick = "Этот сервер находится в режиме только для подписчиков. Чтобы присоединиться, вы должны быть подписчиком {}.\nЧтобы связать свою учетную запись Twitch с TwitchBot, перейдите на <https://dash.twitchbot.io> и нажмите 'Link Account' рядом с Twitch."
            submode_kick_audit_log = "Для этого сервера включен режим только для подписчиков. Чтобы выключить его, наберите '!twitch sub_only off'."
            submode_del_success = emoji.cmd_success + "Режим только для подписчиков был отключен для этого сервера."
            user_not_in_guild = emoji.cmd_fail + "Этого пользователя нет на этом сервере."
            no_login_dash = emoji.cmd_fail + "{user} еще не вошел в панель управления TwitchBot. Чтобы получить канал от другого пользователя, введите `!twitch sub_only on --user-id=(user id here)`."
            no_link_dash = emoji.cmd_fail + "{user} Пользователь не связал свой канал Twitch на панели управления TwitchBot. Чтобы получить канал от другого пользователя, введите `!twitch sub_only on --user-id=(user id here)`."
            http_err_dash = emoji.cmd_fail + "Произошла ошибка при попытке получить информацию с панели управления TwitchBot: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Live Role - Помощь"
            command_usage.description = "С помощью Live Role вы можете настроить роль, которая будет добавляться к пользователям, когда они начнут стримить. TwitchBot автоматически удалит роль, когда пользователь закончит стрим."
            command_usage.add_field(
                name = "Команды",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Устанавливить роль Live для текущего сервера
                `!twitch live_role filter` - Ограничить Live Role для пользователей с определенной ролью
                `!twitch live_role delete` - Удалить конфигурацию Live Role
                `!twitch live_role view` - Сообщить Вам, какая роль установлена в данный момент
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "Роль не указана Пожалуйста, повторите команду и @упомяните роль."
            not_set_up = emoji.cmd_fail + "Для этого сервера Live Role не установлена . Введите `!twitch live_role set`, чтобы установить её."
            role_not_found = emoji.cmd_fail + "Ни одно имя роли не соответствует этому запросу. Не вставляйте в запрос лишние символы, такие как `<`, `>`, или `@`."
            add_success = emoji.cmd_success + "Пользователи на этом сервере, которые запускаются на Twitch, получат роль: **{role}**. Если вы хотите установить фильтр для Live Role, введите `!twitch live_role filter`."
            del_success = emoji.cmd_success + "Конфигурация Live Role успешно удалена с этого сервера."
            filter_success = emoji.cmd_success + "Фильтр Live Role успешно установлен на этом сервере. Обновление ролей всех участников может занять некоторое время."
            missing_perms_ext = emoji.cmd_fail + "Мне необходимы права **`Manage Roles`**, чтобы сделать это.Если у меня есть разрешение, то обязательно переместите роль с именем`TwitchBot` над ролью, которую вы хотите настроить."
            view_response = "Live Role в настоящее время выдает участникам роль: **{role}**, когда они начинают стрим."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Уведомления о стримах - Помощь"
            command_usage.description = "Уведомления о стримах позволяют настроить сообщение, которое отправляется, когда пользователь Twitch выходит в эфир."
            command_usage.add_field(
                name = "Команды",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Добавить уведомление о стриме для стримера в указанный канал
                `!twitch notif remove <#discord_channel> <streamer_name>` - Удалить уведомление о стриме для стримера в указанном канале
                `!twitch notif list [#discord_channel]` - Показать список уведомлений о стримах для указанного канала
                `!twitch notif formatting` - Показать переменные, которые вы можете вставить в сообщении уведомления о стриме
                """)
            )
            limit_reached = emoji.twitch_icon + "Привет! К сожалению, вы достигли максимального количества уведомлений, которые вы можете добавить на этот сервер. Чтобы добавить больше, вы должны пожертвовать на <https://twitchbot.io/premium>."
            prompt1 = "На каком канале вы хотите получать уведомления? Упомяните или введите название одного из них ниже. *(ответьте в течение 60 секунд)*"
            prompt2 = "Введите название канала Twitch, для которого вы хотите настроить уведомление. *(ответьте в течение 60 секунд)*"
            prompt3 = "ведите пользовательское сообщение, которое вы хотите показывать, когда пользователь выходит в эфир, или введите `default` для сообщения по умолчанию. *(ответьте в течение 180 секунд)*"
            text_channel_not_found = emoji.cmd_fail + "Не удалось найти этот текстовый канал. Выход из команды ..."
            twitch_user_not_found = emoji.cmd_fail + "Этот пользователь Twitch не найден. Выход из команды ..."
            twitch_user_not_found_alt = emoji.cmd_fail + "Этот пользователь Twitch не существует. Убедитесь, что вы не добавляете в имя ничего лишнего (например, `<>`), и не @упоминаете пользователя Discord"
            response_timeout = "*Время ответа истекло.*"
            invalid_data = emoji.cmd_fail + "Неверные данные были отправлены с Twitch:"
            malformed_user = emoji.cmd_fail + "Это не похоже на действительного пользователя Twitch. Имя канала может состояить букв, цифр и подчеркивания."
            default_msg = "<https://twitch.tv/{channel}> сейчас онлайн на Twitch!"
            del_fail = emoji.cmd_fail + "Для этого пользователя не было установлено никаких уведомлений."
            del_success = emoji.cmd_success + "Вы больше не получите никаких уведомлений в {channel} когда {user} выйдет в эфир."
            add_success = emoji.cmd_success + "Добавлено уведомление для {user} в {channel}"
            list_title = "Уведомление о стриме в **#{channel}**"
            list_embed_limit = "Пользовательские сообщения не были включены, так как у Discord есть предел, равный 1024 символам. Сообщение все равно покажется, когда пользователь выйдет в эфир."
            no_notifs = "Уведомления"
            notifications = "Для этого канала не настроено никаких уведомлений о стримах."
            bulk_delete_confirm = "**Вы собираетесь удалить {count} уведомлений в {channel}.** Вы уверены, что хотите это сделать? Ответьте `yes`, если хотите продолжить."
            bulk_delete_success = emoji.cmd_success + "Успешно удалено {count} уведомлений из {channel}."
            command_cancelled = "Команда отменена."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Переменные сообщения уведомления"
            notif_variables.description = "Используйте одну из переменных ниже, чтобы вставить данные в сообщение о стриме."
            notif_variables.add_field(
                name = "Доступное форматирование",
                value = textwrap.dedent("""\
                *`$title$`* - Название стрима
                *`$viewers$`* - Количество людей, которые сейчас смотрят стрим
                *`$game$`* - Игра, в которую в данный момент играет стример
                *`$url$`* - URL канала
                *`$name$`* - Название канала
                *`$everyone$`* - Вставиться упоминание @everyone
                *`$here$`* - Вставиться упоминание @here
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "Вам нужно разрешение: **{permission}**, чтобы сделать это."
            bot_need_perm = emoji.cmd_fail + "Мне нужно разрешение: **{permission}**, чтобы сделать это."
            no_pm = emoji.cmd_fail + "Вы можете использовать эту команду только на сервере."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Команды стримов - Помощь"
            command_usage.add_field(
                name = "команды",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - Получить информацию о стриме пользователя
                `!twitch stream watch <user>` - Смотреть трансляцию Twitch в Discord
                `!twitch stream game <name>` - Посмотрите, как кто-то стримит указанную игру
                `!twitch stream top` - Получить информацию о популярном стриме
                """)
            )
            game_desc = "Смотрите {user}, который играет в {game} для {view_count} зрителей:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Эта игра не найдена."
            game_no_streams = emoji.cmd_fail + "Никто не стримит эту игру."
            live = "Онлайн на Twitch"
            stream_not_found = emoji.cmd_fail + "Этот пользователь не существует или не в сети. Убедитесь, что вы вводите только имя пользователя и ничего лишнего, например `()` или `<>`."
            stream_desc = textwrap.dedent("""\
            Играет в {game} для {view_count} зрителей
            **[Смотреть на Twitch](https://twitch.tv/{channel})** или введите `twitch stream watch {channel}`

            Превью стрима:
            """)
        class Users:
            connections = "Соединений для {user}"
            connected = "Подключен к {account}"
            followers = "Фолловеров"
            following = "Фолловит"
            live = "В настоящее время онлайн"
            playing = "Играет в {game} для {view_count} зрителей"
            not_connected = "Нет соединения"
            not_live = "В настоящее время не в сети"
            no_login_dash = "Этот пользователь не посещал [панель управления TwitchBot](http://dash.twitchbot.io)."
            streamer_id = "ID стримера:"
            views = "Просмотры"
            view_profile = "Посмотреть профиль Twitch"
            unknown = "Неизвестный"
            watch_on_twitch = "Смотреть на Twitch"
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

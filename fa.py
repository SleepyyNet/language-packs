from . import _emoji as emoji
import textwrap
import discord

class English:
    def __init__(self):
        self._lang_name = "Persian"
        self._lang_emoji = ":flag_ir:
        self._translator = "MATIN#4861"
        class Audio:
            no_channel = emoji.cmd_fail + "شما باید در یک کانال صوتی باشید."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "برای ادامه دادن لطفا رأی موافق دهید." 
            need_upvote.description = "برای گوش دادن به استریم ها باید به تویچ بات رای موافق دهید! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "می خواهید از رای موافق گذر کنید؟",
                value = "[تویچ بات پیشرفته](https://twitchbot.io/premium) به شما این اجازه را میدهد تا بدون رأی موافق دادن به استریم گوش کنید."
            )
            please_wait = "لطفا صبر کنید... " + emoji.loading
            user_noexist = emoji.cmd_fail + "کاربر یافت نشد یا در حال استریم نیست. سعی کنید لینک کانال را وارد کنید."
            np_title = "در حال پخش در {channel}"
            np_desc = "{title}\n{viewer_count} بیننده"
            np_leave = "برای توقف استریم '!twitch leave' را بنویسید"
            connection_timeout = emoji.cmd_fail + "خطا: زمان اتصال صوتی به پایان رسید."
            not_streaming = "در حال حاضر هیچ استریمی را در این سرور پخش نمی کنم."
            disconnected = "کانال صوتی را ترک کردم."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "کلیپ ها - راهنما"
            command_usage.add_field(
                name = "دستورات",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - یک کلیپ از کاربر ذکر شده را دریافت میکند
                `!twitch clips trending` - یک کلیپ پر بازدید را دریافت میکند
                `!twitch clips game <game>` - یک کلیپ از بازی مورد نظر را دریافت میکند
                `!twitch clips uservoted` - یکی از معروف ترین کلیپ هایی که کاربران تویچ به آن رأی داده اند را دریافت میکند
                """)
            )
            clip_desc = "{user} را ببینید که {game} بازی می کند.:\n{url}"
            no_clips = emoji.cmd_fail + "کلیپ یافت نشد."
            no_votes = emoji.cmd_fail + "تا کنون هیچکس به کلیپی رأی نداده. بعدا امتحان کنید."
            uservote_clip_desc = "{vote_count} رأی برای این کلیپ توسط {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**، رأی موافق شما با خطا مواجه شده است."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "دستورات تویچ بات"
            e.description = ":warning: __**دستورات را بدون `<>` یا `[]` وارد کنید.**__"
            e.add_field(
                name="عمومی",
                value=textwrap.dedent("""\
                `!twitch help` - راهنمای بات را نمایش می دهد
                `!twitch info` - اطلاعات بات را نمایش می دهد
                `!twitch lang` - زبان بات را تنظیم می کند
                `!twitch invite` - لینکی را نمایش میدهد تا تویچ بات را به سرورتان دعوت کنید
                `!twitch status` - وضعیت API تویچ را نمایش می دهد
                `!twitch ping` - مدت زمان تأخیر بات را نشان می دهد
                """),
                inline=False
            )
            e.add_field(
                name="تویچ",
                value=textwrap.dedent("""\
                `!twitch user <user>` - اطلاعات یک کانال تویچ را دریافت می کند
                `!twitch stream user <user>` - اطلاعات استریم یک کاربر تویچ را دریافت می کند
                `!twitch stream watch <user>` - استریم تویچ را از دیسکورد تماشا کنید
                `!twitch stream game <name>` - استریمی از بازی ذکر شده را تماشا کنید
                `!twitch stream top` - اطلاعات مربوط به یک استریم برتر را دریافت می کند
                `!twitch game <name>` - اطلاعاتی از یک بازی روی تویچ را دریافت میکند
                `!twitch top` - معروفترین بازی های تویچ را دریافت می کند
                """),
                inline=False
            )
            e.add_field(
                name="کلیپ ها",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - کلیپی از کاربر مورد نظر را دریافت می کند
                `!twitch clips trending` - یک کلیپ برتر را دریافت میکند
                `!twitch clips game <game>` - یک کلیپ از بازی مورد نظر را دریافت می کند
                `!twitch clips uservoted` - یکی از معروف ترین کلیپ هایی که کاربران تویچ به آن رأی داده اند را دریافت میکند
                """),
                inline=False
            )
            e.add_field(
                name="اعلانات استریمرها",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - اعلانی را برای استریمر مورد نظر در کانال دیسکورد ذکر شده اضافه می کند
                `!twitch notif remove <#discord_channel> <streamer_name>` - اعلانی را برای استریمر مورد نظر در کانال دیسکورد ذکر شده حذف می کند
                `!twitch notif list [#discord_channel]` - تمامی اعلانات را لیست می کند
                `!twitch notif formatting` - متغیرهایی که می توانید در پیغام اعلان استریمر وارد کنید را نمایش می دهد
                """),
                inline=False
            )
            e.add_field(
                name="رُل (نقش) پخش زنده",
                value=textwrap.dedent("""\
                `!twitch live_role set` - رُل پخش زنده را برای سرور کنونی تنظیم میکند
                `!twitch live_role filter` - رُل پخش زنده را به افراد مورد نظر محدود می کند
                `!twitch live_role delete` - رُل کنونی پخش زنده را حذف می کند
                `!twitch live_role view` - نشان میدهد اکنون چه رُلی برای پخش زنده تنظیم شده است
                """),
                inline=False
            )
            e.add_field(
                name="شنیداری",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - گوش دادن به تویچ استریم مورد نظر در کانال صوتی که در آن حضور دارید
                `!twitch nowplaying` - استریم در حال پخش را نشان می دهد، اگر چیزی در حال پخش باشد.
                `!twitch leave` - کانال صوتی را ترک می کند
                """),
                inline=False
            )
            e.add_field(
                name="وضعیت بازی",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - وضعیت بازیکن مورد نظر را در بازی Overwatch نشان می دهد.
                `!twitch fortnite <pc/psn/xbl> <player>` - وضعیت بازیکن مورد نظر را در بازی Fortnite نشان می دهد.
                """),
                inline=False
            )
            e.add_field(
                name="فیلتر پیام",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - فیلتر محتوای نامناسب را در سطح سرور تنظیم می کند
                `!twitch filter remove` - فیلتر محتوای نامناسب را در سطح سرور حذف می کند
                """),
                inline=False
            )
        class Errors:
            err_report = "لطفا این خطا را به توسعه دهندگان تویچ بات در <https://link.twitchbot.io/support> گزارش دهید. "
            forbidden = emoji.cmd_fail + "مجوز لازم برای انجام این کار را ندارم. "
            not_found = emoji.cmd_fail + "کانال دیسکورد مورد نظر پیدا نشد. مطمئن شوید <> را دور نام کانال قرار ندهید."
            not_started = "تویچ بات در حال شروع به کار است. لطفا چند لحظه صبر کنید."
            check_fail = emoji.cmd_fail + "مجوز لازم را برای اجرای این دستور ندارید"
            cooldown = emoji.cmd_fail + "شما می توانید این دستور را در {time} ثانیه دیگر اجرا کنید."
            conn_closed = emoji.cmd_fail + "اتصال صوتی بسته شد. دلیل: `{reason}`"
            missing_arg = emoji.cmd_fail + "پارامتر `{param}` را فراموش کردید."
            too_many_requests = emoji.cmd_fail + "سرورهای شخص ثالث مشکلی در ارتباط دارند. لطفا بعدا امتحان کنید."
        class Filter:
            cmd_usage = "`!twitch help filter` را وارد کنید تا استفاده این دستور را ببینید."
            need_donate = "تنها کاربران تویچ بات پیشرفته می توانند از این دستور استفاده کنند. اطلاعات بیشتر در: <https://twitchbot.io/premium>"
            invalid_sensitivity = "حساسیت باید بین 60 و 85 باشد."
            add_success = emoji.cmd_success + "فیلتر محتوای نامناسب برای این سرور با موفقیت اعمال شد."
            no_filter = emoji.cmd_fail + "هیچ فیلتر محتوای نامناسبی برای این سرور وجود ندارد."
            del_success = emoji.cmd_success + "فیلتر محتوای نامناسب با موفقیت حذف شد."
        class Games:
            no_results = emoji.cmd_fail + "نتیجه ای یافت نشد."
            no_stats_overwatch = emoji.cmd_fail + "اطلاعاتی مربوط به این بازیکن یافت نشد. اگر پروفایل شما خصوصی است، نمیتوانید اطلاعاتی را مشاهده کنید تا زمانی که پروفایلتان عمومی ی شود. لطفا این مراحل را دنبال کنید <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> تا پروفیلتان عمومی شود."
            no_stats_fortnite = emoji.cmd_fail + "بازیکن پیدا نشد. املا نام کاربری را چک کنید."
            view_streams = "نمایش استریم ها"
            top_games = emoji.twitch_icon + "بازی های برتر"
            top_games_desc = "{view_count} بیننده • {channel_count} کانال در حال استریم"
            invalid_battletag = "لطفا بتل تگ خودر را به این فرم وارد کنید: `name#id`."
            invalid_platform = "پلتفرم را از بین `pc`، `psn`، یا `xbl` انتخاب کنید."
            incomplete_data = "اطلاعات پروفیل شما ناقص است. اگر پروفابل شما خصوصی است, این مراحل را دنبال کنید <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> تا آن را عمومی کنید و اطلاعات پروفیلتان را ببینید."
            incomplete_data_short = "برخی اطلاعات ناقص است."
            generic_error = emoji.cmd_fail + "خطا رخ داد:"
            powered_by_overwatch = "طراحی شده توسط owapi.net"
            powered_by_fortnite = "طراحی شده توسط fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**راهنمای تویچ بات**"
            e.add_field(
                name="دستورات",
                value="تویچ بات به دستوراتی که با `twitch` یا `!twitch` شروع شوند پاسخ میدهد.`!twitch commands` را بنویسید تا تمام دستورات قابل اجرا را ببینید.",
                inline=False
            )
            e.add_field(
                name="پشتیبانی",
                value="اگر در خصوص تویچ بات نیاز به کمک دارید، به [support center](https://support.twitchbot.io) سر بزنید یا به [support server](https://discord.gg/UNYzJqV) ملحق شوید.",
                inline=False
            )
            e.add_field(
                name="وب سایت",
                value="می توانید اطلاعات بیشتری در مورد تویچ بات را در https://twitchbot.io ببینید",
                inline=False
            )
            e.add_field(
                name="تویچ بات پیشرفته",
                value="از توسعه تویچ بات حمایت کنید و به قابلیت های کاربردی بیشتری دسترسی پیدا کنید فقط با ماهی 5 دلار. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="رقابت رأی موافق",
                value="هر ماهه به سه نفر اول کسانی که بیشترین رأی موفق را می دهند تویچ بات پیشرفته اهدا می شود. [این جا رأی موافق دهید](https://discordbots.org/bot/twitch/vote) و [جدول امتیازات را از اینجا ببینید](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="درباره",
                value="تویچ بات توسط [Akira#4587](https://disgd.pw) ساخته شده و از discord.py استفاده میکند. برای دیدن دیگر همکاران دستور `twitch info` را وارد کنید.",
                inline=False
            )
            e.add_field(
                name="لینک های دیگر",
                value="[پرسش های متداول](https://twitchbot.io/faq) · [داشبورد](http://dash.twitchbot.io) · [رأی موافق](https://discordbots.org/bot/twitch/vote) · [دعوت بات به سرور](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [وبلاگ](https://medium.com/twitchbot)",
                inline=False
            )
            ###___________________________________ Translate Flag
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

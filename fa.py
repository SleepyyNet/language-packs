from . import _emoji as emoji
import textwrap
import discord

class Persian:
    def __init__(self):
        self._lang_name = "Persian"
        self._lang_emoji = ":flag_ir:"
        self._translator = "MATIN#4861"
        class Audio:
            no_channel = emoji.cmd_fail + "شما باید به یک کانال صوتی متصل باشید."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "برای ادامه دادن لطفا رأی موافق دهید."
            need_upvote.description = "برای گوش دادن به استریم ها باید به تویچ بات رأی موافق دهید! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "می خواهید از رأی موافق گذر کنید؟",
                value = "[تویچ بات پیشرفته](https://twitchbot.io/premium) به شما این اجازه را میدهد تا بدون رأی موافق دادن به استریم گوش کنید."
            )
            please_wait = "لطفا صبر کنید... " + emoji.loading
            user_noexist = emoji.cmd_fail + "کاربر یافت نشد یا در حال استریم نیست. سعی کنید لینک کانال را وارد کنید."
            np_title = "در حال پخش در {channel}"
            np_desc = "{title}\n{viewer_count} بیننده"
            np_leave = "برای توقف استریم بنویسید: '!twitch leave'"
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
                `!twitch clips uservoted` - یکی از کلیپ های معروف که کاربران تویچ به آن رأی داده اند را دریافت میکند
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
                `!twitch ping` - مدت زمان تأخیر (پینگ) بات را نشان می دهد
                """),
                inline=False
            )
            e.add_field(
                name="تویچ",
                value=textwrap.dedent("""\
                `!twitch user <user>` - اطلاعات یک کانال تویچ را دریافت می کند
                `!twitch stream user <user>` - اطلاعات استریم کاربر مورد نظر تویچ را دریافت می کند
                `!twitch stream watch <user>` - استریم تویچ را از دیسکورد تماشا کنید
                `!twitch stream game <name>` - استریمی از بازی ذکر شده را تماشا کنید
                `!twitch stream top` - اطلاعات مربوط به یک استریم برتر را دریافت می کند
                `!twitch game <name>` - اطلاعاتی از بازی مورد نظر روی تویچ را دریافت میکند
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
                `!twitch clips uservoted` - یکی از کلیپ های معروف که کاربران تویچ به آن رأی داده اند را دریافت میکند
                """),
                inline=False
            )
            e.add_field(
                name="اعلانات استریمرها",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - اعلانی را برای استریمر مورد نظر در کانال متنی دیسکورد ذکر شده اضافه می کند
                `!twitch notif remove <#discord_channel> <streamer_name>` - اعلانی را برای استریمر مورد نظر در کانال متنی دیسکورد ذکر شده حذف می کند
                `!twitch notif list [#discord_channel]` - تمامی اعلانات را لیست می کند
                `!twitch notif formatting` - متغیرهایی که می توانید در پیغام اعلان استریمر وارد کنید را نمایش می دهد
                """),
                inline=False
            )
            e.add_field(
                name="رُل (نقش) لایو (پخش زنده)",
                value=textwrap.dedent("""\
                `!twitch live_role set` - رُل لایو را برای سرور کنونی تنظیم میکند
                `!twitch live_role filter` - رُل لایو را به افراد مورد نظر محدود می کند
                `!twitch live_role delete` - رُل کنونی لایو را حذف می کند
                `!twitch live_role view` - نشان میدهد اکنون چه رُلی برای لایو تنظیم شده است
                """),
                inline=False
            )
            e.add_field(
                name="شنیداری",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - گوش دادن به استریم تویچ مورد نظر در کانال صوتی که در آن حضور دارید
                `!twitch nowplaying` - استریم در حال پخش را نشان می دهد، اگر چیزی در حال پخش باشد
                `!twitch leave` - کانال صوتی را ترک می کند
                """),
                inline=False
            )
            e.add_field(
                name="وضعیت بازیکن ها",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - وضعیت بازیکن مورد نظر را در بازی Overwatch نشان می دهد.
                `!twitch fortnite <pc/psn/xbl> <player>` - وضعیت بازیکن مورد نظر را در بازی Fortnite نشان می دهد.
                """),
                inline=False
            )
            e.add_field(
                name="فیلتر پیام ها",
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
            incomplete_data = "اطلاعات پروفیل شما ناقص است. اگر پروفابل شما خصوصی است، این مراحل را دنبال کنید <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> تا آن را عمومی کنید و اطلاعات پروفیلتان را ببینید."
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
                value="اگر در خصوص تویچ بات نیاز به کمک دارید، به [مرکز پشتیبانی](https://support.twitchbot.io) سر بزنید یا به [سرور پشتیبانی](https://discord.gg/UNYzJqV) ملحق شوید.",
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
        class General:
            avail_lang_title = "ترجمه های موجود"
            avail_lang_setmsg = "برای تنظیم زبان تویچ، دستور !twitch lang <language> را وارد کنید."
            stats_embed_title = emoji.twitch_icon + "وضعیت تویچ بات"
            stats_uptime = "مدت بیداری (آپ تایم)"
            stats_usage = "استفاده"
            stats_version = "نسخه"
            stats_shardinfo = "Shard اطلاعات"
            stats_system = "سیستم"
            stats_developer = "توسعه دهنده"
            stats_patrons = "مشتری ها"
            stats_links = "لینک ها"
            stats_links_desc = textwrap.dedent("""\
            **·** وب سایت: https://twitchbot.io
            **·** دیسکورد: https://discord.gg/UNYzJqV
            **·** رأی موافق: https://discordbots.org/bot/twitch/vote
            **·** کمک مالی: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**،می توانید مرا با این لینک به سرور خود دعوت کنید: <https://link.twitchbot.io/invite>"
            invite_msg2 = "کمک می خواهید؟ به سرور پشتیبانی ملحق شوید:  <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "وضعیت تویچ"
            status_cs = "وضعیت کنونی: `{status}`"
            lang_current = "زبان کنونی تویچ بات برای شما **{lang}** است. برای تغییر آن دستور `!twitch lang <lang>` یا `!twitch lang help` را وارد کنید."
            lang_unavail = emoji.cmd_fail + "ترجمه مورد نظر موجود نیست. برای نمایش ترجمه های موجود بنویسید: `!twitch lang help`."
            lang_set = emoji.cmd_success + "زبان **{lang}** با موفقیت برای سرور شما تنظیم شد."
        class Guild:
            submode_command_usage = "بنویسید `!twitch help sub_only` تا استفاده دستور را ببینبد."
            submode_success = emoji.cmd_success + "حالت فقط-مشترکین برای این سرور فعال شد. کاربران جدید باید مشترک کانال {channel} باشند تا بتوانند ملحق شوند. تویچ بات سعی خواهد کرد غیر-مشترکانی که سعی میکنند ملحق شوند را خارج کند و به آنها پیام دهد. نکته: کاربران فعلی خارج نخواهند شد."
            submode_kick = "این سرور در حالت فقط-مشترکین می باشد. برای ملحق شدن، شما باید مشترک کانال {} باشید.\nبرای اتصال حساب تویچ به تویچ بات، مراجعه کنید به <https://dash.twitchbot.io> و دکمه 'Link Account' را بزنید."
            submode_kick_audit_log = "این سرور در حالت فقط-مشترکین می باشد. برای خاموش کردن این حالت دستور '!twitch sub_only off' را وارد کنید."
            submode_del_success = emoji.cmd_success + "حالت فقط-مشترکین غیر فعال شد."
            user_not_in_guild = emoji.cmd_fail + "کاربر مورد نظر در این سرور وجود ندارد."
            no_login_dash = emoji.cmd_fail + "{user} هنوز وارد داشبورد تویچ بات خود نشده است. برای دریافت کانال از کاربری دیگر بنویسید `!twitch sub_only on --user-id=(user id here)`."
            no_link_dash = emoji.cmd_fail + "{user} هنوز اکانت تویچ خود را به داشبورد تویچ بات متصل نکرده است. برای دریافت کانال از کاربری دیگر بنویسید `!twitch sub_only on --user-id=(user id here)`."
            http_err_dash = emoji.cmd_fail + "هنگام گرفتن اطلاعات از داشبورد تویچ بات خطایی رخ داد: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "رُل (نقش) لایو (پخش زنده) - راهنما"
            command_usage.description = "به کمک رُل لایو، میتوانید رُلی را تنظیم کنید تا زمانی که یکی از اعضای سرور شما در تویچ لایو شد، این رُل به او تعلق گیرد. زمانی که شخص به استریم پایان دهد، رُل از او بر داشته می شود."
            command_usage.add_field(
                name = "دستورات",
                value = textwrap.dedent("""\
                `!twitch live_role set` - رُل لایو را برای این سرور تنظیم می کند
                `!twitch live_role filter` - رُل لایو را به افرادی با رُل خواص دیگری محدود می کند
                `!twitch live_role delete` - تنظیمات رُل لایو را حذف می کند
                `!twitch live_role view` - رُل لایو کنونی را نمایش می دهد
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "رُلی مشخص نشده. لطفا دستور مورد نظر را دوباره اجرا کنید و رُل @mention را ذکر کنید."
            not_set_up = emoji.cmd_fail + "هیچ رُل لایوی در این سرور تنظیم نشده است. بنویسید `!twitch live_role set` تا آن را تنظیم کنید."
            role_not_found = emoji.cmd_fail + "هیچ رُلی با این جست و جو پیدا نشد. از کاراکتر اضافه ای همچون `<`، `>`، یا `@` استفاده نکنید."
            add_success = emoji.cmd_success + "از این پس زمانی که اعضای این سرور استریم کنند رُل **{role}** به آنها داده می شود. اگر می خواهید این تغییر صرفا روی رُل خواصی اعمال شود دستور `!twitch live_role filter` را اجرا کنید."
            del_success = emoji.cmd_success + "تنظیمات رُل لایو با موفقیت از این سرور حذف شد."
            filter_success = emoji.cmd_success + "فیلتر رُل لایو با موفقیت تنظیم شد. ممکن است چند لحظه تا بروز شدن رُل همه افراد طول بکشد."
            missing_perms_ext = emoji.cmd_fail + "من به مجوز **`Manage Roles`** برای انجام این کار نیاز دارم. اگر مطمئن هستید که این اجازه را دارم، مطمئن شوید رُلی که به من اختصاص داده اید (TwitchBot( بالا تر از رُل لایو است."
            view_response = "در حال حاضر رُل لایو تنظیم شده است تا زمانی که استریمرها لایو شوند رُل **{role}** به آنها داده شود."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "اعلانات استریمرها - راهنما"
            command_usage.description = "اعلانات استرمرها به شما این امکان را می دهد زمانی که یک کاربر (تعیین شده) تویچ لایو شود، اعلانی در قالب پیامی قابل شخصی سازی در کانال متنی تعیین شده ارسال شود."
            command_usage.add_field(
                name = "دستورات",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - اعلانی را برای استریمر مورد نظر در کانال متنی دیسکورد ذکر شده اضافه می کند
                `!twitch notif remove <#discord_channel> <streamer_name>` - اعلانی را برای استریمر مورد نظر از کانال متنی دیسکورد ذکر شده حذف می کند
                `!twitch notif list [#discord_channel]` - تمامی اعلانات را لیست می کند
                `!twitch notif formatting` - متغیرهایی که می توانید در پیغام اعلان استریمر وارد کنید را نمایش می دهد
                """)
            )
            limit_reached = emoji.twitch_icon + "درود! متاسفانه به سقف تعداد اعلاناتی که می توانید اضافه کنید رسیده اید. برای اضافه کردن بی نهایت اعلان میتوانید نسخه پیشرفته تویچ بات را خریداری کنید."
            prompt1 = "می خواهید در کدام کانال متنی اعلان نمایش داده شود؟ در پایین نام آن را بنویسید یا مورد خطاب قرار دهید.*(تا 60 ثانیه دیگر پاسخ دهید)*"
            prompt2 = "کانال تویچی که می خواهید اعلان در مورد آن باشد را نام ببرید. *(تا 60 ثانیه دیگر پاسخ دهید)*"
            prompt3 = "پیغام دلخواهی که می خواهید هنگام لایو شدن استریمر نمایش داده شود را بنویسید. یا بنویسید `default` تا پیغام پیش فرض نمایش داده شود. *(تا 60 ثانیه دیگر پاسخ دهید)*"
            text_channel_not_found = emoji.cmd_fail + "کانال متنی مورد نظر یافت نشد. خروج از دستور..."
            twitch_user_not_found = emoji.cmd_fail + "کاربر(کانال) مورد نظر تویچ یافت نشد. خروج از دستور..."
            twitch_user_not_found_alt = emoji.cmd_fail + "کاربر مورد نظر تویچ یافت نشد. مطمئن شوید از کاراکتر اضافه ای همچون `<>` استفاده نمی کنید، و کاربر دیسکوردی را مورد خطاب )@mention) قرار نمی دهید."
            response_timeout = "*زمان پاسخ گویی به پایان رسید.*"
            invalid_data = emoji.cmd_fail + "داده ارسال شده توسط تویچ نامعتبر است:"
            malformed_user = emoji.cmd_fail + "بنظر می رسد این نامی معتبر برای کاربران تویچ نیست. تنها میتوانید از _، حروف، و اعداد استفاده کنید."
            default_msg = "<https://twitch.tv/{channel}> هم اکنون استریم می کند!"
            del_fail = emoji.cmd_fail + "اعلانی برای این کاربر تنظیم نشده است."
            del_success = emoji.cmd_success + "از این پس اعلانی در کانال {channel} برای کاربر {user} پخش نخواهد شد."
            add_success = emoji.cmd_success + "اعلانی برای کاربر {user} در کانال {channel} اضافه شد."
            list_title = "اعلان های استریمرها برای کانال **#{channel}**"
            list_embed_limit = "بدلیل محدودیت تعداد کاراکترها (1024( پیغام دلخواه شمااعمال نشد. همچنان اعلان نمایش داده خواهد شد."
            no_notifs = "هیچ اعلانی در این کانال تنظیم نشده است."
            notifications = "اعلان ها"
            bulk_delete_confirm = "**شما در حال حذف تعداد {count} اعلان در کانال {channel} هستید.** آیا مطمئن به انجام این کار می باشید؟ بنویسید `yes` اگر می خواهید ادامه دهید."
            bulk_delete_success = emoji.cmd_success + "تعداد {count} اعلان از کانال {channel} حذف شد."
            command_cancelled = "دستور متوقف شد."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "متغیرهای پیام اعلان"
            notif_variables.description = "برای استفاده از برخی داده استریم، از متغیرهای زیر استفاده کنید."
            notif_variables.add_field(
                name = "قالب های موجود",
                value = textwrap.dedent("""\
                *`$title$`* - عنوان استریم
                *`$viewers$`* - تعداد بیننده های استریم در آن لحظه
                *`$game$`* - بازی که استریمر می کند
                *`$url$`* - آدرس اینترنتی کانال استریم
                *`$name$`* - نام کانال استریم
                *`$everyone$`* - @everyone را مخاطب قرار می دهد.
                *`$here$`* - @here را مخاطب قرار می دهد.
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "شما به مجوز **{permission}** برای انجام این کار نیاز دارید."
            bot_need_perm = emoji.cmd_fail + "من به مجوز **{permission}** برای انجام این کار نیاز دارم."
            no_pm = emoji.cmd_fail + "شما می توانید این دستور را تنها در سرور اجرا کنید."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "دستورات استریم - راهنما"
            command_usage.add_field(
                name = "دستورات",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - اطلاعات استریم یک کاربر تویچ را دریافت می کند
                `!twitch stream watch <user>` - استریم تویچ را از دیسکورد تماشا کنید
                `!twitch stream game <name>` - استریمی از بازی ذکر شده را تماشا کنید
                `!twitch stream top` - اطلاعاتی از یک استریم برتر را دریافت می کند
                """)
            )
            game_desc = "{user} را ببینید که {game} بازی می کند و {view_count} بیننده دارد:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "بازی پیدا نشد."
            game_no_streams = emoji.cmd_fail + "کسی این بازی را استریم نمی کند."
            live = "زنده بر روی تویچ"
            stream_not_found = emoji.cmd_fail + "چنین کاربری وجود ندارد یا آنلاین نیست. مطمئن شوید از کاراکتر های اضافی همچون `()` یا `<>` در نام کاربر استفاده نکنید."
            stream_desc = textwrap.dedent("""\
            {game} بازی می کند برای {view_count} بیننده
            **[از تویچ ببینید](https://twitch.tv/{channel})** یا بنویسید `twitch stream watch {channel}`

            پیش نمایش استریم:
            """)
        class Users:
            connections = "اتصالات برای کاربر {user}"
            connected = "متصل شد به {account}"
            followers = "دنبال کننده ها"
            following = "دنبال می کنند"
            live = "پخش زنده"
            playing = "در حال بازی {game} برای {view_count} بیننده"
            not_connected = "متصل نشد"
            not_live = "آفلاین"
            no_login_dash = "این کاربر از [داشبورد تویچ](http://dash.twitchbot.io) بازدید نکرده."
            streamer_id = "ID استریمر:"
            views = "تعداد نمایش ها"
            view_profile = "نمایش پروفایل تویچ"
            unknown = "ناشناس"
            watch_on_twitch = "از تویچ ببینید"
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

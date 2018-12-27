from . import _emoji as emoji
import textwrap
import discord

class Chinese:
    def __init__(self):
        self._lang_name = "中文(简体)"
        self._lang_emoji = ":flag_cn"
        self._translator = "Dexmio#8239"
        class Audio:
            no_channel = emoji.cmd_fail + "您必须加入语音频道。"
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "请投票以继续"
            need_upvote.description = "您需要投TwitchBot一票，才能继续收听直播 **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "想要跳过投票？",
                value = "[TwitchBot Premium](https://twitchbot.io/premium)让你在听直播时不需要再一直投票。"
            )
            please_wait = "请稍后... " + emoji.loading
            user_noexist = emoji.cmd_fail + "这位用户不存在或目前没在直播。请在频道入链结。"
            np_title = "正在播放 {channel}"
            np_desc = "{title}\n{viewer_count} 正在观看"
            np_leave = "输入 '!twitch leave' 来结束直播"
            connection_timeout = emoji.cmd_fail + "语音连线逾时"
            not_streaming = "我现在没在此服务器直播任何东西。"
            disconnected = "已离开语音频道。"
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Clips - Help"
            command_usage.add_field(
                name = "指令",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - 从Twitch用户取得特定的视频
                `!twitch clips trending` - 取得热门视频
                `!twitch clips game <game>` - 取得特定游戏的视频
                `!twitch clips uservoted` - 寻找TwitchBot用户们投票出最热门的视频
                """)
            )
            clip_desc = "查看 {user} 游玩 {game}:\n{url}"
            no_clips = emoji.cmd_fail + "找不到任何相关视频。"
            no_votes = emoji.cmd_fail + "还没有人对任何视频投票。请等等再回来。"
            uservote_clip_desc = "此部视频有{vote_count}票，由{user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, 你的票无法送达。"
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "TwitchBot 指令"
            e.description = ":warning: __**请勿在指令中输入 `<>` 或 `[]`。**__"
            e.add_field(
                name="一般",
                value=textwrap.dedent("""\
                `!twitch help` - 显示机器人帮助
                `!twitch info` - 显示机器人资讯
                `!twitch lang` - 设定使用语言
                `!twitch invite` - 显示TwitchBot服务器邀请链结
                `!twitch status` - 显示Twitch API 状态
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - 取得Twitch 频道资讯
                `!twitch stream user <user>` - 取得用户直播资讯
                `!twitch stream watch <user>` - 在Discord上观看Twitch直播
                `!twitch stream game <name>` - 观看某人游玩特定的游戏直播
                `!twitch stream top` - 取得最多人观看的直播资讯
                `!twitch game <name>` - 取得Twitch游戏资讯
                `!twitch top` - 取得最热门的Twitch游戏
                """),
                inline=False
            )
            e.add_field(
                name="视频",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - 从Twitch用户取得特定的视频
                `!twitch clips trending` - 取得热门视频
                `!twitch clips game <game>` - 取得特定游戏的影片
                `!twitch clips uservoted` - 寻找TwitchBot用户们投票出最热门的视频
                """),
                inline=False
            )
            e.add_field(
                name="直播主通知",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - 在特定的频道新增一个直播主通知给直播主。
                `!twitch notif remove <#discord_channel> <streamer_name>` - 在特定的频道移除一个给直播主的直播主通知。
                `!twitch notif list [#discord_channel]` - 在特定的频道列出直播主通知
                `!twitch notif formatting` - 显示可新增至直播主通知的变数
                """),
                inline=False
            )
            e.add_field(
                name="直播身分",
                value=textwrap.dedent("""\
                `!twitch live_role set` - 在此服务器上设置一个直播身分
                `!twitch live_role filter` - 限制有直播身分的用户特定的身分
                `!twitch live_role delete` - 删除直播身分的设置
                `!twitch live_role view` - 告诉你现在有那些身分已设置
                """),
                inline=False
            )
            e.add_field(
                name="音讯",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - 在现在的语音频道收听直播
                `!twitch nowplaying` - 显示现在正在播放的直播，如果有的
                `!twitch leave` - 离开语音频道
                """),
                inline=False
            )
            e.add_field(
                name="游戏状态",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - 显示守望先锋玩家状态
                `!twitch fortnite <pc/psn/xbl> <player>` - 显示Fortnite玩家状态
                """),
                inline=False
            )
            e.add_field(
                name="讯息过滤器",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - 设定服务器端病毒过滤器
                `!twitch filter remove` - 移除服务器端病毒过滤器
                """),
                inline=False
            )
        class Errors:
            err_report = "请至<https://link.twitchbot.io/support>回报此错误给开发者。"
            forbidden = emoji.cmd_fail + "我没有正确的权限这么做。"
            not_found = emoji.cmd_fail + "找不到此Discord频道。请确认当你输入`#mention`时没有包含<>。"
            not_started = "TwitchBot还正在启动！请等个几分钟后再试。"
            check_fail = emoji.cmd_fail + "你没有权限使用此指令。"
            cooldown = emoji.cmd_fail + "你可以在{time}秒后再次使用此指令。"
            conn_closed = emoji.cmd_fail + "语音连线已结束。原因： `{reason}`"
            missing_arg = emoji.cmd_fail + "你失去了 `{param}`参数。"
            too_many_requests = emoji.cmd_fail + "第三方服务器在处理我们的要求时出了问题。请稍后在试。"
        class Filter:
            cmd_usage = "输入`!twitch help filter`来查看如可使用指令。"
            need_donate = "只有TwitchBot Premium成员能使用此指令。了解更多： <https://twitchbot.io/premium>"
            invalid_sensitivity = "灵敏度必须在85至60之间。"
            add_success = emoji.cmd_success + "成功在此服务器设置病毒过滤器。"
            no_filter = emoji.cmd_fail + "此服务器没有任何病毒过滤器。"
            del_success = emoji.cmd_success + "成功移除此服务器的病毒过滤器。"
        class Games:
            no_results = emoji.cmd_fail + "没有找到任何结果。"
            no_stats_overwatch = emoji.cmd_fail + "找不到任何此玩家的状态。如果您的个人档案为私人，您将无法看到玩家状态除非您设为公开。请至<https://dotesports.com/overwatch/news/ow-public-private-profile-25347>按照步骤设定您的个人档案至公开。"
            no_stats_fortnite = emoji.cmd_fail + "找不到此玩家。请检察您的拼字或尝试不同平台。"
            view_streams = "观看直播"
            top_games = emoji.twitch_icon + "游戏列表"
            top_games_desc = "{view_count}人观看 • {channel_count}个频道正在直播"
            invalid_battletag = "请依`name#id`格式输入您的 Battletag。"
            invalid_platform = "平台必须是`pc`、`psn`或`xbl`。"
            incomplete_data = "您的个人档案资讯并不完整。您的个人档案仅限私人，请至<https://dotesports.com/overwatch/news/ow-public-private-profile-25347>按照步骤设定您的个人档案至公开。"
            incomplete_data_short = "某些资讯可能遗失或不完整"
            generic_error = emoji.cmd_fail + "错误发生："
            powered_by_overwatch = "由owapi.net所有"
            powered_by_fortnite = "由fortnitetracker.com所有"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot支援**"
            e.add_field(
                name="指令",
                value="TwitchBot支援的指令前缀为`twitch`或`!twitch`。输入`!twitch commands`来查所有能使用指令。",
                inline=False
            )
            e.add_field(
                name="支援",
                value="如果您需要TwitchBot的帮忙，您可以拜访[支援中心](https://support.twitchbot.io)或加入[支援服务器](https://discord.gg/UNYzJqV)。",
                inline=False
            )
            e.add_field(
                name="网站",
                value="您可至https://twitchbot.io查看TwitchBot资讯。",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="用每月$5.00 USD支持TwitchBot开发者并取得好用又有趣的功能。https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="投票竞赛",
                name="我们正在免费送TwitchBot Premium给每月投最多票前三位用户。[这里投票](https://discordbots.org/bot/twitch/vote)以及[查看排行榜](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="关于",
                value="TwitchBot是由[Akira#4587](https://disgd.pw)使用discord.py制作。查看其他贡献者，输入`twitch info`。",
                inline=False
            )
            e.add_field(
                name="其他连结",
                value="[问与答](https://twitchbot.io/faq) · [仪表版](http://dash.twitchbot.io) · [投票](https://discordbots.org/bot/twitch/vote) · [邀请](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [部落格](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "可使用语言"
            avail_lang_setmsg = "设置TwitchBot使用语言，请输入!twitch lang <language>。"
            stats_embed_title = emoji.twitch_icon + "TwitchBot状态"
            stats_uptime = "运行时间"
            stats_usage = "使用量"
            stats_version = "版本"
            stats_shardinfo = "破碎资讯"
            stats_system = "系统"
            stats_developer = "开发者"
            stats_patrons = "赞助人"
            stats_links = "链结"
            stats_links_desc = textwrap.dedent("""\
            **·** Website: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Upvote: https://discordbots.org/bot/twitch/vote
            **·** Donate: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**，您可以使用此链结邀请我至您的服务器：<https://link.twitchbot.io/invite>"
            invite_msg2 = "需要帮忙吗？加入支援服务器：<https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Twitch状态"
            status_cs = "目前状态： `{status}`"
            lang_current = "您现在所使用的TwitchBot语言是 **{lang}**。请输入 `!twitch lang <lang>`或`!twitch lang help`来更改您的语言。"
            lang_unavail = emoji.cmd_fail + "我们尚未翻译此语言，输入 `!twitch lang help`来查看可使用的语言。"
            lang_set = emoji.cmd_success + "成功设置您的TwitchBot语言至**{lang}**。"
        class Guild:
            submode_command_usage = "输入`!twitch help sub_only`来查看如何使用指令。"
            submode_success = emoji.cmd_success + "已在此服务器上启动订阅者模式。新的用户必须订阅才能加入{channel}。TwitchBot会尝试私讯想加入的非订阅者并踢除他们。注意：现存的会员不会被剔除。"
            submode_kick = "此服务器只开放给订阅者。您必须订阅，才能够加入。{}.\nTo 将您的Twitch帐号与TwitchBot连结，请至<https://dash.twitchbot.io> 点击Twitch下方的'Link Account'。"
            submode_kick_audit_log = "此服务器已启动订阅者模式。请输入'!twitch sub_only off'来关闭此功能。"
            submode_del_success = emoji.cmd_success + "已关闭此服务器订阅者模式。"
            user_not_in_guild = emoji.cmd_fail + "此玩家不在这服务器上。"
            no_login_dash = emoji.cmd_fail + "{user} 尚未登入TwitchBot仪表板。获取其他用户的频道，请输入 `!twitch sub_only on --user-id=(user id here)`。"
            no_link_dash = emoji.cmd_fail + "{user} 尚未将他的Twitch帐号与TwitchBot仪表板做链结。获取其他用户的频道，请输入 `!twitch sub_only on --user-id=(user id here)`。"
            http_err_dash = emoji.cmd_fail + "尝试从TwitchBot仪表板取得资讯时发生了错误： {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "直播身分 - 支援"
            command_usage.description = "直播身分，当用户在直播时会给他们的个身分。当他们停止直播时Twitchbot会自动从他们身上移除此身分。"
            command_usage.add_field(
                name = "指令",
                value = textwrap.dedent("""\
                `!twitch live_role set` - 在所这服务器上设置一个直播身分
                `!twitch live_role filter` - 限制有直播身分的使用者特定的身分
                `!twitch live_role delete` - 删除直播身分的设置
                `!twitch live_role view` - 告诉你现在有那些身分已设置
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "没有举出明确身分。请重新输入指令并提及 @mention 一个身分。"
            not_set_up = emoji.cmd_fail + "此服务器没有设置任何直播身分。请输入`!twitch live_role set`来设定一个。"
            role_not_found = emoji.cmd_fail + "找不到此身分。请勿输入不必要的字符，像是 `<`, `>` 或 `@`。"
            add_success = emoji.cmd_success + "在此服务器上直播的用户会得到 **{role}** 身分。如果您想要设置一个过滤器给此身分，请输入 `!twitch live_role filter`。"
            del_success = emoji.cmd_success + "已成功的从此服务器上移出直播者身分。"
            filter_success = emoji.cmd_success + "已成功的在此服务器上设置直播主过滤器。可能会需要花一点时间更新所有用户的身分。"
            missing_perms_ext = emoji.cmd_fail + "我需要**`管理身分组`**权限才能这么做。如果我已拥有该权限，请确保身分名称`TwitchBot`是在你想要设置的身分上方。"
            view_response = "直播身分**{role}**已设置完成，会给予正在直播的用户们。"
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "直播者通知 - 支援"
            command_usage.description = "当有Twitch用户开始直播时，直播主通知能让你客制化您的通知讯息。"
            command_usage.add_field(
                name = "指令",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - 在特定的频道新增一个直播者通知给直播主。
                `!twitch notif remove <#discord_channel> <streamer_name>` - 在特定的频道移除一个直播主通知给直播主。
                `!twitch notif list [#discord_channel]` - 在特定的频道列出直播主通知
                `!twitch notif formatting` - 显示可新增至直播主通知的变数
                """)
            )
            limit_reached = emoji.twitch_icon + "嗨，您好！不幸的是您已经达到设置通知讯息的上限。如果想要设置更多，您需要至以下网址<https://twitchbot.io/premium>来赞助我们。"
            prompt1 = "您想要在那个频道显示您的通知讯息？在下方提及或输入频道名。 *(请在60秒内回应)*"
            prompt2 = "请输入您想要获得通知的Twitch频道名称。 *(请在60秒内回应)*"
            prompt3 = "输入您想要显示在通知的讯息，或输入`default`使用预设讯息。 *(请在180秒内回应)*"
            text_channel_not_found = emoji.cmd_fail + "找不到文字频道。结束设定..."
            twitch_user_not_found = emoji.cmd_fail + "找不到该Twitch用户。结束设定..."
            twitch_user_not_found_alt = emoji.cmd_fail + "该Twitch用户不存在。请确认您没有输入任何额外的字符，像是(such as `<>`)，且没有提及 @mentioning 任何Discord用户。"
            response_timeout = "*回复时间逾时*"
            invalid_data = emoji.cmd_fail + "Twitch发送了无效的数据："
            malformed_user = emoji.cmd_fail + "这看起来不像是有效的Twitch用户。您只能包含下划线，字母和数字。"
            default_msg = "<https://twitch.tv/{channel}>现在正在Twitch上直播！"
            del_fail = emoji.cmd_fail + "没有设置有关这位用户的通知。"
            del_success = emoji.cmd_success + "您不会在{channel}收到任有关{user}的通知。"
            add_success = emoji.cmd_success + "帮{user}在{channel}设置通知讯息。"
            list_title = "**#{channel}**的直播者通知"
            list_embed_limit = "客制化讯息不能包含嵌入讯息，因为Discord有1024个字符限制。使用者开直播时他们还是会显示。"
            no_notifs = "此频道并没有设置任何的直播者通知。"
            notifications = "通知"
            bulk_delete_confirm = "**您将要删除在{channel}的{count}则通知。**您确定您要这么做？回复`yes`如果您确定要这么做。"
            bulk_delete_success = emoji.cmd_success + "成功删除在{channel}的{count}则通知。"
            command_cancelled = "已取消的指令"
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "通知讯息变数"
            notif_variables.description = "插入以下变数讯息到您的直播通知讯息。"
            notif_variables.add_field(
                name = "可用的格式",
                value = textwrap.dedent("""\
                *`$title$`* - 直播标题
                *`$viewers$`* - 直播观看人数
                *`$game$`* - 直播者目前正在玩的游戏
                *`$url$`* - 频道的URL
                *`$name$`* - 频道名称
                *`$everyone$`* - 插入提及所有人 @everyone 
                *`$here$`* - 插入提及这里 @here 
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "您需要**{permission}**权限才能这么做。"
            bot_need_perm = emoji.cmd_fail + "我需要*{permission}**权限才能这么做。"
            no_pm = emoji.cmd_fail + "您只能在这服务器上使用此指令。"
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "直播指令 - 支援"
            command_usage.add_field(
                name = "指令",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - 取得用户直播资讯
                `!twitch stream watch <user>` - 在Discord上观看Twitch直播
                `!twitch stream game <name>` - 观看某人游玩特定的游戏直播
                `!twitch stream top` - 取得最多人观看的直播资讯
                """)
            )
            game_desc = "看看{user}正在玩{game}，有{view_count}人正在观看。 观看数:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "找不到该游戏"
            game_no_streams = emoji.cmd_fail + "没有人正在直播此游戏。"
            live = "Twitch上的直播"
            stream_not_found = emoji.cmd_fail + "用户不存在或不再线上。请确认您只有输入用户名称，没有其他像是 `()`或`<>`。"
            stream_desc = textwrap.dedent("""\
            正在玩{game}，有{view_count}人正在观看
            **[在Twitch上观看](https://twitch.tv/{channel})**或输入`twitch stream watch {channel}`
            直播预览：
            """)
        class Users:
            connections = "有关{user}"
            connected = "已连接至{account}"
            followers = "追随者"
            following = "正在追随"
            live = "正在直播"
            playing = "正在玩{game}，有{view_count}人正在观看"
            not_connected = "无法连接"
            not_live = "现在没有在直播"
            no_login_dash = "这位用户尚未拜访[TwitchBot仪表板](http://dash.twitchbot.io)."
            streamer_id = "直播者ID："
            views = "观看数"
            unknown = "未知"
            watch_on_twitch = "在Twitch上观看"
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

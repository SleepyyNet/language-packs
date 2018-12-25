from . import _emoji as emoji
import textwrap
import discord

class Chinese:
    def __init__(self):
        self._lang_name = "中文"
        self._lang_emoji = ":flag_cn:"
        self._translator = "Dexmio#8239"
        class Audio:
            no_channel = emoji.cmd_fail + "您必須加入語音頻道。"
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "請投票來繼續"
            need_upvote.description = "您需要投TwitchBot一票，才能繼續收聽直播 **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "想要跳過投票？",
                value = "[TwitchBot Premium](https://twitchbot.io/premium)讓你在聽直播時不需要再一直投票。"
            )
            please_wait = "請稍後... " + emoji.loading
            user_noexist = emoji.cmd_fail + "這位使用者不存在或目前沒在直播。請在頻道入鏈結。"
            np_title = "正在播放 {channel}"
            np_desc = "{title}\n{viewer_count} 正在觀看"
            np_leave = "輸入 '!twitch leave' 來結束直播"
            connection_timeout = emoji.cmd_fail + "語音連線逾時"
            not_streaming = "我現在沒在此伺服器直播任何東西。"
            disconnected = "已離開語音頻道。"
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Clips - Help"
            command_usage.add_field(
                name = "指令",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - 從Twitch使用者取得特定的影片
                `!twitch clips trending` - 取得熱門影片
                `!twitch clips game <game>` - 取得特定遊戲的影片
                `!twitch clips uservoted` - 尋找TwitchBot使用者們投票出最熱門的影片
                """)
            )
            clip_desc = "查看 {user} 遊玩 {game}:\n{url}"
            no_clips = emoji.cmd_fail + "找不到任何相關影片。"
            no_votes = emoji.cmd_fail + "還沒有人對任何影片投票。請等等再回來。"
            uservote_clip_desc = "{vote_count} 此部影片的票數由 {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, 你的票無法送達。"
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "TwitchBot 指令"
            e.description = ":warning: __**請勿在指令中輸入 `<>` 或 `[]`。**__"
            e.add_field(
                name="一般",
                value=textwrap.dedent("""\
                `!twitch help` - 顯示機器人幫助
                `!twitch info` - 顯示機器人資訊
                `!twitch lang` - 設定使用語言
                `!twitch invite` - 顯示TwitchBot伺服器邀請鏈結
                `!twitch status` - 顯示Twitch API 狀態
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - 取得Twitch 頻道資訊
                `!twitch stream user <user>` - 取得使用者直播資訊
                `!twitch stream watch <user>` - 在Discord上觀看Twitch直播
                `!twitch stream game <name>` - 觀看某人遊玩特定的遊戲直播
                `!twitch stream top` - 取得最多人觀看的直播資訊
                `!twitch game <name>` - 取得Twitch遊戲資訊
                `!twitch top` - 取得最熱門的Twitch遊戲
                """),
                inline=False
            )
            e.add_field(
                name="影片",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - 從Twitch使用者取得特定的影片
                `!twitch clips trending` - 取得熱門影片
                `!twitch clips game <game>` - 取得特定遊戲的影片
                `!twitch clips uservoted` - 尋找TwitchBot使用者們投票出最熱門的影片
                """),
                inline=False
            )
            e.add_field(
                name="直播者通知",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - 在特定的頻道新增一個直播者通知給直播者。
                `!twitch notif remove <#discord_channel> <streamer_name>` - 在特定的頻道移除一個直播者通知給直播者。
                `!twitch notif list [#discord_channel]` - 在特定的頻道列出直播者通知
                `!twitch notif formatting` - 顯示可新增至直播者通知的變數
                """),
                inline=False
            )
            e.add_field(
                name="直播身分",
                value=textwrap.dedent("""\
                `!twitch live_role set` - 在所這伺服器上設置一個直播身分
                `!twitch live_role filter` - 限制有直播身分的使用者特定的身分
                `!twitch live_role delete` - 刪除直播身分的設置
                `!twitch live_role view` - 告訴你現在有那些身分已設置
                """),
                inline=False
            )
            e.add_field(
                name="音訊",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - 在現在的語音頻道收聽直播
                `!twitch nowplaying` - 顯示現在正在播放的直播，如果有的
                `!twitch leave` - 離開語音頻道
                """),
                inline=False
            )
            e.add_field(
                name="遊戲狀態",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - 顯示鬥陣特工玩家狀態
                `!twitch fortnite <pc/psn/xbl> <player>` - 顯示Fortnite玩家狀態
                """),
                inline=False
            )
            e.add_field(
                name="訊息過濾器",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - 設定伺服器端病毒過濾器
                `!twitch filter remove` - 移除伺服器端病毒過濾器
                """),
                inline=False
            )
        class Errors:
            err_report = "請至<https://link.twitchbot.io/support>回報此錯誤給開發者。"
            forbidden = emoji.cmd_fail + "我沒有正確的權限這麼做。"
            not_found = emoji.cmd_fail + "找不到那個Discord頻道。請確認當你輸入`#mention`時你沒有包含<>。"
            not_started = "TwitchBot還正在啟動！請等個幾分鐘後再試。"
            check_fail = emoji.cmd_fail + "你沒有權限使用此指令。"
            cooldown = emoji.cmd_fail + "你可以在{time}秒後再次使用此指令。"
            conn_closed = emoji.cmd_fail + "語音連線已結束。原因： `{reason}`"
            missing_arg = emoji.cmd_fail + "你失去了 `{param}`參數。"
            too_many_requests = emoji.cmd_fail + "第三方伺服器在處理我們的要求時出了問題。請稍後在試。"
        class Filter:
            cmd_usage = "輸入`!twitch help filter`來查看如可使用指令。"
            need_donate = "只有TwitchBot Premium成員能使用此指令。了解更多： <https://twitchbot.io/premium>"
            invalid_sensitivity = "靈敏度必須在85至60之間。"
            add_success = emoji.cmd_success + "成功在此伺服器設置病毒過濾器。"
            no_filter = emoji.cmd_fail + "此伺服器沒有任何病毒過濾器。"
            del_success = emoji.cmd_success + "成功移除此伺服器的病毒過濾器。"
        class Games:
            no_results = emoji.cmd_fail + "沒有找到任何結果。"
            no_stats_overwatch = emoji.cmd_fail + "找不到任何此玩家的狀態。如果您的個人檔案為私人，您將無法看到玩家狀態除非您設為公開。請至<https://dotesports.com/overwatch/news/ow-public-private-profile-25347>按照步驟設定您的個人檔案至公開。"
            no_stats_fortnite = emoji.cmd_fail + "找不到此玩家。請檢察您的拼字或嘗試不同平台。"
            view_streams = "觀看直播"
            top_games = emoji.twitch_icon + "遊戲列表"
            top_games_desc = "{view_count}人觀看 • {channel_count}個頻道正在直播"
            invalid_battletag = "請依`name#id`格式輸入您的 Battletag。"
            invalid_platform = "平台必須是`pc`、`psn`或`xbl`。"
            incomplete_data = "您的個人檔案資訊並不完整。您的個人檔案僅限私人，請至<https://dotesports.com/overwatch/news/ow-public-private-profile-25347>按照步驟設定您的個人檔案至公開。"
            incomplete_data_short = "某些資訊可能遺失或不完整"
            generic_error = emoji.cmd_fail + "錯誤發生："
            powered_by_overwatch = "由owapi.net所有"
            powered_by_fortnite = "由fortnitetracker.com所有"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot支援**"
            e.add_field(
                name="指令",
                value="TwitchBot支援的指令前綴為`twitch`或`!twitch`。輸入`!twitch commands`來查所有能使用指令。",
                inline=False
            )
            e.add_field(
                name="支援",
                value="如果您需要TwitchBot的幫忙，您可以拜訪[支援中心](https://support.twitchbot.io)或加入[支援伺服器](https://discord.gg/UNYzJqV)。",
                inline=False
            )
            e.add_field(
                name="網站",
                value="您可至https://twitchbot.io查看TwitchBot資訊。",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="用每月$5.00 USD支持TwitchBot開發者並取得好用又有趣的功能。https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="投票競賽",
                name="我們正在免費送TwitchBot Premium給每月投最多票前三位使用者。[這裡投票](https://discordbots.org/bot/twitch/vote)以及[查看排行榜](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="關於",
                value="TwitchBot是由[Akira#4587](https://disgd.pw)使用discord.py製作。查看其他貢獻者，輸入`twitch info`。",
                inline=False
            )
            e.add_field(
                name="其他連結",
                value="[問與答](https://twitchbot.io/faq) · [儀表版](http://dash.twitchbot.io) · [投票](https://discordbots.org/bot/twitch/vote) · [邀請](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [部落格](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "可使用語言"
            avail_lang_setmsg = "設置TwitchBot使用語言，請輸入!twitch lang <language>。"
            stats_embed_title = emoji.twitch_icon + "TwitchBot狀態"
            stats_uptime = "運行時間"
            stats_usage = "使用量"
            stats_version = "版本"
            stats_shardinfo = "破碎資訊"
            stats_system = "系統"
            stats_developer = "開發者"
            stats_patrons = "贊助人"
            stats_links = "鏈結"
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

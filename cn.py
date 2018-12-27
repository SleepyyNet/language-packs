from . import _emoji as emoji
import textwrap
import discord

class Chinese:
    def __init__(self):
        self._lang_name = "中文(繁體)"
        self._lang_emoji = ":flag_tw: :flag_hk"
        self._translator = "Dexmio#8239"
        class Audio:
            no_channel = emoji.cmd_fail + "您必須加入語音頻道。"
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "請投票以繼續"
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
            uservote_clip_desc = "此部影片有{vote_count}票，由{user}:\n{url}"
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
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - 在特定的頻道新增一個直播者通知給直
                `!twitch notif remove <#discord_channel> <streamer_name>` - 在特定的頻道移除一個給直播者的直播者通知。
                `!twitch notif list [#discord_channel]` - 在特定的頻道列出直播者通知
                `!twitch notif formatting` - 顯示可新增至直播者通知的變數
                """),
                inline=False
            )
            e.add_field(
                name="直播身分",
                value=textwrap.dedent("""\
                `!twitch live_role set` - 在此伺服器上設置一個直播身分
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
            not_found = emoji.cmd_fail + "找不到此Discord頻道。請確認當你輸入`#mention`時沒有包含<>。"
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
            stats_patrons = "贊助者"
            stats_links = "鏈結"
            stats_links_desc = textwrap.dedent("""\
            **·** Website: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Upvote: https://discordbots.org/bot/twitch/vote
            **·** Donate: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**，您可以使用此鏈結邀請我至您的伺服器：<https://link.twitchbot.io/invite>"
            invite_msg2 = "需要幫忙嗎？加入支援伺服器：<https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Twitch狀態"
            status_cs = "目前狀態： `{status}`"
            lang_current = "您現在所使用的TwitchBot語言是 **{lang}**。請輸入 `!twitch lang <lang>`或`!twitch lang help`來更改您的語言。"
            lang_unavail = emoji.cmd_fail + "我們尚未翻譯此語言，輸入 `!twitch lang help`來查看可使用的語言。"
            lang_set = emoji.cmd_success + "成功設置您的TwitchBot語言至**{lang}**。"
        class Guild:
            submode_command_usage = "輸入`!twitch help sub_only`來查看如何使用指令。"
            submode_success = emoji.cmd_success + "已在此伺服器上啟動訂閱者模式。新的使用者必須訂閱才能加入{channel}。TwitchBot會嘗試私訊想加入的非訂閱者並踢除他們。注意：現存的會員不會被剔除。"
            submode_kick = "此伺服器只開放給訂閱者。您必須訂閱，才能夠加入。{}.\nTo 將您的Twitch帳號與TwitchBot連結，請至<https://dash.twitchbot.io> 點擊Twitch下方的'Link Account'。"
            submode_kick_audit_log = "此伺服器已啟動訂閱者模式。請輸入'!twitch sub_only off'來關閉此功能。"
            submode_del_success = emoji.cmd_success + "已關閉此伺服器訂閱者模式。"
            user_not_in_guild = emoji.cmd_fail + "此玩家不在這伺服器上。"
            no_login_dash = emoji.cmd_fail + "{user} 尚未登入TwitchBot儀表板。獲取其他用戶的頻道，請輸入 `!twitch sub_only on --user-id=(user id here)`。"
            no_link_dash = emoji.cmd_fail + "{user} 尚未將他的Twitch帳號與TwitchBot儀表板做鏈結。獲取其他用戶的頻道，請輸入 `!twitch sub_only on --user-id=(user id here)`。"
            http_err_dash = emoji.cmd_fail + "嘗試從TwitchBot儀表板取得資訊時發生了錯誤： {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "直播身分 - 支援"
            command_usage.description = "直播身分，當用戶在直播時會給他們的個身分。當他們停止直播時Twitchbot會自動從他們身上移除此身分。"
            command_usage.add_field(
                name = "指令",
                value = textwrap.dedent("""\
                `!twitch live_role set` - 在所這伺服器上設置一個直播身分
                `!twitch live_role filter` - 限制有直播身分的使用者特定的身分
                `!twitch live_role delete` - 刪除直播身分的設置
                `!twitch live_role view` - 告訴你現在有那些身分已設置
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "沒有舉出明確身分。請重新輸入指令並提及 @mention 一個身分。"
            not_set_up = emoji.cmd_fail + "此伺服器沒有設置任何直播身分。請輸入`!twitch live_role set`來設定一個。"
            role_not_found = emoji.cmd_fail + "找不到此身分。請勿輸入不必要的字符，像是 `<`, `>` 或 `@`。"
            add_success = emoji.cmd_success + "在此伺服器上直播的使用者會得到 **{role}** 身分。如果您想要設置一個過濾器給此身分，請輸入 `!twitch live_role filter`。"
            del_success = emoji.cmd_success + "已成功的從此伺服器上移出直播者身分。"
            filter_success = emoji.cmd_success + "已成功的在此伺服器上設置直播者過濾器。可能會需要花一點時間更新所有用戶的身分。"
            missing_perms_ext = emoji.cmd_fail + "我需要**`管理身分組`**權限才能這麼做。如果我已擁有該權限，請確保身分名稱`TwitchBot`是在你想要設置的身分上方。"
            view_response = "直播身分**{role}**已設置完成，會給予正在直播的用戶們。"
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "直播者通知 - 支援"
            command_usage.description = "當有Twitch用戶開始直播時，直播者通知能讓你客製化您的通知訊息。"
            command_usage.add_field(
                name = "指令",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - 在特定的頻道新增一個直播者通知給直播者。
                `!twitch notif remove <#discord_channel> <streamer_name>` - 在特定的頻道移除一個直播者通知給直播者。
                `!twitch notif list [#discord_channel]` - 在特定的頻道列出直播者通知
                `!twitch notif formatting` - 顯示可新增至直播者通知的變數
                """)
            )
            limit_reached = emoji.twitch_icon + "嗨，您好！不幸的是您已經達到設置通知訊息的上限。如果想要設置更多，您需要至以下網址<https://twitchbot.io/premium>來贊助我們。"
            prompt1 = "您想要在那個頻道顯示您的通知訊息？在下方提及或輸入頻道名。 *(請在60秒內回應)*"
            prompt2 = "請輸入您想要獲得通知的Twitch頻道名稱。 *(請在60秒內回應)*"
            prompt3 = "輸入您想要顯示在通知的訊息，或輸入`default`使用預設訊息。 *(請在180秒內回應)*"
            text_channel_not_found = emoji.cmd_fail + "找不到文字頻道。結束設定..."
            twitch_user_not_found = emoji.cmd_fail + "找不到該Twitch用戶。結束設定..."
            twitch_user_not_found_alt = emoji.cmd_fail + "該Twitch用戶不存在。請確認您沒有輸入任何額外的字符，像是(such as `<>`)，且沒有提及 @mentioning 任何Discord用戶。"
            response_timeout = "*回覆時間逾時*"
            invalid_data = emoji.cmd_fail + "Twitch發送了無效的數據："
            malformed_user = emoji.cmd_fail + "這看起來不像是有效的Twitch用戶。您只能包含下劃線，字母和數字。"
            default_msg = "<https://twitch.tv/{channel}>現在正在Twitch上直播！"
            del_fail = emoji.cmd_fail + "沒有設置有關這位用戶的通知。"
            del_success = emoji.cmd_success + "您不會在{channel}收到任有關{user}的通知。"
            add_success = emoji.cmd_success + "幫{user}在{channel}設置通知訊息。"
            list_title = "**#{channel}**的直播者通知"
            list_embed_limit = "客製化訊息不能包含嵌入訊息，因為Discord有1024個字符限制。使用者開直播時他們還是會顯示。"
            no_notifs = "此頻道並沒有設置任何的直播者通知。"
            notifications = "通知"
            bulk_delete_confirm = "**您將要刪除在{channel}的{count}則通知。**您確定您要這麼做？回覆`yes`如果您確定要這麼做。"
            bulk_delete_success = emoji.cmd_success + "成功刪除在{channel}的{count}則通知。"
            command_cancelled = "已取消的指令"
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "通知訊息變數"
            notif_variables.description = "插入以下變數訊息到您的直播通知訊息。"
            notif_variables.add_field(
                name = "可用的格式",
                value = textwrap.dedent("""\
                *`$title$`* - 直播標題
                *`$viewers$`* - 直播觀看人數
                *`$game$`* - 直播者目前正在玩的遊戲
                *`$url$`* - 頻道的URL
                *`$name$`* - 頻道名稱
                *`$everyone$`* - 插入提及所有人 @everyone 
                *`$here$`* - 插入提及這裡 @here 
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "您需要**{permission}**權限才能這麼做。"
            bot_need_perm = emoji.cmd_fail + "我需要*{permission}**權限才能這麼做。"
            no_pm = emoji.cmd_fail + "您只能在這伺服器上使用此指令。"
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "直播指令 - 支援"
            command_usage.add_field(
                name = "指令",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - 取得使用者直播資訊
                `!twitch stream watch <user>` - 在Discord上觀看Twitch直播
                `!twitch stream game <name>` - 觀看某人遊玩特定的遊戲直播
                `!twitch stream top` - 取得最多人觀看的直播資訊
                """)
            )
            game_desc = "看看{user}正在玩{game}，有{view_count}人正在觀看。 觀看數:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "找不到該遊戲"
            game_no_streams = emoji.cmd_fail + "沒有人正在直播此遊戲。"
            live = "Twitch上的直播"
            stream_not_found = emoji.cmd_fail + "使用者不存在或不再線上。請確認您只有輸入用戶名稱，沒有其他像是 `()`或`<>`。"
            stream_desc = textwrap.dedent("""\
            正在玩{game}，有{view_count}人正在觀看
            **[在Twitch上觀看](https://twitch.tv/{channel})**或輸入`twitch stream watch {channel}`

            直播預覽：
            """)
        class Users:
            connections = "有關{user}"
            connected = "已連接至{account}"
            followers = "追隨者"
            following = "正在追隨"
            live = "正在直播"
            playing = "正在玩{game}，有{view_count}人正在觀看"
            not_connected = "無法連接"
            not_live = "現在沒有在直播"
            no_login_dash = "這位使用者尚未拜訪[TwitchBot儀表板](http://dash.twitchbot.io)."
            streamer_id = "直播者ID："
            views = "觀看數"
            unknown = "未知"
            watch_on_twitch = "在Twitch上觀看"
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

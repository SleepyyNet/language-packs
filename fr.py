from . import _emoji as emoji
import textwrap
import discord

class English:
    def __init__(self):
        self._lang_name = "Français"
        self._lang_emoji = ":flag_fr:"
        self._translator = "Nicendredi#1888"
        class Audio:
            no_channel = emoji.cmd_fail + "You need to be in a voice channel."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Please upvote to continue"
            need_upvote.description = "You need to upvote TwitchBot to listen to streams! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Want to skip upvoting?",
                value = "[TwitchBot Premium](https://twitchbot.io/premium) lets you listen to streams without upvoting."
            )
            please_wait = "Please wait... " + emoji.loading
            user_noexist = emoji.cmd_fail + "This user doesn't exist or is not currently streaming. Try entering a link to the channel."
            np_title = "Now playing in {channel}"
            np_desc = "{title}\n{viewer_count} currently watching"
            np_leave = "Type '!twitch leave' to stop the stream"
            connection_timeout = emoji.cmd_fail + "Voice connection timed out."
            not_streaming = "I'm not streaming anything on this server right now."
            disconnected = "Left the voice channel."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Clips - Help"
            command_usage.add_field(
                name = "Commands",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - Gets a clip from the specified Twitch user
                `!twitch clips trending` - Gets a trending clip
                `!twitch clips game <game>` - Gets a clip from the specified game
                `!twitch clips uservoted` - Gets one of the most popular clips voted by TwitchBot users
                """)
            )
            clip_desc = "Check out {user} playing {game}:\n{url}"
            no_clips = emoji.cmd_fail + "No clips were found."
            no_votes = emoji.cmd_fail + "Nobody has voted on any clips yet. Come back later."
            uservote_clip_desc = "{vote_count} votes on this clip by {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, your upvote couldn't be be processed."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "TwitchBot Commands"
            e.description = ":warning: __**Do not put `<>` or `[]` around command arguments.**__"
            e.add_field(
                name="General",
                value=textwrap.dedent("""\
                `!twitch help` - Shows bot help
                `!twitch info` - Shows bot info
                `!twitch invite` - Displays a link to add TwitchBot to your server
                `!twitch status` - Shows Twitch API status
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - Gets info on a Twitch channel
                `!twitch stream user <user>` - Gets info on a user's stream
                `!twitch stream watch <user>` - Watch a Twitch stream from Discord
                `!twitch stream game <name>` - Watch someone stream the specified game
                `!twitch stream top` - Fetches info on a top stream
                `!twitch game <name>` - Gets info on a Twitch game
                `!twitch top` - Gets the most popular Twitch games
                """),
                inline=False
            )
            e.add_field(
                name="Clips",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - Gets a clip from the specified Twitch user
                `!twitch clips trending` - Gets a trending clip
                `!twitch clips game <game>` - Gets a clip from the specified game
                `!twitch clips uservoted` - Gets one of the most popular clips voted by TwitchBot users
                """),
                inline=False
            )
            e.add_field(
                name="Streamer Notifications",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Adds a streamer notification for a streamer to the specified channel
                `!twitch notif remove <#discord_channel> <streamer_name>` - Remove a streamer notification for a streamer to the specified channel
                `!twitch notif list [#discord_channel]` - Lists the streamer notifications for the specified channel
                `!twitch notif formatting` - Shows variables that you can insert into streamer notification messages
                """),
                inline=False
            )
            e.add_field(
                name="Live Role",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Sets the Live Role for the current server
                `!twitch live_role filter` - Restricts Live Role to users with a specific role
                `!twitch live_role delete` - Removes the Live Role configuration
                `!twitch live_role view` - Tells you which role is currently set up
                """),
                inline=False
            )
            e.add_field(
                name="Audio",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - Listen to a Twitch stream in the current voice channel
                `!twitch nowplaying` - Shows the stream currently playing, if any
                `!twitch leave` - Leaves a voice channel
                """),
                inline=False
            )
            e.add_field(
                name="Game Stats",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - Shows Overwatch player stats
                `!twitch fortnite <pc/psn/xbl> <player>` - Shows Fortnite player stats
                """),
                inline=False
            )
            e.add_field(
                name="Message Filter",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Sets the server-wide toxicity filter
                `!twitch filter remove` - Removes the server-wide toxicity filter
                """),
                inline=False
            )
        class Errors:
            err_report = "Please report this error to the developers at <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "I don't have the correct permissions to do that."
            not_found = emoji.cmd_fail + "That Discord channel was not found. Make sure you're not putting <> around it and that you're `#mention`ing it."
            not_started = "TwitchBot is still starting up! Please wait a few minutes before trying again."
            check_fail = emoji.cmd_fail + "You don't have permission to run this command."
            cooldown = emoji.cmd_fail + "You can run this command in {time} seconds."
            conn_closed = emoji.cmd_fail + "The voice connection was closed. Reason: `{reason}`"
            missing_arg = emoji.cmd_fail + "You're missing the `{param}` paramater."
            too_many_requests = emoji.cmd_fail + "Third-party servers are having trouble keeping up with our requests. Please try again later."
        class Filter:
            cmd_usage = "Type `!twitch help filter` to view command usage."
            need_donate = "Only TwitchBot Premium members can use this command. Learn more: <https://twitchbot.io/premium>"
            invalid_sensitivity = "Sensitivity must be between 85 and 60."
            add_success = emoji.cmd_success + "Successfully set this server's toxicity filter."
            no_filter = emoji.cmd_fail + "No toxicity filter exists for this server."
            del_success = emoji.cmd_success + "Successfully removed this server's toxicity filter."
        class Games:
            no_results = emoji.cmd_fail + "No results found."
            no_stats_overwatch = emoji.cmd_fail + "No stats could be found for this player. If your profile is private, you can't see stats for it unless you make it public. Please follow the steps at <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> to make your profile public."
            no_stats_fortnite = emoji.cmd_fail + "Player not found. Check the spelling of the username or try a different platform."
            view_streams = "View Streams"
            top_games = emoji.twitch_icon + "Top Games"
            top_games_desc = "{view_count} viewers • {channel_count} channels streaming"
            invalid_battletag = "Please enter your Battletag in a format of `name#id`."
            invalid_platform = "Platform must be one of `pc`, `psn`, or `xbl`."
            incomplete_data = "Your profile data is incomplete. If your profile is private, follow the steps at <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> to make it public so you can view your stats."
            incomplete_data_short = "Some data may be missing or incomplete"
            generic_error = emoji.cmd_fail + "An error occurred:"
            powered_by_overwatch = "Powered by owapi.net"
            powered_by_fortnite = "Powered by fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot Help**"
            e.add_field(
                name="Commands",
                value="TwitchBot responds to commands starting with `twitch` or `!twitch`. Type `!twitch commands` to view all runnable commands.",
                inline=False
            )
            e.add_field(
                name="Support",
                value="If you need help with TwitchBot, you can visit the [support center](https://support.twitchbot.io) or join the [support server](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Website",
                value="You can view information about TwitchBot at https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Support TwitchBot's development and get a handful of cool features and benefits for just $5.00 USD a month. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Upvote Competition",
                value="We're giving away TwitchBot Premium for FREE to the top three voters at the end of every month! [Upvote here](https://discordbots.org/bot/twitch/vote) and [view the leaderboard](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="About",
                value="TwitchBot was made by [Akira#4587](https://disgd.pw) using discord.py. To view other contributors, type `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Other links",
                value="[FAQ](https://twitchbot.io/faq) · [Dashboard](http://dash.twitchbot.io) · [Upvote](https://discordbots.org/bot/twitch/vote) · [Invite](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
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
            notifications = "No streamer notifications are set up for this channel."
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

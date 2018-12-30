from . import _emoji as emoji
import textwrap
import discord

class Indonesian:
    def __init__(self):
        self._lang_name = "bahasa Indonesia"
        self._lang_emoji = ":flag_id:"
        self._translator = "alcyneous#2803"
        class Audio:
            no_channel = emoji.cmd_fail + "Kamu harus masuk ke channel suara."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Tolong upvoting untuk lanjut"
            need_upvote.description = "Kamu perlu upvoting TwitchBot untuk mendengarkan siaran! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Ingin melewati upvoting?",
                value = "[TwitchBot Premium](https://twitchbot.io/premium) membuat kamu mendengarkan siaran tanpa perlu upvoting."
            )
            please_wait = "Tunggu sebentar... " + emoji.loading
            user_noexist = emoji.cmd_fail + "Pengguna ini tidak ada atau sedang tidak siaran. Coba masukan tautan ke dalam channel."
            np_title = "Sedang dimainkan di {channel}"
            np_desc = "{title}\n{viewer_count} sedang menonton"
            np_leave = "Ketik '!twitch leave' untuk menghentikan siaran"
            connection_timeout = emoji.cmd_fail + "Koneksi suara tidak ada."
            not_streaming = "Aku sedang tidak menyiarkan apapun di server ini."
            disconnected = "Keluar dari channel suara."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Klip - Bantuan"
            command_usage.add_field(
                name = "Perintah",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - Menampilkan klip dari pengguna Twitch yang ditentukan
                `!twitch clips trending` - Menampilkan klip trendi
                `!twitch clips game <game>` - Menampilkan klip berdasarkan game yang ditentukan
                `!twitch clips uservoted` - Menampilkan salah satu klip populer yang divoting oleh pengguna TwitchBot
                """)
            )
            clip_desc = "Periksa {user} sedang bermain {game}:\n{url}"
            no_clips = emoji.cmd_fail + "Tidak ada klip yang ditemukan."
            no_votes = emoji.cmd_fail + "Belum ada siapapun yang memvoting klip sekarang. Coba lagi nanti."
            uservote_clip_desc = "{vote_count} voting untuk klip ini oleh {user}:\n{url}"
            upvote_fail = emoji.cmd_fail + "**{user}**, votingmu tidak dapat diproses."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "Perintah TwitchBot"
            e.description = ":warning: __**Jangan gunakan `<>` atau `[]` saat mengetik perintah.**__"
            e.add_field(
                name="Umum",
                value=textwrap.dedent("""\
                `!twitch help` - Menampilkan bantuan bot
                `!twitch info` - Menampilkan info bot
                `!twitch lang` - Mengganti bahasa bot
                `!twitch invite` - Menampilkan tautan TwitchBot untuk ditambahkan ke servermu
                `!twitch status` - Menampilkan status Twitch API
                `!twitch ping` - Hayo loh!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - Mendapatkan info dari channel Twitch
                `!twitch stream user <user>` - Mendapatkan info dari penyiar
                `!twitch stream watch <user>` - Menonton siaran Twitch di Discord
                `!twitch stream game <name>` - Menonton siaran seseorang berdasarkan game yang dimainkannya
                `!twitch stream top` - Mendapatkan info dari siaran teratas
                `!twitch game <name>` - Mendapatkan info dari game yang sedang disiarkan di Twitch
                `!twitch top` - Mendapatkan info dari game yang paling popular di Twitch 
                """),
                inline=False
            )
            e.add_field(
                name="Klip",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - Menampilkan klip dari pengguna Twitch yang ditentukan
                `!twitch clips trending` - Menampilkan klip trendi
                `!twitch clips game <game>` - Menampilkan klip berdasarkan game yang ditentukan
                `!twitch clips uservoted` - Menampilkan salah satu klip populer yang divoting oleh pengguna TwitchBot
                """),
                inline=False
            )
            e.add_field(
                name="Notifikasi Penyiar",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Menambahkan notifikasi penyiar untuk penyiar di channel yang ditentukan
                `!twitch notif remove <#discord_channel> <streamer_name>` - Menghapus notifikasi penyiar untuk penyiar di channel yang ditentukan
                `!twitch notif list [#discord_channel]` - Daftar notifikasi penyiar pada channel yang ditentukan
                `!twitch notif formatting` - Menampilkan variabel yang bisa kamu masukan ke pesan notifikasi penyiar
                """),
                inline=False
            )
            e.add_field(
                name="Peran Live",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Menetapkan Peran Live untuk server ini
                `!twitch live_role filter` - Membatasi Peran Live untuk pengguna dengan peran tertentu
                `!twitch live_role delete` - Menghapus konfigurasi Peran Live
                `!twitch live_role view` - Memberitahu kamu peran yang sedang disiapkan
                """),
                inline=False
            )
            e.add_field(
                name="Audio",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - Mendengarkan siaran Twitch di channel suara yang sedang dimasuki
                `!twitch nowplaying` - Menampilkan siaran yang sedang dimainkan, jika ada
                `!twitch leave` - Keluar dari channel suara
                """),
                inline=False
            )
            e.add_field(
                name="Status Permainan",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - Menampilkan status pemain Overwatch
                `!twitch fortnite <pc/psn/xbl> <player>` - Menampilkan status pemain Fortnite
                """),
                inline=False
            )
            e.add_field(
                name="Filter Pesan",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Menetapkan filter toxic pada server
                `!twitch filter remove` - Menghapus filter toxic pada server
                """),
                inline=False
            )
        class Errors:
            err_report = "Tolong lapor kesalahan ini ke pengembang di <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "Aku tidak mempunyai izin yang benar untuk melakukan itu."
            not_found = emoji.cmd_fail + "Discord channel itu tidak ditemukan. Pastikan kamu tidak mencantumkan <> saat mengetik dan `#menyebutkan` channelnya."
            not_started = "TwitchBot sedang memulai! Tunggu beberapa menit sebelum mencoba kembali."
            check_fail = emoji.cmd_fail + "Kamu tidak mempunyai izin untuk menjalankan perintah ini."
            cooldown = emoji.cmd_fail + "Kamu bisa menjalankan perintah ini dalam {time} detik."
            conn_closed = emoji.cmd_fail + "Koneksi suara ditutup. Alasan: `{reason}`"
            missing_arg = emoji.cmd_fail + "Kamu tidak mempunyai `{param}` parameter."
            too_many_requests = emoji.cmd_fail + "Server pihak-ketiga mengalami kesulitan memenuhi permintaan kami. Silahkan coba lagi nanti."
        class Filter:
            cmd_usage = "Ketik `!twitch help filter` untuk melihat penggunaan perintah."
            need_donate = "Hanya pengguna TwitchBot Premium yang dapat menggunakan perintah ini. Pelajari lebih lanjut: <https://twitchbot.io/premium>"
            invalid_sensitivity = "sensitivitas harus diantara 85 dan 60."
            add_success = emoji.cmd_success + "Berhasil menetapkan filter toxic di server ini."
            no_filter = emoji.cmd_fail + "Tidak ada filter toxic di server ini."
            del_success = emoji.cmd_success + "Berhasil menghapus filter toxic di server ini."
        class Games:
            no_results = emoji.cmd_fail + "Tidak ditemukan."
            no_stats_overwatch = emoji.cmd_fail + "Tidak ada status untuk pemain ini. Jika profilmu bersifat pribadi, maka kamu tidak dapat melihat statusnya kecuali kalau diubah menjadi publik. Silahkan ikuti langkah-langkahnya di <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> untuk membuat profilmu publik."
            no_stats_fortnite = emoji.cmd_fail + "Pemain tidak ditemukan. Periksa ejaan nama pengguna atau coba platform yang berbeda."
            view_streams = "Lihat Siaran"
            top_games = emoji.twitch_icon + "Permainan Teratas"
            top_games_desc = "{view_count} penonton • {channel_count} channel streaming"
            invalid_battletag = "Silahkan masukan Battletag kamu dengan format `nama#id`."
            invalid_platform = "Platform harus salah satu diantara `pc`, `psn`, atau `xbl`."
            incomplete_data = "Data profilmu tidak lengkap. Jika profilmu bersifat pribadi, Silahkan ikuti langkah-langkahnya di <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> untuk membuat profilmu publik jadi kamu bisa melihat statusmu."
            incomplete_data_short = "Beberapa data mungkin hilang atau tidak lengkap"
            generic_error = emoji.cmd_fail + "Kesalahan terjadi:"
            powered_by_overwatch = "Dipersembahkan oleh owapi.net"
            powered_by_fortnite = "Dipersembahkan oleh fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**Bantuan TwitchBot**"
            e.add_field(
                name="Perintah",
                value="TwitchBot menanggapi perintah yang dimulai dengan `twitch` atau `!twitch`. Ketik `!twitch commands` untuk melihat semua perintah yang dapat dijalankan.",
                inline=False
            )
            e.add_field(
                name="Bantuan",
                value="Jika kamu butuh bantuan dengan TwitchBot, kamu bisa mengunjungi [pusat bantuan](https://support.twitchbot.io) atau bergabung ke [server bantuan](https://discord.gg/UNYzJqV).",
                inline=False
            )
            e.add_field(
                name="Situs web",
                value="Kamu bisa melihat informasi mengenai TwitchBot di https://twitchbot.io",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="Dukung pengembangan TwitchBot dan dapatkan beberapa fitur dan manfaat keren hanya dengan $5.00 USD sebulan. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Kompetisi Upvoting",
                value="Kami memberikan TwitchBot Premium secara GRATIS ke tiga pemilih teratas setiap akhir bulan! [Upvoting disini](https://discordbots.org/bot/twitch/vote) dan [lihat papan peringkat](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="Tentang",
                value="TwitchBot dibuat oleh [Akira#4587](https://disgd.pw) menggunakan discord.py. Untuk melihat kontributor yang lain, ketik `twitch info`.",
                inline=False
            )
            e.add_field(
                name="Tautan lain",
                value="[FAQ](https://twitchbot.io/faq) · [Dashboard](http://dash.twitchbot.io) · [Upvoting](https://discordbots.org/bot/twitch/vote) · [Undang](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
            e.add_field(
                name="Terjemahan ada disini! :flag_mx: :flag_fr: :flag_tr: :flag_it:",
                value="Ketik `!twitch lang help` untuk melihat daftar bahasa yang tersedia pada TwitchBot.",
                inline=False
            )
        class General:
            avail_lang_title = "Terjemahan yang tersedia"
            avail_lang_setmsg = "Untuk menetapkan bahasa TwitchBot, ketik !twitch lang <bahasa>."
            stats_embed_title = emoji.twitch_icon + "Status TwitchBot"
            stats_uptime = "Uptime"
            stats_usage = "Pemakaian"
            stats_version = "Versi"
            stats_shardinfo = "Info Shard"
            stats_system = "Sistem"
            stats_developer = "Pengembang"
            stats_patrons = "Patrons"
            stats_links = "Tautan"
            stats_links_desc = textwrap.dedent("""\
            **·** Situs Web: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Upvoting: https://discordbots.org/bot/twitch/vote
            **·** Donasi: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, kamu dapat mengundangku ke server dengan tautan ini: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Butuh bantuan? Bergabung dengan server bantuan: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Twitch Status"
            status_cs = "Status sekarang: `{status}`"
            lang_current = "Bahasa untuk TwitchBot saat ini adalah **{lang}**. Untuk mengubahnya, ketik `!twitch lang <lang>` atau `!twitch lang help`."
            lang_unavail = emoji.cmd_fail + "Terjemahan itu tidak tersedia. Ketik `!twitch lang help` untuk melihat bahasa yang tersedia."
            lang_set = emoji.cmd_success + "Berhasil menetapkan bahasa TwitchBot ke **{lang}**."
        class Guild:
            submode_command_usage = "Ketik `!twitch help sub_only` untuk melihat penggunaan perintah."
            submode_success = emoji.cmd_success + "Mode Hanya-Pelanggan telah diaktifkan di server ini. Pengguna baru harus menjadi pelanggan untuk {channel} untuk bergabung. TwitchBot akan mencoba untuk DM non-pelanggan yang bergabung dan menendang mereka. Catatan: Pengguna yang sudah ada tidak akan ditendang."
            submode_kick = "Server ini dalam mode hanya-pelanggan. Untuk bergabung, kamu perlu menjadi pelanggan dari {}.\nUntuk menyambungkan akun Twitch kamu dengan TwitchBot, pergi ke <https://dash.twitchbot.io> dan tekan 'Link Account' dibawah Link Twitch."
            submode_kick_audit_log = "Mode Hanya-Pelanggan sedang aktif di server ini. Untuk mematikannya, ketik '!twitch sub_only off'."
            submode_del_success = emoji.cmd_success + "Mode Hanya-Pelanggan telah dimatikan di server ini."
            user_not_in_guild = emoji.cmd_fail + "Pengguna itu tidak ada di server ini."
            no_login_dash = emoji.cmd_fail + "{user} belum masuk ke dashboard TwitchBot. Untuk menampilkan channel dari pengguna lain, ketik `!twitch sub_only on --user-id=(user id disini)`."
            no_link_dash = emoji.cmd_fail + "{user} belum menyambungkan channel Twitch ke dashboard TwitchBot. Untuk menampilkan channel dari pengguna lain, ketik `!twitch sub_only on --user-id=(user id disini)`."
            http_err_dash = emoji.cmd_fail + "Terjadi kesalahan saat mencoba mendapatkan informasi dari dasboard TwitchBot: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Peran Live - Bantuan"
            command_usage.description = "Dengan Peran Live, kamu dapat menetapkan peran untuk ditambahkan ke pengguna saat mereka live. TwitchBot akan secara otomatis menghapus peran saat pengguna berhenti streaming."
            command_usage.add_field(
                name = "Perintah",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Menetapkan Peran Live untuk server ini
                `!twitch live_role filter` - Membatasi Peran Live untuk pengguna dengan peran tertentu
                `!twitch live_role delete` - Menghapus konfigurasi Peran Live
                `!twitch live_role view` - Memberitahu kamu peran yang sedang disiapkan
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "Tidak ada peran yang ditentukan. Silahkan jalankan kembali perintah ini dan @sebut sebuah peran."
            not_set_up = emoji.cmd_fail + "Tidak ada Peran Live yang ditetapkan di server ini. Ketik `!twitch live_role set` untuk menetapkan."
            role_not_found = emoji.cmd_fail + "Tidak ada nama peran yang cocok. Jangan tambahkan karakter ekstra dalam kueri kamu, seperti `<`, `>`, or `@`."
            add_success = emoji.cmd_success + "Pengguna di server ini yang live di Twitch akan mendapat peran **{role}**. Jika kamu mau menetapkan filter untuk Peran Live, ketik `!twitch live_role filter`."
            del_success = emoji.cmd_success + "Berhasil menghapus konfigurasi Peran Live di server ini."
            filter_success = emoji.cmd_success + "Berhasil menetapkan filter peran Live di server ini. Mungkin perlu beberapa saat untuk memperbarui peran semua pengguna."
            missing_perms_ext = emoji.cmd_fail + "Aku butuh izin **`Manage Roles`** untuk melakukan ini. Jika aku mempunyai izinnya, pastikan peran bernama `TwitchBot` berada diatas peran yang ingin kamu tetapkan."
            view_response = "Peran Live saat ini diatur untuk memberikan peran **{role}** kepada anggota saat mereka streaming."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Notifikasi Penyiar - Bantuan"
            command_usage.description = "Notifikasi Penyiar memungkinkan kamu mengatur pesan kostum saat pengguna Twitch sedang live."
            command_usage.add_field(
                name = "Perintah",
                value = textwrap.dedent("""\
		`!twitch notif add [#discord_channel] [streamer_name] [message]` - Menambahkan notifikasi penyiar untuk penyiar di channel yang ditentukan
                `!twitch notif remove <#discord_channel> <streamer_name>` - Menghapus notifikasi penyiar untuk penyiar di channel yang ditentukan
                `!twitch notif list [#discord_channel]` - Daftar notifikasi penyiar pada channel yang ditentukan
                `!twitch notif formatting` - Menampilkan variabel yang bisa kamu masukan ke pesan notifikasi penyiar
                """)
            )
            limit_reached = emoji.twitch_icon + "Halo kamu! Sayangnya sekarang kamu telah mencapai jumlah maksimum notifikasi yang dapat kamu tambahkan ke server ini. Untuk menambahkan lebih banyak, kamu perlu donasi di <https://twitchbot.io/premium>."
            prompt1 = "Di channel mana kamu ingin menerima notifikasi? #Sebutkan atau ketik namanya dibawah. *(menanggapi dalam 60 detik)*"
            prompt2 = "Ketik nama channel Twitch yang ingin kamu tetapkan untuk notifikasi. *(menanggapi dalam 60 detik)*"
            prompt3 = "Masukan pesan kostum yang ingin kamu tampilkan ketika pengguna sedang live, atau ketik `default` untuk pesan standar. *(menanggapi dalam 180 detik)*"
            text_channel_not_found = emoji.cmd_fail + "Tidak dapat menemukan channel teks itu. Keluar dari perintah..."
            twitch_user_not_found = emoji.cmd_fail + "Pengguna Twitch itu tidak dapat ditemukan. Keluar dari perintah..."
            twitch_user_not_found_alt = emoji.cmd_fail + "Pengguna Twitch itu tidak ada. Pastikan kamu tidak menambahkan sesuatu ketika mengetikan namanya (seperti `<>`), dan tidak sedang @menyebut pengguna Discord."
            response_timeout = "*Waktu tanggapan habis.*"
            invalid_data = emoji.cmd_fail + "Data tidak valid dikirim dari Twitch:"
            malformed_user = emoji.cmd_fail + "Itu tidak terlihat seperti pengguna Twitch yang valid. Kamu hanya bisa memasukan garis bawah, huruf, dan angka."
            default_msg = "<https://twitch.tv/{channel}> sekarang sedang live di Twitch!"
            del_fail = emoji.cmd_fail + "Tidak ada notifikasi yang ditetapkan untuk pengguna ini."
            del_success = emoji.cmd_success + "Kamu tidak akan mendapat notifikasi lagi di {channel} ketika {user} sedang live."
            add_success = emoji.cmd_success + "Menambahkan notifikasi untuk {user} di {channel}"
            list_title = "Notifikasi penyiar pada **#{channel}**"
            list_embed_limit = "Pesan kostum tidak termasuk dalam bagian embed dikarenakan ada batas 1024 karakter pada discord. Mereka masih akan ditampilkan ketika pengguna live."
            no_notifs = "Tidak ada notifikasi penyiar yang ditetapkan di channel ini."
            notifications = "Notifikasi"
            bulk_delete_confirm = "**Kamu akan menghapus {count} notifikasi di {channel}.** Kamu yakin ingin melakukan ini? Jawab dengan `yes` jika ingin melanjutkan."
            bulk_delete_success = emoji.cmd_success + "Berhasil menghapus {count} notifikasi di {channel}."
            command_cancelled = "Perintah dibatalkan."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Variabel notifikasi pesan"
            notif_variables.description = "Gunakan salah satu variabel dibawah untuk memasukan data ke dalam pesan notifikasi."
            notif_variables.add_field(
                name = "Format yang tersedia",
                value = textwrap.dedent("""\
                *`$title$`* - Judul siaran
                *`$viewers$`* - Angka penonton yang sedang menonton siaran
                *`$game$`* - Permainan yang sedang dimainkan oleh penyiar
                *`$url$`* - channel URL
                *`$name$`* - Nama channel
                *`$everyone$`* - Menyisipkan sebutan @everyone
                *`$here$`* - Menyisipkan sebutan @here
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "Kamu butuh izin **{permission}** untuk melakukan ini."
            bot_need_perm = emoji.cmd_fail + "Aku butuh izin **{permission}** untuk melakukan ini."
            no_pm = emoji.cmd_fail + "Kamu hanya dapat menggunakan perintah ini di server."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Perintah Siaran - Bantuan"
            command_usage.add_field(
                name = "Perintah",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - Mendapatkan info dari penyiar
                `!twitch stream watch <user>` - Menonton siaran Twitch di Discord
                `!twitch stream game <name>` - Menonton siaran seseorang berdasarkan game yang dimainkannya
                `!twitch stream top` - Mendapatkan info dari siaran teratas
                """)
            )
            game_desc = "Periksa {user} sedang bermain {game} untuk {view_count} penonton:\nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Permainan itu tidak dapat ditemukan."
            game_no_streams = emoji.cmd_fail + "Tidak ada yang menyiarkan permainan itu."
            live = "Sedang Live di Twitch"
            stream_not_found = emoji.cmd_fail + "Pengguna itu tidak ada atau sedang tidak online. Pastikan nama pengguna benar dan tidak menambahkan sesuatu, seperti `()` or `<>`."
            stream_desc = textwrap.dedent("""\
            Sedang bermain {game} untuk {view_count} penonton
            **[Tonton di Twitch](https://twitch.tv/{channel})** atau ketik `twitch stream watch {channel}`

            Tinjauan Siaran:
            """)
        class Users:
            connections = "Koneksi untuk {user}"
            connected = "Terhubung ke {account}"
            followers = "Pengikut"
            following = "Mengikuti"
            live = "Sedang Live"
            playing = "Sedang bermain {game} untuk {view_count} penonton"
            not_connected = "Tidak Terhubung"
            not_live = "Sedang Offline"
            no_login_dash = "Pengguna ini belum mengunjungi [dashboard TwitchBot](http://dash.twitchbot.io)."
            streamer_id = "ID Penyiar:"
            views = "Ditonton"
            view_profile = "Lihat profil Twitch"
            unknown = "Tidak Diketahui"
            watch_on_twitch = "Tonton di Twitch"
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

from . import _emoji as emoji
import textwrap
import discord

class Turkish:
    def __init__(self):
        self._lang_name = "Türk"
        self._lang_emoji = ":flag_tr:"
        self._translator = "Alexei#1991"
        class Audio:
            no_channel = emoji.cmd_fail + "Bir ses kanalında olmanız gerekli."
            need_upvote = discord.Embed(color=0x6441A4)
            need_upvote.title = "Lütfen devam etmek için oy verin"
            need_upvote.description = "Yayınları dinleyebilmek için TwitchBot'a oy vermeniz gerekli! **<https://link.twitchbot.io/upvote>**"
            need_upvote.add_field(
                name = "Oylamayı atlamak ister misiniz?",
                value = "[TwitchBot Premium](https://twitchbot.io/premium) oylamadan yayınları dinlemenizi sağlar."
            )
            please_wait = "Lütfen bekleyin..." + emoji.loading
            user_noexist = emoji.cmd_fail + "Bu kullanıcı mevcut değil veya şuan yayın yapmıyor. Kanala bir bağlantı girmeyi deneyin."
            np_title = "Şuan {channel}'da oynatılıyor"
            np_desc = "{title}\n{viewer_count} şuanda izliyor"
            np_leave = "Yayını durdurmak için '!twitch leave' komutunu kullanın"
            connection_timeout = emoji.cmd_fail + "Ses bağlantısı zaman aşımına uğradı."
            not_streaming = "Şu anda bu sunucuda hiçbir şey yayınlamıyorum."
            disconnected = "Ses kanalından ayrıldı."
        class Clips:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Klipler - Yardım"
            command_usage.add_field(
                name = "Komutlar",
                value = textwrap.dedent("""\
                `!twitch clips from <user>` - Belirtilen Twitch kullanıcısından bir klip alır
                `!twitch clips trending` - Trend bir klip alır
                `!twitch clips game <game>` - Belirtilen oyundan bir klip alır
                `!twitch clips uservoted` - TwitchBot kullanıcılarının oyladığı en popüler kliplerden birini alır
                """)
            )
            clip_desc = "{user} kullanıcısına {game}:\n{url} oynarken göz atın"
            no_clips = emoji.cmd_fail + "Hiçbir klip bulunamadı."
            no_votes = emoji.cmd_fail + "Henüz kimse klibe oy vermedi. Daha sonra tekrar deneyin."
            uservote_clip_desc = "{user}:\n{url} tarafından bu klibe {vote_count} oy verildi"
            upvote_fail = emoji.cmd_fail + "**{user}**, oylamanız işleme alınamadı."
        class CommandsList:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "TwitchBot Komutları"
            e.description = ":warning: __**Komut argümanlarının etrafında `<>` veya `[]` kullanmayın.**__"
            e.add_field(
                name="Genel",
                value=textwrap.dedent("""\
                `!twitch help` - Bot yardımını gösterir
                `!twitch info` - Bot bilgisini gösterir
                `!twitch lang` - Bot dilini belirler
                `!twitch invite` - Sunucunuza TwitchBot eklemek için bir bağlantı görüntüler
                `!twitch status` - Twitch API durumunu gösterir
                `!twitch ping` - Pong!
                """),
                inline=False
            )
            e.add_field(
                name="Twitch",
                value=textwrap.dedent("""\
                `!twitch user <user>` - Twitch kanalı hakkında bilgi alır
                `!twitch stream user <user>` - Bir kullanıcının yayını hakkında bilgi alır
                `!twitch stream watch <user>` - Discord'dan bir Twitch yayını izleyin
                `!twitch stream game <name>` - Birinin belirtilen bir oyununun yayınını izle
                `!twitch stream top` - En iyi yayın hakkında bilgi verir
                `!twitch game <name>` - Bir Twitch oyunu hakkında bilgi alır
                `!twitch top` - En popüler Twitch oyunlarını gösterir
                """),
                inline=False
            )
            e.add_field(
                name="Klipler",
                value=textwrap.dedent("""\
                `!twitch clips from <user>` - Belirtilen Twitch kullanıcısından bir klip alır
                `!twitch clips trending` - Trend bir klip alır
                `!twitch clips game <game>` - Belirtilen oyundan bir klip alır
                `!twitch clips uservoted` - TwitchBot kullanıcılarının oy verdiği en popüler kliplerden birini alır
                """),
                inline=False
            )
            e.add_field(
                name="Yayıncı Bildirimleri",
                value=textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Belirtilen kanala bir yayıncı için Yayıncı Bildirimi ekler
                `!twitch notif remove <#discord_channel> <streamer_name>` - Belirtilen kanaldaki bir yayıncının Yayıncı Bildirimini kaldırır
                `!twitch notif list [#discord_channel]` - Belirtilen kanaldaki Yayıncı Bildirimlerini listeler
                `!twitch notif formatting` - Yayıncı Bildirimlerine ekleyebileceğiniz değişkenleri gösterir
                """),
                inline=False
            )
            e.add_field(
                name="Canlı Rol",
                value=textwrap.dedent("""\
                `!twitch live_role set` - Geçerli sunucu için Canlı Rol ayarlar
                `!twitch live_role filter` - Canlı Rolü belirli bir rolü olan kullanıcılarla sınırlandırır
                `!twitch live_role delete` - Canlı Rol yapılandırmasını kaldırır
                `!twitch live_role view` - Hangi rolün kurulduğunu gösterir
                """),
                inline=False
            )
            e.add_field(
                name="Ses",
                value=textwrap.dedent("""\
                `!twitch listen <user>` - Geçerli ses kanalında bir Twitch yayını dinleyin
                `!twitch nowplaying` - Eğer varsa, oynatılmakta olan yayını gösterir
                `!twitch leave` - Ses kanalından çıkış yapar
                """),
                inline=False
            )
            e.add_field(
                name="Oyun İstatistikleri",
                value=textwrap.dedent("""\
                `!twitch overwatch <pc/psn/xbl> <player>` - Overwatch oyuncu istatistiklerini gösterir
                `!twitch fortnite <pc/psn/xbl> <player>` - Fortnite oyuncu istatistiklerini gösterir
                """),
                inline=False
            )
            e.add_field(
                name="Message Filter",
                value=textwrap.dedent("""\
                `!twitch filter set <sensitivity>` - Sunucu genelinde küfür filtresi ayarlar
                `!twitch filter remove` - Sunucu genelinde küfür filtresini kaldırır
                """),
                inline=False
            )
        class Errors:
            err_report = "Lütfen bu hatayı şu adresteki geliştiricilere bildirin: <https://link.twitchbot.io/support>."
            forbidden = emoji.cmd_fail + "Bunu yapmak için doğru iznim yok."
            not_found = emoji.cmd_fail + "Bu Discord kanalı bulunamadı. Etrafına <> koymadığından ve #bahset'tiğinden emin ol."
            not_started = "Twitch Bot halen başlatılıyor! Lütfen tekrar denemeden önce birkaç dakika bekleyin."
            check_fail = emoji.cmd_fail + "Bu komutu çalıştırma izniniz yok."
            cooldown = emoji.cmd_fail + "Bu komutu {time} saniye içinde çalıştırabilirsiniz."
            conn_closed = emoji.cmd_fail + "Ses bağlantısı kapatıldı. Sebep: `{reason}`"
            missing_arg = emoji.cmd_fail + " `{param}`parametresini unutuyorsunuz."
            too_many_requests = emoji.cmd_fail + "Üçüncü parti sunucular isteklerimizi yerine getirmekte zorlanıyorlar. Lütfen daha sonra tekrar deneyiniz."
        class Filter:
            cmd_usage = "Komut kullanımını görüntülemek için `!twitch help filter` yazın."
            need_donate = "Bu komutu yalnızca TwitchBot Premium üyeleri kullanabilir. Daha fazla bilgi edin: <https://twitchbot.io/premium>"
            invalid_sensitivity = "Hassaslık 85 ile 60 arasında olmalıdır."
            add_success = emoji.cmd_success + "Bu sunucunun küfür filtresi başarıyla ayarlandı."
            no_filter = emoji.cmd_fail + "Bu sunucu için küfür filtresi mevcut değil."
            del_success = emoji.cmd_success + "Bu sunucunun küfür filtresi başarıyla kaldırıldı."
        class Games:
            no_results = emoji.cmd_fail + "Hiçbir sonuç bulunamadı."
            no_stats_overwatch = emoji.cmd_fail + "Bu oyuncu için istatistik bulunamadı. Profiliniz özelse, herkese açık yapmadığınız sürece istatistiklerini göremezsiniz. Profilinizi herkese açık hale getirmek için lütfen <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> adresindeki adımları izleyin."
            no_stats_fortnite = emoji.cmd_fail + "Oyuncu bulunamadı. Kullanıcı adının yazılışını kontrol edin veya farklı bir platform deneyin."
            view_streams = "Yayınları görüntüleyin"
            top_games = emoji.twitch_icon + "En iyi oyunlar"
            top_games_desc = "{view_count} izleyiciler • {channel_count} kanal yayında"
            invalid_battletag = "Lütfen Battletag'inizi `name#id` biçiminde girin."
            invalid_platform = "Platform, `pc`, `psn`, veya `xbl`'den biri olmalıdır."
            incomplete_data = "Profil verileriniz eksik. Profiliniz özelse, herkese açık hale getirmek için <https://dotesports.com/overwatch/news/ow-public-private-profile-25347> adresindeki adımları izleyin, böylece istatistiklerinizi görüntüleyebilirsiniz."
            incomplete_data_short = "Bazı veriler eksik veya tamamlanmamış olabilir"
            generic_error = emoji.cmd_fail + "Bir hata oluştu:"
            powered_by_overwatch = "Powered by owapi.net"
            powered_by_fortnite = "Powered by fortnitetracker.com"
        class HelpCommand:
            e = discord.Embed(color=discord.Color(0x6441A4))
            e.title = emoji.twitch_icon + "**TwitchBot Yardım**"
            e.add_field(
                name="Komutlar",
                value="TwitchBot, `twitch` veya `!twitch` ile başlayan komutlara cevap verir. Çalıştırılabilir tüm komutları görüntülemek için `!twitch commands` yazın.",
                inline=False
            )
            e.add_field(
                name="Destek",
                value="TwitchBot konusunda yardıma ihtiyacınız olursa, [destek merkezini](https://support.twitchbot.io) ziyaret edebilir veya [destek sunucusuna](https://discord.gg/UNYzJqV) katılabilirsiniz.",
                inline=False
            )
            e.add_field(
                name="Web sitesi",
                value="TwitchBot ile ilgili bilgileri https://twitchbot.io adresinde görebilirsiniz.",
                inline=False
            )
            e.add_field(
                name="TwitchBot Premium",
                value="TwitchBot'un gelişimini destekleyin ve ayda yalnızca 5,00 ABD doları karşılığında bir dizi harika özellik ve avantaj elde edin. https://twitchbot.io/premium",
                inline=False
            )
            e.add_field(
                name="Oylama Yarışması",
                value="Her ayın sonunda ilk üç seçmene TwitchBot Premium'u BEDAVA veriyoruz! [Buraya oy verin](https://discordbots.org/bot/twitch/vote) ve [lider sıralamasını görüntüleyin](https://dash.twitchbot.io/leaderboard)",
                inline=False
            )
            e.add_field(
                name="Hakkında",
                value="TwitchBot, [Akira#4587](https://disgd.pw) tarafından discord.py kullanılarak oluşturuldu. Diğer katılımcıları görüntülemek için `twitch info` yazın.",
                inline=False
            )
            e.add_field(
                name="Diğer linkler",
                value="[SSS](https://twitchbot.io/faq) · [Gösterge Paneli](http://dash.twitchbot.io) · [Oyla](https://discordbots.org/bot/twitch/vote) · [Davet](https://discordapp.com/oauth2/authorize?client_id=375805687529209857&permissions=8&scope=bot&response_type=code&redirect_uri=https://twitchbot.io/?invited) · [Blog](https://medium.com/twitchbot)",
                inline=False
            )
        class General:
            avail_lang_title = "Mevcut Çeviriler"
            avail_lang_setmsg = "TwitchBot'un dilini ayarlamak için !twitch lang <language> yazın."
            stats_embed_title = emoji.twitch_icon + "TwitchBot İstatistikleri"
            stats_uptime = "Çalışma Süresi"
            stats_usage = "Kullanım"
            stats_version = "Versiyon"
            stats_shardinfo = "Shard Bilgisi"
            stats_system = "Sistem"
            stats_developer = "Geliştirici"
            stats_patrons = "Patronlar"
            stats_links = "Linkler"
            stats_links_desc = textwrap.dedent("""\
            **·** Website: https://twitchbot.io
            **·** Discord: https://discord.gg/UNYzJqV
            **·** Upvote: https://discordbots.org/bot/twitch/vote
            **·** Donate: https://patreon.com/devakira
            """)
            invite_msg1 = "**{user}**, beni bu bağlantıyla bir sunucuya davet edebilirsiniz: <https://link.twitchbot.io/invite>"
            invite_msg2 = "Yardıma mı ihtiyacınız var? Destek sunucusuna katılın: <https://link.twitchbot.io/support>"
            status_title = emoji.twitch_icon + "Twitch Durumu"
            status_cs = "Şu anki durum: `{status}`"
            lang_current = "TwitchBot için geçerli diliniz **{lang}**. Değiştirmek için, `!twitch lang <lang>` veya `!twitch lang help`yazın."
            lang_unavail = emoji.cmd_fail + "Bu çeviri mevcut değil. Mevcut dilleri görüntülemek için `!twitch lang help` yazın."
            lang_set = emoji.cmd_success + "TwitchBot diliniz başarıyla **{lang}** olarak ayarlandı."
        class Guild:
            submode_command_usage = "Komut kullanımını görüntülemek için `!twitch help sub_only` yazın."
            submode_success = emoji.cmd_success + "Yalnızca-abone modu bu sunucu için etkinleştirildi. Yeni kullanıcıların katılmak için {channel} 'a abone olması gerekecek. TwitchBot katılıp abone olmayan kullanıcılara DM gönderip, onları atmaya çalışacak. Not: mevcut üyeler atılmayacak."
            submode_kick = "Bu sunucu yalnızca-abone modunda. Katılmak için, {} abonesi olmanız gerekli. Twitch hesabınızı TwitchBot'a bağlamak için <https://dash.twitchbot.io> adresine gidin ve Twitch'in altındaki 'Hesap Bağla'ya basın."
            submode_kick_audit_log = "Yalnızca-abone modu bu sunucu için etkinleştirildi. Kapatmak için, '!twitch sub_only off' yazın."
            submode_del_success = emoji.cmd_success + "Yalnızca-abone modu bu sunucu için devre dışı bırakıldı."
            user_not_in_guild = emoji.cmd_fail + "Bu kullanıcı bu sunucuda değil."
            no_login_dash = emoji.cmd_fail + "{user} kullanıcısı henüz TwitchBot panosuna giriş yapmadı. Farklı bir kullanıcıdan kanal almak için, `!twitch sub_only on --user-id=(user id here)` yazın."
            no_link_dash = emoji.cmd_fail + "{user} Twitch kanalını TwitchBot panosuna bağlamadı. Farklı bir kullanıcıdan kanal almak için, `!twitch sub_only on --user-id = (user id here)` yazın."
            http_err_dash = emoji.cmd_fail + "TwitchBot gösterge panelinden bilgi almaya çalışırken bir hata oluştu: {error}"
        class LiveRole:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Canlı Rol - Yardım"
            command_usage.description = "Canlı Rol ile, canlı yayında kullanıcıları eklemek için bir rol belirleyebilirsiniz. Twitch Bot, kullanıcı akışı durdurduğunda rolü otomatik olarak kaldırır."
            command_usage.add_field(
                name = "Komutlar",
                value = textwrap.dedent("""\
                `!twitch live_role set` - Geçerli sunucuya Canlı Rol ayarlar
                `!twitch live_role filter` - Canlı Rolü, belirli bir rolü olan kullanıcılarla sınırlandırır
                `!twitch live_role delete` - Canlı Rol yapılandırmasını kaldırır
                `!twitch live_role view` - Hangi rolün kurulduğunu gösterir
                """)
            )
            no_role_mentioned = emoji.cmd_fail + "Herhangi bir rol belirtilmedi. Lütfen komutu yeniden çalıştırın ve bir rolden @bahsedin."
            not_set_up = emoji.cmd_fail + "Bu sunucu için hiçbir Canlı Rol ayarlanmadı. Bir tane ayarlamak için,`!twitch live_role set` yazın."
            role_not_found = emoji.cmd_fail + "Bu sorgu ile eşleşen bir rol adı yok. Sorgunuza `<`, `>` veya `@` gibi fazladan karakter koymayın."
            add_success = emoji.cmd_success + "Bu sunucuda Twitch’e yayına giren kullanıcılar ** {role} ** rolünü alır. Canlı Rol için bir filtre ayarlamak istiyorsanız, `!twitch live_role filter` yazın."
            del_success = emoji.cmd_success + "Canlı Rol yapılandırması bu sunucudan başarıyla kaldırıldı."
            filter_success = emoji.cmd_success + "Bu sunucunun Canlı Rol filtresi başarıyla ayarlandı. Tüm üyelerin rollerini güncellemek biraz zaman alabilir."
            missing_perms_ext = emoji.cmd_fail + "Bunu yapmak için **`Manage Roles`** iznine ihtiyacım var. İznim varsa, 'TwitchBot' adlı rolü, kurmak istediğiniz rolün üzerine getirdiğinizden emin olun."
            view_response = "Canlı Rol şu anda üyelere yayınlandıklarında ** {role} ** rolü verecek şekilde ayarlandı."
        class Notifs:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Yayıncı Bildirimleri - Yardım"
            command_usage.description = "Yayıncı Bildirimleri, bir Twitch kullanıcısı yayınlandığında gönderilen bir özelleştirilebilir mesaj ayarlamanıza izin verir."
            command_usage.add_field(
                name = "Komutlar",
                value = textwrap.dedent("""\
                `!twitch notif add [#discord_channel] [streamer_name] [message]` - Belirtilen kanala bir yayıncı için Yayıncı Bildirimi ekler
                `!twitch notif remove <#discord_channel> <streamer_name>` - Belirtilen kanal için bir yayıncının Yayıncı Bildirimini kapatır
                `!twitch notif list [#discord_channel]` - Belirtilen kanal için Yayıncı Bildirimlerini listeler
                `!twitch notif formatting` - Yayıncı Bildirimi iletilerine ekleyebileceğiniz değişkenleri gösterir
                """)
            )
            limit_reached = emoji.twitch_icon + "Selam! Maalesef bu sunucuya ekleyebileceğiniz maksimum bildirim miktarına ulaştınız. Daha fazla eklemek için <https://twitchbot.io/premium> adresinden bağış yapmanız gerekli."
            prompt1 = "Bildirimi hangi kanalda almak istiyorsunuz? Aşağıdakilerden birinin adını yazın veya @bahsedin. *(60 saniye içerisinde yanıtlayın)*"
            prompt2 = "Bildirimini ayarlamak istediğiniz Twitch kanalının adını yazın. *(60 saniye içerisinde yanıtlayın)*"
            prompt3 = "Kullanıcı canlı olduğunda görünmesini istediğiniz özel bir mesaj girin veya varsayılan mesaj için `default` yazın. *(180 saniye içerisinde yanıtlayın)*"
            text_channel_not_found = emoji.cmd_fail + "Bu metin kanalı bulunamadı. Komuttan çıkılıyor..."
            twitch_user_not_found = emoji.cmd_fail + "Bu Twitch kullanıcısı bulunamadı. Komuttan çıkılıyor ... "
            twitch_user_not_found_alt = emoji.cmd_fail + "Bu Twitch kullanıcısı yok. Adın etrafına fazladan hiçbir şey koymamaya dikkat edin (örneğin, `<>`gibi) ve bir Discord kullanıcısından @bahset'mediğinzden emin olun."
            response_timeout = "*Yanıt zaman aşımına uğradı.*"
            invalid_data = emoji.cmd_fail + "Twitch'ten geçersiz veri gönderildi:"
            malformed_user = emoji.cmd_fail + "Bu geçerli bir Twitch kullanıcısı gibi görünmüyor. Yalnızca alt çizgi, harf ve rakam ekleyebilirsin."
            default_msg = "<https://twitch.tv/{channel}> şimdi Twitch'te yayında!"
            del_fail = emoji.cmd_fail + "Bu kullanıcı için herhangi bir bildirim ayarlanmadı."
            del_success = emoji.cmd_success + "{User} yayına girdiğinde {channel} içerisinde herhangi bir bildirim almayacaksınız."
            add_success = emoji.cmd_success + "{Channel} içindeki {user} için bir bildirim eklendi."
            list_title = "**#{channel}** için yayıncı bildirimleri"
            list_embed_limit = "Özel iletiler mesaja dahil edilmedi, çünkü bir bölümde Discord tarafından ayarlanmış 1024 karakterlik bir sınır var. Kullanıcının yayına girdiğini göstermeye devam edecekler."
            no_notifs = "Bu kanal için herhangi bir Yayıncı Bildirimi ayarlanmadı."
            notifications = "Bildirimler"
            bulk_delete_confirm = "**{channel} kanalından {count} bildirimi silmek üzeresin.** Bunu yapmak istediğinden emin misin? Devam etmek istiyorsan `yes` yazarak yanıtlayın."
            bulk_delete_success = emoji.cmd_success + "{channel} kanalından başarıyla {count} bildirim silindi."
            command_cancelled = "Komut iptal edildi."
            notif_variables = discord.Embed(color=discord.Color(0x6441A4))
            notif_variables.title = "Bildirim mesajı değişkenleri"
            notif_variables.description = "Bir akış bildirim mesajına veri eklemek için aşağıdaki değişkenlerden birini kullanın."
            notif_variables.add_field(
                name = "Mevcut biçimlendirme",
                value = textwrap.dedent("""\
                *`$title$`* - Yayın başlığı
                *`$viewers$`* - Şu anda yayını izleyen kişi sayısı
                *`$game$`* - Yayıncının şu anda oynadığı oyun
                *`$url$`* - Kanalın URL'si
                *`$name$`* - Kanal adı
                *`$everyone$`* - Bir @everyone bahsetme komutu ekler
                *`$here$`* - Bir @here bahsetme komutu ekler
                """)
            )
        class Permissions:
            user_need_perm = emoji.cmd_fail + "Bunu yapmak için **{permission}** iznine ihtiyacınız var."
            bot_need_perm = emoji.cmd_fail + "Bunu yapmak için **{permission}** iznine ihtiyacım var."
            no_pm = emoji.cmd_fail + "Bu komutu yalnızca bir sunucuda kullanabilirsiniz."
        class Streams:
            command_usage = discord.Embed(color=discord.Color(0x6441A4))
            command_usage.title = "Yayın Komutları - Yardım"
            command_usage.add_field(
                name = "Komutlar",
                value = textwrap.dedent("""\
                `!twitch stream user <user>` - Bir kullanıcının yayın bilgisini alır
                `!twitch stream watch <user>` - Discord'dan bir Twitch yayını izleyin
                `!twitch stream game <name>` - Birinin belirtilen oyuna ait yayınını izleyin
                `!twitch stream top` - En iyi yayınların bilgisini verir
                """)
            )
            game_desc = "Check out {user} playing {game} for {view_count} viewers:\nhttps://twitch.tv/{user}"
            game_desc = "{user}, {view_count} izleyici için {game} oynuyor. \nhttps://twitch.tv/{user}"
            game_not_found = emoji.cmd_fail + "Bu oyun bulunamadı."
            game_no_streams = emoji.cmd_fail + "Kimse bu oyunu yayınlamıyor."
            live = "Twitch'te yayında"
            stream_not_found = emoji.cmd_fail + "Bu kullanıcı mevcut değil veya çevrimiçi değil. Yalnızca kullanıcının adını girdiğinizden ve `()` veya `<>`. gibi fazladan bir şey girmediğinizden emin olun."
            stream_desc = textwrap.dedent("""\
            {view_count} izleyici için {game} oynuyor
            **[Twitch'de izleyin](https://twitch.tv/{channel})** veya `twitch stream watch {channel}` yazın

            Yayın Önizlemesi:
            """)
        class Users:
            connections = "{User} için bağlantılar"
            connected = "{Account} ile bağlanıldı"
            following = "Takipçiler"
            live = "Şu anda canlı"
            playing = "{view_count} izleyici için {game} oynuyor"
            not_connected = "Bağlı değil"
            not_live = "Şu anda Çevrimdışı"
            no_login_dash = "Bu kullanıcı [TwitchBot panosu] ziyaret etmedi.(http://dash.twitchbot.io)"
            streamer_id = "Yayıncı Kimliği"
            views = "Görüntülemeler"
            view_profile = "Twitch Profilini Görüntüle"
            unknown = "Bilinmeyen"
            watch_on_twitch = "Twitch'de izle"
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

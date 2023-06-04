# DoH - DNS over HTTPS

DoH queries resolve over HTTPS for privacy, performance, and security. DoH also makes it easier to use a name server of your choice instead of the one configured for your system.

# Spec

[RFC 8484 - DNS Queries over HTTPS (DoH)](https://tools.ietf.org/html/rfc8484)

# Publicly available servers

| Who runs it | Base URL | Working*| Comment |
|-------------|----------|---------|---------|
| **A**
|[aaflalo.me](https://www.aaflalo.me/2019/01/dns-over-https-server-aaflalo-me/) | Server US: <br>https://dns-nyc.aaflalo.me/dns-query | :heavy_check_mark:  | Runs on Star Brilliant's [dns-over-https](https://github.com/m13253/dns-over-https) <br> Checks for DNSSEC and block advertising |
|[AaronPlayz](https://aaronplayzgaming.com/)|https://dns.aaronplayzgaming.com/dns-query|:heavy_check_mark:|Ad & porn blocking
|aattwwss|https://aattwwss.duckdns.org/dns-query|:heavy_check_mark:|Adblocking
| abel.waringer-atg.de | https://abel.waringer-atg.de/dns-query | :heavy_check_mark:| 
| [Absolight](https://www.absolight.fr/) | https://res-acst1.absolight.net/dns-query <br> https://res-acst3.absolight.net/dns-query <br> https://resolver1.absolight.net/dns-query <br> https://resolver3.absolight.net/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | 
|abstergo.it|https://block.abstergo.it/dns-query|:heavy_check_mark:|Adblocking
|[AdFilter](https://adfilter.net/)|Adelaide: https://adl.adfilter.net/dns-query<br>Perth: https://per.adfilter.net/dns-query<br>Sydney: https://syd.adfilter.net/dns-query|:heavy_check_mark:<br>:heavy_check_mark:<br>:heavy_check_mark:|Adblocking, aggregated statistics kept for 30 days
| [AdGuard](https://adguard-dns.io/en/public-dns.html)     | Default: https://dns.adguard-dns.com/dns-query <br> Family protection: https://family.adguard-dns.com/dns-query <br> Uncensored: https://unfiltered.adguard-dns.com/dns-query <br> | :heavy_check_mark: <br>  :heavy_check_mark: <br> :heavy_check_mark: |Default provides ad-blocking at DNS level, while Family protection adds adult site blocking. DNSSEC enabled and TLS 1.3 | 
|[Adrian Lam](https://adrianlam.com/)|https://dns.adrianlam.com/dns-query|:heavy_check_mark:|Adblocking
|[Agadez.net – Speed Thrills](https://agadez.net/)|https://adguard.agadez.net/dns-query|:heavy_check_mark:|
|agh-dns.net|https://ams.nl.agh-dns.net/dns-query|:heavy_check_mark:|Adblocking
|[AhaDNS Blitz](https://ahadns.com/blitz/)| Uncensored : https://blitz.ahadns.com <br> OISD filter : https://blitz.ahadns.com/1:1 <br> OISD & Energized Porn filter : https://blitz.ahadns.com/1:1.12 | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark:| [Customizable](https://blitz-setup.ahadns.com/) globally distributed DoH-only server with no logging |
| [AhaDNS](https://ahadns.com) | Netherland:<br> https://doh.nl.ahadns.net/dns-query | :heavy_check_mark: | Deprecated in favor of AhaDNS Blitz |
|aidentec.top|https://adtec.aidentec.top/dns-query|:heavy_check_mark:|
|aizi.app|https://www.aizi.app/dns-query|:heavy_check_mark:|
| [alekberg](https://alekberg.net) | Amsterdam Non-filtering: https://dnsnl.alekberg.net/dns-query <br> Sweden Non-filtering: https://dnsse.alekberg.net/dns-query <br> Amsterdam Adblocking: https://dnsnl-noads.alekberg.net/dns-query <br> Sweden Non-filtering: https://dnsse-noads.alekberg.net/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark:| DoH Servers in Spain, Holland and Sweden. No logging, DNSSEC support.|
|[Alibaba Public DNS](https://www.alidns.com/)| https://dns.alidns.com/dns-query | :heavy_check_mark:| [DoH/DoT/DNS Json API](https://www.alidns.com/faqs/#dns-safe), Best DoH/DoT server in China |
| Almir1904 | https://dns.almir1904.eu/dns-query | :heavy_check_mark: | Adblocking
|altapo.ru|https://link.altapo.ru/dns-query|:heavy_check_mark:|
|amlegion.org|https://mailer.amlegion.org/dns-query|:heavy_check_mark:|Adblocking
|[Andrew](https://andrewnw.xyz/)|https://dns.andrewnw.xyz/dns-query|:heavy_check_mark:|Ad & porn blocking
|[Andrews & Arnold](https://aa.net.uk/dns) | https://dns.aa.net.uk/dns-query | :heavy_check_mark: | no logging (see [DNS Disclaimer](https://www.aa.net.uk/legal/dohdot-disclaimer/))|
| Apem Legit | https://d.apemlegit.my.id/dns-query | :heavy_check_mark: | Adblocking
|[ArashiDNS](https://arashi.eu.org/)|https://arashi.eu.org/dns-query|:heavy_check_mark:|
|armorrush|https://armorrush.eu.org/dns-query|:heavy_check_mark:|Adblocking
| [Artikel10](https://dns.artikel10.org/) | https://dns.artikel10.org/dns-query | :heavy_check_mark: | Non-logging service based in Germany
| [Asteroid B612](https://b612.me/) | https://dns.b612.me/dns-query | :heavy_check_mark: |
| [Avast](https://www.avast.com/dns) | https://secure.avastdns.com/dns-query | :heavy_check_mark: | Non-logging
|[Aviontex](https://keweon.center/)|https://dns.keweon.center/dns-query|:heavy_check_mark:|Adblocking
| [Awan.ftp.sh](https://awan.ftp.sh/) | Ads and gambling blocking : https://awan.ftp.sh/dns-query <br> Ads, gambling, drug, tobacco block : https://awan.ftp.sh/no-vice <br> Porn, ads, gambling, drug, tobacco block : https://awan.ftp.sh/noporn-cl <br> Unblocked : https://awan.ftp.sh/unblocked | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | Based in Japan
|aws.ketan.dev|https://pihole.aws.ketan.dev/dns-query|:heavy_check_mark:|Adblocking
| **B**
| [Bancuh](https://blog.bancuh.com/adblock-dns/) | Singapore:<br> https://sg-dns1.bancuh.com/dns-query <br> France:<br> https://fr-dns1.bancuh.com/dns-query <br> Tokyo:<br> https://jp-dns1.bancuh.com/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | Adblocking, porn blocking, log available for originating IP
| [BebasDNS](https://github.com/bebasid/bebasdns) | Singapore:<br> https://dns.bebasid.com/dns-query | :heavy_check_mark: | DNS-based ad-blocking service
| [Belnet](https://dns.belnet.be/) | https://dns.belnet.be/dns-query | :heavy_check_mark: | IP, response code, protocol, and response time are logged for performance & statistic purposes. Hosted in Belgium by the Belgian National Research and Education Network.
|[benpro](https://benpro.fr/)|https://dns.benpro.fr/dns-query|:heavy_check_mark:|Ad & porn blocking
|bit-trail.nl|https://ns3.bit-trail.nl/dns-query|:heavy_check_mark:|Adblocking
| Bitdefender | https://dns.bitdefender.net/dns-query | :heavy_check_mark: |
| [Blahdns](https://blahdns.com/) | Switzerland: <br>https://doh-ch.blahdns.com/dns-query <br> Finland: <br>https://doh-fi.blahdns.com/dns-query <br> Germany: <br>https://doh-de.blahdns.com/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | Based on [Go implementation](https://github.com/m13253/dns-over-https), HAProxy + Dnsdist + Knot-resolver with DNSSEC, No ECS, No logs, Adblock
| [BlissDNS](https://github.com/BlissDNS) | https://us1.blissdns.net/dns-query | :heavy_check_mark: | Adblocking, queries logged for 24 hours
| [Blokada DNS](https://community.blokada.org/t/the-benefits-of-blokada-dns/6646) | https://dns.blokada.org/dns-query | :heavy_check_mark: | No logging.
|bluemood|https://bluemood.me/dns-query|:heavy_check_mark:|Adblocking
|[Bob Strecansky](https://bobstrecansky.com/)|https://dns.bobstrecansky.com/dns-query|:heavy_check_mark:|Ad & porn blocking
|boje8.me|https://doh.boje8.me/dns-query|:heavy_check_mark:|Adblocking
| [Bortzmeyer](https://www.bortzmeyer.org/doh-bortzmeyer-fr-policy.html) | https://doh.bortzmeyer.fr | :heavy_check_mark: | French-based, non-logging. 
|bosco.ovh|https://cloudns.bosco.ovh/dns-query|:heavy_check_mark:|Adblocking
| [Brahma World](https://dns.brahma.world/home.html) | https://dns.brahma.world/dns-query | :heavy_check_mark: | No logging • Blocks Ads + Trackers + Malware + Phishing domains, DNSSEC ready • QNAME Minimization • No EDNS Client-Subnet
|[BT](https://bt.com)|https://doh.bt.com|:heavy_check_mark:|
| [Bunny](https://bunny.net/) | https://doh1.b-cdn.net/dns-query | :heavy_check_mark: | Adblocking
|bw.i81.ru|https://dns.bw.i81.ru/dns-query|:heavy_check_mark:|Adblocking
| **C**
| C-dns | https://www.c-dns.com/dns-query | :heavy_check_mark: | 
|[carson-family.com](https://carson-family.com/)|https://dns.carson-family.com/dns-query|:heavy_check_mark:|Ad & porn blocking
|cbio.top|https://dns2.cbio.top/dns-query|:heavy_check_mark:|Adblocking
| Ccb-net | https://doh.ccb-net.it | :heavy_check_mark: | Adblocking 
| Charter | California: <br>https://doh-01.spectrum.com/dns-query <br> Texas: <br>https://doh-02.spectrum.com/dns-query |:heavy_check_mark:<br>:heavy_check_mark:| Trial - Testing multiple platforms
|[chenu.ch](https://chenu.ch/)|https://dns.chenu.ch/dns-query|:heavy_check_mark:|Adblocking
| Chromeina | https://dns.chromeina.top/dns-query | :heavy_check_mark: | Adblocking 
| [CIRA Canadian Shield](https://www.cira.ca/cybersecurity-services/canadian-shield) | Private: <br>https://private.canadianshield.cira.ca/dns-query <br> Protected: <br>https://protected.canadianshield.cira.ca/dns-query <br> Family: <br>https://family.canadianshield.cira.ca/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | Supports DNSSEC, keeps DNS traffic inside Canada. <br> Private: DNS resolution service that keeps your DNS data private from third-parties. <br> Protected: Includes Private features and adds malware and phishing blocking. <br> Family: Includes Protected and Private features and blocks pornographic content. |
| [Cisco Umbrella (OpenDNS)](https://support.opendns.com/hc/en-us/articles/360038086532-Using-DNS-over-HTTPS-DoH-with-OpenDNS) | Standard: https://doh.opendns.com/dns-query <br> FamilyShield (blocks adult content):  https://doh.familyshield.opendns.com/dns-query | :heavy_check_mark: <br><br> :heavy_check_mark:| DNSSEC, Anycast
| Clanless.ovh | https://dns.clanless.ovh/dns-query | :heavy_check_mark:| Adblocking
| [CleanBrowsing](https://cleanbrowsing.org/help/docs/dnsoverhttps/) | https://doh.cleanbrowsing.org/doh/family-filter/ <br><br> Filter that allows some mixed-content sites: https://doh.cleanbrowsing.org/doh/adult-filter/ <br><br> Malware blocking only: https://doh.cleanbrowsing.org/doh/security-filter/ | :heavy_check_mark: | anycast DoH server with parental control (restricts access to adult content + enforces safe search)
|[CLEARVIEW](https://clearviewtechnology.net/)|https://cvt-ic-us-adns-001.clearviewtechnology.net/dns-query|:heavy_check_mark:|Adblocking
| [Cloudflare](https://developers.cloudflare.com/1.1.1.1/)  | https://cloudflare-dns.com/dns-query <br><br> Mozilla: https://mozilla.cloudflare-dns.com/dns-query <br><br> Block Malware: https://security.cloudflare-dns.com/dns-query <br><br> Block Malware and Adult Content: https://family.cloudflare-dns.com/dns-query <br><br> DNS64: https://dns64.cloudflare-dns.com/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | Supports both -04 and -13 content-types
|cloudnx.cloud|https://dns-secondary.cloudnx.cloud/dns-query|:heavy_check_mark:|
| Comcast | https://doh.xfinity.com/dns-query | :heavy_check_mark:| DNSSEC Validation, [DNS Privacy Policy](https://www.xfinity.com/privacy/policy/dns) |
|[comeonjames.club](https://comeonjames.club/)|https://dns.comeonjames.club/dns-query|:heavy_check_mark:|Adblocking
| [Computer Incident Response Center Luxembourg](https://circl.lu/) | https://dns.circl.lu/dns-query | :heavy_check_mark:| 
| [Comss](https://www.comss.ru/page.php?id=7315) | https://dns.comss.one/dns-query | :heavy_check_mark: | Block ads, tracker, phishing and malware
| [ControlD](https://controld.com/) | Unfiltered: <br>https://freedns.controld.com/p0 <br> Block Malware: <br>https://freedns.controld.com/p1 <br> Block Malware + Ads: <br>https://freedns.controld.com/p2 <br> Block Malware + Ads + Social: <br>https://freedns.controld.com/p3 <br> Block Malware, Ads, Adult content: <br>https://freedns.controld.com/family <br> OISD: <br>https://freedns.controld.com/x-oisd | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | ControlD is a fully customizable anycast DNS service that allows you to not only block annoyances like malware, tracking, ads, IoT telemetry, and more but also unblock over 180 services through a network of proxies in over 100 cities.
|cossxiu|https://cossxiu.ga/dns-query|:heavy_check_mark:|Adblocking
|cretu.xyz|https://dns.cretu.xyz/dns-query|:heavy_check_mark:|Adblocking
|crownor.com|https://dns.crownor.com/dns-query|:heavy_check_mark:|Adblocking
|[CryptoMize](https://cryptomize.com/)|https://dns.cryptomize.com/dns-query|:heavy_check_mark:|
|cwlys.com|https://dns.cwlys.com/dns-query|:heavy_check_mark:|Ad & porn blocking
|[CynthiaLabs](https://cynthialabs.net/)|https://dns.cynthialabs.net/dns-query|:heavy_check_mark:|Adblocking
| [CZ.NIC](https://www.nic.cz/odvr/) | https://odvr.nic.cz/dns-query | :heavy_check_mark:| Runs on [Knot Resolver](https://www.knot-resolver.cz/) (`doh2`), supports DNSSEC, provided by `.cz` TLD operator
| **D**
|d94.xyz|https://dns.d94.xyz/dns-query|:heavy_check_mark:|Adblocking
|d96.info|https://dns.d96.info/dns-query|:heavy_check_mark:|Adblocking
| [Daniel Woffinden](https://daw.dev/) | https://dns.daw.dev/dns-query | :heavy_check_mark: | Adblocking
| [Danielle McLean](https://00dani.me/) | https://ns.00dani.me/dns-query | :heavy_check_mark: |
|darkness.is.my.waifu|https://darkness.is.my.waifu.cz/dns-query|:heavy_check_mark:|
| [data.haus](https://data.haus/) | https://mail.data.haus/dns-query | :heavy_check_mark: | Adblocking, non-logging
| [DataCore](https://datacore.ch/website/page/frontpage) | https://doh.datacore.ch/dns-query | :heavy_check_mark: | Adblocking
| [Datahata.by](https://doh.datahata.by/) | https://doh.datahata.by/dns-query | :heavy_check_mark: |
|datamatter.co.za|https://pihole.datamatter.co.za/dns-query|:heavy_check_mark:|Adblocking
| ddns.network | https://adguard.ddns.network/dns-query | :heavy_check_mark:|Adblocking
|[Decisive DevOps](https://decisivedevops.com/)|https://dns.decisivedevops.com/dns-query|:heavy_check_mark:|Adblocking
| [Decloudus](https://decloudus.com/) |  https://dns.decloudus.com/dns-query | :heavy_check_mark: | Based in Germany. Adblocking
| Dekonix.ru | https://adguard.dekonix.ru/dns-query | :heavy_check_mark: | Adblocking
|depieri.net|https://adguard.depieri.net/dns-query|:heavy_check_mark:|Ad & porn blocking
|dessoi.cloud|https://adguard.dessoi.cloud/dns-query|:heavy_check_mark:|Adblocking
| [Detoxify Porn Blocker](https://detoxifypornblocker.com/) | https://doh-primary-pool.detoxifypornblocker.com/dns-query | :heavy_check_mark: | Block ads and porn
|dewed.de|https://mainframe.dewed.de/dns-query|:heavy_check_mark:|Adblocking
|dgca.myds.me|https://dgca.myds.me/dns-query|:heavy_check_mark:|Adblocking
|dgea.fr|https://dns.dgea.fr/dns-query|:heavy_check_mark:|Adblocking
| [Digitale Gesellschaft](https://www.digitale-gesellschaft.ch/) |  https://dns.digitale-gesellschaft.ch/dns-query | :heavy_check_mark: | No query/IP logging, no filtering, QNAME minimization, TLS 1.3, DNSSEC; https://www.digitale-gesellschaft.ch/dns/ |
| Disconnect.app | https://doh.disconnect.app/dns-query | :heavy_check_mark: | 
| [dns0.eu](https://www.dns0.eu/) | Non-blocking: https://open.dns0.eu<br>Malware blocking: https://dns0.eu<br>Hardened security: https://zero.dns0.eu<br>Child safe: https://kids.dns0.eu | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark:| Non-logging, GDPR compliant
| [DNS For Family](https://dnsforfamily.com/#DNS_Servers_DNS_Over_HTTPS) | https://dns-doh.dnsforfamily.com/dns-query | :heavy_check_mark: | Filter websites for family use, and enforces safe search in Google, YouTube, Bing, DuckDuckGo and Yandex. DNSSEC-ready, non-logging
| [dns.digitalsize.net](https://dns.digitalsize.net/) | https://dns.digitalsize.net/dns-query | :heavy_check_mark: | A public, non-tracking, non-filtering DNS resolver with DNSSEC enabled and hosted in Germany |
| dns.linkr.ninja | https://dns.linkr.ninja/dns-query | :heavy_check_mark: | Adblocking
|dns.nomu.pw|https://ttag.dns.nomu.pw/dns-query|:heavy_check_mark:|Adblocking
| [DNS.SB](https://dns.sb/doh/) | https://doh.dns.sb/dns-query <br> https://doh.sb/dns-query | :heavy_check_mark: <br> :heavy_check_mark:| DNSSEC & QNAME minimization enabled, no logging |
|dns.terumi.club|https://apne1.dns.terumi.club/dns-query|:heavy_check_mark:|Adblocking
|[DNS4all](https://dns4all.eu/)|https://doh.dns4all.eu/dns-query|:heavy_check_mark:| Non-logging
| [dns4me](https://dns4me.net/) | https://nz01.dns4me.net <br> https://au01.dns4me.net <br> https://au02.dns4me.net <br> https://sg01.dns4me.net <br> https://uk01.dns4me.net <br> https://us01.dns4me.net <br> https://us02.dns4me.net <br> https://sa01.dns4me.net <br> https://ca01.dns4me.net <br> https://ca02.dns4me.net | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: |
|dnsadguard.co.uk|https://www.dnsadguard.co.uk/dns-query|:heavy_check_mark:|Adblocking
| [dnscrypt.ca](https://dnscrypt.ca/) | https://dns1.dnscrypt.ca:453/dns-query | :heavy_check_mark:| Canadian, uncensored, no-logs, encrypted, and DNSSEC
| dnsenc.com | https://dnsenc.com/dns-query | :heavy_check_mark:| Adblocking
| [dnsforge.de](https://dnsforge.de/) | https://dnsforge.de/dns-query |:heavy_check_mark:|  No logging. Support DNSSEC. Hosted in Germany|
| [dnsHome.de](https://www.dnshome.de/doh-dot-public-resolver.php) |  https://dns.dnshome.de/dns-query | :heavy_check_mark:| DoH Server in Germany. No logging, No filtering, DNSSEC and own DNS Resolver |
| [dnslow.me](https://dnslow.me/) | https://dnslow.me/dns-query | :heavy_check_mark: | A protective DNS that blocks Ads, Malware, Trackers, Phishing and Newly Registered Domains. Randomly forward requests to different upstreams for enhanced privacy. |
| [DNSPod](https://docs.dnspod.cn/public-dns/dot-doh/) | https://dns.pub/dns-query | :heavy_check_mark: | Operated by Tencent Cloud
| [dnswarden](https://dnswarden.com)| Adblock - <br> https://dns.dnswarden.com/adblock <br><br> Uncensored -<br> https://dns.dnswarden.com/uncensored <br><br> AdultFilter - <br>  https://dns.dnswarden.com/adultfilter | <br>:heavy_check_mark:<br><br><br>:heavy_check_mark:<br><br><br>:heavy_check_mark: | A zero logging DNS with support for DNS-over-HTTPS (DoH), DNS-over-TLS (DoT) & Dnscrypt. Supports DNSSEC, TLS 1.3, QNAME minimization and does own Recursion. EDNS Client Subnet is disabled.<br> Provides 4 different types of filtering options.<br> Adblock - Blocks ads, trackers, viruses, and telemetry.<br> Adultfilter - Blocks adult content, enforces safe search, and includes all the features from adblock. <br> Uncensored - Unrestricted access/no filtering.<br>[Custom Filter](https://dnswarden.com/customfilter.html) where you can choose your own filter lists! <br>For more information look [here](https://github.com/bhanupratapys/dnswarden) or [here](https://dnswarden.com). |
|doh.best|https://dns.doh.best/dns-query|:heavy_check_mark:|Adblocking
|dscloud.me|https://doh.dscloud.me/dns-query|:heavy_check_mark:|Adblocking
| [Dukun.de](https://dukun.de/) |https://dukun.de/dns-query | :heavy_check_mark: |
|[DutchWhite](https://dutchwhite.nl/)|https://dns.dutchwhite.nl/dns-query|:heavy_check_mark:|Adblocking
| **E**
|[EasyMosdns](https://doh.apad.pro/)|https://doh.apad.pro/dns-query|:heavy_check_mark:|
|ebner.tech|https://dns.ebner.tech/dns-query|:heavy_check_mark:|
| [Edgy DNS](https://edgy.network/dns) | https://edgy-dns.com/dns-query | :heavy_check_mark: | Adblocking
|edison42.dev|https://dns.edison42.dev/dns-query|:heavy_check_mark:|Adblocking
|ef67daisuki.club|https://adguard.ef67daisuki.club/dns-query|:heavy_check_mark:|Adblocking
|elbschloss.xyz|https://hole.elbschloss.xyz/dns-query|:heavy_check_mark:|Adblocking
| [Elemental Software](https://elemental.software/) | https://dns.elemental.software/dns-query | :heavy_check_mark: |
|[Elli](https://ellichua.com/)|https://dns.ellichua.com/dns-query|:heavy_check_mark:|Ad & porn blocking
| [Emiliyan Parvanov](https://emiliyan.com/) | https://dns.emiliyan.com/dns-query | :heavy_check_mark: | Adblocking
|[Extrawdw](https://extrawdw.net/)|https://dns.extrawdw.net/dns-query|:heavy_check_mark:|Adblocking
| **F**
| [FAELIX](https://faelix.net/) | https://rdns.faelix.net/ <br> Adblocking: https://pdns.faelix.net/ | :heavy_check_mark: <br> :heavy_check_mark: | No logging, based on dnsdist-doh RC querying our powerdns-recursor resolvers, multiple nodes in UK and CH, [more info](https://faelix.net/ref/dns/#resolving-nameservers) |
|[Familia](https://familiamv.ml/)|https://dnsvps.familiamv.ml/dns-query|:heavy_check_mark:|Adblocking
| Fancyorg.at | https://dns.fancyorg.at/dns-query |  :heavy_check_mark: | Adblocking
|faze.dev|https://dns.faze.dev/dns-query|:heavy_check_mark:|Adblocking
| [FDN](https://www.fdn.fr/) - French Data Network | https://ns0.fdn.fr/dns-query <br> https://ns1.fdn.fr/dns-query |:heavy_check_mark:| No log, no filter, DNSSEC, … ([more informations in French](https://www.fdn.fr/ouverture-des-services-dot-doh/)) |
|[ff0x](https://ff0x.ca/)|https://ag.ff0x.ca/dns-query|:heavy_check_mark:|Adblocking
| [ffmuc.net](https://ffmuc.net/wiki/doku.php?id=knb:dohdot_en) | https://doh.ffmuc.net/dns-query | :heavy_check_mark:| DoH-Server of Freifunk München. No logging, no filter, DNSSEC, own recursion. More in our [wiki](https://ffmuc.net/wiki/doku.php?id=knb:dohdot_en) | 
|[FilipCCz.eu](https://filipccz.eu/)|https://dns.filipccz.eu/dns-query|:heavy_check_mark:|Adblocking
| Flm9.net | https://dns01.flm9.net/dns-query |  :heavy_check_mark: |
| [floDNS](https://www.flodns.com/get-started/) | https://ns1.flodns.net/dns-query <br> https://ns2.flodns.net/dns-query | :heavy_check_mark: <br> :heavy_check_mark: | All queries are logged for statistical analysis by [TalkDNS](https://www.talkdns.com/)
|flwagners.com|https://dns.flwagners.com/dns-query|:heavy_check_mark:|Ad & porn blocking
|[fmipauns](https://mipauns.com/)|https://dns.mipauns.com/dns-query|:heavy_check_mark:|Ad & porn blocking
|fomichev.cloud|https://gateway.fomichev.cloud/dns-query|:heavy_check_mark:|Adblocking
| [Foundation for Applied Privacy](https://applied-privacy.net) | https://doh.applied-privacy.net/query | :heavy_check_mark:| No query/IP logging, no filtering, QNAME minimization, no EDNS client subnet, TLS 1.3, DNSSEC, RFC7706, RFC8198; https://applied-privacy.net/services/dns/ |
|foximao.cn|https://dns.foximao.cn/dns-query|:heavy_check_mark:|Adblocking
| [Fresh Waffles](https://fresh-waffles.online/) | https://adguard.fresh-waffles.online/dns-query | :heavy_check_mark: | Adblocking
| [Froth.zone](https://dns.froth.zone/resolver) | https://dns.froth.zone/dns-query | :heavy_check_mark: | OpenNIC
| [FutaDNS](https://site.futa.gg/) | https://doh.futa.gg/dns-query | :heavy_check_mark: | Based in Taiwan, query logged for 24 hours, adblocking.
| **G**
|[Galuh Multidata Solution](https://gms.net.id/)|https://dns2.gms.net.id/dns-query|:heavy_check_mark:|
|gbrossi.com.br|https://adguard.gbrossi.com.br/dns-query|:heavy_check_mark:|Adblocking
|giize.com|https://bvo.giize.com/dns-query|:heavy_check_mark:|
|[GloryDNS](https://dns.glorydns.com/)|https://dns.glorydns.com/dns-query|:heavy_check_mark:|Ad & porn blocking
| [Gnb09](https://www.gnb09.id/) | https://dns.gnb09.id/dns-query | :heavy_check_mark: | Ad & porn blocking
|[Goldplate](https://goldplate.org/)|https://dns.goldplate.org/dns-query|:heavy_check_mark:|Adblocking
| [Google](https://developers.google.com/speed/public-dns/docs/doh) | https://dns.google/dns-query <br> DNS64: https://dns64.dns.google/dns-query <br> https://8888.google/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark:| Full RFC 8484 support, EDNS, no filtering.
|gosami.xyz|https://vpn.gosami.xyz/dns-query|:heavy_check_mark:|
|greenet.id|https://addguard.greenet.id/dns-query|:heavy_check_mark:|
|gslb2.xfinity.com|https://doh2.gslb2.xfinity.com/dns-query|:heavy_check_mark:|
| [Gustavus Adolphus College](https://gustavus.edu/) | https://cluster-0.gac.edu/dns-query <br> https://cluster-1.gac.edu/dns-query | :heavy_check_mark: <br> :heavy_check_mark:| 
|gztech|https://gztech.me/dns-query|:heavy_check_mark:|Adblocking
| **H**
| [HafidzRadhivalDNS](https://server.hafidzradhival.my.id/) | https://dns.hafidzradhival.my.id/dns-query | :heavy_check_mark: |
| [Hanahira](https://dns.hanahira.dev/) | https://dns.hanahira.dev:4433/dns-query | :heavy_check_mark: | Adblocking
| [HaNeulo](https://haneulo.com/) | https://adguard.haneulo.com/dns-query | :heavy_check_mark: | Adblocking
|haoxuan.xyz|https://dns.haoxuan.xyz/dns-query|:heavy_check_mark:|Adblocking
| [HeliumCloud](https://servers.opennic.org/edit.php?srv=ns2.nj.us.dns.opennic.glue) | https://us-ny-alula.heliumcloud.cc/dns-query | :heavy_check_mark: | OpenNIC
| [Hinet](https://hinet.net/) | https://dns.hinet.net/dns-query | :heavy_check_mark: | Run by Taiwanese ISP
| [hitian.me](https://hitian.me/) | https://hitian.me/dns-query | :heavy_check_mark: | Hosted in Singapore
| [Hoerli.NET](https://hoerli.net/hoerlis-pi-holes-fuers-internet/) | Falkenstein <br> https://pihole1.hoerli.net/dns-query <br> Frankfurt <br> https://pihole2.hoerli.net/dns-query <br> Baden-Baden <br> https://pihole4.hoerli.net/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | Adblocking, no logging
|home27|https://home27.duckdns.org/dns-query|:heavy_check_mark:|Adblocking
|[Hoofoo](https://hoofoo.icu/)|https://hoofoo.icu/dns-query|:heavy_check_mark:|
| [Hostux.net](https://dns.hostux.net) |  Uncensored DNS: <br> https://dns.hostux.net/dns-query <br> Adblocking DNS: <br> https://dns.hostux.net/ads | :heavy_check_mark: <br> :heavy_check_mark: |DNSSEC, no EDNS Client-Subnet, not logging queries' content, hosted in Luxembourg.
| Huque | https://doth.huque.com/dns-query | :heavy_check_mark: | 
| [Hurricane Electric (he.net)](https://he.net)  | https://ordns.he.net/dns-query | :heavy_check_mark:| Also supports DoT and TLS 1.3, Does NOT support DNSSEC. Anycast servers. |
| **I**
|[iBakerServer](https://ibakerserver.pt/)|https://dns-public.ibakerserver.pt/dns-query|:heavy_check_mark:|Adblocking
|[ihatemy.live](https://ihatemy.live/)|https://adguard.ihatemy.live/dns-query|:heavy_check_mark:|Adblocking
| ihctw | https://ihctw.synology.me/dns-query | :heavy_check_mark: | Adblocking
| [iKuuu VPN](https://ikuuu.co/) | https://doh.buzz/dns-query <br> https://doh.beauty/dns-query | :heavy_check_mark: <br> :heavy_check_mark: | 
|imaicool.com|https://dns.imaicool.com/dns-query|:heavy_check_mark:|Adblocking
|imbuffering.com|https://noads.imbuffering.com/dns-query|:heavy_check_mark:|Adblocking
| [In-Berlin](https://www.in-berlin.de/) | https://dns1.in-berlin.de/dns-query | :heavy_check_mark: |
| Indus.me | https://dns.indust.me/dns-query | :heavy_check_mark: | 
| [Institut national de recherche en sciences et technologies du numérique](https://www.inria.fr/fr) | https://qlf-doh.inria.fr/dns-query | :heavy_check_mark: |
| [Institute of Operating Systems and Computer Networks](https://wiki.ibr.cs.tu-bs.de/en/services) | https://doh.ibr.cs.tu-bs.de/dns-query | :heavy_check_mark: |
| [Internet Initiative Japan](https://public.dns.iij.jp/) | https://public.dns.iij.jp/dns-query | :heavy_check_mark: | Planned to run until March 2024 
| [Invisv](https://invisv.com/articles/dns.html) | https://dns.invisv.com/dns-query | :heavy_check_mark: | Implements Oblivious DNS
| [IPv6DNS](https://www.ipv6dns.com/index) | https://dns.ipv6dns.com/dns-query | :heavy_check_mark: |
| Irre.li | https://irre.li/dns-query | :heavy_check_mark: | Adblocking
|[IT Нинзя](https://iamninja.ru/)|https://dns.iamninja.ru/dns-query|:heavy_check_mark:|Ad & porn blocking
|itdept.pro|https://dns.itdept.pro/dns-query|:heavy_check_mark:|Adblocking
|[ivnkn](https://ivnkn.xyz/)|https://ivnkn.xyz/dns-query|:heavy_check_mark:|
| **J**
|[Jack Stockley](https://jstockley.com/)|https://dns.jstockley.com/dns-query|:heavy_check_mark:|Adblocking
| Jackyes.ovh | https://jackyes.ovh/dns-query | :heavy_check_mark: | Adblocking
|jamesxue.xyz|https://tj.jamesxue.xyz/dns-query|:heavy_check_mark:|
| Jfchenier.ca | https://adguard.jfchenier.ca/dns-query | :heavy_check_mark: | Adblocking
|[Jinwoo](https://jinwoo.dev/)|https://dns.jinwoo.dev/dns-query|:heavy_check_mark:|Adblocking
|joaofidelix.com.br|https://dns.joaofidelix.com.br/dns-query|:heavy_check_mark:|Adblocking
| [Jonas Hahnfeld](https://www.hahnjo.de/) | https://dns.hahnjo.de/dns-query | :heavy_check_mark: |
| [jp.tiar.app](https://jp.tiar.app/) | https://jp.tiar.app/dns-query <br> https://jp.tiarap.org/dns-query | :heavy_check_mark: | No Censorship, No Logging, No ECS, support DNSSEC in Japan |
|jsanagustin.net|https://adguard1.jsanagustin.net/dns-query|:heavy_check_mark:|Adblocking
|[Jucker Software Engineering](https://jucker.engineering/)|https://dns.jucker.engineering/dns-query|:heavy_check_mark:|Adblocking
|jurre-home|https://jurre-home.duckdns.org/dns-query|:heavy_check_mark:|Adblocking
| **K**
| [Kamil Szczepański](https://kamilszczepanski.com/) | https://dns.kamilszczepanski.com/dns-query | :heavy_check_mark: | Adblocking
|[Karl.ONE](https://karl.one/)|https://dns.karl.one/dns-query|:heavy_check_mark:|Adblocking
|keithchung|https://keithchung.hopto.org/dns-query|:heavy_check_mark:|Adblocking
| [Kernel-error](https://www.kernel-error.de/2022/03/18/bind-9-18-mit-doh-und-dot/) | https://dns.kernel-error.de/dns-query | :heavy_check_mark: |
| [kescherDNS](https://dns.kescher.at/) | https://dns.kescher.at/dns-query | :heavy_check_mark: | Non-logging, hosted in Vienna and Düsseldorf
| [kilabit.info](https://kilabit.info/) | https://kilabit.info/dns-query | :heavy_check_mark: |
| Killtw.im | https://doh.killtw.im/dns-query | :heavy_check_mark: | Adblocking
|[KinergeticA](https://kinergetica.com/)|https://storydoh.kinergetica.com/dns-query|:heavy_check_mark:|
|[Kishore](https://avdkishore.dev/)|https://adguard.avdkishore.dev/dns-query|:heavy_check_mark:|
|Konikoni428|https://adguard.konikoni428.com/dns-query|:heavy_check_mark:|Adblocking
|korzhov|https://korzhov.dev/dns-query|:heavy_check_mark:|Adblocking
|kpsn.org|https://dart.kpsn.org/dns-query|:heavy_check_mark:|Adblocking
| Krnl.eu | https://xray.krnl.eu/dns-query | :heavy_check_mark: | Adblocking
|krtekvpn|https://krtekvpn.duckdns.org/dns-query|:heavy_check_mark:|Adblocking
|kss.ovh|https://adguard.kss.ovh/dns-query|:heavy_check_mark:|
| **L**
| [La Contre-Voie](https://lacontrevoie.fr/en/services/doh/) | https://doh.lacontrevoie.fr/dns-query | :heavy_check_mark: | Supports DNSSEC and IPv6, not logging queries' content, uses [unbound](https://github.com/NLnetLabs/unbound/). Commits for net neutrality, hosted in France.
| [Lastentarvike](https://lastentarvike.fi) | https://lastentarvike.fi/dns-query | :heavy_check_mark: |
| [LavaDNS](https://dns.lavate.ch/) | Finland: https://eu1.dns.lavate.ch/dns-query | :heavy_check_mark: | DoH server in Finland. No logging, no filtering, no ECS, DNSSEC support. |
|leadmon.net|https://adguard1.leadmon.net/dns-query|:heavy_check_mark:|
|lege.despagne.net|https://adguard.lege.despagne.net/dns-query|:heavy_check_mark:|Adblocking
|lekdijk.online|https://externalmobiel.lekdijk.online/dns-query|:heavy_check_mark:|
| [Lindung](https://lindung.pp.ua/) | Adblocking: https://lindung.pp.ua/dns-query <br> Ad & porn blocking: https://lindung.pp.ua/family | :heavy_check_mark: <br> :heavy_check_mark: |
|[loNET](https://dns.lonet.org/) | https://doh.dns1.lonet.org/dns-query | :heavy_check_mark:|Adblocking
|lz0724.com|https://orau.lz0724.com/dns-query|:heavy_check_mark:|Ad & porn blocking
| **M**
|[maolaohei.xyz](https://maolaohei.xyz)|https://dns.maolaohei.xyz/dns-query|:heavy_check_mark:|Adblocking
| [Masters of Cloud](https://www.masters-of-cloud.de/) | https://masters-of-cloud.de/dns-query | :heavy_check_mark: | 
|meddy94.de|https://adguard.meddy94.de/dns-query|:heavy_check_mark:|Adblocking
| Meeo.win | https://dns.meeo.win/dns-query | :heavy_check_mark: | Adblocking
| [MegaNerd](https://meganerd.nl/encrypted-dns-server) | https://chewbacca.meganerd.nl/dns-query | :heavy_check_mark: | No logging, no filtering, DNSSEC, based in the Netherlands
| Meshkov.info | https://testaghome.meshkov.info/dns-query | :heavy_check_mark: | Adblocking
|mikeliu.org|https://dns.mikeliu.org/dns-query|:heavy_check_mark:|Adblocking
| [Minh Truong](https://truong.fi/) | https://dns.truong.fi/dns-query | :heavy_check_mark: | Adblocking
| [Mobik](https://www.mobik.com/) | https://dnstls.mobik.com/dns-query | :heavy_check_mark: |
|[modr.club](https://modr.club/)|https://ps1.modr.club/dns-query|:heavy_check_mark:|
| [Molinero](https://molinero.dev/) | https://dns.molinero.dev/dns-query | :heavy_check_mark: | Adblocking
|moonssif.com|https://dns.moonssif.com/dns-query|:heavy_check_mark:|Adblocking
| [Morbitzer](https://morbitzer.de/) | https://www.morbitzer.de/dns-query | :heavy_check_mark: | 
|msr177|https://msr177.com/dns-query|:heavy_check_mark:|Adblocking
|[msxnet.ru](https://msxnet.ru/)|https://dns.msxnet.ru/dns-query|:heavy_check_mark:|Adblocking
| [Mullvad](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls/) | Non-blocking https://doh.mullvad.net/dns-query <br> Adblocking https://adblock.doh.mullvad.net/dns-query | :heavy_check_mark: <br> :heavy_check_mark: | Public DoH server in AU, US, DE, GB, SG, and SE with QNAME minimization, audited by [Assured](https://www.assured.se/wp-content/uploads/2021/03/Assured_Mullvad_DoH_server_audit_report.pdf)
|[MULTIMEDIA CONCEPT](https://multimediaconcept.fr/)|https://blockerads.multimediaconcept.fr/dns-query|:heavy_check_mark:|Adblocking
| [murgi.de](https://www.murgi.de/) | https://dns.murgi.de/dns-query | :heavy_check_mark: | Adblocking
|muxinghe.cn|https://dns.muxinghe.cn/dns-query|:heavy_check_mark:|Adblocking
|muxyuji.ru|https://www.muxyuji.ru/dns-query|:heavy_check_mark:|Adblocking
| Myon | https://blackhole.myon.lu/dns-query | :heavy_check_mark: | Adblocking
|mywire.org|https://area51.mywire.org/dns-query|:heavy_check_mark:|Adblocking
|mzrme.cn|https://dns.mzrme.cn/dns-query|:heavy_check_mark:|
| **N**
|nas-server.ru|https://dns.nas-server.ru/dns-query|:heavy_check_mark:|Adblocking
| Nexific.it | https://doh.luigi.nexific.it/dns-query | :heavy_check_mark:|
| [NextDNS](https://nextdns.io) | https://dns.nextdns.io | :heavy_check_mark: | The first cloud-based private DNS service that gives you full control over what is allowed and what is blocked on the Internet. 300,000 domain resolution per month is free with non-filtering afterward until the end of the month. Granular dashboard, Each account can create multiple configurations, which can be used for multiple devices with prefixes to track activities on the dashboard. [Create a config ID](https://my.nextdns.io/start)
|ngc7331.top|https://dns.ngc7331.top/dns-query|:heavy_check_mark:|
| Nhtsky | https://dns.nhtsky.com/dns-query | :heavy_check_mark: | Adblocking
| [NIC.LV](https://doh.lv/) | https://doh.lv/dns-query <br> https://doh.nic.lv/dns-query | :heavy_check_mark: <br> :heavy_check_mark: | Run by .lv TLD registry 
|nguyendn.com|https://dns.nguyendn.com/dns-query|:heavy_check_mark:|Adblocking
|nielsdb.be|https://dns1.nielsdb.be/dns-query|:heavy_check_mark:|Adblocking
|nilanjan.rocks|https://www.nilanjan.rocks/dns-query|:heavy_check_mark:|Adblocking
| [NiYaWe](https://www.niyawe.de/) | https://doh.niyawe.de/dns-query | :heavy_check_mark: |
| [Njalla](https://dns.njal.la/) | https://dns.njal.la/dns-query | :heavy_check_mark: | Non logging, based in Sweden
| [No Ad DNS](https://noaddns.com/) | https://resolver.noaddns.com/dns-query | :heavy_check_mark: | Adblocking
| [Node15](https://node15.com/) | https://pi1.node15.com/dns-query | :heavy_check_mark: | Block ads and porn
|[nolo.ltd](https://nolo.ltd/)|https://sink.nolo.ltd/dns-query|:heavy_check_mark:|Adblocking
|[novali.date](https://novali.date/)|https://dns.novali.date/dns-query|:heavy_check_mark:|Adblocking
|[ns](https://n5.lsasss.com/)|https://n5.lsasss.com/dns-query|:heavy_check_mark:|Adblocking
|NS3|https://dns8.org/dns-query<br>https://n0.eu/dns-query<br>https://ns3.com/dns-query<br>https://ns3.cx/dns-query<br>https://ns3.link/dns-query|:heavy_check_mark:<br>:heavy_check_mark:<br>:heavy_check_mark:<br>:heavy_check_mark:<br>:heavy_check_mark:|
| Nullgate.net | https://dns.nullgate.net/dns-query | :heavy_check_mark: | Adblocking
| **O**
|o1lt|https://o1.lt/dns-query|:heavy_check_mark:|Adblocking
|[ofdoom.net](https://ofdoom.net/)|https://dns.ofdoom.net/dns-query|:heavy_check_mark:|Adblocking
|[ohai.ca](https://ohai.ca/)|https://hermes.ohai.ca/dns-query|:heavy_check_mark:|
|[OneDNS.cc](https://onedns.cc/)|https://secure.onedns.cc/dns-query|:heavy_check_mark:|Adblocking
|[OneDNS.net](https://onedns.net/)|https://doh.onedns.net/dns-query|:heavy_check_mark:|
| [OpenBLD.net DNS](https://lab.sys-adm.in/) | Adapted : https://ada.openbld.net/dns-query <br> Stricted : https://ric.openbld.net/dns-query | :heavy_check_mark: <br> :heavy_check_mark: | Block ads and trackers
|[opnsource.com.au](https://opnsource.com.au/)|https://dns.opnsource.com.au/dns-query|:heavy_check_mark:|Adblocking
|osefcorp|https://osefcorp.duckdns.org/dns-query|:heavy_check_mark:|Adblocking
| [Ozérim](https://ozer.im/) | https://1a.ns.ozer.im/dns-query | :heavy_check_mark: | Adblocking
| **P**
| [PaesaDNS](https://milgradesec.github.io/paesadns/) | https://dns.paesa.es/dns-query | :heavy_check_mark: | Adblocking, non-logging
|[PanSzelescik](https://panszelescik.pl/)|https://dns.panszelescik.pl/dns-query|:heavy_check_mark:|Adblocking
| Path of Grace | https://doh.gcp.pathofgrace.com/dns-query | :heavy_check_mark: | Adblocking
|[PersianNIT](https://persiannit.net/)|https://darya.persiannit.net/dns-query|:heavy_check_mark:|Adblocking
|pleumkungz.com|https://thanos.pleumkungz.com/dns-query|:heavy_check_mark:|Adblocking
|[PlumeDNS](https://plumedns.com/)|https://privacy.plumedns.com/dns-query|:heavy_check_mark:|
|privado.ovh|https://dns.privado.ovh/dns-query|:heavy_check_mark:|Adblocking
|[PriviLab.net](https://privilab.net/)|https://dns.privilab.net/dns-query|:heavy_check_mark:|Adblocking
|[Purbalingga](https://purbalinggakab.go.id/)|https://dns.purbalinggakab.go.id/dns-query|:heavy_check_mark:|Ad & porn blocking
| [PureDNS](https://puredns.org/) | https://puredns.org/dns-query | :heavy_check_mark: | Hosted in Indonesia and Singapore
| **Q**
| [Qihoo 360](https://360.cn) | https://doh.360.cn/dns-query | :heavy_check_mark: | Based in China
| [qquackDNS](https://qquack.org/nameserver) | https://ns1.qquack.org/dns-query | :heavy_check_mark: | Adblocking, non-logging
|[QWER DNS](https://dns.qwer.pw/)|https://ant.dns.qwer.pw/dns-query<br>https://dog.dns.qwer.pw/dns-query<br>https://lion.dns.qwer.pw/dns-query<br>https://tiger.dns.qwer.pw/dns-query<br>https://frog.dns.qwer.pw/dns-query|:heavy_check_mark:<br>:heavy_check_mark:<br>:heavy_check_mark:<br>:heavy_check_mark:<br>:heavy_check_mark:|Adblocking
| **R**
| [R0cket](https://resolver.r0cket.net/) | https://resolver.r0cket.net/dns-query | :heavy_check_mark: | Adblocking, queries are logged and monitored when there's abuse
|[R1BNC](https://r1bnc.com/)|https://r1bnc.com/dns-query|:heavy_check_mark:|Ad & porn blocking
|[Rahul](https://ssrahul96.xyz/)|https://ag.ssrahul96.xyz/dns-query|:heavy_check_mark:|Adblocking
|[Rashedul Islam](https://worthmind.net/)|https://dns.worthmind.net/dns-query|:heavy_check_mark:|Ad & porn blocking
| [Rayneau](https://rayneau.fr/) | https://rayneau.fr/dns-query | :heavy_check_mark: | Block porn and ads
| reckoningslug | https://dns.reckoningslug.name/dns-query | :heavy_check_mark: |
|[Renan Altendorf](https://altendorfme.com/)|https://chaos.altendorfme.com/dns-query|:heavy_check_mark:|Adblocking
| [Restena](https://www.restena.lu/en/service/public-dns-resolver) | https://kaitain.restena.lu/dns-query | :heavy_check_mark: | Based in Luxembourg, DNSSEC, minimal logging for technical functions
| [RethinkDNS](https://www.rethinkdns.com/) | Non-filtering: https://basic.rethinkdns.com/dns-query <br> OISD: https://sky.rethinkdns.com/1:IAAgAA== | :heavy_check_mark: <br> :heavy_check_mark: | [An open-source stub resolver](https://github.com/serverless-dns/serverless-dns) running in 200+ locations world-wide on Cloudfare's network. Fast, secure, private, transparent, configurable DNS resolver. No ECS. Implements CNAME Cloaking. No-logs. [code](https://github.com/celzero/rethink-app). [Configure custom blocklists](https://rethinkdns.com/configure)
| [Rezhajul](https://doh.rezhajul.io/) | https://doh.rezhajul.io/dns-query | :heavy_check_mark: | No Logging, DNSSEC enabled, 1.7M+ hosts filtered (ads, tracker, malware, spam, coinminer and phising).
| [rferee.dev](https://rferee.dev/setup/dns/) | https://resolver.rferee.dev/dns-query/ |:heavy_check_mark:|Adblocking
| Rin.sh | https://dns.rin.sh/dns-query | :heavy_check_mark: |
|[RKJha](https://rkjha.com.np/)|https://dns.rkjha.com.np/dns-query|:heavy_check_mark:|
|[ROKH](https://rokh.biz/)|https://adg.rokh.biz/dns-query|:heavy_check_mark:|
|[ronc.ru](https://ronc.ru/)|https://dns.ronc.ru/dns-query|:heavy_check_mark:|Adblocking
| [RoTunneling](https://www.rotunneling.net/rotunneling-doh-free/) | https://dns.rotunneling.net/dns-query/public | :heavy_check_mark: | Adblocking
|[RougaCh](https://rouga.ch/)|https://adguard-dns.rouga.ch/dns-query|:heavy_check_mark:|Adblocking
|[Rowdy en Geesje](https://rowdyengeesje.nl/)|https://adguard.rowdyengeesje.nl/dns-query|:heavy_check_mark:|
| **S**
|[SAFEITH](https://safeith.com/)|https://dns.safeith.com/dns-query|:heavy_check_mark:|Ad & porn blocking
| [SafeServe](https://www.namecheap.com/dns/free-public-dns/) | https://safeservedns.com/dns-query | :heavy_check_mark: | Operated by Namecheap
| [Safe Surfer](https://safesurfer.io/) | https://doh.safesurfer.io/dns-query | :heavy_check_mark: | Filter porn sites, enforce safe search
|[Saikat](https://rsaikat.com/)|https://o.rsaikat.com/dns-query|:heavy_check_mark:|Adblocking
|[Samutz](https://samutz.com/)|https://cloud.samutz.com/dns-query|:heavy_check_mark:|
|sbdns.co.in|https://sbdns.co.in/dns-query|:heavy_check_mark:|Adblocking
| [Sellan DNS](https://dns.sellan.fr/) | https://dns.sellan.fr/dns-query | :heavy_check_mark: | Adblocking, no logging
|[sev.monster](https://sev.monster/)|https://dns.sev.monster/dns-query|:heavy_check_mark:|
|shalenkov|https://shalenkov.dev/dns-query|:heavy_check_mark:|Adblocking
| [Shecan](https://shecan.ir/) | https://free.shecan.ir/dns-query <br> https://dns.shecan.ir/dns-query <br> https://pro.shecan.ir/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | Based in Iran, proxies sanctioned websites
| [Shimul D](https://shimul.me) | https://do.shimul.me/dns-query | :heavy_check_mark: | Adblocking
| [Shunhang](https://www.shimmerl.top/archives/dnsqx-ls-20-12-21) | https://dns.lsho.top:444/dns-query | :heavy_check_mark: | Adblocking
| Shuting | https://adguard.shuting.idv.tw/dns-query | :heavy_check_mark: | Adblocking
| Silen.org | https://dns.silen.org/dns-query | :heavy_check_mark: | Adblocking
|[Silentlybren](https://silentlybren.com/)|https://dns.silentlybren.com/dns-query|:heavy_check_mark:|Adblocking
|siry.de|https://dns.siry.de/dns-query|:heavy_check_mark:|Adblocking
|sitdns|https://sitdns.com/dns-query|:heavy_check_mark:|Adblocking
|skrep.eu|https://dns.skrep.eu/dns-query|:heavy_check_mark:|Adblocking
| Slinkyman.net | https://dns.slinkyman.net/dns-query | :heavy_check_mark: | Adblocking
| [Softcom](https://www.softcom.net/) | https://clientdns3.softcom.net/dns-query | :heavy_check_mark: |
|[spaceindex.net](https://spaceindex.net/)|https://adguard.spaceindex.net/dns-query|:heavy_check_mark:|
| [SPIL](https://www.spil.co.id/) | https://dns.spil.co.id/dns-query | :heavy_check_mark: | Adblocking
|[SpyRisk](https://spyrisk.fr/)|https://adguard.spyrisk.fr/dns-query|:heavy_check_mark:|Ad & porn blocking
| [Startup Stack](https://startupstack.tech/) | https://dns.startupstack.tech/dns-query | :heavy_check_mark: |
| [Studentenstadt Freimann](https://www.stusta.de/en/) | https://muli.stusta.mhn.de/dns-query <br> https://esel.stusta.mhn.de/dns-query | :heavy_check_mark: <br> :heavy_check_mark: |
|stvsk.ml|https://dns.stvsk.ml/dns-query|:heavy_check_mark:|Adblocking
|sungai.stream|https://doh.sungai.stream/dns-query|:heavy_check_mark:|
|[SunTrack](https://sntrk.ru/)|https://guard.sntrk.ru/dns-query|:heavy_check_mark:|Adblocking
|supercluster.io|https://dns.supercluster.io/dns-query|:heavy_check_mark:|Adblocking
| [Surfshark](https://surfshark.com) | https://dns.surfshark.com/dns-query | :heavy_check_mark: |
|surt|https://surt.ml/dns-query|:heavy_check_mark:|Adblocking
| [SWITCH](https://www.switch.ch/security/info/public-dns/) | https://dns.switch.ch/dns-query | :heavy_check_mark: | DNSSEC validation protects from forged or manipulated DNS data from upstream servers, DNS Query Name Minimisation to improve privacy, [SWITCH DNS Firewall](https://www.switch.ch/dns-firewall/) blocks access to infected or malicious websites and redirects users to a landing page |
| [Syaifullah](https://blog.syaifullah.com/public-dns-services/) | https://dns.syaifullah.com/dns-query | :heavy_check_mark: | Adblocking
| [Syshero](https://syshero.org/) | https://doh.syshero.org/dns-query | :heavy_check_mark: | 
| **T**
| t53.de | https://dns.t53.de/dns-query | :heavy_check_mark: |
|[TechEasy](https://techeasy.org/)|https://dns1.techeasy.org/dns-query|:heavy_check_mark:|Adblocking
| [Telekom Deutschland](https://telekomhilft.telekom.de/t5/Offentliche-Tests-Umfragen/Telekom-hilft-Labor-Testet-mit-uns-DNS-over-HTTPS/m-p/5008054) | https://dns.telekom.de/dns-query | :heavy_check_mark: | 
| [TeraDNS](https://teradns.org/dns-over-https/) | Germany : https://de.teradns.org/dns-query | :heavy_check_mark:| Adblocking, query logged for 24 hours to detect amplification attack.
| [TÉZOÏ](https://www.tezoi.com/) | https://cloud.tezoi.com/dns-query | :heavy_check_mark: | Adblocking
| therifleman.name | https://dns.therifleman.name/dns-query | :heavy_check_mark: | Based in Mumbai, IP not logged, query logged for 24 hours, adblocking
| [Tiarap](https://doh.tiar.app) | https://doh.tiar.app/dns-query <br> https://doh.tiarap.org/dns-query | :heavy_check_mark: <br> :heavy_check_mark: |Based in Singapore, No logging, block Ad/Ad-tracking/Malware, No ECS, DNSSEC |
| Timmes.nl | https://timmes.nl/dns-query | :heavy_check_mark: | Adblocking
|[Timochan](https://timochan.cn/)|https://dns.timochan.cn/dns-query|:heavy_check_mark:|Adblocking
|[TipsyCoffee](https://tipsy.coffee/)|https://dns.tipsy.coffee/dns-query|:heavy_check_mark:|Adblocking
|tk31z|https://tk31z.com/dns-query|:heavy_check_mark:|Adblocking
| Tls-data.de | https://dns.tls-data.de/dns-query | :heavy_check_mark: |
|[toairs](https://toairs.com/)|https://d.toairs.com/dns-query|:heavy_check_mark:|Adblocking
|[TPM](https://apigw.online/)|https://dns.apigw.online/dns-query|:heavy_check_mark:|Adblocking
|tracker.ink|https://dns.tracker.ink/dns-query|:heavy_check_mark:|Adblocking
|tungdnsne|https://tungdnsne.duckdns.org/dns-query|:heavy_check_mark:|Adblocking
| [TWNIC](https://www.twnic.net.tw/) | https://dns.twnic.tw/dns-query | :heavy_check_mark: | No source IP logging. Operated by [Quad101](https://101.101.101.101/index_en.html) project, according to this [announcement](https://blog.twnic.net.tw/2018/12/28/1803/) |
|[Tyler G. Wahl](https://tylerwahl.com/)|https://dns-east.tylerwahl.com/dns-query|:heavy_check_mark:|Adblocking
|typaza|https://typaza.com/dns-query|:heavy_check_mark:|Adblocking
| **U**
| Ueni.dyndns.org | https://ueni.dyndns.org/dns-query | :heavy_check_mark: | Adblocking
|[Universitas Negeri Manado](https://unima.ac.id/)|https://open-resolver1.unima.ac.id/dns-query|:heavy_check_mark:|Adblocking
| [Unstoppable Domains](https://docs.unstoppabledomains.com/d-websites/resolving-dwebsites-in-a-browser/) | https://resolver.unstoppable.io/dns-query | :heavy_check_mark: | Also resolve `.crypto` TLD of Unstoppable Domains.
|[Uplenk](https://uplenk.com/)|https://dns.uplenk.com/dns-query|:heavy_check_mark:|Ad & porn blocking
| **V**
| [Vasili Sviridov](https://vasi.li/) | https://tor.vasi.li/dns-query | :heavy_check_mark: | 
|[vendor vista](https://vendorvista.xyz/)|https://securedns.vendorvista.xyz/dns-query|:heavy_check_mark:|Adblocking
| [VinnyP](https://dns.vinnyp.xyz/privacy) | https://dns.vinnyp.xyz/dns-query | :heavy_check_mark: | No logging, self recursive resolved, block ads, malware & porn.
| [Virga DNS](https://virga.pp.ua) | Adblocking https://virga.pp.ua/dns-query <br> Adblocking & porn blocking https://virga.pp.ua/porn | :heavy_check_mark: <br> :heavy_check_mark: | Server in Japan
|[Vishal Kumar](https://vishalk.com/)|https://dns.vishalk.com/dns-query|:heavy_check_mark:|Ad & porn blocking
| [vMath](https://www.vmath.my.id/) | https://dns.vmath.my.id/dns-query | :heavy_check_mark: | Adblocking
|vokuev.org|https://vpn.vokuev.org/dns-query|:heavy_check_mark:|Ad & porn blocking
|vpms.xyz|https://killads.vpms.xyz/dns-query|:heavy_check_mark:|Adblocking
|vpnglobal.my.id|https://doh.vpnglobal.my.id/dns-query|:heavy_check_mark:|Ad & porn blocking
| **W**
|[wakgood](https://wakgood.net/)|https://dns.wakgood.net/dns-query|:heavy_check_mark:|Adblocking
|wantaquddin|https://wantaquddin.com/dns-query|:heavy_check_mark:|Ad & porn blocking
|[webstor.net](https://webstor.net/)|https://dns.webstor.net/dns-query|:heavy_check_mark:|Ad & porn blocking
| **X**
|xaoimoon.fr|https://adb-home.xaoimoon.fr/dns-query|:heavy_check_mark:|Adblocking
| [xcom.pro](https://doh.xcom.pro/) | https://doh.xcom.pro/dns-query | :heavy_check_mark: | Adblocking
|xenergy.cc|https://xenergy.cc/dns-query|:heavy_check_mark:|Adblocking
|xinfeng16m.top|https://agh.xinfeng16m.top/dns-query|:heavy_check_mark:|
|xm706v.com|https://v2.xm706v.com/dns-query|:heavy_check_mark:|
| **Y**
|yamamoto.ren|https://adguard.yamamoto.ren/dns-query|:heavy_check_mark:|
|yameenassotally.com|https://dns.yameenassotally.com/dns-query|:heavy_check_mark:|Ad & porn blocking
| [Yarp](https://yarp.lefolgoc.net/) | https://yarp.lefolgoc.net/dns-query | :heavy_check_mark: <br> :heavy_check_mark: | Hosted in France, no logging.
|yazilimatolye.com|https://lion.yazilimatolye.com/dns-query|:heavy_check_mark:|Adblocking
|ychen.cf|https://ychen.cf/dns-query|:heavy_check_mark:|Adblocking
|ychen|https://ychen.ga/dns-query|:heavy_check_mark:|Adblocking
|[YekongTAT](https://moeyk.com/)|https://doh.moeyk.com/dns-query|:heavy_check_mark:|
|yingroad.top|https://ora.yingroad.top/dns-query|:heavy_check_mark:|Adblocking
| Youni | https://dns.youni.win/dns-query | :heavy_check_mark: | Adblocking
|yovbak|https://yovbak.com/dns-query|:heavy_check_mark:|Adblocking
|yunmoc.top|https://dns.yunmoc.top/dns-query|:heavy_check_mark:|Adblocking
| **Z**
|zhhz.cc|https://dns140.zhhz.cc/dns-query|:heavy_check_mark:|Adblocking
|zhhz.cc|https://dns168.zhhz.cc/dns-query|:heavy_check_mark:|Adblocking
|zxcvb.pp.ua|https://zxcvb.pp.ua/dns-query|:heavy_check_mark:|Adblocking
|zxi7.cn|https://dns.zxi7.cn/dns-query|:heavy_check_mark:|
| **0-9**
|[0ms.run](https://0ms.run/) | https://0ms.run/dns-query | :heavy_check_mark:| Can also forward to other DoH servers
|1.bsh4.com|https://dns.1.bsh4.com/dns-query|:heavy_check_mark:|Adblocking
|140.238.202.136.sslip.io|https://140.238.202.136.sslip.io/dns-query|:heavy_check_mark:|Ad & porn blocking
|209.wf|https://dns.209.wf/dns-query|:heavy_check_mark:|Adblocking
|23-4.cn|https://dns.23-4.cn/dns-query|:heavy_check_mark:|Adblocking
|240527.xyz|https://dns.240527.xyz|:heavy_check_mark:|Adblocking
|[280blocker](https://280blocker.net/)|https://doh003.280blocker.net/dns-query|:heavy_check_mark:|Ad & porn blocking
|30x.me|https://doh.30x.me/dns-query|:heavy_check_mark:|Adblocking
|4-the.win|https://dns.4-the.win/dns-query|:heavy_check_mark:|
|52306.org|https://dns.52306.org/dns-query|:heavy_check_mark:|
| [5ososea](https://www.5ososea.com/) | Adblocking: https://dns.5ososea.com/dns-query <br> Ad & porn blocking: https://family.5ososea.com/dns-query <br> Ad & porn blocking with safe search: https://kids.5ososea.com/dns-query | :heavy_check_mark: <br> :heavy_check_mark: <br> :heavy_check_mark: | Hosted in Germany, query logged for 24 hours.
|68360612.xyz|https://jp.68360612.xyz/dns-query|:heavy_check_mark:|
| [7sec](https://7sec.com.br/dns/) | https://dns.7sec.com.br/dns-query/ | :heavy_check_mark: | Adblocking
| [7vpn](https://dns.7vpn.com/) | https://dns.7vpn.com/dns-query | :heavy_check_mark: | Adblocking
| **Others**
| @jedisct1  | https://doh.crypto.sx/dns-query | :heavy_check_mark: |a server which runs another project called [doh-proxy](https://github.com/jedisct1/rust-doh), written in Rust.
| [@null31](https://ibuki.cgnat.net)| https://ibuki.cgnat.net/dns-query | :heavy_check_mark: | Based in Brazil / doh-server (nginx - unbound) / dot-server (unbound) / DNSSEC / QNAME minimization / Uncensored / no logging, no ECS, hosted on Oracle Cloud VPS by [null31](https://gitlab.com/null31/DoT-DoH-public-config). |
| @publicarray [dns.seby.io](https://dns.seby.io) | https://doh-2.seby.io/dns-query | :heavy_check_mark: | Australian server that runs [@m13253's Go implementation](https://github.com/m13253/dns-over-https), Unbound with DNSSEC, No ECS, and No logs|

*: Tested via `curl --doh-url <RESOLVER_URI> http://google.com`.

Download a recent snapshot of the above list as JSON from [here](https://github.com/cslev/encrypted_dns_resolvers).

# Private DNS Server with DoH setup examples
| Base | Source | Comment |
|-------------|----------|---------|
| Docker | https://github.com/satishweb/docker-doh | Complete Docker stack using Star Brilliant's [dns-over-https](https://github.com/m13253/dns-over-https) and [Docker Flow Proxy](https://github.com/docker-flow/docker-flow-proxy)
| Docker | https://github.com/coolquasar/dnsproxy | Complete DoH, DoT, and DoQ stack in docker based on Adguard home dnsproxy project. Could host DoH, DoT and DoQ quickly in a cloud server, and run respective clients in local Docker env. It has been tested in Raspberry PI as well

# Supported in browsers and clients

|Name|Version|Comments|
|----|-------|----|
|Firefox|62| [Firefox DNS-over-HTTPS](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) |
|[Bromite](https://www.bromite.org/)|67.0.3396.88|[How to enable DoH](https://github.com/bromite/bromite/wiki/Enabling-DNS-over-HTTPS)|
|curl| 7.62.0 | See [DOH-implementation](DOH-implementation) |
|[OkHttp](https://github.com/square/okhttp/tree/master/okhttp-dnsoverhttps)| 3.11 | See [Providers](https://github.com/square/okhttp/blob/master/okhttp-dnsoverhttps/src/test/java/okhttp3/dnsoverhttps/DohProviders.java) |
| [curl-doh](https://github.com/curl/doh) | n/a | basic stand-alone DoH client that uses curl |
| Chrome | 66 | https://bugs.chromium.org/p/chromium/issues/detail?id=799753 |

# DOH Tools

|Name|Author/Organization|Comments|
|----|-------|----|
|[bulldohzer](https://github.com/commonshost/bulldohzer) | Commonshost | Benchmark DoH and Do53 servers
|[coredns](https://github.com/coredns/coredns)|Cloudflare| CoreDNS is a DNS server/forwarder, written in Go from the Cloud Native Computing Foundation. |
|[dealdoh](https://github.com/noglitchyo/dealdoh)|Maxime Elomari| a middleware to proxy DoH requests to different DNS upstreams, written in PHP.|
|[dns-over-https](https://github.com/m13253/dns-over-https)|Star Brilliant| server-side and client-side implementation, written in Golang|
|[dns2doh](https://github.com/bagder/dns2doh)|Daniel| tool for generating DOH responses and questions.|
|[dnscrypt-proxy](https://github.com/DNSCrypt/dnscrypt-proxy)|Frank Denis|dnscrypt-proxy 2 - A flexible DNS proxy, with support for encrypted DNS protocols.|
|[dnsdist](https://dnsdist.org/)|PowerDNS|supports doh, see <https://dnsdist.org/guides/dns-over-https.html>|
|[dnss](https://github.com/albertito/dnss)|Alberto Bertogli|daemon written in Go which acts as a proxy (the most common use case), and as a server (in case you want end-to-end control).|
|[doh-cf-workers](https://github.com/tina-hello/doh-cf-workers)|tina-hello|A single JS file to forward DoH to DoH on Cloudflare Workers
|[doh-gcf](https://github.com/tina-hello/doh-gcf)|tina-hello|A single C# file to forward DoH to DoH/Do53 on Google Cloud Function 
|[doh-js-client](https://github.com/sc0Vu/doh-js-client)|Peter Lai| client-side implementation of DoH, can be used in nodejs backend.|
|[doh-php-client](https://github.com/dcid/doh-php-client)|Daniel Cid| can be used to test and run DoH requests via PHP applications.|
|[doh-proxy](https://facebookexperimental.github.io/doh-proxy/)|Facebook| tools for DoH|
|[doh-proxy](https://github.com/jedisct1/rust-doh)|Frank Denis| server-side proxy in rust|
|[DOHD](https://github.com/dyne/dohd)|[Dyne.org](https://dyne.org)|Very fast and lightweight daemon written in C functioning as a simple proxy for DNS queries over HTTPS using the HTTP/2 protocol and WolfSSL.
|[dohjs](https://github.com/byu-imaal/dohjs) | [BYU IMAAL](https://imaal.byu.edu) | Client DoH JavaScript library for accessing DNS information from web applications. Can be tested at [dohjs.org](https://dohjs.org)
|[DoH](https://github.com/NotMikeDEV/DoH)|NotMikeDEV|A single PHP file to add DoH forwarder on any PHP-capable server
|[EasyDoH](https://github.com/ElevenPaths/EasyDoH)|ElevenPaths| a simple [add-on for Firefox](https://addons.mozilla.org/es/firefox/addon/easydoh/) that allows one to easily activate DNS over HTTPS and its working mode with just one click.|
|[Encrypted DNS Server](https://github.com/jedisct1/encrypted-dns-server)|Frank Denis|can serve DNSCrypt and DoH traffic simultaneously,  written in Rust.|
|[Encrypted-DNS](https://github.com/Siujoeng-Lau/Encrypted-DNS)|Siujoeng Lau| DNS-over-HTTPS forwarder written in Python|
|[godnsbench](https://github.com/ameshkov/godnsbench) | Andrey Meshkov | Benchmark DoH, Do53, DoT and DoQ servers.
|[h2odoh](https://github.com/xm74/h2odoh)|Max Kostikov| an implementation with H2O HTTP/2 server using embedded mruby.|
|[jDnsProxy](https://github.com/moparisthebest/jDnsProxy)|Travis Burtrum| DNS proxy and cache, implementing [DNS-over-TLS](https://tools.ietf.org/html/rfc7858), [DNS-over-HTTPS](https://tools.ietf.org/html/draft-hoffman-dns-over-https), and [Serve-Stale](https://tools.ietf.org/html/draft-ietf-dnsop-serve-stale)|
|[kdig](https://gitlab.nic.cz/knot/knot-dns)|CZ.NIC|Utility that sends one or more DNS queries to a nameserver. Each query can have individual settings, or it can be specified globally via common settings, which must precede query specification. This utility supports DoH.
|[nss-tls](https://github.com/dimkr/nss-tls)|Dima Krasner| a daemon that makes gethostbyname(), getaddrinfo(), etc. happen through DoH, without any change to applications, thus transparently migrating all applications that don't use their own resolver (like some browsers) from DNS to DoH.|
|[quart-doh](https://github.com/treussart/quart-doh)|Matthieu Treussart| HTTP/2 server who serves a DOH proxy written in Python, with [Quart](https://pgjones.gitlab.io/quart/index.html) Python web microframework.|
|[RouteDNS](https://github.com/folbricht/routedns)|Frank Olbricht| a flexible stub resolver, proxy, and router with support for DoH, DoT, and plain DNS written in Go.|
|[serverless-dns](https://github.com/serverless-dns/serverless-dns)|[RethinkDNS](https://rethinkdns.com/)| Host your own RethinkDNS instance on Cloudflare Worker, support customizable filter from URL parameter
|[Technitium DNS Server](https://github.com/TechnitiumSoftware/DnsServer)|Technitium|A FOSS, cross-platform DNS Server written in C# that can consume as well as host DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) services.
# Other

[Script to parse DoH provider URLs from this wiki page](https://gist.github.com/kimbo/dd65d539970e3a28a10628f15398247b)

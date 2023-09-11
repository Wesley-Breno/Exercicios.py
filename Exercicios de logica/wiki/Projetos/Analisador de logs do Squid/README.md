<h1>Analisador de logs do Squid</h1>
sites bloqueados. Desenvolva um analisador de log do Squid que mostre quais os sites mais bloqueados em uma organização.

<h2>Logs usados de exemplo;</h2>
   
    2023-07-15 10:23:45 Blocked: www.facebook.com - User: john.doe - Category: Social Media
    2023-07-15 10:24:01 Blocked: www.youtube.com - User: jane.smith - Category: Streaming
    2023-07-15 10:24:18 Blocked: www.twitter.com - User: mark.johnson - Category: Social Media
    2023-07-15 10:25:02 Blocked: www.netflix.com - User: sarah.wilson - Category: Streaming
    2023-07-15 10:25:19 Blocked: www.instagram.com - User: robert.davis - Category: Social Media
    2023-07-15 10:26:05 Blocked: www.twitch.tv - User: emily.jackson - Category: Streaming
    2023-07-15 11:07:33 Blocked: www.bet365.com - User: peter.anderson - Category: Gambling
    2023-07-15 11:08:09 Blocked: www.pornhub.com - User: anna.brown - Category: Adult Content
    2023-07-15 11:09:12 Blocked: www.gamingsite.com - User: david.miller - Category: Gaming
    2023-07-15 11:10:05 Blocked: www.dailymail.co.uk - User: olivia.harris - Category: News
    2023-07-15 11:11:22 Blocked: www.gamblingsite2.com - User: andrew.thompson - Category: Gambling
    2023-07-15 14:35:17 Blocked: www.shoppingwebsite.com - User: lisa.wilson - Category: Shopping
    2023-07-15 14:35:32 Blocked: www.bankwebsite.com - User: sam.roberts - Category: Finance
    2023-07-15 14:36:01 Blocked: www.gamblingsite3.com - User: michael.clark - Category: Gambling
    2023-07-15 14:36:22 Blocked: www.newswebsite.com - User: jessica.white - Category: News
    2023-07-15 14:37:05 Blocked: www.socialnetworking.com - User: kevin.andrews - Category: Social Media
    2023-07-16 13:55:13 Blocked: www.gamblingsite7.com - User: oliver.martin - Category: Gambling
    2023-07-16 13:55:31 Blocked: www.socialmedia3.com - User: sophia.rodriguez - Category: Social Media
    2023-07-16 13:56:02 Blocked: www.newssite.com - User: lucas.carter - Category: News
    2023-07-16 13:56:23 Blocked: www.gamblingsite8.com - User: mia.perez - Category: Gambling
    2023-07-16 13:57:05 Blocked: www.shoppingwebsite4.com - User: benjamin.lee - Category: Shopping
    2023-07-16 09:18:17 Blocked: www.adultsite.com - User: ethan.wilson - Category: Adult Content
    2023-07-16 09:18:33 Blocked: www.socialmedia2.com - User: ava.harris - Category: Social Media
    2023-07-16 09:19:02 Blocked: www.gamblingsite6.com - User: noah.thompson - Category: Gambling
    2023-07-16 09:19:22 Blocked: www.shoppingwebsite3.com - User: isabella.smith - Category: Shopping
    2023-07-16 09:20:05 Blocked: www.videostreaming.com - User: james.brown - Category: Streaming
    2023-07-15 15:45:12 Blocked: www.gamblingsite4.com - User: sophia.green - Category: Gambling
    2023-07-15 15:45:32 Blocked: www.musicstreaming.com - User: william.jones - Category: Streaming
    2023-07-15 15:46:01 Blocked: www.newswebsite2.com - User: emma.davis - Category: News
    2023-07-15 15:46:22 Blocked: www.shoppingwebsite2.com - User: jacob.moore - Category: Shopping
    2023-07-15 15:47:05 Blocked: www.gamblingsite5.com - User: mia.murphy - Category: Gambling

Como a descricao do projeto nao foi escrita detalhadamente, mudei um pouco o objetivo... Inves de colocar sites
bloqueados de uma organizacao, coloquei uma listagem de usuarios mais bloqueados em sites aleatorios.
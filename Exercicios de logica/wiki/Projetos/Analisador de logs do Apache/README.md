<h1>Analisador de logs do Apache</h1> 

Desenvolva um analisador de log do Apache que mostre quais as strings de pesquisa do google que mais levam internautas 
para o site da sua organização.

<h3>Arquivo de log usado como exemplo</h3>
    
    127.0.0.1 - - [14/Jul/2023:10:25:36 -0700] "GET /pagina1.html HTTP/1.1" 200 1234 "http://www.google.com/search?q=gatos" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    127.0.0.1 - - [14/Jul/2023:10:26:41 -0700] "GET /pagina2.html HTTP/1.1" 200 987 "http://www.bing.com/search?q=caes" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    127.0.0.1 - - [14/Jul/2023:10:26:41 -0700] "GET /pagina2.html HTTP/1.1" 200 987 "http://www.bing.com/search?q=caes" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    127.0.0.1 - - [14/Jul/2023:10:26:41 -0700] "GET /pagina2.html HTTP/1.1" 200 987 "http://www.bing.com/search?q=caes" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    127.0.0.1 - - [14/Jul/2023:10:27:15 -0700] "GET /pagina3.html HTTP/1.1" 200 567 "http://www.google.com/search?q=gatos" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    127.0.0.1 - - [14/Jul/2023:10:28:02 -0700] "GET /pagina4.html HTTP/1.1" 200 876 "http://www.google.com/search?q=cao" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    127.0.0.1 - - [14/Jul/2023:10:28:02 -0700] "GET /pagina4.html HTTP/1.1" 200 876 "http://www.google.com/search?q=cao" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    127.0.0.1 - - [14/Jul/2023:10:29:17 -0700] "GET /pagina5.html HTTP/1.1" 200 432 "http://www.yahoo.com/search?q=gatos" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    127.0.0.1 - - [14/Jul/2023:10:29:17 -0700] "GET /pagina5.html HTTP/1.1" 200 432 "http://www.yahoo.com/search?q=gatos" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"

<h3>Explicacao sobre os logs e a logica usada</h3>

Como eu nao possuo um servidor Apache, gerei logs aleatorios acima e os usarei para conclusao do projeto. Vamos 
considerar que o site da organização seja sobre um "PetShop".

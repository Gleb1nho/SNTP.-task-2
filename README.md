# SNTP.-task-2
Сервер точного времени, который врёт на заданное количество секунд.

Серверу поступает запрос от клиента, о том, что он хочет узнать время. Сервер спрашивает точное время у системы и <br>
прибавляет к нему заданное в конфигурационном файле количество секунд, после этого отправляет эти данные клиенту.
<br>
<br>
Параметры запуска: python3 sntp_server.py и python3 client.py <br>
В клиенте писать 1, чтобы отправлять запрос и получать ответ, в config.txt указывать количество секунд.
import os
import asyncio
from dotenv import load_dotenv

# Suponiendo que twscrape es una biblioteca hipotética, reemplázala por la que uses.
from twscrape import API, gather


async def fetch_tweets(api, query, limit=100):
    # Esta función asincrónica extrae tweets usando la API de twscrape.
    tweets = await gather(api.search(query, limit=limit))
    return tweets


async def main():
    load_dotenv()  # Carga las variables de entorno desde un archivo .env

    # Estas líneas obtienen las credenciales de Twitter desde las variables de entorno
    username = os.getenv('TWITTER_USERNAME')
    password = os.getenv('TWITTER_PASSWORD')
    email = os.getenv('TWITTER_EMAIL')
    email_password = os.getenv('TWITTER_EMAIL_PASSWORD')

    # Inicializa y configura la API de twscrape con las credenciales de usuario
    api = API()
    await api.pool.add_account(username, password, email, email_password)
    await api.pool.login_all()

    # Llama a la función fetch_tweets para extraer tweets con un término específico
    tweets_petro = await fetch_tweets(api, 'from:petrogustavo', limit=5)
    tweets_bukele = await fetch_tweets(api, 'from:nayibbukele', limit=5)
    tweets_galan = await fetch_tweets(api, 'from:CarlosFGalan', limit=5)

    # Ejemplo de cómo podrías manejar los tweets extraídos
    print("\n\nÚltimos tweets de la cuenta oficial de Gustavo Petro:")
    for tweet in tweets_petro:
        print(f"{tweet.id}\t{tweet.rawContent}\n")

    print("\n\nÚltimos tweets de la cuenta oficial de Nayib Bukele:")
    for tweet in tweets_bukele:
        print(f"{tweet.id}\t{tweet.rawContent}\n")

    print("\n\nÚltimos tweets de la cuenta oficial de Carlos Galán:")
    for tweet in tweets_galan:
        print (f"{tweet.id}\t{tweet.rawContent}\n")


if __name__ == "__main__":
    asyncio.run(main())

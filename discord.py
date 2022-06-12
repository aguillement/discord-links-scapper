from DiscordScraper.HTTP import HTTPClient
from DiscordScraper.DB import Database

if __name__ == '__main__':
    client = HTTPClient()
    client.addRequest('https://www.example.com/')
    client.run()
    
    database = Database('12345678910', '12345678910')
    database.write('01-01-1990', None)

    print(len(client.results[0]))

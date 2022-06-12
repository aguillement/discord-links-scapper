try:
    import asyncio
except ImportError:
    raise Exception('You do not appear to have the asynchronous modules with your installation of Python.')

try:
    import aiohttp
except ImportError:
    raise Exception('You do not appear to have aiohttp installed. Please refer to the README to figure out why.')


class HTTPClient(object):
    def __init__(self, per_host_limit=None, conn_limit=None, ttl=None):
        if per_host_limit is None:
            per_host_limit = 50
        
        if conn_limit is None:
            conn_limit = 0
        
        if ttl is None:
            ttl = 300
        
        self.connector = aiohttp.TCPConnector(limit_per_host=per_host_limit, limit=conn_limit, ttl_dns_cache=ttl)
        
        self.reqlimit = per_host_limit
        self.requests = []
        self.results = []
    
    def addRequest(self, url, headers=None, data=None, method=None):
        if headers is None:
            headers = {}
        
        if data is None:
            data = {}

        if method is None:
            method = 'GET'
        
        self.requests.append({'url': url, 'headers': headers, 'data': data, 'method': method})

    async def execute(self):
        semaphore = asyncio.Semaphore(self.reqlimit)
        session = aiohttp.ClientSession(connector=self.connector)

        async def run(url, headers, data, method, ssl=None):
            if ssl is None:
                ssl = True
            
            async with semaphore:
                async with session.request(method, url, headers=headers, data=data, ssl=ssl, allow_redirects=False) as response:
                    respdata = await response.read()
                    self.results.append(respdata)
            
        await asyncio.gather(*(run(request['url'], request['headers'], request['data'], request['method']) for request in self.requests))
        await session.close()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.execute())
        self.connector.close()

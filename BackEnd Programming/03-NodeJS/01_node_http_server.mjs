import { createServer } from 'node:http';

const server = createServer((req, res) => {
  const url = new URL(req.url ?? '/', `http://${req.headers.host}`);
  const requestId = req.headers['x-request-id'] ?? crypto.randomUUID();

  res.setHeader('Content-Type', 'application/json');
  res.setHeader('X-Request-ID', requestId);

  if (req.method === 'GET' && url.pathname === '/health') {
    res.writeHead(200);
    res.end(JSON.stringify({ status: 'ok' }));
    return;
  }

  res.writeHead(404);
  res.end(JSON.stringify({ error: 'not_found', request_id: requestId }));
});

server.listen(3000, () => console.log('http://localhost:3000'));

process.on('SIGTERM', () => {
  server.close(() => process.exit(0));
});

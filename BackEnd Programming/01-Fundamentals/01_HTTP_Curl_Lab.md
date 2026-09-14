# Practical Lab: HTTP with curl

Build and inspect requests before using a framework.

## Scenario
You are debugging an API that creates users and returns JSON.

```bash
curl -i https://httpbin.org/get
curl -i -X POST https://httpbin.org/post \
  -H 'Content-Type: application/json' \
  -d '{"name":"Ada","role":"engineer"}'
```

## Hands-on tasks

1. Compare `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`.
2. Inspect status code, headers, and body separately.
3. Add an `Authorization: Bearer demo-token` header.
4. Send malformed JSON and document the expected error contract.
5. Measure latency with `curl -w '%{http_code} %{time_total}\n'`.
6. Repeat a request and decide whether it is safe/idempotent.

## Production checklist

- Define timeouts on clients.
- Propagate request/correlation IDs.
- Never log authorization headers or secrets.
- Return machine-readable errors.
- Document cache and idempotency behavior.

## Deliverable
Create `http-notes.md` containing five real API requests, their responses, status-code reasoning, and one failure investigation.
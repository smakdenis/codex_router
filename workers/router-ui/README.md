# Router confirmation UI

This optional Cloudflare Worker is the future MCP endpoint for the AI Mode Router confirmation card.

It is intentionally separated from the skills-only plugin: the routing skill continues to work without a server. The Worker adds only an inline confirmation action and must not store prompts, files, or user identifiers.

## Deploy

1. Create a Cloudflare account and install Wrangler.
2. From this directory, run `npm install`, then `npx wrangler login` and `npm run deploy`.
3. Add the resulting HTTPS `/mcp` URL to the plugin's MCP submission configuration.

Do not publish the MCP-backed version until the endpoint is deployed and reviewed.

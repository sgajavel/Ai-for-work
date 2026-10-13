#!/usr/bin/env node
// Read-only capture of the raw records Notion's web app stores for a page.
// Usage: NOTION_TOKEN_V2=... node inspect.mjs <page-id-or-url> [out.json]
//
// UNVERIFIED: the endpoint and payload shape below come from the unofficial
// web API as I remember it. If Notion has changed it, the first run will show
// the error and we adjust. Nothing here writes to your workspace.

import { writeFileSync, mkdirSync } from "node:fs";
import { dirname } from "node:path";

const token = process.env.NOTION_TOKEN_V2;
if (!token) {
  console.error("Set NOTION_TOKEN_V2 (the token_v2 cookie from your own logged-in browser).");
  process.exit(1);
}

const input = process.argv[2];
if (!input) {
  console.error("Usage: node inspect.mjs <page-id-or-url> [out.json]");
  process.exit(1);
}

const hex = input.match(/[0-9a-f]{32}/i)?.[0] ?? input.replace(/-/g, "");
if (!/^[0-9a-f]{32}$/i.test(hex)) {
  console.error("Could not find a 32 character page id in:", input);
  process.exit(1);
}
const h = hex.toLowerCase();
const pageId = `${h.slice(0, 8)}-${h.slice(8, 12)}-${h.slice(12, 16)}-${h.slice(16, 20)}-${h.slice(20)}`;

const res = await fetch("https://www.notion.so/api/v3/loadPageChunk", {
  method: "POST",
  headers: { "content-type": "application/json", cookie: `token_v2=${token}` },
  body: JSON.stringify({
    pageId,
    limit: 100,
    cursor: { stack: [] },
    chunkNumber: 0,
    verticalColumns: false,
  }),
});

const text = await res.text();
if (!res.ok) {
  console.error(`HTTP ${res.status}\n${text.slice(0, 500)}`);
  process.exit(1);
}

const data = JSON.parse(text);
const blocks = data.recordMap?.block ?? {};
const types = {};
for (const b of Object.values(blocks)) {
  const t = b.value?.value?.type ?? b.value?.type ?? "unknown";
  types[t] = (types[t] ?? 0) + 1;
}
console.log("Block types on this page:", types);

const out = process.argv[3] ?? `captures/${pageId}.json`;
mkdirSync(dirname(out), { recursive: true });
writeFileSync(out, JSON.stringify(data, null, 2));
console.log(`Saved raw capture to ${out}`);

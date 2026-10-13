# notion-private

Experimental tooling for creating Notion buttons and automations through the
web app's private API, which the public API and the Notion connector don't support.

## Read this first

- This API is undocumented. It can change or break without notice.
- It likely violates Notion's terms of service. It acts on your own workspace,
  but Notion could still restrict the account. Use a test workspace if you can.
- It needs your `token_v2` session cookie. That is a full login to your account.
  Keep it in an environment variable. Never paste it into a file or commit it.
  Log out of Notion in the browser to revoke it.

## Step 1: capture (read-only)

1. In Notion, make a throwaway page and add one button by hand, with the
   steps you want to be able to reproduce.
2. Copy the page URL.
3. Run, from your own machine:

   ```
   export NOTION_TOKEN_V2='...'
   node notion-private/inspect.mjs "<page url>"
   ```

4. The raw records are saved under `notion-private/captures/` (git-ignored).
   Review the file before sharing it, since it can contain workspace and user ids.

## Step 2: write (not built yet)

Once a real button capture exists, the writer gets built from it:
clone a captured record with fresh ids, set the steps, submit it. Every
write will default to a dry run and need an explicit `--yes`.

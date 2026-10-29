# MFK landing v4: Netlify deploy

Built from `../v4/index.html` on 2026-10-29. Prototype for internal staff and NDA testers only.

- Upload: drag this folder onto https://app.netlify.com/drop (or Sites > Add new site > Deploy manually).
- Updates: Site > Deploys > drag the folder again; the URL stays the same.
- Privacy: `noindex` meta, `robots.txt` and an `X-Robots-Tag` header keep it out of search. For a password, use Site configuration > Access & security > Password protection (Netlify Pro).
- Rebuild after changing v4: copy `v4/index.html` and its used assets here again (Claude can do this).

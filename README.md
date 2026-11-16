# Me Pegué site

Public home, support and privacy pages for **Me Pegué**, the domino score keeper for
iPhone. Plain static HTML in English and Spanish, served by GitHub Pages.

- **Live:** https://mariocruz.github.io/mepegue/
- **App repo:** private (`MarioCruz/me-pegue`).

## Pages
- `index.html`, `es/index.html` — home page; the Help section is the support page
  (the Support URL in App Store Connect)
- `privacy.html`, `es/privacy.html` — privacy policy (the Privacy Policy URL in App Store
  Connect)
- `assets/` — stylesheet, icon, share image, screenshots, and the script that rebuilds
  the contact link
- `robots.txt`, `sitemap.xml`, `.nojekyll`

## Editing
All text lives in `build.py`. Edit it there and run `python3 build.py`, which rewrites the
four pages, `robots.txt` and `sitemap.xml`. Do not edit the HTML files by hand.

Keep the privacy policy true to the app: if the app ever saves photos, connects to the
internet, or adds a permission, update the policy and its effective date first.

## Moving to a custom domain
Links between pages are relative. To move, add a `CNAME` file, set DNS per the GitHub
Pages docs, change `BASE` in `build.py`, run it, and update the URLs in App Store Connect.

## After the app is released
Replace the "Coming soon" badge in `build.py` with the App Store link, and add
`<meta name="apple-itunes-app" content="app-id=6835237272">` to the home pages.

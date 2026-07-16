# Claude Code Directives

- **Code Style:** Keep code flat and simple. Do not introduce new design patterns, extra abstraction layers, or wrapper helper functions unless explicitly requested.
- **Scope Restriction:** Do not modify any files outside of the ones explicitly requested in the prompt. Do not perform "general cleanup" of unrelated code.
- **Fail-Safe:** If chasing a bug for more than 2 attempts, stop, output current findings, and ask for manual direction. Do not commit or refactor to fix it blindly.

## Project Notes

- The entire site is served from `main.py` — one flat FastAPI file. The homepage is a single
  `HOMEPAGE_HTML` string returned with edge-cache headers. Keep it that way: no templating
  engines, no static-site tooling, no component splitting unless explicitly requested.
- Scroll performance matters: no `backdrop-filter`, no animated `transform`/`box-shadow`
  effects on the page.
- Marketing copy makes no fabricated claims: no invented testimonials, user counts, or
  performance numbers. All tiers are pre-orders; FAQ answers stay honest about risk.
- Deploys: merged to `main` → Vercel auto-deploys. Development happens on
  `claude/passiveautotrades-website-b7ifaw`, merged via PR.

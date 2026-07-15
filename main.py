from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="ai PassiveAutotrades",
    description="Institutional Alpha",
    version="1.0.0",
)


@app.get("/api/data")
def get_sample_data():
    return {
        "data": [
            {"id": 1, "name": "Sample Item 1", "value": 100},
            {"id": 2, "name": "Sample Item 2", "value": 200},
            {"id": 3, "name": "Sample Item 3", "value": 300}
        ],
        "total": 3,
        "timestamp": "2024-01-01T00:00:00Z"
    }


@app.get("/api/items/{item_id}")
def get_item(item_id: int):
    return {
        "item": {
            "id": item_id,
            "name": "Sample Item " + str(item_id),
            "value": item_id * 100
        },
        "timestamp": "2024-01-01T00:00:00Z"
    }


# Rendered once at import time; served from Vercel's edge cache via the
# Cache-Control headers below, so traffic spikes never hit the function.
HOMEPAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades | Institutional Alpha</title>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #050505; color: #fff; font-family: 'Inter', sans-serif; }
        a { text-decoration: none; }

        nav { position: sticky; top: 0; z-index: 10; display: flex; align-items: center; justify-content: space-between;
              padding: 18px 5vw; background: rgba(5,5,5,0.96); border-bottom: 1px solid #161b22; }
        .logo { font-weight: 800; font-size: 1.05rem; color: #fff; letter-spacing: 0.5px; }
        .logo span { color: #58a6ff; }
        .nav-cta { background: #58a6ff; color: #000; padding: 10px 22px; border-radius: 8px; font-weight: 700; font-size: 0.9rem; }

        .hero { position: relative; text-align: center; padding: 110px 20px 80px; overflow: hidden; }
        .hero::before { content: ''; position: absolute; top: -220px; left: 50%; transform: translateX(-50%);
                        width: 900px; height: 500px; background: radial-gradient(ellipse at center, rgba(88,166,255,0.22), transparent 65%);
                        pointer-events: none; }
        .hero > * { position: relative; }
        .pill { display: inline-block; font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; color: #58a6ff;
                border: 1px solid rgba(88,166,255,0.4); background: rgba(88,166,255,0.08); padding: 6px 16px; border-radius: 20px; margin-bottom: 28px; }
        .hero h1 { font-size: clamp(2.4rem, 6vw, 4.2rem); font-weight: 800; line-height: 1.1; margin-bottom: 22px;
                   background: linear-gradient(180deg, #ffffff 30%, #8b949e); -webkit-background-clip: text; background-clip: text;
                   -webkit-text-fill-color: transparent; }
        .hero p.sub { color: #8b949e; font-size: 1.15rem; max-width: 620px; margin: 0 auto 14px; line-height: 1.6; }
        .hero p.note { color: #d29922; font-size: 0.9rem; margin-bottom: 38px; }
        .cta-row { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }
        .btn { background: #58a6ff; color: #000; padding: 15px 30px; border-radius: 8px; font-weight: 700; display: inline-block;
               transition: transform 0.15s ease, box-shadow 0.15s ease; }
        .btn:hover { transform: translateY(-2px); }
        .btn.ghost { background: transparent; color: #fff; border: 1px solid #30363d; }
        .btn.ghost:hover { border-color: #58a6ff; box-shadow: none; }

        .stats { display: flex; justify-content: center; gap: 0; flex-wrap: wrap; border-top: 1px solid #161b22; border-bottom: 1px solid #161b22; }
        .stat { padding: 28px 40px; text-align: center; flex: 1 1 200px; border-right: 1px solid #161b22; }
        .stat:last-child { border-right: none; }
        .stat b { display: block; font-size: 1.15rem; margin-bottom: 4px; }
        .stat span { color: #8b949e; font-size: 0.85rem; }

        section { padding: 90px 5vw; max-width: 1240px; margin: 0 auto; }
        .section-head { text-align: center; margin-bottom: 55px; }
        .section-head h2 { font-size: 2.2rem; font-weight: 800; margin-bottom: 12px; }
        .section-head p { color: #8b949e; max-width: 560px; margin: 0 auto; }

        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
        .feature { background: #0d1117; border: 1px solid #21262d; border-radius: 14px; padding: 32px; transition: border-color 0.2s ease; }
        .feature:hover { border-color: rgba(88,166,255,0.5); }
        .feature .icon { font-size: 1.6rem; margin-bottom: 16px; }
        .feature h3 { font-size: 1.1rem; margin-bottom: 10px; }
        .feature p { color: #8b949e; font-size: 0.92rem; line-height: 1.6; }

        .pricing { display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; }
        .card { background: #0d1117; padding: 40px 28px; border-radius: 14px; border: 1px solid #21262d; text-align: center;
                width: 252px; display: flex; flex-direction: column; transition: transform 0.15s ease, border-color 0.2s ease; }
        .card:hover { transform: translateY(-4px); border-color: #30363d; }
        .card.featured { border: 1px solid #58a6ff; box-shadow: 0 0 40px rgba(88,166,255,0.12); }
        .card .price { font-size: 2.1rem; font-weight: 800; margin: 18px 0 4px; }
        .card .per { color: #8b949e; font-size: 0.8rem; margin-bottom: 14px; }
        .card p.desc { color: #8b949e; font-size: 0.9rem; line-height: 1.55; flex: 1; }
        .card .btn { margin-top: 22px; }
        .badge { display: inline-block; font-size: 0.68rem; font-weight: 700; letter-spacing: 1.5px; padding: 5px 14px;
                 border-radius: 20px; margin-bottom: 16px; align-self: center; }
        .badge.preorder { color: #d29922; border: 1px solid #d29922; background: rgba(210,153,34,0.08); }
        .badge.live { color: #3fb950; border: 1px solid #3fb950; background: rgba(63,185,80,0.08); }

        footer { border-top: 1px solid #161b22; padding: 50px 5vw; text-align: center; }
        footer .brand { font-weight: 800; margin-bottom: 14px; }
        footer .brand span { color: #58a6ff; }
        footer p.disclaimer { color: #484f58; font-size: 0.75rem; max-width: 720px; margin: 0 auto 18px; line-height: 1.6; }
        footer p.copy { color: #8b949e; font-size: 0.8rem; }
    </style>
</head>
<body>
    <nav>
        <a href="/" class="logo">ai <span>PassiveAutotrades</span></a>
        <a href="#pricing" class="nav-cta">Get Access</a>
    </nav>

    <div class="hero">
        <div class="pill">AI-POWERED QUANT ENGINE</div>
        <h1>Institutional Income,<br>Automated.</h1>
        <p class="sub">Run professional-grade Z-score quant strategies without watching charts. High-frequency algorithmic precision, delivered passively.</p>
        <p class="note">The Prototype is live today &mdash; full-engine tiers are pre-orders and unlock at launch.</p>
        <div class="cta-row">
            <a href="#pricing" class="btn">Try the Prototype</a>
            <a href="#features" class="btn ghost">How It Works</a>
        </div>
    </div>

    <div class="stats">
        <div class="stat"><b>24/7</b><span>Market coverage, no screens</span></div>
        <div class="stat"><b>Z-Score</b><span>Statistical quant core</span></div>
        <div class="stat"><b>Hands-Free</b><span>Fully automated execution</span></div>
        <div class="stat"><b>API</b><span>Full access on VIP tier</span></div>
    </div>

    <section id="features">
        <div class="section-head">
            <h2>Built Like a Trading Desk. Runs Like an App.</h2>
            <p>The engine watches the market so you don't have to &mdash; every signal, entry, and exit handled algorithmically.</p>
        </div>
        <div class="features">
            <div class="feature">
                <div class="icon">&#128202;</div>
                <h3>Z-Score Signal Engine</h3>
                <p>Mean-reversion signals derived from statistical deviation, the same class of strategy used on institutional desks &mdash; not gut-feel indicators.</p>
            </div>
            <div class="feature">
                <div class="icon">&#9889;</div>
                <h3>High-Frequency Precision</h3>
                <p>Entries and exits execute algorithmically in milliseconds, around the clock. No hesitation, no emotion, no missed setups while you sleep.</p>
            </div>
            <div class="feature">
                <div class="icon">&#128737;&#65039;</div>
                <h3>Automated Risk Controls</h3>
                <p>Position sizing and exit logic are enforced by the engine on every trade, so a single position never runs unmanaged.</p>
            </div>
        </div>
    </section>

    <section id="pricing">
        <div class="section-head">
            <h2>Choose Your Tier</h2>
            <p>Start with the live Prototype today, or pre-order the full engine at founding prices before launch.</p>
        </div>
        <div class="pricing">
            <!-- Tier 0: Prototype (available now) -->
            <div class="card">
                <span class="badge live">AVAILABLE NOW</span>
                <h3>Prototype</h3>
                <div class="price">$79.99</div>
                <div class="per">one-time</div>
                <p class="desc">Instant access to the live prototype engine. Test-drive the strategy today.</p>
                <a href="YOUR_STRIPE_LINK_4" class="btn">Try Prototype</a>
            </div>

            <!-- Tier 1: Lifetime -->
            <div class="card">
                <span class="badge preorder">PRE-ORDER</span>
                <h3>Founding Alpha</h3>
                <div class="price">$199.99</div>
                <div class="per">one-time</div>
                <p class="desc">Lifetime access. No monthly fees, ever.</p>
                <a href="YOUR_STRIPE_LINK_1" class="btn">Get Started</a>
            </div>

            <!-- Tier 2: Monthly -->
            <div class="card">
                <span class="badge preorder">PRE-ORDER</span>
                <h3>Early Access Pass</h3>
                <div class="price">$49.99</div>
                <div class="per">per month</div>
                <p class="desc">Full engine utility. Billed monthly, cancel anytime.</p>
                <a href="YOUR_STRIPE_LINK_2" class="btn">Claim Monthly</a>
            </div>

            <!-- Tier 3: Annual -->
            <div class="card featured">
                <span class="badge preorder">PRE-ORDER</span>
                <h3>VIP Annual Pass</h3>
                <div class="price">$499.99</div>
                <div class="per">per year</div>
                <p class="desc">Priority execution + full API access.</p>
                <a href="YOUR_STRIPE_LINK_3" class="btn">Claim Annual</a>
            </div>
        </div>
    </section>

    <footer>
        <div class="brand">ai <span>PassiveAutotrades</span></div>
        <p class="disclaimer">Trading involves substantial risk of loss and is not suitable for every investor. Algorithmic strategies can lose money, and past or simulated performance does not guarantee future results. Nothing on this site is financial advice. Only trade with capital you can afford to lose.</p>
        <p class="copy">&copy; 2026 ai PassiveAutotrades. All rights reserved.</p>
    </footer>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def read_root():
    # s-maxage lets Vercel's global CDN serve the page without invoking this
    # function; the edge cache is purged automatically on every deploy, and
    # stale-while-revalidate keeps responses instant while refreshing.
    return HTMLResponse(
        content=HOMEPAGE_HTML,
        headers={
            "Cache-Control": "public, max-age=300, s-maxage=86400, stale-while-revalidate=604800"
        },
    )

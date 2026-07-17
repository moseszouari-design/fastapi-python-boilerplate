from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, Response


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
    <title>ai PassiveAutotrades — Automated Z-Score Quant Trading Engine</title>
    <meta name="description" content="Fully automated Z-score mean-reversion trading engine. Hands-free execution, built-in risk controls, and your funds never leave your own exchange account. Pre-order founding access.">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — Institutional Income, Automated.">
    <meta property="og:description" content="Automated Z-score quant strategies without watching charts. Pre-order founding access before launch.">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="en_US">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="ai PassiveAutotrades — Institutional Income, Automated.">
    <meta name="twitter:description" content="Automated Z-score quant strategies without watching charts. Pre-order founding access before launch.">
    <meta name="twitter:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <script defer src="/_vercel/insights/script.js"></script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "WebSite",
          "@id": "https://aipassiveautotrades.vercel.app/#website",
          "url": "https://aipassiveautotrades.vercel.app/",
          "name": "ai PassiveAutotrades",
          "description": "Automated Z-score mean-reversion trading engine with hands-free execution and built-in risk controls."
        },
        {
          "@type": "Product",
          "@id": "https://aipassiveautotrades.vercel.app/#product",
          "name": "ai PassiveAutotrades",
          "description": "A fully automated trading engine built on Z-score mean reversion, executing around the clock with enforced position sizing and exposure limits. All tiers are founding pre-orders; access is delivered at launch.",
          "brand": { "@type": "Brand", "name": "ai PassiveAutotrades" },
          "image": "https://aipassiveautotrades.vercel.app/og.png",
          "url": "https://aipassiveautotrades.vercel.app/",
          "offers": [
            { "@type": "Offer", "name": "Prototype (Pre-Order)", "price": "79.99", "priceCurrency": "USD", "availability": "https://schema.org/PreOrder", "url": "https://aipassiveautotrades.vercel.app/#pricing" },
            { "@type": "Offer", "name": "Founding Alpha — Lifetime (Pre-Order)", "price": "199.99", "priceCurrency": "USD", "availability": "https://schema.org/PreOrder", "url": "https://aipassiveautotrades.vercel.app/#pricing" },
            { "@type": "Offer", "name": "Early Access Pass — Monthly (Pre-Order)", "price": "49.99", "priceCurrency": "USD", "availability": "https://schema.org/PreOrder", "url": "https://aipassiveautotrades.vercel.app/#pricing" },
            { "@type": "Offer", "name": "VIP Annual Pass (Pre-Order)", "price": "499.99", "priceCurrency": "USD", "availability": "https://schema.org/PreOrder", "url": "https://aipassiveautotrades.vercel.app/#pricing" }
          ]
        },
        {
          "@type": "FAQPage",
          "@id": "https://aipassiveautotrades.vercel.app/#faq",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "What exactly am I buying with a pre-order?",
              "acceptedAnswer": { "@type": "Answer", "text": "You're reserving access to the engine at founding pricing before public launch. Your tier and price are locked to your account permanently. Founding members are onboarded first when the engine goes live, and launch updates are sent to the email you use at checkout." }
            },
            {
              "@type": "Question",
              "name": "Do my funds ever leave my control?",
              "acceptedAnswer": { "@type": "Answer", "text": "No. The engine connects to your own exchange account via API keys that you control and can revoke at any time. We never take custody of your capital, and withdrawal permissions are never required." }
            },
            {
              "@type": "Question",
              "name": "Do I need trading experience?",
              "acceptedAnswer": { "@type": "Answer", "text": "No chart-reading or trading skill is required to operate the engine — configuration is a one-time setup. You should, however, understand that all trading carries real risk of loss before committing any capital." }
            },
            {
              "@type": "Question",
              "name": "Can the engine lose money?",
              "acceptedAnswer": { "@type": "Answer", "text": "Yes. No strategy wins every trade, and mean reversion carries risk in strongly trending markets. That is why the engine enforces position sizing and exposure limits on every trade. Never trade capital you can't afford to lose." }
            },
            {
              "@type": "Question",
              "name": "What's the difference between the tiers?",
              "acceptedAnswer": { "@type": "Answer", "text": "Prototype is single-market entry access to the prototype engine. Founding Alpha is full lifetime access with no recurring fees. Early Access is the same full engine billed monthly with cancel-anytime flexibility. VIP Annual adds priority execution, full API access, and priority support." }
            },
            {
              "@type": "Question",
              "name": "What happens after I pre-order?",
              "acceptedAnswer": { "@type": "Answer", "text": "You'll receive your order confirmation immediately, followed by launch timeline updates and onboarding instructions by email. Founding members onboard before public availability opens." }
            },
            {
              "@type": "Question",
              "name": "Can I get a refund?",
              "acceptedAnswer": { "@type": "Answer", "text": "Yes — pre-orders are fully refundable at any time before launch. Contact support (details are on your purchase receipt) and the refund will be processed. After launch, the monthly and annual passes can be cancelled anytime to stop future billing." }
            }
          ]
        }
      ]
    }
    </script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #050608; --panel: #0c0f14; --panel-2: #10141b; --line: #1c2230; --line-soft: #141924;
            --text: #eef2f8; --muted: #97a1b3; --faint: #5b6474;
            --accent: #4f8ff7; --accent-soft: rgba(79,143,247,0.12); --amber: #d9a13b; --green: #46b876;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-padding-top: 84px; }
        body { background: var(--bg); color: var(--text); font-family: 'Inter', -apple-system, sans-serif;
               -webkit-font-smoothing: antialiased; line-height: 1.6; }
        a { text-decoration: none; color: inherit; }
        .mono { font-family: 'JetBrains Mono', monospace; }
        .wrap { max-width: 1160px; margin: 0 auto; padding: 0 24px; }

        /* ---------- nav ---------- */
        nav { position: sticky; top: 0; z-index: 20; background: rgba(5,6,8,0.97); border-bottom: 1px solid var(--line-soft); }
        .nav-inner { max-width: 1160px; margin: 0 auto; padding: 0 24px; height: 68px; display: flex; align-items: center; gap: 36px; }
        .logo { font-weight: 800; font-size: 1rem; letter-spacing: 0.2px; white-space: nowrap; }
        .logo em { font-style: normal; color: var(--accent); }
        .nav-links { display: flex; gap: 28px; font-size: 0.88rem; color: var(--muted); font-weight: 500; }
        .nav-links a:hover { color: var(--text); }
        .nav-cta { margin-left: auto; background: var(--accent); color: #04070d; padding: 10px 20px; border-radius: 8px;
                   font-weight: 700; font-size: 0.86rem; white-space: nowrap; }
        .nav-cta:hover { background: #6ba1f8; }

        /* ---------- hero ---------- */
        .hero { border-bottom: 1px solid var(--line-soft);
                background: radial-gradient(ellipse 1000px 480px at 70% -120px, rgba(79,143,247,0.13), transparent 65%); }
        .hero-grid { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 60px; align-items: center; padding: 96px 0 88px; }
        .eyebrow { display: inline-flex; align-items: center; gap: 8px; font-size: 0.72rem; font-weight: 700; letter-spacing: 2.2px;
                   color: var(--accent); border: 1px solid rgba(79,143,247,0.35); background: var(--accent-soft);
                   padding: 6px 14px; border-radius: 999px; margin-bottom: 26px; }
        .eyebrow .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--accent); }
        h1 { font-size: clamp(2.3rem, 4.6vw, 3.6rem); font-weight: 800; line-height: 1.08; letter-spacing: -0.02em; margin-bottom: 20px; }
        h1 .grad { background: linear-gradient(90deg, #7db0ff, #4f8ff7); -webkit-background-clip: text;
                   background-clip: text; -webkit-text-fill-color: transparent; }
        .hero-sub { color: var(--muted); font-size: 1.08rem; max-width: 480px; margin-bottom: 18px; }
        .hero-note { display: inline-block; font-size: 0.8rem; font-weight: 600; color: var(--amber);
                     border: 1px solid rgba(217,161,59,0.35); background: rgba(217,161,59,0.07);
                     padding: 7px 14px; border-radius: 8px; margin-bottom: 30px; }
        .cta-row { display: flex; gap: 12px; flex-wrap: wrap; }
        .btn { display: inline-block; padding: 14px 28px; border-radius: 9px; font-weight: 700; font-size: 0.95rem; }
        .btn.primary { background: var(--accent); color: #04070d; }
        .btn.primary:hover { background: #6ba1f8; }
        .btn.ghost { color: var(--text); border: 1px solid var(--line); }
        .btn.ghost:hover { border-color: var(--accent); }
        .hero-foot { display: flex; gap: 22px; margin-top: 26px; color: var(--faint); font-size: 0.78rem; flex-wrap: wrap; }
        .hero-foot span::before { content: '✓'; color: var(--green); margin-right: 6px; font-weight: 700; }

        /* console panel */
        .console { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; overflow: hidden;
                   font-size: 0.78rem; box-shadow: 0 24px 60px rgba(0,0,0,0.45); }
        .console-bar { display: flex; align-items: center; gap: 8px; padding: 12px 16px; border-bottom: 1px solid var(--line-soft);
                       background: var(--panel-2); }
        .console-bar .dots { display: flex; gap: 6px; }
        .console-bar .dots i { width: 10px; height: 10px; border-radius: 50%; background: #2a3242; display: block; }
        .console-bar .title { margin-left: 8px; color: var(--faint); font-size: 0.72rem; letter-spacing: 1px; }
        .console-body { padding: 18px 20px; display: grid; gap: 10px; }
        .crow { display: flex; justify-content: space-between; align-items: baseline; gap: 12px;
                border-bottom: 1px dashed var(--line-soft); padding-bottom: 10px; }
        .crow:last-child { border-bottom: none; padding-bottom: 0; }
        .crow .pair { color: var(--text); font-weight: 600; }
        .crow .z { color: var(--muted); }
        .crow .sig { font-weight: 600; font-size: 0.72rem; letter-spacing: 0.5px; padding: 3px 10px; border-radius: 999px; }
        .sig.armed { color: var(--accent); background: var(--accent-soft); border: 1px solid rgba(79,143,247,0.3); }
        .sig.idle { color: var(--faint); background: rgba(92,100,117,0.1); border: 1px solid var(--line-soft); }
        .console-foot { padding: 12px 20px; border-top: 1px solid var(--line-soft); background: var(--panel-2);
                        color: var(--faint); font-size: 0.7rem; display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
        .console-caption { text-align: center; color: var(--faint); font-size: 0.7rem; margin-top: 12px; letter-spacing: 0.4px; }

        /* ---------- stats strip ---------- */
        .strip { border-bottom: 1px solid var(--line-soft); }
        .strip-inner { max-width: 1160px; margin: 0 auto; padding: 0 24px; display: grid; grid-template-columns: repeat(4, 1fr); }
        .stat { padding: 26px 18px; text-align: center; border-left: 1px solid var(--line-soft); }
        .stat:first-child { border-left: none; }
        .stat b { display: block; font-size: 1.25rem; font-weight: 800; letter-spacing: -0.01em; }
        .stat span { color: var(--faint); font-size: 0.78rem; }

        /* ---------- sections ---------- */
        section { padding: 96px 0; }
        section.alt { background: #07090d; border-top: 1px solid var(--line-soft); border-bottom: 1px solid var(--line-soft); }
        .sec-label { font-size: 0.72rem; font-weight: 700; letter-spacing: 2.4px; color: var(--accent); margin-bottom: 14px; }
        .sec-head { max-width: 640px; margin-bottom: 56px; }
        .sec-head.center { margin-left: auto; margin-right: auto; text-align: center; }
        h2 { font-size: clamp(1.7rem, 3vw, 2.3rem); font-weight: 800; letter-spacing: -0.02em; line-height: 1.15; margin-bottom: 14px; }
        .sec-head p { color: var(--muted); font-size: 1rem; }

        .steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .step { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 30px; }
        .step .num { font-family: 'JetBrains Mono', monospace; color: var(--accent); font-size: 0.8rem; font-weight: 600;
                     display: block; margin-bottom: 16px; }
        .step h3 { font-size: 1.05rem; margin-bottom: 10px; }
        .step p { color: var(--muted); font-size: 0.9rem; }

        .split { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }
        .split .sec-head { margin-bottom: 0; }
        .checklist { display: grid; gap: 14px; margin-top: 26px; }
        .checklist li { list-style: none; display: flex; gap: 12px; color: var(--muted); font-size: 0.93rem; }
        .checklist li::before { content: '✓'; color: var(--green); font-weight: 700; flex-shrink: 0; }
        .quote-box { background: var(--panel); border: 1px solid var(--line); border-left: 3px solid var(--accent);
                     border-radius: 12px; padding: 28px 30px; }
        .quote-box .big { font-size: 1.15rem; font-weight: 600; line-height: 1.5; margin-bottom: 14px; }
        .quote-box .src { color: var(--faint); font-size: 0.8rem; }

        .grid-6 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
        .cell { background: var(--panel); border: 1px solid var(--line); border-radius: 13px; padding: 26px; }
        .cell:hover { border-color: #2a3450; }
        .cell h3 { font-size: 0.98rem; margin-bottom: 8px; }
        .cell p { color: var(--muted); font-size: 0.87rem; }
        .cell .ic { display: inline-flex; width: 38px; height: 38px; align-items: center; justify-content: center;
                    background: var(--accent-soft); border: 1px solid rgba(79,143,247,0.25); border-radius: 9px;
                    margin-bottom: 16px; font-size: 1rem; }

        /* ---------- pricing ---------- */
        .tiers { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; align-items: stretch; }
        .tier { background: var(--panel); border: 1px solid var(--line); border-radius: 15px; padding: 30px 26px;
                display: flex; flex-direction: column; }
        .tier:hover { border-color: #2a3450; }
        .tier.featured { border-color: var(--accent); position: relative; }
        .tier.featured .flag { position: absolute; top: -11px; left: 50%; transform: translateX(-50%);
                               background: var(--accent); color: #04070d; font-size: 0.66rem; font-weight: 800;
                               letter-spacing: 1.2px; padding: 4px 12px; border-radius: 999px; white-space: nowrap; }
        .badge { align-self: flex-start; font-size: 0.64rem; font-weight: 700; letter-spacing: 1.4px; padding: 5px 12px;
                 border-radius: 999px; margin-bottom: 18px; color: var(--amber); border: 1px solid rgba(217,161,59,0.45);
                 background: rgba(217,161,59,0.07); }
        .tier h3 { font-size: 1.02rem; margin-bottom: 4px; }
        .tier .who { color: var(--faint); font-size: 0.78rem; margin-bottom: 18px; }
        .tier .price { font-size: 2rem; font-weight: 800; letter-spacing: -0.02em; }
        .tier .per { color: var(--faint); font-size: 0.78rem; margin-bottom: 20px; }
        .tier ul { list-style: none; display: grid; gap: 10px; margin-bottom: 26px; flex: 1; }
        .tier ul li { display: flex; gap: 10px; color: var(--muted); font-size: 0.84rem; line-height: 1.45; }
        .tier ul li::before { content: '✓'; color: var(--green); font-weight: 700; flex-shrink: 0; }
        .tier .btn { text-align: center; width: 100%; padding: 13px 0; }
        .pricing-note { text-align: center; color: var(--faint); font-size: 0.8rem; margin-top: 26px; }

        /* ---------- faq ---------- */
        .faq { max-width: 760px; margin: 0 auto; display: grid; gap: 12px; }
        details { background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 0 24px; }
        details[open] { border-color: #2a3450; }
        summary { cursor: pointer; list-style: none; font-weight: 600; font-size: 0.96rem; padding: 20px 0;
                  display: flex; justify-content: space-between; align-items: center; gap: 16px; }
        summary::-webkit-details-marker { display: none; }
        summary::after { content: '+'; color: var(--accent); font-size: 1.3rem; font-weight: 400; flex-shrink: 0; }
        details[open] summary::after { content: '\\2212'; }
        details .a { color: var(--muted); font-size: 0.9rem; padding-bottom: 22px; }

        /* ---------- final cta ---------- */
        .final { text-align: center; border-top: 1px solid var(--line-soft);
                 background: radial-gradient(ellipse 800px 400px at 50% 120%, rgba(79,143,247,0.12), transparent 65%); }
        .final h2 { margin-bottom: 12px; }
        .final p { color: var(--muted); max-width: 480px; margin: 0 auto 32px; }

        /* ---------- footer ---------- */
        footer { border-top: 1px solid var(--line-soft); padding: 56px 0 44px; }
        .foot-top { display: flex; justify-content: space-between; gap: 30px; flex-wrap: wrap; margin-bottom: 36px; }
        .foot-links { display: flex; gap: 26px; color: var(--muted); font-size: 0.85rem; }
        .foot-links a:hover { color: var(--text); }
        .disclaimer { color: #4a5261; font-size: 0.73rem; line-height: 1.7; border-top: 1px solid var(--line-soft);
                      padding-top: 26px; max-width: 900px; }
        .copyright { color: var(--faint); font-size: 0.78rem; margin-top: 18px; }

        /* ---------- responsive ---------- */
        @media (max-width: 960px) {
            .hero-grid { grid-template-columns: 1fr; gap: 48px; padding: 64px 0; }
            .split { grid-template-columns: 1fr; gap: 40px; }
            .steps, .grid-6 { grid-template-columns: 1fr 1fr; }
            .tiers { grid-template-columns: 1fr 1fr; }
            .strip-inner { grid-template-columns: 1fr 1fr; }
            .stat:nth-child(3) { border-left: none; }
            .stat { border-top: 1px solid var(--line-soft); }
            .stat:nth-child(-n+2) { border-top: none; }
            .nav-links { display: none; }
        }
        @media (max-width: 620px) {
            .steps, .grid-6, .tiers { grid-template-columns: 1fr; }
            section { padding: 68px 0; }
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-inner">
            <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
            <div class="nav-links">
                <a href="#how">How It Works</a>
                <a href="#strategy">Strategy</a>
                <a href="#pricing">Pricing</a>
                <a href="#faq">FAQ</a>
            </div>
            <a href="#pricing" class="nav-cta">Pre-Order Access</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>AUTOMATED Z-SCORE QUANT ENGINE</div>
                    <h1>Institutional Income,<br><span class="grad">Automated.</span></h1>
                    <p class="hero-sub">A fully automated trading engine built on Z-score mean reversion &mdash; the same statistical methodology quant desks run &mdash; executing around the clock so you never watch a chart.</p>
                    <div class="hero-note">Founding pre-order &mdash; lock lifetime pricing before public launch</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">View Pre-Order Tiers</a>
                        <a href="#how" class="btn ghost">See How It Works</a>
                    </div>
                    <div class="hero-foot">
                        <span>Hands-free execution</span>
                        <span>Built-in risk controls</span>
                        <span>Cancel-anytime option</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">ENGINE &mdash; SIGNAL MONITOR</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC&ndash;USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT &middot; ARMED</span></div>
                            <div class="crow"><span class="pair">ETH&ndash;USD</span><span class="z">z&nbsp;=&nbsp;&minus;0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL&ndash;USD</span><span class="z">z&nbsp;=&nbsp;&minus;2.87</span><span class="sig armed">REVERT &middot; ARMED</span></div>
                            <div class="crow"><span class="pair">XRP&ndash;USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risk check &#10003; &nbsp; sizing &#10003; &nbsp; exposure limits &#10003;</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">Illustrative signal feed &mdash; how the engine reads the market</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>autonomous market coverage</span></div>
            <div class="stat"><b>ms</b><span>algorithmic execution speed</span></div>
            <div class="stat"><b>0</b><span>charts you need to watch</span></div>
            <div class="stat"><b>100%</b><span>rule-based &mdash; zero emotion</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">HOW IT WORKS</div>
            <div class="sec-head">
                <h2>Three steps. Then the engine takes over.</h2>
                <p>No signal groups, no screen time, no discretionary decisions. Once configured, every entry and exit is systematic.</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>Secure Your Tier</h3>
                    <p>Pre-order the tier that fits you. Founding pricing is locked permanently to your account &mdash; it will never be offered again after launch.</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>Connect &amp; Configure</h3>
                    <p>At launch, link the engine to your exchange account and set your risk parameters once. Your funds stay in your own account at all times.</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>The Engine Executes</h3>
                    <p>The Z-score core monitors statistical deviation around the clock and executes entries, exits, and position sizing automatically.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">THE STRATEGY</div>
                    <h2>Why Z-score mean reversion?</h2>
                    <p>Markets overreact. Prices stretch away from their statistical average, and stretched prices tend to snap back. A Z-score measures exactly how stretched a price is &mdash; in standard deviations &mdash; turning &ldquo;this looks overextended&rdquo; into a precise, testable number.</p>
                    <ul class="checklist">
                        <li>Trades a defined statistical edge &mdash; not indicators, hunches, or hype</li>
                        <li>Every position is entered and exited by rule, with risk sized before the trade is placed</li>
                        <li>The same methodology class used on institutional stat-arb desks for decades</li>
                        <li>Emotionless by construction: the engine cannot revenge-trade, FOMO, or hesitate</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">&ldquo;When price deviates beyond &plusmn;2 standard deviations from its rolling mean, the engine arms a reversion position &mdash; and manages it to completion without human input.&rdquo;</div>
                    <div class="src">&mdash; The core rule inside ai PassiveAutotrades, stated plainly. No black box, no mystery signals.</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">WHAT YOU GET</div>
            <div class="sec-head">
                <h2>Engineered like a desk. Delivered like a product.</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>Z-Score Signal Core</h3><p>Rolling-window statistical deviation drives every signal &mdash; transparent, testable, and consistent.</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>Millisecond Execution</h3><p>Signals fire algorithmically the moment thresholds are crossed &mdash; day, night, weekends.</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>Hard Risk Limits</h3><p>Per-trade sizing, exposure caps, and automated exits are enforced on every single position.</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>Your Funds, Your Account</h3><p>The engine connects to your own exchange account. Capital never moves to us.</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>Set-Once Configuration</h3><p>Choose risk level and markets a single time. No ongoing maintenance or babysitting.</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>API Access <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>Full programmatic access to the engine for custom integrations and monitoring.</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">FOUNDING PRE-ORDER</div>
                <h2>Lock your tier before launch</h2>
                <p>Every tier is a pre-order at founding pricing. When the engine launches, founding members onboard first &mdash; and these prices are permanently retired.</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">PRE-ORDER</span>
                    <h3>Prototype</h3>
                    <div class="who">For first-time algo users</div>
                    <div class="price">$79.99</div>
                    <div class="per">one-time</div>
                    <ul>
                        <li>Entry access to the prototype engine</li>
                        <li>Core Z-score strategy, one market</li>
                        <li>Standard risk controls</li>
                        <li>Email support</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Get Prototype</a>
                </div>
                <div class="tier">
                    <span class="badge">PRE-ORDER</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">For long-term believers</div>
                    <div class="price">$199.99</div>
                    <div class="per">one-time &middot; lifetime</div>
                    <ul>
                        <li>Lifetime full-engine access</li>
                        <li>All markets &amp; strategy updates, forever</li>
                        <li>No recurring fees, ever</li>
                        <li>Priority onboarding at launch</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">Claim Lifetime</a>
                </div>
                <div class="tier">
                    <span class="badge">PRE-ORDER</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">For flexible starters</div>
                    <div class="price">$49.99</div>
                    <div class="per">per month</div>
                    <ul>
                        <li>Full engine utility</li>
                        <li>All markets included</li>
                        <li>Cancel anytime</li>
                        <li>Standard support</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">Claim Monthly</a>
                </div>
                <div class="tier featured">
                    <span class="flag">BEST VALUE</span>
                    <span class="badge">PRE-ORDER</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">For serious operators</div>
                    <div class="price">$499.99</div>
                    <div class="per">per year</div>
                    <ul>
                        <li>Everything in Early Access</li>
                        <li>Priority execution queue</li>
                        <li>Full API access</li>
                        <li>Priority support channel</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">Claim Annual</a>
                </div>
            </div>
            <p class="pricing-note">Secure checkout via Stripe &middot; Founding prices retire permanently at public launch</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">QUESTIONS</div>
                <h2>Asked before buying</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>What exactly am I buying with a pre-order?</summary>
                    <div class="a">You're reserving access to the engine at founding pricing before public launch. Your tier and price are locked to your account permanently. Founding members are onboarded first when the engine goes live, and launch updates are sent to the email you use at checkout.</div>
                </details>
                <details>
                    <summary>Do my funds ever leave my control?</summary>
                    <div class="a">No. The engine connects to your own exchange account via API keys that you control and can revoke at any time. We never take custody of your capital, and withdrawal permissions are never required.</div>
                </details>
                <details>
                    <summary>Do I need trading experience?</summary>
                    <div class="a">No chart-reading or trading skill is required to operate the engine &mdash; configuration is a one-time setup. You should, however, understand that all trading carries real risk of loss before committing any capital.</div>
                </details>
                <details>
                    <summary>Can the engine lose money?</summary>
                    <div class="a">Yes. Any honest answer to this question is yes &mdash; no strategy wins every trade, and mean reversion carries risk in strongly trending markets. That's precisely why the engine enforces position sizing and exposure limits on every trade. Never trade capital you can't afford to lose.</div>
                </details>
                <details>
                    <summary>What's the difference between the tiers?</summary>
                    <div class="a">Prototype is single-market entry access to the prototype engine. Founding Alpha is full lifetime access with no recurring fees. Early Access is the same full engine billed monthly with cancel-anytime flexibility. VIP Annual adds priority execution, full API access, and priority support.</div>
                </details>
                <details>
                    <summary>What happens after I pre-order?</summary>
                    <div class="a">You'll receive your order confirmation immediately, followed by launch timeline updates and onboarding instructions by email. Founding members onboard before public availability opens.</div>
                </details>
                <details>
                    <summary>Can I get a refund?</summary>
                    <div class="a">Yes &mdash; pre-orders are fully refundable at any time before launch. Contact support (details are on your purchase receipt) and the refund will be processed. After launch, the monthly and annual passes can be cancelled anytime to stop future billing. Full details in our <a href="/terms" style="color:var(--accent)">Terms of Service</a>.</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>Founding pricing ends at launch.</h2>
            <p>Reserve your tier now &mdash; when the engine goes public, these prices are permanently retired.</p>
            <a href="#pricing" class="btn primary">Pre-Order Your Tier</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">How It Works</a>
                    <a href="#strategy">Strategy</a>
                    <a href="#pricing">Pricing</a>
                    <a href="#faq">FAQ</a>
                    <a href="/terms">Terms</a>
                    <a href="/privacy">Privacy</a>
                </div>
            </div>
            <p class="disclaimer">Risk disclosure: Trading involves substantial risk of loss and is not suitable for every investor. Algorithmic and automated strategies can and do lose money; past or simulated performance does not guarantee future results. ai PassiveAutotrades is a software tool &mdash; it is not an investment adviser, broker-dealer, or fiduciary, and nothing on this site constitutes financial advice or a solicitation to trade. Pre-order purchases grant software access at launch as described above. Only trade with capital you can afford to lose.</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""


LEGAL_STYLE = """
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #050608; color: #eef2f8; font-family: 'Inter', -apple-system, sans-serif; line-height: 1.7; }
    a { color: #4f8ff7; text-decoration: none; }
    .page { max-width: 760px; margin: 0 auto; padding: 64px 24px 96px; }
    .back { display: inline-block; color: #97a1b3; font-size: 0.85rem; margin-bottom: 40px; }
    h1 { font-size: 2rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 8px; }
    .updated { color: #5b6474; font-size: 0.8rem; margin-bottom: 40px; }
    h2 { font-size: 1.15rem; font-weight: 700; margin: 36px 0 10px; }
    p, li { color: #97a1b3; font-size: 0.95rem; margin-bottom: 12px; }
    ul { padding-left: 22px; }
</style>
"""

TERMS_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service | ai PassiveAutotrades</title>
    <meta name="robots" content="index, follow">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/terms">
""" + LEGAL_STYLE + """
</head>
<body>
    <div class="page">
        <a href="/" class="back">&larr; Back to ai PassiveAutotrades</a>
        <h1>Terms of Service</h1>
        <p class="updated">Last updated: July 16, 2026</p>

        <h2>1. What we provide</h2>
        <p>ai PassiveAutotrades ("the Service") sells pre-order access to automated trading software (the "Engine"). A pre-order reserves your access tier at founding pricing; the Engine itself is delivered when it launches. The Service is a software tool only &mdash; it is not an investment adviser, broker-dealer, or fiduciary, and nothing on this site is financial advice.</p>

        <h2>2. Pre-orders and delivery</h2>
        <p>Purchasing a pre-order tier grants you the access described on the pricing page, delivered at launch. Founding members are onboarded before public availability. Launch timing will be communicated by email to the address used at checkout.</p>

        <h2>3. Payments, subscriptions, and cancellation</h2>
        <p>Payments are processed by Stripe. One-time tiers (Prototype, Founding Alpha) are charged once. Subscription tiers (Early Access monthly, VIP Annual yearly) renew automatically until cancelled; you can cancel at any time to stop future billing, and cancellation takes effect at the end of the paid period.</p>

        <h2>4. Refunds</h2>
        <p>Pre-orders are fully refundable at any time before the Engine launches &mdash; contact support and the refund will be processed. After launch, subscription tiers may be cancelled anytime to prevent future charges; charges for periods already delivered are non-refundable except where required by law.</p>

        <h2>5. Trading risk</h2>
        <p>Trading involves substantial risk of loss and is not suitable for every investor. Algorithmic strategies can and do lose money. Past or simulated performance does not guarantee future results. You are solely responsible for your trading decisions, exchange accounts, and capital. Never trade money you cannot afford to lose.</p>

        <h2>6. Your account and conduct</h2>
        <p>You are responsible for the security of your exchange API keys and accounts. You agree not to reverse-engineer, resell, or share access to the Engine without permission.</p>

        <h2>7. Limitation of liability</h2>
        <p>To the maximum extent permitted by law, the Service and its operators are not liable for trading losses, lost profits, or indirect, incidental, or consequential damages arising from use of the Engine. Total liability is limited to the amount you paid for the Service.</p>

        <h2>8. Changes</h2>
        <p>These terms may be updated; material changes will be posted on this page with a new date. Continued use after changes constitutes acceptance.</p>

        <h2>9. Contact</h2>
        <p>Support contact details are provided on your purchase receipt and in launch communications.</p>
    </div>
</body>
</html>
"""

PRIVACY_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy | ai PassiveAutotrades</title>
    <meta name="robots" content="index, follow">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/privacy">
""" + LEGAL_STYLE + """
</head>
<body>
    <div class="page">
        <a href="/" class="back">&larr; Back to ai PassiveAutotrades</a>
        <h1>Privacy Policy</h1>
        <p class="updated">Last updated: July 16, 2026</p>

        <h2>1. What we collect</h2>
        <p>When you purchase, checkout is handled entirely by Stripe: your name, email, and payment details are collected and stored by Stripe under its own privacy policy. We never see or store your card details. If you sign up for launch updates, we store the email address you provide.</p>

        <h2>2. How we use it</h2>
        <ul>
            <li>To deliver what you purchased: order confirmation, launch updates, and onboarding instructions.</li>
            <li>To provide support when you contact us.</li>
            <li>To send launch-related email you signed up for. Every email includes an unsubscribe link.</li>
        </ul>

        <h2>3. What we don't do</h2>
        <p>We do not sell your personal data. We do not share it with third parties except the processors below, and we do not use it for unrelated advertising.</p>

        <h2>4. Processors we rely on</h2>
        <ul>
            <li><strong>Stripe</strong> &mdash; payment processing (stripe.com/privacy)</li>
            <li><strong>Vercel</strong> &mdash; website hosting (vercel.com/legal/privacy-policy)</li>
            <li><strong>MailerLite</strong> &mdash; email updates, if you subscribe (mailerlite.com/legal/privacy-policy)</li>
        </ul>

        <h2>5. Your rights</h2>
        <p>You can request a copy or deletion of your personal data, or unsubscribe from emails at any time, by contacting support (details on your purchase receipt) or using the unsubscribe link in any email.</p>

        <h2>6. Changes</h2>
        <p>Updates to this policy will be posted on this page with a new date.</p>
    </div>
</body>
</html>
"""

ROBOTS_TXT = """User-agent: *
Allow: /

Sitemap: https://aipassiveautotrades.vercel.app/sitemap.xml
"""

SITEMAP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://aipassiveautotrades.vercel.app/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/terms</loc>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/privacy</loc>
    <changefreq>monthly</changefreq>
    <priority>0.3</priority>
  </url>
</urlset>
"""

CACHE_HEADERS = {
    "Cache-Control": "public, max-age=300, s-maxage=86400, stale-while-revalidate=604800"
}


@app.get("/", response_class=HTMLResponse)
def read_root():
    # s-maxage lets Vercel's global CDN serve the page without invoking this
    # function; the edge cache is purged automatically on every deploy, and
    # stale-while-revalidate keeps responses instant while refreshing.
    return HTMLResponse(content=HOMEPAGE_HTML, headers=CACHE_HEADERS)


@app.get("/terms", response_class=HTMLResponse)
def terms():
    return HTMLResponse(content=TERMS_HTML, headers=CACHE_HEADERS)


@app.get("/privacy", response_class=HTMLResponse)
def privacy():
    return HTMLResponse(content=PRIVACY_HTML, headers=CACHE_HEADERS)


@app.get("/robots.txt", response_class=PlainTextResponse)
def robots():
    return PlainTextResponse(content=ROBOTS_TXT, headers=CACHE_HEADERS)


@app.get("/sitemap.xml")
def sitemap():
    return Response(content=SITEMAP_XML, media_type="application/xml", headers=CACHE_HEADERS)

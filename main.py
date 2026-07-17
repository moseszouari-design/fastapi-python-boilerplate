from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, Response


app = FastAPI(
    title="ai PassiveAutotrades",
    description="Institutional Alpha",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
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
    <link rel="alternate" hreflang="en" href="https://aipassiveautotrades.vercel.app/">
    <link rel="alternate" hreflang="es" href="https://aipassiveautotrades.vercel.app/es">
    <link rel="alternate" hreflang="fr" href="https://aipassiveautotrades.vercel.app/fr">
    <link rel="alternate" hreflang="x-default" href="https://aipassiveautotrades.vercel.app/">
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
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
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
        .lang { margin-left: auto; display: flex; gap: 10px; font-size: 0.78rem; font-weight: 600; color: var(--faint); }
        .lang a { color: var(--faint); }
        .lang a:hover { color: var(--text); }
        .lang .cur { color: var(--text); }
        .nav-cta { background: var(--accent); color: #04070d; padding: 10px 20px; border-radius: 8px;
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
            <div class="lang"><span class="cur">EN</span><a href="/es">ES</a><a href="/fr">FR</a></div>
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
            <p class="pricing-note">Secure checkout via Stripe &middot; Pay in USD, EUR, GBP, CAD or AUD &mdash; your currency is detected automatically at checkout &middot; Founding prices retire permanently at public launch</p>
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


# The translated pages reuse the exact stylesheet from the English page so the
# design never drifts between languages.
HOMEPAGE_STYLE = "<style>" + HOMEPAGE_HTML.split("<style>")[1].split("</style>")[0] + "</style>"

HREFLANG_LINKS = """
    <link rel="alternate" hreflang="en" href="https://aipassiveautotrades.vercel.app/">
    <link rel="alternate" hreflang="es" href="https://aipassiveautotrades.vercel.app/es">
    <link rel="alternate" hreflang="fr" href="https://aipassiveautotrades.vercel.app/fr">
    <link rel="alternate" hreflang="x-default" href="https://aipassiveautotrades.vercel.app/">
"""

HOMEPAGE_HTML_ES = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — Motor de Trading Cuantitativo Z-Score Automatizado</title>
    <meta name="description" content="Motor de trading automatizado basado en reversión a la media Z-score. Ejecución sin intervención, controles de riesgo integrados y tus fondos nunca salen de tu propia cuenta. Reserva tu acceso fundador.">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/es">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/es">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — Ingresos Institucionales, Automatizados.">
    <meta property="og:description" content="Estrategias cuantitativas Z-score automatizadas sin mirar gráficos. Reserva tu acceso fundador antes del lanzamiento.">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="es_ES">
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
""" + HOMEPAGE_STYLE + """
</head>
<body>
    <nav>
        <div class="nav-inner">
            <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
            <div class="nav-links">
                <a href="#how">Cómo Funciona</a>
                <a href="#strategy">Estrategia</a>
                <a href="#pricing">Precios</a>
                <a href="#faq">Preguntas</a>
            </div>
            <div class="lang"><a href="/">EN</a><span class="cur">ES</span><a href="/fr">FR</a></div>
            <a href="#pricing" class="nav-cta">Reservar Acceso</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>MOTOR CUANTITATIVO Z-SCORE AUTOMATIZADO</div>
                    <h1>Ingresos Institucionales,<br><span class="grad">Automatizados.</span></h1>
                    <p class="hero-sub">Un motor de trading totalmente automatizado basado en reversión a la media Z-score &mdash; la misma metodología estadística que usan las mesas cuantitativas &mdash; ejecutando las 24 horas para que nunca mires un gráfico.</p>
                    <div class="hero-note">Reserva fundadora &mdash; asegura el precio de por vida antes del lanzamiento público</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">Ver Niveles de Reserva</a>
                        <a href="#how" class="btn ghost">Cómo Funciona</a>
                    </div>
                    <div class="hero-foot">
                        <span>Ejecución sin intervención</span>
                        <span>Controles de riesgo integrados</span>
                        <span>Opción de cancelar cuando quieras</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">MOTOR &mdash; MONITOR DE SEÑALES</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC&ndash;USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT &middot; ARMED</span></div>
                            <div class="crow"><span class="pair">ETH&ndash;USD</span><span class="z">z&nbsp;=&nbsp;&minus;0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL&ndash;USD</span><span class="z">z&nbsp;=&nbsp;&minus;2.87</span><span class="sig armed">REVERT &middot; ARMED</span></div>
                            <div class="crow"><span class="pair">XRP&ndash;USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>riesgo &#10003; &nbsp; tama&ntilde;o &#10003; &nbsp; l&iacute;mites de exposici&oacute;n &#10003;</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">Se&ntilde;ales ilustrativas &mdash; as&iacute; lee el motor el mercado</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>cobertura aut&oacute;noma del mercado</span></div>
            <div class="stat"><b>ms</b><span>velocidad de ejecuci&oacute;n algor&iacute;tmica</span></div>
            <div class="stat"><b>0</b><span>gr&aacute;ficos que necesitas mirar</span></div>
            <div class="stat"><b>100%</b><span>basado en reglas &mdash; cero emociones</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">C&Oacute;MO FUNCIONA</div>
            <div class="sec-head">
                <h2>Tres pasos. Luego el motor toma el control.</h2>
                <p>Sin grupos de se&ntilde;ales, sin horas de pantalla, sin decisiones discrecionales. Una vez configurado, cada entrada y salida es sistem&aacute;tica.</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>Asegura Tu Nivel</h3>
                    <p>Reserva el nivel que mejor te encaje. El precio fundador queda fijado permanentemente en tu cuenta &mdash; no volver&aacute; a ofrecerse despu&eacute;s del lanzamiento.</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>Conecta y Configura</h3>
                    <p>En el lanzamiento, vincula el motor a tu cuenta de exchange y define tus par&aacute;metros de riesgo una sola vez. Tus fondos permanecen en tu propia cuenta en todo momento.</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>El Motor Ejecuta</h3>
                    <p>El n&uacute;cleo Z-score monitorea la desviaci&oacute;n estad&iacute;stica las 24 horas y ejecuta entradas, salidas y tama&ntilde;o de posici&oacute;n autom&aacute;ticamente.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">LA ESTRATEGIA</div>
                    <h2>&iquest;Por qu&eacute; reversi&oacute;n a la media Z-score?</h2>
                    <p>Los mercados sobrerreaccionan. Los precios se alejan de su promedio estad&iacute;stico, y los precios estirados tienden a volver. Un Z-score mide exactamente cu&aacute;nto se ha estirado un precio &mdash; en desviaciones est&aacute;ndar &mdash; convirtiendo &laquo;esto parece sobreextendido&raquo; en un n&uacute;mero preciso y verificable.</p>
                    <ul class="checklist">
                        <li>Opera una ventaja estad&iacute;stica definida &mdash; no indicadores, corazonadas ni hype</li>
                        <li>Cada posici&oacute;n entra y sale por regla, con el riesgo dimensionado antes de colocar la operaci&oacute;n</li>
                        <li>La misma clase de metodolog&iacute;a usada en mesas institucionales de stat-arb durante d&eacute;cadas</li>
                        <li>Sin emociones por construcci&oacute;n: el motor no puede vengarse del mercado, sentir FOMO ni dudar</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">&laquo;Cuando el precio se desv&iacute;a m&aacute;s de &plusmn;2 desviaciones est&aacute;ndar de su media m&oacute;vil, el motor arma una posici&oacute;n de reversi&oacute;n &mdash; y la gestiona hasta el final sin intervenci&oacute;n humana.&raquo;</div>
                    <div class="src">&mdash; La regla central de ai PassiveAutotrades, explicada claramente. Sin caja negra, sin se&ntilde;ales misteriosas.</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">QU&Eacute; OBTIENES</div>
            <div class="sec-head">
                <h2>Dise&ntilde;ado como una mesa de trading. Entregado como un producto.</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>N&uacute;cleo de Se&ntilde;ales Z-Score</h3><p>La desviaci&oacute;n estad&iacute;stica de ventana m&oacute;vil impulsa cada se&ntilde;al &mdash; transparente, verificable y consistente.</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>Ejecuci&oacute;n en Milisegundos</h3><p>Las se&ntilde;ales se disparan algor&iacute;tmicamente en cuanto se cruzan los umbrales &mdash; d&iacute;a, noche y fines de semana.</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>L&iacute;mites de Riesgo Estrictos</h3><p>Tama&ntilde;o por operaci&oacute;n, topes de exposici&oacute;n y salidas autom&aacute;ticas aplicados en cada posici&oacute;n.</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>Tus Fondos, Tu Cuenta</h3><p>El motor se conecta a tu propia cuenta de exchange. El capital nunca se nos transfiere.</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>Configuraci&oacute;n &Uacute;nica</h3><p>Elige nivel de riesgo y mercados una sola vez. Sin mantenimiento continuo ni vigilancia.</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>Acceso API <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>Acceso program&aacute;tico completo al motor para integraciones y monitoreo personalizados.</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">RESERVA FUNDADORA</div>
                <h2>Asegura tu nivel antes del lanzamiento</h2>
                <p>Cada nivel es una reserva a precio fundador. Al lanzarse el motor, los miembros fundadores entran primero &mdash; y estos precios se retiran permanentemente.</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">RESERVA</span>
                    <h3>Prototype</h3>
                    <div class="who">Para quienes empiezan en algo-trading</div>
                    <div class="price">$79.99</div>
                    <div class="per">pago &uacute;nico (USD)</div>
                    <ul>
                        <li>Acceso inicial al motor prototipo</li>
                        <li>Estrategia Z-score b&aacute;sica, un mercado</li>
                        <li>Controles de riesgo est&aacute;ndar</li>
                        <li>Soporte por email</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Obtener Prototype</a>
                </div>
                <div class="tier">
                    <span class="badge">RESERVA</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">Para creyentes a largo plazo</div>
                    <div class="price">$199.99</div>
                    <div class="per">pago &uacute;nico &middot; de por vida (USD)</div>
                    <ul>
                        <li>Acceso completo de por vida</li>
                        <li>Todos los mercados y actualizaciones, para siempre</li>
                        <li>Sin cuotas recurrentes, nunca</li>
                        <li>Incorporaci&oacute;n prioritaria en el lanzamiento</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">Reservar De Por Vida</a>
                </div>
                <div class="tier">
                    <span class="badge">RESERVA</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">Para quienes prefieren flexibilidad</div>
                    <div class="price">$49.99</div>
                    <div class="per">al mes (USD)</div>
                    <ul>
                        <li>Utilidad completa del motor</li>
                        <li>Todos los mercados incluidos</li>
                        <li>Cancela cuando quieras</li>
                        <li>Soporte est&aacute;ndar</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">Reservar Mensual</a>
                </div>
                <div class="tier featured">
                    <span class="flag">MEJOR VALOR</span>
                    <span class="badge">RESERVA</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">Para operadores serios</div>
                    <div class="price">$499.99</div>
                    <div class="per">al a&ntilde;o (USD)</div>
                    <ul>
                        <li>Todo lo de Early Access</li>
                        <li>Cola de ejecuci&oacute;n prioritaria</li>
                        <li>Acceso API completo</li>
                        <li>Canal de soporte prioritario</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">Reservar Anual</a>
                </div>
            </div>
            <p class="pricing-note">Pago seguro v&iacute;a Stripe &middot; Paga en USD, EUR, GBP, CAD o AUD &mdash; tu moneda se detecta autom&aacute;ticamente al pagar &middot; Los precios fundadores se retiran permanentemente en el lanzamiento p&uacute;blico</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">PREGUNTAS</div>
                <h2>Lo que se pregunta antes de comprar</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>&iquest;Qu&eacute; estoy comprando exactamente con una reserva?</summary>
                    <div class="a">Est&aacute;s reservando acceso al motor a precio fundador antes del lanzamiento p&uacute;blico. Tu nivel y precio quedan fijados permanentemente en tu cuenta. Los miembros fundadores se incorporan primero cuando el motor entre en funcionamiento, y las novedades del lanzamiento se env&iacute;an al email que uses al pagar.</div>
                </details>
                <details>
                    <summary>&iquest;Mis fondos salen alguna vez de mi control?</summary>
                    <div class="a">No. El motor se conecta a tu propia cuenta de exchange mediante claves API que t&uacute; controlas y puedes revocar en cualquier momento. Nunca custodiamos tu capital, y jam&aacute;s se requieren permisos de retiro.</div>
                </details>
                <details>
                    <summary>&iquest;Necesito experiencia en trading?</summary>
                    <div class="a">No se requiere saber leer gr&aacute;ficos ni experiencia operando &mdash; la configuraci&oacute;n se hace una sola vez. Eso s&iacute;, debes entender que todo trading conlleva riesgo real de p&eacute;rdida antes de comprometer capital.</div>
                </details>
                <details>
                    <summary>&iquest;Puede el motor perder dinero?</summary>
                    <div class="a">S&iacute;. Cualquier respuesta honesta a esta pregunta es s&iacute; &mdash; ninguna estrategia gana todas las operaciones, y la reversi&oacute;n a la media conlleva riesgo en mercados con tendencias fuertes. Precisamente por eso el motor aplica tama&ntilde;o de posici&oacute;n y l&iacute;mites de exposici&oacute;n en cada operaci&oacute;n. Nunca operes con capital que no puedas permitirte perder.</div>
                </details>
                <details>
                    <summary>&iquest;Cu&aacute;l es la diferencia entre los niveles?</summary>
                    <div class="a">Prototype es acceso inicial de un solo mercado al motor prototipo. Founding Alpha es acceso completo de por vida sin cuotas recurrentes. Early Access es el mismo motor completo facturado mensualmente con cancelaci&oacute;n libre. VIP Annual a&ntilde;ade ejecuci&oacute;n prioritaria, acceso API completo y soporte prioritario.</div>
                </details>
                <details>
                    <summary>&iquest;Qu&eacute; pasa despu&eacute;s de reservar?</summary>
                    <div class="a">Recibir&aacute;s tu confirmaci&oacute;n de pedido de inmediato, seguida de novedades sobre el calendario de lanzamiento e instrucciones de incorporaci&oacute;n por email. Los miembros fundadores entran antes de la disponibilidad p&uacute;blica.</div>
                </details>
                <details>
                    <summary>&iquest;Puedo pedir un reembolso?</summary>
                    <div class="a">S&iacute; &mdash; las reservas son totalmente reembolsables en cualquier momento antes del lanzamiento. Contacta con soporte (los datos est&aacute;n en tu recibo de compra) y se procesar&aacute; el reembolso. Tras el lanzamiento, los pases mensual y anual pueden cancelarse en cualquier momento para detener la facturaci&oacute;n futura. Detalles completos en nuestros <a href="/terms" style="color:var(--accent)">T&eacute;rminos de Servicio</a> (en ingl&eacute;s).</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>El precio fundador termina en el lanzamiento.</h2>
            <p>Reserva tu nivel ahora &mdash; cuando el motor sea p&uacute;blico, estos precios se retiran permanentemente.</p>
            <a href="#pricing" class="btn primary">Reservar Mi Nivel</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">C&oacute;mo Funciona</a>
                    <a href="#strategy">Estrategia</a>
                    <a href="#pricing">Precios</a>
                    <a href="#faq">Preguntas</a>
                    <a href="/terms">T&eacute;rminos</a>
                    <a href="/privacy">Privacidad</a>
                </div>
            </div>
            <p class="disclaimer">Aviso de riesgo: El trading conlleva un riesgo sustancial de p&eacute;rdida y no es adecuado para todos los inversores. Las estrategias algor&iacute;tmicas y automatizadas pueden perder dinero y lo hacen; el rendimiento pasado o simulado no garantiza resultados futuros. ai PassiveAutotrades es una herramienta de software &mdash; no es un asesor de inversiones, broker-dealer ni fiduciario, y nada en este sitio constituye asesoramiento financiero ni una solicitud para operar. Las compras de reserva otorgan acceso al software en el lanzamiento seg&uacute;n lo descrito. Opera solo con capital que puedas permitirte perder.</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>
"""

HOMEPAGE_HTML_FR = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — Moteur de Trading Quantitatif Z-Score Automatisé</title>
    <meta name="description" content="Moteur de trading automatisé basé sur le retour à la moyenne Z-score. Exécution sans intervention, contrôles de risque intégrés et vos fonds ne quittent jamais votre propre compte. Précommandez votre accès fondateur.">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/fr">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/fr">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — Des Revenus Institutionnels, Automatisés.">
    <meta property="og:description" content="Stratégies quantitatives Z-score automatisées sans surveiller les graphiques. Précommandez votre accès fondateur avant le lancement.">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="fr_FR">
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
""" + HOMEPAGE_STYLE + """
</head>
<body>
    <nav>
        <div class="nav-inner">
            <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
            <div class="nav-links">
                <a href="#how">Fonctionnement</a>
                <a href="#strategy">Strat&eacute;gie</a>
                <a href="#pricing">Tarifs</a>
                <a href="#faq">FAQ</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><span class="cur">FR</span></div>
            <a href="#pricing" class="nav-cta">Pr&eacute;commander</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>MOTEUR QUANTITATIF Z-SCORE AUTOMATIS&Eacute;</div>
                    <h1>Des Revenus Institutionnels,<br><span class="grad">Automatis&eacute;s.</span></h1>
                    <p class="hero-sub">Un moteur de trading enti&egrave;rement automatis&eacute; fond&eacute; sur le retour &agrave; la moyenne Z-score &mdash; la m&ecirc;me m&eacute;thodologie statistique que les desks quantitatifs &mdash; ex&eacute;cutant 24h/24 pour que vous ne regardiez plus jamais un graphique.</p>
                    <div class="hero-note">Pr&eacute;commande fondatrice &mdash; verrouillez le tarif &agrave; vie avant le lancement public</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">Voir les Offres</a>
                        <a href="#how" class="btn ghost">Comment &ccedil;a Marche</a>
                    </div>
                    <div class="hero-foot">
                        <span>Ex&eacute;cution sans intervention</span>
                        <span>Contr&ocirc;les de risque int&eacute;gr&eacute;s</span>
                        <span>R&eacute;siliation possible &agrave; tout moment</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">MOTEUR &mdash; MONITEUR DE SIGNAUX</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC&ndash;USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT &middot; ARMED</span></div>
                            <div class="crow"><span class="pair">ETH&ndash;USD</span><span class="z">z&nbsp;=&nbsp;&minus;0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL&ndash;USD</span><span class="z">z&nbsp;=&nbsp;&minus;2.87</span><span class="sig armed">REVERT &middot; ARMED</span></div>
                            <div class="crow"><span class="pair">XRP&ndash;USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risque &#10003; &nbsp; taille &#10003; &nbsp; limites d'exposition &#10003;</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">Flux de signaux illustratif &mdash; comment le moteur lit le march&eacute;</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>couverture autonome du march&eacute;</span></div>
            <div class="stat"><b>ms</b><span>vitesse d'ex&eacute;cution algorithmique</span></div>
            <div class="stat"><b>0</b><span>graphique &agrave; surveiller</span></div>
            <div class="stat"><b>100%</b><span>bas&eacute; sur des r&egrave;gles &mdash; z&eacute;ro &eacute;motion</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">FONCTIONNEMENT</div>
            <div class="sec-head">
                <h2>Trois &eacute;tapes. Puis le moteur prend le relais.</h2>
                <p>Pas de groupes de signaux, pas d'heures d'&eacute;cran, pas de d&eacute;cisions discr&eacute;tionnaires. Une fois configur&eacute;, chaque entr&eacute;e et sortie est syst&eacute;matique.</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>R&eacute;servez Votre Offre</h3>
                    <p>Pr&eacute;commandez l'offre qui vous convient. Le tarif fondateur est verrouill&eacute; d&eacute;finitivement sur votre compte &mdash; il ne sera plus jamais propos&eacute; apr&egrave;s le lancement.</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>Connectez et Configurez</h3>
                    <p>Au lancement, reliez le moteur &agrave; votre compte d'exchange et d&eacute;finissez vos param&egrave;tres de risque une seule fois. Vos fonds restent sur votre propre compte en permanence.</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>Le Moteur Ex&eacute;cute</h3>
                    <p>Le c&oelig;ur Z-score surveille la d&eacute;viation statistique 24h/24 et ex&eacute;cute entr&eacute;es, sorties et dimensionnement des positions automatiquement.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">LA STRAT&Eacute;GIE</div>
                    <h2>Pourquoi le retour &agrave; la moyenne Z-score&nbsp;?</h2>
                    <p>Les march&eacute;s surr&eacute;agissent. Les prix s'&eacute;loignent de leur moyenne statistique, et les prix &eacute;tir&eacute;s tendent &agrave; y revenir. Un Z-score mesure pr&eacute;cis&eacute;ment cet &eacute;tirement &mdash; en &eacute;carts-types &mdash; transformant &laquo;&nbsp;&ccedil;a semble surtendu&nbsp;&raquo; en un nombre pr&eacute;cis et v&eacute;rifiable.</p>
                    <ul class="checklist">
                        <li>Exploite un avantage statistique d&eacute;fini &mdash; pas d'indicateurs, d'intuitions ni de hype</li>
                        <li>Chaque position entre et sort selon une r&egrave;gle, le risque dimensionn&eacute; avant la prise de position</li>
                        <li>La m&ecirc;me classe de m&eacute;thodologie utilis&eacute;e par les desks institutionnels de stat-arb depuis des d&eacute;cennies</li>
                        <li>Sans &eacute;motion par construction&nbsp;: le moteur ne conna&icirc;t ni revanche, ni FOMO, ni h&eacute;sitation</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">&laquo;&nbsp;Quand le prix d&eacute;vie au-del&agrave; de &plusmn;2 &eacute;carts-types de sa moyenne glissante, le moteur arme une position de retour &agrave; la moyenne &mdash; et la g&egrave;re jusqu'au bout sans intervention humaine.&nbsp;&raquo;</div>
                    <div class="src">&mdash; La r&egrave;gle centrale d'ai PassiveAutotrades, &eacute;nonc&eacute;e clairement. Pas de bo&icirc;te noire, pas de signaux myst&egrave;res.</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">CE QUE VOUS OBTENEZ</div>
            <div class="sec-head">
                <h2>Con&ccedil;u comme un desk. Livr&eacute; comme un produit.</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>C&oelig;ur de Signaux Z-Score</h3><p>La d&eacute;viation statistique sur fen&ecirc;tre glissante pilote chaque signal &mdash; transparent, v&eacute;rifiable et constant.</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>Ex&eacute;cution en Millisecondes</h3><p>Les signaux se d&eacute;clenchent alg&eacute;briquement d&egrave;s le franchissement des seuils &mdash; jour, nuit et week-end.</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>Limites de Risque Strictes</h3><p>Dimensionnement par trade, plafonds d'exposition et sorties automatiques appliqu&eacute;s sur chaque position.</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>Vos Fonds, Votre Compte</h3><p>Le moteur se connecte &agrave; votre propre compte d'exchange. Le capital ne nous est jamais transf&eacute;r&eacute;.</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>Configuration Unique</h3><p>Choisissez le niveau de risque et les march&eacute;s une seule fois. Aucune maintenance ni surveillance continue.</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>Acc&egrave;s API <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>Acc&egrave;s programmatique complet au moteur pour int&eacute;grations et monitoring sur mesure.</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">PR&Eacute;COMMANDE FONDATRICE</div>
                <h2>Verrouillez votre offre avant le lancement</h2>
                <p>Chaque offre est une pr&eacute;commande au tarif fondateur. Au lancement du moteur, les membres fondateurs sont int&eacute;gr&eacute;s en premier &mdash; et ces tarifs sont d&eacute;finitivement retir&eacute;s.</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">PR&Eacute;COMMANDE</span>
                    <h3>Prototype</h3>
                    <div class="who">Pour d&eacute;buter en algo-trading</div>
                    <div class="price">$79.99</div>
                    <div class="per">paiement unique (USD)</div>
                    <ul>
                        <li>Acc&egrave;s d'entr&eacute;e au moteur prototype</li>
                        <li>Strat&eacute;gie Z-score de base, un march&eacute;</li>
                        <li>Contr&ocirc;les de risque standard</li>
                        <li>Support par email</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Obtenir Prototype</a>
                </div>
                <div class="tier">
                    <span class="badge">PR&Eacute;COMMANDE</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">Pour les convaincus de long terme</div>
                    <div class="price">$199.99</div>
                    <div class="per">paiement unique &middot; &agrave; vie (USD)</div>
                    <ul>
                        <li>Acc&egrave;s complet &agrave; vie au moteur</li>
                        <li>Tous les march&eacute;s et mises &agrave; jour, pour toujours</li>
                        <li>Aucun frais r&eacute;current, jamais</li>
                        <li>Int&eacute;gration prioritaire au lancement</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">R&eacute;server &Agrave; Vie</a>
                </div>
                <div class="tier">
                    <span class="badge">PR&Eacute;COMMANDE</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">Pour d&eacute;marrer en souplesse</div>
                    <div class="price">$49.99</div>
                    <div class="per">par mois (USD)</div>
                    <ul>
                        <li>Utilit&eacute; compl&egrave;te du moteur</li>
                        <li>Tous les march&eacute;s inclus</li>
                        <li>R&eacute;siliable &agrave; tout moment</li>
                        <li>Support standard</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">R&eacute;server Mensuel</a>
                </div>
                <div class="tier featured">
                    <span class="flag">MEILLEURE OFFRE</span>
                    <span class="badge">PR&Eacute;COMMANDE</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">Pour les op&eacute;rateurs s&eacute;rieux</div>
                    <div class="price">$499.99</div>
                    <div class="per">par an (USD)</div>
                    <ul>
                        <li>Tout Early Access inclus</li>
                        <li>File d'ex&eacute;cution prioritaire</li>
                        <li>Acc&egrave;s API complet</li>
                        <li>Canal de support prioritaire</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">R&eacute;server Annuel</a>
                </div>
            </div>
            <p class="pricing-note">Paiement s&eacute;curis&eacute; via Stripe &middot; Payez en USD, EUR, GBP, CAD ou AUD &mdash; votre devise est d&eacute;tect&eacute;e automatiquement au paiement &middot; Les tarifs fondateurs sont d&eacute;finitivement retir&eacute;s au lancement public</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">QUESTIONS</div>
                <h2>Ce qu'on demande avant d'acheter</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>Qu'est-ce que j'ach&egrave;te exactement avec une pr&eacute;commande&nbsp;?</summary>
                    <div class="a">Vous r&eacute;servez l'acc&egrave;s au moteur au tarif fondateur avant le lancement public. Votre offre et votre tarif sont verrouill&eacute;s d&eacute;finitivement sur votre compte. Les membres fondateurs sont int&eacute;gr&eacute;s en premier au lancement, et les nouvelles du lancement sont envoy&eacute;es &agrave; l'email utilis&eacute; au paiement.</div>
                </details>
                <details>
                    <summary>Mes fonds quittent-ils un jour mon contr&ocirc;le&nbsp;?</summary>
                    <div class="a">Non. Le moteur se connecte &agrave; votre propre compte d'exchange via des cl&eacute;s API que vous contr&ocirc;lez et pouvez r&eacute;voquer &agrave; tout moment. Nous ne d&eacute;tenons jamais votre capital, et les permissions de retrait ne sont jamais requises.</div>
                </details>
                <details>
                    <summary>Faut-il de l'exp&eacute;rience en trading&nbsp;?</summary>
                    <div class="a">Aucune lecture de graphiques ni comp&eacute;tence de trading n'est requise pour utiliser le moteur &mdash; la configuration se fait une seule fois. Vous devez toutefois comprendre que tout trading comporte un risque r&eacute;el de perte avant d'engager du capital.</div>
                </details>
                <details>
                    <summary>Le moteur peut-il perdre de l'argent&nbsp;?</summary>
                    <div class="a">Oui. Toute r&eacute;ponse honn&ecirc;te &agrave; cette question est oui &mdash; aucune strat&eacute;gie ne gagne &agrave; chaque trade, et le retour &agrave; la moyenne comporte un risque dans les march&eacute;s fortement directionnels. C'est pr&eacute;cis&eacute;ment pourquoi le moteur impose dimensionnement et limites d'exposition sur chaque trade. Ne tradez jamais un capital que vous ne pouvez pas vous permettre de perdre.</div>
                </details>
                <details>
                    <summary>Quelle diff&eacute;rence entre les offres&nbsp;?</summary>
                    <div class="a">Prototype est un acc&egrave;s d'entr&eacute;e mono-march&eacute; au moteur prototype. Founding Alpha est l'acc&egrave;s complet &agrave; vie sans frais r&eacute;currents. Early Access est le m&ecirc;me moteur complet factur&eacute; mensuellement, r&eacute;siliable &agrave; tout moment. VIP Annual ajoute l'ex&eacute;cution prioritaire, l'acc&egrave;s API complet et le support prioritaire.</div>
                </details>
                <details>
                    <summary>Que se passe-t-il apr&egrave;s ma pr&eacute;commande&nbsp;?</summary>
                    <div class="a">Vous recevez imm&eacute;diatement votre confirmation de commande, puis les nouvelles du calendrier de lancement et les instructions d'int&eacute;gration par email. Les membres fondateurs sont int&eacute;gr&eacute;s avant la disponibilit&eacute; publique.</div>
                </details>
                <details>
                    <summary>Puis-je &ecirc;tre rembours&eacute;&nbsp;?</summary>
                    <div class="a">Oui &mdash; les pr&eacute;commandes sont int&eacute;gralement remboursables &agrave; tout moment avant le lancement. Contactez le support (coordonn&eacute;es sur votre re&ccedil;u d'achat) et le remboursement sera trait&eacute;. Apr&egrave;s le lancement, les pass mensuel et annuel sont r&eacute;siliables &agrave; tout moment pour stopper la facturation future. D&eacute;tails complets dans nos <a href="/terms" style="color:var(--accent)">Conditions d'Utilisation</a> (en anglais).</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>Le tarif fondateur prend fin au lancement.</h2>
            <p>R&eacute;servez votre offre maintenant &mdash; quand le moteur sera public, ces tarifs seront d&eacute;finitivement retir&eacute;s.</p>
            <a href="#pricing" class="btn primary">Pr&eacute;commander Mon Offre</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">Fonctionnement</a>
                    <a href="#strategy">Strat&eacute;gie</a>
                    <a href="#pricing">Tarifs</a>
                    <a href="#faq">FAQ</a>
                    <a href="/terms">Conditions</a>
                    <a href="/privacy">Confidentialit&eacute;</a>
                </div>
            </div>
            <p class="disclaimer">Avertissement sur les risques&nbsp;: Le trading comporte un risque substantiel de perte et ne convient pas &agrave; tous les investisseurs. Les strat&eacute;gies algorithmiques et automatis&eacute;es peuvent perdre de l'argent et en perdent&nbsp;; les performances pass&eacute;es ou simul&eacute;es ne garantissent pas les r&eacute;sultats futurs. ai PassiveAutotrades est un outil logiciel &mdash; ce n'est ni un conseiller en investissement, ni un courtier, ni un fiduciaire, et rien sur ce site ne constitue un conseil financier ou une sollicitation &agrave; trader. Les pr&eacute;commandes donnent acc&egrave;s au logiciel au lancement comme d&eacute;crit ci-dessus. Ne tradez qu'avec un capital que vous pouvez vous permettre de perdre.</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. Tous droits r&eacute;serv&eacute;s.</p>
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
    <loc>https://aipassiveautotrades.vercel.app/es</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/fr</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
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

NOT_FOUND_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page not found | ai PassiveAutotrades</title>
    <meta name="robots" content="noindex">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
""" + LEGAL_STYLE + """
</head>
<body>
    <div class="page" style="text-align:center; padding-top:120px;">
        <h1>404 &mdash; page not found</h1>
        <p style="margin: 16px 0 32px;">That page doesn't exist. The engine, however, does.</p>
        <a href="/" style="display:inline-block; background:#4f8ff7; color:#04070d; padding:14px 28px; border-radius:9px; font-weight:700;">Back to ai PassiveAutotrades</a>
    </div>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def read_root():
    # s-maxage lets Vercel's global CDN serve the page without invoking this
    # function; the edge cache is purged automatically on every deploy, and
    # stale-while-revalidate keeps responses instant while refreshing.
    return HTMLResponse(content=HOMEPAGE_HTML, headers=CACHE_HEADERS)


@app.get("/es", response_class=HTMLResponse)
def read_root_es():
    return HTMLResponse(content=HOMEPAGE_HTML_ES, headers=CACHE_HEADERS)


@app.get("/fr", response_class=HTMLResponse)
def read_root_fr():
    return HTMLResponse(content=HOMEPAGE_HTML_FR, headers=CACHE_HEADERS)


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


@app.exception_handler(404)
async def not_found(request, exc):
    return HTMLResponse(content=NOT_FOUND_HTML, status_code=404)

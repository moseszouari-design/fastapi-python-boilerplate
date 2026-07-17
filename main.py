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
    <link rel="alternate" hreflang="de" href="https://aipassiveautotrades.vercel.app/de">
    <link rel="alternate" hreflang="pt" href="https://aipassiveautotrades.vercel.app/pt">
    <link rel="alternate" hreflang="ar" href="https://aipassiveautotrades.vercel.app/ar">
    <link rel="alternate" hreflang="fa" href="https://aipassiveautotrades.vercel.app/fa">
    <link rel="alternate" hreflang="ur" href="https://aipassiveautotrades.vercel.app/ur">
    <link rel="alternate" hreflang="hi" href="https://aipassiveautotrades.vercel.app/hi">
    <link rel="alternate" hreflang="bn" href="https://aipassiveautotrades.vercel.app/bn">
    <link rel="alternate" hreflang="ta" href="https://aipassiveautotrades.vercel.app/ta">
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
        @media (max-width: 760px) {
            .nav-inner { flex-wrap: wrap; height: auto; padding-top: 10px; padding-bottom: 10px; row-gap: 6px; }
            .lang { order: 3; width: 100%; margin-left: 0; margin-right: 0; }
        }
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
            <div class="lang"><span class="cur">EN</span><a href="/es">ES</a><a href="/fr">FR</a><a href="/de">DE</a><a href="/pt">PT</a><a href="/ar">AR</a><a href="/fa">FA</a><a href="/ur">UR</a><a href="/hi">HI</a><a href="/bn">BN</a><a href="/ta">TA</a></div>
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
    <link rel="alternate" hreflang="de" href="https://aipassiveautotrades.vercel.app/de">
    <link rel="alternate" hreflang="pt" href="https://aipassiveautotrades.vercel.app/pt">
    <link rel="alternate" hreflang="ar" href="https://aipassiveautotrades.vercel.app/ar">
    <link rel="alternate" hreflang="fa" href="https://aipassiveautotrades.vercel.app/fa">
    <link rel="alternate" hreflang="ur" href="https://aipassiveautotrades.vercel.app/ur">
    <link rel="alternate" hreflang="hi" href="https://aipassiveautotrades.vercel.app/hi">
    <link rel="alternate" hreflang="bn" href="https://aipassiveautotrades.vercel.app/bn">
    <link rel="alternate" hreflang="ta" href="https://aipassiveautotrades.vercel.app/ta">
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
            <div class="lang"><a href="/">EN</a><span class="cur">ES</span><a href="/fr">FR</a><a href="/de">DE</a><a href="/pt">PT</a><a href="/ar">AR</a><a href="/fa">FA</a><a href="/ur">UR</a><a href="/hi">HI</a><a href="/bn">BN</a><a href="/ta">TA</a></div>
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
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><span class="cur">FR</span><a href="/de">DE</a><a href="/pt">PT</a><a href="/ar">AR</a><a href="/fa">FA</a><a href="/ur">UR</a><a href="/hi">HI</a><a href="/bn">BN</a><a href="/ta">TA</a></div>
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

HOMEPAGE_HTML_DE = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — Automatisierte Z-Score Quant-Trading-Engine</title>
    <meta name="description" content="Vollautomatisierte Trading-Engine auf Basis von Z-Score Mean Reversion. Ausführung ohne Ihr Zutun, integrierte Risikokontrollen, Ihre Gelder verlassen nie Ihr eigenes Konto. Jetzt Gründerzugang vorbestellen.">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/de">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/de">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — Institutionelle Erträge, Automatisiert.">
    <meta property="og:description" content="Automatisierte Z-Score-Quant-Strategien ohne Chart-Beobachtung. Gründerzugang vor dem Launch vorbestellen.">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="de_DE">
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
                <a href="#how">So funktioniert's</a>
                <a href="#strategy">Strategie</a>
                <a href="#pricing">Preise</a>
                <a href="#faq">FAQ</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><a href="/fr">FR</a><span class="cur">DE</span><a href="/pt">PT</a><a href="/ar">AR</a><a href="/fa">FA</a><a href="/ur">UR</a><a href="/hi">HI</a><a href="/bn">BN</a><a href="/ta">TA</a></div>
            <a href="#pricing" class="nav-cta">Zugang vorbestellen</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>AUTOMATISIERTE Z-SCORE QUANT-ENGINE</div>
                    <h1>Institutionelle Erträge,<br><span class="grad">Automatisiert.</span></h1>
                    <p class="hero-sub">Eine vollautomatisierte Trading-Engine auf Basis von Z-Score Mean Reversion — derselben statistischen Methodik, die Quant-Desks einsetzen — rund um die Uhr aktiv, damit Sie nie wieder auf Charts starren.</p>
                    <div class="hero-note">Gründer-Vorbestellung — sichern Sie sich den Lifetime-Preis vor dem öffentlichen Launch</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">Vorbestell-Stufen ansehen</a>
                        <a href="#how" class="btn ghost">So funktioniert's</a>
                    </div>
                    <div class="hero-foot">
                        <span>Ausführung ohne Ihr Zutun</span>
                        <span>Integrierte Risikokontrollen</span>
                        <span>Jederzeit kündbar</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">ENGINE — SIGNAL-MONITOR</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC–USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">ETH–USD</span><span class="z">z&nbsp;=&nbsp;−0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL–USD</span><span class="z">z&nbsp;=&nbsp;−2.87</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">XRP–USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>Risiko ✓ &nbsp; Positionsgröße ✓ &nbsp; Exposure-Limits ✓</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">Illustrativer Signal-Feed — so liest die Engine den Markt</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>autonome Marktabdeckung</span></div>
            <div class="stat"><b>ms</b><span>algorithmische Ausführungsgeschwindigkeit</span></div>
            <div class="stat"><b>0</b><span>Charts, die Sie beobachten müssen</span></div>
            <div class="stat"><b>100%</b><span>regelbasiert — null Emotionen</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">SO FUNKTIONIERT'S</div>
            <div class="sec-head">
                <h2>Drei Schritte. Dann übernimmt die Engine.</h2>
                <p>Keine Signal-Gruppen, keine Bildschirmzeit, keine Bauchentscheidungen. Einmal konfiguriert, erfolgt jeder Ein- und Ausstieg systematisch.</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>Stufe sichern</h3>
                    <p>Bestellen Sie die passende Stufe vor. Der Gründerpreis wird dauerhaft an Ihr Konto gebunden — nach dem Launch wird er nie wieder angeboten.</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>Verbinden &amp; konfigurieren</h3>
                    <p>Zum Launch verbinden Sie die Engine mit Ihrem Exchange-Konto und legen Ihre Risikoparameter einmalig fest. Ihre Gelder bleiben jederzeit auf Ihrem eigenen Konto.</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>Die Engine führt aus</h3>
                    <p>Der Z-Score-Kern überwacht die statistische Abweichung rund um die Uhr und führt Einstiege, Ausstiege und Positionsgrößen automatisch aus.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">DIE STRATEGIE</div>
                    <h2>Warum Z-Score Mean Reversion?</h2>
                    <p>Märkte überreagieren. Preise entfernen sich von ihrem statistischen Mittel — und gedehnte Preise neigen dazu, zurückzuschnappen. Ein Z-Score misst exakt, wie gedehnt ein Preis ist — in Standardabweichungen — und macht aus „das wirkt überzogen" eine präzise, überprüfbare Zahl.</p>
                    <ul class="checklist">
                        <li>Handelt einen definierten statistischen Vorteil — keine Indikatoren, Bauchgefühle oder Hype</li>
                        <li>Jede Position wird nach Regeln eröffnet und geschlossen, das Risiko vor dem Trade bemessen</li>
                        <li>Dieselbe Methodenklasse, die institutionelle Stat-Arb-Desks seit Jahrzehnten nutzen</li>
                        <li>Emotionslos per Konstruktion: Die Engine kennt weder Rache-Trades noch FOMO noch Zögern</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">„Weicht der Preis mehr als ±2 Standardabweichungen von seinem gleitenden Mittel ab, armiert die Engine eine Reversionsposition — und managt sie bis zum Abschluss ohne menschliches Zutun."</div>
                    <div class="src">— Die Kernregel von ai PassiveAutotrades, klar formuliert. Keine Blackbox, keine Mysterien-Signale.</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">WAS SIE BEKOMMEN</div>
            <div class="sec-head">
                <h2>Konstruiert wie ein Trading-Desk. Geliefert wie ein Produkt.</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>Z-Score-Signalkern</h3><p>Statistische Abweichung im gleitenden Fenster treibt jedes Signal — transparent, überprüfbar, konsistent.</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>Ausführung in Millisekunden</h3><p>Signale werden algorithmisch ausgelöst, sobald Schwellen überschritten werden — Tag, Nacht, Wochenende.</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>Harte Risikolimits</h3><p>Positionsgröße, Exposure-Obergrenzen und automatische Ausstiege werden bei jeder Position durchgesetzt.</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>Ihre Gelder, Ihr Konto</h3><p>Die Engine verbindet sich mit Ihrem eigenen Exchange-Konto. Kapital wird nie an uns übertragen.</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>Einmalige Konfiguration</h3><p>Risikoniveau und Märkte ein einziges Mal wählen. Keine laufende Wartung, kein Babysitten.</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>API-Zugang <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>Voller programmatischer Zugriff auf die Engine für eigene Integrationen und Monitoring.</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">GRÜNDER-VORBESTELLUNG</div>
                <h2>Sichern Sie Ihre Stufe vor dem Launch</h2>
                <p>Jede Stufe ist eine Vorbestellung zum Gründerpreis. Beim Launch werden Gründungsmitglieder zuerst aufgenommen — und diese Preise dauerhaft eingestellt.</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">VORBESTELLUNG</span>
                    <h3>Prototype</h3>
                    <div class="who">Für Algo-Einsteiger</div>
                    <div class="price">$79.99</div>
                    <div class="per">einmalig (USD)</div>
                    <ul>
                        <li>Einstiegszugang zur Prototyp-Engine</li>
                        <li>Z-Score-Kernstrategie, ein Markt</li>
                        <li>Standard-Risikokontrollen</li>
                        <li>E-Mail-Support</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Prototype sichern</a>
                </div>
                <div class="tier">
                    <span class="badge">VORBESTELLUNG</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">Für langfristig Überzeugte</div>
                    <div class="price">$199.99</div>
                    <div class="per">einmalig · lebenslang (USD)</div>
                    <ul>
                        <li>Lebenslanger Vollzugang zur Engine</li>
                        <li>Alle Märkte &amp; Strategie-Updates, für immer</li>
                        <li>Nie wiederkehrende Gebühren</li>
                        <li>Bevorzugtes Onboarding zum Launch</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">Lifetime sichern</a>
                </div>
                <div class="tier">
                    <span class="badge">VORBESTELLUNG</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">Für flexible Starter</div>
                    <div class="price">$49.99</div>
                    <div class="per">pro Monat (USD)</div>
                    <ul>
                        <li>Voller Funktionsumfang der Engine</li>
                        <li>Alle Märkte inklusive</li>
                        <li>Jederzeit kündbar</li>
                        <li>Standard-Support</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">Monatlich sichern</a>
                </div>
                <div class="tier featured">
                    <span class="flag">BESTES ANGEBOT</span>
                    <span class="badge">VORBESTELLUNG</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">Für ernsthafte Operatoren</div>
                    <div class="price">$499.99</div>
                    <div class="per">pro Jahr (USD)</div>
                    <ul>
                        <li>Alles aus Early Access</li>
                        <li>Priorisierte Ausführungs-Queue</li>
                        <li>Voller API-Zugang</li>
                        <li>Priorisierter Support-Kanal</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">Jährlich sichern</a>
                </div>
            </div>
            <p class="pricing-note">Sichere Zahlung über Stripe · Zahlen Sie in USD, EUR, GBP, CAD oder AUD — Ihre Währung wird beim Checkout automatisch erkannt · Gründerpreise werden zum öffentlichen Launch dauerhaft eingestellt</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">FRAGEN</div>
                <h2>Was vor dem Kauf gefragt wird</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>Was genau kaufe ich mit einer Vorbestellung?</summary>
                    <div class="a">Sie reservieren den Zugang zur Engine zum Gründerpreis vor dem öffentlichen Launch. Ihre Stufe und Ihr Preis werden dauerhaft an Ihr Konto gebunden. Gründungsmitglieder werden beim Go-Live zuerst aufgenommen; Launch-Updates gehen an die beim Checkout verwendete E-Mail-Adresse.</div>
                </details>
                <details>
                    <summary>Verlassen meine Gelder jemals meine Kontrolle?</summary>
                    <div class="a">Nein. Die Engine verbindet sich über API-Schlüssel mit Ihrem eigenen Exchange-Konto — Schlüssel, die Sie kontrollieren und jederzeit widerrufen können. Wir verwahren Ihr Kapital nie, und Auszahlungsberechtigungen sind niemals erforderlich.</div>
                </details>
                <details>
                    <summary>Brauche ich Trading-Erfahrung?</summary>
                    <div class="a">Zum Betrieb der Engine sind weder Chart-Lesen noch Trading-Kenntnisse nötig — die Konfiguration erfolgt einmalig. Sie sollten jedoch verstehen, dass jedes Trading ein reales Verlustrisiko birgt, bevor Sie Kapital einsetzen.</div>
                </details>
                <details>
                    <summary>Kann die Engine Geld verlieren?</summary>
                    <div class="a">Ja. Jede ehrliche Antwort auf diese Frage lautet ja — keine Strategie gewinnt jeden Trade, und Mean Reversion birgt Risiken in stark trendenden Märkten. Genau deshalb erzwingt die Engine Positionsgrößen und Exposure-Limits bei jedem Trade. Handeln Sie nie mit Kapital, dessen Verlust Sie sich nicht leisten können.</div>
                </details>
                <details>
                    <summary>Was unterscheidet die Stufen?</summary>
                    <div class="a">Prototype ist der Einstiegszugang zur Prototyp-Engine mit einem Markt. Founding Alpha ist lebenslanger Vollzugang ohne wiederkehrende Gebühren. Early Access ist dieselbe Voll-Engine mit monatlicher Abrechnung und jederzeitiger Kündigung. VIP Annual ergänzt priorisierte Ausführung, vollen API-Zugang und priorisierten Support.</div>
                </details>
                <details>
                    <summary>Was passiert nach meiner Vorbestellung?</summary>
                    <div class="a">Sie erhalten sofort Ihre Bestellbestätigung, danach Updates zum Launch-Zeitplan und Onboarding-Anweisungen per E-Mail. Gründungsmitglieder werden vor der öffentlichen Verfügbarkeit aufgenommen.</div>
                </details>
                <details>
                    <summary>Bekomme ich eine Rückerstattung?</summary>
                    <div class="a">Ja — Vorbestellungen sind jederzeit vor dem Launch voll erstattungsfähig. Kontaktieren Sie den Support (Details auf Ihrer Kaufquittung), und die Erstattung wird bearbeitet. Nach dem Launch können Monats- und Jahrespass jederzeit gekündigt werden, um künftige Abbuchungen zu stoppen. Details in unseren <a href="/terms" style="color:var(--accent)">Nutzungsbedingungen</a> (auf Englisch).</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>Der Gründerpreis endet mit dem Launch.</h2>
            <p>Reservieren Sie Ihre Stufe jetzt — sobald die Engine öffentlich ist, werden diese Preise dauerhaft eingestellt.</p>
            <a href="#pricing" class="btn primary">Meine Stufe vorbestellen</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">So funktioniert's</a>
                    <a href="#strategy">Strategie</a>
                    <a href="#pricing">Preise</a>
                    <a href="#faq">FAQ</a>
                    <a href="/terms">AGB</a>
                    <a href="/privacy">Datenschutz</a>
                </div>
            </div>
            <p class="disclaimer">Risikohinweis: Trading birgt ein erhebliches Verlustrisiko und ist nicht für jeden Anleger geeignet. Algorithmische und automatisierte Strategien können Geld verlieren und tun es auch; vergangene oder simulierte Ergebnisse garantieren keine zukünftigen Resultate. ai PassiveAutotrades ist ein Software-Werkzeug — kein Anlageberater, Broker-Dealer oder Treuhänder, und nichts auf dieser Website stellt Finanzberatung oder eine Handelsaufforderung dar. Vorbestellungen gewähren Software-Zugang zum Launch wie oben beschrieben. Handeln Sie nur mit Kapital, dessen Verlust Sie sich leisten können.</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. Alle Rechte vorbehalten.</p>
        </div>
    </footer>
</body>
</html>
"""

HOMEPAGE_HTML_PT = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — Motor de Trading Quantitativo Z-Score Automatizado</title>
    <meta name="description" content="Motor de trading totalmente automatizado baseado em reversão à média Z-score. Execução sem intervenção, controles de risco integrados e seus fundos nunca saem da sua própria conta. Reserve seu acesso fundador.">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/pt">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/pt">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — Renda Institucional, Automatizada.">
    <meta property="og:description" content="Estratégias quantitativas Z-score automatizadas sem olhar gráficos. Reserve seu acesso fundador antes do lançamento.">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="pt_BR">
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
                <a href="#how">Como Funciona</a>
                <a href="#strategy">Estratégia</a>
                <a href="#pricing">Preços</a>
                <a href="#faq">Perguntas</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><a href="/fr">FR</a><a href="/de">DE</a><span class="cur">PT</span><a href="/ar">AR</a><a href="/fa">FA</a><a href="/ur">UR</a><a href="/hi">HI</a><a href="/bn">BN</a><a href="/ta">TA</a></div>
            <a href="#pricing" class="nav-cta">Reservar Acesso</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>MOTOR QUANTITATIVO Z-SCORE AUTOMATIZADO</div>
                    <h1>Renda Institucional,<br><span class="grad">Automatizada.</span></h1>
                    <p class="hero-sub">Um motor de trading totalmente automatizado baseado em reversão à média Z-score — a mesma metodologia estatística usada pelas mesas quantitativas — executando 24 horas por dia para você nunca mais olhar um gráfico.</p>
                    <div class="hero-note">Pré-venda fundadora — garanta o preço vitalício antes do lançamento público</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">Ver Níveis de Pré-venda</a>
                        <a href="#how" class="btn ghost">Como Funciona</a>
                    </div>
                    <div class="hero-foot">
                        <span>Execução sem intervenção</span>
                        <span>Controles de risco integrados</span>
                        <span>Cancele quando quiser</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">MOTOR — MONITOR DE SINAIS</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC–USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">ETH–USD</span><span class="z">z&nbsp;=&nbsp;−0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL–USD</span><span class="z">z&nbsp;=&nbsp;−2.87</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">XRP–USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risco ✓ &nbsp; dimensionamento ✓ &nbsp; limites de exposição ✓</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">Feed de sinais ilustrativo — como o motor lê o mercado</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>cobertura autônoma do mercado</span></div>
            <div class="stat"><b>ms</b><span>velocidade de execução algorítmica</span></div>
            <div class="stat"><b>0</b><span>gráficos para você acompanhar</span></div>
            <div class="stat"><b>100%</b><span>baseado em regras — zero emoção</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">COMO FUNCIONA</div>
            <div class="sec-head">
                <h2>Três passos. Depois o motor assume.</h2>
                <p>Sem grupos de sinais, sem horas de tela, sem decisões discricionárias. Uma vez configurado, cada entrada e saída é sistemática.</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>Garanta Seu Nível</h3>
                    <p>Reserve o nível que combina com você. O preço fundador fica travado permanentemente na sua conta — nunca mais será oferecido após o lançamento.</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>Conecte e Configure</h3>
                    <p>No lançamento, vincule o motor à sua conta de exchange e defina seus parâmetros de risco uma única vez. Seus fundos permanecem na sua própria conta o tempo todo.</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>O Motor Executa</h3>
                    <p>O núcleo Z-score monitora o desvio estatístico 24 horas por dia e executa entradas, saídas e dimensionamento de posições automaticamente.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">A ESTRATÉGIA</div>
                    <h2>Por que reversão à média Z-score?</h2>
                    <p>Os mercados exageram. Os preços se afastam da sua média estatística, e preços esticados tendem a voltar. Um Z-score mede exatamente o quanto um preço está esticado — em desvios-padrão — transformando "isso parece exagerado" em um número preciso e testável.</p>
                    <ul class="checklist">
                        <li>Opera uma vantagem estatística definida — não indicadores, palpites ou hype</li>
                        <li>Cada posição entra e sai por regra, com o risco dimensionado antes da operação</li>
                        <li>A mesma classe de metodologia usada em mesas institucionais de stat-arb há décadas</li>
                        <li>Sem emoção por construção: o motor não conhece vingança, FOMO nem hesitação</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">"Quando o preço desvia além de ±2 desvios-padrão da sua média móvel, o motor arma uma posição de reversão — e a gerencia até o fim sem intervenção humana."</div>
                    <div class="src">— A regra central do ai PassiveAutotrades, dita com clareza. Sem caixa-preta, sem sinais misteriosos.</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">O QUE VOCÊ RECEBE</div>
            <div class="sec-head">
                <h2>Projetado como uma mesa de operações. Entregue como um produto.</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>Núcleo de Sinais Z-Score</h3><p>O desvio estatístico em janela móvel comanda cada sinal — transparente, testável e consistente.</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>Execução em Milissegundos</h3><p>Os sinais disparam algoritmicamente no momento em que os limiares são cruzados — dia, noite e fins de semana.</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>Limites de Risco Rígidos</h3><p>Dimensionamento por operação, tetos de exposição e saídas automáticas aplicados em cada posição.</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>Seus Fundos, Sua Conta</h3><p>O motor se conecta à sua própria conta de exchange. O capital nunca é transferido para nós.</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>Configuração Única</h3><p>Escolha nível de risco e mercados uma única vez. Sem manutenção contínua nem vigilância.</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>Acesso API <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>Acesso programático completo ao motor para integrações e monitoramento personalizados.</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">PRÉ-VENDA FUNDADORA</div>
                <h2>Trave seu nível antes do lançamento</h2>
                <p>Cada nível é uma pré-venda a preço fundador. Quando o motor for lançado, os membros fundadores entram primeiro — e esses preços são aposentados permanentemente.</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">PRÉ-VENDA</span>
                    <h3>Prototype</h3>
                    <div class="who">Para iniciantes em algo-trading</div>
                    <div class="price">$79.99</div>
                    <div class="per">pagamento único (USD)</div>
                    <ul>
                        <li>Acesso inicial ao motor protótipo</li>
                        <li>Estratégia Z-score básica, um mercado</li>
                        <li>Controles de risco padrão</li>
                        <li>Suporte por email</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Obter Prototype</a>
                </div>
                <div class="tier">
                    <span class="badge">PRÉ-VENDA</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">Para quem acredita no longo prazo</div>
                    <div class="price">$199.99</div>
                    <div class="per">pagamento único · vitalício (USD)</div>
                    <ul>
                        <li>Acesso completo vitalício ao motor</li>
                        <li>Todos os mercados e atualizações, para sempre</li>
                        <li>Sem taxas recorrentes, nunca</li>
                        <li>Onboarding prioritário no lançamento</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">Garantir Vitalício</a>
                </div>
                <div class="tier">
                    <span class="badge">PRÉ-VENDA</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">Para quem prefere flexibilidade</div>
                    <div class="price">$49.99</div>
                    <div class="per">por mês (USD)</div>
                    <ul>
                        <li>Utilidade completa do motor</li>
                        <li>Todos os mercados incluídos</li>
                        <li>Cancele quando quiser</li>
                        <li>Suporte padrão</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">Garantir Mensal</a>
                </div>
                <div class="tier featured">
                    <span class="flag">MELHOR VALOR</span>
                    <span class="badge">PRÉ-VENDA</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">Para operadores sérios</div>
                    <div class="price">$499.99</div>
                    <div class="per">por ano (USD)</div>
                    <ul>
                        <li>Tudo do Early Access</li>
                        <li>Fila de execução prioritária</li>
                        <li>Acesso API completo</li>
                        <li>Canal de suporte prioritário</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">Garantir Anual</a>
                </div>
            </div>
            <p class="pricing-note">Pagamento seguro via Stripe · Pague em USD, EUR, GBP, CAD ou AUD — sua moeda é detectada automaticamente no checkout · Os preços fundadores são aposentados permanentemente no lançamento público</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">PERGUNTAS</div>
                <h2>O que perguntam antes de comprar</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>O que exatamente estou comprando com uma pré-venda?</summary>
                    <div class="a">Você está reservando acesso ao motor a preço fundador antes do lançamento público. Seu nível e preço ficam travados permanentemente na sua conta. Os membros fundadores entram primeiro quando o motor for ao ar, e as novidades do lançamento vão para o email usado no checkout.</div>
                </details>
                <details>
                    <summary>Meus fundos saem do meu controle em algum momento?</summary>
                    <div class="a">Não. O motor se conecta à sua própria conta de exchange por chaves API que você controla e pode revogar a qualquer momento. Nunca custodiamos seu capital, e permissões de saque jamais são exigidas.</div>
                </details>
                <details>
                    <summary>Preciso de experiência em trading?</summary>
                    <div class="a">Não é preciso ler gráficos nem saber operar — a configuração é feita uma única vez. Você deve, porém, entender que todo trading envolve risco real de perda antes de comprometer capital.</div>
                </details>
                <details>
                    <summary>O motor pode perder dinheiro?</summary>
                    <div class="a">Sim. Qualquer resposta honesta a essa pergunta é sim — nenhuma estratégia vence todas as operações, e a reversão à média tem risco em mercados de tendência forte. É exatamente por isso que o motor aplica dimensionamento de posição e limites de exposição em cada operação. Nunca opere com capital que você não pode perder.</div>
                </details>
                <details>
                    <summary>Qual a diferença entre os níveis?</summary>
                    <div class="a">Prototype é acesso inicial de mercado único ao motor protótipo. Founding Alpha é acesso completo vitalício sem taxas recorrentes. Early Access é o mesmo motor completo cobrado mensalmente com cancelamento livre. VIP Annual adiciona execução prioritária, acesso API completo e suporte prioritário.</div>
                </details>
                <details>
                    <summary>O que acontece depois da pré-venda?</summary>
                    <div class="a">Você recebe a confirmação do pedido imediatamente, seguida de novidades sobre o cronograma de lançamento e instruções de onboarding por email. Os membros fundadores entram antes da disponibilidade pública.</div>
                </details>
                <details>
                    <summary>Posso pedir reembolso?</summary>
                    <div class="a">Sim — as pré-vendas são totalmente reembolsáveis a qualquer momento antes do lançamento. Contate o suporte (dados no seu recibo de compra) e o reembolso será processado. Após o lançamento, os passes mensal e anual podem ser cancelados a qualquer momento para interromper cobranças futuras. Detalhes completos nos nossos <a href="/terms" style="color:var(--accent)">Termos de Serviço</a> (em inglês).</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>O preço fundador termina no lançamento.</h2>
            <p>Reserve seu nível agora — quando o motor for público, esses preços serão aposentados permanentemente.</p>
            <a href="#pricing" class="btn primary">Reservar Meu Nível</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">Como Funciona</a>
                    <a href="#strategy">Estratégia</a>
                    <a href="#pricing">Preços</a>
                    <a href="#faq">Perguntas</a>
                    <a href="/terms">Termos</a>
                    <a href="/privacy">Privacidade</a>
                </div>
            </div>
            <p class="disclaimer">Aviso de risco: Trading envolve risco substancial de perda e não é adequado para todo investidor. Estratégias algorítmicas e automatizadas podem perder dinheiro e perdem; desempenho passado ou simulado não garante resultados futuros. O ai PassiveAutotrades é uma ferramenta de software — não é consultor de investimentos, corretora nem fiduciário, e nada neste site constitui aconselhamento financeiro ou solicitação para operar. As compras de pré-venda concedem acesso ao software no lançamento conforme descrito acima. Opere apenas com capital que você pode perder.</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. Todos os direitos reservados.</p>
        </div>
    </footer>
</body>
</html>
"""

# Arabic needs right-to-left layout: dir="rtl" on <html> plus a few overrides for
# the physical-direction CSS rules; the signal console stays LTR (terminal data).
RTL_OVERRIDES = """
<style>
    .lang { margin-left: 0; margin-right: auto; }
    .quote-box { border-left: 1px solid var(--line); border-right: 3px solid var(--accent); }
    .stat { border-left: none; border-right: 1px solid var(--line-soft); }
    .stat:first-child { border-right: none; }
    .hero-foot span::before, .checklist li::before, .tier ul li::before { margin-right: 0; margin-left: 6px; }
    .console { direction: ltr; }
</style>
"""

HOMEPAGE_HTML_AR = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — محرك تداول كمي آلي بمؤشر Z-Score</title>
    <meta name="description" content="محرك تداول آلي بالكامل يعتمد على استراتيجية العودة إلى المتوسط بمؤشر Z-Score. تنفيذ دون تدخل، ضوابط مخاطر مدمجة، وأموالك لا تغادر حسابك الخاص أبداً. احجز وصول المؤسسين الآن.">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/ar">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/ar">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — دخل مؤسسي، مؤتمت.">
    <meta property="og:description" content="استراتيجيات كمية آلية بمؤشر Z-Score دون مراقبة الرسوم البيانية. احجز وصول المؤسسين قبل الإطلاق.">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="ar_AR">
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
""" + HOMEPAGE_STYLE + RTL_OVERRIDES + """
</head>
<body>
    <nav>
        <div class="nav-inner">
            <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
            <div class="nav-links">
                <a href="#how">كيف يعمل</a>
                <a href="#strategy">الاستراتيجية</a>
                <a href="#pricing">الأسعار</a>
                <a href="#faq">الأسئلة</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><a href="/fr">FR</a><a href="/de">DE</a><a href="/pt">PT</a><span class="cur">AR</span><a href="/fa">FA</a><a href="/ur">UR</a><a href="/hi">HI</a><a href="/bn">BN</a><a href="/ta">TA</a></div>
            <a href="#pricing" class="nav-cta">احجز وصولك</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>محرك كمي آلي بمؤشر Z-SCORE</div>
                    <h1>دخل مؤسسي،<br><span class="grad">مؤتمت.</span></h1>
                    <p class="hero-sub">محرك تداول آلي بالكامل مبني على استراتيجية العودة إلى المتوسط بمؤشر Z-Score — المنهجية الإحصائية ذاتها التي تعتمدها مكاتب التداول الكمي — يعمل على مدار الساعة حتى لا تراقب الرسوم البيانية مجدداً.</p>
                    <div class="hero-note">حجز مسبق للمؤسسين — ثبّت سعراً مدى الحياة قبل الإطلاق العام</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">عرض باقات الحجز المسبق</a>
                        <a href="#how" class="btn ghost">كيف يعمل</a>
                    </div>
                    <div class="hero-foot">
                        <span>تنفيذ دون أي تدخل</span>
                        <span>ضوابط مخاطر مدمجة</span>
                        <span>إمكانية الإلغاء في أي وقت</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">ENGINE — SIGNAL MONITOR</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC–USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">ETH–USD</span><span class="z">z&nbsp;=&nbsp;−0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL–USD</span><span class="z">z&nbsp;=&nbsp;−2.87</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">XRP–USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risk ✓ &nbsp; sizing ✓ &nbsp; exposure ✓</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">شاشة إشارات توضيحية — هكذا يقرأ المحرك السوق</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>تغطية مستقلة للسوق</span></div>
            <div class="stat"><b>ms</b><span>سرعة تنفيذ خوارزمية</span></div>
            <div class="stat"><b>0</b><span>رسوم بيانية عليك مراقبتها</span></div>
            <div class="stat"><b>100%</b><span>قائم على القواعد — صفر عواطف</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">كيف يعمل</div>
            <div class="sec-head">
                <h2>ثلاث خطوات. ثم يتولى المحرك القيادة.</h2>
                <p>لا مجموعات إشارات، لا ساعات أمام الشاشة، لا قرارات مزاجية. بعد الإعداد، يصبح كل دخول وخروج منهجياً بالكامل.</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>احجز باقتك</h3>
                    <p>احجز الباقة المناسبة لك مسبقاً. سعر المؤسسين يُثبَّت في حسابك بشكل دائم — ولن يُعرض مجدداً بعد الإطلاق.</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>اربط وهيّئ</h3>
                    <p>عند الإطلاق، اربط المحرك بحسابك في منصة التداول وحدد معايير المخاطر مرة واحدة. أموالك تبقى في حسابك الخاص في جميع الأوقات.</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>المحرك ينفّذ</h3>
                    <p>يراقب نواة Z-Score الانحراف الإحصائي على مدار الساعة وينفّذ الدخول والخروج وتحديد حجم المراكز تلقائياً.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">الاستراتيجية</div>
                    <h2>لماذا العودة إلى المتوسط بمؤشر Z-Score؟</h2>
                    <p>الأسواق تبالغ في ردود أفعالها. تبتعد الأسعار عن متوسطها الإحصائي، والأسعار الممتدة تميل إلى العودة. يقيس مؤشر Z-Score بدقة مدى امتداد السعر — بالانحرافات المعيارية — فيحوّل «هذا يبدو مبالغاً فيه» إلى رقم دقيق قابل للاختبار.</p>
                    <ul class="checklist">
                        <li>يتداول ميزة إحصائية محددة — لا مؤشرات عشوائية ولا حدس ولا ضجيج</li>
                        <li>كل مركز يُفتح ويُغلق وفق قاعدة، مع تحديد المخاطر قبل تنفيذ الصفقة</li>
                        <li>فئة المنهجية ذاتها المستخدمة في مكاتب المراجحة الإحصائية المؤسسية منذ عقود</li>
                        <li>بلا عواطف بحكم التصميم: المحرك لا يعرف الانتقام ولا الخوف من الفوات ولا التردد</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">«عندما ينحرف السعر أكثر من ±2 انحراف معياري عن متوسطه المتحرك، يسلّح المحرك مركز عودة إلى المتوسط — ويديره حتى النهاية دون تدخل بشري.»</div>
                    <div class="src">— القاعدة الأساسية داخل ai PassiveAutotrades، معلنة بوضوح. لا صندوق أسود، ولا إشارات غامضة.</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">ما الذي تحصل عليه</div>
            <div class="sec-head">
                <h2>مُصمَّم كمكتب تداول. يُسلَّم كمنتج.</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>نواة إشارات Z-Score</h3><p>الانحراف الإحصائي على نافذة متحركة يقود كل إشارة — شفاف وقابل للاختبار ومتسق.</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>تنفيذ بالمللي ثانية</h3><p>تنطلق الإشارات خوارزمياً لحظة تجاوز العتبات — ليلاً ونهاراً وفي عطلات نهاية الأسبوع.</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>حدود مخاطر صارمة</h3><p>حجم لكل صفقة، وسقوف تعرض، وخروج آلي تُفرض على كل مركز دون استثناء.</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>أموالك، حسابك</h3><p>يتصل المحرك بحسابك الخاص في منصة التداول. رأس المال لا يُحوَّل إلينا أبداً.</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>إعداد لمرة واحدة</h3><p>اختر مستوى المخاطر والأسواق مرة واحدة فقط. لا صيانة مستمرة ولا مراقبة.</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>وصول API <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>وصول برمجي كامل إلى المحرك للتكاملات والمراقبة المخصصة.</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">حجز المؤسسين المسبق</div>
                <h2>ثبّت باقتك قبل الإطلاق</h2>
                <p>كل باقة هي حجز مسبق بسعر المؤسسين. عند إطلاق المحرك، ينضم الأعضاء المؤسسون أولاً — وتُسحب هذه الأسعار نهائياً.</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">حجز مسبق</span>
                    <h3>Prototype</h3>
                    <div class="who">لمن يبدأ في التداول الخوارزمي</div>
                    <div class="price">$79.99</div>
                    <div class="per">دفعة واحدة (دولار أمريكي)</div>
                    <ul>
                        <li>وصول مبدئي إلى محرك النموذج الأولي</li>
                        <li>استراتيجية Z-Score الأساسية، سوق واحد</li>
                        <li>ضوابط مخاطر قياسية</li>
                        <li>دعم عبر البريد الإلكتروني</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">احصل على Prototype</a>
                </div>
                <div class="tier">
                    <span class="badge">حجز مسبق</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">للمؤمنين بالمدى الطويل</div>
                    <div class="price">$199.99</div>
                    <div class="per">دفعة واحدة · مدى الحياة (دولار أمريكي)</div>
                    <ul>
                        <li>وصول كامل مدى الحياة إلى المحرك</li>
                        <li>جميع الأسواق وتحديثات الاستراتيجية، للأبد</li>
                        <li>لا رسوم متكررة، أبداً</li>
                        <li>انضمام ذو أولوية عند الإطلاق</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">احجز مدى الحياة</a>
                </div>
                <div class="tier">
                    <span class="badge">حجز مسبق</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">لمن يفضّل المرونة</div>
                    <div class="price">$49.99</div>
                    <div class="per">شهرياً (دولار أمريكي)</div>
                    <ul>
                        <li>الاستفادة الكاملة من المحرك</li>
                        <li>جميع الأسواق مشمولة</li>
                        <li>ألغِ في أي وقت</li>
                        <li>دعم قياسي</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">احجز شهرياً</a>
                </div>
                <div class="tier featured">
                    <span class="flag">أفضل قيمة</span>
                    <span class="badge">حجز مسبق</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">للمتداولين الجادين</div>
                    <div class="price">$499.99</div>
                    <div class="per">سنوياً (دولار أمريكي)</div>
                    <ul>
                        <li>كل ما في Early Access</li>
                        <li>أولوية في طابور التنفيذ</li>
                        <li>وصول API كامل</li>
                        <li>قناة دعم ذات أولوية</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">احجز سنوياً</a>
                </div>
            </div>
            <p class="pricing-note">دفع آمن عبر Stripe · ادفع بالدولار الأمريكي أو اليورو أو الجنيه الإسترليني أو الدولار الكندي أو الأسترالي — تُكتشف عملتك تلقائياً عند الدفع · تُسحب أسعار المؤسسين نهائياً عند الإطلاق العام</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">الأسئلة</div>
                <h2>ما يُسأل قبل الشراء</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>ما الذي أشتريه بالضبط بالحجز المسبق؟</summary>
                    <div class="a">أنت تحجز الوصول إلى المحرك بسعر المؤسسين قبل الإطلاق العام. باقتك وسعرك يُثبَّتان في حسابك بشكل دائم. ينضم الأعضاء المؤسسون أولاً عند تشغيل المحرك، وتُرسل مستجدات الإطلاق إلى البريد الإلكتروني المستخدم عند الدفع.</div>
                </details>
                <details>
                    <summary>هل تخرج أموالي من سيطرتي في أي وقت؟</summary>
                    <div class="a">لا. يتصل المحرك بحسابك الخاص في منصة التداول عبر مفاتيح API تتحكم بها أنت ويمكنك إلغاؤها في أي وقت. لا نحتفظ برأس مالك أبداً، ولا تُطلب صلاحيات السحب مطلقاً.</div>
                </details>
                <details>
                    <summary>هل أحتاج إلى خبرة في التداول؟</summary>
                    <div class="a">لا حاجة لقراءة الرسوم البيانية أو مهارة في التداول لتشغيل المحرك — الإعداد يتم مرة واحدة. لكن عليك أن تدرك أن كل تداول ينطوي على خطر خسارة حقيقي قبل استثمار أي رأس مال.</div>
                </details>
                <details>
                    <summary>هل يمكن أن يخسر المحرك المال؟</summary>
                    <div class="a">نعم. أي إجابة صادقة عن هذا السؤال هي نعم — لا توجد استراتيجية تربح كل صفقة، والعودة إلى المتوسط تنطوي على مخاطر في الأسواق ذات الاتجاهات القوية. لهذا بالتحديد يفرض المحرك تحديد حجم المراكز وحدود التعرض على كل صفقة. لا تتداول أبداً برأس مال لا يمكنك تحمّل خسارته.</div>
                </details>
                <details>
                    <summary>ما الفرق بين الباقات؟</summary>
                    <div class="a">Prototype وصول مبدئي بسوق واحد إلى محرك النموذج الأولي. Founding Alpha وصول كامل مدى الحياة دون رسوم متكررة. Early Access هو المحرك الكامل ذاته بفوترة شهرية مع إلغاء حر. VIP Annual يضيف أولوية التنفيذ ووصول API الكامل والدعم ذا الأولوية.</div>
                </details>
                <details>
                    <summary>ماذا يحدث بعد الحجز المسبق؟</summary>
                    <div class="a">تصلك رسالة تأكيد الطلب فوراً، تليها مستجدات الجدول الزمني للإطلاق وتعليمات الانضمام عبر البريد الإلكتروني. ينضم الأعضاء المؤسسون قبل الإتاحة العامة.</div>
                </details>
                <details>
                    <summary>هل يمكنني استرداد أموالي؟</summary>
                    <div class="a">نعم — الحجوزات المسبقة قابلة للاسترداد بالكامل في أي وقت قبل الإطلاق. تواصل مع الدعم (البيانات في إيصال الشراء) وسيُعالج الاسترداد. بعد الإطلاق، يمكن إلغاء الباقتين الشهرية والسنوية في أي وقت لإيقاف الفوترة المستقبلية. التفاصيل الكاملة في <a href="/terms" style="color:var(--accent)">شروط الخدمة</a> (بالإنجليزية).</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>سعر المؤسسين ينتهي عند الإطلاق.</h2>
            <p>احجز باقتك الآن — عندما يصبح المحرك عاماً، تُسحب هذه الأسعار نهائياً.</p>
            <a href="#pricing" class="btn primary">احجز باقتي</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">كيف يعمل</a>
                    <a href="#strategy">الاستراتيجية</a>
                    <a href="#pricing">الأسعار</a>
                    <a href="#faq">الأسئلة</a>
                    <a href="/terms">الشروط</a>
                    <a href="/privacy">الخصوصية</a>
                </div>
            </div>
            <p class="disclaimer">إفصاح عن المخاطر: ينطوي التداول على خطر خسارة كبير وهو غير مناسب لكل مستثمر. الاستراتيجيات الخوارزمية والآلية يمكن أن تخسر المال وهي تخسره فعلاً؛ الأداء السابق أو المحاكى لا يضمن النتائج المستقبلية. ai PassiveAutotrades أداة برمجية — ليست مستشاراً استثمارياً ولا وسيطاً مالياً ولا جهة ائتمانية، ولا شيء في هذا الموقع يشكل نصيحة مالية أو دعوة للتداول. مشتريات الحجز المسبق تمنح الوصول إلى البرنامج عند الإطلاق كما هو موضح أعلاه. تداول فقط برأس مال يمكنك تحمّل خسارته.</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. جميع الحقوق محفوظة.</p>
        </div>
    </footer>
</body>
</html>
"""

HOMEPAGE_HTML_FA = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — موتور معاملات کمّی خودکار Z-Score</title>
    <meta name="description" content="موتور معاملاتی کاملاً خودکار مبتنی بر بازگشت به میانگین Z-Score. اجرای بدون دخالت، کنترل ریسک داخلی، و سرمایه شما هرگز از حساب خودتان خارج نمی‌شود. دسترسی بنیان‌گذاران را پیش‌خرید کنید.">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/fa">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/fa">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — درآمد نهادی، خودکار.">
    <meta property="og:description" content="استراتژی‌های کمّی Z-Score خودکار بدون تماشای نمودار. دسترسی بنیان‌گذاران را پیش از عرضه پیش‌خرید کنید.">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="fa_IR">
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
""" + HOMEPAGE_STYLE + RTL_OVERRIDES + """
</head>
<body>
    <nav>
        <div class="nav-inner">
            <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
            <div class="nav-links">
                <a href="#how">نحوه کار</a>
                <a href="#strategy">استراتژی</a>
                <a href="#pricing">قیمت‌ها</a>
                <a href="#faq">پرسش‌ها</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><a href="/fr">FR</a><a href="/de">DE</a><a href="/pt">PT</a><a href="/ar">AR</a><span class="cur">FA</span><a href="/ur">UR</a><a href="/hi">HI</a><a href="/bn">BN</a><a href="/ta">TA</a></div>
            <a href="#pricing" class="nav-cta">پیش‌خرید دسترسی</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>موتور کمّی خودکار Z-SCORE</div>
                    <h1>درآمد نهادی،<br><span class="grad">خودکار.</span></h1>
                    <p class="hero-sub">یک موتور معاملاتی کاملاً خودکار بر پایه بازگشت به میانگین Z-Score — همان روش‌شناسی آماری میزهای معاملات کمّی — که شبانه‌روز اجرا می‌کند تا شما دیگر هرگز به نمودار خیره نشوید.</p>
                    <div class="hero-note">پیش‌خرید بنیان‌گذاران — قیمت مادام‌العمر را پیش از عرضه عمومی قفل کنید</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">مشاهده پلن‌های پیش‌خرید</a>
                        <a href="#how" class="btn ghost">نحوه کار</a>
                    </div>
                    <div class="hero-foot">
                        <span>اجرای بدون دخالت</span>
                        <span>کنترل ریسک داخلی</span>
                        <span>امکان لغو در هر زمان</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">ENGINE — SIGNAL MONITOR</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC–USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">ETH–USD</span><span class="z">z&nbsp;=&nbsp;−0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL–USD</span><span class="z">z&nbsp;=&nbsp;−2.87</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">XRP–USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risk ✓ &nbsp; sizing ✓ &nbsp; exposure ✓</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">نمای نمونه سیگنال‌ها — موتور بازار را این‌گونه می‌خواند</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>پوشش خودکار بازار</span></div>
            <div class="stat"><b>ms</b><span>سرعت اجرای الگوریتمی</span></div>
            <div class="stat"><b>0</b><span>نموداری که باید تماشا کنید</span></div>
            <div class="stat"><b>100%</b><span>قانون‌محور — بدون احساسات</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">نحوه کار</div>
            <div class="sec-head">
                <h2>سه گام. سپس موتور کنترل را به دست می‌گیرد.</h2>
                <p>نه گروه سیگنال، نه ساعت‌ها پای نمایشگر، نه تصمیم‌های سلیقه‌ای. پس از پیکربندی، هر ورود و خروج سیستماتیک است.</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>پلن خود را رزرو کنید</h3>
                    <p>پلن مناسب خود را پیش‌خرید کنید. قیمت بنیان‌گذاران برای همیشه روی حساب شما قفل می‌شود — پس از عرضه دیگر هرگز ارائه نخواهد شد.</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>اتصال و پیکربندی</h3>
                    <p>هنگام عرضه، موتور را به حساب صرافی خود متصل کنید و پارامترهای ریسک را یک بار تنظیم کنید. سرمایه شما همیشه در حساب خودتان می‌ماند.</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>موتور اجرا می‌کند</h3>
                    <p>هسته Z-Score انحراف آماری را شبانه‌روز رصد می‌کند و ورود، خروج و اندازه پوزیشن را خودکار اجرا می‌کند.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">استراتژی</div>
                    <h2>چرا بازگشت به میانگین Z-Score؟</h2>
                    <p>بازارها بیش‌واکنشی‌اند. قیمت‌ها از میانگین آماری خود فاصله می‌گیرند و قیمت‌های کشیده‌شده تمایل به بازگشت دارند. Z-Score دقیقاً اندازه می‌گیرد قیمت چقدر کشیده شده — به انحراف معیار — و «به نظر بیش‌ازحد رفته» را به عددی دقیق و آزمون‌پذیر تبدیل می‌کند.</p>
                    <ul class="checklist">
                        <li>معامله بر مبنای یک مزیت آماری تعریف‌شده — نه اندیکاتور، نه حدس، نه هیاهو</li>
                        <li>هر پوزیشن طبق قاعده باز و بسته می‌شود و ریسک پیش از معامله اندازه‌گیری می‌شود</li>
                        <li>همان خانواده روش‌هایی که میزهای نهادی آربیتراژ آماری دهه‌هاست به کار می‌برند</li>
                        <li>بدون احساسات به‌حکم طراحی: موتور نه انتقام می‌گیرد، نه FOMO دارد و نه تردید می‌کند</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">«وقتی قیمت بیش از ±۲ انحراف معیار از میانگین متحرک خود فاصله بگیرد، موتور یک پوزیشن بازگشتی مسلح می‌کند — و آن را تا پایان بدون دخالت انسانی مدیریت می‌کند.»</div>
                    <div class="src">— قاعده اصلی ai PassiveAutotrades، بیان‌شده به‌روشنی. نه جعبه سیاه، نه سیگنال‌های مرموز.</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">چه چیزی دریافت می‌کنید</div>
            <div class="sec-head">
                <h2>مهندسی‌شده مانند یک میز معاملات. تحویل‌شده مانند یک محصول.</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>هسته سیگنال Z-Score</h3><p>انحراف آماری روی پنجره متحرک هر سیگنال را هدایت می‌کند — شفاف، آزمون‌پذیر و یکنواخت.</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>اجرا در میلی‌ثانیه</h3><p>سیگنال‌ها به‌محض عبور از آستانه‌ها الگوریتمی شلیک می‌شوند — روز، شب و آخر هفته.</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>حدود ریسک سخت‌گیرانه</h3><p>اندازه هر معامله، سقف اکسپوژر و خروج خودکار روی هر پوزیشن اعمال می‌شود.</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>سرمایه شما، حساب شما</h3><p>موتور به حساب صرافی خود شما متصل می‌شود. سرمایه هرگز به ما منتقل نمی‌شود.</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>پیکربندی یک‌باره</h3><p>سطح ریسک و بازارها را فقط یک بار انتخاب کنید. بدون نگهداری یا مراقبت مداوم.</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>دسترسی API <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>دسترسی برنامه‌نویسی کامل به موتور برای یکپارچه‌سازی و پایش سفارشی.</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">پیش‌خرید بنیان‌گذاران</div>
                <h2>پلن خود را پیش از عرضه قفل کنید</h2>
                <p>هر پلن یک پیش‌خرید با قیمت بنیان‌گذاران است. هنگام عرضه موتور، اعضای بنیان‌گذار اول وارد می‌شوند — و این قیمت‌ها برای همیشه بازنشسته می‌شوند.</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">پیش‌خرید</span>
                    <h3>Prototype</h3>
                    <div class="who">برای تازه‌واردان معاملات الگوریتمی</div>
                    <div class="price">$79.99</div>
                    <div class="per">پرداخت یک‌باره (دلار آمریکا)</div>
                    <ul>
                        <li>دسترسی اولیه به موتور نمونه</li>
                        <li>استراتژی پایه Z-Score، یک بازار</li>
                        <li>کنترل ریسک استاندارد</li>
                        <li>پشتیبانی ایمیلی</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">دریافت Prototype</a>
                </div>
                <div class="tier">
                    <span class="badge">پیش‌خرید</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">برای باورمندان بلندمدت</div>
                    <div class="price">$199.99</div>
                    <div class="per">پرداخت یک‌باره · مادام‌العمر (دلار آمریکا)</div>
                    <ul>
                        <li>دسترسی کامل مادام‌العمر به موتور</li>
                        <li>همه بازارها و به‌روزرسانی‌ها، برای همیشه</li>
                        <li>بدون هزینه تکرارشونده، هرگز</li>
                        <li>ورود با اولویت هنگام عرضه</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">رزرو مادام‌العمر</a>
                </div>
                <div class="tier">
                    <span class="badge">پیش‌خرید</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">برای شروع منعطف</div>
                    <div class="price">$49.99</div>
                    <div class="per">ماهانه (دلار آمریکا)</div>
                    <ul>
                        <li>کارایی کامل موتور</li>
                        <li>شامل همه بازارها</li>
                        <li>لغو در هر زمان</li>
                        <li>پشتیبانی استاندارد</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">رزرو ماهانه</a>
                </div>
                <div class="tier featured">
                    <span class="flag">بهترین ارزش</span>
                    <span class="badge">پیش‌خرید</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">برای معامله‌گران جدی</div>
                    <div class="price">$499.99</div>
                    <div class="per">سالانه (دلار آمریکا)</div>
                    <ul>
                        <li>همه امکانات Early Access</li>
                        <li>صف اجرای با اولویت</li>
                        <li>دسترسی کامل API</li>
                        <li>کانال پشتیبانی با اولویت</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">رزرو سالانه</a>
                </div>
            </div>
            <p class="pricing-note">پرداخت امن با Stripe · با دلار آمریکا، یورو، پوند، دلار کانادا یا استرالیا بپردازید — ارز شما هنگام پرداخت خودکار تشخیص داده می‌شود · قیمت‌های بنیان‌گذاران با عرضه عمومی برای همیشه حذف می‌شوند</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">پرسش‌ها</div>
                <h2>آنچه پیش از خرید می‌پرسند</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>با پیش‌خرید دقیقاً چه می‌خرم؟</summary>
                    <div class="a">شما دسترسی به موتور را با قیمت بنیان‌گذاران، پیش از عرضه عمومی، رزرو می‌کنید. پلن و قیمت شما برای همیشه روی حسابتان قفل می‌شود. اعضای بنیان‌گذار هنگام راه‌اندازی اول وارد می‌شوند و اخبار عرضه به ایمیلی که هنگام پرداخت استفاده کرده‌اید ارسال می‌شود.</div>
                </details>
                <details>
                    <summary>آیا سرمایه‌ام هرگز از کنترلم خارج می‌شود؟</summary>
                    <div class="a">خیر. موتور از طریق کلیدهای API به حساب صرافی خود شما متصل می‌شود — کلیدهایی که شما کنترل می‌کنید و هر زمان می‌توانید باطل کنید. ما هرگز سرمایه شما را نگه نمی‌داریم و مجوز برداشت هیچ‌گاه لازم نیست.</div>
                </details>
                <details>
                    <summary>آیا به تجربه معامله‌گری نیاز دارم؟</summary>
                    <div class="a">برای کار با موتور نه نمودارخوانی لازم است نه مهارت معامله — پیکربندی یک بار انجام می‌شود. اما پیش از واردکردن سرمایه باید بدانید که هر معامله‌ای ریسک واقعی زیان دارد.</div>
                </details>
                <details>
                    <summary>آیا موتور ممکن است ضرر کند؟</summary>
                    <div class="a">بله. هر پاسخ صادقانه‌ای به این پرسش «بله» است — هیچ استراتژی‌ای همه معاملات را نمی‌برد و بازگشت به میانگین در بازارهای بهشدت روند‌دار ریسک دارد. دقیقاً به همین دلیل موتور اندازه پوزیشن و حدود اکسپوژر را روی هر معامله اعمال می‌کند. هرگز با سرمایه‌ای معامله نکنید که توان از دست دادنش را ندارید.</div>
                </details>
                <details>
                    <summary>تفاوت پلن‌ها چیست؟</summary>
                    <div class="a">Prototype دسترسی اولیه تک‌بازاره به موتور نمونه است. Founding Alpha دسترسی کامل مادام‌العمر بدون هزینه تکرارشونده است. Early Access همان موتور کامل با پرداخت ماهانه و لغو آزاد است. VIP Annual اجرای با اولویت، دسترسی کامل API و پشتیبانی با اولویت را اضافه می‌کند.</div>
                </details>
                <details>
                    <summary>بعد از پیش‌خرید چه می‌شود؟</summary>
                    <div class="a">تأییدیه سفارش را بلافاصله دریافت می‌کنید و سپس اخبار زمان‌بندی عرضه و دستورالعمل ورود از طریق ایمیل می‌رسد. اعضای بنیان‌گذار پیش از دسترسی عمومی وارد می‌شوند.</div>
                </details>
                <details>
                    <summary>آیا می‌توانم وجهم را پس بگیرم؟</summary>
                    <div class="a">بله — پیش‌خریدها تا پیش از عرضه در هر زمان کاملاً قابل استردادند. با پشتیبانی تماس بگیرید (اطلاعات در رسید خرید شماست) تا استرداد انجام شود. پس از عرضه، پلن‌های ماهانه و سالانه هر زمان قابل لغو هستند تا صورتحساب آینده متوقف شود. جزئیات کامل در <a href="/terms" style="color:var(--accent)">شرایط خدمات</a> (به انگلیسی).</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>قیمت بنیان‌گذاران با عرضه پایان می‌یابد.</h2>
            <p>همین حالا پلن خود را رزرو کنید — وقتی موتور عمومی شود، این قیمت‌ها برای همیشه حذف می‌شوند.</p>
            <a href="#pricing" class="btn primary">رزرو پلن من</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">نحوه کار</a>
                    <a href="#strategy">استراتژی</a>
                    <a href="#pricing">قیمت‌ها</a>
                    <a href="#faq">پرسش‌ها</a>
                    <a href="/terms">شرایط</a>
                    <a href="/privacy">حریم خصوصی</a>
                </div>
            </div>
            <p class="disclaimer">افشای ریسک: معامله‌گری ریسک زیان قابل‌توجهی دارد و برای هر سرمایه‌گذاری مناسب نیست. استراتژی‌های الگوریتمی و خودکار می‌توانند ضرر کنند و ضرر هم می‌کنند؛ عملکرد گذشته یا شبیه‌سازی‌شده تضمینی برای نتایج آینده نیست. ai PassiveAutotrades یک ابزار نرم‌افزاری است — نه مشاور سرمایه‌گذاری، نه کارگزار و نه امین، و هیچ‌چیز در این وب‌سایت توصیه مالی یا دعوت به معامله نیست. خرید پیش‌فروش، دسترسی به نرم‌افزار را هنگام عرضه مطابق توضیحات بالا فراهم می‌کند. تنها با سرمایه‌ای معامله کنید که توان از دست دادنش را دارید.</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. تمامی حقوق محفوظ است.</p>
        </div>
    </footer>
</body>
</html>
"""

HOMEPAGE_HTML_UR = """
<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — خودکار Z-Score کوانٹ ٹریڈنگ انجن</title>
    <meta name="description" content="Z-Score مین ریورژن پر مبنی مکمل خودکار ٹریڈنگ انجن۔ بغیر مداخلت ایگزیکیوشن، بلٹ اِن رسک کنٹرول، اور آپ کے فنڈز کبھی آپ کے اپنے اکاؤنٹ سے باہر نہیں جاتے۔ فاؤنڈر رسائی ابھی پری آرڈر کریں۔">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/ur">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/ur">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — ادارہ جاتی آمدنی، خودکار۔">
    <meta property="og:description" content="چارٹ دیکھے بغیر خودکار Z-Score کوانٹ حکمتِ عملیاں۔ لانچ سے پہلے فاؤنڈر رسائی پری آرڈر کریں۔">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="ur_PK">
    <script defer src="/_vercel/insights/script.js"></script>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
""" + HOMEPAGE_STYLE + RTL_OVERRIDES + """
</head>
<body>
    <nav>
        <div class="nav-inner">
            <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
            <div class="nav-links">
                <a href="#how">طریقہ کار</a>
                <a href="#strategy">حکمتِ عملی</a>
                <a href="#pricing">قیمتیں</a>
                <a href="#faq">سوالات</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><a href="/fr">FR</a><a href="/de">DE</a><a href="/pt">PT</a><a href="/ar">AR</a><a href="/fa">FA</a><span class="cur">UR</span><a href="/hi">HI</a><a href="/bn">BN</a><a href="/ta">TA</a></div>
            <a href="#pricing" class="nav-cta">رسائی پری آرڈر کریں</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>خودکار Z-SCORE کوانٹ انجن</div>
                    <h1>ادارہ جاتی آمدنی،<br><span class="grad">خودکار۔</span></h1>
                    <p class="hero-sub">Z-Score مین ریورژن پر مبنی ایک مکمل خودکار ٹریڈنگ انجن — وہی شماریاتی طریقہ کار جو کوانٹ ڈیسک استعمال کرتے ہیں — چوبیس گھنٹے چلتا ہے تاکہ آپ کبھی چارٹ نہ دیکھیں۔</p>
                    <div class="hero-note">فاؤنڈر پری آرڈر — عوامی لانچ سے پہلے تاحیات قیمت مقفل کریں</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">پری آرڈر پلان دیکھیں</a>
                        <a href="#how" class="btn ghost">طریقہ کار</a>
                    </div>
                    <div class="hero-foot">
                        <span>بغیر مداخلت ایگزیکیوشن</span>
                        <span>بلٹ اِن رسک کنٹرول</span>
                        <span>کسی بھی وقت منسوخی</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">ENGINE — SIGNAL MONITOR</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC–USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">ETH–USD</span><span class="z">z&nbsp;=&nbsp;−0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL–USD</span><span class="z">z&nbsp;=&nbsp;−2.87</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">XRP–USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risk ✓ &nbsp; sizing ✓ &nbsp; exposure ✓</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">مثالی سگنل فیڈ — انجن مارکیٹ کو یوں پڑھتا ہے</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>خودمختار مارکیٹ کوریج</span></div>
            <div class="stat"><b>ms</b><span>الگورتھمک ایگزیکیوشن کی رفتار</span></div>
            <div class="stat"><b>0</b><span>چارٹ جو آپ کو دیکھنے ہوں</span></div>
            <div class="stat"><b>100%</b><span>اصول پر مبنی — صفر جذبات</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">طریقہ کار</div>
            <div class="sec-head">
                <h2>تین مراحل۔ پھر انجن سنبھال لیتا ہے۔</h2>
                <p>نہ سگنل گروپ، نہ اسکرین کے گھنٹے، نہ صوابدیدی فیصلے۔ ایک بار کنفیگر ہونے کے بعد ہر انٹری اور ایگزٹ منظم ہے۔</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>اپنا پلان محفوظ کریں</h3>
                    <p>اپنے لیے موزوں پلان پری آرڈر کریں۔ فاؤنڈر قیمت مستقل طور پر آپ کے اکاؤنٹ سے منسلک ہو جاتی ہے — لانچ کے بعد یہ دوبارہ کبھی پیش نہیں ہوگی۔</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>جوڑیں اور کنفیگر کریں</h3>
                    <p>لانچ پر انجن کو اپنے ایکسچینج اکاؤنٹ سے جوڑیں اور رسک پیرامیٹر ایک بار طے کریں۔ آپ کے فنڈز ہر وقت آپ کے اپنے اکاؤنٹ میں رہتے ہیں۔</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>انجن ایگزیکیوٹ کرتا ہے</h3>
                    <p>Z-Score کور چوبیس گھنٹے شماریاتی انحراف پر نظر رکھتا ہے اور انٹری، ایگزٹ اور پوزیشن سائزنگ خودکار انجام دیتا ہے۔</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">حکمتِ عملی</div>
                    <h2>Z-Score مین ریورژن ہی کیوں؟</h2>
                    <p>مارکیٹیں حد سے زیادہ ردعمل دیتی ہیں۔ قیمتیں اپنے شماریاتی اوسط سے دور نکل جاتی ہیں، اور کھنچی ہوئی قیمتیں واپس پلٹنے کی طرف مائل ہوتی ہیں۔ Z-Score بالکل ناپتا ہے کہ قیمت کتنی کھنچی ہے — معیاری انحراف میں — اور «یہ حد سے بڑھا لگتا ہے» کو ایک درست، قابلِ آزمائش عدد بنا دیتا ہے۔</p>
                    <ul class="checklist">
                        <li>ایک متعین شماریاتی برتری پر تجارت — نہ انڈیکیٹر، نہ اندازے، نہ شور</li>
                        <li>ہر پوزیشن اصول کے تحت کھلتی اور بند ہوتی ہے، رسک ٹریڈ سے پہلے ناپا جاتا ہے</li>
                        <li>وہی طریقہ کار جو ادارہ جاتی سٹیٹ-آرب ڈیسک عشروں سے استعمال کرتے ہیں</li>
                        <li>ساخت ہی سے بے جذبات: انجن نہ بدلہ لیتا ہے، نہ FOMO رکھتا ہے، نہ ہچکچاتا ہے</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">«جب قیمت اپنے رولنگ اوسط سے ±2 معیاری انحراف سے آگے نکل جائے تو انجن ایک ریورژن پوزیشن تیار کرتا ہے — اور اسے بغیر انسانی مداخلت کے انجام تک پہنچاتا ہے۔»</div>
                    <div class="src">— ai PassiveAutotrades کا بنیادی اصول، صاف لفظوں میں۔ نہ بلیک باکس، نہ پراسرار سگنل۔</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">آپ کو کیا ملتا ہے</div>
            <div class="sec-head">
                <h2>ٹریڈنگ ڈیسک کی طرح تیار۔ پروڈکٹ کی طرح فراہم۔</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>Z-Score سگنل کور</h3><p>رولنگ ونڈو شماریاتی انحراف ہر سگنل چلاتا ہے — شفاف، قابلِ آزمائش اور مستقل۔</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>ملی سیکنڈ ایگزیکیوشن</h3><p>حدیں عبور ہوتے ہی سگنل الگورتھم سے چلتے ہیں — دن، رات اور ویک اینڈ۔</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>سخت رسک حدود</h3><p>فی ٹریڈ سائزنگ، ایکسپوژر کیپ اور خودکار ایگزٹ ہر پوزیشن پر نافذ ہوتے ہیں۔</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>آپ کے فنڈز، آپ کا اکاؤنٹ</h3><p>انجن آپ کے اپنے ایکسچینج اکاؤنٹ سے جڑتا ہے۔ سرمایہ کبھی ہمیں منتقل نہیں ہوتا۔</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>ایک بار کنفیگریشن</h3><p>رسک لیول اور مارکیٹیں صرف ایک بار چنیں۔ نہ مسلسل دیکھ بھال، نہ نگرانی۔</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>API رسائی <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>حسبِ ضرورت انٹیگریشن اور مانیٹرنگ کے لیے انجن تک مکمل پروگرامیٹک رسائی۔</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">فاؤنڈر پری آرڈر</div>
                <h2>لانچ سے پہلے اپنا پلان مقفل کریں</h2>
                <p>ہر پلان فاؤنڈر قیمت پر پری آرڈر ہے۔ انجن لانچ ہونے پر فاؤنڈنگ ممبر پہلے شامل ہوتے ہیں — اور یہ قیمتیں مستقل طور پر ختم کر دی جاتی ہیں۔</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">پری آرڈر</span>
                    <h3>Prototype</h3>
                    <div class="who">الگو ٹریڈنگ کے نئے صارفین کے لیے</div>
                    <div class="price">$79.99</div>
                    <div class="per">یکمشت (امریکی ڈالر)</div>
                    <ul>
                        <li>پروٹوٹائپ انجن تک ابتدائی رسائی</li>
                        <li>بنیادی Z-Score حکمتِ عملی، ایک مارکیٹ</li>
                        <li>معیاری رسک کنٹرول</li>
                        <li>ای میل سپورٹ</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Prototype حاصل کریں</a>
                </div>
                <div class="tier">
                    <span class="badge">پری آرڈر</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">طویل مدتی یقین رکھنے والوں کے لیے</div>
                    <div class="price">$199.99</div>
                    <div class="per">یکمشت · تاحیات (امریکی ڈالر)</div>
                    <ul>
                        <li>انجن تک تاحیات مکمل رسائی</li>
                        <li>تمام مارکیٹیں اور اپڈیٹس، ہمیشہ کے لیے</li>
                        <li>کوئی بار بار فیس نہیں، کبھی نہیں</li>
                        <li>لانچ پر ترجیحی آن بورڈنگ</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">تاحیات محفوظ کریں</a>
                </div>
                <div class="tier">
                    <span class="badge">پری آرڈر</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">لچک پسند کرنے والوں کے لیے</div>
                    <div class="price">$49.99</div>
                    <div class="per">ماہانہ (امریکی ڈالر)</div>
                    <ul>
                        <li>انجن کی مکمل سہولت</li>
                        <li>تمام مارکیٹیں شامل</li>
                        <li>کسی بھی وقت منسوخ کریں</li>
                        <li>معیاری سپورٹ</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">ماہانہ محفوظ کریں</a>
                </div>
                <div class="tier featured">
                    <span class="flag">بہترین قیمت</span>
                    <span class="badge">پری آرڈر</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">سنجیدہ ٹریڈرز کے لیے</div>
                    <div class="price">$499.99</div>
                    <div class="per">سالانہ (امریکی ڈالر)</div>
                    <ul>
                        <li>Early Access کا سب کچھ</li>
                        <li>ترجیحی ایگزیکیوشن قطار</li>
                        <li>مکمل API رسائی</li>
                        <li>ترجیحی سپورٹ چینل</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">سالانہ محفوظ کریں</a>
                </div>
            </div>
            <p class="pricing-note">Stripe کے ذریعے محفوظ ادائیگی · USD، EUR، GBP، CAD یا AUD میں ادا کریں — چیک آؤٹ پر آپ کی کرنسی خودکار پہچانی جاتی ہے · فاؤنڈر قیمتیں عوامی لانچ پر مستقل ختم ہو جاتی ہیں</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">سوالات</div>
                <h2>خریدنے سے پہلے کیا پوچھا جاتا ہے</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>پری آرڈر سے میں بالکل کیا خرید رہا ہوں؟</summary>
                    <div class="a">آپ عوامی لانچ سے پہلے فاؤنڈر قیمت پر انجن کی رسائی محفوظ کر رہے ہیں۔ آپ کا پلان اور قیمت مستقل طور پر آپ کے اکاؤنٹ سے منسلک ہو جاتے ہیں۔ انجن لائیو ہونے پر فاؤنڈنگ ممبر پہلے شامل ہوتے ہیں، اور لانچ کی اطلاعات اسی ای میل پر آتی ہیں جو آپ نے چیک آؤٹ پر استعمال کی۔</div>
                </details>
                <details>
                    <summary>کیا میرے فنڈز کبھی میرے کنٹرول سے نکلتے ہیں؟</summary>
                    <div class="a">نہیں۔ انجن API کلیدوں کے ذریعے آپ کے اپنے ایکسچینج اکاؤنٹ سے جڑتا ہے — کلیدیں جو آپ کنٹرول کرتے ہیں اور کسی بھی وقت منسوخ کر سکتے ہیں۔ ہم کبھی آپ کا سرمایہ اپنے پاس نہیں رکھتے، اور وِتھڈرال اجازت کبھی درکار نہیں ہوتی۔</div>
                </details>
                <details>
                    <summary>کیا مجھے ٹریڈنگ کا تجربہ چاہیے؟</summary>
                    <div class="a">انجن چلانے کے لیے نہ چارٹ پڑھنا ضروری ہے نہ ٹریڈنگ کی مہارت — کنفیگریشن ایک بار کی جاتی ہے۔ البتہ سرمایہ لگانے سے پہلے آپ کو سمجھنا چاہیے کہ ہر ٹریڈنگ میں نقصان کا حقیقی خطرہ ہوتا ہے۔</div>
                </details>
                <details>
                    <summary>کیا انجن پیسہ کھو سکتا ہے؟</summary>
                    <div class="a">جی ہاں۔ اس سوال کا ہر ایماندار جواب ہاں ہے — کوئی حکمتِ عملی ہر ٹریڈ نہیں جیتتی، اور مضبوط رجحان والی مارکیٹوں میں مین ریورژن خطرہ رکھتا ہے۔ اسی لیے انجن ہر ٹریڈ پر پوزیشن سائزنگ اور ایکسپوژر حدود نافذ کرتا ہے۔ کبھی ایسا سرمایہ نہ لگائیں جس کا نقصان آپ برداشت نہ کر سکیں۔</div>
                </details>
                <details>
                    <summary>پلانز میں کیا فرق ہے؟</summary>
                    <div class="a">Prototype پروٹوٹائپ انجن تک ایک مارکیٹ کی ابتدائی رسائی ہے۔ Founding Alpha بغیر بار بار فیس کے تاحیات مکمل رسائی ہے۔ Early Access وہی مکمل انجن ماہانہ بلنگ اور آزاد منسوخی کے ساتھ ہے۔ VIP Annual میں ترجیحی ایگزیکیوشن، مکمل API رسائی اور ترجیحی سپورٹ شامل ہیں۔</div>
                </details>
                <details>
                    <summary>پری آرڈر کے بعد کیا ہوتا ہے؟</summary>
                    <div class="a">آپ کو فوراً آرڈر کی تصدیق ملتی ہے، پھر لانچ ٹائم لائن کی اطلاعات اور آن بورڈنگ ہدایات ای میل سے آتی ہیں۔ فاؤنڈنگ ممبر عوامی دستیابی سے پہلے شامل ہوتے ہیں۔</div>
                </details>
                <details>
                    <summary>کیا مجھے رقم واپس مل سکتی ہے؟</summary>
                    <div class="a">جی ہاں — پری آرڈر لانچ سے پہلے کسی بھی وقت مکمل قابلِ واپسی ہیں۔ سپورٹ سے رابطہ کریں (تفصیل آپ کی خریداری کی رسید پر ہے) اور رقم واپس کر دی جائے گی۔ لانچ کے بعد ماہانہ اور سالانہ پاس کسی بھی وقت منسوخ کر کے آئندہ بلنگ روکی جا سکتی ہے۔ مکمل تفصیل ہماری <a href="/terms" style="color:var(--accent)">شرائطِ خدمت</a> میں (انگریزی میں)۔</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>فاؤنڈر قیمت لانچ پر ختم ہو جاتی ہے۔</h2>
            <p>اپنا پلان ابھی محفوظ کریں — انجن عوامی ہوتے ہی یہ قیمتیں مستقل ختم ہو جائیں گی۔</p>
            <a href="#pricing" class="btn primary">میرا پلان پری آرڈر کریں</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">طریقہ کار</a>
                    <a href="#strategy">حکمتِ عملی</a>
                    <a href="#pricing">قیمتیں</a>
                    <a href="#faq">سوالات</a>
                    <a href="/terms">شرائط</a>
                    <a href="/privacy">پرائیویسی</a>
                </div>
            </div>
            <p class="disclaimer">رسک ڈسکلوژر: ٹریڈنگ میں نقصان کا نمایاں خطرہ ہے اور یہ ہر سرمایہ کار کے لیے موزوں نہیں۔ الگورتھمک اور خودکار حکمتِ عملیاں پیسہ کھو سکتی ہیں اور کھوتی ہیں؛ ماضی یا سمولیٹڈ کارکردگی مستقبل کے نتائج کی ضمانت نہیں۔ ai PassiveAutotrades ایک سافٹ ویئر ٹول ہے — نہ سرمایہ کاری مشیر، نہ بروکر ڈیلر، نہ امین، اور اس ویب سائٹ پر کچھ بھی مالی مشورہ یا ٹریڈ کی دعوت نہیں۔ پری آرڈر خریداری اوپر بیان کردہ طریقے سے لانچ پر سافٹ ویئر رسائی دیتی ہے۔ صرف اتنا سرمایہ لگائیں جس کا نقصان آپ برداشت کر سکیں۔</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades۔ جملہ حقوق محفوظ ہیں۔</p>
        </div>
    </footer>
</body>
</html>
"""

HOMEPAGE_HTML_HI = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — स्वचालित Z-Score क्वांट ट्रेडिंग इंजन</title>
    <meta name="description" content="Z-Score मीन रिवर्ज़न पर आधारित पूर्णतः स्वचालित ट्रेडिंग इंजन। बिना हस्तक्षेप निष्पादन, बिल्ट-इन रिस्क कंट्रोल, और आपके फ़ंड कभी आपके अपने खाते से बाहर नहीं जाते। फ़ाउंडर एक्सेस अभी प्री-ऑर्डर करें।">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/hi">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/hi">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — संस्थागत आय, स्वचालित।">
    <meta property="og:description" content="चार्ट देखे बिना स्वचालित Z-Score क्वांट रणनीतियाँ। लॉन्च से पहले फ़ाउंडर एक्सेस प्री-ऑर्डर करें।">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="hi_IN">
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
                <a href="#how">कैसे काम करता है</a>
                <a href="#strategy">रणनीति</a>
                <a href="#pricing">क़ीमतें</a>
                <a href="#faq">प्रश्न</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><a href="/fr">FR</a><a href="/de">DE</a><a href="/pt">PT</a><a href="/ar">AR</a><a href="/fa">FA</a><a href="/ur">UR</a><span class="cur">HI</span><a href="/bn">BN</a><a href="/ta">TA</a></div>
            <a href="#pricing" class="nav-cta">एक्सेस प्री-ऑर्डर करें</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>स्वचालित Z-SCORE क्वांट इंजन</div>
                    <h1>संस्थागत आय,<br><span class="grad">स्वचालित।</span></h1>
                    <p class="hero-sub">Z-Score मीन रिवर्ज़न पर बना पूर्णतः स्वचालित ट्रेडिंग इंजन — वही सांख्यिकीय पद्धति जो क्वांट डेस्क अपनाते हैं — चौबीसों घंटे चलता है ताकि आपको कभी चार्ट न देखना पड़े।</p>
                    <div class="hero-note">फ़ाउंडर प्री-ऑर्डर — सार्वजनिक लॉन्च से पहले आजीवन क़ीमत लॉक करें</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">प्री-ऑर्डर प्लान देखें</a>
                        <a href="#how" class="btn ghost">कैसे काम करता है</a>
                    </div>
                    <div class="hero-foot">
                        <span>बिना हस्तक्षेप निष्पादन</span>
                        <span>बिल्ट-इन रिस्क कंट्रोल</span>
                        <span>कभी भी रद्द करने का विकल्प</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">ENGINE — SIGNAL MONITOR</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC–USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">ETH–USD</span><span class="z">z&nbsp;=&nbsp;−0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL–USD</span><span class="z">z&nbsp;=&nbsp;−2.87</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">XRP–USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risk ✓ &nbsp; sizing ✓ &nbsp; exposure ✓</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">उदाहरणात्मक सिग्नल फ़ीड — इंजन बाज़ार को ऐसे पढ़ता है</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>स्वायत्त बाज़ार कवरेज</span></div>
            <div class="stat"><b>ms</b><span>एल्गोरिथमिक निष्पादन गति</span></div>
            <div class="stat"><b>0</b><span>चार्ट जो आपको देखने हों</span></div>
            <div class="stat"><b>100%</b><span>नियम-आधारित — शून्य भावनाएँ</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">कैसे काम करता है</div>
            <div class="sec-head">
                <h2>तीन क़दम। फिर इंजन संभाल लेता है।</h2>
                <p>न सिग्नल ग्रुप, न स्क्रीन के घंटे, न मनमाने फ़ैसले। एक बार कॉन्फ़िगर होने पर हर एंट्री और एग्ज़िट व्यवस्थित है।</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>अपना प्लान सुरक्षित करें</h3>
                    <p>अपने लिए सही प्लान प्री-ऑर्डर करें। फ़ाउंडर क़ीमत स्थायी रूप से आपके खाते से जुड़ जाती है — लॉन्च के बाद यह दोबारा कभी नहीं मिलेगी।</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>जोड़ें और कॉन्फ़िगर करें</h3>
                    <p>लॉन्च पर इंजन को अपने एक्सचेंज खाते से जोड़ें और रिस्क पैरामीटर एक बार तय करें। आपके फ़ंड हर समय आपके अपने खाते में रहते हैं।</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>इंजन निष्पादित करता है</h3>
                    <p>Z-Score कोर चौबीसों घंटे सांख्यिकीय विचलन पर नज़र रखता है और एंट्री, एग्ज़िट व पोज़िशन साइज़िंग स्वतः करता है।</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">रणनीति</div>
                    <h2>Z-Score मीन रिवर्ज़न ही क्यों?</h2>
                    <p>बाज़ार अति-प्रतिक्रिया करते हैं। क़ीमतें अपने सांख्यिकीय औसत से दूर खिंच जाती हैं, और खिंची हुई क़ीमतें लौटने की प्रवृत्ति रखती हैं। Z-Score ठीक-ठीक मापता है कि क़ीमत कितनी खिंची है — मानक विचलनों में — और "यह ज़्यादा बढ़ा हुआ लगता है" को एक सटीक, परखने योग्य संख्या बना देता है।</p>
                    <ul class="checklist">
                        <li>एक परिभाषित सांख्यिकीय बढ़त पर ट्रेड — न इंडिकेटर, न अटकलें, न शोर</li>
                        <li>हर पोज़िशन नियम से खुलती-बंद होती है, जोखिम ट्रेड से पहले तय होता है</li>
                        <li>वही पद्धति-वर्ग जो संस्थागत स्टैट-आर्ब डेस्क दशकों से इस्तेमाल करते हैं</li>
                        <li>बनावट से ही भावना-रहित: इंजन न बदला लेता है, न FOMO करता है, न हिचकिचाता है</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">"जब क़ीमत अपने रोलिंग औसत से ±2 मानक विचलन से आगे निकल जाती है, इंजन एक रिवर्ज़न पोज़िशन तैयार करता है — और उसे बिना मानवीय हस्तक्षेप के अंजाम तक पहुँचाता है।"</div>
                    <div class="src">— ai PassiveAutotrades का मूल नियम, साफ़ शब्दों में। न ब्लैक बॉक्स, न रहस्यमय सिग्नल।</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">आपको क्या मिलता है</div>
            <div class="sec-head">
                <h2>ट्रेडिंग डेस्क की तरह निर्मित। प्रोडक्ट की तरह प्रदत्त।</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>Z-Score सिग्नल कोर</h3><p>रोलिंग-विंडो सांख्यिकीय विचलन हर सिग्नल चलाता है — पारदर्शी, परखने योग्य और सुसंगत।</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>मिलीसेकंड निष्पादन</h3><p>सीमाएँ पार होते ही सिग्नल एल्गोरिथम से चलते हैं — दिन, रात और सप्ताहांत।</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>कठोर जोखिम सीमाएँ</h3><p>प्रति-ट्रेड साइज़िंग, एक्सपोज़र कैप और स्वचालित एग्ज़िट हर पोज़िशन पर लागू।</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>आपके फ़ंड, आपका खाता</h3><p>इंजन आपके अपने एक्सचेंज खाते से जुड़ता है। पूँजी कभी हमें हस्तांतरित नहीं होती।</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>एक बार का सेटअप</h3><p>जोखिम स्तर और बाज़ार सिर्फ़ एक बार चुनें। न लगातार रखरखाव, न निगरानी।</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>API एक्सेस <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>कस्टम इंटीग्रेशन और मॉनिटरिंग के लिए इंजन तक पूर्ण प्रोग्रामेटिक पहुँच।</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">फ़ाउंडर प्री-ऑर्डर</div>
                <h2>लॉन्च से पहले अपना प्लान लॉक करें</h2>
                <p>हर प्लान फ़ाउंडर क़ीमत पर प्री-ऑर्डर है। इंजन लॉन्च होते ही फ़ाउंडिंग सदस्य सबसे पहले शामिल होते हैं — और ये क़ीमतें स्थायी रूप से हट जाती हैं।</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">प्री-ऑर्डर</span>
                    <h3>Prototype</h3>
                    <div class="who">एल्गो-ट्रेडिंग में नए लोगों के लिए</div>
                    <div class="price">$79.99</div>
                    <div class="per">एकमुश्त (US डॉलर)</div>
                    <ul>
                        <li>प्रोटोटाइप इंजन तक शुरुआती पहुँच</li>
                        <li>मूल Z-Score रणनीति, एक बाज़ार</li>
                        <li>मानक रिस्क कंट्रोल</li>
                        <li>ईमेल सपोर्ट</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Prototype पाएँ</a>
                </div>
                <div class="tier">
                    <span class="badge">प्री-ऑर्डर</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">दीर्घकालिक विश्वास रखने वालों के लिए</div>
                    <div class="price">$199.99</div>
                    <div class="per">एकमुश्त · आजीवन (US डॉलर)</div>
                    <ul>
                        <li>इंजन तक आजीवन पूर्ण पहुँच</li>
                        <li>सभी बाज़ार और अपडेट, हमेशा के लिए</li>
                        <li>कोई आवर्ती शुल्क नहीं, कभी नहीं</li>
                        <li>लॉन्च पर प्राथमिकता ऑनबोर्डिंग</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">आजीवन सुरक्षित करें</a>
                </div>
                <div class="tier">
                    <span class="badge">प्री-ऑर्डर</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">लचीलापन चाहने वालों के लिए</div>
                    <div class="price">$49.99</div>
                    <div class="per">प्रति माह (US डॉलर)</div>
                    <ul>
                        <li>इंजन की पूरी उपयोगिता</li>
                        <li>सभी बाज़ार शामिल</li>
                        <li>कभी भी रद्द करें</li>
                        <li>मानक सपोर्ट</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">मासिक सुरक्षित करें</a>
                </div>
                <div class="tier featured">
                    <span class="flag">सर्वश्रेष्ठ मूल्य</span>
                    <span class="badge">प्री-ऑर्डर</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">गंभीर ट्रेडरों के लिए</div>
                    <div class="price">$499.99</div>
                    <div class="per">प्रति वर्ष (US डॉलर)</div>
                    <ul>
                        <li>Early Access का सब कुछ</li>
                        <li>प्राथमिकता निष्पादन क़तार</li>
                        <li>पूर्ण API एक्सेस</li>
                        <li>प्राथमिकता सपोर्ट चैनल</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">वार्षिक सुरक्षित करें</a>
                </div>
            </div>
            <p class="pricing-note">Stripe से सुरक्षित भुगतान · USD, EUR, GBP, CAD या AUD में भुगतान करें — चेकआउट पर आपकी मुद्रा स्वतः पहचानी जाती है · फ़ाउंडर क़ीमतें सार्वजनिक लॉन्च पर स्थायी रूप से हट जाती हैं</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">प्रश्न</div>
                <h2>ख़रीदने से पहले पूछे जाने वाले सवाल</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>प्री-ऑर्डर से मैं वास्तव में क्या ख़रीद रहा हूँ?</summary>
                    <div class="a">आप सार्वजनिक लॉन्च से पहले फ़ाउंडर क़ीमत पर इंजन की पहुँच आरक्षित कर रहे हैं। आपका प्लान और क़ीमत स्थायी रूप से आपके खाते से जुड़ जाते हैं। इंजन लाइव होते ही फ़ाउंडिंग सदस्य सबसे पहले शामिल होते हैं, और लॉन्च की जानकारी चेकआउट पर इस्तेमाल किए गए ईमेल पर भेजी जाती है।</div>
                </details>
                <details>
                    <summary>क्या मेरे फ़ंड कभी मेरे नियंत्रण से बाहर जाते हैं?</summary>
                    <div class="a">नहीं। इंजन API कुंजियों से आपके अपने एक्सचेंज खाते से जुड़ता है — कुंजियाँ जिन्हें आप नियंत्रित करते हैं और कभी भी रद्द कर सकते हैं। हम कभी आपकी पूँजी अपने पास नहीं रखते, और निकासी अनुमतियाँ कभी आवश्यक नहीं होतीं।</div>
                </details>
                <details>
                    <summary>क्या मुझे ट्रेडिंग अनुभव चाहिए?</summary>
                    <div class="a">इंजन चलाने के लिए न चार्ट पढ़ना ज़रूरी है न ट्रेडिंग कौशल — कॉन्फ़िगरेशन एक बार का काम है। हाँ, पूँजी लगाने से पहले आपको समझना चाहिए कि हर ट्रेडिंग में नुक़सान का वास्तविक जोखिम होता है।</div>
                </details>
                <details>
                    <summary>क्या इंजन पैसा गँवा सकता है?</summary>
                    <div class="a">हाँ। इस प्रश्न का हर ईमानदार उत्तर हाँ है — कोई रणनीति हर ट्रेड नहीं जीतती, और मज़बूत ट्रेंड वाले बाज़ारों में मीन रिवर्ज़न जोखिम भरा है। ठीक इसीलिए इंजन हर ट्रेड पर पोज़िशन साइज़िंग और एक्सपोज़र सीमाएँ लागू करता है। कभी ऐसी पूँजी से ट्रेड न करें जिसे खोना आप सह न सकें।</div>
                </details>
                <details>
                    <summary>प्लानों में क्या अंतर है?</summary>
                    <div class="a">Prototype प्रोटोटाइप इंजन तक एक-बाज़ार की शुरुआती पहुँच है। Founding Alpha बिना आवर्ती शुल्क के आजीवन पूर्ण पहुँच है। Early Access वही पूर्ण इंजन मासिक बिलिंग और मुक्त रद्दीकरण के साथ है। VIP Annual में प्राथमिकता निष्पादन, पूर्ण API एक्सेस और प्राथमिकता सपोर्ट जुड़ते हैं।</div>
                </details>
                <details>
                    <summary>प्री-ऑर्डर के बाद क्या होता है?</summary>
                    <div class="a">आपको तुरंत ऑर्डर की पुष्टि मिलती है, फिर लॉन्च समय-सारणी की जानकारी और ऑनबोर्डिंग निर्देश ईमेल से आते हैं। फ़ाउंडिंग सदस्य सार्वजनिक उपलब्धता से पहले शामिल होते हैं।</div>
                </details>
                <details>
                    <summary>क्या मुझे रिफ़ंड मिल सकता है?</summary>
                    <div class="a">हाँ — प्री-ऑर्डर लॉन्च से पहले किसी भी समय पूर्ण रिफ़ंड योग्य हैं। सपोर्ट से संपर्क करें (विवरण आपकी ख़रीद रसीद पर है) और रिफ़ंड प्रोसेस कर दिया जाएगा। लॉन्च के बाद मासिक और वार्षिक पास कभी भी रद्द कर भविष्य की बिलिंग रोकी जा सकती है। पूरा विवरण हमारी <a href="/terms" style="color:var(--accent)">सेवा की शर्तों</a> में (अंग्रेज़ी में)।</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>फ़ाउंडर क़ीमत लॉन्च पर समाप्त हो जाती है।</h2>
            <p>अपना प्लान अभी आरक्षित करें — इंजन सार्वजनिक होते ही ये क़ीमतें स्थायी रूप से हट जाएँगी।</p>
            <a href="#pricing" class="btn primary">मेरा प्लान प्री-ऑर्डर करें</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">कैसे काम करता है</a>
                    <a href="#strategy">रणनीति</a>
                    <a href="#pricing">क़ीमतें</a>
                    <a href="#faq">प्रश्न</a>
                    <a href="/terms">शर्तें</a>
                    <a href="/privacy">गोपनीयता</a>
                </div>
            </div>
            <p class="disclaimer">जोखिम प्रकटीकरण: ट्रेडिंग में नुक़सान का पर्याप्त जोखिम है और यह हर निवेशक के लिए उपयुक्त नहीं है। एल्गोरिथमिक और स्वचालित रणनीतियाँ पैसा गँवा सकती हैं और गँवाती हैं; अतीत या सिम्युलेटेड प्रदर्शन भविष्य के परिणामों की गारंटी नहीं है। ai PassiveAutotrades एक सॉफ़्टवेयर टूल है — यह निवेश सलाहकार, ब्रोकर-डीलर या न्यासी नहीं है, और इस साइट पर कुछ भी वित्तीय सलाह या ट्रेड का आग्रह नहीं है। प्री-ऑर्डर ख़रीद ऊपर वर्णित अनुसार लॉन्च पर सॉफ़्टवेयर पहुँच देती है। केवल उतनी पूँजी से ट्रेड करें जिसे खोना आप सह सकें।</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. सर्वाधिकार सुरक्षित।</p>
        </div>
    </footer>
</body>
</html>
"""

HOMEPAGE_HTML_BN = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — স্বয়ংক্রিয় Z-Score কোয়ান্ট ট্রেডিং ইঞ্জিন</title>
    <meta name="description" content="Z-Score মিন রিভার্সনের উপর ভিত্তি করে সম্পূর্ণ স্বয়ংক্রিয় ট্রেডিং ইঞ্জিন। হস্তক্ষেপ ছাড়া এক্সিকিউশন, বিল্ট-ইন রিস্ক কন্ট্রোল, এবং আপনার ফান্ড কখনও আপনার নিজের অ্যাকাউন্ট ছেড়ে যায় না। প্রতিষ্ঠাতা অ্যাক্সেস এখনই প্রি-অর্ডার করুন।">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/bn">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/bn">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — প্রাতিষ্ঠানিক আয়, স্বয়ংক্রিয়।">
    <meta property="og:description" content="চার্ট না দেখে স্বয়ংক্রিয় Z-Score কোয়ান্ট কৌশল। লঞ্চের আগে প্রতিষ্ঠাতা অ্যাক্সেস প্রি-অর্ডার করুন।">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="bn_BD">
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
                <a href="#how">কীভাবে কাজ করে</a>
                <a href="#strategy">কৌশল</a>
                <a href="#pricing">মূল্য</a>
                <a href="#faq">প্রশ্ন</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><a href="/fr">FR</a><a href="/de">DE</a><a href="/pt">PT</a><a href="/ar">AR</a><a href="/fa">FA</a><a href="/ur">UR</a><a href="/hi">HI</a><span class="cur">BN</span><a href="/ta">TA</a></div>
            <a href="#pricing" class="nav-cta">অ্যাক্সেস প্রি-অর্ডার করুন</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>স্বয়ংক্রিয় Z-SCORE কোয়ান্ট ইঞ্জিন</div>
                    <h1>প্রাতিষ্ঠানিক আয়,<br><span class="grad">স্বয়ংক্রিয়।</span></h1>
                    <p class="hero-sub">Z-Score মিন রিভার্সনের উপর নির্মিত সম্পূর্ণ স্বয়ংক্রিয় ট্রেডিং ইঞ্জিন — কোয়ান্ট ডেস্কগুলি যে পরিসংখ্যানগত পদ্ধতি ব্যবহার করে সেটিই — চব্বিশ ঘণ্টা চলে যাতে আপনাকে আর কখনও চার্ট দেখতে না হয়।</p>
                    <div class="hero-note">প্রতিষ্ঠাতা প্রি-অর্ডার — পাবলিক লঞ্চের আগে আজীবন মূল্য লক করুন</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">প্রি-অর্ডার প্ল্যান দেখুন</a>
                        <a href="#how" class="btn ghost">কীভাবে কাজ করে</a>
                    </div>
                    <div class="hero-foot">
                        <span>হস্তক্ষেপ ছাড়া এক্সিকিউশন</span>
                        <span>বিল্ট-ইন রিস্ক কন্ট্রোল</span>
                        <span>যেকোনো সময় বাতিলের সুযোগ</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">ENGINE — SIGNAL MONITOR</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC–USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">ETH–USD</span><span class="z">z&nbsp;=&nbsp;−0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL–USD</span><span class="z">z&nbsp;=&nbsp;−2.87</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">XRP–USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risk ✓ &nbsp; sizing ✓ &nbsp; exposure ✓</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">উদাহরণমূলক সিগন্যাল ফিড — ইঞ্জিন বাজারকে এভাবে পড়ে</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>স্বাধীন বাজার কভারেজ</span></div>
            <div class="stat"><b>ms</b><span>অ্যালগরিদমিক এক্সিকিউশনের গতি</span></div>
            <div class="stat"><b>0</b><span>চার্ট যা আপনাকে দেখতে হবে</span></div>
            <div class="stat"><b>100%</b><span>নিয়মভিত্তিক — শূন্য আবেগ</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">কীভাবে কাজ করে</div>
            <div class="sec-head">
                <h2>তিনটি ধাপ। তারপর ইঞ্জিন দায়িত্ব নেয়।</h2>
                <p>কোনো সিগন্যাল গ্রুপ নেই, স্ক্রিনের সামনে ঘণ্টা নেই, খেয়ালখুশির সিদ্ধান্ত নেই। একবার কনফিগার হলে প্রতিটি এন্ট্রি ও এক্সিট নিয়মমাফিক।</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>আপনার প্ল্যান নিশ্চিত করুন</h3>
                    <p>আপনার উপযুক্ত প্ল্যানটি প্রি-অর্ডার করুন। প্রতিষ্ঠাতা মূল্য স্থায়ীভাবে আপনার অ্যাকাউন্টে লক হয়ে যায় — লঞ্চের পরে এটি আর কখনও দেওয়া হবে না।</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>সংযুক্ত করুন ও কনফিগার করুন</h3>
                    <p>লঞ্চে ইঞ্জিনটি আপনার এক্সচেঞ্জ অ্যাকাউন্টের সাথে যুক্ত করুন এবং একবারই রিস্ক প্যারামিটার ঠিক করুন। আপনার ফান্ড সবসময় আপনার নিজের অ্যাকাউন্টেই থাকে।</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>ইঞ্জিন এক্সিকিউট করে</h3>
                    <p>Z-Score কোর চব্বিশ ঘণ্টা পরিসংখ্যানগত বিচ্যুতি পর্যবেক্ষণ করে এবং এন্ট্রি, এক্সিট ও পজিশন সাইজিং স্বয়ংক্রিয়ভাবে সম্পন্ন করে।</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">কৌশল</div>
                    <h2>কেন Z-Score মিন রিভার্সন?</h2>
                    <p>বাজার অতিপ্রতিক্রিয়া করে। দাম তার পরিসংখ্যানগত গড় থেকে দূরে সরে যায়, আর টানটান দাম ফিরে আসার প্রবণতা রাখে। Z-Score ঠিক মাপে দাম কতটা সরেছে — স্ট্যান্ডার্ড ডেভিয়েশনে — ফলে "এটা অতিরিক্ত মনে হচ্ছে" পরিণত হয় একটি নির্ভুল, যাচাইযোগ্য সংখ্যায়।</p>
                    <ul class="checklist">
                        <li>একটি সংজ্ঞায়িত পরিসংখ্যানগত সুবিধায় ট্রেড — ইন্ডিকেটর, অনুমান বা হাইপ নয়</li>
                        <li>প্রতিটি পজিশন নিয়ম মেনে খোলে ও বন্ধ হয়, ঝুঁকি ট্রেডের আগেই নির্ধারিত</li>
                        <li>প্রাতিষ্ঠানিক স্ট্যাট-আর্ব ডেস্কগুলি দশকের পর দশক এই শ্রেণির পদ্ধতিই ব্যবহার করে</li>
                        <li>গঠনগতভাবেই আবেগহীন: ইঞ্জিন প্রতিশোধ নেয় না, FOMO করে না, দ্বিধা করে না</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">"দাম যখন তার রোলিং গড় থেকে ±২ স্ট্যান্ডার্ড ডেভিয়েশনের বেশি সরে যায়, ইঞ্জিন একটি রিভার্সন পজিশন প্রস্তুত করে — এবং মানুষের হস্তক্ষেপ ছাড়াই তা শেষ পর্যন্ত পরিচালনা করে।"</div>
                    <div class="src">— ai PassiveAutotrades-এর মূল নিয়ম, সরল ভাষায়। কোনো ব্ল্যাক বক্স নেই, রহস্যময় সিগন্যাল নেই।</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">আপনি যা পাবেন</div>
            <div class="sec-head">
                <h2>ট্রেডিং ডেস্কের মতো নির্মিত। প্রোডাক্টের মতো সরবরাহকৃত।</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>Z-Score সিগন্যাল কোর</h3><p>রোলিং-উইন্ডো পরিসংখ্যানগত বিচ্যুতি প্রতিটি সিগন্যাল চালায় — স্বচ্ছ, যাচাইযোগ্য ও সামঞ্জস্যপূর্ণ।</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>মিলিসেকেন্ডে এক্সিকিউশন</h3><p>সীমা অতিক্রম করা মাত্র সিগন্যাল অ্যালগরিদমে চলে — দিন, রাত, সাপ্তাহিক ছুটি।</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>কঠোর ঝুঁকি সীমা</h3><p>প্রতি-ট্রেড সাইজিং, এক্সপোজার সীমা ও স্বয়ংক্রিয় এক্সিট প্রতিটি পজিশনে প্রযোজ্য।</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>আপনার ফান্ড, আপনার অ্যাকাউন্ট</h3><p>ইঞ্জিন আপনার নিজের এক্সচেঞ্জ অ্যাকাউন্টের সাথে যুক্ত হয়। মূলধন কখনও আমাদের কাছে যায় না।</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>একবারের সেটআপ</h3><p>ঝুঁকির মাত্রা ও বাজার একবারই বেছে নিন। চলমান রক্ষণাবেক্ষণ বা নজরদারি নেই।</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>API অ্যাক্সেস <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>কাস্টম ইন্টিগ্রেশন ও মনিটরিংয়ের জন্য ইঞ্জিনে সম্পূর্ণ প্রোগ্রাম্যাটিক অ্যাক্সেস।</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">প্রতিষ্ঠাতা প্রি-অর্ডার</div>
                <h2>লঞ্চের আগে আপনার প্ল্যান লক করুন</h2>
                <p>প্রতিটি প্ল্যান প্রতিষ্ঠাতা মূল্যে প্রি-অর্ডার। ইঞ্জিন লঞ্চ হলে প্রতিষ্ঠাতা সদস্যরা আগে যুক্ত হন — এবং এই মূল্যগুলি স্থায়ীভাবে তুলে নেওয়া হয়।</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">প্রি-অর্ডার</span>
                    <h3>Prototype</h3>
                    <div class="who">অ্যালগো-ট্রেডিংয়ে নতুনদের জন্য</div>
                    <div class="price">$79.99</div>
                    <div class="per">এককালীন (মার্কিন ডলার)</div>
                    <ul>
                        <li>প্রোটোটাইপ ইঞ্জিনে প্রাথমিক অ্যাক্সেস</li>
                        <li>মূল Z-Score কৌশল, একটি বাজার</li>
                        <li>স্ট্যান্ডার্ড রিস্ক কন্ট্রোল</li>
                        <li>ইমেইল সাপোর্ট</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Prototype নিন</a>
                </div>
                <div class="tier">
                    <span class="badge">প্রি-অর্ডার</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">দীর্ঘমেয়াদে বিশ্বাসীদের জন্য</div>
                    <div class="price">$199.99</div>
                    <div class="per">এককালীন · আজীবন (মার্কিন ডলার)</div>
                    <ul>
                        <li>ইঞ্জিনে আজীবন সম্পূর্ণ অ্যাক্সেস</li>
                        <li>সব বাজার ও কৌশল আপডেট, চিরকাল</li>
                        <li>কোনো পুনরাবৃত্ত ফি নেই, কখনও না</li>
                        <li>লঞ্চে অগ্রাধিকার অনবোর্ডিং</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">আজীবন নিশ্চিত করুন</a>
                </div>
                <div class="tier">
                    <span class="badge">প্রি-অর্ডার</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">নমনীয়তা পছন্দকারীদের জন্য</div>
                    <div class="price">$49.99</div>
                    <div class="per">প্রতি মাসে (মার্কিন ডলার)</div>
                    <ul>
                        <li>ইঞ্জিনের সম্পূর্ণ সুবিধা</li>
                        <li>সব বাজার অন্তর্ভুক্ত</li>
                        <li>যেকোনো সময় বাতিল করুন</li>
                        <li>স্ট্যান্ডার্ড সাপোর্ট</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">মাসিক নিশ্চিত করুন</a>
                </div>
                <div class="tier featured">
                    <span class="flag">সেরা মূল্য</span>
                    <span class="badge">প্রি-অর্ডার</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">গুরুতর ট্রেডারদের জন্য</div>
                    <div class="price">$499.99</div>
                    <div class="per">প্রতি বছরে (মার্কিন ডলার)</div>
                    <ul>
                        <li>Early Access-এর সবকিছু</li>
                        <li>অগ্রাধিকার এক্সিকিউশন সারি</li>
                        <li>সম্পূর্ণ API অ্যাক্সেস</li>
                        <li>অগ্রাধিকার সাপোর্ট চ্যানেল</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">বার্ষিক নিশ্চিত করুন</a>
                </div>
            </div>
            <p class="pricing-note">Stripe-এর মাধ্যমে নিরাপদ পেমেন্ট · USD, EUR, GBP, CAD বা AUD-তে পরিশোধ করুন — চেকআউটে আপনার মুদ্রা স্বয়ংক্রিয়ভাবে শনাক্ত হয় · পাবলিক লঞ্চে প্রতিষ্ঠাতা মূল্য স্থায়ীভাবে তুলে নেওয়া হয়</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">প্রশ্ন</div>
                <h2>কেনার আগে যা জিজ্ঞাসা করা হয়</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>প্রি-অর্ডারে আমি আসলে কী কিনছি?</summary>
                    <div class="a">আপনি পাবলিক লঞ্চের আগে প্রতিষ্ঠাতা মূল্যে ইঞ্জিনের অ্যাক্সেস সংরক্ষণ করছেন। আপনার প্ল্যান ও মূল্য স্থায়ীভাবে আপনার অ্যাকাউন্টে লক হয়। ইঞ্জিন চালু হলে প্রতিষ্ঠাতা সদস্যরা আগে যুক্ত হন, আর লঞ্চের খবর চেকআউটে ব্যবহৃত ইমেইলে পাঠানো হয়।</div>
                </details>
                <details>
                    <summary>আমার ফান্ড কি কখনও আমার নিয়ন্ত্রণের বাইরে যায়?</summary>
                    <div class="a">না। ইঞ্জিন API কী-র মাধ্যমে আপনার নিজের এক্সচেঞ্জ অ্যাকাউন্টের সাথে যুক্ত হয় — কী যা আপনি নিয়ন্ত্রণ করেন এবং যেকোনো সময় বাতিল করতে পারেন। আমরা কখনও আপনার মূলধন রাখি না, এবং উত্তোলনের অনুমতি কখনও প্রয়োজন হয় না।</div>
                </details>
                <details>
                    <summary>আমার কি ট্রেডিং অভিজ্ঞতা দরকার?</summary>
                    <div class="a">ইঞ্জিন চালাতে চার্ট পড়া বা ট্রেডিং দক্ষতা লাগে না — কনফিগারেশন একবারের কাজ। তবে মূলধন বিনিয়োগের আগে বুঝতে হবে যে প্রতিটি ট্রেডিংয়ে প্রকৃত ক্ষতির ঝুঁকি থাকে।</div>
                </details>
                <details>
                    <summary>ইঞ্জিন কি টাকা হারাতে পারে?</summary>
                    <div class="a">হ্যাঁ। এই প্রশ্নের প্রতিটি সৎ উত্তরই হ্যাঁ — কোনো কৌশল প্রতিটি ট্রেড জেতে না, আর শক্তিশালী ট্রেন্ডের বাজারে মিন রিভার্সনের ঝুঁকি আছে। ঠিক এই কারণেই ইঞ্জিন প্রতিটি ট্রেডে পজিশন সাইজিং ও এক্সপোজার সীমা প্রয়োগ করে। এমন মূলধন দিয়ে কখনও ট্রেড করবেন না যা হারানোর সামর্থ্য আপনার নেই।</div>
                </details>
                <details>
                    <summary>প্ল্যানগুলির মধ্যে পার্থক্য কী?</summary>
                    <div class="a">Prototype হলো প্রোটোটাইপ ইঞ্জিনে এক-বাজারের প্রাথমিক অ্যাক্সেস। Founding Alpha হলো পুনরাবৃত্ত ফি ছাড়া আজীবন সম্পূর্ণ অ্যাক্সেস। Early Access একই সম্পূর্ণ ইঞ্জিন, মাসিক বিলিং ও স্বাধীন বাতিলসহ। VIP Annual যোগ করে অগ্রাধিকার এক্সিকিউশন, সম্পূর্ণ API অ্যাক্সেস ও অগ্রাধিকার সাপোর্ট।</div>
                </details>
                <details>
                    <summary>প্রি-অর্ডারের পরে কী হয়?</summary>
                    <div class="a">আপনি সাথে সাথে অর্ডার নিশ্চিতকরণ পাবেন, তারপর ইমেইলে লঞ্চ সময়সূচির খবর ও অনবোর্ডিং নির্দেশনা। প্রতিষ্ঠাতা সদস্যরা পাবলিক প্রাপ্যতার আগে যুক্ত হন।</div>
                </details>
                <details>
                    <summary>আমি কি রিফান্ড পেতে পারি?</summary>
                    <div class="a">হ্যাঁ — লঞ্চের আগে যেকোনো সময় প্রি-অর্ডার সম্পূর্ণ ফেরতযোগ্য। সাপোর্টে যোগাযোগ করুন (বিস্তারিত আপনার ক্রয় রসিদে) এবং রিফান্ড প্রক্রিয়া করা হবে। লঞ্চের পরে মাসিক ও বার্ষিক পাস যেকোনো সময় বাতিল করে ভবিষ্যৎ বিলিং বন্ধ করা যায়। সম্পূর্ণ বিবরণ আমাদের <a href="/terms" style="color:var(--accent)">সেবার শর্তাবলিতে</a> (ইংরেজিতে)।</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>প্রতিষ্ঠাতা মূল্য লঞ্চেই শেষ।</h2>
            <p>এখনই আপনার প্ল্যান সংরক্ষণ করুন — ইঞ্জিন পাবলিক হলে এই মূল্যগুলি স্থায়ীভাবে তুলে নেওয়া হবে।</p>
            <a href="#pricing" class="btn primary">আমার প্ল্যান প্রি-অর্ডার করুন</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">কীভাবে কাজ করে</a>
                    <a href="#strategy">কৌশল</a>
                    <a href="#pricing">মূল্য</a>
                    <a href="#faq">প্রশ্ন</a>
                    <a href="/terms">শর্তাবলি</a>
                    <a href="/privacy">গোপনীয়তা</a>
                </div>
            </div>
            <p class="disclaimer">ঝুঁকি প্রকাশ: ট্রেডিংয়ে উল্লেখযোগ্য ক্ষতির ঝুঁকি রয়েছে এবং এটি সব বিনিয়োগকারীর জন্য উপযুক্ত নয়। অ্যালগরিদমিক ও স্বয়ংক্রিয় কৌশল অর্থ হারাতে পারে এবং হারায়ও; অতীত বা সিমুলেটেড পারফরম্যান্স ভবিষ্যৎ ফলাফলের নিশ্চয়তা দেয় না। ai PassiveAutotrades একটি সফটওয়্যার টুল — এটি বিনিয়োগ উপদেষ্টা, ব্রোকার-ডিলার বা ট্রাস্টি নয়, এবং এই সাইটের কিছুই আর্থিক পরামর্শ বা ট্রেডের আমন্ত্রণ নয়। প্রি-অর্ডার ক্রয় উপরে বর্ণিত অনুযায়ী লঞ্চে সফটওয়্যার অ্যাক্সেস দেয়। শুধু সেই মূলধন দিয়ে ট্রেড করুন যা হারানোর সামর্থ্য আপনার আছে।</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. সর্বস্বত্ব সংরক্ষিত।</p>
        </div>
    </footer>
</body>
</html>
"""

HOMEPAGE_HTML_TA = """
<!DOCTYPE html>
<html lang="ta">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades — தானியங்கி Z-Score குவாண்ட் டிரேடிங் இன்ஜின்</title>
    <meta name="description" content="Z-Score சராசரி மீட்சியை அடிப்படையாகக் கொண்ட முழு தானியங்கி டிரேடிங் இன்ஜின். தலையீடின்றி செயலாக்கம், உள்ளமைந்த ரிஸ்க் கட்டுப்பாடுகள், உங்கள் நிதி உங்கள் சொந்தக் கணக்கை விட்டு வெளியேறாது. நிறுவனர் அணுகலை இப்போதே முன்பதிவு செய்யுங்கள்.">
    <link rel="canonical" href="https://aipassiveautotrades.vercel.app/ta">
""" + HREFLANG_LINKS + """
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#050608">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://aipassiveautotrades.vercel.app/ta">
    <meta property="og:site_name" content="ai PassiveAutotrades">
    <meta property="og:title" content="ai PassiveAutotrades — நிறுவன வருமானம், தானியங்கி.">
    <meta property="og:description" content="வரைபடங்களைப் பார்க்காமல் தானியங்கி Z-Score குவாண்ட் உத்திகள். வெளியீட்டுக்கு முன் நிறுவனர் அணுகலை முன்பதிவு செய்யுங்கள்.">
    <meta property="og:image" content="https://aipassiveautotrades.vercel.app/og.png">
    <meta property="og:locale" content="ta_IN">
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
                <a href="#how">எப்படி வேலை செய்கிறது</a>
                <a href="#strategy">உத்தி</a>
                <a href="#pricing">விலைகள்</a>
                <a href="#faq">கேள்விகள்</a>
            </div>
            <div class="lang"><a href="/">EN</a><a href="/es">ES</a><a href="/fr">FR</a><a href="/de">DE</a><a href="/pt">PT</a><a href="/ar">AR</a><a href="/fa">FA</a><a href="/ur">UR</a><a href="/hi">HI</a><a href="/bn">BN</a><span class="cur">TA</span></div>
            <a href="#pricing" class="nav-cta">அணுகலை முன்பதிவு செய்</a>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap">
            <div class="hero-grid">
                <div>
                    <div class="eyebrow"><span class="dot"></span>தானியங்கி Z-SCORE குவாண்ட் இன்ஜின்</div>
                    <h1>நிறுவன வருமானம்,<br><span class="grad">தானியங்கி.</span></h1>
                    <p class="hero-sub">Z-Score சராசரி மீட்சியில் கட்டப்பட்ட முழு தானியங்கி டிரேடிங் இன்ஜின் — குவாண்ட் டெஸ்க்குகள் பயன்படுத்தும் அதே புள்ளியியல் முறை — இரவு பகலாக இயங்குகிறது, நீங்கள் இனி வரைபடங்களைப் பார்க்கத் தேவையில்லை.</p>
                    <div class="hero-note">நிறுவனர் முன்பதிவு — பொது வெளியீட்டுக்கு முன் வாழ்நாள் விலையைப் பூட்டுங்கள்</div>
                    <div class="cta-row">
                        <a href="#pricing" class="btn primary">முன்பதிவுத் திட்டங்களைக் காண</a>
                        <a href="#how" class="btn ghost">எப்படி வேலை செய்கிறது</a>
                    </div>
                    <div class="hero-foot">
                        <span>தலையீடின்றி செயலாக்கம்</span>
                        <span>உள்ளமைந்த ரிஸ்க் கட்டுப்பாடுகள்</span>
                        <span>எப்போது வேண்டுமானாலும் ரத்து</span>
                    </div>
                </div>
                <div>
                    <div class="console mono">
                        <div class="console-bar">
                            <div class="dots"><i></i><i></i><i></i></div>
                            <span class="title">ENGINE — SIGNAL MONITOR</span>
                        </div>
                        <div class="console-body">
                            <div class="crow"><span class="pair">BTC–USD</span><span class="z">z&nbsp;=&nbsp;+2.31</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">ETH–USD</span><span class="z">z&nbsp;=&nbsp;−0.42</span><span class="sig idle">IN BAND</span></div>
                            <div class="crow"><span class="pair">SOL–USD</span><span class="z">z&nbsp;=&nbsp;−2.87</span><span class="sig armed">REVERT · ARMED</span></div>
                            <div class="crow"><span class="pair">XRP–USD</span><span class="z">z&nbsp;=&nbsp;+0.96</span><span class="sig idle">IN BAND</span></div>
                        </div>
                        <div class="console-foot">
                            <span>risk ✓ &nbsp; sizing ✓ &nbsp; exposure ✓</span>
                            <span>24/7</span>
                        </div>
                    </div>
                    <div class="console-caption">எடுத்துக்காட்டு சிக்னல் ஃபீட் — இன்ஜின் சந்தையை இப்படிப் படிக்கிறது</div>
                </div>
            </div>
        </div>
    </header>

    <div class="strip">
        <div class="strip-inner">
            <div class="stat"><b>24/7</b><span>தன்னாட்சி சந்தைக் கண்காணிப்பு</span></div>
            <div class="stat"><b>ms</b><span>அல்காரிதம் செயலாக்க வேகம்</span></div>
            <div class="stat"><b>0</b><span>நீங்கள் பார்க்க வேண்டிய வரைபடங்கள்</span></div>
            <div class="stat"><b>100%</b><span>விதிமுறை அடிப்படை — உணர்ச்சி இல்லை</span></div>
        </div>
    </div>

    <section id="how">
        <div class="wrap">
            <div class="sec-label">எப்படி வேலை செய்கிறது</div>
            <div class="sec-head">
                <h2>மூன்று படிகள். பிறகு இன்ஜின் பொறுப்பேற்கிறது.</h2>
                <p>சிக்னல் குழுக்கள் இல்லை, திரை நேரம் இல்லை, மனம்போன போக்கில் முடிவுகள் இல்லை. ஒருமுறை அமைத்தபின், ஒவ்வொரு நுழைவும் வெளியேற்றமும் முறைப்படி நடக்கிறது.</p>
            </div>
            <div class="steps">
                <div class="step">
                    <span class="num">01</span>
                    <h3>உங்கள் திட்டத்தை உறுதி செய்யுங்கள்</h3>
                    <p>உங்களுக்கு ஏற்ற திட்டத்தை முன்பதிவு செய்யுங்கள். நிறுவனர் விலை உங்கள் கணக்கில் நிரந்தரமாகப் பூட்டப்படும் — வெளியீட்டுக்குப் பிறகு அது மீண்டும் வழங்கப்படாது.</p>
                </div>
                <div class="step">
                    <span class="num">02</span>
                    <h3>இணைத்து அமையுங்கள்</h3>
                    <p>வெளியீட்டின்போது இன்ஜினை உங்கள் எக்ஸ்சேஞ்ச் கணக்குடன் இணைத்து, ரிஸ்க் அளவுருக்களை ஒருமுறை அமையுங்கள். உங்கள் நிதி எப்போதும் உங்கள் சொந்தக் கணக்கிலேயே இருக்கும்.</p>
                </div>
                <div class="step">
                    <span class="num">03</span>
                    <h3>இன்ஜின் செயல்படுத்துகிறது</h3>
                    <p>Z-Score மையம் புள்ளியியல் விலகலை இரவு பகலாகக் கண்காணித்து, நுழைவு, வெளியேற்றம், பொசிஷன் அளவை தானாகவே செயல்படுத்துகிறது.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="strategy" class="alt">
        <div class="wrap">
            <div class="split">
                <div class="sec-head">
                    <div class="sec-label">உத்தி</div>
                    <h2>ஏன் Z-Score சராசரி மீட்சி?</h2>
                    <p>சந்தைகள் மிகைத் தூண்டுதலுக்கு உள்ளாகின்றன. விலைகள் தம் புள்ளியியல் சராசரியிலிருந்து விலகிச் செல்கின்றன; இழுபட்ட விலைகள் திரும்பும் போக்கு கொண்டவை. விலை எவ்வளவு இழுபட்டுள்ளது என்பதை Z-Score துல்லியமாக அளக்கிறது — நியம விலகல்களில் — "இது அதிகமாகத் தெரிகிறது" என்பதைத் துல்லியமான, சரிபார்க்கக்கூடிய எண்ணாக மாற்றுகிறது.</p>
                    <ul class="checklist">
                        <li>வரையறுக்கப்பட்ட புள்ளியியல் அனுகூலத்தில் வர்த்தகம் — காட்டிகள், ஊகங்கள், பரபரப்பு அல்ல</li>
                        <li>ஒவ்வொரு பொசிஷனும் விதிப்படி திறந்து மூடப்படுகிறது; ரிஸ்க் வர்த்தகத்துக்கு முன்பே அளவிடப்படுகிறது</li>
                        <li>நிறுவன ஸ்டேட்-ஆர்ப் டெஸ்க்குகள் பல தசாப்தங்களாகப் பயன்படுத்தும் அதே முறை வகை</li>
                        <li>வடிவமைப்பிலேயே உணர்ச்சியற்றது: இன்ஜினுக்கு பழிவாங்கலோ, FOMO-வோ, தயக்கமோ இல்லை</li>
                    </ul>
                </div>
                <div class="quote-box">
                    <div class="big">"விலை தனது நகரும் சராசரியிலிருந்து ±2 நியம விலகல்களுக்கு மேல் விலகும்போது, இன்ஜின் ஒரு மீட்சி பொசிஷனைத் தயார்படுத்துகிறது — மனிதத் தலையீடின்றி இறுதிவரை நிர்வகிக்கிறது."</div>
                    <div class="src">— ai PassiveAutotrades-இன் மையவிதி, தெளிவாகச் சொல்லப்பட்டது. கறுப்புப் பெட்டி இல்லை, மர்மச் சிக்னல்கள் இல்லை.</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="wrap">
            <div class="sec-label">நீங்கள் பெறுவது</div>
            <div class="sec-head">
                <h2>டிரேடிங் டெஸ்க் போலக் கட்டப்பட்டது. தயாரிப்பு போல வழங்கப்படுகிறது.</h2>
            </div>
            <div class="grid-6">
                <div class="cell"><span class="ic">&#128202;</span><h3>Z-Score சிக்னல் மையம்</h3><p>நகரும்-சாளர புள்ளியியல் விலகல் ஒவ்வொரு சிக்னலையும் இயக்குகிறது — வெளிப்படை, சரிபார்க்கக்கூடியது, சீரானது.</p></div>
                <div class="cell"><span class="ic">&#9889;</span><h3>மில்லி வினாடி செயலாக்கம்</h3><p>வரம்புகள் தாண்டியதும் சிக்னல்கள் அல்காரிதப்படி இயங்கும் — பகல், இரவு, வார இறுதி.</p></div>
                <div class="cell"><span class="ic">&#128737;&#65039;</span><h3>கடுமையான ரிஸ்க் வரம்புகள்</h3><p>ஒவ்வொரு வர்த்தக அளவு, எக்ஸ்போஷர் உச்சவரம்பு, தானியங்கி வெளியேற்றம் — ஒவ்வொரு பொசிஷனிலும் அமல்.</p></div>
                <div class="cell"><span class="ic">&#128273;</span><h3>உங்கள் நிதி, உங்கள் கணக்கு</h3><p>இன்ஜின் உங்கள் சொந்த எக்ஸ்சேஞ்ச் கணக்குடன் இணைகிறது. மூலதனம் எங்களுக்கு ஒருபோதும் மாற்றப்படாது.</p></div>
                <div class="cell"><span class="ic">&#128295;</span><h3>ஒருமுறை அமைப்பு</h3><p>ரிஸ்க் நிலையையும் சந்தைகளையும் ஒருமுறை மட்டும் தேர்வு செய்யுங்கள். தொடர் பராமரிப்போ கண்காணிப்போ இல்லை.</p></div>
                <div class="cell"><span class="ic">&#128225;</span><h3>API அணுகல் <span style="color:var(--faint);font-weight:400;font-size:0.75rem">(VIP)</span></h3><p>தனிப்பயன் ஒருங்கிணைப்பு மற்றும் கண்காணிப்புக்கான முழு நிரலாக்க அணுகல்.</p></div>
            </div>
        </div>
    </section>

    <section id="pricing" class="alt">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">நிறுவனர் முன்பதிவு</div>
                <h2>வெளியீட்டுக்கு முன் உங்கள் திட்டத்தைப் பூட்டுங்கள்</h2>
                <p>ஒவ்வொரு திட்டமும் நிறுவனர் விலையிலான முன்பதிவு. இன்ஜின் வெளியாகும்போது நிறுவனர் உறுப்பினர்கள் முதலில் இணைவார்கள் — இந்த விலைகள் நிரந்தரமாக விலக்கப்படும்.</p>
            </div>
            <div class="tiers">
                <div class="tier">
                    <span class="badge">முன்பதிவு</span>
                    <h3>Prototype</h3>
                    <div class="who">அல்கோ டிரேடிங் புதியவர்களுக்கு</div>
                    <div class="price">$79.99</div>
                    <div class="per">ஒருமுறை (அமெரிக்க டாலர்)</div>
                    <ul>
                        <li>ப்ரோட்டோடைப் இன்ஜினுக்கு ஆரம்ப அணுகல்</li>
                        <li>அடிப்படை Z-Score உத்தி, ஒரு சந்தை</li>
                        <li>நிலையான ரிஸ்க் கட்டுப்பாடுகள்</li>
                        <li>மின்னஞ்சல் ஆதரவு</li>
                    </ul>
                    <a href="https://buy.stripe.com/9B6aEWcdX0xO16Z0l4d3i00" class="btn primary">Prototype பெறுங்கள்</a>
                </div>
                <div class="tier">
                    <span class="badge">முன்பதிவு</span>
                    <h3>Founding Alpha</h3>
                    <div class="who">நீண்டகால நம்பிக்கையாளர்களுக்கு</div>
                    <div class="price">$199.99</div>
                    <div class="per">ஒருமுறை · வாழ்நாள் (அமெரிக்க டாலர்)</div>
                    <ul>
                        <li>இன்ஜினுக்கு வாழ்நாள் முழு அணுகல்</li>
                        <li>அனைத்து சந்தைகளும் மேம்பாடுகளும், என்றென்றும்</li>
                        <li>தொடர் கட்டணங்கள் இல்லவே இல்லை</li>
                        <li>வெளியீட்டில் முன்னுரிமை இணைப்பு</li>
                    </ul>
                    <a href="https://buy.stripe.com/3cIdR80vfa8odTL0l4d3i01" class="btn primary">வாழ்நாளை உறுதி செய்</a>
                </div>
                <div class="tier">
                    <span class="badge">முன்பதிவு</span>
                    <h3>Early Access Pass</h3>
                    <div class="who">நெகிழ்வு விரும்புவோருக்கு</div>
                    <div class="price">$49.99</div>
                    <div class="per">மாதத்திற்கு (அமெரிக்க டாலர்)</div>
                    <ul>
                        <li>இன்ஜினின் முழுப் பயன்</li>
                        <li>அனைத்து சந்தைகளும் உள்ளடக்கம்</li>
                        <li>எப்போது வேண்டுமானாலும் ரத்து</li>
                        <li>நிலையான ஆதரவு</li>
                    </ul>
                    <a href="https://buy.stripe.com/00wcN4di180geXP9VEd3i02" class="btn ghost">மாதாந்திரம் உறுதி செய்</a>
                </div>
                <div class="tier featured">
                    <span class="flag">சிறந்த மதிப்பு</span>
                    <span class="badge">முன்பதிவு</span>
                    <h3>VIP Annual Pass</h3>
                    <div class="who">தீவிர டிரேடர்களுக்கு</div>
                    <div class="price">$499.99</div>
                    <div class="per">ஆண்டுக்கு (அமெரிக்க டாலர்)</div>
                    <ul>
                        <li>Early Access-இன் அனைத்தும்</li>
                        <li>முன்னுரிமை செயலாக்க வரிசை</li>
                        <li>முழு API அணுகல்</li>
                        <li>முன்னுரிமை ஆதரவு சேனல்</li>
                    </ul>
                    <a href="https://buy.stripe.com/5kQ7sKguddkAcPH9VEd3i03" class="btn primary">ஆண்டுத் திட்டத்தை உறுதி செய்</a>
                </div>
            </div>
            <p class="pricing-note">Stripe மூலம் பாதுகாப்பான கட்டணம் · USD, EUR, GBP, CAD அல்லது AUD-இல் செலுத்துங்கள் — செக்அவுட்டில் உங்கள் நாணயம் தானாகக் கண்டறியப்படும் · பொது வெளியீட்டில் நிறுவனர் விலைகள் நிரந்தரமாக விலக்கப்படும்</p>
        </div>
    </section>

    <section id="faq">
        <div class="wrap">
            <div class="sec-head center">
                <div class="sec-label">கேள்விகள்</div>
                <h2>வாங்கும் முன் கேட்கப்படுவது</h2>
            </div>
            <div class="faq">
                <details>
                    <summary>முன்பதிவில் நான் சரியாக என்ன வாங்குகிறேன்?</summary>
                    <div class="a">பொது வெளியீட்டுக்கு முன் நிறுவனர் விலையில் இன்ஜின் அணுகலை நீங்கள் முன்பதிவு செய்கிறீர்கள். உங்கள் திட்டமும் விலையும் உங்கள் கணக்கில் நிரந்தரமாகப் பூட்டப்படும். இன்ஜின் இயங்கத் தொடங்கியதும் நிறுவனர் உறுப்பினர்கள் முதலில் இணைக்கப்படுவார்கள்; வெளியீட்டுத் தகவல்கள் செக்அவுட்டில் பயன்படுத்திய மின்னஞ்சலுக்கு அனுப்பப்படும்.</div>
                </details>
                <details>
                    <summary>என் நிதி எப்போதாவது என் கட்டுப்பாட்டை விட்டு வெளியேறுமா?</summary>
                    <div class="a">இல்லை. நீங்கள் கட்டுப்படுத்தும், எப்போது வேண்டுமானாலும் ரத்து செய்யக்கூடிய API விசைகள் மூலம் இன்ஜின் உங்கள் சொந்த எக்ஸ்சேஞ்ச் கணக்குடன் இணைகிறது. உங்கள் மூலதனத்தை நாங்கள் ஒருபோதும் வைத்திருக்க மாட்டோம்; பணமெடுப்பு அனுமதிகள் ஒருபோதும் தேவையில்லை.</div>
                </details>
                <details>
                    <summary>எனக்கு டிரேடிங் அனுபவம் தேவையா?</summary>
                    <div class="a">இன்ஜினை இயக்க வரைபடம் படிக்கவோ டிரேடிங் திறமையோ தேவையில்லை — அமைப்பு ஒருமுறை மட்டுமே. இருப்பினும், மூலதனத்தை ஈடுபடுத்தும் முன் ஒவ்வொரு வர்த்தகத்திலும் உண்மையான இழப்பு அபாயம் உள்ளது என்பதைப் புரிந்து கொள்ள வேண்டும்.</div>
                </details>
                <details>
                    <summary>இன்ஜின் பணத்தை இழக்க முடியுமா?</summary>
                    <div class="a">ஆம். இந்தக் கேள்விக்கான ஒவ்வொரு நேர்மையான பதிலும் ஆம் — எந்த உத்தியும் ஒவ்வொரு வர்த்தகத்திலும் வெல்வதில்லை; வலுவான போக்குள்ள சந்தைகளில் சராசரி மீட்சிக்கு அபாயம் உண்டு. அதனால்தான் இன்ஜின் ஒவ்வொரு வர்த்தகத்திலும் பொசிஷன் அளவையும் எக்ஸ்போஷர் வரம்புகளையும் கட்டாயமாக்குகிறது. இழக்கச் சகிக்க முடியாத மூலதனத்தில் ஒருபோதும் வர்த்தகம் செய்யாதீர்கள்.</div>
                </details>
                <details>
                    <summary>திட்டங்களுக்கு இடையிலான வேறுபாடு என்ன?</summary>
                    <div class="a">Prototype — ப்ரோட்டோடைப் இன்ஜினுக்கு ஒற்றைச் சந்தை ஆரம்ப அணுகல். Founding Alpha — தொடர் கட்டணமின்றி வாழ்நாள் முழு அணுகல். Early Access — அதே முழு இன்ஜின், மாதாந்திரக் கட்டணம், சுதந்திரமான ரத்து. VIP Annual — முன்னுரிமை செயலாக்கம், முழு API அணுகல், முன்னுரிமை ஆதரவு கூடுதல்.</div>
                </details>
                <details>
                    <summary>முன்பதிவுக்குப் பிறகு என்ன நடக்கும்?</summary>
                    <div class="a">உடனே ஆர்டர் உறுதிப்படுத்தல் கிடைக்கும்; பிறகு வெளியீட்டு கால அட்டவணைத் தகவல்களும் இணைப்பு வழிமுறைகளும் மின்னஞ்சலில் வரும். நிறுவனர் உறுப்பினர்கள் பொது கிடைப்பதற்கு முன் இணைக்கப்படுவார்கள்.</div>
                </details>
                <details>
                    <summary>எனக்குப் பணத்திரும்பம் கிடைக்குமா?</summary>
                    <div class="a">ஆம் — வெளியீட்டுக்கு முன் எப்போது வேண்டுமானாலும் முன்பதிவுகள் முழுமையாகத் திரும்பப்பெறத்தக்கவை. ஆதரவைத் தொடர்பு கொள்ளுங்கள் (விவரங்கள் உங்கள் வாங்கல் ரசீதில்); பணத்திரும்பம் செயல்படுத்தப்படும். வெளியீட்டுக்குப் பிறகு மாத மற்றும் ஆண்டு பாஸ்களை எப்போது வேண்டுமானாலும் ரத்து செய்து எதிர்கால கட்டணங்களை நிறுத்தலாம். முழு விவரங்கள் எங்கள் <a href="/terms" style="color:var(--accent)">சேவை விதிமுறைகளில்</a> (ஆங்கிலத்தில்).</div>
                </details>
            </div>
        </div>
    </section>

    <section class="final">
        <div class="wrap">
            <h2>நிறுவனர் விலை வெளியீட்டோடு முடிவடைகிறது.</h2>
            <p>இப்போதே உங்கள் திட்டத்தை முன்பதிவு செய்யுங்கள் — இன்ஜின் பொதுவானதும் இந்த விலைகள் நிரந்தரமாக விலக்கப்படும்.</p>
            <a href="#pricing" class="btn primary">என் திட்டத்தை முன்பதிவு செய்</a>
        </div>
    </section>

    <footer>
        <div class="wrap">
            <div class="foot-top">
                <a href="#" class="logo">ai <em>PassiveAutotrades</em></a>
                <div class="foot-links">
                    <a href="#how">எப்படி வேலை செய்கிறது</a>
                    <a href="#strategy">உத்தி</a>
                    <a href="#pricing">விலைகள்</a>
                    <a href="#faq">கேள்விகள்</a>
                    <a href="/terms">விதிமுறைகள்</a>
                    <a href="/privacy">தனியுரிமை</a>
                </div>
            </div>
            <p class="disclaimer">அபாய வெளிப்படுத்தல்: வர்த்தகத்தில் கணிசமான இழப்பு அபாயம் உள்ளது; இது ஒவ்வொரு முதலீட்டாளருக்கும் ஏற்றதல்ல. அல்காரிதம் மற்றும் தானியங்கி உத்திகள் பணத்தை இழக்கக்கூடும், இழக்கின்றன; கடந்தகால அல்லது உருவகப்படுத்தப்பட்ட செயல்திறன் எதிர்கால முடிவுகளுக்கு உத்தரவாதம் அல்ல. ai PassiveAutotrades ஒரு மென்பொருள் கருவி — முதலீட்டு ஆலோசகரோ, தரகர்-வியாபாரியோ, நம்பிக்கைப் பொறுப்பாளரோ அல்ல; இந்தத் தளத்தில் எதுவும் நிதி ஆலோசனையோ வர்த்தக அழைப்போ அல்ல. முன்பதிவு வாங்கல்கள் மேலே விவரித்தபடி வெளியீட்டில் மென்பொருள் அணுகலை வழங்கும். இழக்கச் சகிக்கக்கூடிய மூலதனத்தில் மட்டுமே வர்த்தகம் செய்யுங்கள்.</p>
            <p class="copyright">&copy; 2026 ai PassiveAutotrades. அனைத்து உரிமைகளும் பாதுகாக்கப்பட்டவை.</p>
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
    <loc>https://aipassiveautotrades.vercel.app/de</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/pt</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/ar</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/fa</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/ur</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/hi</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/bn</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aipassiveautotrades.vercel.app/ta</loc>
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


@app.get("/de", response_class=HTMLResponse)
def read_root_de():
    return HTMLResponse(content=HOMEPAGE_HTML_DE, headers=CACHE_HEADERS)


@app.get("/pt", response_class=HTMLResponse)
def read_root_pt():
    return HTMLResponse(content=HOMEPAGE_HTML_PT, headers=CACHE_HEADERS)


@app.get("/ar", response_class=HTMLResponse)
def read_root_ar():
    return HTMLResponse(content=HOMEPAGE_HTML_AR, headers=CACHE_HEADERS)


@app.get("/fa", response_class=HTMLResponse)
def read_root_fa():
    return HTMLResponse(content=HOMEPAGE_HTML_FA, headers=CACHE_HEADERS)


@app.get("/ur", response_class=HTMLResponse)
def read_root_ur():
    return HTMLResponse(content=HOMEPAGE_HTML_UR, headers=CACHE_HEADERS)


@app.get("/hi", response_class=HTMLResponse)
def read_root_hi():
    return HTMLResponse(content=HOMEPAGE_HTML_HI, headers=CACHE_HEADERS)


@app.get("/bn", response_class=HTMLResponse)
def read_root_bn():
    return HTMLResponse(content=HOMEPAGE_HTML_BN, headers=CACHE_HEADERS)


@app.get("/ta", response_class=HTMLResponse)
def read_root_ta():
    return HTMLResponse(content=HOMEPAGE_HTML_TA, headers=CACHE_HEADERS)


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

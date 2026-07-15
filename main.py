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


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ai PassiveAutotrades | Institutional Alpha</title>
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <style>
        body { background: #050505; color: #fff; font-family: 'Inter', sans-serif; margin: 0; padding: 0; }
        .hero { text-align: center; padding: 100px 20px; }
        .hero h1 { font-size: 3.5rem; margin-bottom: 20px; }
        .hero p { color: #8b949e; font-size: 1.2rem; max-width: 600px; margin: 0 auto 40px; }

        .pricing { display: flex; justify-content: center; gap: 20px; padding: 50px 20px; flex-wrap: wrap; }
        .card { background: #111; padding: 40px; border-radius: 12px; border: 1px solid #222; text-align: center; width: 300px; }
        .card.featured { border: 1px solid #58a6ff; }
        .btn { background: #58a6ff; color: #000; padding: 15px 30px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="hero">
        <h1>Institutional Income, Automated.</h1>
        <p>Run professional-grade Z-score quant strategies without watching charts. High-frequency algorithmic precision, delivered passively.</p>
    </div>

    <div class="pricing">
        <!-- Tier 1: Lifetime -->
        <div class="card">
            <h3>Founding Alpha</h3>
            <div style="font-size: 2rem; margin: 20px 0;">$199.99</div>
            <p>Lifetime access. No monthly fees.</p>
            <a href="YOUR_STRIPE_LINK_1" class="btn">Get Started</a>
        </div>

        <!-- Tier 2: Monthly -->
        <div class="card">
            <h3>Early Access Pass</h3>
            <div style="font-size: 2rem; margin: 20px 0;">$49.99</div>
            <p>Full engine utility. Billed monthly.</p>
            <a href="YOUR_STRIPE_LINK_2" class="btn">Claim Monthly</a>
        </div>

        <!-- Tier 3: Annual -->
        <div class="card featured">
            <h3>VIP Annual Pass</h3>
            <div style="font-size: 2rem; margin: 20px 0;">$499.99</div>
            <p>Priority execution + Full API access.</p>
            <a href="YOUR_STRIPE_LINK_3" class="btn">Claim Annual</a>
        </div>
    </div>
</body>
</html>
"""

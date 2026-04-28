<div align="center">
  <br />
  <img src="https://img.shields.io/badge/-%F0%9F%A7%A0%20CONSULTING%20DECISION%20ENGINE-0a0a0a?style=for-the-badge&labelColor=0a0a0a" alt="CDE" />
  <br /><br />

  <p>
    <strong>A Production-Grade, AI-Powered Strategic Advisory Platform</strong><br/>
    <sub>Bridging quantitative rigor with executive-grade generative intelligence.</sub>
  </p>

  <br />

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white" /></a>&nbsp;
    <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-3.0.2-000000?style=flat-square&logo=flask&logoColor=white" /></a>&nbsp;
    <a href="https://groq.com/"><img src="https://img.shields.io/badge/Groq-Llama%203-F55036?style=flat-square" /></a>&nbsp;
    <a href="https://plotly.com/"><img src="https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=flat-square&logo=plotly&logoColor=white" /></a>&nbsp;
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22C55E?style=flat-square" /></a>
  </p>

  <p>
    <a href="#-overview">Overview</a> &nbsp;·&nbsp;
    <a href="#-modules">Modules</a> &nbsp;·&nbsp;
    <a href="#-architecture">Architecture</a> &nbsp;·&nbsp;
    <a href="#-getting-started">Getting Started</a> &nbsp;·&nbsp;
    <a href="#-deployment">Deployment</a> &nbsp;·&nbsp;
    <a href="#-contributing">Contributing</a>
  </p>

  <br />
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>

<br />

## 📌 Overview

The **Consulting Decision Engine (CDE)** is a full-stack web application that transforms complex business problems into structured, boardroom-ready recommendations — fast.

It does this by combining two layers that most tools keep separate:

- **Deterministic financial modeling** — rigorous simulations using real mathematical frameworks (price elasticity, MCDM scoring, benchmarking deltas)
- **Generative AI synthesis** — Groq's high-speed Llama 3 inference translates quantitative outputs into plain-English executive narratives

The result is a platform where every insight is mathematically anchored. No hallucinated strategies, no generic advice — just data-grounded intelligence designed for decision-makers.

<br />

## 🧩 Modules

<details>
<summary><strong>📊 &nbsp;Pricing Strategy Optimization</strong></summary>

<br />

Analyzes historical price elasticity and current cost structures to simulate revenue and profit curves across a defined price range. Identifies the exact price point that maximizes gross margin without triggering excessive customer churn.

**Outputs**
- Interactive revenue vs. price curves (Plotly)
- Margin expansion projections by scenario
- Price elasticity sensitivity metrics

</details>

<details>
<summary><strong>🌍 &nbsp;Market Entry Evaluation</strong></summary>

<br />

Applies a weighted Multi-Criteria Decision Matrix (MCDM) across competitive density, regulatory friction, and total addressable market size to objectively score and rank geographic or demographic expansion targets.

**Outputs**
- Radar charts of market viability per candidate
- Comparative multi-market scoring table
- Strategic entry phasing recommendations

</details>

<details>
<summary><strong>📉 &nbsp;Cost Reduction & Benchmarking</strong></summary>

<br />

Benchmarks current operational expenditures against synthesized industry standards. Surfaces systemic inefficiencies and quantifies the projected bottom-line impact of targeted cost optimization initiatives.

**Outputs**
- Cost breakdown waterfall charts
- Inefficiency heatmaps by department or function
- Projected ROI on individual cost-reduction interventions

</details>

<details>
<summary><strong>🧠 &nbsp;Generative Strategic Synthesis (Groq + Llama 3)</strong></summary>

<br />

The platform's intelligence layer. All deterministic computation outputs are serialized and injected as structured context into Groq's inference engine. The model generates concise executive summaries, identifies second-order strategic impacts, and articulates trade-offs in plain English — ready to be dropped into a board deck.

**Approach**: Zero-shot and few-shot prompting with grounded mathematical context, ensuring outputs remain factually tethered to the underlying data.

</details>

<br />

## 🏗 Architecture

```
consulting_engine/
│
├── app/
│   ├── blueprints/           # Flask route blueprints (one per analytical module)
│   ├── models/               # Core computation engines (elasticity, MCDM, benchmarks)
│   └── templates/            # Jinja2 HTML templates (glassmorphism UI)
│
├── utils/
│   └── data_loader.py        # Synthetic market data generation pipeline
│
├── static/                   # CSS, client-side JS, Plotly assets
│
├── Dockerfile
├── requirements.txt
├── .env.example
└── app.py                    # Application factory
```

<br />

| Layer | Technology | Role |
|---|---|---|
| **Frontend** | Vanilla HTML/CSS, Plotly.js | Glassmorphism UI, interactive charts |
| **Backend** | Flask 3.0, Blueprint architecture | Routing, request handling, API orchestration |
| **Data Engine** | Pandas, NumPy | Deterministic simulation & aggregation |
| **LLM Layer** | Groq API (Llama 3) | Executive narrative generation |
| **Containerization** | Docker | Portable deployment |
| **Process Manager** | Gunicorn | Production WSGI server |

<br />

## 🚀 Getting Started

### Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.9 or higher |
| Git | Any recent version |
| Groq API Key | [Get one here →](https://console.groq.com/) |

<br />

### Step 1 — Clone the Repository

```bash
git clone https://github.com/AlexKochu/consulting_engine.git
cd consulting_engine
```

### Step 2 — Set Up the Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3 — Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` and add your credentials:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 4 — Generate the Synthetic Data Model

The analytics engines require a baseline data matrix before first launch. Run this once:

```bash
python utils/data_loader.py
```

### Step 5 — Launch the Application

```bash
flask run
```

Open your browser and navigate to **http://localhost:5000**

<br />

## ☁️ Deployment

<details>
<summary><strong>Option A &nbsp;—&nbsp; Render (Native Python)</strong></summary>

<br />

1. Connect your GitHub repository to [Render](https://render.com) as a **Web Service**.
2. Set the runtime to **Python 3**.
3. Configure the following commands:

| Setting | Value |
|---|---|
| **Build Command** | `pip install -r requirements.txt && python utils/data_loader.py` |
| **Start Command** | `gunicorn "app:create_app()"` |

4. Navigate to the **Environment** tab and add `GROQ_API_KEY` as a secret variable.
5. Deploy.

</details>

<details>
<summary><strong>Option B &nbsp;—&nbsp; Railway (Dockerized)</strong></summary>

<br />

1. Link your GitHub repository to a new [Railway](https://railway.app) project.
2. Railway will auto-detect the included `Dockerfile` — no additional configuration needed.
3. Add `GROQ_API_KEY` to the service's **Variables** panel.
4. Deploy and expose the generated public domain.

</details>

<br />

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome.

**Before opening a pull request**, please open an [issue](https://github.com/AlexKochu/consulting_engine/issues) first to discuss the proposed change. This keeps the review process clean and focused.

```
1. Fork the repository
2. Create your feature branch  →  git checkout -b feature/your-feature-name
3. Commit your changes         →  git commit -m "feat: describe your change"
4. Push to your branch         →  git push origin feature/your-feature-name
5. Open a Pull Request
```

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit message formatting.

<br />

## 📜 License

This project is released under the **MIT License**. See the [`LICENSE`](LICENSE) file for full terms.

<br />

<div align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
  <br /><br />
  <sub>Built with precision by <a href="https://github.com/AlexKochu"><strong>Alex</strong></a></sub>
  <br />
  <sub>If this project helped you, consider giving it a ⭐</sub>
</div>
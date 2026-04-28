<div align="center">
  <br />

  <h1>Consulting Decision Engine</h1>

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
    <a href="#overview">Overview</a> &nbsp;·&nbsp;
    <a href="#modules">Modules</a> &nbsp;·&nbsp;
    <a href="#architecture">Architecture</a> &nbsp;·&nbsp;
    <a href="#getting-started">Getting Started</a> &nbsp;·&nbsp;
    <a href="#deployment">Deployment</a> &nbsp;·&nbsp;
    <a href="#project-structure">Project Structure</a> &nbsp;·&nbsp;
    <a href="#contributing">Contributing</a>
  </p>

  <br />
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>

<br />

## Overview

The **Consulting Decision Engine (CDE)** is a full-stack web application that transforms complex business problems into structured, boardroom-ready recommendations.

It does this by combining two layers that most tools keep separate:

- **Deterministic financial modeling** — rigorous simulations using real mathematical frameworks (price elasticity, MCDM scoring, benchmarking deltas)
- **Generative AI synthesis** — Groq's high-speed Llama 3 inference translates quantitative outputs into plain-English executive narratives

The result is a platform where every insight is mathematically anchored. No hallucinated strategies, no generic advice — just data-grounded intelligence designed for decision-makers.

<br />

## Modules

<details>
<summary><strong>Pricing Strategy Optimization</strong></summary>

<br />

Analyzes historical price elasticity and current cost structures to simulate revenue and profit curves across a defined price range. Identifies the exact price point that maximizes gross margin without triggering excessive customer churn.

**Outputs**
- Interactive revenue vs. price curves (Plotly)
- Margin expansion projections by scenario
- Price elasticity sensitivity metrics

</details>

<details>
<summary><strong>Market Entry Evaluation</strong></summary>

<br />

Applies a weighted Multi-Criteria Decision Matrix (MCDM) across competitive density, regulatory friction, and total addressable market size to objectively score and rank geographic or demographic expansion targets.

**Outputs**
- Radar charts of market viability per candidate
- Comparative multi-market scoring table
- Strategic entry phasing recommendations

</details>

<details>
<summary><strong>Cost Reduction and Benchmarking</strong></summary>

<br />

Benchmarks current operational expenditures against synthesized industry standards. Surfaces systemic inefficiencies and quantifies the projected bottom-line impact of targeted cost optimization initiatives.

**Outputs**
- Cost breakdown waterfall charts
- Inefficiency heatmaps by department or function
- Projected ROI on individual cost-reduction interventions

</details>

<details>
<summary><strong>Generative Strategic Synthesis (Groq + Llama 3)</strong></summary>

<br />

The platform's intelligence layer. All deterministic computation outputs are serialized and injected as structured context into Groq's inference engine. The model generates concise executive summaries, identifies second-order strategic impacts, and articulates trade-offs in plain English — ready to be inserted into a board deck.

**Approach**: Zero-shot and few-shot prompting with grounded mathematical context, ensuring outputs remain factually tethered to the underlying data.

</details>

<br />

## Architecture

| Layer | Technology | Role |
|---|---|---|
| **Frontend** | Vanilla HTML/CSS, Plotly.js | Glassmorphism UI, interactive charts |
| **Backend** | Flask 3.0, Blueprint architecture | Routing, request handling, API orchestration |
| **Data Engine** | Pandas, NumPy | Deterministic simulation and aggregation |
| **LLM Layer** | Groq API (Llama 3) | Executive narrative generation |
| **Containerization** | Docker | Portable deployment |
| **Process Manager** | Gunicorn | Production WSGI server |

<br />

## Getting Started

### Prerequisites

| Requirement | Notes |
|---|---|
| Python 3.9+ | Required for all backend modules |
| Git | Any recent version |
| Groq API Key | [Obtain here](https://console.groq.com/) |

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

## Deployment

<details>
<summary><strong>Option A — Render (Native Python)</strong></summary>

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
<summary><strong>Option B — Railway (Dockerized)</strong></summary>

<br />

1. Link your GitHub repository to a new [Railway](https://railway.app) project.
2. Railway will auto-detect the included `Dockerfile` — no additional configuration needed.
3. Add `GROQ_API_KEY` to the service's **Variables** panel.
4. Deploy and expose the generated public domain.

</details>

<br />

## Project Structure

The following tree reflects the full consulting workflow of the engine — from data ingestion through analysis to AI-generated output.

```
consulting_engine/
│
├── app/
│   │
│   ├── blueprints/
│   │   ├── pricing.py                  # Pricing strategy routes
│   │   ├── market_entry.py             # Market evaluation routes
│   │   ├── cost_reduction.py           # Cost benchmarking routes
│   │   └── synthesis.py               # LLM synthesis orchestration routes
│   │
│   ├── models/
│   │   ├── pricing_model.py            # Price elasticity & margin simulation
│   │   ├── mcdm_model.py              # Multi-criteria decision matrix engine
│   │   ├── benchmarking_model.py       # Industry benchmark comparison logic
│   │   └── groq_client.py             # Groq API wrapper & prompt templates
│   │
│   └── templates/
│       ├── base.html                   # Shared layout (glassmorphism shell)
│       ├── dashboard.html              # Landing page & module selector
│       ├── pricing.html                # Pricing strategy UI & chart container
│       ├── market_entry.html           # Market radar chart UI
│       ├── cost_reduction.html         # Waterfall & heatmap UI
│       └── synthesis.html             # Executive summary output panel
│
├── static/
│   ├── css/
│   │   └── main.css                   # Global glassmorphism styles
│   └── js/
│       └── charts.js                  # Plotly chart initialization helpers
│
├── utils/
│   ├── data_loader.py                 # Synthetic data generation pipeline
│   └── formatters.py                  # Output serialization for LLM context
│
├── data/
│   └── synthetic/
│       ├── pricing_data.csv            # Simulated price-volume-cost matrix
│       ├── market_scores.csv           # Candidate market attribute scores
│       └── cost_benchmarks.csv         # Industry benchmark expense profiles
│
├── prompts/
│   ├── pricing_prompt.txt             # Few-shot prompt: pricing narrative
│   ├── market_entry_prompt.txt        # Few-shot prompt: market entry summary
│   ├── cost_reduction_prompt.txt      # Few-shot prompt: cost analysis narrative
│   └── synthesis_prompt.txt           # Master prompt: full strategic synthesis
│
├── tests/
│   ├── test_pricing_model.py          # Unit tests for elasticity calculations
│   ├── test_mcdm_model.py             # Unit tests for MCDM scoring
│   └── test_groq_client.py            # Integration tests for LLM responses
│
├── .env.example                       # Environment variable template
├── requirements.txt                   # Python dependency manifest
├── Dockerfile                         # Container definition for Railway
├── gunicorn.conf.py                   # Gunicorn worker configuration
└── app.py                             # Application factory (create_app)
```

### Consulting Workflow

The engine follows a linear three-phase consulting pipeline:

```
[ Raw Business Input ]
        |
        v
[ Phase 1 — Quantitative Analysis ]
  Deterministic models process user inputs.
  Pandas/NumPy compute curves, scores, and deltas.
        |
        v
[ Phase 2 — Visual Reporting ]
  Plotly renders interactive charts inline.
  Results are displayed on the module-specific dashboard page.
        |
        v
[ Phase 3 — Generative Synthesis ]
  Serialized model outputs are injected into structured prompts.
  Groq (Llama 3) generates the executive narrative.
  Output is rendered on the synthesis panel — board-deck ready.
```

<br />

## Contributing

Contributions, bug reports, and feature requests are welcome. Please open an [issue](https://github.com/AlexKochu/consulting_engine/issues) before submitting a pull request to discuss the proposed change.

```
1. Fork the repository
2. Create your feature branch  →  git checkout -b feature/your-feature-name
3. Commit your changes         →  git commit -m "feat: describe your change"
4. Push to your branch         →  git push origin feature/your-feature-name
5. Open a Pull Request
```

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit message formatting.

<br />

## License

This project is released under the **MIT License**. See the [`LICENSE`](LICENSE) file for full terms.

<br />

<div align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
  <br /><br />
  <sub>Built by <a href="https://github.com/AlexKochu"><strong>Alex</strong></a></sub>
  <br />
  <sub>If this project helped you, consider giving it a star.</sub>
</div>
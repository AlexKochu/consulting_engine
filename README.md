<div align="center">
  <br />

  <h1>StratifyAI — Consulting Decision Engine</h1>

  <p>
    <strong>A Production-Grade, AI-Powered Strategic Advisory Platform</strong><br/>
    <sub>Bridging deterministic financial rigor with executive-grade generative intelligence.</sub>
  </p>

  <br />

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white" /></a>&nbsp;
    <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask&logoColor=white" /></a>&nbsp;
    <a href="https://groq.com/"><img src="https://img.shields.io/badge/Groq-Llama%203.1-F55036?style=flat-square" /></a>&nbsp;
    <a href="https://plotly.com/"><img src="https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=flat-square&logo=plotly&logoColor=white" /></a>&nbsp;
    <a href="https://vercel.com/"><img src="https://img.shields.io/badge/Vercel-Frontend-000000?style=flat-square&logo=vercel&logoColor=white" /></a>&nbsp;
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22C55E?style=flat-square" /></a>
  </p>

  <p>
    <a href="#overview">Overview</a> &nbsp;·&nbsp;
    <a href="#strategy-engines">Strategy Engines</a> &nbsp;·&nbsp;
    <a href="#architecture">Architecture</a> &nbsp;·&nbsp;
    <a href="#getting-started">Getting Started</a> &nbsp;·&nbsp;
    <a href="#deployment">Deployment</a> &nbsp;·&nbsp;
    <a href="#project-structure">Project Structure</a> &nbsp;·&nbsp;
    <a href="#contributing">Contributing</a>
  </p>

  <p>
    <strong>Live Demo →</strong> <a href="https://consulting-engine.vercel.app/">consulting-engine.vercel.app</a>
  </p>

  <br />
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
</div>

<br />

## Overview

**StratifyAI** is a full-stack strategic advisory platform that transforms complex business problems into boardroom-ready recommendations.

Most business tools operate at one of two extremes — raw data outputs (spreadsheets) or generic, unanchored AI advice (chatbots). StratifyAI bridges this gap by combining two layers that most platforms keep separate:

- **Deterministic financial modeling** — rigorous simulations built on real mathematical frameworks: price elasticity curves, MCDM scoring matrices, and cost benchmarking deltas
- **Generative AI synthesis** — Groq's high-speed Llama 3.1 inference engine translates quantitative outputs into plain-English executive narratives

Every insight is mathematically anchored before the AI touches it. No hallucinated strategies, no generic advice — just data-grounded intelligence built for decision-makers.

<br />

## Strategy Engines

<details>
<summary><strong>Pricing Strategy Optimization</strong></summary>

<br />

Simulates revenue and profit curves across a defined price range by analyzing historical price elasticity and current cost structures. Identifies the exact price point that maximizes gross margin without triggering excessive customer churn.

**Outputs**
- Interactive revenue vs. price curves (Plotly)
- Margin expansion projections by scenario
- Price elasticity sensitivity metrics

</details>

<details>
<summary><strong>Market Entry Evaluation</strong></summary>

<br />

Applies a weighted Multi-Criteria Decision Matrix (MCDM) across dimensions including competitive density, regulatory friction, and total addressable market size. Objectively scores and ranks geographic or demographic expansion targets.

**Outputs**
- Radar charts of market viability per candidate
- Comparative multi-market scoring table
- Strategic entry phasing recommendations

</details>

<details>
<summary><strong>Cost Reduction and Benchmarking</strong></summary>

<br />

Benchmarks current operational expenditures — across COGS, R&D, and IT infrastructure — against synthesized industry standards. Surfaces systemic inefficiencies and quantifies the projected bottom-line impact of targeted optimization initiatives.

**Outputs**
- Cost breakdown waterfall charts
- Inefficiency heatmaps by department or function
- Projected ROI on individual cost-reduction interventions

</details>

<details>
<summary><strong>Generative Strategic Synthesis (Groq + Llama 3.1)</strong></summary>

<br />

The platform's intelligence layer. All deterministic computation outputs are serialized and injected as structured context into Groq's inference engine. The model generates concise executive summaries, identifies second-order strategic impacts, and articulates trade-offs in plain English — ready to be inserted into a board deck.

**Approach:** Zero-shot prompting with grounded mathematical context, ensuring all AI outputs remain factually tethered to pre-calculated figures. The AI explains the numbers; it does not invent them.

</details>

<br />

## Architecture

| Layer | Technology | Role |
|---|---|---|
| **Frontend** | Vanilla JS, CSS3, HTML5 | CARYNTH UI, glassmorphism design, responsive state management |
| **Backend** | Python / Flask 3.0 | API orchestration, CORS handling, request routing |
| **Data Engine** | Pandas, NumPy | Deterministic financial simulations and MCDM scoring logic |
| **LLM Layer** | Groq API (Llama 3.1) | Zero-shot executive narrative generation |
| **Visualization** | Plotly.js | Interactive charts and strategic heatmaps |
| **Deployment** | Render (Backend), Vercel (Frontend) | Scalable cloud hosting with CI/CD integration |

### Consulting Workflow

The engine follows a linear three-phase pipeline:

```
[ Raw Business Input ]
        |
        v
[ Phase 1 — Quantitative Analysis ]
  Deterministic models process user-submitted metrics.
  Pandas/NumPy compute elasticity curves, MCDM scores, and cost deltas.
        |
        v
[ Phase 2 — Visual Reporting ]
  Plotly renders interactive charts inline on the dashboard.
  Results are displayed per module with drill-down capability.
        |
        v
[ Phase 3 — Generative Synthesis ]
  Serialized model outputs are injected into structured prompts.
  Groq (Llama 3.1) generates the executive narrative.
  Output is rendered on the synthesis panel — board-deck ready.
```

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
git clone https://github.com/AlexKochu/consulting-engine.git
cd consulting-engine
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

### Step 4 — Launch the Backend

```bash
flask run
```

### Step 5 — Serve the Frontend

Open `frontend/index.html` directly in a browser, or serve it with any static file server:

```bash
npx serve frontend/
```

Navigate to **http://localhost:5000**

<br />

## Deployment

<details>
<summary><strong>Option A — Render + Vercel (Recommended)</strong></summary>

<br />

The project ships with pre-configured deployment files for both platforms.

**Backend → Render**

1. Connect your GitHub repository to [Render](https://render.com) as a **Web Service**.
2. Set the runtime to **Python 3**.
3. Configure the following:

| Setting | Value |
|---|---|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn "app:create_app()"` |

4. Add `GROQ_API_KEY` as a secret environment variable.
5. Deploy. The included `render.yaml` handles remaining configuration automatically.

**Frontend → Vercel**

1. Connect your GitHub repository to [Vercel](https://vercel.com).
2. Set the root directory to `frontend/`.
3. Update the API base URL in `frontend/app.js` to point to your Render service URL.
4. Deploy. The included `vercel.json` handles routing configuration automatically.

</details>

<details>
<summary><strong>Option B — Docker (Self-Hosted)</strong></summary>

<br />

```bash
docker build -t stratify-ai .
docker run -p 5000:5000 -e GROQ_API_KEY=your_key_here stratify-ai
```

</details>

<br />

## Project Structure

```
consulting-engine/
│
├── backend/
│   ├── app.py                          # Application factory (create_app)
│   │
│   ├── blueprints/
│   │   ├── pricing.py                  # Pricing strategy routes
│   │   ├── market_entry.py             # Market evaluation routes
│   │   ├── cost_reduction.py           # Cost benchmarking routes
│   │   └── synthesis.py               # LLM synthesis orchestration
│   │
│   ├── models/
│   │   ├── pricing_model.py            # Price elasticity & margin simulation
│   │   ├── mcdm_model.py              # Multi-criteria decision matrix engine
│   │   ├── benchmarking_model.py       # Industry benchmark comparison logic
│   │   └── groq_client.py             # Groq API wrapper & prompt templates
│   │
│   ├── utils/
│   │   └── formatters.py              # Output serialization for LLM context
│   │
│   ├── render.yaml                     # Render deployment configuration
│   ├── gunicorn.conf.py                # Gunicorn worker configuration
│   └── requirements.txt
│
├── frontend/
│   ├── index.html                      # Application entry point
│   ├── app.js                          # State management and API calls
│   ├── charts.js                       # Plotly chart initialization helpers
│   ├── styles/
│   │   └── carynth.css                # CARYNTH UI design system
│   └── vercel.json                     # Vercel deployment configuration
│
├── .env.example                        # Environment variable template
├── Dockerfile                          # Container definition
└── README.md
```

<br />

## Design Decisions

**Why separate the AI from the calculations?**
Standard LLMs generate numbers as part of their output, making them prone to hallucination in financial contexts. StratifyAI inverts this: Python computes all financial figures first, then the LLM is given only those verified numbers to explain. This guarantees mathematical accuracy while still producing polished, human-readable analysis.

**Why Groq over OpenAI?**
Groq's inference speed is significantly faster at equivalent output quality, which is essential for a platform where users expect near-instant narrative generation after submitting inputs.

**Why Vanilla JS over a framework?**
The frontend requirements — form handling, chart rendering, API calls, and theme toggling — are well within what Vanilla JS handles cleanly. Avoiding a build pipeline keeps the frontend lean and the Vercel deployment straightforward.

<br />

## Contributing

Contributions, bug reports, and feature requests are welcome. Please open an [issue](https://github.com/AlexKochu/consulting-engine/issues) before submitting a pull request to discuss the proposed change.

```
1. Fork the repository
2. Create your feature branch  →  git checkout -b feature/your-feature-name
3. Commit your changes         →  git commit -m "feat: describe your change"
4. Push to your branch         →  git push origin feature/your-feature-name
5. Open a Pull Request
```

Please follow [Conventional Commits](https://www.conventionalcommits.org/) for commit message formatting.

<br />

## Roadmap

- [ ] User authentication and saved scenario history
- [ ] PDF export for executive summaries
- [ ] Additional strategy engines (M&A fit analysis, competitive benchmarking)
- [ ] Scenario comparison view — side-by-side analysis across multiple inputs
- [ ] Multi-language narrative output

<br />

## License

This project is released under the **MIT License**. See the [`LICENSE`](LICENSE) file for full terms.

<br />

<div align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />
  <br /><br />
  <sub>Built by <a href="https://github.com/AlexKochu"><strong>Alex</strong></a></sub>
  <br />
  <sub>If this project was useful, consider leaving a star.</sub>
</div>
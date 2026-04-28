# Consulting Decision Engine

A production-ready Flask-based web application that transforms user-defined business problems into structured, data-driven consulting recommendations using deterministic logic, synthetic datasets, and LLM-assisted reasoning.

## Features
- **Pricing Strategy**: Analyzes price elasticity and simulates revenue curves to find the optimal price point.
- **Market Entry**: Evaluates target regions using weighted multi-criteria scoring.
- **Cost Reduction**: Benchmarks current operational costs against industry standards to identify inefficiencies.
- **Generative AI Insights**: Uses Groq (Llama 3) to generate narrative executive summaries and strategic insights.
- **Downloadable Reports**: Generates standalone HTML reports with all data and insights.

## Local Setup

1. **Clone or navigate to the directory**
   ```bash
   cd consulting_engine
   ```

2. **Set up virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```
   Add your `GROQ_API_KEY` to the `.env` file.

5. **Generate Synthetic Data**
   The application requires data to run deterministic logic. Generate it locally:
   ```bash
   python utils/data_loader.py
   ```

6. **Run the App**
   ```bash
   flask run
   ```
   Open `http://localhost:5000` in your browser.

## Deployment Instructions

### Option 1: Render

1. Create a new Web Service on Render and link your GitHub repository.
2. Settings:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python utils/data_loader.py`
   - **Start Command**: `gunicorn "app:create_app()"`
3. Add Environment Variables:
   - `GROQ_API_KEY` = your_api_key
   - `PYTHON_VERSION` = 3.11.0

### Option 2: Railway (using Docker)

1. Connect your repository to Railway.
2. Railway will automatically detect the `Dockerfile`.
3. Add the `GROQ_API_KEY` in the Variables tab.
4. Deploy!

## Architecture

- **`app.py` / `routes.py`**: Flask application layer and routing.
- **`services/`**: Core deterministic business logic (`pricing.py`, `market.py`, `cost.py`) and the LLM integration (`llm_service.py`).
- **`utils/data_loader.py`**: Generates synthetic CSV datasets to `data/` folder, ensuring non-linear correlations.
- **`templates/` & `static/`**: Frontend layer built with HTML, Plotly.js, and premium CSS glassmorphism.

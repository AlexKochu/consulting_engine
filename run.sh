#!/bin/bash

# Kill all background processes started by this script when it is stopped
trap "kill 0" EXIT

echo "----------------------------------------"
echo "🚀 StratifyAI: Starting Services"
echo "----------------------------------------"

# 1. Start Backend (Render-ready folder)
echo "📦 Starting Backend API on port 5001..."
source venv/bin/activate
(cd backend && python3 app.py) &

# 2. Start Frontend (Vercel-ready folder)
echo "🌐 Starting Frontend UI on port 3000..."
(cd frontend && python3 -m http.server 3000 --bind 127.0.0.1) &

echo "----------------------------------------"
echo "✅ Both services are now running!"
echo "👉 Frontend URL: http://localhost:3000/landing.html"
echo "👉 Backend API:  http://localhost:5001/health"
echo "----------------------------------------"
echo "Press Ctrl+C to stop both services."

wait

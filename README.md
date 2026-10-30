⚡ Qloo-vibe (v2.0) — Complete Technical Guide & Source Instructions
​Qloo-vibe (formerly TasteIQ) is an agentic, glassmorphic Cultural Intelligence Platform designed for the Qloo Agentic Hackathon. It extracts 360-degree cross-category cultural connections (Music, Movies, Dining, Fashion, Travel) from a single seed entity using Qloo's Taste Graph API.
​🎨 Design System & Color Palette
​Brand Logo: Electric Yellow (#EAB308 / #FACC15) with animated visual glow.
​Dark Theme:
​Background: Deep Navy Blue (#0A0F1D / #0E1117)
​Glass Containers: rgba(255, 255, 255, 0.05) with 1px solid rgba(255, 255, 255, 0.1)
​Highlights: Neon Pink (#EC4899), Bright White, Warm Orange (#F97316), Muted Gray
​Light Theme:
​Background: Soft Lavender / Light Purple (#F3E8FF)
​Highlights: Vivid Pink, Pure White, Deep Charcoal, Bright Yellow
​🏗️ Architecture & Key Components
​Global Header:
​Left: Electric Yellow Logo + Live Source Badge (Powered by Qloo-vibe + Qloo API + AI Agent).
​Right: Dynamic Theme Switcher (Dark Navy / Light Purple) + 3-Dots Dropdown Menu.
​15-Language Switcher: Instant UI translation across English, Hindi, Spanish, French, Mandarin, Arabic, Portuguese, Bengali, Russian, Japanese, German, Korean, Turkish, Vietnamese, and Italian.
​"How to Use" Modal: Interactive onboarding guide.
​3-Tab Interface:
​Tab 1: Input: Search Seed Entity (Artist, Film, Brand, City), select main Category, pick Target Audience (Gen-Z, Luxury, Niche Indie, Mainstream), and adjust Intensity/Diversity sliders.
​Tab 2: Output: Houses all 10 advanced cultural analysis features with data source indicators (Live Qloo Data vs Simulated Fallback).
​Tab 3: Saved Manager: Bookmark favorite matches and categorize non-favorites with full local storage persistence.
​10 Advanced UI Features:
​Interactive 3D Taste Graph Mesh: Rotatable node network (using Three.js / Vis.js).
​AI Persona Avatar & Badge: Generates demographic archetypes (e.g., Cyber-Minimalist Creator).
​Live Affinity Heatmap Bars: Color-coded percentage similarity progress bars.
​Cultural DNA Radar Chart: 5-axis balanced web chart for Music, Film, Fashion, Dining, Travel.
​Real-Time Vibe Preview Player: Audio track sample cards with animated equalizer bars.
​Co-Branding Match Matrix: Grid displaying top 5 brand partnership affinities.
​One-Click PDF/JSON Exporter: Executive briefing deck exporter and raw JSON viewer.
​Glassmorphic Cyberpunk UI: Custom Tailwind styling with smooth Framer Motion transitions.
​Audience Scenario Simulator: Dynamic recalculation filter toggles.
​MIT License Badge & Footer: Direct links to Qloo API docs and open-source repository.
​⚙️ How Data Connection Works (Live API vs Mock Engine)
​The backend/integration logic operates on a Smart Dual-Engine:
​Live Qloo API Integration:
​Target Base URL: https://hackathon.api.qloo.com
​Key Authorization: Passed via X-Api-Key or QLOO_API_KEY header.
​Live Badge: Displays a Green "Live Qloo Data" badge in Tab 2.
​Fallback Mock Data Engine:
​Activated automatically if QLOO_API_KEY is not present or if an API network timeout/401 occurs.
​Generates realistic, math-grounded cultural intelligence responses so the UI remains 100% functional during hackathon demos.
​Fallback Badge: Displays a Yellow "Simulated Data" badge.

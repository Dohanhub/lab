**Developer Directive – READ FIRST**

- **Do NOT** rename existing folders.
- **Do NOT** create new folders.
- Only **update** the current structure and files as instructed.

---

# doganBS Streamlit / Python “One‑App” Feature Catalog – *Dedicated to Omar*

*100+ ready‑to‑embed modules, widgets, and engine stubs for your Strategic Intelligence Suite*

*This document supersedes all previous AFTECH‑branded catalogs; every reference has been updated to ****doganBS****.*

## A. Core Streamlit UX Widgets (1 – 15)

1. **st.button()** – Standard action trigger.
2. **st.download\_button()** – Export any report (PDF/XLSX/DOCX).
3. **st.file\_uploader()** – Multi‑source uploads (Excel, CSV, PDF).
4. **st.chat\_message()** – In‑app AI conversation pane.
5. **st.progress() / st.spinner()** – Task feedback indicators.
6. **st.toast()** – Non‑blocking notifications (success, warning, error).
7. **st.toggle()** – Mode switches (e.g., Presentation / Edit).
8. **st.dataframe()** – Quick data preview with sort & filter.
9. **st.data\_editor()** – Editable grid for inline corrections.
10. **st.metric()** – KPI card with delta.
11. **st.slider() / st.select\_slider()** – Threshold & scenario controls.
12. **st.selectbox() / st.multiselect()** – Dynamic filter pickers.
13. **st.date\_input() / st.time\_input()** – Scheduling & timeline inputs.
14. **st.camera\_input()** – Capture signatures or document images.
15. **st.tabs() + st.expander()** – Hierarchical, clutter‑free layout.

## B. Advanced Streamlit Components (16 – 25)

16. **streamlit‑option‑menu** – Icon‑driven sidebar navigation.
17. **streamlit‑aggrid** – Spreadsheet‑like grid with formulas & conditional formatting.
18. **streamlit‑extras: copy‑to‑clipboard** – One‑click code / value copy.
19. **streamlit‑extras: keyboard‑shortcuts** – Power‑user productivity keys.
20. **streamlit‑tags** – Keyword tagging for RFQs & knowledge base.
21. **streamlit‑lottie** – Animated success / error cues.
22. **st.components.v1.iframe()** – Embed Power BI, Grafana, or Tableau.
23. **streamlit‑authenticator** – JWT / OAuth role‑based login.
24. **st.session\_state** – Cross‑page memory for drill‑through context.
25. **Custom CSS injector** – RTL/LTR switch + brand colors.

## C. Plotly & Visual Analytics (26 – 40)

26. **Bar / Column Chart** – Revenue vs Target.
27. **Line & Area Chart** – Trend lines with forecast overlay.
28. **Scatter / Bubble Plot** – Margin vs Lead‑time analysis.
29. **Treemap** – GP contribution by sector > vendor.
30. **Sunburst** – Multi‑level hierarchy (Region → Sector → Project).
31. **Sankey Diagram** – Cost flow from Budget to GP.
32. **Funnel Chart** – RFQ → Proposal → Win pipeline.
33. **Gantt / Timeline** – Project schedule & critical path.
34. **Heatmap** – Risk matrix (Impact vs Probability).
35. **Waterfall** – Variance explanation (Plan → Actual).
36. **Gauge / Bullet** – SLA health indicator.
37. **Violin / Box Plot** – Cost distribution & outliers.
38. **Polar Chart** – Capability radar for vendor scoring.
39. **3‑D Surface** – Scenario landscape (Cost, Time, Scope).
40. **Animated Choropleth** – Geo KPI play‑through (if needed).

## D. Data Processing & Quality (41 – 55)

41. **pandas pipe() chains** – Clean, join, aggregate.
42. **pyjanitor.clean\_names()** – Column standardisation.
43. **missingno matrix** – Visual null inspection.
44. **great\_expectations** – Data validation suite.
45. **pydantic models** – Strict schema enforcement.
46. **duckdb SQL** – In‑memory analytics without DB server.
47. **polars** – Lightning‑fast columnar ops for big CSV.
48. **pyarrow parquet cache** – Compressed, rapid reloads.
49. **dask delayed()** – Parallel ETL for large files.
50. **openpyxl / xlsxwriter** – Styled Excel BoQ output.
51. **pdfplumber** – Extract tables from scanned PDFs.
52. **rapidfuzz** – Deduplicate vendor names.
53. **dateparser** – Free‑text date normalisation.
54. **schema‑mapper auto‑align** – Column mismatch resolver.
55. **Custom error handler + logging to CSV & Sentry.**

## E. AI / LLM & Copilot Functions (56 – 70)

56. **OpenAI ChatCompletion** – Natural‑language query & rewrite.
57. **LangChain RetrievalQA** – Ask KPIs “why down?”.
58. **FAISS vector store** – Local semantic search over past proposals.
59. **LlamaIndex (GPT Index)** – Knowledge graph for RFQs.
60. **Haystack Document QA** – PDF contract interrogation.
61. **Auto‑summariser** – 100‑word exec brief generator.
62. **Sentiment & intent classifier** – Vendor email triage.
63. **Keyword extractor** – Auto‑tag RFQs & risks.
64. **Text‑to‑Speech (gTTS)** – Arabic/English voice briefing.
65. **Speech‑to‑Text (Whisper)** – Dictate notes.
66. **OpenAI Function‑Calling** – LLM triggers Streamlit actions.
67. **Time‑series forecasting (Prophet / NeuralProphet).**
68. **Anomaly detection (ADTK / tsfresh).**
69. **Reinforcement learner** – KPI target auto‑optimiser.
70. **Auto‑prompt memory** – Learns user preferences.

## F. KPI & Executive Metrics (71 – 80)

71. **Dynamic KPI card generator** – Plug‑and‑play metric list.
72. **Threshold slider with real‑time color change.**
73. **Drill‑down filter chain (Region → Sector → Project).**
74. **Delta vs Target badges** – 👍 / ⚠️ / ❌ icons.
75. **Snapshot comparator** – Month‑over‑Month toggle.
76. **Weighted scorecard engine** – 0–100 strategic value.
77. **Idle cost tracker** – Live SAR leakage meter.
78. **Compliance percentage ring** – NCA alignment.
79. **Resource utilisation gauge** – Head‑count vs plan.
80. **What‑if simulator panel** – Slider‑based scenario engine.

## G. RFQ / Proposal & Compliance (81 – 90)

81. **RFQ inbox parser (imap\_tools).**
82. **SharePoint list fetch (shareplum).**
83. **docxtpl proposal builder** – Arabic & English templates.
84. **BoQ margin calculator** – Auto‑VAT, markup tiers.
85. **Vendor clarification tracker** – Comment thread per RFQ.
86. **Weighted evaluation matrix with AgGrid.**
87. **NCA baseline checker (YAML rules).**
88. **Etimad form auto‑fill CSV exporter.**
89. **Risk‑flag LLM – highlights non‑compliant clauses.**
90. **PDF merger & stamp for final submission.**

## H. Vendor / Technology Scoring (91 – 95)

91. **Capability radar (Plotly polar).**
92. **CVSS vulnerability pull via NVD API.**
93. **Total‑Cost‑of‑Ownership calculator.**
94. **Cloud readiness heatmap.**
95. **Delivery lead‑time versus SLA scatter.**

## I. Business & Governance Utilities (96 – 100)

96. **streamlit‑authenticator role gates (Admin / Sales / Finance / SPV).**
97. **Audit ledger – CSV log + st.dataframe viewer.**
98. **GitHub webhook badge – show commit hash & agent notes.**
99. **Auto‑email exporter – send PDF to CEO / SVP.**
100. **Health‑check ping panel – SAP / SharePoint / Power BI status.**

---

## J. Architecture (Front‑End / Back‑End / Data‑Layer)

| Layer          | Tech Stack                                    | Folder Scope                        | Purpose                                                  |
| -------------- | --------------------------------------------- | ----------------------------------- | -------------------------------------------------------- |
| **Front‑End**  | Streamlit widgets (Sections A–C) + custom CSS | `/components/` & `/modules/*_ui.py` | Responsive UI, bilingual RTL/LTR, advanced navigation.   |
| **Back‑End**   | Python services (Sections D–I)                | `/modules/`                         | Data cleansing, AI engines, business logic, API calls.   |
| **Data‑Layer** | DuckDB + Parquet cache **inside** `/data/`    | `/data/`                            | Persistent yet portable storage; no external DB servers. |

*Integrity Rule → All logic must reference existing paths; no folder name changes.*

## K. Predictive Mapping & Role‑Based Guidance

| Role                               | Smart Screen Set                              | Predictive & Automation Features                                                |
| ---------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------- |
| **Solution Director**              | "Solution Cockpit", "Digital‑Twin Sandbox"    | Cost‑risk simulation, vendor capability radar, AI case‑study suggestions.       |
| **Sales Director**                 | "Pipeline Command", "Deal Acceleration"       | Win‑probability scoring, price‑sensitivity curves, auto‑generated battle‑cards. |
| **Commercial Director**            | "Margin Guardian", "Contract Validator"       | Real‑time GP drift alerts, BoQ optimiser, NCA/SDAIA compliance audit.           |
| **SVP / CEO**                      | "Executive Dashboard", "Strategic Brief"      | 5‑min AI brief, weighted scorecards, scenario impact snapshots.                 |
| **Self‑Smart Agent (doganBS Bot)** | Appears on every page via `st.chat_message()` | Learns user context, triggers reports, schedules tasks, voice briefing (gTTS).  |

**Multi‑Screen Navigation:** utilise `streamlit‑option‑menu` with icons; session\_state remembers last drill‑path; full‑screen toggle for board‑room mode.

**Mapping & Visual Guidance:** Sankey for cost flow, sunburst for org hierarchy, interactive floor‑map for project sites (if coordinates supplied).

---

## L. Beyond‑Universe Innovations (101 – 150)

*Exploratory and next‑decade capabilities drawn from field experience and R&D roadmaps.*

|  #  | Futuristic Feature                            | Concept Snapshot                                                                           |
| --- | --------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 101 | **Quantum KPI Solver**                        | Leverages local Qiskit simulator to optimise multi‑variable margins in milliseconds.       |
| 102 | **Digital‑Twin Drone Sync**                   | Auto‑launches a drone flight (via API) to capture live site images and embed in dashboard. |
| 103 | **AR Holo‑Dashboard**                         | Generates a WebXR layer; view KPIs as floating cards through HoloLens.                     |
| 104 | **Neural Voice Brief**                        | Uses Whisper + gTTS for bidirectional voice interaction in noisy environments.             |
| 105 | **Blockchain Audit Ledger**                   | Writes critical RFQ actions as hashes on a private Ethereum testnet for tamper‑proof logs. |
| 106 | **Edge‑ML Model Push**                        | Exports lightweight TensorFlow Lite models to on‑prem Raspberry Pi gateways.               |
| 107 | **Gesture Navigation**                        | Camera‑based hand‑gesture control for boardroom presentations (using MediaPipe).           |
| 108 | **Predictive Cash‑Flow Waterfall**            | Combines GPT‑4 trend explanation with Monte‑Carlo cash simulations.                        |
| 109 | **Dark‑Mode Circadian Shift**                 | UI auto‑tunes brightness based on local sunset API for eye comfort.                        |
| 110 | **IoT Sensor Heatmap**                        | Real‑time Plotly heatmap from MQTT topics; colors drift when anomalies spike.              |
| 111 | **5G Latency Monitor**                        | Pings field routers; shows latency violin plots per vendor eSIM.                           |
| 112 | **Auto‑Ethical Risk Scanner**                 | Flags ESG or data‑privacy non‑compliance in proposals via NLP rules.                       |
| 113 | **CV‑Based Invoice Reader**                   | YOLO‑v8 detects tables in scanned invoices and routes to BoQ comparison.                   |
| 114 | **Dynamic Carbon Footprint KPI**              | Calculates CO₂ per project phase using emission factors API.                               |
| 115 | **Gamified Sales League**                     | Real‑time leaderboard with achievement badges and confetti Lottie on target hit.           |
| 116 | **Emotion AI for Calls**                      | Analyses Teams call sentiment and posts a morale metric.                                   |
| 117 | **Real‑Time FX Hedging Predictor**            | Recommends SAR hedge positions via Prophet forecasts + FX API.                             |
| 118 | **Satellite Weather Overlay**                 | Pulls NOAA imagery to anticipate logistics delays.                                         |
| 119 | **AI‑Generated Infographic Export**           | Creates branded infographic slides in PPTX automatically.                                  |
| 120 | **Zero‑Touch CI/CD**                          | GitHub Actions auto‑deploy Docker image to internal Kubernetes on merge.                   |
| 121 | **Self‑Healing ETL**                          | Detects schema drift → auto‑maps fields or opens ticket.                                   |
| 122 | **Auto‑Narrated Board Pack**                  | Generates a narrated MP4 walkthrough of monthly KPIs.                                      |
| 123 | **Smart Legal Clause Builder**                | GPT prompts build customised SLA clauses in Arabic & English.                              |
| 124 | **Crowd‑Forecast Module**                     | Collects distributed probability estimates from team and aggregates Brier score.           |
| 125 | **Decentralised ID Login**                    | DID / verifiable credentials for vendor portal authentication.                             |
| 126 | **Zero‑Copy Data Share**                      | Uses Apache Arrow Flight for memory‑mapped data between notebooks.                         |
| 127 | **Dynamic Pricing Bot**                       | Scrapes competitor catalogues nightly and suggests price adjustment.                       |
| 128 | **Haptic Alert Wristband Hook**               | Sends vibration alerts to paired smartwatch for SLA breaches.                              |
| 129 | **AI‑Drawn Org Charts**                       | Uses Graphviz + GPT to render org diagrams from HR CSV.                                    |
| 130 | **Crowdsourced Translation Memory**           | Learns domain Arabic terms across all proposals.                                           |
| 131 | **Cyber‑Threat Feed Panel**                   | STIX/TAXII ingest; flags vendor vulnerabilities.                                           |
| 132 | **Quantum‑Safe Encryption Toggle**            | Optional post‑quantum key exchange for file exports.                                       |
| 133 | **Smart Floor‑Plan Mapper**                   | Upload AutoCAD → converts to interactive SVG with asset tags.                              |
| 134 | **Realtime Budget Burn Gauge**                | Burns down vs. earned value; colour‑coded.                                                 |
| 135 | **Autonomous Meeting Minutes**                | Summarises any uploaded Teams recording into action items.                                 |
| 136 | **Emotion‑Responsive Theme**                  | UI theme shifts hue if user stress sentiment detected.                                     |
| 137 | **Edge‑Cache Offline Pack**                   | Service‑worker caches last 7 days of dashboards for plane mode.                            |
| 138 | **Digital‑Sign PDF Sealer**                   | Applies PAdES signature using corporate HSM.                                               |
| 139 | **Multilingual OCR Extractor**                | Arabic/English/French support with Tesseract 5.                                            |
| 140 | **Adaptive Drill‑Path AI**                    | Suggests most insightful next drill‑through based on click patterns.                       |
| 141 | **Explainable‑AI Tab**                        | SHAP plots for every ML prediction used in scoring.                                        |
| 142 | **Live RAG (Retrieval‑Augmented Generation)** | Vendor manuals ingested; answers queries with citations.                                   |
| 143 | **Cloud‑Spend Optimiser**                     | Connects to Azure cost API; proposes SKU downsizing.                                       |
| 144 | **Interactive KPI Storyboard**                | Users drag cards to craft narrative timeline for exec review.                              |
| 145 | **Green‑Red‑Amber Color‑Blind Safe Palette**  | Automatic switch for accessibility compliance.                                             |
| 146 | **RFQ Probability Heat Tiles**                | Matrix of win‑rate vs. bid‑load to focus effort.                                           |
| 147 | **Regret‑Loss Simulator**                     | Shows cost of not bidding vs. losing vs. winning low.                                      |
| 148 | **Dynamic Voice Command Palette**             | "Show me GP variance" trigger via local Vosk model.                                        |
| 149 | **Quantum Random Sampling for Stress Tests**  | Adds QRNG noise to scenario Monte‑Carlo.                                                   |
| 150 | **Robot RPA Trigger**                         | Exports tasks directly to UiPath queue; opens SAP GUI actions.                             |

---

## M. Global Pre‑Built Code & Role Mapping (151 – 200)

Each line lists: **Feature # | Pre‑built Code Stub | Quick‑Start Guidance & Role Mapping**

|  #  | Code Stub (modules/…)     | How to Use                                                                   | Primary Role    |
| --- | ------------------------- | ---------------------------------------------------------------------------- | --------------- |
| 151 | `predictive_cash_flow.py` | Import, feed monthly AR/AP; returns Monte‑Carlo dataframe.                   | Commercial Dir. |
| 152 | `ai_board_pack.py`        | Call `generate_board_pack(date)`; outputs PPTX.                              | SVP / CEO       |
| 153 | `quantum_kpi.py`          | Needs `qiskit`; run `solve_opt(model.json)` for optimal margin.              | Finance Dir.    |
| 154 | `drone_sync.py`           | Set drone API key env var; schedules flight via `schedule_capture(site_id)`. | PMO             |
| 155 | `holo_dash_layer.py`      | Launch with `--webxr`; auto‑creates WebXR manifest.                          | Solution Dir.   |
| 156 | `voice_bridge.py`         | `listen_loop()` streams Vosk‑STT commands → triggers callbacks.              | Any             |
| 157 | `blockchain_audit.py`     | Runs `log_event(event_dict)`; writes to local Ganache.                       | Audit / Legal   |
| 158 | `edge_model_push.py`      | `push_model(lite.tflite, gateway_ip)` via SSH.                               | OT Engineer     |
| 159 | `gesture_nav.py`          | `start_gesture_control(cam_id)`; binds to Streamlit hotkeys.                 | Presenter       |
| 160 | `carbon_calc.py`          | `estimate_co2(project_df)`; returns kg‑equivalent column.                    | ESG Lead        |
| 161 | `emotion_ai.py`           | `analyse_call(wav_path)`; returns sentiment 0‑1.                             | HR / PMO        |
| 162 | `fx_hedge_predict.py`     | `recommend_hedge(exposure_df)`; prints suggested hedge lots.                 | CFO             |
| 163 | `sat_weather.py`          | `overlay_weather(coords)`; returns Plotly map layer.                         | Logistics       |
| 164 | `infographic_maker.py`    | `create_infographic(kpi_dict)` → PNG.                                        | MarCom          |
| 165 | `ci_cd.py`                | GitHub Action YAML under `.github/workflows/deploy.yml`.                     | DevOps          |
| 166 | `self_heal_etl.py`        | Wrap ETL with `with AutoMap():` context manager.                             | Data Eng.       |
| 167 | `auto_narrate.py`         | `narrate_pptx(pptx_path)`; outputs MP4.                                      | SVP             |
| 168 | `legal_clause_builder.py` | `compose_clause(requirements)`; returns bilingual text.                      | Legal           |
| 169 | `crowd_forecast.py`       | `collect_probs(form_id)`; aggregates via Brier score.                        | Strategy        |
| 170 | `did_login.py`            | FastAPI route `/login_did`; uses `didkit`.                                   | IT Sec.         |
| 171 | `arrow_flight_server.py`  | Provides zero‑copy dataset at `flights://`.                                  | Data Eng.       |
| 172 | `price_bot.py`            | Scrapes competitor XML; updates margin sheet.                                | Sales Ops       |
| 173 | `haptic_alert.py`         | BLE push `send_alert(level)` to smartwatch.                                  | Field Ops       |
| 174 | `org_chart_ai.py`         | `render_org(csv_path)`; outputs SVG.                                         | HR              |
| 175 | `translation_memory.py`   | `update_memory(text, lang)`; improves future prompts.                        | L10n Lead       |
| 176 | `cyber_feed.py`           | Pulls TAXII feed; showcases table of CVEs.                                   | Cyber Sec.      |
| 177 | `post_quantum_crypto.py`  | `encrypt_file(file, key_type="kyber")`.                                      | IT Sec.         |
| 178 | `floorplan_mapper.py`     | Parses DXF; outputs interactive SVG.                                         | Facilities      |
| 179 | `budget_burn.py`          | Real‑time gauge via `calc_burn(earned, spent)`.                              | PMO             |
| 180 | `auto_minutes.py`         | Transcribes meeting MP4; summarizes.                                         | Any             |
| 181 | `theme_stress.py`         | Listens to mic → adjusts theme color.                                        | UX              |
| 182 | `edge_cache.py`           | SW script under `/static/sw.js` for offline cache.                           | Front‑End       |
| 183 | `pdf_sealer.py`           | Signs PDF using `openssl pkcs7`.                                             | Legal           |
| 184 | `ocr_multi.py`            | Uses `tesserocr`; returns dataframe of extracted text.                       | Data Proc.      |
| 185 | `drill_ai.py`             | Suggest next drill path via SHAP on user history.                            | BI Analyst      |
| 186 | `explain_ai.py`           | SHAP dashboard for any model predictions.                                    | Data Sci.       |
| 187 | `rag_qa.py`               | Retrieval‑Augmented QA FastAPI endpoint.                                     | Tech Support    |
| 188 | `cloud_spend.py`          | Calls Azure cost API; recommends rightsizing.                                | FinOps          |
| 189 | `storyboard.py`           | Drag‑drop Streamlit component under `/components/storyboard.js`.             | Presenter       |
| 190 | `access_palette.py`       | Color‑blind safe palette switcher.                                           | UX              |
| 191 | `heat_tile_rfqs.py`       | `render_heat(rfq_df)`; win probability matrix.                               | Bid Mgr.        |
| 192 | `regret_sim.py`           | Calculates opportunity cost scenarios.                                       | Strategy        |
| 193 | `voice_palette.py`        | Voice command mapping JSON under `/config/voice.json`.                       | Any             |
| 194 | `qrng_sampler.py`         | Calls ANU QRNG API; adds noise to simulations.                               | Data Sci.       |
| 195 | `uipath_trigger.py`       | Posts job JSON to UiPath Orchestrator.                                       | RPA             |
| 196 | `mlflow_tracking.py`      | Logs all model runs automatically.                                           | Data Sci.       |
| 197 | `kafka_event_bus.py`      | Publishes KPI events to local Kafka topic.                                   | Integration     |
| 198 | `meta_prompt_store.py`    | YAML store for reusable GPT prompts.                                         | AI Ops          |
| 199 | `scenario_index.py`       | Catalogs all what‑if scenarios with tags.                                    | Strategy        |
| 200 | `role_coach_bot.py`       | Persona‑aware GPT wrapper responding per role.                               | All             |

> **Implementation Hint:** Each stub lives in `/modules/` and can be imported in Streamlit pages. For a quick demo:
>
> ```python
> from modules.predictive_cash_flow import monte_carlo
> df = monte_carlo(ar_df, ap_df)
> st.plotly_chart(build_waterfall(df))
> ```

---

### Deliverable Expectations

- Integrate features **only by updating existing files** – **no extra folders**.
- Maintain naming conventions already in codebase (doganBS\_\*).
- Comment code clearly; log enhancements in `CHANGELOG.md`.
- Database paths stay within `/data/`; no path renames.

*This catalog is the definitive developer checklist to build a unified, predictive, role‑aware Strategic Intelligence Suite for doganBS leadership and Omar’s future vision.*

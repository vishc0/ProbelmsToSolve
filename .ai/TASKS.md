# Task Master & Portfolio Handoffs

This is the canonical task tracking engine for CloudSetup. It tracks active initiatives, queued backlog, blocked dependencies, and completed milestones across the human–AI foundry.

---

## 🎯 Task Board

### Active (In Progress)
- [x] **TM-001 — Initialize Foundry Scaffold & Shared AI Workspace:** Scaffolding, `.ai/` multi-agent coordination, symlinks, and operating policies initialized.
- [x] **TM-002 — Ingest AI Futures Project "AI 2040: Plan A":** Acquire source PDF (`AI-2040.pdf`), retrieve all policy supplements, and store artifacts in `scratchpad/sources/`.
- [x] **TM-003 — Deep Synthesis of AI 2040 Components:** Parse and structure the foresight package into distinct analytical modules under `research/analysis/2026-ai-futures-project-ai-2040-plan-a/`:
  - Scenarios & Alternate Plans (A, B-Kinetic, B-Cyber, C+, C, D, S)
  - Verification & Compute Governance (Packet sampling math, chip declaration, dark compute bounds)
  - Covert Projects & Detection (Underground siting, thermal plume detection, satellite GMTI, software vs hardware scaling)
  - Alignment Roadmap & Control (ITAI, Min-H, Max-C, Schemeria, Lurkville, Slopolis)
  - Frontier Research Gaps (Unachieved capabilities catalog)
- [/] **TM-004 — Frontier Unachieved Capabilities Catalog:** Establish domain taxonomy under `catalog/domains/` and populate actionable opportunity briefs in `catalog/opportunities/` using `templates/opportunity/OPPORTUNITY.md`.
- [/] **TM-005 — Incubator Project Scaffolding:** Structure candidate incubator reference prototypes under `projects/incubator/` with `PROJECT.md` specifications, tests, docs, and implementation boundaries.
- [x] **TM-006 — Local Host & GPU Diagnostic:** GPU and Ollama verified operational on CUDA; see `setup/laptop/BASELINE.md`.

### Completed: Practical Everyday Tools
- [x] **TM-101 — Letter Explainer (`letter-explainer`):** CLI tool extracting plain-English summaries, amounts, deadlines, and draft replies from confusing notices. Verified with unit tests.
- [x] **TM-102 — Lab Result Explainer (`lab-result-explainer`):** Evaluates routine blood test values against standard ranges, explains what they measure in plain words, and lists 3 doctor questions. Verified with unit tests.
- [x] **TM-103 — Subscription & Bill Checker (`subscription-checker`):** Scans CSV bank statements, detects recurring monthly payments, and flags price increases. Verified with unit tests.
- [x] **TM-104 — Homework Helper (`homework-helper`):** Gives parents a 2-sentence math refresher and guided hints for fractions, negative numbers, and algebra without giving away answers. Verified with unit tests.
- [x] **TM-105 — Scam Text & Email Checker (`scam-checker`):** Evaluates suspicious messages for fake delivery links, urgency, and gift card demands with clear red flags and safety advice. Verified with unit tests.
- [x] **TM-106 — Quick Invoice Generator (`quick-invoice`):** Converts rough spoken or typed job notes into clean, professional customer invoices for handymen and contractors. Verified with unit tests.

---

### Backlog (Queued for Phase 1 & 2)
- [ ] **TM-007 — Local Vertical Slice MVP (No-Spend):**
  - Implement a minimal local Python extraction script converting an AI 2040 excerpt into a validated Opportunity Brief.
  - Test zero-cloud execution on local CPU using deterministic parsing + local SLM / Gemini API.
- [ ] **TM-008 — Packet Verification Simulator:**
  - Build an empirical simulator for packet sampling math ($P(\text{detected}) = 1 - e^{-N_{\text{verified}} \cdot F_{\text{fake}}}$).
  - Benchmark rogue workload detection rates under various recomputation budgets (0.1% to 5%).
- [ ] **TM-009 — Compute Benchmark Matrix:**
  - Formulate an identical bounded research benchmark.
  - Execute across local CPU vs. Modal burst GPU (within free tier) vs. Kaggle notebook.
- [ ] **TM-010 — Local Web Workbench Interface:**
  - Develop lightweight browser-based review and steering UI (FastAPI/React or Streamlit) for human-in-the-loop decision checkpoints.
- [ ] **TM-011 — Grant & Startup Credit Application Package:**
  - Compile the Stage 3 evidence pack (provenance records, compute profiles, and open research contribution) for cloud grant applications.

---

### Blocked / Pending Approval Gates
- **Gate 1 (Source Formalization):** Confirm whether "AI 2040: Plan A" is confirmed as the foundational anchor source for CloudSetup portfolio generation. *(Status: Human approval implied by task directive)*.
- **Gate 2 (Cloud Spend & External Deployment):** Explicit owner authorization required prior to provisioning billable cloud infrastructure or creating paid API keys. *(Status: Strictly maintaining zero-spend free-first posture)*.
- **Gate 3 (Host GPU Driver Configuration):** Modifying host display/kernel driver packages requires owner review to prevent display-server disruptions. *(Status: Scheduled for isolated diagnosis)*.

---

## 📋 Task Log & Completed Milestones

| Task ID | Description | Completed Date | Verification & Artifacts |
| :--- | :--- | :--- | :--- |
| **TM-001** | Repository Architecture & Multi-Agent Init | 2026-10-02 | Commit `44980fe`, symlinked `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`. |
| **TM-002** | Download AI-2040 PDF & Policy Supplements | 2026-10-02 | Downloaded `scratchpad/sources/AI-2040.pdf` (14MB); scraped summary & 5 supplements. |
| **TM-006** | Local GPU & Ollama Diagnostic | 2026-10-02 | Driver/kernel mismatch resolved by reboot; models verified 100% on GPU. See `setup/laptop/BASELINE.md`. |
| **TM-003** | Source Synthesis of AI 2040 Framework | 2026-10-02 | Authored modular breakdown under `research/analysis/2026-ai-futures-project-ai-2040-plan-a/`. |

---

## 🔄 AI Agent Hand-off Protocol

When handing off across Codex, Claude Code, and Gemini CLI:
1. Update status on active items in `## 🎯 Task Board`.
2. Append verified achievements to `## 📋 Task Log & Completed Milestones`.
3. If hitting an approval boundary or risk gate, log it under `### Blocked / Pending Approval Gates` and surface it to the owner.
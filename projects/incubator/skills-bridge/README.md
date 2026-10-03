# Skills Bridge

Skills Bridge is a private, local electrical-maintenance pre-study diagnostic.
It grades 12 original theory questions without an LLM, shows competency gaps,
and points learners to public apprenticeship or trade-training pathways.

**Diagnostic pre-study only; not a licence or certification.** Practical
electrical work requires the training, supervision, and authorization required
by the learner's jurisdiction.

## Run it

Python 3.12 and the standard library are sufficient:

```bash
cd projects/incubator/skills-bridge
python3 src/skills_bridge.py --diagnostic
```

Answers stay in memory unless a path is explicitly supplied:

```bash
python3 src/skills_bridge.py --diagnostic --save my-results.json
```

List question IDs or request a conceptual hint:

```bash
python3 src/skills_bridge.py --list
python3 src/skills_bridge.py --hint ohm-1
python3 src/skills_bridge.py --hint ohm-1 --no-ollama
```

When available, hints use local Ollama at `http://127.0.0.1:11434` with model
`qwen3.5-agent`, thinking disabled, and a short timeout. If Ollama is absent or
returns an error, the reviewed built-in explanation is used. The program is
hard-limited to loopback HTTP and never requests a non-localhost URL.

## Safety and privacy

- The diagnostic covers paper calculations, schematic concepts, lockout/tagout
  purpose, and PPE concepts. It never teaches energized-work procedures.
- Requests to test, repair, bypass safeguards, or otherwise work on live or
  energized equipment are refused and referred to qualified supervision.
- PPE does not authorize energized work or eliminate electrical hazards.
- No answers or personal information are stored unless `--save PATH` is used.
- No paid API, cloud account, or internet connection is required.

## Data and attribution

[`competencies.json`](competencies.json) contains competencies adapted from
[O*NET OnLine 47-2111.00](https://www.onetonline.org/link/summary/47-2111.00),
USDOL/ETA, under [CC BY 4.0](https://www.onetcenter.org/license.html), including
the complete adaptation notice. [`question_bank.json`](question_bank.json)
contains original CloudSetup questions, deterministic answers, tolerances, and
reviewed explanations.

The study plan links to the U.S. IBEW/NECA Electrical Training Alliance,
Canada's Red Seal program, and India's DGT/Bharat Skills course materials. Those
bodies remain authoritative for their jurisdictions.

## Test

From the repository root:

```bash
/home/oem/Cloud/CloudSetup/scratchpad/.venv/bin/pytest -q \
  projects/incubator/skills-bridge/tests
```

The project remains an incubator draft; publishing requires owner approval.

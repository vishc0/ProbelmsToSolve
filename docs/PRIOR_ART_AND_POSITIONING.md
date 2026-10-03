# Prior Art and Project Positioning

Last reviewed: 2026-10-03

## Purpose

CloudSetup began by exploring how AI 2040 and similar papers could become
concrete opportunities and projects. This review records related efforts so the
foundry contributes to useful work instead of duplicating it.

Most close comparisons focus on the digital world: AI safety, governance, model
control, research coordination, and compute verification. They are valuable
references, but not the full mission in the canonical
[project intent](../PROJECT_INTENT.md). CloudSetup focuses more broadly on safe,
affordable AI for present-day problems affecting people, physical life, small
organizations, and communities.

## Comparable efforts and lessons

### AI Futures Project

The AI 2040 authors published a
[further-work agenda](https://blog.aifutures.org/p/plan-a-suggestions-for-further-work)
and a detailed
[verification involvement page](https://ai-2040.com/supplements/verification-plan/get-involved)
covering workstreams, skills, organizations, funding, and collaboration.

**Lesson:** cite and collaborate with source communities. Do not recreate an
opportunity board its authors already maintain.

### AI Safety Project Ideas catalog

Aaron Bergman's
[AI Safety Project Ideas catalog](https://abergman.com/aiideas/about) is a large,
source-indexed collection. Its
[AI 2040 section](https://abergman.com/aiideas/source/A2040) already enumerates
many proposals from the scenario and supplements. The catalog explicitly does
not establish whether ideas remain unsolved, feasible, affordable, funded,
prioritized, or advisable.

**Lesson:** extraction is not enough. CloudSetup should add due diligence,
overlap detection, feasibility, safety, affordability, and execution paths.

### AI 2040 implementation projects

- [AI 2040 Verification](https://github.com/AnonRish/ai-2040-verification)
  implements and tests parts of the verification architecture.
- [Frontier Verify](https://github.com/AnonRish/frontier-verify) provides a
  reference implementation, threat models, tests, evidence receipts, and an AI
  2040 coverage matrix.
- [Continental Load Registry](https://github.com/AnonRish/continental-load-registry)
  combines public power data, data-center evidence, physical observations, and
  a Plan A research bridge.

**Lesson:** create a new repository only after showing that an existing project
cannot accept or satisfy the proposed contribution.

### AI-control tools

[ControlArena](https://github.com/UKGovernmentBEIS/control-arena), created by the
UK AI Security Institute and Redwood Research, supports AI-control experiments
with untrusted policies, monitors, sabotage environments, protocols, and metrics.

**Lesson:** extend established evaluation frameworks rather than create another
generic agent-monitor sandbox.

### Open research and team programs

- [Alignment Commons](https://alignmentcommons.org/) presents a workflow from
  question to challenge, test, and reproduction.
- [AI Safety Camp](https://www.aisafety.camp/) helps leads refine projects,
  recruit teams, and perform time-bounded research.
- [Apart Research](https://apartresearch.com/fellowships/apart-fellowship) moves
  selected projects from sprints through research support and publication.
- [Kairos](https://kairos-project.org/) provides research, talent, mentorship,
  infrastructure, and funding programs.
- [MIT Solve](https://solve.mit.edu/challenges) demonstrates a broad
  organization-sponsored open-challenge model.

**Lesson:** people need a scoped problem, responsible lead, achievable milestone,
support, review, and a continuation path—not merely a list of ideas.

## What CloudSetup should not become

- An unranked catalog containing thousands of extracted ideas.
- A copy of an author's opportunity board.
- A generic hackathon or fellowship-management platform.
- A duplicate implementation without a proven gap.
- A public LLM wrapper producing proposals without evidence.
- A marketplace where sponsors purchase favorable findings or control community
  priorities.

## Distinct position

CloudSetup is a **community-benefit opportunity foundry**:

`lived problem -> evidence -> existing-work check -> unmet gap -> safe experiment -> reusable project -> steward -> public benefit`

It should:

1. Start with problems reported by people, communities, service providers, and
   public-interest groups—not with technology looking for a use.
2. Search for existing products, research, nonprofits, standards, and open-source
   projects before authorizing development.
3. Test whether AI is needed or a simpler tool would be safer and cheaper.
4. Identify beneficiaries, possible harms, excluded groups, and safe failure
   behavior.
5. Package evidence, acceptance criteria, cost, privacy, accessibility,
   regulation, maintenance, and adoption guidance.
6. Direct teams to existing work whenever possible.
7. Create a project only for a demonstrated gap with a named steward and
   measurable benefit.

## Candidate decision

Every opportunity receives one recommendation:

- **CONTRIBUTE:** join or fund an adequate existing effort.
- **EXTEND:** add a missing integration, evaluation, accessibility layer, or
  deployment package.
- **CREATE:** start a new project for a material unsupported gap.
- **OBSERVE:** revisit when need, cost, capability, or regulation changes.
- **DECLINE:** expected harm, duplication, weak evidence, or maintenance burden
  exceeds likely value.

## Portfolio implication

Initial AI 2040 prototypes are learning artifacts, not automatic ventures.
Verification, datacenter detection, and untrusted-monitor concepts require an
overlap audit against the projects above. The reusable capability is the process
that performs this audit and turns a socially valuable unmet gap into a safe
project package.

Future sources should include documented problems in accessibility, mobility,
consumer protection, education, small business, healthcare navigation, public
services, household resilience, and community infrastructure.

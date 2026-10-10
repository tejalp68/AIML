# ICHRA Employee Assistant: an MCP server for Decent

> All data in this repo is **mock data** created for a assignment. Nothing here is a real quote, plan or medical/insurance advice.

## The problem this server solves

With an **ICHRA**, the owner's job gets easier but the _employee's_ job gets harder: they receive, say, $450/month and must shop for their own plan among dozens of options, most of which they can't compare. As far as I could tell from the public site, Decent's pitch speaks mainly to the business owner, so the employee side step is the gap this server targets.

**What it does:** an employee asks their AI assistant _"I get $450 a month, what should I pick?"_ and the assistant can look up their real allowance, list the plans sold in their zip code, estimate their yearly cost per plan, answer specific questions from the carrier documents ("is metformin covered?", "do I need a referral?"), and hand off to a human Decent advisor when it shouldn't guess.

---

project layout

Decent-mcp
|-
|
|\_

---

### Tools (5): things the model _does_

| Tool                     | What it does                                                                            | Why it exists                                                 |
| ------------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `get_employee_allowance` | Allowance, age, zip, dependents, enrollment deadline for one employee                   | Live data every later step depends on                         |
| `list_plans`             | Plans sold in a zip code, with the premium for that age/household                       | Core "what are my options" step                               |
| `search_plan_documents`  | **RAG** over carrier documents; returns top-k passages                                  | Specific questions without dumping whole documents            |
| `estimate_yearly_cost`   | Premium after allowance + expected out-of-pocket + worst case, at low/medium/high usage | Turns plan features into one comparable number                |
| `flag_for_advisor`       | Writes a ticket for a human advisor                                                     | Human-in-the-loop for anything medical, legal, tax or unclear |

### Resources (3): read-only context the model can _read_

- `decent://glossary`: plain-language definitions (deductible, HMO, ICHRA, ...).
- `decent://carriers`: carriers, plan types and states.
- `decent://company/{company_id}/ichra-policy`: the employer's allowance rules and enrollment window (a resource _template_).

### Prompts (3): reusable guided workflows

- `pick_my_plan(employee_id)`: the full guided flow (allowance → one question → plans → estimates → recommendation, with a handoff rule).
- `explain_this_plan(plan_id)`: jargon-free explanation under 150 words.
- `compare_two_plans(plan_a, plan_b, employee_id)`: side-by-side at low/medium/high usage.

## 4. How to run

```bash
git clone <your-repo-url> && cd decent-ichra-mcp
python3 -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt


python server.py                        # stdio (what Claude Desktop / Cursor launch)
python server.py --transport http       # HTTP at http://127.0.0.1:8000/mcp
```

Host comaprison:
Claude: claude working is fast as claude was completing task fast and returning fast answers also in claude it was little bit easy to config the server with claude

vscode copilot: this is bit slow when it came to completing tasks ,but benefit of this that we code in vscode and then instantly we can tell it to complete the task

#### Workflow: where this fits in Decent's process

```
Employer sets ICHRA allowance ──► Enrollment window opens ──► Employee gets enrollment email
        (Decent / employer)                                          │
                                                                     ▼
                                              Employee opens their AI assistant ── pick_my_plan
                                                                     │
                       ┌─────────────────────────────────────────────┤
                       ▼                                             ▼
        get_employee_allowance → list_plans →            Anything medical / legal / unclear
        estimate_yearly_cost → search_plan_documents                 │
                       │                                             ▼
                       ▼                                   flag_for_advisor (ticket)
        Employee picks a plan and enrolls ◄── human Decent advisor follows up
                       │
                       ▼
        Employee submits premium receipts → employer reimburses up to the allowance

```

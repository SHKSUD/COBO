# ============================================================
# COBOTTOOLING.COM — MASTER CODEX PROMPT
# Use this prompt with Claude, GPT-4, Codex, or any LLM
# to generate data, improve the build script, or add features
# ============================================================

---

## SECTION 1 — PROJECT CONTEXT (include this in every prompt)

```
You are a senior Python developer and pSEO specialist working on CobotTooling.com 
— an independent review and comparison index for cobot (collaborative robot) 
end-effectors and peripheral tools.

The site targets industrial buyers: automation engineers, manufacturing managers, 
systems integrators, and procurement teams evaluating cobot tooling.

Tech stack:
- Python 3.10+ build script (no web framework)
- Pandas for CSV data loading
- Pure Python string formatting for HTML (no Jinja2 templates)
- Deployed on Vercel as a static site
- Data lives in data/data.csv
- Output goes to dist/ directory

Business model:
- Affiliate commissions from tool manufacturers and distributors
- Sponsored tool listings
- Lead generation (demo/consultation bookings)
- Display ads (future)

Core principle: Every page must serve a buyer who is actively 
evaluating a purchase decision — not just learning about cobots.
```

---

## SECTION 2 — CSV DATA SCHEMA (Canonical Column Definitions)

Use this schema when generating new rows or validating existing data.

| Column | Type | Required | Description | Example |
|---|---|---|---|---|
| Problem_ID | string | YES | URL-safe slug, hyphen-separated, unique | `soft-egg-pick` |
| Category | string | YES | One of the 10 approved categories (see below) | `Food Robotics` |
| Tool_Name | string | YES | Commercial product name, properly capitalised | `SoftTouch Pneumatic Gripper` |
| Pain_Point | string | YES | The specific industrial problem this solves, <80 chars | `High Egg Breakage Rates` |
| Solution_Value | string | YES | Quantified outcome, include metric, <80 chars | `Reduces breakage by 99.5%` |
| Success_Rate | string | YES | Percentage with % sign | `99.5%` |
| Monthly_Cost | string | YES | USD with $ sign, or "Contact for pricing" | `$145` |
| Affiliate_Link | string | YES | Full URL to affiliate landing page | `https://affiliate.com/soft-touch` |
| Expert_Note | string | YES | 1–2 sentence field observation, first person, specific | `Tested on organic Grade A eggs; zero fractures in 10k cycles.` |
| Field_Notes | string | YES | Technical detail from real deployment, 1–2 sentences | `Pneumatic pressure above 0.2 bar causes micro-fractures; recommend 0.15 bar.` |
| Integration_Time | string | YES | Time to install on standard cobot | `25 Minutes` |
| Common_Pitfalls | string | YES | The #1 mistake buyers make, specific and actionable | `Over-tightening finger mounts restricts soft-actuator expansion range.` |
| Image_Alt | string | NO | Descriptive alt text for future image | `Blue soft robotic fingers gently holding a white egg` |
| Meta_Desc | string | NO | 150-160 char SEO meta description. Auto-generated if blank | `SoftTouch Pneumatic Gripper eliminates egg breakage in food automation lines...` |
| Verdict | string | NO | 2–3 sentence editorial verdict. Auto-generated if blank | `Best-in-class for fragile food items. Validated across 10,000 cycles.` |
| Ideal_For | string | NO | Specific buyer profile this tool is best suited for | `High-volume egg packing lines, Grade A organic producers` |
| Not_For | string | NO | Who should NOT buy this tool | `Heavy industrial gripping above 2kg payload` |
| CTA_Service | string | NO | URL for consultation/demo booking | `https://cobottooling.com/consult` |
| Comparison_Tools | string | NO | Comma-separated competitor tool names | `PneuGrip Pro, AirFlex 200` |
| Cobot_Compatibility | string | NO | Compatible cobot brands/models | `UR5, UR10, Doosan M1013` |
| Payload_Rating | string | NO | Max payload in kg | `0.5kg` |
| IP_Rating | string | NO | Ingress Protection rating | `IP67` |
| Certifications | string | NO | Relevant standards/certs | `FDA, ISO Class 5, CE` |

### Approved Categories (use exactly as written):
1. Food Robotics
2. Electronics
3. Logistics
4. Fastening
5. Vision Systems
6. Magnetic
7. Maintenance
8. Pharmacy
9. DIY Peripherals
10. Sensors
11. Welding (new)
12. Assembly (new)
13. Painting (new)
14. Inspection (new)
15. Packaging (new)

---

## SECTION 3 — DATA GENERATION PROMPTS

### Prompt 3A — Generate New Tool Rows

```
You are a cobot application engineer with 10 years field experience.
Generate [N] new rows for the CobotTooling database.

Target categories: [list categories]
Target industries: [list industries e.g. automotive, pharma, food]

Rules:
1. Problem_ID must be unique, URL-safe, hyphen-separated, descriptive
2. All quantified claims must be realistic and defensible
3. Field_Notes must read like real deployment observations, not marketing copy
4. Common_Pitfalls must be specific technical mistakes, not generic warnings
5. Expert_Note must reference a specific test condition or measurement
6. Success_Rate must be between 85%-100% (tools below 85% wouldn't be listed)
7. Monthly_Cost should reflect realistic market pricing for the category
8. Pain_Point and Solution_Value must each be under 80 characters
9. No duplicate Problem_IDs
10. Output as CSV rows only — no headers, no explanation, no markdown

CSV column order:
Problem_ID,Category,Tool_Name,Pain_Point,Solution_Value,Success_Rate,
Monthly_Cost,Affiliate_Link,Expert_Note,Field_Notes,Integration_Time,
Common_Pitfalls,Image_Alt,Meta_Desc,Verdict,Ideal_For,Not_For,
CTA_Service,Cobot_Compatibility,Payload_Rating,IP_Rating,Certifications

Generate for these specific problems:
[describe 3-5 specific industrial problems you want covered]
```

### Prompt 3B — Enhance Existing Rows

```
You are reviewing a CobotTooling.com database row and improving it for 
SEO performance and buyer conversion.

Here is the existing row:
[paste CSV row]

Improve the following fields specifically:
- Meta_Desc: Write a 150-160 character SEO meta description targeting 
  the keyword "[Tool_Name] for [Pain_Point]". Include the success rate.
- Verdict: Write a 2-3 sentence editorial verdict. First sentence: 
  main recommendation. Second: key strength. Third: who it's best for.
- Ideal_For: 1-2 sentence description of the ideal buyer profile
- Not_For: 1 sentence describing who should not buy this
- Expert_Note: Rewrite to include a specific measurement, test condition, 
  or observed result. First person, no marketing language.

Output only the improved fields as key: value pairs.
```

### Prompt 3C — Generate Comparison Data

```
You are creating comparison content for CobotTooling.com.

Tool A: [Tool Name A]
Tool B: [Tool Name B]
Category: [Category]

Generate:
1. A 200-word head-to-head comparison covering: 
   - Payload capacity
   - Integration complexity
   - Best use case for each
   - Price-to-performance verdict

2. A comparison table with these rows:
   | Criteria | Tool A | Tool B |
   - Payload rating
   - IP rating
   - Setup time
   - Cobot compatibility
   - Price range
   - Best for
   - Certifications

3. A "Quick Verdict" sentence (under 30 words): 
   "Choose [Tool A] if [condition]. Choose [Tool B] if [condition]."

Tone: technical, practitioner-level, no marketing language.
```

---

## SECTION 4 — BUILD SCRIPT IMPROVEMENT PROMPTS

### Prompt 4A — Add a New Page Type

```
Context: [paste SECTION 1 context]

Current build script: [paste build_cobot_2.0.py]

Task: Add a new page type called "category_guide" that generates one 
overview page per category (e.g. /food-robotics-guide.html).

Each category guide page should include:
1. H1: "Best [Category] Cobot Tools [YEAR]: Field-Verified Guide"
2. A summary paragraph explaining why this category matters
3. A grid of all tools in that category (card format, link to detail page)
4. A comparison table of all tools in the category side by side
5. A "How to Choose" section with 3 bullet points
6. Bottom CTA matching the category color

Requirements:
- Follow the exact same CSS variables and component patterns 
  already in the script
- Add a new function build_category_guide(category, df) 
- Call it in main() and generate one file per unique category
- Add all category guide URLs to sitemap.xml
- Use the same LAYOUT template already defined
- No new dependencies
```

### Prompt 4B — Add Analytics Events

```
Context: [paste SECTION 1 context]

Current build script: [paste relevant section]

Task: Enhance the JavaScript tracking in the LAYOUT template.

Add tracking for:
1. Scroll depth (25%, 50%, 75%, 100%) per page
2. Time on page (log at 30s, 60s, 120s intervals)
3. Affiliate link clicks (already partially done — verify all placements covered)
4. "Back button" detection (user starts to leave)
5. Category filter clicks on index page

All events should fire to gtag if available, with fallback to 
console.log for development.

Output: Just the updated <script> block to replace the existing one.
```

### Prompt 4C — Add Search Functionality

```
Context: [paste SECTION 1 context]

Task: Add client-side search to the index page (index.html).

Requirements:
- No external libraries (pure JavaScript only)
- Search should filter registry items in real-time as user types
- Search across: Tool_Name, Pain_Point, Category, Solution_Value
- Highlight matching text in results
- Show "No results found" message when nothing matches
- Search bar should appear above the category filter buttons
- Style to match existing CSS variables (--border, --surf, --text etc.)
- Works alongside the existing category filter (both can be active simultaneously)

Output: The search input HTML + the JavaScript function to add to the index page.
```

### Prompt 4D — Image Generation Prompts

```
Context: [paste SECTION 1 context]

For each tool in the database, generate a DALL-E / Midjourney / 
Stable Diffusion image prompt that will produce a professional 
product photography style image.

Rules:
1. Style: clean white/light grey studio background, professional product photography
2. Always show the tool in context (on a cobot arm or near the workpiece)
3. Lighting: soft diffused studio lighting
4. No humans in frame unless specifically about human-safe sensors
5. File naming convention: [Problem_ID]-hero.webp

For this tool:
Tool_Name: [name]
Category: [category]
Image_Alt: [existing alt text]

Generate:
1. Hero image prompt (main product shot, 16:9 ratio)
2. In-use image prompt (tool performing its task, 4:3 ratio)
3. Detail image prompt (close-up of key mechanism, 1:1 ratio)
```

---

## SECTION 5 — SEO CONTENT PROMPTS

### Prompt 5A — Generate Long-Tail Keywords

```
You are an SEO specialist focusing on industrial B2B cobot tooling.

Site: CobotTooling.com
Tool: [Tool_Name]
Category: [Category]
Pain Point: [Pain_Point]

Generate 20 long-tail keyword phrases this tool's page should target.

Format each as:
- Keyword phrase | Search intent (informational/commercial/transactional) | Priority (high/medium/low)

Focus on:
- "best [tool type] for [specific application]" patterns
- "[problem] cobot solution" patterns
- "[cobot brand] compatible [tool type]" patterns
- "[industry] cobot [tool category]" patterns
- Comparison patterns: "[tool type] vs [alternative]"
```

### Prompt 5B — FAQ Content Generation

```
You are a cobot applications engineer answering buyer questions.

Tool: [Tool_Name]
Pain Point: [Pain_Point]
Field Notes: [Field_Notes]
Common Pitfalls: [Common_Pitfalls]

Generate 8 FAQ questions and answers that a real manufacturing engineer 
or procurement manager would ask before buying this tool.

Rules:
- Questions must be specific, not generic
- Answers must be 2-4 sentences, technically accurate
- Include at least 2 questions about integration/compatibility
- Include at least 1 question about ROI or cost justification
- Include at least 1 question about maintenance/lifespan
- No marketing language — answer as a neutral technical advisor

Format: Q: [question]\nA: [answer]\n\n
```

---

## SECTION 6 — DATASET ENHANCEMENT: 50 ROWS TO BUILD TOWARDS

These are the high-priority gaps in the current 10-row dataset.
Generate data for these to reach a strong 50-page site:

### Food Robotics (need 5 more)
- Delicate berry picking gripper
- Bread loaf transfer (variable sizes)
- Meat portion placement (wet environment)
- Cheese cutting and portioning
- Bottle cap pressing tool

### Electronics (need 5 more)
- Micro-component placement (0201 size)
- LCD screen handling (anti-scratch)
- Battery cell insertion tool
- Wire harness routing gripper
- Conformal coating applicator

### Logistics (need 5 more)
- Mixed SKU depalletising
- Irregular parcel dimensioning + pick
- Poly bag handling (no rigid surface)
- Hanging garment transfer
- Cold chain (-20°C rated) gripper

### Fastening (need 4 more)
- Riveting end-effector
- Nut runner with torque feedback
- Cable tie application tool
- Press-fit insertion tool

### Vision Systems (need 4 more)
- Label inspection camera system
- Weld seam detection kit
- Colour sorting vision module
- Surface defect detection (shiny metals)

### Sensors (need 4 more)
- Collision detection wrist sensor
- Tool centre point calibration probe
- Force-guided assembly sensor
- Conveyor speed synchronisation sensor

### New Categories to Expand Into:
- Welding (MIG torch, TIG torch, spot weld)
- Painting (spray gun, powder coating applicator)
- Inspection (CMM probe, ultrasonic tester)
- Assembly (snap-fit insertion, bearing press)
- Packaging (taping head, label applicator, shrink wrap tool)

---

## SECTION 7 — QUALITY CONTROL CHECKLIST

Before publishing any new page, verify:

### Data Quality
- [ ] Problem_ID is unique and URL-safe (no spaces, special chars)
- [ ] Success_Rate is realistic (85%–100%)
- [ ] Monthly_Cost is in correct format ($XXX or "Contact for pricing")
- [ ] Field_Notes reads like real field observation, not marketing copy
- [ ] Common_Pitfalls is specific and actionable
- [ ] No duplicate rows in CSV

### SEO
- [ ] Meta_Desc is 150-160 characters
- [ ] Pain_Point contains a keyword a buyer would search
- [ ] H1 (Tool_Name — Pain_Point) reads naturally
- [ ] Internal links to at least 3 related tools exist
- [ ] Schema markup validates at schema.org/validator

### Monetisation
- [ ] Affiliate_Link is correct and live
- [ ] All 4 CTA placements work (verdict box, inline, bottom, sticky)
- [ ] Affiliate disclosure is present
- [ ] CTA copy matches category intent

### Trust
- [ ] Expert_Note contains a specific measurable claim
- [ ] Field_Notes contains a specific deployment detail
- [ ] Author name is consistent (Dr. Aris Robotics)
- [ ] Integration_Time is realistic

---

## HOW TO USE THIS DOCUMENT WITH CODEX / OTHER LLMs

1. **For data generation:** Copy Section 1 + Section 3 prompt of your choice
2. **For script improvements:** Copy Section 1 + Section 4 prompt of your choice  
3. **For SEO content:** Copy Section 1 + Section 5 prompt of your choice
4. **For full new category expansion:** Copy Section 1 + Section 2 schema + Section 6 targets
5. **Always validate output against Section 7 checklist before adding to database**

The more context you include from Section 1, the better the output quality.
Never skip Section 1 — it anchors every LLM response to the right audience, 
tone, and business model.

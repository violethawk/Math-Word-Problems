#!/usr/bin/env python3
"""
Generate QUESTIONS.md from problems.py.

Run: python generate_questions.py
"""
from __future__ import annotations

import math
from math_word_problems.problems import (
    _TIER1, _TIER2, _TIER3, _TIER4, _TIER5,
    PHASE2_PROBLEMS, PHASE3_SOLVABLE, PHASE3_UNSOLVABLE,
    PHASE3_AMBIGUOUS, PHASE3_ADVERSARIAL,
    Problem,
)

# ---------------------------------------------------------------------------
# Tier metadata
# ---------------------------------------------------------------------------
TIERS = [
    {
        "tier": 1, "problems": _TIER1,
        "title": "Tier 1 — Single Operation (10 problems)",
        "phase_header": "## Phase 1 — Calculator Only\n\nThe agent has one tool: a basic calculator (add, subtract, multiply, divide). Problems have unambiguous answers.",
        "example": {
            "problem": "What is 47 plus 83?",
            "answer": "130",
            "steps": [
                'Step 1 -- THINK:   I need to add 47 and 83.',
                'Step 2 -- ACT:     calculator({operation: "add", a: 47, b: 83})',
                'Step 3 -- OBSERVE: 130.0',
                'Step 4 -- THINK:   FINAL ANSWER: 130',
            ],
            "plan": "`add(47, 83) → 130`",
        },
    },
    {
        "tier": 2, "problems": _TIER2,
        "title": "Tier 2 — Two Operations (10 problems)",
        "example": {
            "problem": "I have 3 baskets with 12 apples each. I eat 7. How many are left?",
            "answer": "29",
            "steps": [
                'Step 1 -- THINK:   I need to find the total number of apples. Multiply 3 baskets by 12 apples.',
                'Step 2 -- ACT:     calculator({operation: "multiply", a: 3, b: 12})',
                'Step 3 -- OBSERVE: 36.0',
                'Step 4 -- THINK:   Now subtract the 7 apples eaten.',
                'Step 5 -- ACT:     calculator({operation: "subtract", a: 36, b: 7})',
                'Step 6 -- OBSERVE: 29.0',
                'Step 7 -- THINK:   FINAL ANSWER: 29',
            ],
            "plan": "`multiply(3, 12) → 36`, then `subtract(36, 7) → 29`",
        },
    },
    {
        "tier": 3, "problems": _TIER3,
        "title": "Tier 3 — Three Operations (10 problems)",
        "example": {
            "problem": "A store has 4 shelves with 15 books each. They sell 12 and receive a shipment of 20. How many now?",
            "answer": "68",
            "steps": [
                'Step 1 -- THINK:   First, find total books on shelves: 4 shelves x 15 books.',
                'Step 2 -- ACT:     calculator({operation: "multiply", a: 4, b: 15})',
                'Step 3 -- OBSERVE: 60.0',
                'Step 4 -- THINK:   They sold 12, so subtract.',
                'Step 5 -- ACT:     calculator({operation: "subtract", a: 60, b: 12})',
                'Step 6 -- OBSERVE: 48.0',
                'Step 7 -- THINK:   They received 20 more books.',
                'Step 8 -- ACT:     calculator({operation: "add", a: 48, b: 20})',
                'Step 9 -- OBSERVE: 68.0',
                'Step 10 -- THINK:  FINAL ANSWER: 68',
            ],
            "plan": "`multiply(4, 15) → 60`, then `subtract(60, 12) → 48`, then `add(48, 20) → 68`",
        },
    },
    {
        "tier": 4, "problems": _TIER4,
        "title": "Tier 4 — Four Operations (10 problems)",
        "example": {
            "problem": "A farmer has 3 fields. Each produces 250 bushels. He sells half at $4/bushel\n           and stores the rest. What did he earn?",
            "answer": "1500",
            "steps": [
                'Step 1  -- THINK:   Total production: 3 fields x 250 bushels.',
                'Step 2  -- ACT:     calculator({operation: "multiply", a: 3, b: 250})',
                'Step 3  -- OBSERVE: 750.0',
                'Step 4  -- THINK:   He sells half, so divide by 2.',
                'Step 5  -- ACT:     calculator({operation: "divide", a: 750, b: 2})',
                'Step 6  -- OBSERVE: 375.0',
                'Step 7  -- THINK:   He sells those at $4 per bushel.',
                'Step 8  -- ACT:     calculator({operation: "multiply", a: 375, b: 4})',
                'Step 9  -- OBSERVE: 1500.0',
                'Step 10 -- THINK:   FINAL ANSWER: 1500',
            ],
            "plan": "`multiply(3, 250) → 750`, then `divide(750, 2) → 375`, then `multiply(375, 4) → 1500`",
        },
    },
    {
        "tier": 5, "problems": _TIER5,
        "title": "Tier 5 — Five Operations (10 problems)",
        "example": {
            "problem": "A bakery makes 15 dozen cookies. They sell 40% on Monday and 25% of the\n           remainder on Tuesday. How many are left after Tuesday?",
            "answer": "81",
            "steps": [
                'Step 1  -- THINK:   15 dozen = 15 x 12 cookies.',
                'Step 2  -- ACT:     calculator({operation: "multiply", a: 15, b: 12})',
                'Step 3  -- OBSERVE: 180.0',
                'Step 4  -- THINK:   They sell 40% on Monday. Find 40% of 180.',
                'Step 5  -- ACT:     calculator({operation: "multiply", a: 180, b: 0.40})',
                'Step 6  -- OBSERVE: 72.0',
                'Step 7  -- THINK:   Subtract Monday\'s sales from total.',
                'Step 8  -- ACT:     calculator({operation: "subtract", a: 180, b: 72})',
                'Step 9  -- OBSERVE: 108.0',
                'Step 10 -- THINK:   Now 25% of the remainder (108) is sold on Tuesday.',
                'Step 11 -- ACT:     calculator({operation: "multiply", a: 108, b: 0.25})',
                'Step 12 -- OBSERVE: 27.0',
                'Step 13 -- THINK:   Subtract Tuesday\'s sales.',
                'Step 14 -- ACT:     calculator({operation: "subtract", a: 108, b: 27})',
                'Step 15 -- OBSERVE: 81.0',
                'Step 16 -- THINK:   FINAL ANSWER: 81',
            ],
            "plan": "`multiply(15, 12) → 180`, then `multiply(180, 0.40) → 72`, then `subtract(180, 72) → 108`, then `multiply(108, 0.25) → 27`, then `subtract(108, 27) → 81`",
        },
    },
    {
        "tier": 6, "problems": PHASE2_PROBLEMS,
        "title": "Tier 6 — Tool Selection Required",
        "phase_header": "## Phase 2 — Multiple Tools\n\nThe agent chooses between four tools: calculator, unit_converter, percentage_calculator, and date_calculator. Problems don't specify which tool to use.",
        "example": {
            "problem": "A recipe calls for 2.5 cups of flour for 4 servings. You're making 8 servings.\n           How many grams of flour do you need?",
            "answer": "600",
            "steps": [
                'Step 1  -- THINK:   I need to scale the recipe from 4 to 8 servings first. That\'s a ratio of 8/4 = 2.',
                'Step 2  -- ACT:     calculator({operation: "divide", a: 8, b: 4})',
                'Step 3  -- OBSERVE: 2.0',
                'Step 4  -- THINK:   Multiply 2.5 cups by the scaling factor of 2.',
                'Step 5  -- ACT:     calculator({operation: "multiply", a: 2.5, b: 2.0})',
                'Step 6  -- OBSERVE: 5.0',
                'Step 7  -- THINK:   Now convert 5 cups of flour to grams. I need the unit converter.',
                'Step 8  -- ACT:     unit_converter({value: 5.0, from_unit: "cups_flour", to_unit: "grams"})',
                'Step 9  -- OBSERVE: 600.0',
                'Step 10 -- THINK:   FINAL ANSWER: 600',
            ],
            "plan": "Tools used: calculator (scaling) + unit_converter (cups to grams)",
        },
    },
    {
        "tier": 7, "problems": PHASE3_SOLVABLE,
        "title": "Tier 7 — Solvable (with distractors and tricks)",
        "phase_header": "## Phase 3 — Incomplete Information\n\nThe agent must recognize unsolvable problems and reject them rather than hallucinate. Solvable problems are mixed with unsolvable ones, ambiguous problems, and messy real-world inputs.",
        "example": {
            "problem": "John is 35 years old and weighs 180 lbs. He buys 6 apples at $0.75 each.\n           How much does he spend?",
            "answer": "4.5",
            "steps": [
                'Step 1 -- THINK:   The age (35) and weight (180 lbs) are irrelevant distractors.',
                '                    I just need to multiply 6 apples by $0.75.',
                'Step 2 -- ACT:     calculator({operation: "multiply", a: 6, b: 0.75})',
                'Step 3 -- OBSERVE: 4.5',
                'Step 4 -- THINK:   FINAL ANSWER: 4.5',
            ],
            "plan": "Key skill: filtering irrelevant information.",
        },
    },
    {
        "tier": 8, "problems": PHASE3_UNSOLVABLE,
        "title": "Tier 8 — Unsolvable (10 problems)",
        "example": {
            "problem": "Two trains leave cities 400 miles apart, heading toward each other. Train A\n           goes 60 mph. When do they meet?",
            "answer": "UNSOLVABLE",
            "steps": [
                "Step 1 -- THINK:   To find when the trains meet, I need both speeds so I can compute",
                "                    the combined closing rate. Train A's speed is 60 mph, but Train B's",
                "                    speed is not given. Without it, I cannot solve this problem.",
                "",
                "UNSOLVABLE: Train B's speed is missing. I cannot determine when the trains meet",
                "without knowing how fast Train B is traveling.",
            ],
            "plan": "Key skill: recognizing missing information instead of hallucinating an answer.",
        },
    },
    {
        "tier": 9, "problems": PHASE3_AMBIGUOUS,
        "title": "Tier 9 — Advanced Reasoning Under Ambiguity",
        "example": {
            "problem": "A train leaves Chicago at 60 mph. Another train leaves New York at an\n           unknown speed. How far has the Chicago train traveled after 3 hours?",
            "answer": "180",
            "steps": [
                "Step 1 -- THINK:   The second train's speed is unknown, but irrelevant to the question.",
                "                    I only need to compute distance for the Chicago train: 60 mph × 3 hours.",
                'Step 2 -- ACT:     calculator({operation: "multiply", a: 60, b: 3})',
                "Step 3 -- OBSERVE: 180.0",
                "Step 4 -- THINK:   The New York train's speed is missing, but the question only asks",
                "                    about the Chicago train. FINAL ANSWER: 180",
            ],
            "plan": "Key skill: solving the solvable part and ignoring irrelevant missing information.",
        },
    },
    {
        "tier": 10, "problems": PHASE3_ADVERSARIAL,
        "title": "Tier 10 — Adversarial and Real-World Inputs",
        "example": {
            "problem": "ok so i bought like 4 boxes of granola bars, 12 in each,\n           gave 7 away, how many left",
            "answer": "41",
            "steps": [
                'Step 1 -- THINK:   Despite the informal phrasing, this is: 4 boxes × 12 bars − 7 given away.',
                'Step 2 -- ACT:     calculator({operation: "multiply", a: 4, b: 12})',
                'Step 3 -- OBSERVE: 48.0',
                'Step 4 -- THINK:   Now subtract the 7 given away.',
                'Step 5 -- ACT:     calculator({operation: "subtract", a: 48, b: 7})',
                'Step 6 -- OBSERVE: 41.0',
                'Step 7 -- THINK:   FINAL ANSWER: 41',
            ],
            "plan": "Key skill: parsing real-world messy input into a clean computation.",
        },
    },
]


def _fmt_answer(p: Problem) -> str:
    """Format a problem's expected answer for display."""
    if math.isnan(p.expected_answer):
        return "UNSOLVABLE"
    val = p.expected_answer
    if val == int(val):
        return str(int(val))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _fmt_answer_with_alts(p: Problem) -> str:
    """Format answer including accepted alternatives."""
    primary = _fmt_answer(p)
    if not p.accepted_answers:
        return primary
    alts = []
    for a in p.accepted_answers:
        if a == int(a):
            alts.append(str(int(a)))
        else:
            alts.append(f"{a:.2f}".rstrip("0").rstrip("."))
    return f"{primary} or {' or '.join(alts)}"


def generate() -> str:
    total_problems = sum(len(t["problems"]) for t in TIERS)
    total_tiers = len(TIERS)

    lines = [
        "# Complete Question & Answer Set",
        "",
        f"{total_problems} problems across 3 phases and {total_tiers} difficulty tiers. "
        "Every problem, its expected answer, and the operation plan (where applicable).",
        "",
        "For each tier, one full worked example is shown first, followed by the remaining problems.",
        "",
        "---",
        "",
    ]

    for tier_info in TIERS:
        # Phase header (only for first tier of each phase)
        if "phase_header" in tier_info:
            lines.append(tier_info["phase_header"])
            lines.append("")

        # Tier heading
        lines.append(f"### {tier_info['title']}")
        lines.append("")

        # Worked example
        ex = tier_info["example"]
        lines.append("#### Worked Example")
        lines.append("")
        lines.append("```")
        lines.append(f'Problem:  "{ex["problem"]}"')
        lines.append(f'Answer:   {ex["answer"]}')
        lines.append("")
        for step in ex["steps"]:
            lines.append(step)
        lines.append("```")
        lines.append("")
        lines.append(ex["plan"])
        lines.append("")

        # Problem table
        problems = tier_info["problems"]
        tier_num = tier_info["tier"]

        if tier_num == 8:
            # Unsolvable tier uses different columns
            lines.append(f"#### All Tier {tier_num} Problems")
            lines.append("")
            lines.append("| # | Problem | What's Missing |")
            lines.append("|---|---------|----------------|")
            missing_info = [
                "Train B's speed",
                "Orange price and quantity breakdown",
                "Individual side lengths",
                "Distance",
                "Amount of blue paint",
                "Production count and costs",
                "Total candy and middle child's share",
                "Fill rate (can't assume constant)",
                "Second plane's speed",
                "Salary amount",
            ]
            for i, prob in enumerate(problems, 1):
                info = missing_info[i - 1] if i <= len(missing_info) else "Unknown"
                lines.append(f"| {i} | {prob.problem} | {info} |")
        else:
            lines.append(f"#### All Tier {tier_num} Problems")
            lines.append("")
            lines.append("| # | Problem | Answer |")
            lines.append("|---|---------|--------|")
            for i, prob in enumerate(problems, 1):
                answer = _fmt_answer_with_alts(prob)
                lines.append(f"| {i} | {prob.problem} | {answer} |")

        lines.append("")
        lines.append("---")
        lines.append("")

    # Remove trailing separator
    while lines and lines[-1] in ("", "---"):
        lines.pop()
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    content = generate()
    with open("QUESTIONS.md", "w") as f:
        f.write(content)
    # Count problems
    total = sum(len(t["problems"]) for t in TIERS)
    print(f"Generated QUESTIONS.md with {total} problems across {len(TIERS)} tiers.")

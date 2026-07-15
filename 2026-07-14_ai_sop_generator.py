#!/usr/bin/env python3
"""
AI Agency SOP & Process Documentation Generator
Generates Standard Operating Procedures, process docs, and workflow guides.
Framework: D.O.C.U.M.E.N.T. — Define, Outline, Compile, Unify, Maintain, Execute, Nurture, Train

Standalone: $14 | Bundle: $37 | Agency License: $97
"""

import json
import os
import sys
import argparse
from datetime import datetime
from textwrap import dedent

# ═══════════════════════════════════════════════════════════════
# SOP DATA
# ═══════════════════════════════════════════════════════════════

SOP_FRAMEWORKS = {
    "onboarding": {
        "name": "Client Onboarding Process",
        "description": "End-to-end SOP for onboarding new clients from signed contract to kickoff",
        "categories": ["Client Management", "Operations"],
        "steps": 12,
        "templates": ["Welcome Email Sequence", "Client Intake Form", "Kickoff Meeting Agenda",
                       "Discovery Document Template", "System Access Setup Checklist",
                       "Data Migration Protocol", "Integration Configuration Guide",
                       "Client Dashboard Setup", "Reporting Schedule Template",
                       "Internal Handoff Document", "Stakeholder Map", "Project Timeline Template"]
    },
    "discovery_audit": {
        "name": "Client Discovery & Automation Audit",
        "description": "Process for auditing a client's current workflows and identifying automation opportunities",
        "categories": ["Sales", "Service Delivery"],
        "steps": 10,
        "templates": ["Pre-Audit Questionnaire", "Tech Stack Inventory", "Process Mapping Worksheet",
                       "Time & Cost Analysis Template", "Automation Opportunity Matrix",
                       "ROI Calculator Template", "Audit Report Template", "Priority Scoring Framework",
                       "Recommendations Deck", "Implementation Roadmap"]
    },
    "implementation": {
        "name": "Automation Implementation Protocol",
        "description": "Standard procedure for building and deploying automation solutions",
        "categories": ["Service Delivery", "Engineering"],
        "steps": 14,
        "templates": ["Solution Architecture Template", "Development Environment Setup",
                       "API Key & Credential Management", "Testing Protocol Checklist",
                       "UAT Sign-Off Form", "Deployment Runbook", "Rollback Procedure",
                       "Error Handling Protocol", "Performance Benchmark Template",
                       "Documentation Template", "Client Training Guide", "Go-Live Checklist",
                       "Post-Launch Review Template", "Handoff to Support"]
    },
    "support": {
        "name": "Client Support & Maintenance SOP",
        "description": "Ongoing support, monitoring, and maintenance procedures for active clients",
        "categories": ["Service Delivery", "Operations"],
        "steps": 11,
        "templates": ["Ticket Intake & Triage Protocol", "SLA Definition Template",
                       "Escalation Matrix", "Routine Maintenance Checklist",
                       "Health Check Report Template", "Incident Response Runbook",
                       "Change Management Log", "Monthly Performance Review",
                       "Client Satisfaction Survey", "Renewal Conversation Script",
                       "Quarterly Business Review Template"]
    },
    "sales": {
        "name": "Sales & Pipeline Management Process",
        "description": "End-to-end sales process from lead capture to closed-won",
        "categories": ["Sales", "Growth"],
        "steps": 13,
        "templates": ["Lead Qualification Scorecard", "Discovery Call Script",
                       "Demo Preparation Checklist", "Proposal Delivery Protocol",
                       "Objection Response Matrix", "Follow-Up Sequence Template",
                       "Contract Negotiation Guide", "Close Process Checklist",
                       "Handoff to Delivery Team", "Lost Deal Analysis Template",
                       "CRM Hygiene Standard", "Pipeline Review Agenda",
                       "Referral Request Script"]
    },
    "reporting": {
        "name": "Client Reporting & Communication Standards",
        "description": "Standard for how the agency reports progress and communicates with clients",
        "categories": ["Client Management", "Operations"],
        "steps": 9,
        "templates": ["Weekly Status Update Template", "Monthly Report Framework",
                       "KPI Dashboard Layout", "Executive Summary Template",
                       "Communication Cadence Matrix", "Email Response SLA",
                       "Emergency Communication Protocol", "Client Portal Setup Guide",
                       "Feedback Collection Process"]
    },
    "hiring": {
        "name": "Team Hiring & Onboarding SOP",
        "description": "Process for recruiting, interviewing, and onboarding new team members",
        "categories": ["People", "Operations"],
        "steps": 11,
        "templates": ["Job Description Template", "Interview Scorecard",
                       "Skills Assessment Framework", "Reference Check Script",
                       "Offer Letter Template", "New Hire Equipment Checklist",
                       "Tool Access Provisioning Guide", "Buddy Assignment Protocol",
                       "90-Day Onboarding Plan", "Probation Review Template",
                       "Role Documentation Handoff"]
    },
    "quality": {
        "name": "Quality Assurance & Review Process",
        "description": "Standards and procedures for maintaining quality across all deliverables",
        "categories": ["Operations", "Service Delivery"],
        "steps": 8,
        "templates": ["Deliverable Quality Checklist", "Peer Review Protocol",
                       "Client Feedback Integration Process", "Error Log Template",
                       "Root Cause Analysis Framework", "Continuous Improvement Tracker",
                       "Quality Metrics Dashboard", "Quarterly Audit Template"]
    }
}

INDUSTRIES = [
    "Real Estate", "Legal", "E-Commerce", "Healthcare", "Financial Services",
    "Education & Training", "Media & Entertainment", "Professional Services",
    "SaaS & Technology", "Manufacturing", "Hospitality", "Non-Profit",
    "Logistics & Supply Chain", "Insurance", "Construction"
]

SERVICE_LINES = [
    "Email Automation", "CRM Integration", "Lead Generation Automation",
    "Reporting & Analytics", "Data Migration & Integration",
    "Document & Contract Automation", "Customer Support Automation",
    "Social Media Automation", "E-Commerce Operations", "HR & Payroll Automation",
    "Financial Process Automation", "Project Management Automation"
]

AGENCY_TYPES = [
    "Boutique (1-5 people)", "Growth Agency (6-20 people)",
    "Scale Agency (21-50 people)", "Enterprise Agency (50+ people)",
    "Freelancer / Solo Operator"
]


def get_sop_data(sop_key):
    """Get SOP framework data by key."""
    return SOP_FRAMEWORKS.get(sop_key)


def generate_sop_document(sop_key, industry, service_line, agency_type, include_templates=True):
    """Generate a complete SOP document."""
    framework = get_sop_data(sop_key)
    if not framework:
        return None

    today = datetime.now().strftime("%Y-%m-%d")
    doc_id = f"SOP-{sop_key.upper()}-{today.replace('-', '')}"

    steps_content = []
    for i, tmpl in enumerate(framework["templates"], 1):
        step_desc = generate_step_description(tmpl, industry, service_line)
        steps_content.append({
            "step_number": i,
            "step_name": tmpl,
            "description": step_desc,
            "owner": assign_owner(sop_key, i),
            "estimated_time": estimate_time(i),
            "status": "Not Started",
            "notes": ""
        })

    doc = {
        "doc_id": doc_id,
        "generated": today,
        "framework": {
            "key": sop_key,
            "name": framework["name"],
            "description": framework["description"],
            "steps": framework["steps"],
            "total_steps": framework["steps"],
            "categories": framework["categories"]
        },
        "context": {
            "industry": industry,
            "service_line": service_line,
            "agency_type": agency_type,
            "agency_type_desc": get_agency_desc(agency_type)
        },
        "steps": steps_content,
        "metadata": {
            "status": "Draft",
            "version": "1.0",
            "last_reviewed": today,
            "next_review": calculate_next_review(today),
            "approved_by": "",
            "effective_date": today
        },
        "templates_included": include_templates,
        "quality_metrics": generate_quality_metrics(sop_key),
        "revision_history": [
            {"version": "1.0", "date": today, "author": "AI Revenue Toolkit", "changes": "Initial document generation"}
        ]
    }

    return doc


def generate_step_description(template_name, industry, service_line):
    """Generate a contextual step description."""
    descriptions = {
        "Welcome Email Sequence": f"Create automated email sequence for new {industry} clients including welcome, account setup instructions, stakeholder introduction, and kickoff scheduling. Tailor tone to {service_line} scope.",
        "Client Intake Form": f"Design comprehensive intake form collecting {industry} client requirements, current tool stack, automation maturity level, success criteria, and compliance needs. Integrate with {service_line} discovery process.",
        "Kickoff Meeting Agenda": f"Structure kickoff meeting covering project scope, timeline, communication channels, success metrics for {industry} client. Define {service_line} deliverables and milestones.",
        "Lead Qualification Scorecard": f"Build qualification scorecard scoring {industry} leads on budget, authority, need, timeline, and fit with {service_line} offerings. Define minimum threshold for pipeline entry.",
        "Demo Preparation Checklist": f"Prepare environment, case studies, and industry-specific examples for {industry} prospects. Configure {service_line} demo scenario showing measurable outcomes.",
        "KPI Dashboard Layout": f"Design real-time dashboard tracking {industry}-specific KPIs including {service_line} metrics, cost savings, efficiency gains, and satisfaction scores.",
        "Escalation Matrix": f"Define escalation path for {industry} client issues by severity level. Map {service_line} support tiers to response times and resolution SLAs.",
        "Testing Protocol Checklist": f"Execute QA testing across {industry}-specific scenarios including edge cases, data validation, and {service_line} integration testing. Document pass/fail criteria.",
        "Deployment Runbook": f"Step-by-step deployment checklist for {industry} environments including {service_line} configuration, API connections, data migration, and rollback procedures.",
        "Documentation Template": f"Generate {industry}-specific documentation covering {service_line} architecture, configuration, admin guide, and end-user training materials.",
    }
    return descriptions.get(template_name, f"Standard procedure for {template_name} adapted for {industry} clients with {service_line} focus.")


def assign_owner(sop_key, step_number):
    """Assign role-based owner for each step."""
    owners = {
        "onboarding": ["Client Success", "Project Manager", "Solutions Architect", "Integration Specialist",
                       "Data Engineer", "Developer", "QA Lead", "Client Success", "Reporting Specialist",
                       "Operations", "Client Success", "Project Manager"],
        "sales": ["Marketing", "SDR", "Solutions Consultant", "Proposal Writer", "Sales Engineer",
                  "SDR", "Account Executive", "Account Executive", "Account Executive", "Sales Ops",
                  "Sales Ops", "Sales Manager", "Account Executive"],
        "implementation": ["Solutions Architect", "Developer", "Security Lead", "QA Engineer",
                          "Client Success", "DevOps", "DevOps", "Developer", "Performance Lead",
                          "Technical Writer", "Client Success", "Project Manager", "Project Manager", "Support Lead"],
        "support": ["Support Lead", "Operations", "Support Lead", "Developer", "Support Lead",
                    "Developer", "Operations", "Client Success", "Client Success", "Account Manager", "Account Manager"],
        "reporting": ["Client Success", "Reporting Lead", "Data Analyst", "Account Manager",
                      "Operations", "Client Success", "Operations", "Developer", "Client Success"],
        "hiring": ["HR/Operations", "HR/Operations", "Team Lead", "HR/Operations", "HR/Operations",
                   "IT/Operations", "IT/Operations", "Team Lead", "Team Lead", "HR/Operations", "Operations"],
        "quality": ["QA Lead", "QA Lead", "Client Success", "QA Lead", "Operations",
                    "Operations", "QA Lead", "Operations"],
        "discovery_audit": ["Solutions Architect", "Data Analyst", "Solutions Architect",
                            "Financial Analyst", "Solutions Consultant", "Financial Analyst",
                            "Solutions Consultant", "Solutions Architect", "Proposal Writer", "Solutions Architect"]
    }
    owners_list = owners.get(sop_key, ["Team Member"] * 20)
    idx = min(step_number - 1, len(owners_list) - 1)
    return owners_list[idx]


def estimate_time(step_number):
    """Estimate time per step."""
    base = step_number * 0.5
    return f"{max(1, int(base))}-{max(2, int(base * 2))} hours"


def get_agency_desc(agency_type):
    """Get description for agency type."""
    descs = {
        "Boutique (1-5 people)": "Small team where everyone wears multiple hats. SOPs critical for consistency.",
        "Growth Agency (6-20 people)": "Growing team needing standardized processes across departments.",
        "Scale Agency (21-50 people)": "Established agency requiring formal SOP documentation for scale.",
        "Enterprise Agency (50+ people)": "Large agency with dedicated departments needing enterprise-grade SOPs.",
        "Freelancer / Solo Operator": "Individual operator using SOPs to systematize and prepare for scaling."
    }
    return descs.get(agency_type, "An agency building structured operations.")


def calculate_next_review(today_str):
    """Calculate next review date (90 days from today)."""
    from datetime import timedelta
    d = datetime.strptime(today_str, "%Y-%m-%d")
    return (d + timedelta(days=90)).strftime("%Y-%m-%d")


def generate_quality_metrics(sop_key):
    """Generate quality metrics for the SOP."""
    metrics = {
        "onboarding": [
            {"metric": "Time to First Value", "target": "≤ 14 days", "current": "", "status": "Not Measured"},
            {"metric": "Client Satisfaction (30-day)", "target": "≥ 4.5/5", "current": "", "status": "Not Measured"},
            {"metric": "Setup Completion Rate", "target": "100%", "current": "", "status": "Not Measured"},
        ],
        "sales": [
            {"metric": "Qualified Lead Response Time", "target": "≤ 1 hour", "current": "", "status": "Not Measured"},
            {"metric": "Proposal Win Rate", "target": "≥ 40%", "current": "", "status": "Not Measured"},
            {"metric": "Pipeline Accuracy", "target": "± 15% forecast", "current": "", "status": "Not Measured"},
        ],
        "quality": [
            {"metric": "Deliverable Defect Rate", "target": "≤ 2%", "current": "", "status": "Not Measured"},
            {"metric": "Client Revision Requests", "target": "≤ 1 per deliverable", "current": "", "status": "Not Measured"},
            {"metric": "On-Time Delivery", "target": "≥ 95%", "current": "", "status": "Not Measured"},
        ]
    }
    return metrics.get(sop_key, [
        {"metric": "Process Adherence Rate", "target": "≥ 90%", "current": "", "status": "Not Measured"},
        {"metric": "Completion Time vs Estimate", "target": "± 20%", "current": "", "status": "Not Measured"},
        {"metric": "Stakeholder Satisfaction", "target": "≥ 4.0/5", "current": "", "status": "Not Measured"},
    ])


def format_markdown(doc):
    """Format SOP document as Markdown."""
    fw = doc["framework"]
    ctx = doc["context"]
    meta = doc["metadata"]
    lines = []

    lines.append(f"# {fw['name']}")
    lines.append(f"## Standard Operating Procedure — {ctx['industry']} | {ctx['service_line']}")
    lines.append("")
    lines.append(f"**Document ID:** {doc['doc_id']}")
    lines.append(f"**Generated:** {doc['generated']}")
    lines.append(f"**Version:** {meta['version']}")
    lines.append(f"**Status:** {meta['status']}")
    lines.append(f"**Effective Date:** {meta['effective_date']}")
    lines.append(f"**Next Review:** {meta['next_review']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## Framework: {fw['name']}")
    lines.append("")
    lines.append(f"_{fw['description']}_")
    lines.append("")
    lines.append(f"**Categories:** {', '.join(fw['categories'])}")
    lines.append(f"**Total Steps:** {fw['steps']}")
    lines.append(f"**Agency Type:** {ctx['agency_type']} — {ctx['agency_type_desc']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Procedure Steps")
    lines.append("")

    for step in doc["steps"]:
        lines.append(f"### Step {step['step_number']}: {step['step_name']}")
        lines.append("")
        lines.append(f"**Owner:** {step['owner']}")
        lines.append(f"**Estimated Time:** {step['estimated_time']}")
        lines.append(f"**Status:** {step['status']}")
        lines.append("")
        lines.append(step['description'])
        lines.append("")
        if step['notes']:
            lines.append(f"> **Notes:** {step['notes']}")
            lines.append("")
        if step['step_number'] < len(doc['steps']):
            lines.append("---")
            lines.append("")

    # Quality Metrics
    lines.append("## Quality Metrics")
    lines.append("")
    lines.append("| Metric | Target | Current | Status |")
    lines.append("|--------|--------|---------|--------|")
    for qm in doc["quality_metrics"]:
        lines.append(f"| {qm['metric']} | {qm['target']} | {qm.get('current', '')} | {qm['status']} |")
    lines.append("")

    # Revision History
    lines.append("## Revision History")
    lines.append("")
    lines.append("| Version | Date | Author | Changes |")
    lines.append("|---------|------|--------|---------|")
    for rev in doc["revision_history"]:
        lines.append(f"| {rev['version']} | {rev['date']} | {rev['author']} | {rev['changes']} |")
    lines.append("")

    return "\n".join(lines)


def format_html(doc):
    """Format SOP document as HTML."""
    fw = doc["framework"]
    ctx = doc["context"]
    meta = doc["metadata"]

    steps_html = ""
    for step in doc["steps"]:
        steps_html += f"""
        <div class="step-card">
            <h3>Step {step['step_number']}: {step['step_name']}</h3>
            <div class="step-meta">
                <span class="badge badge-owner">{step['owner']}</span>
                <span class="badge badge-time">{step['estimated_time']}</span>
                <span class="badge badge-status">{step['status']}</span>
            </div>
            <p>{step['description']}</p>
        </div>
        """

    quality_rows = ""
    for qm in doc["quality_metrics"]:
        quality_rows += f"<tr><td>{qm['metric']}</td><td>{qm['target']}</td><td>{qm.get('current', '')}</td><td>{qm['status']}</td></tr>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{fw['name']} — Standard Operating Procedure</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0a0a0f; color: #e0e0e0; line-height: 1.6; }}
  .container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
  .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; padding: 40px; margin-bottom: 30px; color: white; }}
  .header h1 {{ font-size: 2em; margin-bottom: 10px; }}
  .header .meta {{ display: flex; flex-wrap: wrap; gap: 15px; margin-top: 20px; font-size: 0.9em; opacity: 0.9; }}
  .meta-item {{ background: rgba(255,255,255,0.15); padding: 4px 12px; border-radius: 20px; }}
  .section {{ background: #12121a; border: 1px solid #2a2a3a; border-radius: 8px; padding: 24px; margin-bottom: 20px; }}
  .section h2 {{ color: #667eea; margin-bottom: 15px; font-size: 1.4em; }}
  .step-card {{ background: #1a1a2e; border: 1px solid #2a2a3a; border-radius: 8px; padding: 20px; margin-bottom: 12px; }}
  .step-card h3 {{ color: #a78bfa; margin-bottom: 10px; }}
  .step-meta {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px; }}
  .badge {{ padding: 3px 10px; border-radius: 12px; font-size: 0.8em; font-weight: 600; }}
  .badge-owner {{ background: #1e3a5f; color: #93c5fd; }}
  .badge-time {{ background: #1e3a2f; color: #86efac; }}
  .badge-status {{ background: #3a2a1e; color: #fde68a; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
  th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #2a2a3a; }}
  th {{ color: #667eea; font-weight: 600; }}
  .footer {{ text-align: center; color: #666; font-size: 0.8em; margin-top: 40px; padding: 20px; border-top: 1px solid #2a2a3a; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>{fw['name']}</h1>
    <p>{fw['description']}</p>
    <div class="meta">
      <span class="meta-item">ID: {doc['doc_id']}</span>
      <span class="meta-item">Version {meta['version']}</span>
      <span class="meta-item">{ctx['industry']}</span>
      <span class="meta-item">{ctx['service_line']}</span>
    </div>
  </div>

  <div class="section">
    <h2>Context</h2>
    <p><strong>Industry:</strong> {ctx['industry']}</p>
    <p><strong>Service Line:</strong> {ctx['service_line']}</p>
    <p><strong>Agency Type:</strong> {ctx['agency_type']}</p>
    <p><strong>Categories:</strong> {', '.join(fw['categories'])}</p>
    <p><strong>Total Steps:</strong> {fw['steps']}</p>
  </div>

  <h2 style="color:#667eea;margin-bottom:15px;">Procedure Steps ({len(doc['steps'])} total)</h2>
  {steps_html}

  <div class="section">
    <h2>Quality Metrics</h2>
    <table>
      <tr><th>Metric</th><th>Target</th><th>Current</th><th>Status</th></tr>
      {quality_rows}
    </table>
  </div>

  <div class="footer">
    <p>Generated by AI Revenue Toolkit — SOP Generator v1.0</p>
    <p>Next Review: {meta['next_review']} | Version: {meta['version']}</p>
  </div>
</div>
</body>
</html>"""


def list_sops():
    """List all available SOP frameworks."""
    print("\nAvailable SOP Frameworks:")
    print("=" * 70)
    print(f"{'Key':<25} {'Name':<40} {'Steps'}")
    print("-" * 70)
    for key, fw in sorted(SOP_FRAMEWORKS.items()):
        print(f"{key:<25} {fw['name']:<40} {fw['steps']}")
    print("=" * 70)
    print(f"Total: {len(SOP_FRAMEWORKS)} frameworks | {sum(f['steps'] for f in SOP_FRAMEWORKS.values())} total step templates")
    print()


def list_industries():
    """List available industries."""
    print("\nAvailable Industries:")
    for i, ind in enumerate(INDUSTRIES, 1):
        print(f"  {i:2d}. {ind}")
    print()


def interactive_mode():
    """Run in interactive mode."""
    print("\n" + "=" * 60)
    print("  AI AGENCY SOP & PROCESS DOCUMENTATION GENERATOR")
    print("=" * 60)

    # List SOPs
    list_sops()

    # Select SOP
    sop_key = input("\nEnter SOP key (or number): ").strip().lower()
    try:
        idx = int(sop_key) - 1
        sop_key = sorted(SOP_FRAMEWORKS.keys())[idx]
    except (ValueError, IndexError):
        pass

    if sop_key not in SOP_FRAMEWORKS:
        print(f"Unknown SOP: {sop_key}")
        return

    # List industries
    list_industries()
    ind_choice = input("Enter industry name or number: ").strip()
    try:
        idx = int(ind_choice) - 1
        industry = INDUSTRIES[idx]
    except (ValueError, IndexError):
        industry = ind_choice

    # Service line
    print("\nService Lines:")
    for i, sl in enumerate(SERVICE_LINES, 1):
        print(f"  {i:2d}. {sl}")
    sl_choice = input("\nEnter service line (name or number): ").strip()
    try:
        idx = int(sl_choice) - 1
        service_line = SERVICE_LINES[idx]
    except (ValueError, IndexError):
        service_line = sl_choice

    # Agency type
    print("\nAgency Types:")
    for i, at in enumerate(AGENCY_TYPES, 1):
        print(f"  {i:2d}. {at}")
    at_choice = input("\nEnter agency type (name or number): ").strip()
    try:
        idx = int(at_choice) - 1
        agency_type = AGENCY_TYPES[idx]
    except (ValueError, IndexError):
        agency_type = at_choice

    # Output format
    fmt = input("\nOutput format (markdown/html/both) [both]: ").strip().lower() or "both"

    # Generate
    doc = generate_sop_document(sop_key, industry, service_line, agency_type)

    # Output directory
    out_dir = input("\nOutput directory [./sop_output]: ").strip() or "./sop_output"
    os.makedirs(out_dir, exist_ok=True)

    base_name = f"sop_{sop_key}_{industry.lower().replace(' ', '_').replace('&', 'and')}"
    results = []

    if fmt in ("markdown", "both"):
        md = format_markdown(doc)
        path = os.path.join(out_dir, f"{base_name}.md")
        with open(path, "w") as f:
            f.write(md)
        results.append(("Markdown", path))

    if fmt in ("html", "both"):
        html = format_html(doc)
        path = os.path.join(out_dir, f"{base_name}.html")
        with open(path, "w") as f:
            f.write(html)
        results.append(("HTML", path))

    # Also save JSON
    json_path = os.path.join(out_dir, f"{base_name}.json")
    with open(json_path, "w") as f:
        json.dump(doc, f, indent=2)
    results.append(("JSON", json_path))

    print("\n" + "=" * 60)
    print("  GENERATION COMPLETE")
    print("=" * 60)
    for fmt_name, path in results:
        size = os.path.getsize(path)
        print(f"  {fmt_name:<10} → {path}  ({size:,} bytes)")
    print(f"\n  Framework: {SOP_FRAMEWORKS[sop_key]['name']}")
    print(f"  Industry:  {industry}")
    print(f"  Service:   {service_line}")
    print(f"  Steps:     {len(doc['steps'])}")
    print("=" * 60)


def batch_mode(sop_keys, industries, service_lines, agency_types, out_dir="./sop_batch_output"):
    """Generate multiple SOPs in batch."""
    os.makedirs(out_dir, exist_ok=True)
    generated = []

    for sop_key in sop_keys:
        for industry in industries:
            for service_line in service_lines:
                for agency_type in agency_types:
                    if sop_key not in SOP_FRAMEWORKS:
                        continue
                    doc = generate_sop_document(sop_key, industry, service_line, agency_type)
                    base_name = f"sop_{sop_key}_{industry.lower().replace(' ', '_').replace('&', 'and')}"

                    # Write all formats
                    md = format_markdown(doc)
                    with open(os.path.join(out_dir, f"{base_name}.md"), "w") as f:
                        f.write(md)

                    html = format_html(doc)
                    with open(os.path.join(out_dir, f"{base_name}.html"), "w") as f:
                        f.write(html)

                    with open(os.path.join(out_dir, f"{base_name}.json"), "w") as f:
                        json.dump(doc, f, indent=2)

                    generated.append({
                        "sop": sop_key,
                        "industry": industry,
                        "service_line": service_line,
                        "files": [
                            f"{base_name}.md",
                            f"{base_name}.html",
                            f"{base_name}.json"
                        ]
                    })

    return generated


def generate_report(doc):
    """Generate a one-page summary/report from an SOP document."""
    fw = doc["framework"]
    ctx = doc["context"]
    lines = []
    lines.append(f"# SOP Summary: {fw['name']}")
    lines.append(f"**Industry:** {ctx['industry']} | **Service:** {ctx['service_line']}")
    lines.append(f"**Total Steps:** {fw['steps']} | **Categories:** {', '.join(fw['categories'])}")
    lines.append("")
    lines.append("## Quick Reference")
    for step in doc["steps"]:
        lines.append(f"- **Step {step['step_number']}:** {step['step_name']} ({step['owner']})")
    lines.append("")
    lines.append(f"## Quality Targets")
    for qm in doc["quality_metrics"]:
        lines.append(f"- {qm['metric']}: target {qm['target']}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="AI Agency SOP & Process Documentation Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent("""\
            Examples:
              %(prog)s -s onboarding -i "Real Estate" -l "Email Automation" -o ./sops
              %(prog)s -s sales -i "E-Commerce" -l "CRM Integration" --html
              %(prog)s --list-sops
              %(prog)s --interactive
              %(prog)s --batch --all-sops -i "Real Estate,Legal,SaaS" -o ./full_sop_library
        """)
    )

    parser.add_argument("-s", "--sop", help="SOP framework key (use --list-sops to see all)")
    parser.add_argument("-i", "--industry", help="Target industry")
    parser.add_argument("-l", "--service-line", help="Service line focus")
    parser.add_argument("-a", "--agency-type", default="Growth Agency (6-20 people)",
                        help="Agency type (default: Growth Agency)")
    parser.add_argument("-o", "--output-dir", default="./sop_output", help="Output directory")
    parser.add_argument("--html", action="store_true", help="Output HTML only")
    parser.add_argument("--markdown", action="store_true", help="Output Markdown only")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    parser.add_argument("--report", action="store_true", help="Generate summary report instead of full SOP")
    parser.add_argument("--list-sops", action="store_true", help="List available SOP frameworks")
    parser.add_argument("--list-industries", action="store_true", help="List available industries")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    parser.add_argument("--batch", action="store_true", help="Batch generate multiple SOPs")
    parser.add_argument("--all-sops", action="store_true", help="Generate all SOP frameworks (batch mode)")
    parser.add_argument("--all-industries", action="store_true", help="Generate for all industries (batch mode)")

    args = parser.parse_args()

    if args.list_sops:
        list_sops()
        return

    if args.list_industries:
        list_industries()
        return

    if args.interactive:
        interactive_mode()
        return

    # Determine output format
    formats = []
    if args.html:
        formats.append("html")
    if args.markdown:
        formats.append("markdown")
    if args.json:
        formats.append("json")
    if not formats:
        formats = ["markdown", "html", "json"]

    # Batch mode
    if args.batch or args.all_sops:
        sops = sorted(SOP_FRAMEWORKS.keys()) if args.all_sops else [args.sop]
        industries = INDUSTRIES if args.all_industries else [args.industry]
        service_lines = [args.service_line] if args.service_line else SERVICE_LINES[:2]
        out_dir = args.output_dir
        gen = batch_mode(sops, industries, service_lines, [args.agency_type], out_dir)
        print(f"Generated {len(gen)} SOP documents in {out_dir}")
        return

    # Single SOP generation
    if not args.sop or not args.industry:
        parser.print_help()
        print("\nUse --interactive for guided mode, or provide -s and -i")
        return

    doc = generate_sop_document(args.sop, args.industry, args.service_line or "General Automation", args.agency_type)
    if not doc:
        print(f"Unknown SOP framework: {args.sop}")
        list_sops()
        return

    os.makedirs(args.output_dir, exist_ok=True)
    base_name = f"sop_{args.sop}_{args.industry.lower().replace(' ', '_').replace('&', 'and')}"

    if args.report:
        report = generate_report(doc)
        path = os.path.join(args.output_dir, f"{base_name}_report.md")
        with open(path, "w") as f:
            f.write(report)
        print(f"Report saved to {path}")
        return

    for fmt in formats:
        if fmt == "markdown":
            content = format_markdown(doc)
            path = os.path.join(args.output_dir, f"{base_name}.md")
        elif fmt == "html":
            content = format_html(doc)
            path = os.path.join(args.output_dir, f"{base_name}.html")
        elif fmt == "json":
            content = json.dumps(doc, indent=2)
            path = os.path.join(args.output_dir, f"{base_name}.json")
        with open(path, "w") as f:
            f.write(content)
        print(f"{fmt.upper():<10} → {path}")

    print(f"\nDone. Total steps: {len(doc['steps'])}")


if __name__ == "__main__":
    main()

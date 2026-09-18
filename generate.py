#!/usr/bin/env python3
"""Generates all AD Investments service sub-pages + services.html overview
from a single data-driven template. Run: python3 generate.py
"""
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO = "https://i.ibb.co/N2tqmM7z/ad-investments-logo.png"

# ---------------------------------------------------------------------------
# Shared building blocks
# ---------------------------------------------------------------------------

ALL_INTERESTS = [
    "Stock Advisory", "Mutual Funds", "Fixed Deposits", "Demat Services",
    "NCD/RBI Bonds", "Sovereign Gold Bond", "Capital Gain Bonds (54EC)", "NPS",
    "Life Insurance", "Health Insurance", "Motor Insurance", "Home Loan",
    "Auto Loan", "Personal Loan", "Loan on MF/LIC", "Retirement Planning",
    "HDFC Bank Saving Account", "HDFC Credit Card", "Portfolio Review",
    "Goal-Based Planning", "Other",
]

NAV_DROPDOWN = """
        <div class="dropdown">
          <div class="dropdown-section">
            <span class="dropdown-label">Investments</span>
            <a href="mutual-funds.html">Mutual Funds</a>
            <a href="fixed-deposits.html">Fixed Deposits</a>
            <a href="demat.html">Demat Services</a>
            <a href="bonds.html">NCD/RBI Bonds</a>
            <a href="sgb.html">Sovereign Gold Bond</a>
            <a href="capital-gains.html">Capital Gain Bonds (54EC)</a>
            <a href="nps.html">NPS</a>
          </div>
          <div class="dropdown-section">
            <span class="dropdown-label">Insurance</span>
            <a href="life-insurance.html">Life Insurance</a>
            <a href="health-insurance.html">Health Insurance</a>
            <a href="motor-insurance.html">Motor Insurance</a>
          </div>
          <div class="dropdown-section">
            <span class="dropdown-label">Loans</span>
            <a href="home-loan.html">Home Loan</a>
            <a href="auto-loan.html">Auto Loan</a>
            <a href="personal-loan.html">Personal Loan</a>
            <a href="loan-mf-lic.html">Loan on MF/LIC</a>
          </div>
          <div class="dropdown-section">
            <span class="dropdown-label">Planning</span>
            <a href="retirement.html">Retirement Planning</a>
            <a href="stock-advisory.html">Stock Advisory</a>
          </div>
          <div class="dropdown-section">
            <span class="dropdown-label">Banking</span>
            <a href="hdfc-savings.html">HDFC Bank Saving A/c</a>
            <a href="hdfc-credit.html">HDFC Credit Card</a>
          </div>
        </div>"""

MOBILE_MENU_SERVICES = """
      <div class="mobile-menu-services-group">
        <span class="mobile-menu-services-label">Investments</span>
        <a href="mutual-funds.html">Mutual Funds</a>
        <a href="fixed-deposits.html">Fixed Deposits</a>
        <a href="demat.html">Demat Services</a>
        <a href="bonds.html">NCD/RBI Bonds</a>
        <a href="sgb.html">Sovereign Gold Bond</a>
        <a href="capital-gains.html">Capital Gain Bonds (54EC)</a>
        <a href="nps.html">NPS</a>
      </div>
      <div class="mobile-menu-services-group">
        <span class="mobile-menu-services-label">Insurance</span>
        <a href="life-insurance.html">Life Insurance</a>
        <a href="health-insurance.html">Health Insurance</a>
        <a href="motor-insurance.html">Motor Insurance</a>
      </div>
      <div class="mobile-menu-services-group">
        <span class="mobile-menu-services-label">Loans</span>
        <a href="home-loan.html">Home Loan</a>
        <a href="auto-loan.html">Auto Loan</a>
        <a href="personal-loan.html">Personal Loan</a>
        <a href="loan-mf-lic.html">Loan on MF/LIC</a>
      </div>
      <div class="mobile-menu-services-group">
        <span class="mobile-menu-services-label">Planning</span>
        <a href="retirement.html">Retirement Planning</a>
        <a href="stock-advisory.html">Stock Advisory</a>
      </div>
      <div class="mobile-menu-services-group">
        <span class="mobile-menu-services-label">Banking</span>
        <a href="hdfc-savings.html">HDFC Bank Saving A/c</a>
        <a href="hdfc-credit.html">HDFC Credit Card</a>
      </div>"""

WHATSAPP_NUMBER = "919335459707"
WHATSAPP_MESSAGE = "Hi, I would like to consult about my finances."


def nav_html():
    return f"""  <nav>
    <a class="nav-logo" href="index.html">
      <img src="{LOGO}" alt="AD Investments"/>
    </a>

    <ul class="nav-links">
      <li>
        <a href="services.html" class="has-dropdown">Services</a>{NAV_DROPDOWN}
      </li>
      <li><a href="about.html">About</a></li>
      <li><a href="index.html#contact">Contact</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">Book Consultation</a>
    <button class="nav-toggle" id="navToggle" type="button" aria-label="Open menu" aria-expanded="false">
      <span></span>
    </button>
  </nav>

  <div class="mobile-menu" id="mobileMenu">
    <a href="index.html">Home</a>
    <button class="mobile-menu-services-toggle" type="button">Services</button>
    <div class="mobile-menu-services">{MOBILE_MENU_SERVICES}
    </div>
    <a href="about.html">About</a>
    <a href="index.html#contact">Contact</a>
    <a href="index.html#contact" class="nav-cta">Book Consultation</a>
  </div>"""


def cursor_html():
    return """  <div class="cursor" id="cursor"></div>
  <div class="cursor-follower" id="follower"></div>"""


def whatsapp_float_html():
    import urllib.parse
    text = urllib.parse.quote(WHATSAPP_MESSAGE)
    return f"""  <a class="whatsapp-float" href="https://wa.me/{WHATSAPP_NUMBER}?text={text}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">
    <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M16.004 3C9.377 3 4 8.373 4 15c0 2.386.7 4.607 1.908 6.474L4 29l7.73-1.865A11.94 11.94 0 0 0 16.004 27C22.63 27 28 21.627 28 15S22.63 3 16.004 3Zm0 21.818c-1.98 0-3.86-.55-5.47-1.523l-.392-.233-4.59 1.107 1.128-4.47-.257-.406A9.77 9.77 0 0 1 5.182 15c0-5.964 4.858-10.818 10.822-10.818S26.818 9.036 26.818 15 21.968 24.818 16.004 24.818Zm5.98-8.145c-.327-.164-1.93-.953-2.23-1.062-.3-.109-.518-.164-.737.164-.218.327-.845 1.062-1.036 1.28-.19.218-.382.245-.71.082-.327-.164-1.382-.51-2.633-1.626-.973-.868-1.63-1.94-1.82-2.267-.19-.327-.02-.504.144-.667.148-.148.327-.382.49-.573.164-.19.218-.327.327-.545.109-.218.055-.41-.027-.573-.082-.164-.737-1.775-1.01-2.43-.266-.64-.537-.553-.737-.563l-.628-.011c-.218 0-.573.082-.873.41-.3.327-1.145 1.12-1.145 2.73 0 1.611 1.173 3.167 1.336 3.386.164.218 2.308 3.525 5.593 4.943.782.338 1.392.54 1.868.69.785.25 1.5.215 2.065.13.63-.094 1.93-.79 2.202-1.552.273-.763.273-1.417.19-1.553-.082-.136-.3-.218-.627-.382Z"/></svg>
  </a>"""


def breadcrumb_html(category, current):
    if category is None:
        return f"""      <div class="breadcrumb reveal">
        <a href="index.html">Home</a><span class="sep">/</span><span class="current">{current}</span>
      </div>"""
    return f"""      <div class="breadcrumb reveal">
        <a href="index.html">Home</a><span class="sep">/</span><a href="services.html">Services</a><span class="sep">/</span><a href="services.html#{category.lower()}">{category}</a><span class="sep">/</span><span class="current">{current}</span>
      </div>"""


def interest_options_html(selected):
    opts = []
    for label in ALL_INTERESTS:
        sel = " selected" if label == selected else ""
        opts.append(f"              <option{sel}>{label}</option>")
    return "\n".join(opts)


def contact_section_html(selected_interest, heading_emphasis="Consultation"):
    return f"""  <!-- CONTACT -->
  <section class="section contact-section" id="contact">
    <div class="contact-inner">
      <div class="contact-left reveal">
        <div class="section-label">
          <span>Get In Touch</span>
        </div>
        <h2>Book a Free <em style="font-style:italic;color:var(--gold)">{heading_emphasis}</em></h2>
        <p>Talk to us for free. No commitments. We'll review your financial situation and show you exactly how to move forward — step by step.</p>
        <div class="contact-info">
          <div class="contact-item">
            <div class="contact-icon">📞</div>
            <div class="contact-detail">
              <strong>Call Us</strong>
              <span>+91 73790 08786</span>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-icon">💬</div>
            <div class="contact-detail">
              <strong>WhatsApp</strong>
              <span>Message us anytime</span>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-icon">📍</div>
            <div class="contact-detail">
              <strong>Location</strong>
              <span>Lucknow, Uttar Pradesh</span>
            </div>
          </div>
        </div>
      </div>
      <div class="contact-right reveal">
        <h3>Request a Callback</h3>
        <form id="contactForm" onsubmit="sendToWhatsApp(event)">
          <div class="form-group">
            <label>Your Name</label>
            <input type="text" id="fname" placeholder="Amit Kumar" required/>
          </div>
          <div class="form-group">
            <label>Phone Number</label>
            <input type="tel" id="fphone" placeholder="+91 98765 43210" required/>
          </div>
          <div class="form-group">
            <label>Interested In</label>
            <select id="finterest">
{interest_options_html(selected_interest)}
            </select>
          </div>
          <div class="form-group">
            <label>Message (Optional)</label>
            <textarea id="fmessage" placeholder="Tell us briefly about your financial goals..."></textarea>
          </div>
          <button type="submit" class="form-submit">Request Free Consultation</button>
        </form>
      </div>
    </div>
  </section>"""


def footer_html():
    return """  <!-- FOOTER -->
  <footer style="background:#0E0E0E;border-top:1px solid rgba(201,168,76,0.15);padding:60px 24px 0;">
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:40px;padding-bottom:48px;" class="footer-grid">
      <div>
        <img src=\"""" + LOGO + """\" alt="AD Investments" style="height:48px;margin-bottom:16px;display:block;"/>
        <h4 style="font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:400;color:var(--white);margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid var(--gold);display:inline-block;">About Us</h4>
        <p style="font-size:13px;line-height:1.8;color:var(--white-dim);margin-top:12px;">AD Investments is a fully dedicated Financial Distribution Company based in Lucknow. Our purpose is to help investors preserve and grow their wealth through disciplined, goal-based financial planning.</p>
      </div>
      <div>
        <h4 style="font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:400;color:var(--white);margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid var(--gold);display:inline-block;">Quick Links</h4>
        <ul style="list-style:none;margin-top:12px;display:flex;flex-direction:column;gap:10px;">
          <li><a href="index.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Home</a></li>
          <li><a href="services.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Services</a></li>
          <li><a href="about.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● About Us</a></li>
          <li><a href="index.html#contact" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Contact</a></li>
          <li><a href="index.html#contact" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Book Consultation</a></li>
        </ul>
      </div>
      <div>
        <h4 style="font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:400;color:var(--white);margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid var(--gold);display:inline-block;">Our Services</h4>
        <ul style="list-style:none;margin-top:12px;display:flex;flex-direction:column;gap:10px;">
          <li><a href="mutual-funds.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Mutual Funds</a></li>
          <li><a href="life-insurance.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Life Insurance</a></li>
          <li><a href="health-insurance.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Health Insurance</a></li>
          <li><a href="fixed-deposits.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Fixed Deposits</a></li>
          <li><a href="retirement.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Retirement Planning</a></li>
          <li><a href="home-loan.html" style="color:var(--white-dim);text-decoration:none;font-size:13px;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">● Home Loan</a></li>
        </ul>
      </div>
      <div>
        <h4 style="font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:400;color:var(--white);margin-bottom:12px;padding-bottom:8px;border-bottom:2px solid var(--gold);display:inline-block;">Get In Touch</h4>
        <ul style="list-style:none;margin-top:12px;display:flex;flex-direction:column;gap:14px;">
          <li style="display:flex;gap:10px;align-items:flex-start;"><span style="color:var(--gold);">📍</span><span style="font-size:13px;color:var(--white-dim);line-height:1.6;">Lucknow, Uttar Pradesh, India</span></li>
          <li style="display:flex;gap:10px;align-items:center;"><span style="color:var(--gold);">📞</span><a href="tel:+917379008786" style="font-size:13px;color:var(--white-dim);text-decoration:none;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">+91 73790 08786</a></li>
          <li style="display:flex;gap:10px;align-items:center;"><span style="color:var(--gold);">💬</span><a href="https://wa.me/917379008786" target="_blank" style="font-size:13px;color:var(--white-dim);text-decoration:none;" onmouseover="this.style.color='#C9A84C'" onmouseout="this.style.color='rgba(245,242,236,0.6)'">WhatsApp Us</a></li>
        </ul>
      </div>
    </div>
    <div style="border-top:1px solid rgba(201,168,76,0.1);padding:20px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
      <div style="font-size:12px;color:rgba(245,242,236,0.3);">© 2025 AD Investments. Lucknow, India. All rights reserved.</div>
      <div style="font-size:12px;color:rgba(245,242,236,0.3);">AMFI Registered | ARN-331443 | Validity: 08 Sep 2026</div>
    </div>
  </footer>"""


DISCLAIMERS = {
    "mf": """  <div style="background:#0A0A0A;padding:24px 20px;font-size:11px;color:rgba(245,242,236,0.3);line-height:1.8;text-align:center;">
    <p style="max-width:1000px;margin:0 auto 8px;"><strong style="color:rgba(201,168,76,0.5);">Risk Factors —</strong> Investments in Mutual Funds are subject to Market Risks. Read all scheme related documents carefully before investing. Mutual Fund Schemes do not assure or guarantee any returns. Past performances of any Mutual Fund Scheme may or may not be sustained in future. There is no guarantee that the investment objective of any suggested scheme shall be achieved. All existing and prospective investors are advised to check and evaluate the Exit loads and other cost structure (TER) applicable at the time of making the investment before finalizing on any investment decision for Mutual Funds schemes. We deal in Regular Plans only for Mutual Fund Schemes and earn a Trailing Commission on client investments. Disclosure for commission earnings is made to clients at the time of investments. Option of Direct Plan for every Mutual Fund Scheme is available to investors offering advantage of lower expense ratio. We are not entitled to earn any commission on Direct plans. Hence we do not deal in Direct Plans.</p>
    <p style="margin-top:8px;">
      <a href="https://www.sebi.gov.in" target="_blank" style="color:rgba(201,168,76,0.5);text-decoration:none;">SEBI</a> &nbsp;|&nbsp;
      <a href="https://www.amfiindia.com" target="_blank" style="color:rgba(201,168,76,0.5);text-decoration:none;">AMFI</a> &nbsp;|&nbsp;
      <a href="https://www.sebi.gov.in/filings/mutual-funds.html" target="_blank" style="color:rgba(201,168,76,0.5);text-decoration:none;">SID/SAI/KIM</a>
    </p>
  </div>""",
    "market": """  <div style="background:#0A0A0A;padding:24px 20px;font-size:11px;color:rgba(245,242,236,0.3);line-height:1.8;text-align:center;">
    <p style="max-width:1000px;margin:0 auto;"><strong style="color:rgba(201,168,76,0.5);">Risk Factors —</strong> Investments in securities and the securities market are subject to market risks. Please read all related offer documents / issue documents carefully before investing. Past performance is not indicative of future returns. There is no assurance or guarantee of returns on any product mentioned on this page. AD Investments acts as a distributor and does not provide investment advice unless separately agreed; please consult your financial advisor before taking any investment decision.</p>
  </div>""",
    "loan": """  <div style="background:#0A0A0A;padding:24px 20px;font-size:11px;color:rgba(245,242,236,0.3);line-height:1.8;text-align:center;">
    <p style="max-width:1000px;margin:0 auto;"><strong style="color:rgba(201,168,76,0.5);">Disclaimer —</strong> Loan approval, sanctioned amount, interest rate, processing fee and other charges are at the sole discretion of the respective bank / NBFC and subject to their credit policy, documentation and eligibility criteria. Rates and terms shown are indicative and subject to change without notice. AD Investments acts as a facilitator / referral partner and does not guarantee approval or specific terms.</p>
  </div>""",
    "insurance": """  <div style="background:#0A0A0A;padding:24px 20px;font-size:11px;color:rgba(245,242,236,0.3);line-height:1.8;text-align:center;">
    <p style="max-width:1000px;margin:0 auto;"><strong style="color:rgba(201,168,76,0.5);">Disclaimer —</strong> Insurance is the subject matter of solicitation. Please read the policy wording, prospectus, terms, conditions and exclusions carefully before concluding a sale. AD Investments acts as a referral / facilitator and is not an insurance company; final underwriting, pricing and claim decisions rest solely with the respective insurer.</p>
  </div>""",
    "banking": """  <div style="background:#0A0A0A;padding:24px 20px;font-size:11px;color:rgba(245,242,236,0.3);line-height:1.8;text-align:center;">
    <p style="max-width:1000px;margin:0 auto;"><strong style="color:rgba(201,168,76,0.5);">Disclaimer —</strong> Account opening, card issuance, limits, fees and charges are at the sole discretion of HDFC Bank and subject to its eligibility criteria, KYC and internal policies. AD Investments acts as a referral partner; all approvals and servicing are handled directly by HDFC Bank.</p>
  </div>""",
}

CATEGORY_ANCHOR = {
    "Investments": "investments",
    "Insurance": "insurance",
    "Loans": "loans",
    "Planning": "planning",
    "Banking": "banking",
}


def render_benefits(benefits):
    cards = []
    for icon, title, desc in benefits:
        cards.append(f"""      <div class="service-card reveal" style="cursor:default;">
        <div class="service-icon">{icon}</div>
        <div class="service-title">{title}</div>
        <p class="service-desc">{desc}</p>
      </div>""")
    return "\n".join(cards)


def render_points(points):
    items = []
    for i, (title, desc) in enumerate(points, start=1):
        items.append(f"""          <div class="why-point">
            <div class="why-num">{i:02d}</div>
            <div class="why-text">
              <strong>{title}</strong>
              <span>{desc}</span>
            </div>
          </div>""")
    return "\n".join(items)


def render_faqs(faqs):
    items = []
    for q, a in faqs:
        items.append(f"""      <details class="faq-item reveal">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>""")
    return "\n".join(items)


def render_intro(paragraphs):
    return "\n".join(f'      <p class="intro-text reveal">{p}</p>' for p in paragraphs)


PAGE_SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | AD Investments</title>
  <meta name="description" content="{meta_description}"/>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="assets/style.css"/>
</head>
<body>

{cursor}
{whatsapp}

  <!-- NAV -->
{nav}

  <!-- PAGE HERO -->
  <section class="page-hero">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="hero-content" style="max-width:760px;">
{breadcrumb}
      <div class="page-hero-icon">{icon}</div>
      <h1 style="font-size:clamp(40px,5.5vw,64px);">{h1}</h1>
      <p class="hero-sub" style="max-width:600px;">{hero_sub}</p>
      <div class="hero-actions">
        <a href="#contact" class="btn-primary">Get Started</a>
        <a href="services.html" class="btn-secondary">
          All Services
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>
  </section>

  <!-- INTRO -->
  <section class="section" style="padding-top:0;">
    <div class="section-label reveal">
      <span>Overview</span>
    </div>
{intro}
  </section>

  <!-- BENEFITS -->
  <section class="section" style="padding-top:0;">
    <div class="section-label reveal">
      <span>Key Benefits</span>
    </div>
    <h2 class="reveal">Why It Belongs In <em style="font-style:italic;color:var(--gold)">Your Plan</em></h2>
    <div class="services-grid cols-3">
{benefits}
    </div>
  </section>

  <!-- WHY US -->
  <section class="section why-section">
    <div class="why-grid">
      <div class="why-left reveal">
        <div class="section-label">
          <span>Why AD Investments</span>
        </div>
        <h2>How We <em style="font-style:italic;color:var(--gold)">Help You</em></h2>
        <div class="why-points">
{points}
        </div>
      </div>
      <div class="why-right reveal">
        <div class="why-visual">
          <p class="testimonial-text">"{testimonial}"</p>
          <div class="testimonial-author">
            <div class="author-avatar">{testimonial_initial}</div>
            <div>
              <div class="author-name">{testimonial_name}</div>
              <div class="author-role">{testimonial_role}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section" style="padding-top:0;">
    <div class="section-label reveal">
      <span>Common Questions</span>
    </div>
    <h2 class="reveal">Frequently <em style="font-style:italic;color:var(--gold)">Asked</em></h2>
    <div class="faq-list">
{faqs}
    </div>
  </section>

{contact}

{footer}

  <!-- DISCLAIMER -->
{disclaimer}

  <script src="assets/main.js"></script>
</body>
</html>
"""


def build_page(slug, title, meta_description, category, icon, h1, hero_sub,
                intro, benefits, points, faqs, disclaimer_key, default_interest,
                testimonial, testimonial_name, testimonial_role):
    html = PAGE_SHELL.format(
        title=title,
        meta_description=meta_description,
        cursor=cursor_html(),
        whatsapp=whatsapp_float_html(),
        nav=nav_html(),
        breadcrumb=breadcrumb_html(category, title),
        icon=icon,
        h1=h1,
        hero_sub=hero_sub,
        intro=render_intro(intro),
        benefits=render_benefits(benefits),
        points=render_points(points),
        testimonial=testimonial,
        testimonial_initial=testimonial_name[0],
        testimonial_name=testimonial_name,
        testimonial_role=testimonial_role,
        faqs=render_faqs(faqs),
        contact=contact_section_html(default_interest, title),
        footer=footer_html(),
        disclaimer=DISCLAIMERS[disclaimer_key],
    )
    path = os.path.join(OUT_DIR, slug)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", slug)


# ---------------------------------------------------------------------------
# Service data
# ---------------------------------------------------------------------------

SERVICES = [
    dict(
        slug="mutual-funds.html",
        title="Mutual Funds",
        meta_description="SIP and lump sum mutual fund investment guidance across equity, debt and hybrid categories, tailored to your goals — from AD Investments, Lucknow.",
        category="Investments", icon="💼",
        h1="Mutual Fund <em>Investments</em>",
        hero_sub="SIP or lump sum — we help you choose the right mix of equity, debt and hybrid funds to match your financial timeline and risk appetite.",
        intro=[
            "Mutual funds pool money from many investors and are professionally managed across equity, debt, hybrid and other asset classes. They remain one of the most accessible ways for salaried families in Lucknow to participate in long-term wealth creation without needing to track individual stocks.",
            "At AD Investments, we don't push a one-size-fits-all fund list. We look at your income, goals, time horizon and comfort with volatility before recommending a portfolio — and we stay with you to review and rebalance it as your life changes.",
        ],
        benefits=[
            ("🎯", "Goal Mapping", "Every fund we recommend is tied to a specific goal — retirement, a child's education, a home down payment — not a random tip."),
            ("🔄", "SIP Discipline", "Start a Systematic Investment Plan from as little as a few thousand rupees a month and build wealth through market cycles."),
            ("⚖️", "Risk-Matched Mix", "A blend of equity, debt and hybrid schemes calibrated to how much volatility you can actually sleep through."),
            ("📋", "Ongoing Review", "We track fund performance and rebalance your portfolio periodically, not just at the time of purchase."),
            ("🧮", "Tax-Aware Planning", "Fund selection accounts for capital gains tax treatment and ELSS options where relevant to your tax planning."),
            ("🤝", "Regular Plan Support", "We service Regular Plans, which means ongoing hand-holding, statements support and query resolution at no extra cost to you."),
        ],
        points=[
            ("Personalised Fund Selection", "No generic best-fund lists. We shortlist schemes based on your actual income, goals and risk tolerance."),
            ("Transparent Process", "You always know which funds you hold, how they're performing, and why we recommended them."),
            ("Long-Term Relationship", "We stay with your portfolio from your first SIP through decades of compounding — not just the first purchase."),
        ],
        faqs=[
            ("What is the minimum amount to start a SIP?", "Many mutual fund schemes allow SIPs starting from as low as ₹500–₹1,000 per month, though the right amount for you depends on your goals — we'll help you work that out."),
            ("Is my money safe in mutual funds?", "Mutual funds are market-linked and carry risk; they are not guaranteed. Equity funds can be volatile in the short term but have historically rewarded patient, long-term investors. Debt funds carry relatively lower but non-zero risk."),
            ("Regular Plan or Direct Plan — what's the difference?", "Direct Plans have a lower expense ratio but come with no advisory support. We deal in Regular Plans, which include a small trailing commission in exchange for ongoing guidance, portfolio reviews and support — fully disclosed to you at the time of investment."),
            ("Can I withdraw my mutual fund investment anytime?", "Most open-ended mutual funds offer daily liquidity, though some schemes (like ELSS) have a lock-in period and certain funds may charge an exit load if redeemed early."),
        ],
        disclaimer_key="mf", default_interest="Mutual Funds",
        testimonial="AD Investments helped me start my first SIP 6 years ago. Today my portfolio has grown beyond what I ever imagined. They feel like family.",
        testimonial_name="Rahul Srivastava", testimonial_role="Government Employee, Lucknow",
    ),
    dict(
        slug="fixed-deposits.html",
        title="Fixed Deposits",
        meta_description="Corporate and bank fixed deposits with guaranteed returns, matched to your investment horizon — arranged by AD Investments, Lucknow.",
        category="Investments", icon="🏦",
        h1="Fixed <em>Deposits</em>",
        hero_sub="Safe, predictable returns with corporate and bank fixed deposits selected to match your investment horizon and liquidity needs.",
        intro=[
            "Fixed Deposits remain the anchor of many Indian household portfolios — a place to park money with a known, contracted rate of return over a fixed tenure, away from market ups and downs.",
            "We work with a panel of bank and corporate FD issuers so you're not limited to whatever your neighbourhood bank branch happens to be offering, and we help you compare tenure, interest payout frequency and credit rating before you commit.",
        ],
        benefits=[
            ("📈", "Fixed, Known Returns", "Your interest rate is locked in at the time of booking, so you know exactly what you'll earn over the tenure."),
            ("🗓️", "Flexible Tenures", "Choose tenures from a few months to several years depending on when you'll need the money back."),
            ("💵", "Payout Options", "Pick monthly, quarterly, or cumulative interest payout based on whether you need regular income or growth."),
            ("🏢", "Corporate & Bank Options", "Compare rates across bank FDs and highly rated corporate/NBFC deposits for potentially higher returns."),
            ("👴", "Senior Citizen Rates", "We flag additional interest offered to senior citizens on eligible deposits."),
            ("📄", "Simple Paperwork", "We handle the documentation and application process so booking an FD takes minutes, not a full afternoon."),
        ],
        points=[
            ("Rate Comparison", "We compare current rates across our panel of banks and corporates so you don't settle for the first offer you see."),
            ("Credit Quality Checks", "For corporate deposits, we highlight credit ratings so you understand the safety profile before you invest."),
            ("Renewal Reminders", "We track your FD maturity dates and reach out ahead of time so your money is never left idle at a low rollover rate."),
        ],
        faqs=[
            ("Are fixed deposits completely risk-free?", "Bank FDs up to ₹5 lakh per bank are covered under DICGC deposit insurance. Corporate/NBFC FDs are not bank deposits and carry issuer credit risk, which is why we highlight credit ratings before you invest."),
            ("What's the difference between cumulative and non-cumulative FDs?", "Cumulative FDs reinvest interest and pay it out at maturity along with the principal. Non-cumulative FDs pay interest at regular intervals (monthly/quarterly) — useful if you need periodic income."),
            ("Is FD interest taxable?", "Yes, interest earned on fixed deposits is added to your taxable income and taxed as per your applicable slab rate. TDS may also apply above certain thresholds."),
            ("Can I break my FD before maturity?", "Most FDs allow premature withdrawal, usually with a reduced interest rate or a small penalty — terms vary by issuer and we'll explain these before you book."),
        ],
        disclaimer_key="market", default_interest="Fixed Deposits",
        testimonial="I wanted zero surprises with my retirement corpus. AD Investments laid out every FD option clearly and never pushed me into anything.",
        testimonial_name="Meena Gupta", testimonial_role="Retired Bank Officer, Lucknow",
    ),
    dict(
        slug="demat.html",
        title="Demat Services",
        meta_description="Open and manage a Demat account with expert guidance to start investing in stocks, bonds and ETFs — AD Investments, Lucknow.",
        category="Investments", icon="📊",
        h1="Demat <em>Services</em>",
        hero_sub="Open and manage your Demat account seamlessly. Start investing in stocks, bonds and ETFs with expert guidance at every step.",
        intro=[
            "A Demat account holds your shares, bonds, ETFs and other securities in electronic form — it's the gateway to participating in the stock market, applying for IPOs, and holding instruments like NCDs, RBI Bonds and Sovereign Gold Bonds.",
            "We assist with account opening, documentation and KYC so the process is smooth, and we're available to answer the practical questions that come up once your account is live — corporate actions, statements, nomination and more.",
        ],
        benefits=[
            ("📝", "Guided Account Opening", "We walk you through the paperwork and KYC so your Demat and trading account is activated without back-and-forth delays."),
            ("🔗", "Linked Trading Account", "Get your Demat account linked with a trading account so you can buy and sell securities in one seamless flow."),
            ("🎟️", "IPO Access", "Hold a Demat account to apply for IPOs and receive share allotments directly into your holdings."),
            ("🪙", "Hold Bonds & Gold", "Use the same account to hold NCDs, RBI Bonds, and Sovereign Gold Bonds alongside your equity holdings."),
            ("👪", "Nomination Support", "We help you set up nomination correctly so your holdings pass smoothly to your family when needed."),
            ("📞", "Ongoing Support", "Questions about corporate actions, statements or transfers? We're a call away even after the account is opened."),
        ],
        points=[
            ("Hassle-Free Onboarding", "We simplify the documentation so you're not stuck deciphering forms on your own."),
            ("One Point of Contact", "Instead of navigating a call centre, you have a local advisor who knows your account and your goals."),
            ("Connected to Your Broader Plan", "Your Demat holdings are viewed as part of your overall portfolio, not an isolated account."),
        ],
        faqs=[
            ("What documents do I need to open a Demat account?", "Typically PAN card, Aadhaar, a cancelled cheque or bank statement, a passport-size photo, and your signature — we'll confirm the exact current requirements when you start."),
            ("Is there a minimum balance required?", "No, Demat accounts don't require you to maintain a minimum securities balance, though annual maintenance charges (AMC) typically apply."),
            ("Can I have more than one Demat account?", "Yes, individuals can hold multiple Demat accounts across different depository participants if needed."),
            ("What happens to my Demat holdings if something happens to me?", "This is exactly why nomination matters — with a valid nomination or will, your holdings transfer to your nominee/legal heir through a defined process."),
        ],
        disclaimer_key="market", default_interest="Demat Services",
        testimonial="Opening my Demat account felt intimidating until AD Investments walked me through every step. I was investing in my first IPO within a week.",
        testimonial_name="Ankit Verma", testimonial_role="IT Professional, Lucknow",
    ),
    dict(
        slug="bonds.html",
        title="NCD / RBI Bonds",
        meta_description="Non-Convertible Debentures and RBI Bonds for stable, fixed-income returns outside traditional FDs — AD Investments, Lucknow.",
        category="Investments", icon="📜",
        h1="NCD & <em>RBI Bonds</em>",
        hero_sub="Add stable, fixed-income instruments to your portfolio through Non-Convertible Debentures and Government of India / RBI-backed bonds.",
        intro=[
            "Non-Convertible Debentures (NCDs) are fixed-income instruments issued by companies to raise debt, offering a fixed coupon over a defined tenure. RBI/Government bonds, in contrast, carry sovereign backing and are used by conservative investors seeking safety with a steady return.",
            "We help you understand the credit rating, coupon structure and tenure of available NCD issues, and keep you informed when new RBI/Government bond issuances open for subscription.",
        ],
        benefits=[
            ("💰", "Fixed Coupon Income", "Earn a predictable, periodic interest payout over the life of the bond."),
            ("🏛️", "Sovereign-Backed Options", "RBI/Government bonds carry sovereign credit backing, appealing to safety-first investors."),
            ("⭐", "Credit Rating Transparency", "We share the credit rating of each NCD issue so you understand the risk before investing."),
            ("📆", "Tenure Choices", "Pick from short, medium or long tenure bonds depending on when you'll need liquidity."),
            ("📈", "Portfolio Diversification", "Bonds add a fixed-income layer that behaves differently from equities, smoothing overall portfolio volatility."),
            ("🗞️", "New Issue Alerts", "We notify you when fresh NCD or bond issues open, so you don't miss attractive windows."),
        ],
        points=[
            ("Issue-by-Issue Evaluation", "We don't recommend every bond that comes to market — only issues that fit sound credit and rate criteria."),
            ("Plain-Language Explanations", "Bond offer documents are dense; we translate the coupon, tenure and rating into a clear picture."),
            ("Held Safely in Demat", "Your bonds are held electronically in your Demat account alongside the rest of your holdings."),
        ],
        faqs=[
            ("What's the difference between an NCD and a company FD?", "NCDs are tradable on stock exchanges and held in Demat form, offering potential liquidity before maturity, unlike most corporate FDs which are non-transferable."),
            ("Are RBI Bonds completely safe?", "RBI/Government-backed bonds carry sovereign credit risk, which is considered very low, though returns are market-linked to prevailing rates at the time of issue and are not guaranteed to beat inflation."),
            ("Can I sell an NCD before maturity?", "Listed NCDs can potentially be sold on the stock exchange before maturity, subject to market liquidity and prevailing price, which may be above or below your purchase price."),
            ("Is interest from bonds taxable?", "Yes, interest income from NCDs and most bonds is taxable as per your income slab, unless specifically notified as tax-free by the issuer."),
        ],
        disclaimer_key="market", default_interest="NCD/RBI Bonds",
        testimonial="I wanted something steadier than the stock market but better than a plain savings account. The bond options AD Investments showed me fit perfectly.",
        testimonial_name="Suresh Chandra", testimonial_role="Business Owner, Lucknow",
    ),
    dict(
        slug="sgb.html",
        title="Sovereign Gold Bond",
        meta_description="Invest in Sovereign Gold Bonds — a government-backed alternative to physical gold with annual interest — via AD Investments, Lucknow.",
        category="Investments", icon="🪙",
        h1="Sovereign <em>Gold Bond</em>",
        hero_sub="A smarter way to hold gold — government-backed Sovereign Gold Bonds that track gold prices and pay you annual interest on top.",
        intro=[
            "Sovereign Gold Bonds (SGBs) are Government of India securities denominated in grams of gold, issued as a substitute for holding physical gold. They eliminate concerns around storage, purity and making charges while offering a fixed annual interest on the invested amount.",
            "For families who traditionally buy gold for weddings or as a long-term store of value, SGBs offer a paper-based alternative that can be held safely in a Demat account or as a certificate.",
        ],
        benefits=[
            ("🏅", "No Storage Worries", "Skip locker fees, theft risk and purity concerns that come with physical gold."),
            ("💹", "Annual Interest", "Earn a fixed annual interest on your invested amount, in addition to any price appreciation in gold."),
            ("🚫", "No Making Charges", "Unlike jewellery, SGBs carry no making charges or purity deductions."),
            ("🧾", "Capital Gains Benefit", "Capital gains on SGBs held to maturity may enjoy tax exemptions as per prevailing income tax rules."),
            ("🔐", "Government Backing", "Issued by the RBI on behalf of the Government of India, carrying sovereign credit backing."),
            ("🔄", "Tradable Option", "Listed SGBs can potentially be traded on the stock exchange if you need liquidity before maturity."),
        ],
        points=[
            ("Issue Window Tracking", "We keep you informed about RBI's periodic SGB subscription windows so you don't miss them."),
            ("Right-Sized Allocation", "We help you decide how much of your portfolio should sit in gold, based on your overall asset allocation."),
            ("Simple Application Process", "We guide you through the application, whether through Demat or certificate form."),
        ],
        faqs=[
            ("What is the tenure of a Sovereign Gold Bond?", "SGBs typically have an 8-year tenure, with an option for early redemption from the 5th year onward on interest payment dates."),
            ("How is the interest paid?", "Interest is usually paid semi-annually at a fixed rate on the initial investment amount, credited directly to your bank account."),
            ("Is the gold price risk still there?", "Yes — the redemption value is linked to prevailing gold prices, so while you avoid making charges, your capital is still subject to gold price fluctuations."),
            ("Can NRIs invest in SGBs?", "As per current RBI guidelines, SGBs are available to resident Indian individuals, HUFs, trusts and certain institutions; NRIs are generally not eligible to invest — rules can change, so we'll confirm current eligibility with you."),
        ],
        disclaimer_key="market", default_interest="Sovereign Gold Bond",
        testimonial="We always bought gold for festivals. AD Investments showed us how Sovereign Gold Bonds give the same gold exposure, minus the locker anxiety.",
        testimonial_name="Priya & Manoj Tiwari", testimonial_role="Homemakers, Lucknow",
    ),
    dict(
        slug="capital-gains.html",
        title="Capital Gain Bonds (54EC)",
        meta_description="Save long-term capital gains tax on property sales by investing in Section 54EC capital gain bonds — AD Investments, Lucknow.",
        category="Investments", icon="🧾",
        h1="Capital Gain Bonds <em>(54EC)</em>",
        hero_sub="Sold property recently? Section 54EC capital gain bonds can help you save long-term capital gains tax while earning a fixed return.",
        intro=[
            "When you sell land or a building and realise long-term capital gains, Section 54EC of the Income Tax Act allows you to invest the gains in specified bonds (issued by entities such as REC, PFC and IRFC) to claim exemption from capital gains tax, subject to conditions and limits.",
            "Timing matters — these bonds must typically be purchased within 6 months of the sale/transfer of the property. We help you understand the window, the investment limit, and the issuer options available at the time.",
        ],
        benefits=[
            ("🛡️", "Tax Exemption on LTCG", "Invest eligible long-term capital gains within the prescribed window to claim exemption under Section 54EC."),
            ("🏛️", "AAA-Rated Issuers", "Bonds are issued by government-backed entities such as REC, PFC and IRFC, known for high credit quality."),
            ("📅", "Clear Timelines", "We flag the 6-month investment deadline from the date of transfer so you don't miss the window."),
            ("💵", "Fixed Interest", "Earn a fixed annual interest over the bond's tenure, though returns are modest compared to the tax saved."),
            ("🔒", "Defined Lock-in", "A defined lock-in period applies, which we explain upfront so there are no surprises."),
            ("📄", "Application Support", "We help you complete the application within the tight post-sale timeline."),
        ],
        points=[
            ("Deadline-Driven Guidance", "We understand these bonds are time-sensitive and prioritise fast, accurate application support."),
            ("Investment Limit Clarity", "We explain the maximum investment limit eligible for exemption under Section 54EC so you plan the balance amount correctly."),
            ("Coordination With Your CA", "We're happy to coordinate with your chartered accountant to make sure the exemption is claimed correctly in your tax filing."),
        ],
        faqs=[
            ("How soon after selling property must I invest?", "Under current rules, the investment in 54EC bonds must generally be made within 6 months from the date of transfer of the capital asset — this is a strict deadline."),
            ("Is there a maximum investment limit?", "Yes, there is a cap on the amount eligible for exemption under Section 54EC in a financial year — we'll confirm the current limit with you before you invest."),
            ("What is the lock-in period?", "These bonds typically carry a multi-year lock-in period during which they cannot be sold, transferred or used as collateral."),
            ("Is the interest earned taxable?", "Yes, while the capital gains invested are exempt, the interest income earned on 54EC bonds is taxable as per your income slab."),
        ],
        disclaimer_key="market", default_interest="Capital Gain Bonds (54EC)",
        testimonial="After selling our ancestral plot, we were confused about capital gains tax. AD Investments got our 54EC bonds sorted within the deadline.",
        testimonial_name="Vinod Kumar Mishra", testimonial_role="Property Seller, Lucknow",
    ),
    dict(
        slug="nps.html",
        title="National Pension System (NPS)",
        meta_description="Build a disciplined retirement corpus with the National Pension System, with additional tax benefits under Section 80CCD — AD Investments, Lucknow.",
        category="Investments", icon="🏛️",
        h1="National Pension <em>System</em>",
        hero_sub="A government-backed, market-linked retirement savings scheme that combines disciplined investing with additional tax benefits.",
        intro=[
            "The National Pension System (NPS) is a voluntary, long-term retirement savings scheme regulated by the PFRDA, allowing you to invest systematically across equity, corporate debt and government securities through professional fund managers.",
            "Beyond retirement savings, NPS offers an additional tax deduction over and above the standard 80C limit, making it a popular addition to the retirement plans of salaried professionals across Lucknow.",
        ],
        benefits=[
            ("🎯", "Dedicated Retirement Corpus", "Contributions are locked toward retirement, building disciplined, long-term savings you won't be tempted to dip into."),
            ("➕", "Extra Tax Deduction", "Claim an additional deduction under Section 80CCD(1B), over and above the ₹1.5 lakh limit under Section 80C."),
            ("⚖️", "Choice of Asset Mix", "Choose your allocation across equity, corporate bonds and government securities, or opt for auto-allocation by age."),
            ("💸", "Low Cost Structure", "NPS is known for one of the lowest fund management costs among market-linked retirement products."),
            ("🔄", "Portable Account", "Your NPS account (PRAN) stays with you across employers and cities throughout your career."),
            ("🏦", "Annuity at Retirement", "At retirement, a portion is used to purchase an annuity providing you a regular pension income."),
        ],
        points=[
            ("Right-Fit Asset Allocation", "We help you choose an equity/debt mix suited to your age and risk appetite, and review it periodically."),
            ("Tax Planning Integration", "NPS is positioned within your overall tax-saving strategy alongside 80C instruments, not in isolation."),
            ("Retirement-Stage Guidance", "As you approach retirement, we help you understand annuity options and the partial withdrawal rules."),
        ],
        faqs=[
            ("What is the extra tax benefit under NPS?", "You can claim up to ₹50,000 as an additional deduction under Section 80CCD(1B), over and above the ₹1.5 lakh limit available under Section 80C — subject to prevailing tax rules."),
            ("When can I withdraw from NPS?", "NPS is primarily a retirement product; full withdrawal is generally allowed from age 60, with partial withdrawal permitted under specific conditions before that."),
            ("Is NPS return guaranteed?", "No, NPS returns are market-linked and depend on the performance of the underlying equity, corporate debt and government securities you're invested in."),
            ("What happens to my NPS corpus at retirement?", "As per current rules, a portion of the corpus can be withdrawn as a lump sum (tax-free up to specified limits) and the remainder must be used to purchase an annuity that pays you a regular pension."),
        ],
        disclaimer_key="market", default_interest="NPS",
        testimonial="I didn't realise how much extra tax I could save until AD Investments explained the NPS 80CCD(1B) benefit. It's now part of my yearly routine.",
        testimonial_name="Deepak Awasthi", testimonial_role="Private Sector Employee, Lucknow",
    ),
    dict(
        slug="life-insurance.html",
        title="Life Insurance",
        meta_description="Term and life insurance plans to protect your family's financial future, matched to your income and responsibilities — AD Investments, Lucknow.",
        category="Insurance", icon="🛡️",
        h1="Life <em>Insurance</em>",
        hero_sub="Protect your family's financial future with the right cover — term plans, savings-linked plans and family income protection, explained simply.",
        intro=[
            "Life insurance exists to make sure your family's financial life doesn't fall apart if something happens to you. Yet many people are either under-insured, over-paying for the wrong kind of policy, or holding multiple overlapping plans that don't actually add up to real protection.",
            "We start with a simple question — what would your family need to maintain their lifestyle, pay off debts and meet future goals without your income? — and work backward to the right cover and policy type.",
        ],
        benefits=[
            ("🛡️", "Adequate Term Cover", "We help you calculate the right sum assured based on income, liabilities and future goals — not a round number picked at random."),
            ("💰", "Affordable Premiums", "Compare term plans across insurers to find strong coverage at a premium that fits your budget."),
            ("👨‍👩‍👧", "Family Income Protection", "Riders and plan structures designed to replace your income for your family if the unexpected happens."),
            ("🏥", "Critical Illness Riders", "Add critical illness and disability riders where it makes sense to broaden your protection."),
            ("📉", "Loan Protection", "Cover outstanding home, auto or personal loans so debt doesn't become your family's burden."),
            ("📋", "Claim Assistance", "We don't disappear after the policy is issued — we help your family navigate the claims process if it's ever needed."),
        ],
        points=[
            ("Needs-Based, Not Product-Pushed", "We calculate your actual protection gap before recommending any policy."),
            ("Multi-Insurer Comparison", "We compare plans across insurers so you're not limited to a single company's offering."),
            ("Reviewed As Life Changes", "Marriage, children, a new home loan — we revisit your cover as your responsibilities grow."),
        ],
        faqs=[
            ("How much life cover do I actually need?", "A common rule of thumb is 10–15 times your annual income, but the right number depends on your outstanding loans, dependents, and future goals like children's education — we'll work this out with you."),
            ("What's the difference between term insurance and other life insurance plans?", "Term insurance offers pure protection — a large cover at a low premium with no maturity payout if you outlive the term. Savings-linked plans combine insurance with an investment/maturity component, usually at a much lower cover-per-rupee."),
            ("Do pre-existing health conditions affect my premium?", "Yes, insurers assess your medical history and may adjust premiums, add exclusions, or require additional tests — we'll help you disclose accurately to avoid claim issues later."),
            ("What happens if I miss a premium payment?", "Most policies offer a grace period; missing it beyond the grace period can lapse the policy, though many allow reinstatement within a defined window subject to conditions."),
        ],
        disclaimer_key="insurance", default_interest="Life Insurance",
        testimonial="After our second child was born, AD Investments recalculated our term cover properly. We were underinsured for years without realising it.",
        testimonial_name="Rohit & Kavita Singh", testimonial_role="Working Parents, Lucknow",
    ),
    dict(
        slug="health-insurance.html",
        title="Health Insurance",
        meta_description="Individual and family floater health insurance plans that protect your savings from medical emergencies — AD Investments, Lucknow.",
        category="Insurance", icon="🩺",
        h1="Health <em>Insurance</em>",
        hero_sub="Medical costs shouldn't derail your savings. We help you choose individual or family floater health cover that actually works when you need it.",
        intro=[
            "A single hospitalisation can undo years of careful saving. Health insurance protects your financial plan from that risk — but only if the policy has adequate cover, the right hospital network, and terms that don't surprise you at claim time.",
            "We compare plans across insurers on sum insured, waiting periods, room rent limits, and claim settlement track record, rather than just the lowest premium on offer.",
        ],
        benefits=[
            ("👨‍👩‍👧‍👦", "Family Floater Options", "A single policy covering your entire family, often more cost-effective than individual policies for each member."),
            ("🏥", "Cashless Network", "We check hospital network coverage in and around Lucknow before recommending a plan."),
            ("📈", "No-Claim Bonus", "Understand how your sum insured can grow over claim-free years without extra premium."),
            ("👴", "Senior Citizen Cover", "Plans designed for older parents, accounting for pre-existing condition waiting periods."),
            ("💊", "OPD & Add-on Riders", "Optional riders for OPD, maternity or critical illness cover where relevant to your family's needs."),
            ("📋", "Claims Support", "We assist with claim documentation and coordination with the insurer when you actually need to use the policy."),
        ],
        points=[
            ("Adequate Sum Insured", "We help you avoid the common trap of being under-insured relative to actual hospitalisation costs today."),
            ("Fine-Print Review", "Room rent capping, co-pay clauses and sub-limits are explained upfront, not discovered during a claim."),
            ("Family-Wide View", "We look at your whole family's health cover together, not policy by policy in isolation."),
        ],
        faqs=[
            ("What is a waiting period?", "Most health policies have an initial waiting period (commonly 30 days, except accidents) before claims are admissible, plus longer waiting periods for specific illnesses and pre-existing conditions — these vary by insurer and plan."),
            ("Is a family floater better than individual policies?", "A family floater shares one sum insured across all members and is often cheaper, but if one member claims heavily in a year, less cover may remain for others — the right choice depends on your family's health profile."),
            ("Does health insurance cover pre-existing diseases?", "Most policies cover pre-existing diseases only after a specified waiting period (commonly 2–4 years), which varies by insurer and plan."),
            ("Can I port my existing health policy to a new insurer?", "Yes, IRDAI guidelines allow policy portability, letting you switch insurers while carrying forward accrued waiting period credit, subject to the process and timelines defined by regulation."),
        ],
        disclaimer_key="insurance", default_interest="Health Insurance",
        testimonial="When my father was hospitalised, the cashless claim AD Investments had set up for us made an already stressful time so much easier.",
        testimonial_name="Anjali Pandey", testimonial_role="Software Engineer, Lucknow",
    ),
    dict(
        slug="motor-insurance.html",
        title="Motor Insurance",
        meta_description="Car and two-wheeler insurance with the right cover, add-ons and claim support — AD Investments, Lucknow.",
        category="Insurance", icon="🚗",
        h1="Motor <em>Insurance</em>",
        hero_sub="Comprehensive or third-party motor insurance for your car or two-wheeler, with the right add-ons and hassle-free claim support.",
        intro=[
            "Motor insurance is mandatory under Indian law, but the difference between a bare-minimum third-party policy and a well-structured comprehensive plan can matter enormously the day you actually need to make a claim.",
            "We help you choose appropriate cover — including own-damage protection, add-ons like zero-depreciation and roadside assistance — and we're available when it's time to actually file a claim.",
        ],
        benefits=[
            ("🚗", "Comprehensive Cover", "Protection against own vehicle damage, theft and third-party liability in a single policy."),
            ("🛡️", "Zero-Depreciation Add-on", "Get full claim value on replaced parts without depreciation deduction, especially useful for newer vehicles."),
            ("🆘", "Roadside Assistance", "Add-on cover for breakdowns, towing and emergency support on the road."),
            ("💰", "No-Claim Bonus Protection", "Options to protect your accumulated no-claim bonus even after a claim."),
            ("🏍️", "Two-Wheeler Plans", "Dedicated cover options for two-wheelers, not just cars."),
            ("📋", "Claim Filing Support", "We guide you through documentation and follow-up when you need to file a claim."),
        ],
        points=[
            ("Right-Sized Policy", "We help you avoid both under-insurance and paying for add-ons you don't actually need."),
            ("Renewal Reminders", "We track your policy expiry so your vehicle is never accidentally left uninsured."),
            ("Claims Advocacy", "When you need to claim, we help you navigate the process rather than leaving you to deal with it alone."),
        ],
        faqs=[
            ("Is third-party insurance enough for my car?", "Third-party insurance is the legal minimum and covers damage/injury to others, but it does not cover damage to your own vehicle — comprehensive cover is generally recommended for adequate protection."),
            ("What is IDV (Insured Declared Value)?", "IDV is the maximum sum assured fixed by the insurer, representing the current market value of your vehicle — it directly affects your premium and the payout in case of total loss or theft."),
            ("Does my no-claim bonus carry over if I change insurers?", "Yes, no-claim bonus is generally transferable between insurers, provided you can furnish proof of your claim-free history from the previous policy."),
            ("What should I do immediately after an accident?", "Ensure safety first, then inform the insurer promptly, take photos of the damage, and avoid getting the vehicle repaired before a survey where a claim is intended — we can guide you through the exact steps."),
        ],
        disclaimer_key="insurance", default_interest="Motor Insurance",
        testimonial="My car insurance claim after a minor accident was settled without a single runaround, thanks to AD Investments following up on my behalf.",
        testimonial_name="Naveen Yadav", testimonial_role="Shop Owner, Lucknow",
    ),
    dict(
        slug="home-loan.html",
        title="Home Loan",
        meta_description="Compare home loan offers from top banks and NBFCs and get end-to-end application support — AD Investments, Lucknow.",
        category="Loans", icon="🏠",
        h1="Home <em>Loan</em>",
        hero_sub="Get the best home loan deals from top banks and NBFCs. We compare rates and guide you through the entire process, start to finish.",
        intro=[
            "Buying a home is likely the largest financial decision you'll make, and the loan structure you choose — interest rate type, tenure, and lender — has a real impact on your total cost over 15-20 years.",
            "We compare offers across our panel of banks and NBFCs on interest rate, processing fee and eligibility, and help you through documentation, sanction and disbursement.",
        ],
        benefits=[
            ("🏦", "Multi-Lender Comparison", "See offers across several banks and NBFCs instead of relying on a single branch's rate card."),
            ("📉", "Rate Negotiation Support", "We help present your profile in the best light to potentially secure a more competitive rate."),
            ("📄", "Documentation Help", "Guidance on the full paperwork checklist so your file isn't delayed by missing documents."),
            ("⏱️", "Faster Processing", "Our familiarity with lender processes can help speed up sanction and disbursement timelines."),
            ("💳", "Balance Transfer Advice", "If you already have a home loan, we assess whether a balance transfer to a lower rate makes financial sense."),
            ("🧮", "EMI Planning", "We help you understand how tenure and rate choices affect your monthly EMI and total interest outgo."),
        ],
        points=[
            ("Objective Comparisons", "We show you real numbers across lenders instead of pushing whichever bank pays the highest referral fee."),
            ("End-to-End Support", "From application to sanction letter to disbursement, we stay involved so you're not left chasing paperwork alone."),
            ("Life-of-Loan Relationship", "We're available for questions on part-prepayment, rate resets or refinancing long after disbursement."),
        ],
        faqs=[
            ("How much home loan am I eligible for?", "Eligibility depends on your income, existing obligations, credit score and the lender's policy — typically lenders fund a portion of the property value with the rest as your down payment, and we'll help estimate your specific eligibility."),
            ("Fixed or floating interest rate — which is better?", "Floating rates move with market benchmarks and are more common in India, often starting lower than fixed rates; fixed rates offer payment certainty but may be reset periodically depending on the lender's terms. We'll explain both in the context of current offers."),
            ("What documents are typically required?", "Identity and address proof, income documents (salary slips/ITR), bank statements, and property documents are commonly required — the exact list varies by lender and employment type."),
            ("Can I prepay my home loan?", "Most floating-rate home loans allow part-prepayment or foreclosure without penalty as per RBI guidelines for individual borrowers; fixed-rate loans may have different terms — we'll clarify based on your specific loan."),
        ],
        disclaimer_key="loan", default_interest="Home Loan",
        testimonial="AD Investments compared three banks for our home loan and got us a noticeably better rate than what our own bank branch initially quoted.",
        testimonial_name="Sandeep & Ritu Shukla", testimonial_role="First-Time Homebuyers, Lucknow",
    ),
    dict(
        slug="auto-loan.html",
        title="Auto Loan",
        meta_description="Car and two-wheeler loans with competitive rates and quick processing, arranged across our lender panel — AD Investments, Lucknow.",
        category="Loans", icon="🚙",
        h1="Auto <em>Loan</em>",
        hero_sub="Financing for your next car or two-wheeler — competitive rates, quick processing, and a comparison across our panel of lenders.",
        intro=[
            "Whether it's your first car or an upgrade, the right auto loan structure means lower total interest and a comfortable EMI. We help you compare offers rather than accepting the first quote from a dealership's in-house financing desk.",
            "We assist with eligibility checks, documentation, and coordination with the lender so your loan is sanctioned in time for your vehicle purchase or delivery timeline.",
        ],
        benefits=[
            ("🚗", "New & Used Vehicle Financing", "Loan options for both new vehicle purchases and select used vehicles."),
            ("📊", "Rate Comparison", "We compare interest rates and processing fees across multiple lenders before you commit."),
            ("⚡", "Quick Turnaround", "Coordinated documentation to help your loan get sanctioned within your purchase timeline."),
            ("💵", "Flexible Tenure", "Choose a repayment tenure that balances EMI affordability with total interest cost."),
            ("🏍️", "Two-Wheeler Loans", "Financing options for two-wheelers alongside four-wheeler loans."),
            ("🔁", "Top-Up & Refinance", "Guidance on refinancing an existing auto loan if a better rate becomes available."),
        ],
        points=[
            ("Dealer-Independent Advice", "We're not tied to a single dealership's financing partner, so you see genuinely comparative offers."),
            ("Clear EMI Math", "We lay out EMI, total interest and tenure trade-offs before you sign anything."),
            ("Paperwork Support", "We help assemble the required documents so processing isn't held up by missing paperwork."),
        ],
        faqs=[
            ("What is the typical loan-to-value for a car loan?", "Lenders commonly finance a large portion of the on-road price, with the balance payable as a down payment — exact ratios vary by lender, vehicle type and your credit profile."),
            ("Does my credit score affect my auto loan rate?", "Yes, a higher credit score generally helps you access more competitive interest rates and faster approval."),
            ("Can I prepay or foreclose my auto loan?", "Most auto loans allow foreclosure or part-prepayment, though some lenders charge a foreclosure fee, particularly in the early part of the tenure — we'll clarify the specific terms for your loan."),
            ("Is loan protection insurance necessary?", "It's optional but can be worth considering, as it covers your outstanding loan in the event of the borrower's death or specific contingencies — we can explain if it fits your situation."),
        ],
        disclaimer_key="loan", default_interest="Auto Loan",
        testimonial="I compared the dealer's financing offer with what AD Investments arranged — theirs saved me a noticeable amount in interest over the loan term.",
        testimonial_name="Abhishek Tripathi", testimonial_role="Marketing Executive, Lucknow",
    ),
    dict(
        slug="personal-loan.html",
        title="Personal Loan",
        meta_description="Quick, unsecured personal loans for emergencies, weddings, medical needs and more — competitive rates via AD Investments, Lucknow.",
        category="Loans", icon="💳",
        h1="Personal <em>Loan</em>",
        hero_sub="Quick, unsecured financing for weddings, medical needs, home renovation or emergencies — matched to a rate and tenure that works for you.",
        intro=[
            "Personal loans offer fast, collateral-free access to funds for life's unplanned or big-ticket expenses. Because they're unsecured, interest rates and eligibility vary widely across lenders based on your income and credit profile.",
            "We help you compare offers, understand the true cost including processing fees, and choose a tenure that keeps your EMI manageable without stretching repayment unnecessarily long.",
        ],
        benefits=[
            ("⚡", "Fast Disbursal", "Streamlined documentation aimed at getting funds to you quickly when time matters."),
            ("🔓", "No Collateral Required", "Unsecured financing — no need to pledge property, gold or other assets."),
            ("📊", "Rate Comparison", "See offers across lenders rather than accepting the first pre-approved offer in your inbox."),
            ("🧮", "True Cost Clarity", "We factor in processing fees and other charges, not just the headline interest rate."),
            ("📅", "Flexible Tenure", "Choose a repayment period that balances EMI comfort with total interest paid."),
            ("💍", "Purpose-Fit Guidance", "Whether it's a wedding, medical need or renovation, we help size the loan to the actual requirement."),
        ],
        points=[
            ("Eligibility-First Approach", "We check your likely eligibility before applying, avoiding unnecessary credit inquiries on your report."),
            ("No Over-Borrowing", "We help you borrow what you need for the purpose at hand, not the maximum you're offered."),
            ("Fee Transparency", "Processing fees, foreclosure charges and other costs are explained before you sign."),
        ],
        faqs=[
            ("How is my personal loan eligibility decided?", "Lenders assess your income, existing EMIs, credit score and employment stability — a higher credit score generally improves both eligibility and the rate offered."),
            ("How quickly can I get the loan disbursed?", "Disbursal timelines vary by lender and how quickly documentation is completed; well-prepared applications with a clean credit profile are typically processed faster."),
            ("Are there charges besides the interest rate?", "Most personal loans carry a processing fee, and some lenders charge foreclosure or prepayment charges — we'll walk you through the full cost breakdown before you apply."),
            ("Can I foreclose my personal loan early?", "Most lenders allow foreclosure after a minimum number of EMIs, often with a foreclosure charge — terms vary and we'll clarify them for your specific loan."),
        ],
        disclaimer_key="loan", default_interest="Personal Loan",
        testimonial="A sudden medical expense in the family needed quick funds. AD Investments helped us get a personal loan sanctioned within days.",
        testimonial_name="Poonam Dixit", testimonial_role="Teacher, Lucknow",
    ),
    dict(
        slug="loan-mf-lic.html",
        title="Loan on Mutual Funds / LIC Policy",
        meta_description="Unlock liquidity against your mutual fund units or LIC policy without breaking your investment — AD Investments, Lucknow.",
        category="Loans", icon="🔐",
        h1="Loan on <em>MF / LIC</em>",
        hero_sub="Need funds without breaking your long-term investments? Borrow against your mutual fund units or LIC policy instead of redeeming them.",
        intro=[
            "Selling a long-term investment to meet a short-term cash need can permanently derail your financial plan and trigger tax on gains you didn't intend to realise yet. A loan against mutual funds or an LIC policy lets you access liquidity while your investment stays invested and continues working toward its original goal.",
            "We help you understand the eligible schemes/policies, the loan-to-value ratio offered, and the applicable interest rate before you pledge anything.",
        ],
        benefits=[
            ("📈", "Investment Stays Invested", "Your mutual fund units or LIC policy keep growing/earning while you use the loan amount."),
            ("⚡", "Faster Than Fresh Loans", "Often quicker to process than an unsecured personal loan, since the pledge itself is the security."),
            ("💰", "Competitive Interest", "Rates are typically lower than unsecured personal loans, given the collateral backing."),
            ("🧾", "No Tax Trigger", "Since you're not redeeming your investment, you avoid triggering capital gains tax on the pledged units."),
            ("🔓", "Partial Pledge Options", "Pledge only a portion of your holdings rather than your entire portfolio."),
            ("🔄", "Flexible Repayment", "Repayment structures suited to overdraft-style or term-loan formats depending on the lender."),
        ],
        points=[
            ("Eligibility Check First", "We confirm which of your holdings are actually eligible to be pledged before you apply."),
            ("LTV Transparency", "We explain the loan-to-value ratio offered against your specific fund/policy category."),
            ("Unwinding Guidance", "We explain how the pledge is released once the loan is repaid, so your investment returns to full liquidity."),
        ],
        faqs=[
            ("What percentage of my mutual fund value can I borrow?", "Loan-to-value typically differs for equity vs. debt mutual funds, with lenders generally offering a lower percentage against equity funds due to volatility — we'll confirm current ratios with the lender."),
            ("Does my mutual fund keep earning returns while pledged?", "Yes, your units remain invested and continue to be subject to market performance; the pledge only restricts you from redeeming them until the loan is repaid or the lien is released."),
            ("Can I take a loan against any LIC policy?", "Only certain policy types (typically traditional/endowment policies with a surrender value) are eligible; pure term plans generally do not qualify."),
            ("What happens if I don't repay the loan?", "As with any secured loan, the lender can adjust or liquidate the pledged units/policy value to recover the outstanding amount if repayment isn't made as agreed."),
        ],
        disclaimer_key="loan", default_interest="Loan on MF/LIC",
        testimonial="I needed funds for a business opportunity but didn't want to touch my mutual funds. Borrowing against them instead was exactly the solution AD Investments suggested.",
        testimonial_name="Rajesh Agarwal", testimonial_role="Small Business Owner, Lucknow",
    ),
    dict(
        slug="retirement.html",
        title="Retirement Planning",
        meta_description="Build a secure retirement corpus with a mix of NPS, mutual funds and systematic strategies designed for the long term — AD Investments, Lucknow.",
        category="Planning", icon="🎯",
        h1="Retirement <em>Planning</em>",
        hero_sub="Build a secure retirement corpus with NPS, mutual funds and systematic investment strategies designed specifically for the long term.",
        intro=[
            "Retirement planning isn't a single product — it's a strategy that combines the right mix of instruments, contribution discipline, and periodic review over decades. Starting early and staying consistent matters more than chasing the 'best' fund in any given year.",
            "We build a retirement roadmap around your target corpus, current age, and risk appetite, combining instruments like NPS, mutual funds, PPF and other options as appropriate — then revisit the plan as your income and goals evolve.",
        ],
        benefits=[
            ("🧮", "Corpus Goal Setting", "We help you estimate how much you'll realistically need at retirement, accounting for inflation."),
            ("⚖️", "Diversified Instrument Mix", "A blend across NPS, mutual funds and other instruments rather than relying on a single product."),
            ("📈", "Systematic Contributions", "SIP-based discipline that builds your corpus steadily rather than relying on lump-sum timing."),
            ("➕", "Tax-Efficient Structuring", "Instrument selection that also considers available tax deductions along the way."),
            ("🔄", "Periodic Rebalancing", "As retirement approaches, we help shift the mix toward more capital-preservation-focused instruments."),
            ("👴", "Post-Retirement Income Planning", "Guidance on structuring your corpus into a regular income stream once you actually retire."),
        ],
        points=[
            ("Age-Appropriate Strategy", "Your plan reflects where you are today — 30 and just starting, or 50 and catching up."),
            ("Realistic Corpus Targets", "We factor in inflation and lifestyle expectations rather than arbitrary round numbers."),
            ("Decades-Long Partnership", "We check in periodically as income, goals and market conditions change over your working years."),
        ],
        faqs=[
            ("At what age should I start retirement planning?", "The earlier the better — starting in your late 20s or early 30s lets compounding do much of the work, but it's never too late to start; we tailor the strategy to your current age."),
            ("How much should I save for retirement?", "This depends on your desired retirement lifestyle, expected expenses, inflation and years to retirement — we'll help you calculate a realistic, personalised target."),
            ("Should retirement savings be all equity or all debt?", "Neither extreme is usually ideal — a mix that shifts from growth-oriented (more equity) toward capital-preservation (more debt) as you approach retirement is a commonly recommended approach, though it depends on your individual risk profile."),
            ("Can I combine NPS with mutual funds for retirement?", "Yes, many investors use NPS for its tax benefits and disciplined lock-in alongside mutual fund SIPs for additional flexibility and liquidity."),
        ],
        disclaimer_key="market", default_interest="Retirement Planning",
        testimonial="At 35, retirement felt distant and abstract. AD Investments turned it into an actual number and a monthly plan I could follow.",
        testimonial_name="Sanjay Bhatt", testimonial_role="Bank Manager, Lucknow",
    ),
    dict(
        slug="stock-advisory.html",
        title="Stock Advisory",
        meta_description="Research-backed stock recommendations tailored to your risk appetite, combining fundamental and technical analysis — AD Investments, Lucknow.",
        category="Planning", icon="📈",
        h1="Stock <em>Advisory</em>",
        hero_sub="Research-backed stock recommendations tailored to your risk appetite. We analyse fundamentals, technicals and market trends so you don't have to.",
        intro=[
            "Direct equity investing can build significant wealth over time, but it demands research, discipline and the ability to separate noise from signal — three things most working professionals simply don't have hours in the day for.",
            "We track markets, screen companies on fundamentals and technicals, and share ideas suited to your risk profile and time horizon, whether you're looking to trade actively or build long-term equity positions.",
        ],
        benefits=[
            ("🔍", "Fundamental Analysis", "Stock ideas backed by analysis of financials, management quality and business fundamentals."),
            ("📉", "Technical Insights", "Entry and exit context informed by price action and technical indicators where relevant."),
            ("⚖️", "Risk-Matched Ideas", "Recommendations calibrated to whether you're conservative, moderate or aggressive in your equity approach."),
            ("📰", "Market Commentary", "Regular updates on market trends and events that could affect your holdings."),
            ("🎯", "Goal-Aligned Positioning", "Equity ideas positioned as part of your broader portfolio and goals, not standalone bets."),
            ("📞", "Direct Access", "A direct line to ask questions about a stock, sector or market move, rather than a faceless app notification."),
        ],
        points=[
            ("Research Before Recommendation", "Every idea we share is backed by analysis, not market rumour or tips."),
            ("Risk-First Framing", "We're upfront about the risk in every recommendation, not just the potential upside."),
            ("Ongoing Portfolio View", "We track how your equity ideas are performing together, not just as isolated picks."),
        ],
        faqs=[
            ("Is stock advisory suitable for beginners?", "Yes, but we tailor the pace and complexity to your experience — beginners typically start with a smaller, more conservative allocation while building familiarity with market movements."),
            ("Do you guarantee returns on recommended stocks?", "No — equity markets are inherently risky and no advisor can guarantee returns. Our recommendations are research-backed but subject to market risk, and past performance is not indicative of future results."),
            ("How often will I receive stock recommendations?", "This depends on market conditions and opportunities identified through our research — we prioritise quality of ideas over frequency."),
            ("What's the difference between stock advisory and a mutual fund?", "Stock advisory involves direct ownership of individual company shares based on our recommendations, requiring more active involvement from you, whereas mutual funds are professionally managed pooled investments — many investors use both."),
        ],
        disclaimer_key="market", default_interest="Stock Advisory",
        testimonial="I used to buy stocks on tips from friends. Having actual research behind each recommendation from AD Investments changed how I invest completely.",
        testimonial_name="Amit Saxena", testimonial_role="Chartered Accountant, Lucknow",
    ),
    dict(
        slug="hdfc-savings.html",
        title="HDFC Bank Saving Account",
        meta_description="Open an HDFC Bank Savings Account with guided assistance and doorstep documentation support — AD Investments, Lucknow.",
        category="Banking", icon="🏧",
        h1="HDFC Bank <em>Savings A/c</em>",
        hero_sub="Open an HDFC Bank Savings Account with guided, hassle-free assistance — from documentation to activation.",
        intro=[
            "A savings account is the foundation of everyday banking and the base from which SIPs, insurance premiums and bill payments are managed. As an HDFC Bank referral partner, we help you open the right variant of savings account for your needs.",
            "Whether it's a standard savings account, a salary account, or a variant with added benefits, we guide you through eligibility, documentation and the opening process.",
        ],
        benefits=[
            ("📝", "Guided Documentation", "We help you assemble KYC documents correctly the first time, avoiding processing delays."),
            ("🏠", "Doorstep Assistance", "Support coordinating document pickup and account-related formalities where available."),
            ("💳", "Debit Card & Net Banking Setup", "Assistance getting your debit card and net/mobile banking activated promptly."),
            ("💰", "Account Variant Guidance", "Understand the difference between regular, salary, and premium savings account variants."),
            ("🔗", "Linked to Your Financial Plan", "A savings account that fits into the broader financial structure we help you build."),
            ("📞", "Post-Opening Support", "We remain a point of contact for account-related questions after opening."),
        ],
        points=[
            ("One-Window Assistance", "We simplify what can otherwise be a multi-visit branch process."),
            ("Right Variant for You", "Not every savings account variant suits every customer — we help you pick correctly."),
            ("Ongoing Relationship", "Your savings account becomes the base account for other services we help you set up."),
        ],
        faqs=[
            ("What documents are needed to open an HDFC savings account?", "Typically PAN card, Aadhaar or another valid address proof, and a recent photograph — exact requirements can vary by account type and are confirmed at the time of application."),
            ("Is there a minimum balance requirement?", "Yes, most HDFC Bank savings account variants require a minimum average balance, which varies by account type and branch location — we'll confirm current requirements for the variant you choose."),
            ("How long does account activation take?", "Timelines depend on document verification and KYC completion; we help ensure your documentation is complete to avoid avoidable delays."),
            ("Can I link my mutual fund and insurance payments to this account?", "Yes, once active, your savings account can be used for SIP auto-debits, insurance premium payments and other recurring transactions we help set up for you."),
        ],
        disclaimer_key="banking", default_interest="HDFC Bank Saving Account",
        testimonial="Opening a new bank account always felt like a full day off work. AD Investments got my HDFC savings account activated with minimal branch visits.",
        testimonial_name="Neha Srivastava", testimonial_role="HR Professional, Lucknow",
    ),
    dict(
        slug="hdfc-credit.html",
        title="HDFC Credit Card",
        meta_description="Apply for an HDFC Bank Credit Card suited to your spending pattern, with guided application support — AD Investments, Lucknow.",
        category="Banking", icon="💎",
        h1="HDFC <em>Credit Card</em>",
        hero_sub="Apply for an HDFC Bank Credit Card matched to your spending pattern — travel, cashback, rewards or everyday use — with guided support.",
        intro=[
            "The right credit card can add real value through rewards, cashback and travel benefits, or become an expensive trap if it doesn't match your spending habits and repayment discipline. We help you choose based on how you actually spend, not just the flashiest offer.",
            "As an HDFC Bank referral partner, we guide you through the application, required documentation, and help set expectations on eligibility before you apply.",
        ],
        benefits=[
            ("🎁", "Spend-Matched Card Choice", "We recommend a card variant based on your actual spending categories — fuel, travel, groceries, dining."),
            ("✈️", "Travel & Rewards Options", "Access to cards offering travel miles, lounge access or reward points where suited to your lifestyle."),
            ("💸", "Cashback Options", "Straightforward cashback card variants for those who prefer simplicity over points programs."),
            ("📊", "Eligibility Guidance", "An honest read on your likely eligibility before you apply, to avoid unnecessary credit inquiries."),
            ("📝", "Application Support", "Help assembling the documentation needed for a smooth application process."),
            ("🧾", "Responsible Usage Tips", "Guidance on using credit responsibly to build your credit score rather than damage it."),
            ],
        points=[
            ("Card Matched to Lifestyle", "We don't push the highest-commission card — we match the card to your spending pattern."),
            ("Transparent on Fees", "Annual fees, interest rates and reward redemption terms are explained clearly upfront."),
            ("Credit Health Awareness", "We help you understand how card usage affects your credit score over time."),
        ],
        faqs=[
            ("What documents are needed to apply for a credit card?", "Typically PAN card, address proof, income proof (salary slips or ITR) and photographs — the exact list depends on the card variant and your employment type."),
            ("Will applying for a credit card affect my credit score?", "Yes, each application typically triggers a credit inquiry which can have a small, temporary impact on your credit score — this is why we help you check likely eligibility before applying."),
            ("What's the difference between a rewards card and a cashback card?", "Rewards cards accumulate points redeemable for products, travel or vouchers, often with category-based multipliers, while cashback cards return a percentage of your spend directly — the better choice depends on your spending habits."),
            ("How is my credit limit decided?", "HDFC Bank determines your credit limit based on your income, credit score, existing obligations and internal risk policies at the time of approval."),
        ],
        disclaimer_key="banking", default_interest="HDFC Credit Card",
        testimonial="AD Investments helped me pick an HDFC card that actually matched my travel spending instead of the generic one I almost signed up for.",
        testimonial_name="Karan Malhotra", testimonial_role="Sales Manager, Lucknow",
    ),
]

for svc in SERVICES:
    build_page(**svc)

# ---------------------------------------------------------------------------
# services.html — full services overview / index page
# ---------------------------------------------------------------------------

GROUPS = [
    ("Investments", "investments", [
        ("mutual-funds.html", "💼", "Mutual Funds", "SIP or lump sum across equity, debt and hybrid categories."),
        ("fixed-deposits.html", "🏦", "Fixed Deposits", "Safe, guaranteed returns with bank and corporate FDs."),
        ("demat.html", "📊", "Demat Services", "Open and manage your Demat account with expert guidance."),
        ("bonds.html", "📜", "NCD / RBI Bonds", "Fixed-income instruments for stable, predictable returns."),
        ("sgb.html", "🪙", "Sovereign Gold Bond", "Gold exposure with annual interest, no storage worries."),
        ("capital-gains.html", "🧾", "Capital Gain Bonds (54EC)", "Save LTCG tax on property sales under Section 54EC."),
        ("nps.html", "🏛️", "NPS", "Retirement savings with extra tax benefit under 80CCD(1B)."),
    ]),
    ("Insurance", "insurance", [
        ("life-insurance.html", "🛡️", "Life Insurance", "Term and life cover to protect your family's future."),
        ("health-insurance.html", "🩺", "Health Insurance", "Individual and family floater plans for medical emergencies."),
        ("motor-insurance.html", "🚗", "Motor Insurance", "Comprehensive cover for your car or two-wheeler."),
    ]),
    ("Loans", "loans", [
        ("home-loan.html", "🏠", "Home Loan", "Compare offers from top banks and NBFCs."),
        ("auto-loan.html", "🚙", "Auto Loan", "Financing for your next car or two-wheeler."),
        ("personal-loan.html", "💳", "Personal Loan", "Quick, unsecured funds for life's big and small needs."),
        ("loan-mf-lic.html", "🔐", "Loan on MF/LIC", "Unlock liquidity without breaking your investments."),
    ]),
    ("Planning", "planning", [
        ("retirement.html", "🎯", "Retirement Planning", "A systematic, long-term roadmap to your retirement corpus."),
        ("stock-advisory.html", "📈", "Stock Advisory", "Research-backed stock recommendations for your risk profile."),
    ]),
    ("Banking", "banking", [
        ("hdfc-savings.html", "🏧", "HDFC Bank Saving A/c", "Guided assistance to open your HDFC savings account."),
        ("hdfc-credit.html", "💎", "HDFC Credit Card", "A credit card matched to your spending pattern."),
    ]),
]


def render_services_index():
    groups_html = []
    for label, anchor, items in GROUPS:
        cards = []
        for slug, icon, title, desc in items:
            cards.append(f"""        <a href="{slug}" class="service-card reveal">
          <div class="service-icon">{icon}</div>
          <div class="service-title">{title}</div>
          <p class="service-desc">{desc}</p>
          <div class="service-arrow">→</div>
        </a>""")
        groups_html.append(f"""    <div class="services-index-group" id="{anchor}">
      <div class="services-index-label reveal">{label}</div>
      <div class="services-grid cols-3">
{chr(10).join(cards)}
      </div>
    </div>""")

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>All Services | AD Investments</title>
  <meta name="description" content="Explore all 18 financial services offered by AD Investments, Lucknow — investments, insurance, loans, planning and banking."/>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="assets/style.css"/>
</head>
<body>

{cursor_html()}
{whatsapp_float_html()}

  <!-- NAV -->
{nav_html()}

  <!-- PAGE HERO -->
  <section class="page-hero">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="hero-content" style="max-width:760px;">
{breadcrumb_html(None, "All Services")}
      <h1 style="font-size:clamp(40px,5.5vw,64px);">Every Way We Help You <em>Grow</em></h1>
      <p class="hero-sub" style="max-width:600px;">18 financial services across investments, insurance, loans, planning and banking — each backed by personalised, local guidance in Lucknow.</p>
      <div class="hero-actions">
        <a href="index.html#contact" class="btn-primary">Book Consultation</a>
      </div>
    </div>
  </section>

  <!-- SERVICES -->
  <section class="section" style="padding-top:0;">
{chr(10).join(groups_html)}
  </section>

{contact_section_html("Other", "Consultation")}

{footer_html()}

  <script src="assets/main.js"></script>
</body>
</html>
"""
    with open(os.path.join(OUT_DIR, "services.html"), "w") as f:
        f.write(body)
    print("wrote services.html")


render_services_index()
print("Done. Generated", len(SERVICES) + 1, "pages.")

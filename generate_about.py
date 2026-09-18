#!/usr/bin/env python3
"""Builds about.html, reusing shared components from generate.py.
Run after generate.py (or standalone — importing generate.py regenerates
the service pages too, which is harmless/idempotent).
"""
import os
import generate as g

OUT_DIR = g.OUT_DIR

body = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>About Us | AD Investments</title>
  <meta name="description" content="AD Investments is a Lucknow-based financial distribution company helping families invest, insure and plan with personalised, transparent guidance."/>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="assets/style.css"/>
</head>
<body>

{g.cursor_html()}
{g.whatsapp_float_html()}

  <!-- NAV -->
{g.nav_html()}

  <!-- PAGE HERO -->
  <section class="page-hero">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="hero-content" style="max-width:760px;">
{g.breadcrumb_html(None, "About Us")}
      <h1 style="font-size:clamp(40px,5.5vw,64px);">Lucknow's Trusted <em>Financial Partner</em></h1>
      <p class="hero-sub" style="max-width:620px;">AD Investments is a fully dedicated Financial Distribution Company based in Lucknow, helping families preserve and grow their wealth through disciplined, goal-based financial planning.</p>
      <div class="hero-actions">
        <a href="index.html#contact" class="btn-primary">Book Consultation</a>
        <a href="services.html" class="btn-secondary">
          Our Services
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>
  </section>

  <!-- STORY -->
  <section class="section" style="padding-top:0;">
    <div class="section-label reveal">
      <span>Our Story</span>
    </div>
    <h2 class="reveal">Built On <em style="font-style:italic;color:var(--gold)">Trust</em>, Not Transactions</h2>
    <p class="intro-text reveal">We started AD Investments with a simple belief — that Lucknow's salaried families and small business owners deserve the same quality of financial guidance available in bigger cities, delivered by people who actually know their names and their goals.</p>
    <p class="intro-text reveal">Today we support clients across investments, insurance, loans and banking, acting as a single point of contact instead of sending them from one product specialist to another. Every recommendation is weighed against one question: is this genuinely right for this client's situation?</p>
  </section>

  <!-- STATS -->
  <section class="section why-section" style="padding-top:60px;padding-bottom:60px;">
    <div class="services-grid cols-3">
      <div class="service-card reveal" style="cursor:default;text-align:center;">
        <div class="stat-number" style="margin:0 auto 8px;">50+</div>
        <div class="stat-label">Happy Clients</div>
      </div>
      <div class="service-card reveal" style="cursor:default;text-align:center;">
        <div class="stat-number" style="margin:0 auto 8px;">18</div>
        <div class="stat-label">Financial Services</div>
      </div>
      <div class="service-card reveal" style="cursor:default;text-align:center;">
        <div class="stat-number" style="margin:0 auto 8px;">2+</div>
        <div class="stat-label">Years of Service</div>
      </div>
    </div>
  </section>

  <!-- WHY US -->
  <section class="section why-section" id="why">
    <div class="why-grid">
      <div class="why-left reveal">
        <div class="section-label">
          <span>Why AD Investments</span>
        </div>
        <h2>Trusted by Families <em style="font-style:italic;color:var(--gold)">Across Lucknow</em></h2>
        <p>We're not a faceless corporation. We're a local firm that understands the aspirations of Lucknow's salaried families — and we've been guiding them for over a decade combined experience.</p>
        <div class="why-points">
          <div class="why-point">
            <div class="why-num">01</div>
            <div class="why-text">
              <strong>Personalised Advice</strong>
              <span>No generic recommendations. Every plan is built around your specific income, goals, and risk tolerance.</span>
            </div>
          </div>
          <div class="why-point">
            <div class="why-num">02</div>
            <div class="why-text">
              <strong>Transparent Process</strong>
              <span>You always know where your money is, how it's performing, and what we're doing with it.</span>
            </div>
          </div>
          <div class="why-point">
            <div class="why-num">03</div>
            <div class="why-text">
              <strong>Long Term Relationship</strong>
              <span>We grow with you — from your first SIP to building a multi-crore portfolio over decades.</span>
            </div>
          </div>
        </div>
      </div>
      <div class="why-right reveal">
        <div class="why-visual">
          <p class="testimonial-text">"AD Investments helped me start my first SIP 6 years ago. Today my portfolio has grown beyond what I ever imagined. They feel like family."</p>
          <div class="testimonial-author">
            <div class="author-avatar">R</div>
            <div>
              <div class="author-name">Rahul Srivastava</div>
              <div class="author-role">Government Employee, Lucknow</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- WHAT WE OFFER -->
  <section class="section" style="padding-top:0;">
    <div class="section-label reveal">
      <span>What We Offer</span>
    </div>
    <h2 class="reveal">Five Pillars, <em style="font-style:italic;color:var(--gold)">One Advisor</em></h2>
    <div class="services-grid cols-3">
      <a href="services.html#investments" class="service-card reveal">
        <div class="service-icon">📈</div>
        <div class="service-title">Investments</div>
        <p class="service-desc">Mutual funds, FDs, Demat, bonds, SGB, capital gain bonds and NPS.</p>
        <div class="service-arrow">→</div>
      </a>
      <a href="services.html#insurance" class="service-card reveal">
        <div class="service-icon">🛡️</div>
        <div class="service-title">Insurance</div>
        <p class="service-desc">Life, health and motor insurance matched to your family's needs.</p>
        <div class="service-arrow">→</div>
      </a>
      <a href="services.html#loans" class="service-card reveal">
        <div class="service-icon">🏠</div>
        <div class="service-title">Loans</div>
        <p class="service-desc">Home, auto, personal loans and loans against MF/LIC.</p>
        <div class="service-arrow">→</div>
      </a>
      <a href="services.html#planning" class="service-card reveal">
        <div class="service-icon">🎯</div>
        <div class="service-title">Planning</div>
        <p class="service-desc">Retirement planning and research-backed stock advisory.</p>
        <div class="service-arrow">→</div>
      </a>
      <a href="services.html#banking" class="service-card reveal">
        <div class="service-icon">🏧</div>
        <div class="service-title">Banking</div>
        <p class="service-desc">HDFC Bank savings account and credit card assistance.</p>
        <div class="service-arrow">→</div>
      </a>
      <a href="index.html#contact" class="service-card reveal">
        <div class="service-icon">📞</div>
        <div class="service-title">Talk To Us</div>
        <p class="service-desc">Book a free, no-commitment consultation to review your finances.</p>
        <div class="service-arrow">→</div>
      </a>
    </div>
  </section>

{g.contact_section_html("Other", "Consultation")}

{g.footer_html()}

  <!-- DISCLAIMER -->
{g.DISCLAIMERS["mf"]}

  <script src="assets/main.js"></script>
</body>
</html>
"""

with open(os.path.join(OUT_DIR, "about.html"), "w") as f:
    f.write(body)
print("wrote about.html")

---
title: Tech Radar chart
hide: [toc]
---

# Tech Radar chart

Welcome to our **Interactive Technology Radar**. This responsive living map visualises the 77 technologies, frameworks, operational platforms, and engineering patterns evaluated across our software and systems practice.

- **Touch & Click Friendly**: Tap or click any numbered marker on the radar or in the mobile-friendly directory below to view detailed rationale, tags, and guideline links.
- **Filter & Search**: Use the quadrant and ring filter buttons or type in the search bar to highlight specific technologies.
- **Methodology & Rules**: Read **[Overview & Methodology](../radar/)** for ring criteria and ARB governance.
- **Tabular Directory**: View the complete reference catalog in the **[Complete Blips Directory](../radar/directory/)**.

<div id="radar-container" class="radar-app-root">

  <!-- Mobile View Switcher (Visible on mobile/tablet) -->
  <div class="radar-mobile-switcher">
    <button type="button" id="tab-canvas-btn" class="mobile-tab-btn active-tab">🧭 Visual Radar</button>
    <button type="button" id="tab-list-btn" class="mobile-tab-btn">📋 Technology List</button>
  </div>

  <!-- Controls Toolbar -->
  <div class="radar-toolbar">
    <!-- Search box -->
    <div class="radar-search-box">
      <input type="text" id="radar-search" placeholder="🔍 Search technologies, tags..." 
             aria-label="Search technologies" />
    </div>

    <!-- Quadrant Filter -->
    <div class="radar-quad-filter">
      <label for="radar-quad-select" class="radar-label">Quadrant:</label>
      <select id="radar-quad-select" aria-label="Select Quadrant">
        <option value="all">All Quadrants</option>
        <option value="languages-and-frameworks">1. Languages & Frameworks</option>
        <option value="platforms-and-operations">2. Platforms & Operations</option>
        <option value="tools">3. Tools & Utilities</option>
        <option value="methods-and-patterns">4. Methods & Patterns</option>
      </select>
    </div>

    <!-- Ring Filter Buttons -->
    <div class="radar-ring-filter">
      <span class="radar-label">Ring:</span>
      <div class="ring-btn-group">
        <button type="button" class="ring-filter-btn" data-ring="all">All</button>
        <button type="button" class="ring-filter-btn" data-ring="adopt">Adopt</button>
        <button type="button" class="ring-filter-btn" data-ring="trial">Trial</button>
        <button type="button" class="ring-filter-btn" data-ring="assess">Assess</button>
        <button type="button" class="ring-filter-btn" data-ring="hold">Hold</button>
      </div>
    </div>

    <!-- Domain Tag Filter -->
    <div class="radar-tag-filter">
      <span class="radar-label">Domain:</span>
      <div class="tag-btn-group" id="radar-tag-group">
        <button type="button" class="tag-filter-chip active-tag-chip" data-tag="all">All</button>
        <button type="button" class="tag-filter-chip" data-tag="embedded">#embedded</button>
        <button type="button" class="tag-filter-chip" data-tag="cloud">#cloud</button>
        <button type="button" class="tag-filter-chip" data-tag="security">#security</button>
        <button type="button" class="tag-filter-chip" data-tag="architecture">#architecture</button>
        <button type="button" class="tag-filter-chip" data-tag="devops">#devops</button>
        <button type="button" class="tag-filter-chip" data-tag="iot">#iot</button>
      </div>
    </div>
  </div>

  <!-- Radar Graphic Canvas Card -->
  <div id="radar-canvas-panel" class="radar-canvas-card">
    <div id="radar-svg-wrapper" class="radar-svg-container">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="100%" height="auto" style="width: 100%; max-width: 800px; height: auto; aspect-ratio: 1 / 1; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; display: block; margin: 0 auto;">
        <defs>
          <radialGradient id="grad-adopt" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#4CAF50" stop-opacity="0.18"/><stop offset="100%" stop-color="#4CAF50" stop-opacity="0.08"/></radialGradient>
          <radialGradient id="grad-trial" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#2196F3" stop-opacity="0.15"/><stop offset="100%" stop-color="#2196F3" stop-opacity="0.06"/></radialGradient>
          <radialGradient id="grad-assess" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FF9800" stop-opacity="0.15"/><stop offset="100%" stop-color="#FF9800" stop-opacity="0.06"/></radialGradient>
          <radialGradient id="grad-hold" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#F44336" stop-opacity="0.12"/><stop offset="100%" stop-color="#F44336" stop-opacity="0.05"/></radialGradient>
          <filter id="blip-shadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-color="#000" flood-opacity="0.25"/></filter>
        </defs>
        <rect class="radar-svg-bg" width="800" height="800" rx="16" />
        <circle cx="400" cy="400" r="350" fill="url(#grad-hold)" stroke="#ef9a9a" stroke-width="1.5" stroke-dasharray="4,4"/>
        <circle cx="400" cy="400" r="270" fill="url(#grad-assess)" stroke="#ffe082" stroke-width="1.5" stroke-dasharray="4,4"/>
        <circle cx="400" cy="400" r="190" fill="url(#grad-trial)" stroke="#90caf9" stroke-width="1.5" stroke-dasharray="4,4"/>
        <circle cx="400" cy="400" r="110" fill="url(#grad-adopt)" stroke="#a5d6a7" stroke-width="2"/>
        <line class="radar-grid-line" x1="45" y1="400" x2="755" y2="400" stroke-width="2" />
        <line class="radar-grid-line" x1="400" y1="45" x2="400" y2="755" stroke-width="2" />
        <text class="radar-ring-label ring-adopt" x="400" y="380" text-anchor="middle" font-size="12" font-weight="800" letter-spacing="1.5">ADOPT</text>
        <text class="radar-ring-label ring-trial" x="400" y="250" text-anchor="middle" font-size="12" font-weight="800" letter-spacing="1.5">TRIAL</text>
        <text class="radar-ring-label ring-assess" x="400" y="155" text-anchor="middle" font-size="12" font-weight="800" letter-spacing="1.5">ASSESS</text>
        <text class="radar-ring-label ring-hold" x="400" y="75" text-anchor="middle" font-size="12" font-weight="800" letter-spacing="1.5">HOLD</text>
        <text class="radar-quad-title" x="55" y="38" font-size="15" font-weight="800">1. LANGUAGES &amp; FRAMEWORKS</text>
        <text class="radar-quad-title" x="745" y="38" text-anchor="end" font-size="15" font-weight="800">2. PLATFORMS &amp; OPERATIONS</text>
        <text class="radar-quad-title" x="55" y="775" font-size="15" font-weight="800">3. TOOLS &amp; UTILITIES</text>
        <text class="radar-quad-title" x="745" y="775" text-anchor="end" font-size="15" font-weight="800">4. METHODS &amp; PATTERNS</text>
        <g class="radar-blip" id="blip-1" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="446.9" cy="410.8" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="446.9" cy="410.8" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="446.9" y="414.3" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">1</text>
          <title>#1 ADRs (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-2" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="461.4" cy="419.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="461.4" cy="419.3" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="461.4" y="422.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">2</text>
          <title>#2 Agile (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-3" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="410.8" cy="446.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="410.8" cy="446.9" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="410.8" y="450.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">3</text>
          <title>#3 arc42 (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-4" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="478.6" cy="418.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="478.6" cy="418.1" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="478.6" y="421.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">4</text>
          <title>#4 AsyncAPI (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-5" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="492.4" cy="429.0" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="492.4" cy="429.0" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="492.4" y="432.5" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">5</text>
          <title>#5 Barr Group Coding Guidelines (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-6" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="337.9" cy="362.7" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="337.9" cy="362.7" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="337.9" y="366.2" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">6</text>
          <title>#6 C# (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-7" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="312.1" cy="366.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="312.1" cy="366.3" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="312.1" y="369.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">7</text>
          <title>#7 C++ (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-8" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="352.5" cy="381.8" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="352.5" cy="381.8" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="352.5" y="385.3" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">8</text>
          <title>#8 C (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-9" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="458.1" cy="427.7" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="458.1" cy="427.7" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="458.1" y="431.2" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">9</text>
          <title>#9 C4 Model (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-10" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="444.9" cy="417.2" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="444.9" cy="417.2" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="444.9" y="420.7" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">10</text>
          <title>#10 C4 (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-11" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="204.2" cy="279.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="204.2" cy="279.3" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="204.2" y="282.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">11</text>
          <title>#11 CertC (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-12" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="475.3" cy="428.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="475.3" cy="428.9" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="475.3" y="432.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">12</text>
          <title>#12 CICD (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-13" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="562.6" cy="237.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="562.6" cy="237.4" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="562.6" y="240.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">13</text>
          <title>#13 CloudEvents (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-14" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="279.3" cy="595.8" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="279.3" cy="595.8" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="279.3" y="599.3" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">14</text>
          <title>#14 Coverity (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-15" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="592.9" cy="474.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="592.9" cy="474.1" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="592.9" y="477.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">15</text>
          <title>#15 CQRS (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-16" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="442.1" cy="423.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="442.1" cy="423.3" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="442.1" y="426.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">16</text>
          <title>#16 Diátaxis (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-17" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="423.8" cy="349.0" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="423.8" cy="349.0" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="423.8" y="352.5" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">17</text>
          <title>#17 Docker (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-18" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="470.5" cy="439.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="470.5" cy="439.1" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="470.5" y="442.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">18</text>
          <title>#18 Docs as code (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-19" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="453.7" cy="435.5" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="453.7" cy="435.5" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="453.7" y="439.0" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">19</text>
          <title>#19 DoD (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-20" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="480.8" cy="453.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="480.8" cy="453.4" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="480.8" y="456.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">20</text>
          <title>#20 Domain-driven design (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-21" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="597.1" cy="518.5" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="597.1" cy="518.5" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="597.1" y="522.0" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">21</text>
          <title>#21 DoR (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-22" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="487.5" cy="441.6" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="487.5" cy="441.6" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="487.5" y="445.1" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">22</text>
          <title>#22 DRY (Don't Repeat Yourself) (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-23" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="448.3" cy="442.6" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="448.3" cy="442.6" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="448.3" y="446.1" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">23</text>
          <title>#23 Edge Architectures for IoT (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-24" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="438.4" cy="429.0" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="438.4" cy="429.0" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="438.4" y="432.5" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">24</text>
          <title>#24 ETSI EN 303 645 (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-25" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="441.9" cy="448.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="441.9" cy="448.9" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="441.9" y="452.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">25</text>
          <title>#25 Event-Driven Architecture (EDA) (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-26" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="464.4" cy="448.5" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="464.4" cy="448.5" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="464.4" y="452.0" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">26</text>
          <title>#26 Event Driven (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-27" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="636.5" cy="490.8" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="636.5" cy="490.8" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="636.5" y="494.3" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">27</text>
          <title>#27 Event Sourcing (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-28" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="434.0" cy="434.0" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="434.0" cy="434.0" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="434.0" y="437.5" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">28</text>
          <title>#28 Event storming (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-29" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="472.6" cy="464.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="472.6" cy="464.1" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="472.6" y="467.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">29</text>
          <title>#29 Event Streaming (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-30" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="455.0" cy="330.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="455.0" cy="330.4" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="455.0" y="333.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">30</text>
          <title>#30 FreeRTOS (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-31" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="347.5" cy="420.2" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="347.5" cy="420.2" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="347.5" y="423.7" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">31</text>
          <title>#31 gcc (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-32" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="359.4" cy="369.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="359.4" cy="369.4" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="359.4" y="372.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">32</text>
          <title>#32 Go (golang) (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-33" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="439.8" cy="360.2" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="439.8" cy="360.2" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="439.8" y="363.7" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">33</text>
          <title>#33 Google Cloud Platform (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-34" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="350.6" cy="347.0" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="350.6" cy="347.0" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="350.6" y="350.5" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">34</text>
          <title>#34 GraphQL (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-35" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="410.1" cy="463.6" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="410.1" cy="463.6" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="410.1" y="467.1" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">35</text>
          <title>#35 gRPC (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-36" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="565.1" cy="524.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="565.1" cy="524.4" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="565.1" y="527.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">36</text>
          <title>#36 ISO 30141 (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-37" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="324.8" cy="343.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="324.8" cy="343.3" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="324.8" y="346.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">37</text>
          <title>#37 JSON (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-38" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="463.0" cy="473.6" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="463.0" cy="473.6" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="463.0" y="477.1" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">38</text>
          <title>#38 Kanban (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-39" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="457.0" cy="457.0" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="457.0" cy="457.0" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="457.0" y="460.5" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">39</text>
          <title>#39 KISS (Keep It Simple, Stupid) (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-40" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="429.0" cy="438.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="429.0" cy="438.4" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="429.0" y="441.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">40</text>
          <title>#40 Layered Architecture (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-41" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="434.6" cy="454.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="434.6" cy="454.3" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="434.6" y="457.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">41</text>
          <title>#41 Lightweight Architecture Evaluations (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-42" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="369.4" cy="359.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="369.4" cy="359.4" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="369.4" y="362.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">42</text>
          <title>#42 Markdown (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-43" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="379.8" cy="452.5" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="379.8" cy="452.5" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="379.8" y="456.0" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">43</text>
          <title>#43 Mermaid (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-44" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="292.2" cy="507.8" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="292.2" cy="507.8" r="10" fill="#1565c0" stroke="#ffffff" stroke-width="1.5" />
          <text x="292.2" y="511.3" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">44</text>
          <title>#44 Mermaid Diagrams (TRIAL)</title>
        </g>
        <g class="radar-blip" id="blip-45" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="452.1" cy="481.7" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="452.1" cy="481.7" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="452.1" y="485.2" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">45</text>
          <title>#45 Microservices (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-46" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="279.3" cy="204.2" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="279.3" cy="204.2" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="279.3" y="207.7" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">46</text>
          <title>#46 MISRA C++ (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-47" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="448.5" cy="464.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="448.5" cy="464.4" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="448.5" y="467.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">47</text>
          <title>#47 MISRA C (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-48" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="423.3" cy="442.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="423.3" cy="442.1" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="423.3" y="445.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">48</text>
          <title>#48 Modular Monolith (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-49" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="475.5" cy="353.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="475.5" cy="353.4" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="475.5" y="356.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">49</text>
          <title>#49 MQTT (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-50" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="418.1" cy="478.6" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="418.1" cy="478.6" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="418.1" y="482.1" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">50</text>
          <title>#50 oauth2 (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-51" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="354.3" cy="476.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="354.3" cy="476.1" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="354.3" y="479.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">51</text>
          <title>#51 OpenAPI (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-52" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="426.8" cy="458.6" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="426.8" cy="458.6" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="426.8" y="462.1" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">52</text>
          <title>#52 OWASP (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-53" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="439.1" cy="470.5" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="439.1" cy="470.5" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="439.1" y="474.0" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">53</text>
          <title>#53 PEP 8 (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-54" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="366.1" cy="444.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="366.1" cy="444.9" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="366.1" y="448.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">54</text>
          <title>#54 PlantUML (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-55" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="386.2" cy="328.8" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="386.2" cy="328.8" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="386.2" y="332.3" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">55</text>
          <title>#55 protobuf (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-56" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="367.1" cy="335.4" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="367.1" cy="335.4" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="367.1" y="338.9" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">56</text>
          <title>#56 Python (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-57" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="440.3" cy="488.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="440.3" cy="488.1" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="440.3" y="491.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">57</text>
          <title>#57 REST (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-58" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="556.9" cy="568.2" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="556.9" cy="568.2" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="556.9" y="571.7" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">58</text>
          <title>#58 RFC9457 (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-59" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="443.9" cy="625.8" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="443.9" cy="625.8" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="443.9" y="629.3" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">59</text>
          <title>#59 rRPC (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-60" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="343.3" cy="324.8" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="343.3" cy="324.8" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="343.3" y="328.3" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">60</text>
          <title>#60 Rust (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-61" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="417.2" cy="444.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="417.2" cy="444.9" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="417.2" y="448.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">61</text>
          <title>#61 Scrum (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-62" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="602.3" cy="552.5" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="602.3" cy="552.5" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="602.3" y="556.0" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">62</text>
          <title>#62 SEI ATAM (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-63" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="524.4" cy="565.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="524.4" cy="565.1" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="524.4" y="568.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">63</text>
          <title>#63 SEI CBAM (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-64" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="451.0" cy="376.2" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="451.0" cy="376.2" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="451.0" y="379.7" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">64</text>
          <title>#64 Serverless (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-65" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="504.4" cy="604.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="504.4" cy="604.9" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="504.4" y="608.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">65</text>
          <title>#65 SOA (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-66" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="335.1" cy="460.5" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="335.1" cy="460.5" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="335.1" y="464.0" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">66</text>
          <title>#66 SQLite (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-67" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="204.2" cy="520.7" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="204.2" cy="520.7" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="204.2" y="524.2" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">67</text>
          <title>#67 Structurizr (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-68" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="418.3" cy="461.7" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="418.3" cy="461.7" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="418.3" y="465.2" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">68</text>
          <title>#68 TOGAF (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-69" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="428.9" cy="475.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="428.9" cy="475.3" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="428.9" y="478.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">69</text>
          <title>#69 UML Modeling (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-70" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="552.5" cy="602.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="552.5" cy="602.3" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="552.5" y="605.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">70</text>
          <title>#70 V-Model (ASSESS)</title>
        </g>
        <g class="radar-blip" id="blip-71" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="320.9" cy="440.3" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="320.9" cy="440.3" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="320.9" y="443.8" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">71</text>
          <title>#71 Visual Studio Code (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-72" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="355.1" cy="433.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="355.1" cy="433.9" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="355.1" y="437.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">72</text>
          <title>#72 VS code (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-73" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="622.7" cy="622.7" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="622.7" cy="622.7" r="10" fill="#c62828" stroke="#ffffff" stroke-width="1.5" />
          <text x="622.7" y="626.2" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">73</text>
          <title>#73 Waterfall (HOLD)</title>
        </g>
        <g class="radar-blip" id="blip-74" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="427.6" cy="492.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="427.6" cy="492.9" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="427.6" y="496.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">74</text>
          <title>#74 YAGNI (You Aren’t Gonna Need It) (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-75" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="381.8" cy="352.5" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="381.8" cy="352.5" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="381.8" y="356.0" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">75</text>
          <title>#75 YAML (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-76" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="486.9" cy="382.1" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="486.9" cy="382.1" r="10" fill="#2e7d32" stroke="#ffffff" stroke-width="1.5" />
          <text x="486.9" y="385.6" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">76</text>
          <title>#76 Yocto Project (ADOPT)</title>
        </g>
        <g class="radar-blip" id="blip-77" filter="url(#blip-shadow)" style="touch-action: manipulation; cursor: pointer;">
          <circle cx="474.1" cy="592.9" r="24" fill="transparent" pointer-events="all" class="touch-target" />
          <circle cx="474.1" cy="592.9" r="10" fill="#e65100" stroke="#ffffff" stroke-width="1.5" />
          <text x="474.1" y="596.4" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">77</text>
          <title>#77 Zachman Framework (ASSESS)</title>
        </g>
      </svg>
    </div>
    
    <!-- Floating Info Note -->
    <div class="radar-hint-note">
      💡 <em>Tap or click any numbered marker on the radar to inspect complete technical details.</em>
    </div>
  </div>

  <!-- Modal Popup Component -->
  <div id="radar-modal-overlay" class="radar-modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div id="radar-modal-card" class="radar-modal-container">
      
      <!-- Modal Header -->
      <div class="radar-modal-header">
        <div class="radar-modal-header-text">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span id="modal-id" class="modal-id-badge"></span>
            <h2 id="modal-title" class="modal-title-text"></h2>
          </div>
          <div class="modal-meta-row">
            <span id="modal-ring-badge" class="modal-ring-chip"></span>
            <span id="modal-quadrant" class="modal-quadrant-text"></span>
          </div>
        </div>
        <button type="button" id="modal-close-btn" class="modal-close-button" aria-label="Close dialog">&times;</button>
      </div>

      <!-- Modal Body -->
      <div class="radar-modal-body">
        <!-- Tags Container -->
        <div id="modal-tags" class="modal-tags-container"></div>
        
        <!-- Description & Rationale -->
        <div id="modal-body-text" class="modal-body-content"></div>
      </div>

      <!-- Modal Footer -->
      <div id="modal-footer" class="radar-modal-footer">
        <div id="modal-link-container"></div>
        <button type="button" id="modal-dismiss-btn" class="modal-dismiss-btn">Dismiss</button>
      </div>
    </div>
  </div>

  <!-- Synchronized Quadrant Lists Below Radar -->
  <div id="radar-list-panel" class="radar-list-container">
    <h2 class="radar-list-title">Technologies by Quadrant</h2>
    <div class="radar-cards-grid" id="radar-cards-grid"></div>
  </div>

</div>

<!-- Client-side Interactive Script -->
<script>
(function() {
  const blipsData = [{"id": 1, "title": "ADRs", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["documentation", "decision-making"], "body": "Architectural Decision Records (ADRs) are a proven method for capturing important architectural decisions made during a project. By documenting these decisions, teams can ensure that the rationale behind key architectural choices is recorded for future reference. This practice enhances communication among team members and stakeholders, providing a clear historical context that aids in understanding the evolution of a system's architecture.\n\nADRs are particularly useful in agile environments where decisions are made frequently and need to be communicated efficiently. They help in maintaining a lightweight and accessible record of decisions, which is crucial for onboarding new team members or revisiting past decisions when the context or requirements change.\n\nThe adoption of ADRs is recommended in the methods-and-patterns quadrant as it reflects a mature approach to managing architectural complexity through structured documentation. As teams increasingly recognize the value of maintaining decision logs, ADRs have become a standard practice in many organizations, emphasizing their relevance in the adopt ring.", "link": "../guides/decision-records/", "link_title": "ADR Authoring Guide (GU-005)", "x": 446.9, "y": 410.8}, {"id": 2, "title": "Agile", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["software-development", "project-management"], "body": "Agile is a set of principles and practices for software development that emphasizes flexibility, collaboration, and customer satisfaction. It involves iterative development, where requirements and solutions evolve through the collaborative efforts of cross-functional teams. Agile methodologies, such as Scrum and Kanban, focus on delivering small, incremental changes quickly, allowing for frequent reassessment and adjustment. This approach enhances the ability to respond to change effectively, making it a valuable method in dynamic and complex environments. In the methods-and-patterns quadrant, Agile is placed in the adopt ring due to its widespread acceptance and proven success in improving project outcomes and fostering innovation across various industries.", "link": "../guides/agile-requirements-and-user-stories/", "link_title": "Agile Requirements & User Stories (GU-024)", "x": 461.4, "y": 419.3}, {"id": 3, "title": "arc42", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["software-architecture", "documentation"], "body": "arc42 is a template for documenting software and system architectures. It is designed to help architects efficiently communicate design decisions and structural concepts without being overly prescriptive. The template is structured to cover all relevant aspects of an architecture, including requirements, constraints, quality goals, and the rationale behind architectural decisions.\n\narc42 is particularly useful for ensuring consistency and clarity in architectural documentation, making it easier for teams to understand and work with complex systems. Given its flexibility and comprehensive nature, it has become a widely adopted standard in the industry for architecture documentation, which is why it resides in the \"adopt\" ring.\n\nIn the \"methods-and-patterns\" quadrant, arc42 is relevant because it provides a structured approach to documenting architectures, which is an essential part of the architectural process. By adopting arc42, organizations can improve communication across teams and stakeholders, facilitating better understanding and collaboration in software development projects.", "link": "../handbook/01-introduction-to-architecture/", "link_title": "Architecture Handbook: Foundations (GD-002)", "x": 410.8, "y": 446.9}, {"id": 4, "title": "AsyncAPI", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["event-driven-architecture", "api-specification"], "body": "AsyncAPI is an open-source initiative that provides a specification for defining event-driven architectures. Similar to how OpenAPI specifies RESTful APIs, AsyncAPI focuses on asynchronous APIs, allowing developers to standardize the communication between microservices and other components in distributed systems. It is highly useful for creating a clear, machine-readable contract for services that utilize messaging systems such as Kafka, MQTT, or RabbitMQ.\n\nThe relevance of AsyncAPI in the methods-and-patterns quadrant stems from its ability to enhance the design and documentation processes of complex, event-driven systems. By adopting AsyncAPI, organizations can improve collaboration between different teams, streamline integration processes, and ensure consistency across their asynchronous communication channels. Its adoption is growing as event-driven architectures become more prevalent in systems requiring scalable and resilient communication patterns.", "link": "../standards/api-design/", "link_title": "API Design Standards (GU-020)", "x": 478.6, "y": 418.1}, {"id": 5, "title": "Barr Group Coding Guidelines", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["embedded-systems", "safety-critical"], "body": "The Barr Group Coding Guidelines are a set of coding standards specifically designed for the development of embedded system software. These guidelines emphasize the importance of writing clear, maintainable, and reliable code to ensure the safety and efficiency of embedded systems, which are often used in critical applications like automotive, medical devices, and industrial control systems.\n\nAdopting the Barr Group Coding Guidelines is beneficial as they provide best practices for avoiding common programming pitfalls and enhancing code quality. Key areas of focus include naming conventions, commenting, and the use of assertions and error handling. By following these guidelines, developers can produce more robust and less error-prone software, which is crucial in environments where failure could lead to significant harm or damage.\n\nThe relevance of these guidelines in the \"methods-and-patterns\" quadrant stems from their role in shaping the way developers think and approach coding in embedded systems. In the \"adopt\" ring, they represent a mature and widely-accepted practice that can significantly improve the quality and reliability of software in the embedded systems domain.", "link": "../standards/c-coding-standard/", "link_title": "C Coding Standards (GU-009)", "x": 492.4, "y": 429.0}, {"id": 6, "title": "C#", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["object-oriented", "cross-platform", "microsoft-ecosystem"], "body": "C# is a modern, object-oriented programming language developed by Microsoft as part of its .NET initiative. It is designed for building a wide range of applications, from web and mobile apps to enterprise software and cloud-based solutions. C# is known for its ease of use, safety, and versatility, making it a popular choice among developers.\n\nIn the \"languages-and-frameworks\" quadrant, C# stands out due to its robust feature set, including strong typing, automatic memory management, and extensive libraries. It is particularly well-suited for developing applications within the Microsoft ecosystem, but it also supports cross-platform development with the advent of .NET Core and .NET 5/6, allowing applications to run on Windows, Linux, and macOS.\n\nAdopting C# is recommended because of its mature tooling, strong community support, and continuous evolution aligned with modern software development needs. Its integration with Azure and other cloud services further enhances its relevance in today's technology landscape, making it a strategic choice for organizations looking to build scalable, maintainable, and efficient applications.", "link": "../primers/programming-and-tools/", "link_title": "Programming & Tools Primer", "x": 337.9, "y": 362.7}, {"id": 7, "title": "C++", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["object-oriented", "performance-critical", "systems-programming"], "body": "C++ is a general-purpose programming language known for its high performance and efficiency. It supports object-oriented, procedural, and generic programming, making it versatile for a wide range of applications. C++ is particularly useful for systems programming, game development, and applications requiring real-time processing or resource-constrained environments, such as embedded systems. Its ability to directly manipulate hardware resources, coupled with extensive libraries and frameworks, makes it an essential language in areas where performance is critical.\n\nIn the context of languages and frameworks, C++ remains highly relevant as it continually evolves with new standards, such as C++20 and the upcoming C++23, which introduce modern features and improvements. Its adoption is crucial for projects where performance and fine-grained control over system resources are paramount, supporting complex systems and large-scale applications with high reliability and efficiency.", "link": "../standards/c-coding-standard/", "link_title": "C Coding Standards (GU-009)", "x": 312.1, "y": 366.3}, {"id": 8, "title": "C", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["systems-programming", "embedded-systems", "performance"], "body": "C is a general-purpose, procedural programming language that has been a cornerstone of software development since its creation in the early 1970s. Known for its efficiency and control over system resources, C is particularly useful for system programming, such as operating systems, device drivers, and embedded systems. Its syntax and structure have influenced many other languages, making it a foundational language for software engineers.\n\nIn the languages-and-frameworks quadrant, C's relevance is undeniable due to its widespread adoption for performance-critical applications. The \"adopt\" ring reflects its mature status and the industry's continued reliance on it for developing robust, high-performance systems. Despite the emergence of higher-level languages, C remains a vital tool for developers needing fine-grained control over hardware and resources. Its ongoing utility in systems programming and embedded development underscores its enduring importance in the tech landscape.", "link": "../standards/c-coding-standard/", "link_title": "C Coding Standards (GU-009)", "x": 352.5, "y": 381.8}, {"id": 9, "title": "C4 Model", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["architecture"], "body": "C4 Model provides a simple, hierarchical way to visualize architecture.", "link": "../guides/c4-model/", "link_title": "C4 Architecture Modelling Guide (GD-001)", "x": 458.1, "y": 427.7}, {"id": 10, "title": "C4", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["software-architecture", "documentation", "modeling"], "body": "The C4 model is a framework for visualizing the architecture of software systems. It provides a set of hierarchical diagrams, namely Context, Container, Component, and Code, that help teams understand and communicate the structure and design of their software. By using these diagrams, teams can ensure that everyone—from developers to stakeholders—has a clear and consistent understanding of how the system is structured and how its components interact.\n\nC4 is particularly useful because it strikes a balance between simplicity and detail, making it easier for teams to maintain and use over time compared to more complex architectural frameworks. Its relevance in the \"methods-and-patterns\" quadrant reflects its role as a best practice for documenting and designing software architecture. The \"adopt\" ring indicates that it is a mature and widely accepted approach in the industry, recommended for use in most projects to enhance clarity and communication.", "link": "../guides/c4-model/", "link_title": "C4 Architecture Modelling Guide (GD-001)", "x": 444.9, "y": 417.2}, {"id": 11, "title": "CertC", "ring": "assess", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["safety-critical", "embedded-systems"], "body": "CertC is a programming language extension and a set of guidelines designed to enhance the safety and reliability of C code, particularly in safety-critical and embedded system environments. Its main purpose is to address common pitfalls in C programming, such as buffer overflows and undefined behaviors, which can lead to catastrophic failures in critical systems. By providing stricter rules and additional checks, CertC helps developers write more robust and predictable code.\n\nThe relevance of CertC in the languages-and-frameworks quadrant is significant due to its focus on improving code safety in environments where errors can have severe consequences. In the assess ring, it indicates that while it shows promise and is being explored for its potential benefits, widespread adoption may still be forthcoming as the industry evaluates its integration into existing workflows and toolchains.", "link": "../standards/misra-c/", "link_title": "MISRA Guidelines (GU-012)", "x": 204.2, "y": 279.3}, {"id": 12, "title": "CICD", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["automation", "devops", "software-development"], "body": "Continuous Integration and Continuous Deployment (CICD) is a set of practices aimed at improving the software development lifecycle by automating the process of integrating code changes and deploying them to production. It is particularly useful for ensuring that software is consistently built, tested, and deployed, reducing the risk of human error and speeding up the delivery of new features and bug fixes.\n\nIn the \"methods-and-patterns\" quadrant, CICD represents a best practice pattern that integrates seamlessly into modern DevOps strategies. It is categorized under the \"adopt\" ring, indicating that it is a mature and widely accepted practice that organizations should incorporate into their development processes to improve efficiency and collaboration between development and operations teams.\n\nBy automating the build, test, and deployment phases, CICD helps teams to detect issues early, reduce integration problems, and deliver higher quality software. This approach aligns with agile methodologies, enabling iterative development and continuous feedback, crucial for maintaining competitive advantage in fast-paced markets.", "link": "../primers/cicd-pipelines/", "link_title": "CI/CD Pipelines Primer", "x": 475.3, "y": 428.9}, {"id": 13, "title": "CloudEvents", "ring": "assess", "quadrant": "platforms-and-operations", "quadrant_name": "Platforms & Operations", "tags": ["event-driven", "interoperability"], "body": "CloudEvents is a specification for describing event data in a common way, aiming to simplify event-driven systems and improve interoperability between different services and platforms. By standardizing the structure and metadata of events, CloudEvents enables easier integration and processing across diverse environments, reducing the complexity of event-driven architectures.\n\nIn the platforms-and-operations quadrant, CloudEvents is significant as it facilitates seamless communication and coordination between distributed systems, cloud services, and microservices. As organizations increasingly adopt cloud-native architectures and event-driven patterns, assessing CloudEvents can provide insights into its potential to standardize event handling and enhance the scalability and resilience of applications.\n\nCloudEvents is positioned in the \"assess\" ring because it is gaining traction and shows promise, but organizations should evaluate its integration and performance in their specific use cases before broader adoption.", "link": "../primers/cloud/", "link_title": "Cloud & Platforms Primer", "x": 562.6, "y": 237.4}, {"id": 14, "title": "Coverity", "ring": "assess", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["static-analysis", "code-quality", "security"], "body": "Coverity is a static analysis tool used for identifying defects in software codebases. It is particularly useful for detecting a wide range of issues such as security vulnerabilities, resource leaks, and concurrency defects before they manifest in production environments. Coverity is relevant in the \"tools\" quadrant because it provides developers and development teams with a robust mechanism to improve code quality and maintainability through automated code review processes. In the \"assess\" ring, it reflects its growing importance as organizations increasingly prioritize integrating security and quality assurance early in the software development lifecycle, aligning with practices like DevSecOps. As the landscape of software development continues to evolve, tools like Coverity are integral in ensuring software reliability and security compliance.", "link": "../primers/static-code-analysis/", "link_title": "Static Code Analysis Primer", "x": 279.3, "y": 595.8}, {"id": 15, "title": "CQRS", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["architecture", "design-pattern"], "body": "Command Query Responsibility Segregation (CQRS) is a design pattern that separates the read and write operations of a data store into distinct models. This separation is useful in systems that require scalability and have complex business logic, as it allows for optimized query performance and simplifies the management of complex domain logic. CQRS is particularly relevant in the methods-and-patterns quadrant because it provides a strategic approach to handling data operations in software architecture. It is placed in the assess ring, indicating that while it shows promise and can address specific architectural challenges, it should be evaluated carefully for suitability within the context of a project's requirements. CQRS can be especially beneficial when combined with Event Sourcing to provide a complete history of changes to the system’s state.", "link": "../handbook/03-architecture-patterns/", "link_title": "Architecture Handbook: Patterns (GD-002)", "x": 592.9, "y": 474.1}, {"id": 16, "title": "Diátaxis", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["documentation", "knowledge-management"], "body": "Diátaxis is a systematic framework for organizing and writing technical documentation, aimed at improving the clarity and usability of documentation by categorizing content into four distinct types: tutorials, how-to guides, technical references, and explanations. This method helps writers and developers create comprehensive and user-friendly documentation, ensuring that users can find the right information at the right time.\n\nBy adopting Diátaxis, organizations can enhance the effectiveness of their documentation, leading to better user experiences and reduced support costs. Its relevance in the methods-and-patterns quadrant lies in its structured approach to knowledge management, making it an essential practice for teams looking to innovate and optimize their documentation processes. As the industry increasingly recognizes the importance of good documentation, Diátaxis stands out as a best practice, thus earning its place in the adopt ring.", "link": "../guidelines/documentation-as-code/", "link_title": "Docs-as-Code Guide (GU-010)", "x": 442.1, "y": 423.3}, {"id": 17, "title": "Docker", "ring": "adopt", "quadrant": "platforms-and-operations", "quadrant_name": "Platforms & Operations", "tags": ["containerization", "devops", "microservices"], "body": "Docker is a platform that allows developers to automate the deployment of applications inside lightweight, portable containers. These containers include everything needed to run an application, which ensures consistency across different development and production environments. Docker is particularly useful for streamlining development workflows and simplifying operations by providing a consistent environment for running applications.\n\nIn the platforms-and-operations quadrant, Docker plays a crucial role in modern DevOps practices by enabling continuous integration and continuous deployment (CI/CD) pipelines. It facilitates microservices architecture by allowing developers to break down applications into smaller, manageable services that can be developed, tested, and deployed independently.\n\nDocker has reached the adopt ring due to its widespread acceptance and proven benefits in enhancing efficiency, scalability, and reliability within software development processes. Its relevance continues to grow as more organizations embrace cloud-native development and seek to modernize their application delivery processes.", "link": "../handbook/05-cloud-architecture/", "link_title": "Architecture Handbook: Cloud (GD-002)", "x": 423.8, "y": 349.0}, {"id": 18, "title": "Docs as code", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["documentation", "collaboration", "version-control"], "body": "Docs as code is a methodology that applies software development practices to documentation. This approach involves using tools such as version control systems (e.g., Git) to manage and collaborate on documentation in the same way developers work on code. It encourages the use of plain text formats, such as Markdown or reStructuredText, which can be easily tracked, reviewed, and modified.\n\nThis method is particularly useful as it promotes collaboration between developers and technical writers, ensuring documentation is up-to-date and accurate. It also allows for better integration with CI/CD pipelines, enabling automated checks and deployments of documentation alongside the software it describes.\n\nIn the methods-and-patterns quadrant, adopting docs as code represents a shift towards more efficient, scalable, and reliable documentation processes. As organizations increasingly recognize the importance of high-quality documentation, this approach has become a best practice in the industry, fitting well within the \"adopt\" ring.", "link": "../guidelines/documentation-as-code/", "link_title": "Docs-as-Code Guide (GU-010)", "x": 470.5, "y": 439.1}, {"id": 19, "title": "DoD", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["software-development", "agile"], "body": "The Definition of Done (DoD) is a key concept in Agile methodologies that refers to a shared understanding among the team about what it means for a piece of work to be considered complete. It is useful because it ensures that everyone has clarity on the quality criteria and the necessary steps to achieve that quality, which helps in delivering consistent and predictable outcomes. In the methods-and-patterns quadrant, DoD is crucial as it provides a framework to guide the development process, ensuring alignment and reducing ambiguity. By adopting DoD, teams can improve their collaboration, enhance the quality of deliverables, and increase stakeholder satisfaction.", "link": "../templates/definition-of-done/", "link_title": "Definition of Done (DoD) Guide (GU-003)", "x": 453.7, "y": 435.5}, {"id": 20, "title": "Domain-driven design", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["software-architecture", "design-patterns"], "body": "Domain-driven design (DDD) is a strategic approach to software development that emphasizes collaboration between technical and domain experts to create a model that reflects the business domain. It focuses on understanding the core domain, creating a shared language (ubiquitous language), and structuring the codebase around the business concepts to improve alignment between software design and business needs.\n\nDDD is useful because it helps teams produce software that is more maintainable, flexible, and aligned with business goals. It encourages breaking down complex systems into bounded contexts, which can be developed, tested, and deployed independently, fostering agility and scalability.\n\nIn the Tech Radar, DDD is placed in the \"adopt\" ring of the \"methods-and-patterns\" quadrant. This placement reflects its maturity and proven effectiveness in numerous real-world applications. It is widely recognized as a best practice for developing complex systems where understanding and evolving the business domain is crucial. With its focus on collaboration and communication, DDD has become increasingly relevant in today's fast-paced and ever-changing business environments.", "link": "../primers/domain-driven-design/", "link_title": "Domain-Driven Design Primer", "x": 480.8, "y": 453.4}, {"id": 21, "title": "DoR", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["agile", "project-management"], "body": "The Definition of Ready (DoR) is a critical concept in agile project management that ensures a backlog item is prepared for execution by the development team. It sets a checklist of conditions that must be met before work can begin on a particular task, thereby reducing ambiguities and improving the chances of successful delivery. In the context of methods and patterns, DoR plays a significant role in enhancing workflow efficiency and team alignment. By assessing the DoR, teams can ensure that they have a clear understanding of the requirements, acceptance criteria, and necessary resources, ultimately leading to more predictable and manageable development cycles. This makes it an essential practice for teams striving to improve their agile processes and deliver high-quality software consistently.", "link": "../templates/definition-of-ready/", "link_title": "Definition of Ready (DoR) Guide (GU-004)", "x": 597.1, "y": 518.5}, {"id": 22, "title": "DRY (Don't Repeat Yourself)", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["software-design-principle", "code-quality"], "body": "DRY (Don't Repeat Yourself) is a fundamental software design principle aimed at reducing the repetition of code and logic within a system. By emphasizing the elimination of redundancy, DRY encourages developers to create more maintainable, scalable, and efficient codebases. It is particularly useful in preventing the proliferation of bugs, as updates and changes only need to be made in a single location rather than multiple places. This principle is especially relevant in the \"methods-and-patterns\" quadrant, as it pertains to the overall approach to structuring and organizing code. Being in the \"adopt\" ring highlights its established importance and widespread acceptance in modern software development practices. DRY's emphasis on clean and maintainable code aligns with best practices for improving code quality and long-term sustainability of software projects.", "link": "../standards/software-architecture-principles/", "link_title": "Fundamental Software Architecture Principles (GU-019)", "x": 487.5, "y": 441.6}, {"id": 23, "title": "Edge Architectures for IoT", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["edge-computing", "IoT", "distributed-systems"], "body": "Edge Architectures for IoT involve deploying computational resources closer to the data source in IoT ecosystems, rather than relying solely on centralized cloud data centers. This approach aims to reduce latency, improve bandwidth efficiency, and enhance data privacy by processing data locally or at the edge of the network. As IoT devices proliferate, generating vast amounts of data, edge architectures become crucial for real-time analytics and decision-making. By adopting edge architectures, organizations can ensure more responsive and reliable IoT systems, making it a vital method and pattern in the modern technological landscape. The adoption ring signifies its growing importance and maturity in the industry, as businesses increasingly look to optimize their IoT deployments for performance and cost-effectiveness.", "link": "../handbook/06-iot-and-embedded-systems/", "link_title": "Architecture Handbook: IoT & Embedded (GD-002)", "x": 448.3, "y": 442.6}, {"id": 24, "title": "ETSI EN 303 645", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["IoT-security", "cybersecurity-standards"], "body": "ETSI EN 303 645 is a cybersecurity standard developed by the European Telecommunications Standards Institute (ETSI) for consumer Internet of Things (IoT) devices. It establishes a set of baseline requirements to ensure devices are secure by design, addressing key areas such as data protection, software updates, and vulnerability reporting. This standard is useful as it provides manufacturers with a clear framework to mitigate security risks, enhancing consumer trust and protecting user data. In the methods-and-patterns quadrant, ETSI EN 303 645 is particularly relevant as it sets fundamental guidelines for developing secure IoT devices, emphasizing the need for security considerations during the design phase. The adoption of this standard is encouraged due to the increasing prevalence of IoT devices and the associated security challenges, making it crucial for organizations involved in IoT development to prioritize security best practices.", "link": "../handbook/07-security-and-standards/", "link_title": "Architecture Handbook: Security & Standards (GD-002)", "x": 438.4, "y": 429.0}, {"id": 25, "title": "Event-Driven Architecture (EDA)", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["scalability", "real-time-processing"], "body": "Event-Driven Architecture (EDA) is a design paradigm in which decoupled systems communicate through the production and consumption of events. It is particularly useful for building scalable and responsive systems, as it allows for real-time data processing and asynchronous communication. EDA is increasingly relevant in the methods-and-patterns quadrant due to its ability to handle high volumes of data and its fit with modern distributed systems. By adopting EDA, organizations can create systems that are more agile and responsive to changes, facilitating innovation and improving user experiences. Its relevance in the \"adopt\" ring suggests that it is a well-established and effective approach that is recommended for widespread use across various industries.", "link": "../handbook/03-architecture-patterns/", "link_title": "Architecture Handbook: Patterns (GD-002)", "x": 441.9, "y": 448.9}, {"id": 26, "title": "Event Driven", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["asynchronous", "scalability", "reactive-programming"], "body": "Event Driven architecture is a design paradigm that emphasizes the production, detection, consumption, and reaction to events. An event can be defined as a significant change in the state of a system, and this approach is particularly useful for building scalable and decoupled systems. By adopting an Event Driven approach, systems can achieve greater responsiveness and flexibility, as components can operate independently and asynchronously, reacting to changes as they occur.\n\nThis method is especially relevant in today's microservices and cloud-native environments, where systems benefit from being loosely coupled and highly responsive. In the methods-and-patterns quadrant, Event Driven is a critical pattern that supports modern software architecture needs, enabling systems to handle complex workflows and data processing tasks efficiently. Its placement in the \"adopt\" ring indicates that it is a mature approach that organizations should incorporate into their architecture to enhance agility and scalability.", "link": "../primers/event-driven-architecture/", "link_title": "Event-Driven Architecture Primer", "x": 464.4, "y": 448.5}, {"id": 27, "title": "Event Sourcing", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["data-management", "system-architecture"], "body": "Event Sourcing is a method of capturing all changes to the state of an application as a sequence of events. Instead of storing just the current state, every change is recorded as an immutable event, which can be replayed to reconstruct past states or derive new information. This approach is useful for maintaining a clear audit trail, enabling system scalability, and supporting complex business logic by reconstructing states at any point in time.\n\nIn the \"methods-and-patterns\" quadrant, Event Sourcing offers a strategic approach to handling state management and data consistency across distributed systems. It is especially relevant in the \"assess\" ring as organizations explore its potential benefits and challenges before full adoption. Its application can lead to improved traceability, easier debugging, and better alignment with domain-driven design principles. However, like any architectural choice, it comes with trade-offs, such as increased complexity in data management and potential challenges in system performance.", "link": "../primers/event-driven-architecture/", "link_title": "Event-Driven Architecture Primer", "x": 636.5, "y": 490.8}, {"id": 28, "title": "Event storming", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["collaborative-design", "domain-driven-design"], "body": "Event storming is a workshop-based method used to quickly explore complex business domains by focusing on domain events. It is particularly useful for building a shared understanding among cross-functional teams, including developers, domain experts, and stakeholders. By identifying key events that occur within a system, teams can collaboratively map out processes and uncover insights that lead to better software design and implementation.\n\nEvent storming is relevant in the \"methods-and-patterns\" quadrant as it provides a structured approach to domain-driven design (DDD), allowing teams to visually represent workflows and interactions in a manner that's easy to grasp. Positioned in the \"adopt\" ring, event storming has proven its effectiveness in fostering communication and aligning technical solutions with business goals. Its ability to simplify complex systems and enhance team collaboration makes it a valuable technique for organizations aiming to improve their design and development processes.", "link": "../primers/event-storming/", "link_title": "Event Storming Primer", "x": 434.0, "y": 434.0}, {"id": 29, "title": "Event Streaming", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["real-time-data", "scalability", "distributed-systems"], "body": "Event Streaming is a data processing paradigm that treats data as a continuous stream of events, allowing for real-time data processing and analysis. This approach is particularly useful for applications that require immediate insights from data, such as fraud detection, real-time analytics, and monitoring systems. By adopting event streaming, organizations can build scalable and responsive systems that react to data changes in real-time, rather than processing data in batches.\n\nIn the methods-and-patterns quadrant, event streaming represents a shift from traditional data processing methods, enabling more dynamic and responsive architectures. Its adoption is increasingly relevant as businesses demand quicker and more efficient ways to handle large volumes of data. This method not only enhances scalability and performance but also supports the growing need for distributed systems that can manage data across various sources. As such, event streaming is a crucial tool in the modern software architecture toolkit, facilitating the creation of robust, high-performance applications.", "link": "../primers/kafka-event-streaming/", "link_title": "Kafka Event Streaming Primer", "x": 472.6, "y": 464.1}, {"id": 30, "title": "FreeRTOS", "ring": "adopt", "quadrant": "platforms-and-operations", "quadrant_name": "Platforms & Operations", "tags": ["real-time-operating-system", "embedded-systems", "IoT"], "body": "FreeRTOS is a real-time operating system kernel designed for embedded devices and microcontrollers. It provides a lightweight and robust platform that supports a wide range of hardware architectures, making it ideal for resource-constrained environments common in IoT (Internet of Things) applications. FreeRTOS enables developers to create reliable, real-time applications with features like task management, inter-task communication, and memory management, all while maintaining a small footprint.\n\nThe decision to place FreeRTOS in the \"adopt\" ring reflects its widespread acceptance and proven stability in the industry. It is a mature and well-supported option that has been adopted by numerous organizations worldwide for both commercial and open-source projects. In the \"platforms-and-operations\" quadrant, FreeRTOS is highly relevant due to its role in operating system management for embedded systems, providing essential operational capabilities in real-time environments. Its versatility and ease of integration make it a valuable asset for projects aiming to leverage the growing landscape of connected devices and smart applications.", "link": "../primers/rtos-and-freertos/", "link_title": "FreeRTOS Basics Primer", "x": 455.0, "y": 330.4}, {"id": 31, "title": "gcc", "ring": "adopt", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["compiler", "open-source", "C", "C++"], "body": "The GNU Compiler Collection (gcc) is a comprehensive and widely-used set of compilers for various programming languages, most notably C, C++, and Fortran. As an open-source project under the GNU umbrella, gcc is highly valued for its robustness, performance, and cross-platform capabilities. It serves as a critical tool in software development, enabling the translation of high-level code into executable machine code across various architectures. In the tools quadrant and adopt ring, gcc is an essential part of the development toolchain for many organizations and projects due to its maturity, extensive community support, and continuous updates. Its relevance spans from education to enterprise applications, making it a staple in both learning environments and professional software engineering practices.", "link": "../primers/static-code-analysis/", "link_title": "Static Code Analysis Primer", "x": 347.5, "y": 420.2}, {"id": 32, "title": "Go (golang)", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["concurrency", "performance", "simplicity"], "body": "Go, also known as golang, is a statically typed, compiled programming language designed by Google. It is renowned for its simplicity, efficiency, and strong support for concurrent programming, making it a popular choice for developing scalable and high-performance applications. Go's syntax is clean and concise, which reduces the complexity associated with managing large codebases. Its garbage collection, strict dependency management, and built-in testing capabilities enhance developer productivity and code reliability.\n\nIn the languages-and-frameworks quadrant, Go sits in the adopt ring because it has proven itself in production environments across various industries. Its robust standard library and vibrant ecosystem of third-party packages make it an excellent choice for building web servers, networking tools, and cloud services. The language's ability to compile to a single binary without dependencies further simplifies deployment and distribution.\n\nGo's concurrency model, based on goroutines and channels, allows developers to efficiently utilize multicore processors, which is crucial for modern applications demanding high performance. This feature, combined with its simplicity and speed, underscores its relevance and adoption in the software development landscape.", "link": "../primers/programming-and-tools/", "link_title": "Programming Tools Primer", "x": 359.4, "y": 369.4}, {"id": 33, "title": "Google Cloud Platform", "ring": "adopt", "quadrant": "platforms-and-operations", "quadrant_name": "Platforms & Operations", "tags": ["cloud"], "body": "GCP provides scalable cloud solutions for modern architectures.", "link": "../handbook/05-cloud-architecture/", "link_title": "Architecture Handbook: Cloud (GD-002)", "x": 439.8, "y": 360.2}, {"id": 34, "title": "GraphQL", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["api-design", "data-fetching", "flexibility"], "body": "GraphQL is a query language for your APIs and a runtime for executing those queries by using a type system you define for your data. It provides an alternative to REST, enabling clients to request exactly the data they need, in the shape they need it. This approach reduces over-fetching and under-fetching of data, a common problem with traditional REST APIs.\n\nIn the \"languages-and-frameworks\" quadrant, GraphQL stands out due to its ability to streamline and optimize data interactions between clients and servers, making it extremely useful for applications with complex data requirements. Its flexibility and efficiency have led to its adoption by many organizations seeking to improve their API performance and developer experience.\n\nPlaced in the \"adopt\" ring, GraphQL has proven its reliability and effectiveness, with robust community support and widespread use in production environments. It has become a go-to choice for developers looking to implement efficient, flexible, and scalable API solutions.", "link": "../standards/api-design/", "link_title": "API Design Standards (GU-020)", "x": 350.6, "y": 347.0}, {"id": 35, "title": "gRPC", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["remote-procedure-call", "microservices"], "body": "gRPC is a high-performance, open-source universal remote procedure call (RPC) framework developed by Google. It uses HTTP/2 for transport, Protocol Buffers as the interface description language, and provides features such as authentication, load balancing, and more. gRPC is particularly useful in microservices architectures, where it enables efficient and language-agnostic communication between services. Its ability to support multiple languages makes it a versatile choice for distributed systems.\n\nIn the \"methods-and-patterns\" quadrant, gRPC stands out due to its strong support for service-to-service communication, making it a preferred pattern for modern cloud-native applications. By placing it in the \"adopt\" ring, we're indicating that gRPC is a mature and stable technology that organizations can confidently implement to improve the performance and scalability of their service-oriented architectures.", "link": "../standards/api-design/", "link_title": "API Design Standards (GU-020)", "x": 410.1, "y": 463.6}, {"id": 36, "title": "ISO 30141", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["IoT", "architecture", "standards"], "body": "ISO 30141 is an international standard that provides a reference architecture for the Internet of Things (IoT). It offers a framework to design IoT systems with a focus on interoperability, connectivity, and security. This standard is useful because it establishes a common understanding and approach to developing IoT solutions, which is crucial given the increasing complexity and scale of IoT deployments.\n\nThe relevance of ISO 30141 in the methods-and-patterns quadrant lies in its ability to guide architects and developers in designing robust IoT systems. By adopting this reference architecture, organizations can ensure that their IoT solutions are built on a foundation of best practices, promoting system reliability and scalability. In the assess ring, ISO 30141 is evaluated for its potential to streamline IoT development processes and its applicability to various industry sectors.", "link": "../guides/scaling-architecture/01-advice-process/", "link_title": "Scaling Architecture (GD-003)", "x": 565.1, "y": 524.4}, {"id": 37, "title": "JSON", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["data-interchange", "lightweight-format"], "body": "JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is language-independent but uses conventions that are familiar to programmers of the C family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. JSON is widely adopted due to its simplicity and flexibility in representing data structures, making it a staple in web development and various APIs.\n\nIn the context of languages and frameworks, JSON serves as a universal medium for data interchange between systems, providing a straightforward way to serialize and deserialize data. Its adoption is crucial for developing modern web applications, enabling seamless communication between client-side and server-side components. JSON's relevance in this quadrant and its placement in the \"adopt\" ring highlight its established role as a foundational technology that continues to be integral in software architecture and development practices.", "link": "../primers/infrastructure-as-code/", "link_title": "Infrastructure as Code Primer", "x": 324.8, "y": 343.3}, {"id": 38, "title": "Kanban", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["agile", "project-management", "workflow-optimization"], "body": "Kanban is a popular workflow management method designed to help visualize work, maximize efficiency, and improve continuously. It is widely adopted in various industries, especially in software development, as part of Agile methodologies. Kanban uses visual cues—typically through a board divided into columns that represent different stages of a process—to track work items as they progress. This visualization allows teams to manage work by balancing demands with available capacity and identifying bottlenecks in the workflow.\n\nThe reason Kanban is categorized under the \"adopt\" ring in the \"methods-and-patterns\" quadrant is due to its proven effectiveness in optimizing workflow and enhancing team collaboration. It is not only useful for managing tasks in software development but also adaptable to other types of project management scenarios. By adopting Kanban, organizations can achieve greater flexibility and improved productivity, making it a significant method for modern project management practices.", "link": "../standards/api-design/", "link_title": "API Design Standards (GU-020)", "x": 463.0, "y": 473.6}, {"id": 39, "title": "KISS (Keep It Simple, Stupid)", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["simplicity", "efficiency", "design-principle"], "body": "KISS, an acronym for \"Keep It Simple, Stupid,\" is a design principle that emphasizes simplicity in design and implementation. It advocates for avoiding unnecessary complexity, suggesting that systems function best if they are kept simple rather than made complicated. This principle is applicable across various fields, including software development, engineering, and user interface design.\n\nIn the context of software architecture, KISS is invaluable as it encourages developers to design solutions that are easy to understand, maintain, and scale. This simplicity can lead to increased productivity, fewer bugs, and easier onboarding for new team members. By adopting KISS in the \"methods-and-patterns\" quadrant, organizations can streamline their processes and enhance the overall quality of their software products. The principle's relevance is underscored by its widespread acceptance and proven effectiveness in improving both the development lifecycle and user experience.", "link": "../primers/kafka-event-streaming/", "link_title": "Kafka Event Streaming Primer", "x": 457.0, "y": 457.0}, {"id": 40, "title": "Layered Architecture", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["architecture-pattern", "software-design"], "body": "Layered Architecture is a widely used architectural pattern in software design that organizes the system into a series of layers, each with a distinct responsibility. This pattern typically includes layers such as presentation, business logic, and data access. The primary advantage of Layered Architecture is its ability to separate concerns, making systems more modular, maintainable, and scalable. Each layer can be developed, tested, and maintained independently, allowing teams to work on different parts of the system simultaneously without significant interference.\n\nIn the methods-and-patterns quadrant, Layered Architecture is crucial as it provides a foundational structure for building robust and organized solutions. Its adoption across various industries signifies its reliability and effectiveness in addressing complex software requirements. This architecture is especially beneficial for enterprise applications where clarity and separation of concerns are paramount. By adopting Layered Architecture, organizations can ensure that their applications are easier to manage and evolve over time, thus aligning with modern software development practices.", "link": "../handbook/05-cloud-architecture/", "link_title": "Architecture Handbook: Cloud (GD-002)", "x": 429.0, "y": 438.4}, {"id": 41, "title": "Lightweight Architecture Evaluations", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["architecture", "evaluation", "agile"], "body": "Lightweight Architecture Evaluations refer to a streamlined approach to assessing and reviewing software architecture. Unlike traditional, exhaustive architectural reviews, this method focuses on agility, enabling teams to quickly evaluate architectural decisions without extensive documentation or formal processes. This approach is especially useful in agile and fast-paced development environments, where time and resources for detailed analysis may be limited. In the \"methods-and-patterns\" quadrant, Lightweight Architecture Evaluations help teams stay responsive to change and ensure that architectural decisions align with evolving project needs. The \"adopt\" ring suggests that this practice has proven benefits and should be considered a standard approach for teams seeking to maintain agility while ensuring sound architectural principles.", "link": "../primers/lightweight-architecture-evaluations/", "link_title": "Architecture Evaluations Primer", "x": 434.6, "y": 454.3}, {"id": 42, "title": "Markdown", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["documentation", "markup-language"], "body": "Markdown is a lightweight markup language that allows users to format plain text using a simple syntax. It is widely used for creating formatted text using a plain text editor, making it a popular choice for documentation, readme files, blog posts, and more. Its simplicity and ease of use make it accessible to users who may not have extensive technical knowledge, while still being powerful enough for more complex formatting needs.\n\nIn the context of languages and frameworks, Markdown stands out as a versatile tool that integrates seamlessly with various platforms and services, including GitHub, where it is commonly used for project documentation. The language's ability to convert plain text into HTML makes it incredibly useful for web content creation and management.\n\nMarkdown's widespread adoption and support across numerous platforms underscore its importance in modern software development environments. Its role in improving documentation quality and accessibility aligns with current best practices, justifying its placement in the 'adopt' ring of the Tech Radar.", "link": "../primers/embedded-systems-design/", "link_title": "Embedded Systems Design Primer", "x": 369.4, "y": 359.4}, {"id": 43, "title": "Mermaid", "ring": "adopt", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["diagramming", "visualization", "documentation"], "body": "Mermaid is a JavaScript-based diagramming and charting tool that enables developers and content creators to create complex diagrams from simple text definitions. It is particularly useful for generating flowcharts, sequence diagrams, Gantt charts, and more, using a straightforward syntax that integrates seamlessly into various documentation systems, such as Markdown and static site generators like Jekyll and Docusaurus.\n\nMermaid has gained traction due to its ease of use, which allows users to focus on content rather than the intricacies of drawing tools. It is relevant in the tools quadrant as it enhances documentation workflows, offering a programmatic method to include visual content directly in textual documentation. In the adopt ring, Mermaid is recognized for its maturity and broad adoption, indicating it is a reliable choice for organizations looking to improve their documentation capabilities. Its integration with platforms like GitHub and GitLab further underscores its utility in collaborative environments, making it a natural fit for teams aiming to enhance communication and understanding through visual aids.", "link": "../handbook/05-cloud-architecture/", "link_title": "Architecture Handbook: Observability (GD-002)", "x": 379.8, "y": 452.5}, {"id": 44, "title": "Mermaid Diagrams", "ring": "trial", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["visualization", "documentation"], "body": "Mermaid is a JavaScript-based diagramming and charting tool that allows for dynamic, code-based visualizations. It's particularly useful for architecture diagrams, flowcharts, and Gantt charts in technical documentation. Mermaid syntax integrates seamlessly into Markdown files for inline visualization.\n\n### Example Mermaid Diagram\n\nBelow is an example of a simple Mermaid flowchart:\n\n```mermaid\nsequenceDiagram\n    Alice->>+John: Hello John, how are you?\n    Alice->>+John: John, can you hear me?\n    John-->>-Alice: Hi Alice, I can hear you!\n    John-->>-Alice: I feel great!\n```\n\nwill produce\n\n![Mermaid Image](/images/mermaid.png)", "link": "../standards/lwm2m-objects/", "link_title": "LwM2M Objects Specification (GU-008)", "x": 292.2, "y": 507.8}, {"id": 45, "title": "Microservices", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["architecture", "scalability", "resilience"], "body": "Microservices is an architectural style that structures an application as a collection of loosely coupled services, each of which implements a business capability. This approach enhances flexibility and scalability, allowing for the independent deployment of services, which can be developed, tested, and deployed independently by different teams.\n\nThe microservices architecture is particularly useful in large, complex applications where the agility and speed of deployment are crucial. It allows organizations to scale specific components of an application without impacting the entire system, improving resource utilization and resilience.\n\nIn the methods-and-patterns quadrant of the Tech Radar, microservices are classified in the adopt ring, indicating that they are a well-established practice with proven benefits. Many organizations have successfully utilized microservices to achieve greater modularity, fault isolation, and faster time-to-market, making it a crucial pattern in modern software development.", "link": "../primers/terminal-modernisation/", "link_title": "Terminal Modernisation Primer", "x": 452.1, "y": 481.7}, {"id": 46, "title": "MISRA C++", "ring": "assess", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["safety-critical", "coding-guidelines"], "body": "MISRA C++ is a set of guidelines designed to facilitate the safe and secure use of the C++ programming language in critical systems. Originally developed for the automotive industry, it has been widely adopted in other sectors, such as aerospace and industrial automation, where software reliability is paramount. MISRA C++ provides a collection of best practices that help developers avoid common pitfalls and undefined behaviors in C++ programming, which are crucial in environments where software failure can have severe consequences.\n\nThe \"assess\" ring indicates that organizations should evaluate the potential benefits and challenges of adopting MISRA C++ guidelines in their projects. Its relevance in the \"languages-and-frameworks\" quadrant underscores its role in shaping how C++ is used in developing robust and dependable software systems. Given the increasing reliance on software in safety-critical applications, MISRA C++ is becoming increasingly relevant as organizations strive to enhance their software quality and reliability.", "link": "../primers/modular-monolith-vs-microservices/", "link_title": "Modular Monolith vs Microservices Primer", "x": 279.3, "y": 204.2}, {"id": 47, "title": "MISRA C", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["safety-critical", "coding-standard"], "body": "MISRA C is a set of software development guidelines for the C programming language, developed by the Motor Industry Software Reliability Association (MISRA). It is widely adopted in industries where safety and reliability are paramount, such as automotive, aerospace, and medical devices. The guidelines aim to facilitate code safety, portability, and reliability in the embedded systems environment by imposing restrictions on the use of certain C language features that can lead to unsafe or unpredictable behavior.\n\nMISRA C is particularly relevant in the \"methods-and-patterns\" quadrant because it provides a structured approach to writing robust and maintainable C code. The guidelines are not just applicable to critical systems but are also useful for any software development process that prioritizes code quality and long-term maintainability.\n\nThe \"adopt\" ring reflects its mature status and widespread acceptance across industries that require stringent compliance with safety standards. By adhering to MISRA C, organizations can ensure that their software meets rigorous safety requirements, reducing the risk of defects and enhancing overall system reliability.", "link": "../guides/cybersecurity/", "link_title": "Connected Systems Cybersecurity (GD-004)", "x": 448.5, "y": 464.4}, {"id": 48, "title": "Modular Monolith", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["architecture", "software-design", "scalability"], "body": "The Modular Monolith is a software architecture pattern that emphasizes structuring a monolithic application into distinct modules, each encapsulating a specific domain or functionality. Unlike traditional monoliths, where all components are intertwined, a Modular Monolith promotes a high degree of modularity within a single deployable unit. This approach allows for clearer boundaries, easier maintenance, and the possibility of gradually transitioning to a microservices architecture if needed.\n\nAdopting a Modular Monolith can be highly advantageous for organizations that require a balance between the simplicity of monolithic applications and the modularity of microservices. It is particularly useful in scenarios where the complexity of microservices is not justified or the team is not yet ready to manage the operational overhead associated with distributed systems.\n\nIn the methods-and-patterns quadrant, the Modular Monolith is a valuable architectural strategy, offering scalability and flexibility without the immediate need to fully commit to a microservices approach. As such, it has been placed in the adopt ring, indicating that it is a recommended practice for teams looking to efficiently manage their software architecture while maintaining the option for future architectural evolution.", "link": "../standards/misra-c/", "link_title": "MISRA Guidelines (GU-012)", "x": 423.3, "y": 442.1}, {"id": 49, "title": "MQTT", "ring": "adopt", "quadrant": "platforms-and-operations", "quadrant_name": "Platforms & Operations", "tags": ["IoT", "messaging-protocol"], "body": "MQTT (Message Queuing Telemetry Transport) is a lightweight, publish-subscribe network protocol commonly used for machine-to-machine (M2M) communication and is a cornerstone in the Internet of Things (IoT) ecosystems. It is designed for connections with remote locations where a small code footprint is required, or the network bandwidth is limited. MQTT is particularly useful for its simplicity and efficiency in constrained environments, making it ideal for IoT applications where devices need to communicate reliably over potentially unreliable networks.\n\nMQTT's relevance in the platforms-and-operations quadrant stems from its role in enabling efficient, real-time communication across distributed systems. Its ability to handle thousands of lightweight clients and its minimal use of bandwidth make it an attractive choice for operations that require scalable and efficient messaging solutions. Given its widespread adoption and proven reliability, MQTT is placed in the \"adopt\" ring, signifying its maturity and readiness for use in production environments across various industries.", "link": "../primers/mqtt/", "link_title": "MQTT Protocol Primer", "x": 475.5, "y": 353.4}, {"id": 50, "title": "oauth2", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["authentication", "security"], "body": "OAuth2 is an open standard for access delegation commonly used to grant websites or applications limited access to user information on another website without exposing the user's credentials. It is particularly significant in the realm of authentication and authorization protocols, making it a pivotal method in securing web applications and APIs. By enabling secure token-based authentication, OAuth2 allows developers to build robust security layers, enhancing user privacy and data protection.\n\nIts adoption in the \"methods-and-patterns\" quadrant reflects its widespread usage and maturity as a standard practice in software development. OAuth2 provides a flexible framework that supports various authentication flows, catering to both web and mobile applications, which is why it is a critical component in modern application architecture. The adoption ring indicates that it's a well-established practice recommended for use in most relevant projects, ensuring secure and scalable authentication strategies.", "link": "../handbook/06-iot-and-embedded-systems/", "link_title": "Architecture Handbook: IoT & Embedded (GD-002)", "x": 418.1, "y": 478.6}, {"id": 51, "title": "OpenAPI", "ring": "adopt", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["API-design", "documentation"], "body": "OpenAPI is a specification for building APIs that provides a standard, language-agnostic interface describing RESTful APIs. It's widely adopted in the industry due to its ability to streamline API development processes. By using OpenAPI, developers can automate the generation of API documentation, client libraries, and server stubs, which reduces the likelihood of errors and accelerates development timelines.\n\nWithin the \"tools\" quadrant, OpenAPI is especially relevant as it enhances collaboration across teams by providing a clear, shared understanding of API functionalities. Being in the \"adopt\" ring signifies that OpenAPI is a mature, stable solution that offers significant value to organizations looking to optimize their API development and management practices. The specification's ability to improve interoperability and facilitate the integration of various systems makes it a crucial asset in modern software architecture.", "link": "../primers/oauth-and-oidc/", "link_title": "OAuth 2.0 & OIDC Primer", "x": 354.3, "y": 476.1}, {"id": 52, "title": "OWASP", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["security", "best-practices"], "body": "The Open Web Application Security Project (OWASP) is an essential resource in the field of web application security. It is a non-profit foundation that works to improve the security of software through community-driven open-source software projects, hundreds of local chapters worldwide, tens of thousands of members, and leading educational and training conferences. OWASP is renowned for its comprehensive resources such as the OWASP Top Ten, a regularly updated list of the most critical security risks to web applications.\n\nAdopting OWASP's methodologies and guidelines is crucial for organizations aiming to enhance their security posture. It provides developers and security professionals with the tools and knowledge needed to identify and mitigate vulnerabilities effectively. The emphasis on practical, up-to-date best practices makes OWASP highly relevant in the \"methods-and-patterns\" quadrant, and its widespread acceptance and utility across industries justify its placement in the \"adopt\" ring. By integrating OWASP principles, organizations can ensure that they are implementing robust security measures to protect their web applications against emerging threats.", "link": "../handbook/05-cloud-architecture/", "link_title": "Architecture Handbook: Observability (GD-002)", "x": 426.8, "y": 458.6}, {"id": 53, "title": "PEP 8", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["coding-standards", "python"], "body": "PEP 8 is the style guide for Python code, providing conventions on how to format Python code for maximum readability. It is widely adopted in the Python community, ensuring consistency across diverse codebases. PEP 8 covers various aspects, including indentation, naming conventions, and best practices for writing clear and maintainable code.\n\nIts relevance in the \"methods-and-patterns\" quadrant stems from its role in defining coding patterns that improve code quality and collaboration. Being in the \"adopt\" ring indicates that PEP 8 is a mature and essential standard that should be fully integrated into Python development practices. Adhering to PEP 8 not only enhances readability but also facilitates better teamwork and reduces the likelihood of errors.", "link": "../primers/owasp-top-10/", "link_title": "OWASP Top 10 Primer", "x": 439.1, "y": 470.5}, {"id": 54, "title": "PlantUML", "ring": "adopt", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["diagramming", "visualization", "documentation"], "body": "PlantUML is an open-source tool that allows users to create UML diagrams from a plain text language. It is widely appreciated for its simplicity and the ease with which complex diagrams can be generated without needing to use graphical editing tools. PlantUML supports a variety of UML diagrams, including sequence diagrams, use case diagrams, class diagrams, and more, making it a versatile choice for software architects and developers.\n\nThe tool is particularly beneficial in agile environments where rapid iteration and clear communication are key. By using text files to describe diagrams, PlantUML integrates seamlessly with version control systems, allowing teams to track changes and collaborate efficiently. Its ability to be embedded in wikis and integrated with popular tools like Visual Studio Code enhances its utility in maintaining up-to-date documentation.\n\nIn the context of 'tools', PlantUML is placed in the 'adopt' ring because it represents a mature technology that has been proven effective in production environments. Its ability to streamline the documentation process and improve collaboration makes it a valuable asset for teams committed to maintaining clear and accessible software documentation.", "link": "../standards/c-coding-standard/", "link_title": "C Coding Standards (GU-009)", "x": 366.1, "y": 444.9}, {"id": 55, "title": "protobuf", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["serialization", "cross-platform", "performance"], "body": "Protocol Buffers (protobuf) is a language-neutral, platform-neutral, extensible mechanism for serializing structured data. Developed by Google, it is widely adopted for its efficiency in data serialization, especially in scenarios where performance and portability are crucial. Protobuf offers a compact binary format, which reduces the size of the payload and improves the speed of data transmission compared to traditional text-based formats like JSON or XML.\n\nIn the context of the Tech Radar, protobuf is placed in the \"adopt\" ring under the \"languages-and-frameworks\" quadrant. This positioning reflects its maturity and widespread use in production environments where developers need a reliable, performant solution for data interchange between microservices, APIs, and other cross-platform systems. It provides strong typing, backward compatibility, and is supported by numerous programming languages, making it a versatile tool in modern software development.", "link": "../primers/plantuml-and-mermaid/", "link_title": "PlantUML & Mermaid Primer", "x": 386.2, "y": 328.8}, {"id": 56, "title": "Python", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["programming-language", "high-level", "versatile"], "body": "Python is a high-level, interpreted programming language known for its simplicity and readability, making it an excellent choice for beginners and experienced developers alike. Its extensive standard library and vibrant ecosystem of third-party packages enable rapid development in various domains, including web development, data analysis, artificial intelligence, and scientific computing.\n\nPython's versatility and ease of use have made it a staple in software development, data science, and academic research. Its community-driven nature ensures continuous improvement and innovation, helping it remain relevant in the fast-evolving tech landscape.\n\nIn the context of languages and frameworks, Python's wide adoption across multiple industries and its role as a foundational tool in emerging technologies like machine learning and data analytics justify its placement in the 'adopt' ring. Its impact on productivity and its role in fostering an inclusive programming environment further solidify its standing as a must-have language for modern software development.", "link": "../handbook/05-cloud-architecture/", "link_title": "Architecture Handbook: Observability (GD-002)", "x": 367.1, "y": 335.4}, {"id": 57, "title": "REST", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["web-architecture", "api-design"], "body": "REST (Representational State Transfer) is an architectural style that is widely used for designing networked applications. It leverages standard HTTP methods, such as GET, POST, PUT, and DELETE, to facilitate communication between clients and servers. RESTful services are stateless and typically return data in formats like JSON or XML, making them highly interoperable and scalable.\n\nREST is a crucial pattern in the methods-and-patterns quadrant due to its simplicity and effectiveness in building web APIs. It enables developers to create efficient, reliable, and easy-to-use interfaces that are integral to modern web services. Its adoption is widespread, thanks to its clear conventions and the ease with which it integrates into existing web technologies, making it a cornerstone of contemporary web architecture.", "link": "../guidelines/pull-requests-and-review/", "link_title": "Pull Request Standards (GU-015)", "x": 440.3, "y": 488.1}, {"id": 58, "title": "RFC9457", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["networking", "security", "internet-standards"], "body": "RFC9457 is a significant document in the realm of Internet standards, focusing on improving security protocols within networking systems. It provides a comprehensive framework for enhancing secure communications across different platforms and operations. RFC9457 is essential for developers and network architects who need to ensure their systems are compliant with modern security standards, particularly in an era where cyber threats are increasingly sophisticated.\n\nThis document is placed in the \"assess\" ring because it is relatively new and requires thorough evaluation by organizations to determine its applicability and potential benefits. The \"methods-and-patterns\" quadrant is appropriate as RFC9457 outlines systematic approaches to implementing enhanced security protocols. Its relevance is especially critical for teams tasked with safeguarding data transmission over the internet, making it a valuable resource for organizations aiming to advance their security measures.", "link": "../primers/python-for-automation/", "link_title": "Python for Automation Primer", "x": 556.9, "y": 568.2}, {"id": 59, "title": "rRPC", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["remote-procedure-call", "microservices"], "body": "rRPC, or Reactive Remote Procedure Call, is an emerging method that enhances the traditional RPC model by incorporating reactive programming principles. This approach is particularly useful in systems where responsiveness and scalability are critical, such as microservices architectures. By leveraging a non-blocking, event-driven paradigm, rRPC enables more efficient use of system resources and improves the overall performance of distributed applications.\n\nThe \"assess\" ring indicates that rRPC is a promising technology worth exploring, but it may still be maturing or not yet widely adopted. It belongs in the \"methods-and-patterns\" quadrant because it represents an innovative approach to designing communication patterns in software architecture. As organizations increasingly adopt microservices for their scalability and flexibility, exploring advanced techniques like rRPC can provide significant benefits in terms of system efficiency and responsiveness.", "link": "../standards/api-design/", "link_title": "API Design Standards (GU-020)", "x": 443.9, "y": 625.8}, {"id": 60, "title": "Rust", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["systems-programming", "memory-safety", "concurrency"], "body": "Rust is a systems programming language that aims to provide memory safety without sacrificing performance. It is designed to compete with traditional languages like C and C++ by offering powerful abstractions while ensuring safety through its unique ownership model. Rust is particularly useful in contexts requiring high performance and safety, such as embedded systems, operating systems, and game engines. Its rich type system and emphasis on concurrency make it an excellent choice for developing robust and efficient applications.\n\nRust's importance in the languages-and-frameworks quadrant is underscored by its rapidly growing ecosystem and adoption by major tech companies. The language's ability to prevent common programming errors such as null pointer dereferencing, buffer overflows, and data races makes it a compelling option for developers looking to build reliable software. Given its strengths and increasing popularity, Rust is positioned in the \"adopt\" ring, indicating that it is mature and ready for widespread use in production environments.", "link": "../primers/rust-for-systems/", "link_title": "Rust for Systems Primer", "x": 343.3, "y": 324.8}, {"id": 61, "title": "Scrum", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["agile", "project-management", "team-collaboration"], "body": "Scrum is an agile framework for managing complex projects, primarily focused on software development. It facilitates a flexible, iterative approach where work is broken down into sprints, typically lasting two to four weeks. Scrum emphasizes collaboration, accountability, and continuous improvement, making it an essential tool for teams aiming to deliver high-quality software efficiently. The framework includes defined roles (such as Scrum Master and Product Owner), events (such as daily stand-ups and sprint reviews), and artifacts (like product backlogs) to ensure transparency and enhance productivity.\n\nIn the context of the methods-and-patterns quadrant, Scrum is highly relevant due to its structured yet adaptable approach to project management. It is positioned in the adopt ring because it has proven to be highly effective across various industries and is widely recognized as a best practice for agile teams. By adopting Scrum, organizations can improve their responsiveness to change, foster greater team collaboration, and ultimately deliver more value to their customers.", "link": "../primers/secure-coding-practices/", "link_title": "Secure Coding Practices Primer", "x": 417.2, "y": 444.9}, {"id": 62, "title": "SEI ATAM", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["architecture-evaluation", "software-quality"], "body": "The Software Engineering Institute's Architecture Tradeoff Analysis Method (SEI ATAM) is a systematic approach used for evaluating software architectures. It is particularly useful in identifying architectural risks early in the development process and provides a framework for understanding how well an architecture meets its quality attribute requirements, such as performance, modifiability, and security.\n\nATAM involves stakeholders in a series of structured workshops to capture various perspectives, which helps in uncovering potential trade-offs and critical issues. By focusing on quality attributes and their interactions, it facilitates informed decision-making about architectural strategies.\n\nIn the methods-and-patterns quadrant, ATAM stands out as a critical tool for organizations looking to enhance their architecture assessment processes. Positioned in the assess ring, it is recommended for teams wanting to evaluate the robustness and risk factors of their architectural choices, especially before committing substantial resources to full-scale development. This makes it an essential practice for organizations aiming to improve the quality and effectiveness of their software systems.", "link": "../guidelines/version-control-and-versioning/", "link_title": "Conventional Commits (GU-014)", "x": 602.3, "y": 552.5}, {"id": 63, "title": "SEI CBAM", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["architecture-evaluation", "cost-benefit-analysis"], "body": "The SEI Cost Benefit Analysis Method (CBAM) is a structured approach designed to help software architects and decision-makers evaluate the trade-offs among various architectural decisions. By integrating economic considerations with architectural needs, CBAM allows teams to assess the potential costs and benefits associated with different design options. This method is especially relevant in the methods-and-patterns quadrant as it provides a systematic approach to evaluating and justifying architectural choices, ensuring that they align with business goals and constraints.\n\nIn the assess ring, SEI CBAM is valuable for organizations seeking to incorporate more quantitative approaches in their decision-making processes. It is particularly useful in scenarios where multiple stakeholders are involved, and architectural decisions have a significant impact on business value. By evaluating potential architectural investments and their anticipated return, CBAM supports informed decision-making and prioritization, making it an essential tool for organizations aiming to optimize their software architecture in alignment with strategic objectives.", "link": "../handbook/05-cloud-architecture/", "link_title": "Architecture Handbook: Cloud (GD-002)", "x": 524.4, "y": 565.1}, {"id": 64, "title": "Serverless", "ring": "adopt", "quadrant": "platforms-and-operations", "quadrant_name": "Platforms & Operations", "tags": ["cloud-computing", "scalability", "cost-efficiency"], "body": "Serverless computing is a cloud-computing execution model where the cloud provider dynamically manages the allocation and provisioning of servers. By allowing developers to run code in response to events without the complexity of managing infrastructure, serverless abstracts away the server management, enabling teams to focus more on writing code and less on server maintenance. This approach can lead to significant cost savings, as it inherently scales with demand and charges are based only on the compute time consumed.\n\nIn the platforms-and-operations quadrant, serverless is highly relevant due to its operational efficiency and ability to accelerate deployment cycles. Its capability to automatically scale and handle high concurrency makes it an attractive choice for modern application architectures. With major cloud providers offering robust serverless platforms, such as AWS Lambda, Azure Functions, and Google Cloud Functions, the adoption of serverless architectures in production environments has become increasingly viable. As organizations look to enhance agility and reduce operational overhead, serverless is becoming a key pillar in cloud-native strategies.", "link": "../primers/static-code-analysis/", "link_title": "Static Code Analysis Primer", "x": 451.0, "y": 376.2}, {"id": 65, "title": "SOA", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["service-oriented-architecture", "integration-patterns"], "body": "Service-Oriented Architecture (SOA) is a design pattern where distinct services are provided to other components by application components through a communication protocol over a network. SOA's primary goal is to allow easy integration between different applications and to facilitate business processes by making these services reusable and interoperable. This architecture style is particularly useful for organizations aiming to create complex systems that are agile and can be modified or extended with minimal impact on existing services.\n\nSOA is relevant in the \"methods-and-patterns\" quadrant because it provides a framework for structuring and organizing software components that can be reused across different projects and solutions. The \"assess\" ring is appropriate as organizations are continuously evaluating how best to integrate SOA with modern microservices architectures, considering cloud-native approaches and the need for more dynamic, scalable solutions. As technology evolves, businesses are assessing whether traditional SOA implementations meet their needs or if new patterns are required to adapt to the changing landscape.", "link": "../guides/cybersecurity/01-threat-modeling-foundations/", "link_title": "Threat Modeling Foundations (GD-004)", "x": 504.4, "y": 604.9}, {"id": 66, "title": "SQLite", "ring": "adopt", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["embedded-database", "lightweight-database"], "body": "SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. It is the most widely deployed database engine in the world, embedded into all sorts of applications. Its simplicity and ease of use make it an ideal choice for embedded database needs, mobile apps, and small to medium-sized applications that do not require the overhead of a full-scale database server.\n\nIn the tools quadrant, SQLite is categorized in the adopt ring because it has been proven as a reliable and mature technology. It offers zero-configuration, which means no setup or administration is needed, making it an excellent choice for developers seeking a hassle-free database solution. Its ability to handle most SQL queries and its support for ACID transactions make it relevant for a wide range of applications. SQLite's lightweight nature also contributes to its adoption in environments where resources are constrained. This makes it a versatile tool in a developer's toolkit.", "link": "../guides/c4-model/06-structurizr-dsl-reference/", "link_title": "C4 Guide: Structurizr DSL (GD-001)", "x": 335.1, "y": 460.5}, {"id": 67, "title": "Structurizr", "ring": "assess", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["architecture-diagrams", "software-design", "cloud"], "body": "Structurizr is a tool designed for creating software architecture diagrams based on the C4 model, which emphasizes clarity and simplicity in visualizing software architecture. It is particularly useful for software architects and developers who need to communicate complex systems effectively. Structurizr allows users to define their architecture models using code, enabling version control and integration with existing development workflows. In the tools quadrant, Structurizr stands out as a modern approach to diagramming that aligns with agile methodologies and continuous integration practices. In the assess ring, it is recommended for evaluation as it can potentially enhance documentation and understanding of software systems within organizations, especially those adopting cloud-native technologies.", "link": "../handbook/03-architecture-patterns/", "link_title": "Architecture Handbook: Patterns (GD-002)", "x": 204.2, "y": 520.7}, {"id": 68, "title": "TOGAF", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["enterprise-architecture", "best-practices"], "body": "TOGAF, which stands for The Open Group Architecture Framework, is a comprehensive framework used for developing and managing enterprise architecture. It is widely adopted by organizations to improve business efficiency and ensure that IT aligns with business objectives. As a key player in the methods-and-patterns quadrant, TOGAF provides a structured approach for organizing and governing information technology infrastructure.\n\nIts utility lies in its ability to help organizations optimize and standardize processes, reduce redundancy, and ensure interoperability across systems. By adopting TOGAF, enterprises can better manage the complexity of IT systems, reduce costs, and support business transformation initiatives. Its relevance is underscored by its flexibility and the vast community that supports it, making it a robust choice for enterprises looking to implement best practices in architecture development.", "link": "../handbook/05-cloud-architecture/", "link_title": "Architecture Handbook: Cloud (GD-002)", "x": 418.3, "y": 461.7}, {"id": 69, "title": "UML Modeling", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["design"], "body": "Unified Modeling Language (UML) is a standard way to visualize software architecture.", "link": "../guides/cybersecurity/01-threat-modeling-foundations/", "link_title": "Threat Modeling Foundations (GD-004)", "x": 428.9, "y": 475.3}, {"id": 70, "title": "V-Model", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["software-development", "testing", "project-management"], "body": "The V-Model, also known as the Verification and Validation model, is a software development process that emphasizes the importance of testing at each stage of development. It extends the traditional waterfall model by associating a testing phase with each corresponding development stage. This ensures that validation and verification are integral parts of the development lifecycle, leading to early detection and correction of defects.\n\nThe V-Model is useful because it provides a structured approach to software development, where each phase must be completed before the next begins, ensuring clarity and order. It is particularly beneficial in environments where compliance and quality are critical, such as in safety-critical systems and regulated industries.\n\nIn the methods-and-patterns quadrant, the V-Model is assessed because while it offers a disciplined and organized approach, its rigidity may not suit all projects, especially those requiring rapid iteration or agile methodologies. Nevertheless, understanding and potentially integrating the principles of the V-Model can enhance a team's ability to manage projects with stringent quality and testing requirements.", "link": "../standards/unique-identifiers/", "link_title": "Unique Identifiers Guide (GU-023)", "x": 552.5, "y": 602.3}, {"id": 71, "title": "Visual Studio Code", "ring": "adopt", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["editor"], "body": "VS Code is a popular editor for development with rich plugin support.", "link": "../primers/terminal-modernisation/", "link_title": "Terminal Modernisation Primer", "x": 320.9, "y": 440.3}, {"id": 72, "title": "VS code", "ring": "adopt", "quadrant": "tools", "quadrant_name": "Tools & Utilities", "tags": ["code-editor", "IDE", "developer-productivity"], "body": "Visual Studio Code (VS Code) is a widely-used, open-source code editor developed by Microsoft. It provides developers with an efficient, lightweight, and highly customizable environment to write and debug code across various programming languages. VS Code is particularly appreciated for its rich extension ecosystem, enabling users to enhance functionality with plugins for specific languages, integrations, and developer tools.\n\nAs a tool, VS Code is invaluable for its speed, intuitive user interface, and built-in features such as IntelliSense, debugging support, and Git integration. Its relevance in the \"adopt\" ring signifies broad acceptance and trust in its capabilities among development teams, making it a go-to choice for many coding projects. The tool's adaptability across different operating systems and robust community support further solidify its position in aiding developer productivity and collaboration.", "link": "../primers/terminal-modernisation/", "link_title": "Terminal Modernisation Primer", "x": 355.1, "y": 433.9}, {"id": 73, "title": "Waterfall", "ring": "hold", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["project-management", "software-development"], "body": "Waterfall is a traditional software development methodology that follows a linear and sequential approach, akin to a cascading waterfall. Each phase—such as requirements gathering, design, implementation, testing, and maintenance—must be completed before the next one begins. This method is useful in projects where requirements are well-understood and unlikely to change, as it emphasizes thorough documentation and a clear project roadmap.\n\nDespite its structured approach, Waterfall is placed in the \"hold\" ring because contemporary software development often demands flexibility to accommodate changing requirements and iterative improvements, which are better supported by agile methodologies. In the \"methods-and-patterns\" quadrant, Waterfall serves as a historical reference point that helps understand the evolution of software development practices. It remains relevant for certain industries like aerospace and construction, where rigorous adherence to specifications is critical.", "link": "../primers/agile-development/", "link_title": "Agile Development Primer", "x": 622.7, "y": 622.7}, {"id": 74, "title": "YAGNI (You Aren’t Gonna Need It)", "ring": "adopt", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["software-development", "agile-practices"], "body": "YAGNI (You Aren’t Gonna Need It) is a fundamental principle of agile software development that encourages developers to avoid adding functionality until it is necessary. By adhering to YAGNI, teams can maintain a lean codebase, reduce complexity, and focus on delivering features that provide immediate value to the user. This principle is particularly useful in iterative development environments where requirements can change rapidly, and maintaining flexibility is crucial. Within the methods-and-patterns quadrant, YAGNI is a foundational practice, promoting efficient workflow and resource use. It is recommended for adoption as it aligns with the modern emphasis on agility and responsiveness in software development. Implementing YAGNI can help organizations avoid over-engineering and concentrate efforts on current needs, ensuring that development remains focused and productive.", "link": "../standards/software-architecture-principles/", "link_title": "Software Architecture Principles (GU-019)", "x": 427.6, "y": 492.9}, {"id": 75, "title": "YAML", "ring": "adopt", "quadrant": "languages-and-frameworks", "quadrant_name": "Languages & Frameworks", "tags": ["data-serialization", "configuration"], "body": "YAML, which stands for \"YAML Ain't Markup Language,\" is a human-readable data serialization standard that is commonly used for configuration files and data interchange between programming languages. Its concise and easy-to-read syntax makes it an excellent choice for configuration files and data serialization, particularly in environments where developers and system administrators need to work closely together, such as in DevOps practices.\n\nYAML's relevance in the \"languages-and-frameworks\" quadrant stems from its widespread adoption across various technologies and platforms. It is supported by many programming languages and is the preferred format for configuration files in numerous frameworks and tools, such as Docker Compose, Ansible, and Kubernetes.\n\nIn terms of the \"adopt\" ring, YAML has already proven its value and stability in production environments across different domains, making it a reliable choice for organizations looking to streamline their configuration management and data serialization processes. Its simplicity and readability have contributed to its popularity, cementing its place as a key component in modern software development and deployment practices.", "link": "../guidelines/documentation-as-code/", "link_title": "Docs-as-Code Guide (GU-010)", "x": 381.8, "y": 352.5}, {"id": 76, "title": "Yocto Project", "ring": "adopt", "quadrant": "platforms-and-operations", "quadrant_name": "Platforms & Operations", "tags": ["linux"], "body": "Yocto Project helps build custom Linux-based systems for embedded applications.", "link": "../primers/embedded-systems-design/", "link_title": "Embedded Systems Design Primer", "x": 486.9, "y": 382.1}, {"id": 77, "title": "Zachman Framework", "ring": "assess", "quadrant": "methods-and-patterns", "quadrant_name": "Methods & Patterns", "tags": ["enterprise-architecture", "framework"], "body": "The Zachman Framework is a comprehensive enterprise architecture framework for organizing and categorizing the various perspectives involved in enterprise architecture. It provides a structured way to view and define an enterprise's architecture by considering different aspects like data, functionality, network, people, time, and motivation across multiple perspectives, such as business owner, architect, designer, builder, and user.\n\nThe framework is particularly useful for ensuring that all aspects of an enterprise's architecture are considered and integrated effectively, promoting consistency and communication across different departments and stakeholders. Its relevance in the \"methods-and-patterns\" quadrant stems from its systematic approach to enterprise architecture, allowing organizations to assess and plan their architectural strategies comprehensively.\n\nPlacing it in the \"assess\" ring indicates that while the framework is well-established and valuable for certain organizations, it's essential to evaluate its fit for your specific context and needs before adoption. The tags highlight its role in enterprise architecture and its nature as a framework guiding organizational structure and processes.", "link": "../handbook/01-introduction-to-architecture/", "link_title": "Architecture Handbook: Foundations (GD-002)", "x": 474.1, "y": 592.9}];

  function isDarkMode() {
    return document.body.getAttribute('data-md-color-scheme') === 'slate';
  }

  const ringStyles = {
    'adopt': { color: '#2e7d32', bg: '#e8f5e9', border: '#a5d6a7', label: 'Adopt', darkColor: '#81c784', darkBg: 'rgba(76, 175, 80, 0.22)', darkBorder: '#388e3c' },
    'trial': { color: '#1565c0', bg: '#e3f2fd', border: '#90caf9', label: 'Trial', darkColor: '#64b5f6', darkBg: 'rgba(33, 150, 243, 0.22)', darkBorder: '#1976d2' },
    'assess': { color: '#e65100', bg: '#fff3e0', border: '#ffe082', label: 'Assess', darkColor: '#ffb74d', darkBg: 'rgba(255, 152, 0, 0.22)', darkBorder: '#f57c00' },
    'hold': { color: '#c62828', bg: '#ffebee', border: '#ef9a9a', label: 'Hold', darkColor: '#e57373', darkBg: 'rgba(244, 67, 54, 0.22)', darkBorder: '#d32f2f' }
  };

  let activeRing = 'all';
  let activeQuad = 'all';
  let activeTag = 'all';
  let searchTerm = '';

  function init() {
    setupModalEvents();
    setupFilterEvents();
    setupMobileTabs();
    renderCardsGrid();
    setupBlipEvents();
    applyFilters();
    setupThemeObserver();
  }

  function setupMobileTabs() {
    const tabCanvas = document.getElementById('tab-canvas-btn');
    const tabList = document.getElementById('tab-list-btn');
    const canvasPanel = document.getElementById('radar-canvas-panel');
    const listPanel = document.getElementById('radar-list-panel');

    if (tabCanvas && tabList && canvasPanel && listPanel) {
      tabCanvas.addEventListener('click', function() {
        tabCanvas.classList.add('active-tab');
        tabList.classList.remove('active-tab');
        canvasPanel.classList.remove('mobile-hidden');
        listPanel.classList.remove('mobile-visible-only');
      });

      tabList.addEventListener('click', function() {
        tabList.classList.add('active-tab');
        tabCanvas.classList.remove('active-tab');
        canvasPanel.classList.add('mobile-hidden');
        listPanel.classList.add('mobile-visible-only');
        listPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    }
  }

  // Open modal with blip data
  window.openRadarModal = function(blipId) {
    const blip = blipsData.find(b => b.id === blipId);
    if (!blip) return;

    const overlay = document.getElementById('radar-modal-overlay');
    const modalId = document.getElementById('modal-id');
    const modalTitle = document.getElementById('modal-title');
    const modalRingBadge = document.getElementById('modal-ring-badge');
    const modalQuadrant = document.getElementById('modal-quadrant');
    const modalTags = document.getElementById('modal-tags');
    const modalBodyText = document.getElementById('modal-body-text');
    const modalLinkContainer = document.getElementById('modal-link-container');

    const dark = isDarkMode();
    const style = ringStyles[blip.ring] || { color: '#333', bg: '#eee', border: '#cbd5e1', label: blip.ring, darkColor: '#cbd5e1', darkBg: '#334155', darkBorder: '#475569' };

    modalId.textContent = blip.id;
    modalId.style.background = style.color;
    modalTitle.textContent = blip.title;
    
    modalRingBadge.textContent = style.label;
    modalRingBadge.style.color = dark ? (style.darkColor || style.color) : style.color;
    modalRingBadge.style.background = dark ? (style.darkBg || style.bg) : style.bg;
    modalRingBadge.style.border = '1px solid ' + (dark ? (style.darkBorder || style.border) : style.border);

    modalQuadrant.textContent = 'Quadrant: ' + blip.quadrant_name;

    // Tags
    modalTags.innerHTML = '';
    if (blip.tags && blip.tags.length > 0) {
      blip.tags.forEach(t => {
        const span = document.createElement('span');
        span.className = 'modal-tag-chip';
        span.textContent = '#' + t;
        modalTags.appendChild(span);
      });
    }

    // Body paragraphs
    const paras = blip.body.split(/\n\n+/);
    modalBodyText.innerHTML = paras.map(p => '<p>' + escapeHtml(p) + '</p>').join('');

    // Guideline reference link
    modalLinkContainer.innerHTML = '';
    if (blip.link) {
      const a = document.createElement('a');
      a.href = blip.link;
      a.className = 'modal-guideline-link';
      a.innerHTML = '📖 ' + escapeHtml(blip.link_title || 'Related Guideline') + ' &rarr;';
      modalLinkContainer.appendChild(a);
    }

    overlay.style.display = 'flex';
    document.body.style.overflow = 'hidden'; // Prevent background scrolling on mobile
  };

  function closeModal() {
    const overlay = document.getElementById('radar-modal-overlay');
    if (overlay) overlay.style.display = 'none';
    document.body.style.overflow = '';
  }

  function setupModalEvents() {
    const overlay = document.getElementById('radar-modal-overlay');
    const closeBtn = document.getElementById('modal-close-btn');
    const dismissBtn = document.getElementById('modal-dismiss-btn');

    if (closeBtn) closeBtn.onclick = closeModal;
    if (dismissBtn) dismissBtn.onclick = closeModal;
    if (overlay) {
      overlay.onclick = function(e) {
        if (e.target === overlay) closeModal();
      };
    }
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeModal();
    });
  }

  function setupFilterEvents() {
    const searchInput = document.getElementById('radar-search');
    if (searchInput) {
      searchInput.oninput = function() {
        searchTerm = searchInput.value.toLowerCase().trim();
        applyFilters();
      };
    }

    const quadSelect = document.getElementById('radar-quad-select');
    if (quadSelect) {
      quadSelect.onchange = function() {
        activeQuad = quadSelect.value;
        applyFilters();
      };
    }

    const ringBtns = document.querySelectorAll('.ring-filter-btn');
    ringBtns.forEach(btn => {
      btn.onclick = function() {
        activeRing = btn.getAttribute('data-ring');
        ringBtns.forEach(b => {
          b.classList.remove('active-ring-btn');
          b.style.background = '';
          b.style.color = '';
          b.style.borderColor = '';
        });
        btn.classList.add('active-ring-btn');
        const st = ringStyles[activeRing];
        const dark = isDarkMode();
        if (st) {
          btn.style.background = dark ? st.darkBg : st.bg;
          btn.style.color = dark ? st.darkColor : st.color;
          btn.style.borderColor = dark ? st.darkBorder : st.border;
        } else {
          btn.style.background = dark ? '#14B8A6' : '#003C64';
          btn.style.color = '#ffffff';
          btn.style.borderColor = dark ? '#14B8A6' : '#003C64';
        }
        applyFilters();
      };
    });
  }

  function setupBlipEvents() {
    blipsData.forEach(b => {
      const el = document.getElementById('blip-' + b.id);
      if (el) {
        // Tap / Click handler
        el.onclick = function(e) {
          e.preventDefault();
          window.openRadarModal(b.id);
        };
        el.onmouseenter = function() {
          el.setAttribute('transform', 'scale(1.3) translate(' + (-b.x * 0.3 / 1.3) + ',' + (-b.y * 0.3 / 1.3) + ')');
        };
        el.onmouseleave = function() {
          el.removeAttribute('transform');
        };
      }
    });
  }

  function applyFilters() {
    blipsData.forEach(b => {
      let matches = true;

      if (activeRing !== 'all' && b.ring !== activeRing) matches = false;
      if (activeQuad !== 'all' && b.quadrant !== activeQuad) matches = false;
      if (activeTag !== 'all') {
        const hasTag = b.tags && b.tags.some(t => {
          const tl = t.toLowerCase();
          if (activeTag === 'embedded') return tl.includes('embedded') || tl.includes('iot') || tl.includes('real-time') || tl.includes('safety') || tl.includes('c');
          if (activeTag === 'cloud') return tl.includes('cloud') || tl.includes('container') || tl.includes('microservices') || tl.includes('serverless');
          if (activeTag === 'security') return tl.includes('security') || tl.includes('threat') || tl.includes('crypt') || tl.includes('compliance');
          if (activeTag === 'architecture') return tl.includes('architecture') || tl.includes('design') || tl.includes('domain') || tl.includes('pattern') || tl.includes('modeling');
          if (activeTag === 'devops') return tl.includes('devops') || tl.includes('automation') || tl.includes('version-control') || tl.includes('testing') || tl.includes('ci');
          if (activeTag === 'iot') return tl.includes('iot') || tl.includes('embedded') || tl.includes('edge');
          return tl.includes(activeTag);
        });
        if (!hasTag) matches = false;
      }

      if (searchTerm) {
        const titleMatch = b.title.toLowerCase().includes(searchTerm);
        const tagsMatch = b.tags && b.tags.some(t => t.toLowerCase().includes(searchTerm));
        const bodyMatch = b.body.toLowerCase().includes(searchTerm);
        if (!titleMatch && !tagsMatch && !bodyMatch) matches = false;
      }

      const blipEl = document.getElementById('blip-' + b.id);
      if (blipEl) {
        blipEl.style.opacity = matches ? '1' : '0.12';
        blipEl.style.pointerEvents = matches ? 'auto' : 'none';
      }

      const itemEl = document.getElementById('radar-item-' + b.id);
      if (itemEl) {
        itemEl.style.display = matches ? 'flex' : 'none';
      }
    });
  }

  function renderCardsGrid() {
    const grid = document.getElementById('radar-cards-grid');
    if (!grid) return;
    grid.innerHTML = '';

    const quads = [
      { key: 'languages-and-frameworks', name: '1. Languages & Frameworks' },
      { key: 'platforms-and-operations', name: '2. Platforms & Operations' },
      { key: 'tools', name: '3. Tools & Utilities' },
      { key: 'methods-and-patterns', name: '4. Methods & Patterns' }
    ];

    quads.forEach(q => {
      const qBlips = blipsData.filter(b => b.quadrant === q.key);
      const colDiv = document.createElement('div');
      colDiv.className = 'radar-quad-col';

      const title = document.createElement('h3');
      title.className = 'radar-quad-col-title';
      title.textContent = q.name + ' (' + qBlips.length + ')';
      colDiv.appendChild(title);

      const listDiv = document.createElement('div');
      listDiv.className = 'radar-quad-col-list';

      qBlips.forEach(b => {
        const item = document.createElement('div');
        item.id = 'radar-item-' + b.id;
        item.className = 'radar-blip-item-card';
        
        const dark = isDarkMode();
        const style = ringStyles[b.ring] || { color: '#333', bg: '#eee', darkColor: '#cbd5e1', darkBg: '#334155' };
        const ringBg = dark ? (style.darkBg || style.bg) : style.bg;
        const ringColor = dark ? (style.darkColor || style.color) : style.color;
        item.innerHTML = '<div class="blip-item-left">' +
          '<span class="blip-item-num" style="background: ' + style.color + ';">' + b.id + '</span>' +
          '<span class="blip-item-title">' + escapeHtml(b.title) + '</span>' +
          '</div>' +
          '<span class="blip-item-ring" style="color: ' + ringColor + '; background: ' + ringBg + ';">' + b.ring + '</span>';

        item.onmouseenter = function() {
          item.classList.add('blip-hovered');
          const blipSvg = document.getElementById('blip-' + b.id);
          if (blipSvg) blipSvg.setAttribute('transform', 'scale(1.4) translate(' + (-b.x * 0.4 / 1.4) + ',' + (-b.y * 0.4 / 1.4) + ')');
        };
        item.onmouseleave = function() {
          item.classList.remove('blip-hovered');
          const blipSvg = document.getElementById('blip-' + b.id);
          if (blipSvg) blipSvg.removeAttribute('transform');
        };
        item.onclick = function() {
          window.openRadarModal(b.id);
        };

        listDiv.appendChild(item);
      });

      colDiv.appendChild(listDiv);
      grid.appendChild(colDiv);
    });
  }

  function setupThemeObserver() {
    const observer = new MutationObserver(function(mutations) {
      for (const m of mutations) {
        if (m.attributeName === 'data-md-color-scheme') {
          renderCardsGrid();
          const ringBtns = document.querySelectorAll('.ring-filter-btn');
          const dark = isDarkMode();
          ringBtns.forEach(b => {
            if (b.classList.contains('active-ring-btn')) {
              const r = b.getAttribute('data-ring');
              const st = ringStyles[r];
              if (st) {
                b.style.background = dark ? (st.darkBg || st.bg) : st.bg;
                b.style.color = dark ? (st.darkColor || st.color) : st.color;
                b.style.borderColor = dark ? (st.darkBorder || st.border) : st.border;
              } else {
                b.style.background = dark ? '#14B8A6' : '#003C64';
                b.style.color = '#ffffff';
                b.style.borderColor = dark ? '#14B8A6' : '#003C64';
              }
            } else {
              b.style.background = '';
              b.style.color = '';
              b.style.borderColor = '';
            }
          });
          break;
        }
      }
    });
    observer.observe(document.body, { attributes: true });
  }

  function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>

<style>
/* Radar Mobile & Desktop Responsive Styles */
.radar-app-root {
  margin: 1.5rem 0;
  font-family: inherit;
}

.radar-mobile-switcher {
  display: none;
  justify-content: center;
  gap: 8px;
  margin-bottom: 1rem;
}

.mobile-tab-btn {
  flex: 1;
  max-width: 200px;
  padding: 8px 14px;
  font-size: 0.85rem;
  font-weight: 700;
  border-radius: 8px;
  border: 1px solid #cbd5e1;
  background: #f8fafc;
  color: #475569;
  cursor: pointer;
  min-height: 44px;
  touch-action: manipulation;
}

.mobile-tab-btn.active-tab {
  background: #003C64;
  color: #ffffff;
  border-color: #003C64;
}

.radar-toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
  padding: 12px 16px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
}

.radar-search-box {
  flex: 1 1 240px;
  min-width: 200px;
}

.radar-search-box input {
  width: 100%;
  padding: 9px 14px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  font-size: 0.9rem;
  outline: none;
  min-height: 42px;
  box-sizing: border-box;
}

.radar-quad-filter {
  display: flex;
  align-items: center;
  gap: 6px;
}

.radar-label {
  font-size: 0.8rem;
  font-weight: 700;
  color: #64748b;
  text-transform: uppercase;
}

.radar-quad-filter select {
  padding: 8px 12px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  font-size: 0.85rem;
  background: #fff;
  cursor: pointer;
  min-height: 42px;
}

.radar-ring-filter {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.ring-btn-group {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.ring-filter-btn {
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid #cbd5e1;
  background: #f8fafc;
  color: #334155;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  min-height: 38px;
  touch-action: manipulation;
}

.radar-tag-filter {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  width: 100%;
  margin-top: 6px;
  padding-top: 8px;
  border-top: 1px dashed #e2e8f0;
}

[data-md-color-scheme="slate"] .radar-tag-filter {
  border-top-color: #334155;
}

.tag-btn-group {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tag-filter-chip {
  padding: 4px 10px;
  font-size: 0.78rem;
  font-weight: 600;
  border-radius: 12px;
  border: 1px solid #cbd5e1;
  background: #f1f5f9;
  color: #475569;
  cursor: pointer;
  transition: all 0.15s ease;
  touch-action: manipulation;
  min-height: 32px;
}

.tag-filter-chip:hover {
  background: #e2e8f0;
  color: #0f172a;
}

.tag-filter-chip.active-tag-chip {
  background: #003C64;
  color: #ffffff;
  border-color: #003C64;
}

[data-md-color-scheme="slate"] .tag-filter-chip {
  background: #1e293b;
  border-color: #475569;
  color: #94a3b8;
}

[data-md-color-scheme="slate"] .tag-filter-chip:hover {
  background: #334155;
  color: #f8fafc;
}

[data-md-color-scheme="slate"] .tag-filter-chip.active-tag-chip {
  background: #14B8A6;
  color: #0f172a;
  border-color: #14B8A6;
}

.radar-canvas-card {
  position: relative;
  width: 100%;
  max-width: 820px;
  margin: 0 auto;
  text-align: center;
  border-radius: 12px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 16px rgba(0,0,0,0.06);
  padding: 10px;
  box-sizing: border-box;
}

.radar-svg-container {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  overflow: hidden;
  position: relative;
}

.radar-svg-container svg {
  width: 100%;
  max-width: 800px;
  height: auto;
  aspect-ratio: 1 / 1;
  display: block;
  margin: 0 auto;
}

.radar-hint-note {
  font-size: 0.85rem;
  color: #64748b;
  margin-top: 8px;
}

.radar-blip {
  transition: transform 0.15s ease-out, opacity 0.2s ease;
  touch-action: manipulation;
}

.radar-blip:hover circle:not(.touch-target) {
  stroke-width: 2.5;
  stroke: #ffeb3b;
}

/* Modal Popup */
.radar-modal-backdrop {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(4px);
  z-index: 99999;
  align-items: center;
  justify-content: center;
  padding: 16px;
  box-sizing: border-box;
}

.radar-modal-container {
  background: #ffffff;
  width: 100%;
  max-width: 600px;
  max-height: 85vh;
  border-radius: 14px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  animation: radarFadeIn 0.2s ease-out;
}

.radar-modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 18px 22px;
  border-bottom: 1px solid #e2e8f0;
  background: #f8fafc;
}

.modal-id-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #003C64;
  color: #ffffff;
  font-weight: 800;
  font-size: 0.85rem;
}

.modal-title-text {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 700;
  color: #0f172a;
}

.modal-meta-row {
  margin-top: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.modal-ring-chip {
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  padding: 3px 10px;
  border-radius: 12px;
  letter-spacing: 0.5px;
}

.modal-quadrant-text {
  font-size: 0.8rem;
  color: #475569;
  font-weight: 600;
}

.modal-close-button {
  background: transparent;
  border: none;
  font-size: 1.8rem;
  color: #64748b;
  cursor: pointer;
  min-width: 44px;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  line-height: 1;
}

.radar-modal-body {
  padding: 20px 22px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  flex: 1;
}

.modal-tags-container {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 14px;
}

.modal-tag-chip {
  background: #f1f5f9;
  color: #475569;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: monospace;
}

.modal-body-content {
  font-size: 0.95rem;
  line-height: 1.65;
  color: #334155;
}

.modal-body-content p {
  margin: 0 0 12px 0;
}

.radar-modal-footer {
  padding: 14px 22px;
  border-top: 1px solid #e2e8f0;
  background: #f8fafc;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}

.modal-guideline-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #003C64;
  font-weight: 700;
  font-size: 0.85rem;
  text-decoration: none;
}

.modal-dismiss-btn {
  padding: 8px 18px;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  background: #ffffff;
  font-size: 0.85rem;
  font-weight: 600;
  color: #334155;
  cursor: pointer;
  min-height: 38px;
  touch-action: manipulation;
}

/* Quadrant Lists Grid */
.radar-list-container {
  margin-top: 2rem;
}

.radar-list-title {
  font-size: 1.3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #003C64;
}

.radar-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
}

.radar-quad-col {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 14px;
  display: flex;
  flex-direction: column;
}

.radar-quad-col-title {
  margin: 0 0 10px 0;
  font-size: 1rem;
  font-weight: 700;
  color: #003C64;
  border-bottom: 2px solid #cbd5e1;
  padding-bottom: 6px;
}

.radar-quad-col-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
  overflow-y: auto;
  max-height: 420px;
  -webkit-overflow-scrolling: touch;
}

.radar-blip-item-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 12px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s ease;
  min-height: 46px;
  box-sizing: border-box;
  touch-action: manipulation;
}

.radar-blip-item-card.blip-hovered {
  border-color: #003C64;
  background: #f1f5f9;
}

.blip-item-left {
  display: flex;
  align-items: center;
  gap: 8px;
}

.blip-item-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  color: #fff;
  font-size: 0.75rem;
  font-weight: bold;
}

.blip-item-title {
  font-size: 0.88rem;
  font-weight: 600;
  color: #1e293b;
}

.blip-item-ring {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 10px;
}

/* Mobile Media Queries */
@media (max-width: 768px) {
  .radar-mobile-switcher {
    display: flex;
  }
  .radar-toolbar {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
  }
  .radar-search-box {
    width: 100%;
  }
  .radar-quad-filter {
    width: 100%;
    justify-content: space-between;
  }
  .radar-quad-filter select {
    flex: 1;
  }
  .radar-ring-filter {
    width: 100%;
    justify-content: space-between;
  }
  .ring-btn-group {
    flex: 1;
    justify-content: space-between;
  }
  .ring-filter-btn {
    flex: 1;
    text-align: center;
    padding: 6px 4px;
    font-size: 0.75rem;
  }
  .mobile-hidden {
    display: none !important;
  }
  .mobile-visible-only {
    display: block !important;
  }
  #radar-modal-overlay {
    padding: 10px;
    align-items: flex-end;
  }
  #radar-modal-card {
    max-height: 90vh;
    border-radius: 16px 16px 0 0;
  }
  .modal-title-text {
    font-size: 1.15rem;
  }
  .radar-modal-footer {
    flex-direction: column;
    align-items: stretch;
  }
  .modal-dismiss-btn {
    width: 100%;
  }
}

@keyframes radarFadeIn {
  from { opacity: 0; transform: scale(0.96); }
  to { opacity: 1; transform: scale(1); }
}

/* --- Dark Mode (Slate Palette) Adaptive Styling --- */
.radar-svg-bg {
  fill: #ffffff;
  transition: fill 0.3s ease;
}
.radar-grid-line {
  stroke: #b0bec5;
  transition: stroke 0.3s ease;
}
.radar-quad-title {
  fill: #003C64;
  transition: fill 0.3s ease;
}
.radar-ring-label.ring-adopt { fill: #2e7d32; }
.radar-ring-label.ring-trial { fill: #1565c0; }
.radar-ring-label.ring-assess { fill: #e65100; }
.radar-ring-label.ring-hold { fill: #c62828; }

[data-md-color-scheme="slate"] .radar-svg-bg {
  fill: #1e293b;
}
[data-md-color-scheme="slate"] .radar-grid-line {
  stroke: #475569;
}
[data-md-color-scheme="slate"] .radar-quad-title {
  fill: #94a3b8;
}
[data-md-color-scheme="slate"] .radar-ring-label.ring-adopt { fill: #81c784; }
[data-md-color-scheme="slate"] .radar-ring-label.ring-trial { fill: #64b5f6; }
[data-md-color-scheme="slate"] .radar-ring-label.ring-assess { fill: #ffb74d; }
[data-md-color-scheme="slate"] .radar-ring-label.ring-hold { fill: #e57373; }

[data-md-color-scheme="slate"] .radar-canvas-card {
  background: #1e293b;
  border-color: #334155;
  box-shadow: 0 4px 16px rgba(0,0,0,0.35);
}
[data-md-color-scheme="slate"] .radar-hint-note {
  color: #94a3b8;
}
[data-md-color-scheme="slate"] .radar-toolbar {
  background: #1e293b;
  border-color: #334155;
}
[data-md-color-scheme="slate"] .radar-label {
  color: #94a3b8;
}
[data-md-color-scheme="slate"] .radar-search-box input {
  background: #0f172a;
  color: #f1f5f9;
  border-color: #334155;
}
[data-md-color-scheme="slate"] .radar-search-box input::placeholder {
  color: #64748b;
}
[data-md-color-scheme="slate"] .radar-quad-filter select {
  background: #0f172a;
  color: #f1f5f9;
  border-color: #334155;
}
[data-md-color-scheme="slate"] .ring-filter-btn {
  background: #0f172a;
  color: #cbd5e1;
  border-color: #334155;
}
[data-md-color-scheme="slate"] .ring-filter-btn:hover {
  background: #1e293b;
  border-color: #475569;
}
[data-md-color-scheme="slate"] .radar-list-title {
  color: #e2e8f0;
}
[data-md-color-scheme="slate"] .radar-quad-col {
  background: #1e293b;
  border-color: #334155;
}
[data-md-color-scheme="slate"] .radar-quad-col-title {
  color: #94a3b8;
  border-bottom-color: #334155;
}
[data-md-color-scheme="slate"] .radar-blip-item-card {
  background: #0f172a;
  border-color: #334155;
}
[data-md-color-scheme="slate"] .radar-blip-item-card.blip-hovered {
  border-color: #14B8A6;
  background: #14202e;
}
[data-md-color-scheme="slate"] .blip-item-title {
  color: #e2e8f0;
}
[data-md-color-scheme="slate"] .mobile-tab-btn {
  background: #0f172a;
  color: #94a3b8;
  border-color: #334155;
}
[data-md-color-scheme="slate"] .mobile-tab-btn.active-tab {
  background: #14B8A6;
  color: #ffffff;
  border-color: #14B8A6;
}

/* Modal Slate Dark Theme */
[data-md-color-scheme="slate"] .radar-modal-container {
  background: #1e293b;
  color: #f1f5f9;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
}
[data-md-color-scheme="slate"] .radar-modal-header {
  background: #0f172a;
  border-bottom-color: #334155;
}
[data-md-color-scheme="slate"] .modal-title-text {
  color: #f8fafc;
}
[data-md-color-scheme="slate"] .modal-quadrant-text {
  color: #94a3b8;
}
[data-md-color-scheme="slate"] .modal-close-button {
  color: #94a3b8;
}
[data-md-color-scheme="slate"] .modal-close-button:hover {
  background: #334155;
  color: #ffffff;
}
[data-md-color-scheme="slate"] .modal-tag-chip {
  background: #334155;
  color: #cbd5e1;
}
[data-md-color-scheme="slate"] .modal-body-content {
  color: #cbd5e1;
}
[data-md-color-scheme="slate"] .radar-modal-footer {
  background: #0f172a;
  border-top-color: #334155;
}
[data-md-color-scheme="slate"] .modal-guideline-link {
  color: #14B8A6;
}
[data-md-color-scheme="slate"] .modal-dismiss-btn {
  background: #334155;
  color: #e2e8f0;
  border-color: #475569;
}
[data-md-color-scheme="slate"] .modal-dismiss-btn:hover {
  background: #475569;
  color: #ffffff;
}
</style>

"""
Implementation of the GrantAdvisorWorkflow for the MCP server.
This provides simulated expert advice similar to the Gradio app.
"""
from datetime import datetime
from typing import Dict, Any, List, Optional

class GrantAdvisorWorkflow:
    """
    Workflow that simulates expert advisors for grant research and planning.
    """
    
    def __init__(self):
        pass
        
    def generate_financial_plan(self, topic: str, location: str = "") -> str:
        """Generate a financial management strategic framework."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        return f"""# Financial Management Strategic Framework
**Generated:** {timestamp}  
**Topic:** {topic}  
**Location:** {location or "Not specified"}

## Executive Summary
This strategic framework provides proven financial management approaches specifically designed for small non-profit operations pursuing {topic}. Focus is on building sustainable infrastructure, establishing transparent systems, and demonstrating fiscal responsibility to funders.

## Budget Development Framework

### Cost Structure Approach for Small Organizations
**Personnel (Typically 60-70% of budget):**
- Core program staff (director, coordinator, part-time support)
- Consider volunteer coordination to extend capacity
- Build in professional development allocations
- Plan for benefits if full-time positions created

**Operations (Typically 20-30% of budget):**
- Shared office space or donated facilities
- Technology infrastructure (cloud-based to minimize upfront costs)
- Insurance and compliance requirements
- Utilities and basic supplies

**Program Delivery (Typically 10-20% of budget):**
- Materials and participant supplies
- Transportation or accessibility support
- Community outreach and engagement
- Evaluation and data collection

### Sustainability Planning Framework

**Multi-Source Revenue Diversification:**
- Primary: Competitive grant funding (federal, state, foundation)
- Secondary: Earned revenue streams (fees-for-service, training, consulting)
- Tertiary: Community partnerships (in-kind, shared resources)
- Strategic principle: No single funding source should exceed 40% of annual budget

**Operating Reserve Building:**
- Start small: Target 1-month reserves in Year 1
- Build gradually: 2-3 month reserves by Year 2
- Mature stability: 3-6 month reserves by Year 3
- Use reserves strategically: Bridge funding gaps, not ongoing operations

## Financial Management Systems for Small Organizations

### Essential Infrastructure
**Chart of Accounts:**
- Set up program-based accounting from day one
- Track restricted vs. unrestricted funds separately
- Create expense categories that match common grant budgets
- Use cloud-based accounting (QuickBooks Online, Xero, or free options like Wave)

**Internal Controls (Even with Small Staff):**
- Dual signature requirement for checks/transfers
- Monthly bank reconciliation by someone other than bookkeeper
- Board treasurer reviews financials monthly
- Annual independent financial review or audit when required

**Grant Financial Management:**
- Create separate tracking for each grant award
- Set calendar reminders for reporting deadlines
- Document match requirements and in-kind contributions
- Track time allocation for staff split across multiple grants

## Funder Fiscal Responsibility Expectations

### What Funders Look For in Small Organizations
**Financial Transparency:**
- Clear budget narratives that justify every line item
- Honest assessment of organizational capacity
- Documentation of financial management systems
- Board financial oversight evidence

**Cost Allocation Methodology:**
- Reasonable indirect cost rates (10-15% common for small orgs)
- Documented time-tracking for shared staff
- Clear methodology for allocating shared costs
- Consistency across all grant applications

## Budget Development Process

### Needs-Based Budgeting Approach
1. **Start with Program Design:**
   - What activities will you actually deliver?
   - What staff time is required (be realistic)?
   - What supplies/materials are essential vs. nice-to-have?

2. **Personnel Calculations:**
   - Break down by position and % FTE (Full-Time Equivalent)
   - Include benefits (typically 20-30% of salary)
   - Account for professional development
   - Consider volunteer coordination time

3. **Non-Personnel Expenses:**
   - Facilities: Shared space, donated space, or lease?
   - Technology: Cloud-based subscriptions vs. purchased software
   - Supplies: Estimate per participant/per program cycle
   - Travel: Local vs. regional vs. conference attendance

4. **Indirect/Administrative Costs:**
   - Executive oversight (% of Executive Director time)
   - Bookkeeping and financial management
   - Fundraising/development activities
   - General liability insurance, compliance costs

## Financial Checklist for Grant Applications

### Before You Apply
- [ ] Understand full cost of program delivery
- [ ] Know your organization's indirect cost rate
- [ ] Have current financial statements ready
- [ ] Board-approved annual budget in place
- [ ] Financial management systems documented
- [ ] Banking and fiscal oversight policies written

### Application Budget Development
- [ ] Budget matches narrative activities exactly
- [ ] All costs are reasonable and allocable
- [ ] Match/cost-share requirements can be met
- [ ] Indirect costs calculated correctly
- [ ] Multi-year budgets show realistic escalation
- [ ] Budget narrative explains all line items
"""

    def generate_grant_expert_plan(self, topic: str, location: str = "") -> str:
        """Generate a grant strategy and proposal development framework."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        return f"""# Grant Strategy & Proposal Development Framework
**Generated:** {timestamp}  
**Topic:** {topic}  
**Location:** {location or "Not specified"}

## Executive Summary
This strategic framework provides proven grant development processes specifically designed for small non-profit operations pursuing {topic}. Focus is on building funder relationships, developing compelling narratives, and creating reusable proposal components that increase efficiency.

## Grant Opportunity Assessment Framework

### Identifying the Right Opportunities for Small Organizations

**Federal Grant Considerations:**
- **Capacity requirements:** Do you have staff to manage complex reporting?
- **Match requirements:** Can you meet cost-sharing obligations?
- **Timeline:** Application to award often 6-12 months—can you wait?
- **Competition level:** Success rates typically 10-25%
- **Reporting burden:** Monthly/quarterly reports vs. annual
- **Best for:** Organizations with some grant experience, fiscal infrastructure

**Foundation Grant Considerations:**
- **Alignment:** Mission must clearly align with foundation priorities
- **Geographic focus:** Many limit to specific regions or communities
- **Relationship requirement:** Local foundations value community connection
- **Timeline:** Often faster (3-6 months)
- **Best for:** Smaller budgets, pilot programs, capacity building

**Corporate Giving Considerations:**
- **Employee engagement:** Programs that involve corporate volunteers
- **Measurement focus:** Clear, quantifiable outcomes
- **Quick turnaround:** Often annual cycles
- **Best for:** Community-visible programs, partnerships

## Strategic Grant Calendar Development

### 12-Month Planning Cycle for Small Organizations

**Phase 1: Preparation (Months 1-3)**
*Build your foundation before applying*

**Program Design Finalization:**
- Evidence-based logic model showing inputs → activities → outputs → outcomes
- Clear differentiation from existing services
- Community input documentation
- Evaluation plan with realistic data collection

**Organizational Readiness:**
- Current financial statements and budget
- Board list with community representation
- Letters of support from authentic partners (not form letters)
- 501(c)(3) determination letter
- Annual report or program overview

**Phase 2: First Application Wave (Months 4-6)**
*Start with best-fit opportunities*

- Apply to 2-3 foundation opportunities where you have connection
- Submit 1-2 federal/state opportunities with longer timelines
- Follow up appropriately (not excessively) on letters of inquiry
- Request feedback if you receive declinations

**Phase 3: Building Momentum (Months 7-9)**
*Leverage early wins or learning*

- Submit 3-4 additional applications
- Update proposal library based on feedback
- Cultivate relationships with program officers
- Begin reporting on any funded grants (critical for credibility)
- Adjust strategy based on success patterns

**Phase 4: Sustainability Planning (Months 10-12)**
*Look ahead while managing current grants*

- Submit 2-3 final applications for year
- Plan Year 2 grant calendar
- Conduct stewardship for all funders (funded and not funded)
- Analyze what worked: What was our success rate by funder type?
- Build relationships for multi-year or renewal funding

## Competitive Positioning for Small Organizations

### Leveraging Your Strengths

**Community-Based Authenticity:**
- Deep understanding of local needs
- Lived experience in the community you serve
- Trusted relationships that larger organizations can't replicate
- Flexibility to adapt quickly to community feedback

**Nimble & Responsive:**
- Can pilot innovative approaches
- Lower overhead allows more program dollars
- Direct connection between leadership and service delivery
- Quick decision-making without bureaucracy

**Partnership Orientation:**
- Collaborative rather than competitive stance
- Complement existing services rather than duplicate
- Bring community stakeholders together
- Build capacity in the community, not just your organization

## Grant Proposal Narrative Development

### Writing Strategy for Small Organizations

**The "Goldilocks" Approach to Proposals:**
- Not too corporate (avoid jargon, stay authentic)
- Not too informal (maintain professionalism)
- Just right (clear, compelling, evidence-based with community voice)

### Core Narrative Components with Small Org Focus

**1. Need Statement (15-20% of proposal)**
- Quantitative data about community need
- Qualitative stories that bring data to life
- Gap analysis: What's missing in current services?

**2. Program Design (30-40% of proposal)**
- Clear goals and objectives (SMART)
- Evidence-based methodology
- Timeline and implementation plan
- Staffing and management plan

**3. Evaluation (10-15% of proposal)**
- Process measures (did we do what we said?)
- Outcome measures (did it make a difference?)
- Data collection methods feasible for small staff
- Continuous improvement loop

**4. Organizational Capacity (10-15% of proposal)**
- History and mission
- Staff and board qualifications
- Financial stability and management
- Past successes and track record

**5. Budget and Sustainability (10-15% of proposal)**
- Realistic, detailed budget
- Narrative justification for expenses
- Future funding plan beyond this grant
- Community support and leverage
"""

    def generate_research_plan(self, topic: str, location: str = "") -> str:
        """Generate a research coordination plan."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        return f"""# Research Coordination & Data Strategy
**Generated:** {timestamp}  
**Topic:** {topic}  
**Location:** {location or "Not specified"}

## Executive Summary
This research coordination plan outlines a strategy for gathering, organizing, and utilizing data to support grant applications for {topic}. The focus is on efficient research methods suitable for small teams with limited time.

## Research Strategy

### 1. Needs Assessment Research
**Objective:** Document the specific problem or need your program addresses.

**Data Sources:**
- **Public Data:** Census Bureau, local government reports, health department statistics
- **Community Input:** Surveys, focus groups, community meetings
- **Academic Research:** Studies on similar interventions or populations
- **Service Data:** Your own waiting lists, intake forms, or service gaps

**Action Steps:**
- [ ] Identify 3-5 key data points that define the need
- [ ] Collect 2-3 powerful stories from community members
- [ ] Find 1-2 academic studies supporting your approach
- [ ] Compile into a "Needs Statement" document for reuse

### 2. Funder Research
**Objective:** Identify funders whose priorities align with your mission.

**Research Tools:**
- **Databases:** Candid (Foundation Directory), GrantStation, Instrumentl
- **Free Sources:** 990 forms (ProPublica, GuideStar), funder websites
- **Networks:** Local grantmakers associations, community foundations
- **Peers:** Annual reports of similar organizations (see who funds them)

**Selection Criteria:**
- **Mission Alignment:** Do they fund what you do?
- **Geographic Focus:** Do they fund in your area?
- **Grant Size:** Is their typical grant size appropriate for you?
- **Type of Support:** Do they give the type of funding you need (project vs. operating)?

### 3. Evidence-Based Practice Research
**Objective:** Demonstrate that your proposed solution is likely to work.

**Key Questions:**
- What models have worked elsewhere for this problem?
- What are the "best practices" in your field?
- How does your approach align with or improve upon these practices?
- What evidence supports your specific methodology?

**Action Steps:**
- [ ] Literature review of successful interventions
- [ ] Interviews with experts or practitioners in the field
- [ ] Documentation of your own pilot results or past success
- [ ] Creation of a "Theory of Change" or Logic Model

## Data Management for Grant Applications

### Organizing Your Research
**Central Repository:**
- Create a shared folder (Google Drive, Dropbox, etc.)
- Folders for: Needs Data, Funder Research, Evidence Base, Org Docs
- Maintain a "Boilerplate" document with standard language
- Keep a "Grant Calendar" spreadsheet

### Data Collection for Evaluation
**Simple Metrics to Track:**
- **Outputs:** Number of people served, sessions held, materials distributed
- **Outcomes:** Changes in knowledge, behavior, condition, or status
- **Demographics:** Who are you serving? (Age, race, income, location)
- **Feedback:** Satisfaction surveys, testimonials, suggestions

**Tools for Small Orgs:**
- **Surveys:** Google Forms, SurveyMonkey (free versions)
- **Tracking:** Excel or Google Sheets (start simple)
- **Intake:** Standardized forms for all participants
- **Stories:** Regular method for capturing success stories (e.g., monthly staff meeting)

## Research Checklist for Grant Readiness

### Essential Data Points
- [ ] Community demographics (poverty rate, education, etc.)
- [ ] Specific problem statistics (e.g., disease rate, dropout rate)
- [ ] Number of people currently served vs. need
- [ ] Cost per participant or service unit
- [ ] Success rates or outcome data from past work
- [ ] List of potential partners and their roles

### Funder Research Output
- [ ] List of top 10 prospect funders
- [ ] Calendar of upcoming deadlines
- [ ] Contact information for program officers
- [ ] Notes on recent awards by each funder
- [ ] Application guidelines and requirements for each

---
*This research plan is designed to support evidence-based grant applications for small non-profit organizations.*
"""

    def generate_crash_course_plan(self, topic: str, location: str = "") -> str:
        """Generate a crash course plan for the 'Make It Happen' persona."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        return f"""# The "Make It Happen" Crash Course
**Generated:** {timestamp}
**Topic:** {topic}
**Location:** {location or "Not specified"}

## ⚡ The "Oh, We Can Do That!" Strategy

Look, I know you just saw this grant and thought, "Wait, if we squint, our community garden project is actually 'urban climate resilience infrastructure,' right?"

**You are correct.** And we're going to make them believe it too.

Here is your 24-hour crash course on turning "we have an idea" into "we have a funded project."

### 1. The "Reverse Engineer" Innovation Method
Don't start with what you do. Start with what they want.
*   **They want:** "Youth workforce development."
*   **You have:** A bike repair co-op.
*   **The Pivot:** You are not fixing bikes. You are "providing technical vocational training in sustainable transportation mechanics for at-risk youth."
*   **The Action:** Read the "Eligible Activities" section first. If you can do 50% of it, you can learn the other 50% by the time the check clears.

### 2. The "Shoestring to Gold" Budget Hack
They want to see value? Show them how you turn a dollar into ten.
*   **In-Kind Everything:** Your neighbor's garage? That's "donated facility space ($1,200/mo value)." Your cousin designing the flyer? "Professional graphic design services ($500 value)."
*   **The "Multiplier Effect":** Explain how their $5,000 grant unlocks $20,000 of volunteer labor. Funders love feeling like they're the gas in a car that's already moving.

### 3. The Narrative: "We Are The Only Ones"
Forget "we are a good organization." Boring.
*   **The Hook:** "While others talk about [topic], we are literally in the streets doing it with duct tape and passion."
*   **The Urgency:** "This problem is happening NOW. We are ready NOW. We just need the fuel."
*   **The "Witty" Confidence:** Write like you're already doing it and you're just inviting them to put their logo on the success.

### 4. The "Kitchen Sink" Partnership
You're small? Look big.
*   **Text everyone:** "Hey, can I put you down as a 'community partner' on this grant? I just need you to say you like us."
*   **The Coalition:** Suddenly, you aren't one person with a laptop. You are a "Coalition of Community Stakeholders."

## 🚀 The 3-Hour Proposal Sprint Checklist
*   [ ] **Hour 1: The Skim & Spin.** Read the RFP. Highlight the buzzwords. Rewrite your mission statement using ONLY their buzzwords.
*   [ ] **Hour 2: The "Good Enough" Budget.** Round numbers. Make sure it adds up. Don't overthink the pennies.
*   [ ] **Hour 3: The Passion Pitch.** Write the narrative. Be bold. Be specific. Use active verbs. "We WILL," not "We hope to."

**Final Advice:** Submit it at 11:59 PM if you have to. A submitted "good" proposal beats a perfect one on your hard drive. Go get 'em, tiger.
"""

    def orchestrate_plan(self, topic: str, location: str = "") -> str:
        """Generate a comprehensive orchestrated plan combining all aspects."""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        return f"""# Comprehensive MAI Advisor Strategic Plan
**Generated:** {timestamp}  
**Topic:** {topic}  
**Location:** {location or "Not specified"}

## Executive Summary
This comprehensive strategic plan integrates financial management, grant strategy, and research coordination to support your organization's goals regarding {topic}. It is designed to provide a holistic roadmap for sustainable growth and funding success.

## Integrated Strategic Roadmap

### Phase 1: Foundation Building (Months 1-3)
**Financial Focus:**
- Establish program-based accounting and internal controls
- Develop a detailed, needs-based annual budget
- Set up financial reporting systems for transparency

**Grant Focus:**
- Finalize program design and logic model
- Develop core narrative components (Need, Approach, Capacity)
- Identify top 10 prospect funders

**Research Focus:**
- Conduct needs assessment and gather key data points
- Collect community stories and stakeholder input
- Research evidence-based practices to support your model

### Phase 2: Implementation & Application (Months 4-6)
**Financial Focus:**
- Monitor budget-to-actuals monthly
- Begin building operating reserves (target 1 month)
- Document in-kind contributions and volunteer time

**Grant Focus:**
- Submit 2-3 high-alignment foundation applications
- Submit 1 federal/state application (if ready)
- Engage with program officers and funders

**Research Focus:**
- Implement data collection for program evaluation
- Track outputs and initial outcomes
- Refine "Needs Statement" with new data

### Phase 3: Growth & Sustainability (Months 7-12)
**Financial Focus:**
- Review and adjust budget based on funding success
- Increase operating reserves (target 2-3 months)
- Plan for diversified revenue streams beyond grants

**Grant Focus:**
- Expand application volume based on initial feedback
- Cultivate long-term funder relationships
- Report on successes to build credibility

**Research Focus:**
- Analyze evaluation data for annual report
- Conduct "lessons learned" review
- Update research on emerging trends and best practices

## Key Success Factors

1. **Alignment:** Ensure financial, grant, and research strategies are aligned with your mission.
2. **Consistency:** Maintain consistent messaging and data across all documents.
3. **Transparency:** Be open and honest with funders, board, and community.
4. **Adaptability:** Be willing to adjust your plan based on feedback and results.
5. **Persistence:** Grant seeking is a long-term process; stay committed.

## Next Steps
1. Review the detailed Financial, Grant, and Research plans provided.
2. Convene your board or leadership team to discuss this roadmap.
3. Assign responsibilities for key tasks in Phase 1.
4. Set a regular meeting schedule to review progress.

---
*Generated by MAI Advisor MCP - Orchestrating Success for Non-Profits*
""" + f"""
        
---

# ⚡ CRASH COURSE FINAL PLAN: The "Get It Done" Summary

Okay, you read all that "strategic framework" stuff above? Great. Now here is the cheat sheet for the person who has to actually write this thing tonight.

## The 3-Sentence Pitch
1.  **The Problem:** "{topic} in {location} is a disaster/opportunity waiting to happen, and nobody is fixing it like we are."
2.  **The Solution:** "We are going to [specific action] using [specific method] to help [specific number] people immediately."
3.  **The Ask:** "Give us the money so we can stop fundraising and start working."

## The "Don't Forget" List
*   **Budget:** Did you pay yourself? (Seriously, put in a salary line).
*   **Letters of Support:** Call that one board member who knows the mayor.
*   **Formatting:** Use bold text. Skimmers are your audience.
*   **Submit Button:** It crashes at 4:59 PM. Submit at 4:00 PM.

**Go make magic.**
"""

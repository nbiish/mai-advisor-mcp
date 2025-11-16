"""
MAI Advisor - Gradio App with Exact Workflow
Workflow: topic/location → orchestrator → 3 search engines → experts → final plan
"""
import gradio as gr
from pathlib import Path
from datetime import datetime
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from dork_generator import GrantDorkGenerator
from output_manager import output_manager


# ============================================================================
# SIMULATED AI FUNCTIONS (Replace with real Gemini/Perplexity calls)
# ============================================================================

def simulate_expert_plan(expert_name: str, topic: str, location: str = "") -> str:
    """
    Simulate expert generating strategic plan (max 2700 tokens).
    In production, this would call Gemini/Perplexity API.
    
    Focus: Strategic guidance for small non-profit operations.
    No specific dollar amounts - provide frameworks and proven processes.
    """
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    templates = {
        "financial": f"""# Financial Management Strategic Framework
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

**Financial Health Indicators Small Non-Profits Should Track:**
- Months of operating reserves available
- Percentage of budget from diverse sources
- Grant reporting compliance rate (target: 100%)
- Budget-to-actual variance (target: <10%)
- Program cost per participant served

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

### Board Finance Committee Role
**Monthly Responsibilities:**
- Review financial statements and variance reports
- Monitor cash flow projections
- Ensure compliance with grant restrictions
- Flag risks to leadership early

**Annual Strategic Planning:**
- Develop annual budget with realistic revenue projections
- Assess reserve adequacy
- Review and update financial policies
- Plan for sustainability beyond current grants

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

**Sustainability Beyond Grant Period:**
- Articulate 2-3 year financial sustainability plan
- Show diversified funding strategy
- Demonstrate community investment (volunteers, in-kind, partners)
- Realistic earned revenue or fee-for-service plans

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

### Budget Narrative Best Practices
- Justify every line item with clear reasoning
- Show how costs are calculated (unit cost × quantity)
- Explain any items that might raise questions
- Demonstrate cost-effectiveness and efficiency
- Reference community wage data for personnel
- Highlight cost-sharing or matching contributions

## Financial Reporting & Compliance

### Grant Reporting Timeline Management
**Create a Master Calendar:**
- List all grant reporting deadlines
- Set internal deadlines 2 weeks before due dates
- Assign responsibility for each report
- Track submission and funder acknowledgment

**Financial Report Components:**
- Budget-to-actual comparison with variance explanations
- Narrative on budget modifications if any
- Documentation of match or in-kind contributions
- Photos, testimonials, or outcome data supporting expenditures

**Common Small Organization Challenges:**
- Late reporting (damages funder relationships)
- Incomplete backup documentation
- Confusion about allowable expenses
- Poor communication about budget modifications

**Solutions:**
- Calendar automation and team notifications
- File organization system for receipts and documentation
- Read grant agreements carefully; ask questions early
- Submit modification requests proactively, not retroactively

## Risk Management Strategies

### Financial Risks Small Organizations Face
1. **Grant Payment Delays:**
   - Mitigation: Request advance or quarterly payments
   - Maintain line of credit for cash flow gaps
   - Build 30-60 day operating reserves
   - Communicate with funders about reimbursement timeline

2. **Underfunding of Indirect Costs:**
   - Mitigation: Develop federally-approved indirect cost rate
   - Advocate with funders for adequate overhead support
   - Seek general operating support grants
   - Build fundraising for unrestricted funds

3. **Staff Turnover Mid-Grant:**
   - Mitigation: Document all processes and procedures
   - Cross-train team members
   - Budget for recruitment and onboarding
   - Maintain good funder communication

4. **Scope Creep Without Additional Funding:**
   - Mitigation: Clear program design and boundaries
   - Written partnership agreements
   - Regular program review against original scope
   - Learn to say "no" to mission drift

### Contingency Planning
- Identify which expenses could be reduced quickly if needed
- Maintain list of potential bridge funding sources
- Build relationships before you need emergency help
- Have board-approved plan for financial stress scenarios

## Key Recommendations for Small Non-Profit Financial Management

1. **Invest in Systems Early:**
   - Cloud accounting software
   - Time-tracking for grant compliance
   - Document management system
   - Board portal for financial transparency

2. **Build Financial Literacy Across Team:**
   - Regular all-staff budget updates
   - Board training on non-profit finances
   - Program staff understand budget connection to their work
   - Development staff can speak intelligently about finances

3. **Relationship-Based Financial Management:**
   - Communicate proactively with funders about challenges
   - Submit modification requests when needed, not at end of grant
   - Build trust through transparency and compliance
   - Ask program officers for guidance on allowable expenses

4. **Plan for Growth:**
   - Financial systems that can scale
   - Budget templates that work across multiple funders
   - Progressive steps toward audit-readiness
   - Board development to include financial expertise

5. **Sustainability Focus:**
   - Every grant should move you toward sustainability, not dependence
   - Use grants to build capacity (systems, staff, reputation)
   - Develop community ownership and investment
   - Plan exit strategies even as you're starting

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

### Post-Award Financial Management
- [ ] Grant agreement thoroughly reviewed
- [ ] Accounting system set up for grant tracking
- [ ] Reporting calendar created with reminders
- [ ] Staff trained on allowable expenses
- [ ] File organization system in place
- [ ] Backup documentation process established

---

*This framework is designed for small non-profit operations building financial sustainability through grants while maintaining funder confidence and regulatory compliance.*
""",
        
        "grant": f"""# Grant Strategy & Proposal Development Framework
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

### Opportunity Screening Checklist
Before investing 15-20 hours in an application, verify:
- [ ] Your organization meets all eligibility requirements
- [ ] You can meet match/cost-share obligations
- [ ] Timeline aligns with your program readiness
- [ ] Reporting requirements are manageable with current capacity
- [ ] You have capacity to apply while managing existing grants
- [ ] Mission alignment is authentic, not forced

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

**Funder Research & Relationship Building:**
- Identify 25-30 potential funders across multiple types
- Attend funder information sessions and office hours
- Schedule informational interviews (not to ask for money)
- Subscribe to grant opportunity newsletters
- Join local grantmakers association events

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

### Addressing Small Organization Concerns Proactively

**Limited Track Record:**
- Emphasize team experience even if organization is new
- Partner with established organizations for credibility
- Start with smaller pilot grants to build history
- Highlight community need and support even if org is young

**Capacity Questions:**
- Be honest about current capacity
- Show plan for building capacity with grant support
- Demonstrate board governance and oversight
- Use fiscal sponsors if needed for first grants

**Sustainability Concerns:**
- Articulate plan beyond grant period (even if it's seeking more grants)
- Show community investment (volunteers, in-kind, partnerships)
- Develop earned revenue components where feasible
- Build multi-year funding relationships, not one-off grants

## Grant Proposal Narrative Development

### Writing Strategy for Small Organizations

**The "Goldilocks" Approach to Proposals:**
- Not too corporate (avoid jargon, stay authentic)
- Not too informal (maintain professionalism)
- Just right (clear, compelling, evidence-based with community voice)

### Core Narrative Components with Small Org Focus

**1. Need Statement (15-20% of proposal)**

*What to include:*
- Quantitative data about community need
- Qualitative stories that bring data to life
- Gap analysis: What's missing in current services?
- Geographic/population specificity
- Why this need matters now

*Small org advantage:*
- You know the community intimately
- You can provide specific, local data vs. national statistics
- Your stories are authentic, not manufactured

*Common mistakes:*
- Only national statistics without local connection
- Describing your organization instead of community need
- Assuming everyone understands why this matters
- Too much description, not enough analysis

**2. Program Design (30-35% of proposal)**

*What to include:*
- Clear activities with timeline
- Theory of change or logic model
- Staffing plan with realistic capacity
- Partner roles and commitments
- Cultural competency and community voice
- Adaptations for specific population needs

*Small org advantage:*
- Flexibility to be truly community-driven
- Direct service delivery (no layers of bureaucracy)
- Innovation without corporate constraints
- Authentic partnerships, not transactional

*Common mistakes:*
- Vague activities without clear implementation plan
- Overpromising what small team can deliver
- Copying program design from another organization
- No clear timeline or phasing

**3. Outcomes & Evaluation (20-25% of proposal)**

*What to include:*
- SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound)
- Data collection methods appropriate to your capacity
- Mix of quantitative and qualitative measures
- How you'll use data for continuous improvement
- Third-party evaluation if required/budgeted

*Small org advantage:*
- Close relationships with participants enable authentic feedback
- Can gather stories and testimonials naturally
- Rapid iteration based on what you learn

*Common mistakes:*
- Goals that aren't measurable
- Evaluation plan beyond your actual capacity
- Only tracking outputs (participants served) not outcomes (change created)
- Expensive evaluation that takes money from programs

**4. Organizational Capacity (15-20% of proposal)**

*What to include:*
- Leadership team experience (even if org is new, people aren't)
- Board composition and governance
- Financial management systems
- Past performance (or team's past performance)
- Quality assurance and oversight

*Small org advantage:*
- Direct leadership involvement in program
- Board members actively engaged (not just names)
- Personal accountability and mission-driven

*Addressing capacity concerns:*
- Fiscal sponsor arrangement if needed
- Technical assistance partnerships
- Board development plan
- Honest about growing capacity with grant support

**5. Budget & Budget Narrative (10-15% of proposal)**

*What to include:*
- Line-item budget matching all activities
- Budget narrative justifying every expense
- Cost-sharing or matching contributions clearly identified
- Sustainability plan beyond grant
- Reasonable indirect costs

*Small org considerations:*
- Shared staff allocations must be clearly documented
- In-kind contributions properly valued
- Don't underprice to seem competitive—value your work
- Show how grant builds capacity, not just sustains it

## Proposal Development Workflow

### Efficient Process for Small Staff

**Week 1: Foundation**
- Read RFP/guidelines thoroughly
- Attend technical assistance webinar if offered
- Gather all required attachments
- Create outline mapping to funder priorities

**Week 2: First Draft**
- Write need statement and program design
- Develop logic model or theory of change
- Draft budget aligned with activities
- Identify data sources for evaluation

**Week 3: Refinement**
- Write evaluation and organizational capacity sections
- Complete budget narrative
- Get internal review from colleague
- Draft executive summary/abstract (write last)

**Week 4: Final Review**
- External reviewer (board member, trusted partner)
- Compliance check: Did we answer every question?
- Attachment organization and naming
- Submit 48 hours before deadline (not last minute)

### Building a Proposal Library

**Core Modules to Develop (Reusable across proposals):**
- Organizational history and mission (200-300 words)
- Board list with affiliations
- Financial management description
- Evaluation approach and tools
- Sample partnership letters
- Team bios with relevant experience
- Community needs data (updated annually)

**Customization Strategy:**
- Never copy-paste entire proposal
- Customize to each funder's priorities and language
- Update data and examples
- Ensure logic flows smoothly (not patchwork)

## Funder Relationship Development

### Beyond Transactional Applications

**Pre-Application Engagement:**
- Attend funder information sessions
- Request informational interviews (not pitch meetings)
- Ask thoughtful questions about priorities
- Share your learning, not just your needs
- Connect funders to community voices

**During Application Process:**
- Submit letter of inquiry before full proposal if allowed
- Ask clarifying questions if RFP is unclear
- Respect submission deadlines (early is professional)
- Follow formatting and length requirements exactly

**Post-Decision (Whether Funded or Not):**
- Thank funders for consideration
- Request feedback on declined applications
- Share learning from funded work
- Invite funders to see programs firsthand
- Consistent communication, not just when asking for money

**Stewardship Best Practices:**
- Report on time, every time
- Share successes and challenges honestly
- Credit funders appropriately (ask about recognition preferences)
- Involve funders in learning, not just compliance
- Build multi-year relationships, not one-off transactions

## Common Small Organization Grant Challenges & Solutions

### Challenge 1: Limited Time for Grant Writing
**Solutions:**
- Focus on fewer, better-fit opportunities
- Build proposal library to reduce redundancy
- Train program staff to contribute to narrative
- Consider part-time grant writer or consultant for major opportunities
- Join peer learning groups to share resources

### Challenge 2: Lack of Track Record
**Solutions:**
- Emphasize team experience over organizational history
- Start with smaller "proof of concept" grants
- Partner with established organization as fiscal sponsor
- Gather strong letters of support from community
- Document community need thoroughly

### Challenge 3: Weak Evaluation Capacity
**Solutions:**
- Partner with local university for evaluation support
- Use validated tools (don't create from scratch)
- Budget for evaluation consultant if needed
- Start simple and build over time
- Focus on most meaningful outcomes, not everything

### Challenge 4: Grant Application Rejected
**Solutions:**
- Request reviewer feedback
- Identify patterns across multiple rejections
- Revise and resubmit to other funders
- Build relationship for next year's funding cycle
- Use feedback to strengthen organizational capacity

### Challenge 5: Can't Meet Match Requirements
**Solutions:**
- In-kind contributions (volunteer time, donated space)
- Partner contributions
- Other grant funding (if allowed)
- Board giving and fundraising
- Earned revenue from programs

## Key Recommendations for Small Non-Profit Grant Success

1. **Quality Over Quantity:**
   - Better to submit 10 strong applications than 25 rushed ones
   - Focus on best-fit opportunities where mission aligns authentically
   - Build relationships, not just submit applications

2. **Invest in Relationships:**
   - Funder relationships are long-term investments
   - Program officers are allies, not adversaries
   - Transparency builds trust more than perfection

3. **Build Reusable Systems:**
   - Proposal library saves time and ensures consistency
   - Grant calendar prevents last-minute scrambles
   - Reporting templates make compliance easier

4. **Leverage Your Small-Organization Strengths:**
   - Community connection and authenticity
   - Flexibility and innovation
   - Direct accountability and mission focus

5. **Know When to Say No:**
   - Wrong-fit grants waste time and don't get funded
   - Mission drift damages organizational credibility
   - Capacity constraints are real—honor them

6. **Celebrate and Learn:**
   - Share wins with team and community
   - Analyze what works: Which approaches yield best results?
   - Build institutional knowledge, not just individual expertise

## Grant Success Checklist

### Before Submitting
- [ ] Reviewed by someone not involved in writing
- [ ] All questions in RFP addressed
- [ ] Budget matches narrative exactly
- [ ] All required attachments included
- [ ] Follows formatting requirements (length, font, margins)
- [ ] Submitted through correct portal/method
- [ ] Confirmation of receipt obtained

### After Submission
- [ ] Thank you sent to all contributors
- [ ] Logged in grant tracking system
- [ ] Follow-up communication planned
- [ ] Reporting deadlines calendared if funded
- [ ] Next steps identified regardless of outcome

---

*This framework is designed for small non-profit operations building sustainable grant funding through strategic, relationship-based approaches that honor organizational capacity while pursuing community impact.*
""",
        
        "research": f"""# Research & Evidence-Based Strategy Framework
**Generated:** {timestamp}  
**Topic:** {topic}  
**Location:** {location or "Not specified"}

## Executive Summary
This framework provides research methodologies and evidence-gathering strategies specifically designed for small non-profit operations developing {topic}. Focus is on leveraging existing data, demonstrating community need, and building evaluation capacity that funders value.

## Community Needs Assessment Framework

### Conducting Needs Assessment with Limited Resources

**Primary Data Collection (What You Gather Directly):**
- Community surveys (online tools: Google Forms, SurveyMonkey free tiers)
- Focus groups with target population (6-10 participants, 2-3 groups)
- Key informant interviews (community leaders, service providers)
- Community forums or listening sessions
- Photovoice or community mapping exercises

**Secondary Data Sources (Free/Low-Cost):**
- U.S. Census Bureau (American FactFinder, demographic data)
- County health rankings and roadmaps
- School district data (if education-focused)
- State/local government reports
- United Way community assessments
- Existing academic research

**Needs Assessment Questions to Answer:**
1. Who is the target population (demographics, geography)?
2. What specific needs exist (documented through data)?
3. What gaps exist in current services?
4. Why does this need matter now (urgency, trends)?
5. How did you involve community voice in identifying needs?

### Demonstrating Need Without Large-Scale Studies

**Small Organization Strategies:**
- Partner with local university for research support
- Leverage existing community assessments (don't duplicate)
- Combine quantitative data with compelling qualitative stories
- Use comparison data (national vs. local to show gap)
- Document waiting lists, referral patterns, community requests

**Common Mistakes:**
- Relying only on national statistics without local connection
- Describing your organization instead of community need
- Assuming everyone knows why this matters
- No community voice in needs identification

## Evidence-Based Practice Research

### Identifying Proven Models for Your Work

**Where to Find Evidence-Based Practices:**
- Federal clearinghouses (SAMHSA, What Works Clearinghouse, etc.)
- Academic databases (Google Scholar is free)
- Professional association best practice guides
- Peer organizations with evaluation data
- Technical assistance providers in your field

**Adapting Evidence-Based Models for Small Organizations:**
- Core components vs. optional enhancements
- Fidelity to model vs. community adaptation
- Resource requirements and scalability
- Training and technical assistance needs
- Cultural adaptation while maintaining effectiveness

**Documenting Your Approach:**
- Logic model showing theory of change
- How your approach aligns with evidence-based principles
- Adaptations made for your community context
- Plan for measuring fidelity and outcomes

### Building Your Own Evidence Base

**Even New Organizations Can:**
- Document program activities and participant engagement
- Track outputs (numbers served, hours of service)
- Gather participant feedback and satisfaction data
- Collect stories and testimonials
- Monitor short-term progress indicators

**Progressive Evaluation Strategy:**
- **Year 1:** Track participation, satisfaction, immediate outputs
- **Year 2:** Add outcome measurement with validated tools
- **Year 3:** Longer-term outcomes and impact assessment
- Ongoing: Use data for continuous improvement

## Competitive Landscape Analysis

### Understanding Your Service Environment

**Collaboration vs. Competition Framework:**
- Map existing services (who does what, for whom, where)
- Identify gaps (unserved populations, geographic areas, service types)
- Determine your niche (what makes you different/needed)
- Build partnerships rather than duplicate successful programs

**Questions to Research:**
1. What organizations provide similar services?
2. Who do they serve (and who do they NOT serve)?
3. What are their hours, locations, eligibility requirements?
4. Where are the waitlists or capacity constraints?
5. How can you complement rather than compete?

**Demonstrating Your Unique Value:**
- Population focus (cultural, linguistic, identity-specific)
- Geographic focus (neighborhood, rural area not covered)
- Service delivery approach (hours, location, format)
- Integration of services (wraparound, holistic)
- Community-driven governance and design

## Funder Landscape & Priorities Research

### Understanding What Funders Care About

**Federal Grant Trends (Research Before Applying):**
- Review previous year's abstracts of funded projects
- Attend bidders conferences and webinars
- Read agency strategic plans and priorities
- Join mailing lists for funding announcements
- Note match requirements and reporting expectations

**Foundation Research Strategies:**
- Use Foundation Directory Online (library access often free)
- Review foundation 990 tax forms (public record)
- Analyze foundation websites for stated priorities
- Identify recently funded similar projects
- Attend foundation information sessions

**What to Document:**
- Alignment between your mission and funder priorities
- Geographic restrictions (do you qualify?)
- Organization size and budget preferences
- Multi-year funding patterns
- Application deadlines and cycles

## Stakeholder Engagement & Community Voice

### Authentic Community Participation

**Meaningful Engagement vs. Tokenism:**
- Community members in leadership roles (board, advisory committee)
- Compensation for community expertise (stipends, gifts)
- Language accessibility and cultural responsiveness
- Multiple ways to participate (in-person, virtual, written)
- Act on community feedback (don't just collect it)

**Documenting Community Support:**
- Letters from community members (not just organizations)
- Results of community surveys or forums
- Photos and quotes from community events
- Partnership MOUs with community-based organizations
- Community advisory board meeting minutes

**Questions Funders Want Answered:**
1. Who designed this program (community-driven vs. imposed)?
2. How do you ensure cultural relevance and responsiveness?
3. What role do community members play in governance?
4. How will you be accountable to the community?

## Implementation Planning & Timeline Development

### Realistic Phasing for Small Organizations

**Pilot Before Scaling:**
- **Months 1-3:** Planning, partnership development, staff hiring
- **Months 4-6:** Pilot with small cohort, test and refine
- **Months 7-9:** Implement improvements from pilot learning
- **Months 10-12:** Document outcomes, plan for sustainability/scale

**Capacity-Appropriate Growth:**
- Don't over-promise what small staff can deliver
- Build in learning time and course correction
- Phase participant enrollment (don't flood capacity)
- Allow time for relationship-building (community, partners)

**Risk Identification & Mitigation:**

| Risk | Likelihood | Mitigation Strategy |
|------|------------|---------------------|
| Staff turnover | Medium-High | Cross-training, documentation, succession planning |
| Lower than expected enrollment | Medium | Multiple recruitment strategies, partnerships |
| Partnership challenges | Medium | Clear MOUs, regular communication, flexibility |
| Delayed grant funding | High | Build reserves, seek advance payments, line of credit |

## Data Collection & Evaluation Framework

### Evaluation Planning for Small Organizations

**Start Simple, Build Over Time:**
- Year 1: Participation data, satisfaction surveys
- Year 2: Add outcome measurement (pre/post)
- Year 3: Longer-term outcomes, comparison data

**Free or Low-Cost Evaluation Tools:**
- Validated instruments in public domain
- Partner with university graduate students
- Peer organization shared tools
- State or national association resources
- Funder-provided evaluation frameworks

**Data Collection Methods:**

**Quantitative:**
- Participation tracking (attendance, demographics)
- Pre/post surveys or assessments
- Program quality observation tools
- Administrative data (school records, health records with permission)

**Qualitative:**
- Participant interviews or focus groups
- Open-ended survey questions
- Staff and partner observations
- Success stories and case studies
- Photovoice or participant-generated documentation

### What to Measure (Outcomes, Not Just Outputs)

**Outputs (What You Do):**
- Number of participants served
- Hours of service delivered
- Materials distributed
- Events/workshops conducted

**Outcomes (Changes Created):**
- **Short-term (0-6 months):** Knowledge, attitudes, skills gained
- **Medium-term (6-18 months):** Behavior changes, goal progress
- **Long-term (1-3+ years):** Status improvements, systems change

**Impact (Community-Level Change):**
- Population-level indicators
- Systems or policy changes
- Community capacity development
- Cultural or norm shifts

### Evaluation Budget Guidance

**Typical Allocation:**
- 5-10% of program budget for evaluation
- Can include staff time, tools, external evaluator
- Build in from beginning (not afterthought)
- Scale to organizational capacity

**Small Organization Options:**
- In-house evaluation with validated tools
- University partnership (practicum student)
- Evaluation consultant for design, you implement
- Peer learning collaborative evaluation

## Research-to-Practice Translation

### Making Research Accessible and Actionable

**Literature Review Process for Non-Researchers:**
1. Identify 3-5 key search terms
2. Search Google Scholar, federal clearinghouses
3. Focus on meta-analyses and systematic reviews
4. Read abstracts first, then promising full articles
5. Extract key findings, limitations, implications

**Translating Research to Grant Proposals:**
- "Research shows [cite source]"
- "Evidence-based practices include [cite source]"
- "Our approach aligns with [theory/framework]"
- "Studies demonstrate [outcomes you expect]"

**Building Your Research Library:**
- Organize by topic in shared drive
- Create annotated bibliography
- Update annually with new research
- Share with board and staff for organizational learning

## Recommended Data & Research Tools for Small Non-Profits

### Free or Low-Cost Resources

**Demographic & Community Data:**
- Census.gov (American FactFinder)
- County Health Rankings
- Kids Count Data Center (Annie E. Casey Foundation)
- DataUSA.io
- State/local government open data portals

**Evidence-Based Practice Databases:**
- What Works Clearinghouse (education)
- SAMHSA Evidence-Based Practices Resource Center (behavioral health)
- Child Welfare Information Gateway (child/family services)
- The Community Guide (public health)

**Survey & Data Collection:**
- Google Forms (free)
- SurveyMonkey (limited free tier)
- Qualtrics (some orgs get free access)
- REDCap (free for research, some institutions)

**Data Analysis:**
- Excel or Google Sheets (basic analysis)
- JASP or PSPP (free statistics software)
- R or Python (free, steep learning curve)

**Evaluation Frameworks:**
- W.K. Kellogg Foundation Logic Model Guide
- CDC Framework for Program Evaluation
- PEAR (Performance Excellence in Action for Results)

## Key Recommendations for Small Non-Profit Research Strategy

1. **Leverage Existing Data:**
   - Don't reinvent the wheel—use published research
   - Partner with universities for research capacity
   - Access free government and foundation data sources

2. **Start Where You Are:**
   - Simple data collection is better than none
   - Build evaluation capacity progressively
   - Use validated tools rather than creating new ones

3. **Community Voice is Data:**
   - Qualitative data is powerful in grant proposals
   - Stories bring statistics to life
   - Participatory research builds authenticity

4. **Make Evaluation Useful, Not Just Required:**
   - Use data for continuous improvement
   - Share findings with community and funders
   - Build organizational learning culture

5. **Invest in Relationships:**
   - Local university partnerships
   - Peer organization collaboratives
   - Funder technical assistance opportunities

6. **Be Honest About Limitations:**
   - Small sample sizes
   - Limited comparison groups
   - Resource constraints
   - Plan for building capacity over time

## Research Strategy Checklist for Grant Applications

### Community Need Documentation
- [ ] Local demographic data from credible sources
- [ ] Service gap analysis (what's missing)
- [ ] Community voice in needs identification
- [ ] Trend data showing urgency
- [ ] Comparison to regional or national data

### Evidence-Base Documentation
- [ ] Reviewed relevant research literature
- [ ] Identified evidence-based practices
- [ ] Developed logic model or theory of change
- [ ] Documented how your approach aligns with evidence
- [ ] Planned for fidelity and adaptation

### Evaluation Planning
- [ ] Identified realistic outcomes to measure
- [ ] Selected appropriate data collection methods
- [ ] Chosen validated tools when available
- [ ] Planned evaluation budget (5-10% of program)
- [ ] Identified evaluation expertise (in-house or partner)

### Competitive Landscape
- [ ] Mapped existing service providers
- [ ] Identified your unique value proposition
- [ ] Documented gaps you will fill
- [ ] Planned for collaboration vs. competition

---

*This framework is designed for small non-profit operations building credible, evidence-based grant proposals that demonstrate community need, promising approaches, and commitment to learning and improvement.*
"""
    }
    
    return templates.get(expert_name, f"# {expert_name.title()} Expert Plan\n\n{topic}")


def simulate_orchestrator_synthesis(topic: str, location: str, expert_plans: list) -> str:
    """
    Simulate orchestrator synthesizing all expert plans into final grant plan.
    In production, this would use orchestration model to review all plans.
    
    Focus: Strategic synthesis for small non-profit operations.
    No specific dollar amounts - provide integrated framework.
    """
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    # Count words in expert plans
    total_words = sum(len(plan["content"].split()) for plan in expert_plans)
    
    final_plan = f"""# Comprehensive Grant Strategy & Implementation Framework
**Generated:** {timestamp}  
**Topic:** {topic}  
**Location:** {location or "Not specified"}  
**Synthesized from {len(expert_plans)} Expert Strategic Frameworks** ({total_words:,} words analyzed)

---

## Executive Summary

This integrated strategic framework synthesizes financial management, grant development, and research-based planning specifically for small non-profit operations pursuing **{topic}**. The framework focuses on building sustainable infrastructure, demonstrating community impact, and positioning for competitive grant success.

**Strategic Approach:**
- Evidence-based program design with community voice
- Diversified funding strategy building toward sustainability
- Rigorous evaluation demonstrating measurable outcomes
- Authentic partnerships leveraging collective capacity
- Progressive capacity building (systems that scale)

**Timeline:** 12-month implementation with phased milestones  
**Target Outcomes:** Measurable community impact with documented success for future funding

---

## I. Strategic Foundations

### Organizational Readiness Assessment

**Before Pursuing Grants, Ensure You Have:**

**Governance & Leadership:**
- [ ] Active board with community representation
- [ ] Board-approved annual budget and strategic plan
- [ ] Executive leadership with relevant experience
- [ ] Financial oversight and audit readiness
- [ ] Conflict of interest and key policies documented

**Financial Infrastructure:**
- [ ] Chart of accounts for program-based tracking
- [ ] Cloud-based accounting system in place
- [ ] Bank accounts and fiscal controls established
- [ ] Indirect cost methodology documented
- [ ] Grant financial management procedures written

**Program Readiness:**
- [ ] Logic model or theory of change developed
- [ ] Evidence-based approach identified
- [ ] Evaluation framework designed
- [ ] Community needs documented
- [ ] Cultural competency and accessibility planned

**Partnership Foundation:**
- [ ] Letters of support from authentic partners
- [ ] MOUs with key collaborators
- [ ] Community advisory structure in place
- [ ] Referral and coordination agreements established

### Mission Alignment Check

**Questions to Ask Before Each Grant Application:**
1. Does this opportunity truly align with our core mission?
2. Do we have capacity to deliver what we're proposing?
3. Can we meet match/cost-share requirements?
4. Are reporting requirements manageable for our staff?
5. Will this grant build capacity or create dependence?
6. Does the timeline align with our organizational readiness?

---

## II. Financial Management Framework

### Budget Development Strategy

**Cost Structure for Small Operations:**
- **Personnel (60-70%):** Core program and administrative staff
- **Operations (20-30%):** Facilities, technology, insurance, compliance
- **Program Delivery (10-20%):** Materials, supplies, participant support

**Key Principles:**
- Build budgets from activities, not arbitrary percentages
- Include true costs (don't underprice to seem competitive)
- Document all cost allocation methodologies
- Plan for indirect costs (10-15% typical for small orgs)
- Show in-kind and matching contributions clearly

### Multi-Source Revenue Diversification

**Strategic Funding Mix:**
- **Primary (60-70%):** Competitive grants (federal, state, foundation)
- **Secondary (20-30%):** Earned revenue, fees-for-service, partnerships
- **Tertiary (10-20%):** Individual giving, special events, corporate support

**Risk Mitigation:**
- No single funding source exceeds 40% of annual budget
- Multi-year grants provide stability
- Unrestricted funding supports infrastructure
- Operating reserves build financial cushion

### Operating Reserve Strategy

**Progressive Reserve Building:**
- **Year 1 Target:** 1-month operating expenses
- **Year 2 Target:** 2-3 months operating expenses
- **Year 3 Target:** 3-6 months operating expenses (financial stability)

**Reserve Use Guidelines:**
- Bridge timing gaps between grant payments
- Cover unexpected expenses or revenue shortfalls
- Support capacity investments (not ongoing operations)
- Provide runway for strategic planning

### Financial Reporting & Compliance Systems

**Essential Infrastructure:**
- Grant-specific accounting codes in chart of accounts
- Time-tracking for staff working across multiple grants
- File organization for receipts and backup documentation
- Reporting calendar with advance reminders (2+ weeks)
- Variance analysis process for budget-to-actual review

**Board Finance Committee Role:**
- Monthly financial review and variance analysis
- Quarterly cash flow projections
- Annual budget development and reserve assessment
- Policy review and risk management oversight

---

## III. Grant Acquisition Strategy

### 12-Month Grant Calendar

**Phase 1: Preparation (Months 1-3)**
*Foundation before applying*

**Organizational Capacity:**
- Finalize program design with clear logic model
- Gather authentic letters of support (5-10 partners)
- Develop evaluation framework with realistic measures
- Complete community needs assessment
- Update organizational documents (budget, board list, 990, etc.)

**Funder Research & Cultivation:**
- Identify 25-30 potential funders across types (federal, state, foundation, corporate)
- Attend funder information sessions and office hours
- Schedule informational interviews (relationship-building, not pitching)
- Join grantmaker association events and mailing lists
- Review funded project abstracts to understand funder priorities

**Proposal Development:**
- Create modular proposal library (reusable components)
- Develop core narratives (organizational overview, need statement, evaluation approach)
- Build team bios and organizational capacity descriptions
- Compile community data and evidence base research

**Phase 2: Strategic Application Wave (Months 4-6)**
*Best-fit opportunities first*

- Submit 2-3 foundation applications (where you have relationship)
- Submit 1-2 federal/state applications (longer timelines)
- Follow up appropriately on letters of inquiry
- Request feedback on any declinations
- Adjust approach based on learning

**Phase 3: Momentum Building (Months 7-9)**
*Leverage early wins and feedback*

- Submit 3-4 additional applications
- Update proposal library based on reviewer feedback
- Begin reporting on any funded grants (critical credibility)
- Cultivate program officer relationships
- Present at community forums to demonstrate expertise

**Phase 4: Sustainability Planning (Months 10-12)**
*Position for Year 2 and beyond*

- Submit final applications for current cycle
- Conduct stewardship with all funders (funded and declined)
- Analyze success patterns: What worked? Where did we succeed?
- Plan Year 2 grant calendar with multi-year renewal focus
- Build board and community fundraising capacity

### Competitive Positioning for Small Organizations

**Leverage Your Unique Strengths:**
- **Community authenticity:** Deep local knowledge and trusted relationships
- **Nimbleness:** Quick adaptation to community needs and feedback
- **Innovation:** Pilot new approaches without bureaucratic constraints
- **Direct accountability:** Leadership connected to daily program delivery

**Address Capacity Concerns Proactively:**
- Honest about current capacity with plan for growth
- Fiscal sponsor partnership if needed for credibility
- Technical assistance and peer learning investments
- Board development and governance strengthening

**Collaboration Over Competition:**
- Partner with established organizations for credibility
- Fill gaps rather than duplicate successful programs
- Build collective impact through authentic partnerships
- Share credit and learning across sector

### Grant Proposal Development Workflow

**Efficient Process for Small Staff (4-Week Timeline):**

**Week 1: Foundation**
- Read RFP thoroughly, attend TA webinar if offered
- Create outline mapping to funder priorities
- Gather required attachments and documents
- Review past successful proposals (yours or peers)

**Week 2: First Draft**
- Write need statement grounded in local data
- Develop program design narrative with clear activities
- Draft budget aligned with all proposed activities
- Create logic model or theory of change visual

**Week 3: Refinement**
- Complete evaluation and organizational capacity sections
- Write detailed budget narrative justifying every line
- Draft executive summary (write last, summarizes everything)
- Internal review by colleague for clarity and completeness

**Week 4: Final Polish**
- External review by board member or trusted partner
- Compliance check: Every question answered? All requirements met?
- Proofread for typos, formatting, professional presentation
- Submit 48+ hours before deadline (technology issues happen)

### Proposal Narrative Components

**1. Community Need & Context (15-20% of proposal)**
- Local data demonstrating specific need
- Qualitative stories bringing statistics to life
- Gap analysis: What's currently missing?
- Community voice in needs identification
- Why this matters now (urgency, trends)

**2. Program Design & Implementation (30-35% of proposal)**
- Clear activities with realistic timeline
- Logic model showing inputs → activities → outputs → outcomes
- Staffing plan appropriate to capacity
- Partner roles with documented commitments
- Cultural competency and accessibility approach
- Quality assurance and continuous improvement

**3. Evaluation & Outcomes (20-25% of proposal)**
- SMART goals aligned with funder priorities
- Mix of quantitative and qualitative measures
- Data collection methods realistic for capacity
- Plan for using data to improve (not just report)
- Third-party evaluation if required/budgeted

**4. Organizational Capacity (15-20% of proposal)**
- Leadership team experience and qualifications
- Board composition, governance, financial oversight
- Financial management systems and controls
- Past performance or relevant track record
- Quality standards and accountability mechanisms

**5. Budget & Sustainability (10-15% of proposal)**
- Line-item budget matching all narrative activities
- Budget narrative justifying calculations
- Cost-sharing or match clearly identified
- Sustainability plan beyond grant period
- Reasonable indirect costs with methodology

---

## IV. Research & Evidence Base

### Community Needs Documentation

**Data Collection Strategies for Small Organizations:**

**Primary Sources (What You Gather):**
- Community surveys (Google Forms, SurveyMonkey free)
- Focus groups with target population (6-10 participants, 2-3 groups)
- Key informant interviews (service providers, community leaders)
- Community forums and listening sessions
- Photovoice or community mapping

**Secondary Sources (Free/Low-Cost):**
- U.S. Census Bureau demographic data
- County health rankings and community assessments
- School district data (if education-focused)
- State/local government reports
- Existing academic research and published studies

**Demonstrating Need Effectively:**
- Combine quantitative data with compelling qualitative stories
- Local data more powerful than only national statistics
- Show gap between need and current service capacity
- Document community voice and participation in assessment
- Trend data showing why this matters now

### Evidence-Based Practice Integration

**Finding Relevant Research:**
- Federal clearinghouses (SAMHSA, What Works Clearinghouse)
- Google Scholar for academic literature (free)
- Professional association best practice guides
- Peer organizations with published evaluations
- Technical assistance provider resources

**Adapting to Your Context:**
- Core components vs. optional enhancements
- Fidelity to model while allowing community adaptation
- Resource requirements and scalability for small orgs
- Cultural adaptation maintaining effectiveness

**Building Your Evidence Library:**
- Logic model showing theory of change
- Alignment with evidence-based principles
- Documentation of adaptations made
- Plan for measuring fidelity and outcomes

### Evaluation Framework Development

**Progressive Evaluation Strategy:**
- **Year 1:** Participation tracking, satisfaction, immediate outputs
- **Year 2:** Add outcome measurement with validated tools
- **Year 3:** Longer-term outcomes and impact assessment
- Ongoing: Data-driven continuous improvement

**Measurement Approach:**

**Outputs (What You Do):**
- Participants served (demographics)
- Hours/sessions delivered
- Materials distributed
- Events/workshops conducted

**Outcomes (Change Created):**
- Short-term (0-6 months): Knowledge, attitudes, skills
- Medium-term (6-18 months): Behaviors, goal progress
- Long-term (1-3+ years): Status changes, community impact

**Free/Low-Cost Evaluation Tools:**
- Validated instruments in public domain
- University graduate student partnerships
- Peer organization shared tools
- State/national association resources
- Funder-provided frameworks

---

## V. Partnership & Collaboration Strategy

### Strategic Partnership Development

**Types of Partnerships:**
- **Referral partnerships:** Exchange participants/clients
- **Co-location partnerships:** Shared space reducing costs
- **Service integration:** Wraparound support for participants
- **Capacity building:** Shared training, back-office, evaluation
- **Advocacy partnerships:** Collective voice for systems change

**Partnership Best Practices:**
- Written MOUs clarifying roles, responsibilities, resources
- Regular communication (monthly meetings minimum)
- Shared data and learning (with proper privacy protocols)
- Joint funding applications when appropriate
- Credit sharing and mutual benefit

### Community Engagement Framework

**Authentic Participation vs. Tokenism:**
- Community members in leadership roles (board, advisory)
- Compensation for community expertise (stipends, honoraria)
- Language accessibility and cultural responsiveness
- Multiple engagement methods (in-person, virtual, written)
- Action on feedback (don't just collect input)

**Documenting Community Voice:**
- Letters from community members (not just organizations)
- Community survey/forum results
- Photos and quotes from engagement events
- Partnership MOUs with community-based groups
- Advisory board meeting documentation

---

## VI. Implementation Timeline

### Year 1: Foundation & Proof of Concept

**Months 1-3: Planning & Preparation**
- Finalize program design based on community input
- Hire key staff (Executive Director, Program Coordinator)
- Establish partnerships through MOUs
- Set up financial and data systems
- Submit first grant applications

**Months 4-6: Pilot Launch**
- Recruit initial participant cohort (start small)
- Deliver programming with close attention to quality
- Implement evaluation and data collection
- Adjust based on real-time feedback
- Submit additional grant applications

**Months 7-9: Refinement & Documentation**
- Analyze pilot data and participant feedback
- Refine program model based on learning
- Document success stories and early outcomes
- Expand participant enrollment
- Begin grant reporting for funded projects

**Months 10-12: Evaluation & Planning**
- Complete Year 1 evaluation and outcomes documentation
- Prepare funder reports highlighting impact
- Plan Year 2 with expansion strategy
- Steward funder relationships for renewals
- Celebrate wins with community and stakeholders

### Phased Growth Strategy

**Year 1: Prove the Model**
- Small-scale implementation with strong quality
- Rigorous data collection and documentation
- Build community trust and credibility
- Secure initial funding portfolio

**Year 2: Strengthen & Expand**
- Scale to additional sites or populations
- Add staff capacity strategically
- Develop earned revenue streams
- Pursue multi-year grant renewals

**Year 3: Sustainability & Leadership**
- Achieve financial sustainability (diverse funding)
- Regional expansion or replication
- Thought leadership (publications, presentations)
- Technical assistance to peer organizations

---

## VII. Risk Management

### Common Risks & Mitigation Strategies

**Financial Risks:**
- **Grant payment delays:** Build reserves, request advance payments, line of credit
- **Underfunded overhead:** Develop indirect cost rate, seek unrestricted funding
- **Staff turnover:** Competitive compensation, professional development, succession planning
- **Scope creep:** Clear boundaries, written agreements, regular scope review

**Programmatic Risks:**
- **Low enrollment:** Multiple recruitment strategies, partnerships, accessibility
- **Participant retention:** Engagement strategies, transportation, incentives
- **Partnership challenges:** Clear MOUs, regular communication, conflict resolution
- **Quality concerns:** Staff training, supervision, fidelity monitoring

**External Risks:**
- **Funding environment changes:** Diversification, relationship building, flexibility
- **Community needs shifts:** Advisory board input, ongoing needs assessment
- **Competition:** Unique positioning, collaboration focus, complementary services
- **Leadership transition:** Succession planning, cross-training, documentation

### Contingency Planning

**Have Board-Approved Plans For:**
- Expense reduction if revenue falls short
- Bridge funding sources for emergencies
- Critical vs. discretionary spending priorities
- Communication protocols during financial stress

---

## VIII. Success Metrics & Accountability

### Organizational Effectiveness Indicators

**Financial Health:**
- Months of operating reserves available
- Percentage of budget from diverse sources (no source >40%)
- Grant reporting compliance rate (target: 100%)
- Budget-to-actual variance (target: <10%)
- Cost per participant/outcome

**Programmatic Quality:**
- Participant retention rates (target: 70%+)
- Participant satisfaction (target: 85%+)
- Outcome achievement rates (target: 70%+)
- Partner satisfaction and collaboration strength
- Fidelity to evidence-based model

**Grant Development Success:**
- Applications submitted per year (target: 10-15 for small orgs)
- Success rate (target: 25-35%)
- Relationships with program officers (target: 10+)
- Proposal library modules developed (target: 5-7)
- On-time submission rate (target: 100%)

**Community Impact:**
- Documented changes in participants' lives
- Community-level indicators (when applicable)
- Systems or policy changes influenced
- Reputation and community trust

### Learning & Adaptation

**Continuous Improvement Practices:**
- Quarterly program review with data analysis
- Staff debriefs after major milestones
- Participant feedback loops
- Partner collaboration meetings
- Board learning sessions

**Knowledge Management:**
- Document processes and lessons learned
- Share findings through reports and presentations
- Contribute to field knowledge
- Build organizational memory (not dependent on individuals)

---

## IX. Sustainability Strategy

### Beyond Grant Dependence

**Multi-Year Sustainability Plan:**

**Year 1 Focus: Build Foundation**
- Prove program model with strong outcomes
- Document impact rigorously
- Build funder and community relationships
- Secure initial grant funding portfolio

**Year 2 Focus: Diversify & Strengthen**
- Add 2-3 new funding sources
- Develop earned revenue components
- Pursue multi-year grant renewals
- Strengthen board fundraising capacity

**Year 3 Focus: Long-Term Viability**
- Achieve 50%+ funding from diverse sources
- Build significant operating reserves (3-6 months)
- Establish fee-for-service or social enterprise
- Create endowment or planned giving program

### Earned Revenue Development

**Appropriate Models for Non-Profits:**
- Fee-for-service (sliding scale for accessibility)
- Training and technical assistance to other organizations
- Consulting based on your expertise
- Social enterprise aligned with mission
- Contract services to government or larger organizations

**Key Principles:**
- Mission-aligned (not distraction)
- Community-accessible (not excluding those who can't pay)
- Scalable (can grow without excessive new costs)
- Complements grants (doesn't compete for staff time)

---

## X. Next Steps & Action Plan

### Immediate Priorities (Months 1-3)

**Organizational Readiness:**
- [ ] Convene planning team (staff, board, community advisors)
- [ ] Finalize program design and logic model
- [ ] Complete community needs assessment
- [ ] Gather letters of support from partners
- [ ] Update all organizational documents

**Financial Infrastructure:**
- [ ] Set up grant-ready accounting system
- [ ] Develop budget templates and cost allocation methods
- [ ] Create financial policies and procedures manual
- [ ] Establish internal controls and oversight
- [ ] Calculate indirect cost rate

**Grant Development:**
- [ ] Research and prioritize 25-30 potential funders
- [ ] Develop proposal library core modules
- [ ] Create grant calendar for 12-month cycle
- [ ] Attend funder information sessions
- [ ] Submit first 2-3 grant applications

**Evaluation Planning:**
- [ ] Select validated outcome measurement tools
- [ ] Design data collection systems and workflows
- [ ] Train staff on evaluation procedures
- [ ] Establish baseline data collection
- [ ] Partner with evaluator if needed

### Long-Term Success Factors

**Critical Elements for Sustainability:**
1. **Mission-Driven:** Stay true to purpose, resist mission drift
2. **Community-Centered:** Authentic partnerships and accountability
3. **Evidence-Based:** Ground work in research and continuous learning
4. **Financially Sound:** Diversified funding, reserves, transparent management
5. **Adaptive:** Responsive to feedback and changing conditions
6. **Collaborative:** Build with others, share credit and learning

**Building Blocks of Organizational Capacity:**
- Strong governance with engaged board
- Competent staff with professional development
- Effective financial management systems
- Robust partnerships and community relationships
- Data-driven decision making and quality improvement
- Strategic planning and risk management

---

## Conclusion

This comprehensive framework synthesizes financial management, grant development, and evidence-based planning specifically for small non-profit operations. Success in grant funding requires more than just writing skills—it demands organizational readiness, authentic community partnerships, rigorous evaluation, and sustainable infrastructure.

**Key Takeaways:**

1. **Start with readiness:** Build systems before pursuing major grants
2. **Focus on relationships:** Funders invest in people and trust, not just programs
3. **Prove your model:** Start small, document well, scale with evidence
4. **Diversify strategically:** Multiple funding sources reduce risk
5. **Stay community-centered:** Authentic partnerships are your competitive advantage
6. **Be honest about capacity:** Better to do fewer things well than many things poorly
7. **Use data for learning:** Evaluation drives improvement, not just compliance
8. **Build to last:** Every grant should strengthen capacity, not create dependence

**Remember:** Small organizations have unique strengths—community connection, flexibility, innovation, direct accountability. Leverage these advantages while building the infrastructure that funders require. Your impact matters, and with strategic planning, you can secure the resources to achieve your mission sustainably.

---

**Implementation Timeline:** Begin with immediate priorities, build progressively, stay focused on mission  
**Evaluation:** Track metrics quarterly, adjust strategy based on data  
**Sustainability:** Multi-year plan moving from grant dependence to diversified stability  

**Expert Framework Sources:**
- Financial Management Strategic Framework
- Grant Strategy & Proposal Development Framework  
- Research & Evidence-Based Strategy Framework

---

*This strategic framework is designed to guide small non-profit operations from initial grant readiness through sustainable growth, with emphasis on community-centered approaches, evidence-based practices, and authentic impact.*
"""
    
    return final_plan


def generate_ai_agent_todo(topic: str, location: str, dorks: dict) -> str:
    """
    Generate AI browser agent instructions for finding grants and helping users complete applications.
    
    Creates actionable, step-by-step instructions for advanced AI agents (2027+) with browser
    capabilities to discover grants, analyze opportunities, and guide users through application completion.
    
    Args:
        topic: Grant topic/focus area
        location: Geographic location (optional)
        dorks: Dictionary with google, bing, duckduckgo search queries
        
    Returns:
        Markdown content with step-by-step AI agent instructions
    """
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    ai_todo = f"""# AI Browser Agent Task List: Grant Application Assistant
**Generated:** {timestamp}  
**Topic:** {topic}  
**Location:** {location or "Not specified"}  
**Agent Capability Required:** Browser tools, form filling, document analysis, web navigation

---

## PRIMARY MISSION

You are an AI agent helping a small non-profit organization discover relevant grants and **complete their applications**. This is not just research—you will actively guide the user through filling out applications, uploading documents, and submitting proposals.

**Success = Submitted grant applications, not just a list of opportunities.**

---

## PHASE 1: GRANT DISCOVERY

### Task 1.1: Execute Search Dorks

**Action:** Use your browser to search each engine with optimized queries.

**Google Search:**
```
{dorks.get('google', 'grants + ' + topic)}
```

**Bing Search:**
```
{dorks.get('bing', 'grants ' + topic)}
```

**DuckDuckGo Search:**
```
{dorks.get('duckduckgo', 'grants ' + topic)}
```

**Execution Steps:**
1. Open browser to each search engine
2. Enter search dork exactly as provided
3. Extract first 30 results from each
4. Click through to verify grant is still open
5. Extract: Deadline, award amount, eligibility, application link
6. Add to tracking database with status: "DISCOVERED"

**Output:** CSV file with columns: [Funder, Program, Deadline, Award_Range, Application_URL, Status]

---

### Task 1.2: Visit Major Grant Databases

**Action:** Navigate to foundation databases and extract open opportunities.

**Sites to visit:**
1. **Grants.gov** (https://www.grants.gov)
   - Filter: Non-profit eligible
   - Filter: Posted last 60 days
   - Filter: Keyword = "{topic}"
   - Extract: All matching opportunities
   - Download: Opportunity synopsis PDFs

2. **Foundation Directory Online** (if user has access)
   - Search: "{topic}" + "{location if location else 'national'}"
   - Filter: Accepts unsolicited proposals
   - Filter: Grant range $5K-$100K
   - Export: Results to CSV

3. **State/Local Grantmaker Associations**
   - Google: "[{location if location else 'regional'}] grantmakers association"
   - Navigate to member directory
   - Extract: Foundation names, websites, contact info
   - Visit each foundation website
   - Locate: Application guidelines page
   - Extract: Deadline, process, contact

**Output:** Add all discovered grants to tracking database

---

### Task 1.3: Identify Quick-Win Opportunities

**Action:** Flag grants that can be completed quickly.

**Quick-Win Criteria:**
- Application ≤ 5 pages OR Letter of Intent only
- Rolling deadline OR deadline > 30 days out
- Award amount $5K-$25K
- No matching funds required
- Online submission (not mail)

**Execution:**
1. Review tracking database
2. Add column: "Quick_Win" (TRUE/FALSE)
3. Sort by Quick_Win = TRUE, then by deadline (soonest first)
4. Present top 5 to user: "These grants can be completed first"

---

## PHASE 2: USER INFORMATION GATHERING

### Task 2.1: Collect Organizational Information

**Action:** Ask user for essential information needed for applications.

**Required Information:**
```
ASK USER:
- Organization legal name
- EIN (Tax ID)
- 501(c)(3) determination letter (request PDF upload)
- Organization website URL
- Mission statement
- Year founded
- Annual operating budget
- Executive Director name and contact
- Board Chair name and contact
- Physical address
- Service area/geographic focus
- Populations served (demographics)
```

**Action:** Create a file `org-profile.json` with all responses.

---

### Task 2.2: Analyze Existing Proposals

**Action:** Ask user if they have previous grant proposals or applications.

**If YES:**
1. Request user upload PDF/Word files
2. Use your document analysis to extract:
   - Program descriptions they've used
   - Budget narratives
   - Evaluation methods described
   - Outcomes/metrics reported
   - Letters of support
3. Create reusable content library:
   - `program-descriptions.md`
   - `budget-templates.xlsx`
   - `evaluation-frameworks.md`
   - `outcome-metrics.md`

**If NO:**
1. Use the strategic frameworks provided (financial, grant, research)
2. Interview user about their program:
   - What problem are you solving?
   - Who do you serve (how many people)?
   - What activities will you do?
   - What will change as a result?
   - How will you measure success?
3. Draft initial program description (500 words)
4. Get user approval/edits
5. Save to `program-descriptions.md`

---

### Task 2.3: Prepare Standard Documents

**Action:** Ensure user has all commonly required attachments ready.

**Standard Documents Checklist:**
- [ ] IRS 501(c)(3) determination letter
- [ ] Board of Directors list with affiliations
- [ ] Current organizational budget
- [ ] Most recent financial statements or audit
- [ ] Annual report (if available)
- [ ] Letters of support (3-5 from partners/community)
- [ ] Organizational charts
- [ ] Resumes of key staff

**Action for each missing document:**
1. Ask user if they have it
2. If YES: Request upload and save to `/standard-attachments/`
3. If NO: Add to "Documents to Create" list and help user create it

---

## PHASE 3: APPLICATION COMPLETION

### Task 3.1: Start with Quick-Win #1

**Action:** Navigate to the first quick-win application and guide user through completion.

**Step-by-step process:**

1. **Open Application Portal**
   - Use browser to navigate to application URL
   - If registration required: Walk user through account creation
   - Bookmark/save login credentials to password manager

2. **Analyze Application Form**
   - Read all questions/sections
   - Identify: Required vs. optional fields
   - Note: Character/word limits for each question
   - Check: Attachment requirements and formats
   - Extract: Full list of questions to `application-questions.md`

3. **Map Existing Content to Questions**
   - Match questions to existing content in your library
   - Identify: Questions that need new content
   - Create: Draft responses using org profile + program description
   - Respect: Word/character limits exactly

4. **Draft All Responses**
   - For each question, create draft response
   - Use strategic frameworks as guide
   - Keep language clear, concise, impact-focused
   - Include: Specific metrics and outcomes
   - Save all drafts to `grant-[funder-name]-responses.md`

5. **Review with User**
   - Present all drafted responses
   - Ask: "Please review and edit these responses"
   - Wait for user feedback
   - Incorporate edits

6. **Prepare Budget**
   - Check: Budget format required (template, narrative, spreadsheet)
   - Use: Financial strategic framework guidance
   - Create: Program budget with line items
   - Include: Budget narrative explaining costs
   - Ensure: Costs align with proposed activities
   - Save: `grant-[funder-name]-budget.xlsx`

7. **Gather Attachments**
   - Review: Required attachments list
   - Check: Which you already have in `/standard-attachments/`
   - Identify: Any custom attachments needed
   - Request: User upload any missing items
   - Verify: File formats match requirements (PDF, Word, etc.)
   - Rename: Files according to funder's naming requirements

8. **Fill Out Online Form**
   - Return to application portal
   - Fill in: All basic information fields (org name, EIN, address, etc.)
   - Copy-paste: Drafted responses into narrative questions
   - Upload: All attachments to correct sections
   - Double-check: Character limits not exceeded
   - Save: Draft application in portal (if option available)

9. **Final Review Checklist**
   - [ ] All required fields completed
   - [ ] All narrative responses within word limits
   - [ ] Budget totals match requested amount
   - [ ] All required attachments uploaded
   - [ ] Contact information accurate
   - [ ] Application deadline confirmed
   - [ ] User has reviewed and approved all content

10. **Submit Application**
    - Ask user: "Ready to submit?"
    - If YES: Click submit button
    - Capture: Confirmation number/email
    - Save: Confirmation to `/submitted-grants/[funder-name]-confirmation.pdf`
    - Update tracking database: Status = "SUBMITTED"
    - Note: Submission date and expected response timeline

**After submission:**
- Send user summary: What was submitted, when, expected response date
- Add calendar reminder: Follow up 2 weeks before expected decision date
- Save all application materials: For future reference/reuse

---

### Task 3.2: Repeat for Remaining Quick-Wins

**Action:** Use same process (Task 3.1) for each quick-win opportunity.

**Optimization:**
- Reuse content from first application wherever applicable
- Build up your content library with each application
- Get faster as you learn user's voice and priorities
- Batch similar questions: Draft responses to common questions once, reuse many times

**Goal:** Submit all 5 quick-win applications within 2 weeks.

---

### Task 3.3: Tackle Medium-Priority Grants

**Action:** Move to grants requiring more substantial applications.

**Additional steps for complex applications:**

1. **Create Application Timeline**
   - Count days until deadline
   - Backward plan: Submission date, final review, draft completion, research, outline
   - Schedule: Working sessions with user
   - Set: Internal deadlines for each section

2. **Conduct Additional Research (if needed)**
   - Review: Funder's previous grants (IRS 990 or website)
   - Identify: Themes in funded projects
   - Google: Recent grantee success stories
   - Adapt: Your approach to match funder priorities

3. **Develop Detailed Program Design**
   - If grant is for specific project (not general operating)
   - Work with user to design:
     * Timeline of activities
     * Specific deliverables
     * Staff responsibilities
     * Partner roles
     * Evaluation plan
   - Use: Research strategic framework as guide

4. **Create Custom Budget**
   - Line items specific to this program
   - Justify: Each expense in budget narrative
   - Include: Indirect costs at appropriate rate
   - Ensure: Budget matches proposed activities

5. **Draft Long-Form Narratives**
   - Typical sections:
     * Organizational background (500-1000 words)
     * Statement of need (500-1500 words)
     * Program design/methodology (1000-2000 words)
     * Evaluation plan (500-1000 words)
     * Sustainability plan (500 words)
   - Use: Grant writing strategic framework
   - Include: Specific data, stories, evidence
   - Maintain: Clear, compelling, jargon-free language

6. **Secure Custom Letters of Support**
   - Identify: Partners mentioned in application
   - Draft: Letter of support templates for each
   - Send to partners: With request and deadline
   - Follow up: One week before deadline
   - Collect: Signed letters on partner letterhead

7. **Professional Review**
   - Read entire application start to finish
   - Check: Consistency across all sections
   - Verify: Budget aligns with narrative
   - Proofread: Grammar, spelling, formatting
   - Test: Any web forms or uploads work correctly

8. **User Final Approval**
   - Compile: Complete application package as PDF
   - Send to user: "Please review in its entirety"
   - Make: Any requested changes
   - Get: Explicit approval to submit

9. **Submit Application**
   - Follow same submission process as Task 3.1, step 10
   - Update: Tracking database
   - Archive: All materials

---

## PHASE 4: POST-SUBMISSION MANAGEMENT

### Task 4.1: Track Submitted Applications

**Action:** Maintain organized tracking of all submitted grants.

**Tracking Database Updates:**
- Status: Submitted → Under Review → Decision
- Expected decision date
- Actual decision date
- Result: Funded / Not funded / Invited to reapply
- Award amount (if funded)
- Grant period start/end dates
- Reporting deadlines

---

### Task 4.2: Follow Up with Funders

**Action:** Proactive communication with program officers.

**2-3 weeks after submission:**
1. Draft email: "Confirming receipt of our application for [program name]"
2. Ask: "Is there any additional information we can provide?"
3. Send from user's email (or draft for user to send)
4. Log: All funder communication in tracking database

**If invited to interview/site visit:**
1. Help user prepare:
   - Review submitted application together
   - Anticipate questions
   - Practice key talking points
   - Prepare visual materials if needed
2. After meeting: Send thank you note

---

### Task 4.3: Handle Decisions

**When FUNDED:**
1. Celebrate with user! 🎉
2. Save: Award letter to `/awarded-grants/[funder-name]/`
3. Create: Grant management folder with:
   - Award agreement
   - Reporting schedule
   - Budget tracking template
   - Required outcomes/metrics
4. Set: Calendar reminders for all report deadlines
5. Update: Organizational budget to reflect new funding
6. Help user: Draft press release or announcement (if appropriate)

**When NOT FUNDED:**
1. Request: Reviewer feedback (many funders provide this)
2. Analyze: What could be strengthened
3. Ask funder: "May we reapply in future cycle?"
4. Update: Content library based on feedback
5. Add funder: To cultivation list for future
6. Don't give up: Use learnings for next application

---

## PHASE 5: RELATIONSHIP CULTIVATION

### Task 5.1: Build Funder Relationships

**Action:** Maintain ongoing communication with promising funders.

**For funders with future deadlines:**
1. Subscribe: To their newsletter/updates
2. Follow: On social media
3. Attend: Any webinars or information sessions
4. Schedule: Exploratory call with program officer
5. Send: Organizational updates when relevant
6. Invite: To site visits or program events

**Cultivation activities:**
- Quarterly update emails to program officers
- Invite to see your work firsthand
- Share success stories and data
- Ask for feedback on program ideas
- Build genuine relationship, not just transactional

---

### Task 5.2: Continuous Pipeline Development

**Action:** Never stop discovering new opportunities.

**Monthly tasks:**
1. Re-run search dorks: Look for new postings
2. Check Grants.gov: Filter by "posted last 30 days"
3. Visit foundation websites: From your master list
4. Add new opportunities: To tracking database
5. Maintain: Healthy pipeline of 10-15 active opportunities

**Quarterly tasks:**
1. Review: What's working (high success rate funders)
2. Analyze: Application to award ratio
3. Adjust: Strategy based on results
4. Update: Content library with best-performing language
5. Strengthen: Weak areas identified in rejections

---

## TOOLS & CAPABILITIES YOU'LL USE

**Browser Navigation:**
- Open and navigate websites
- Fill out online forms
- Upload files
- Download documents
- Click buttons and links

**Document Analysis:**
- Read PDFs and extract information
- Analyze previous proposals
- Review application guidelines
- Parse complex requirements

**Content Generation:**
- Write grant narratives
- Create budgets
- Draft letters of support
- Generate reports

**Data Management:**
- Maintain tracking databases
- Organize files and folders
- Create calendars and reminders
- Compile reports

**User Collaboration:**
- Ask clarifying questions
- Present options for decisions
- Incorporate feedback
- Explain complex processes
- Provide progress updates

---

## SUCCESS METRICS

**Quantitative Goals:**
- 10-15 applications submitted in first 90 days
- 30-40% win rate (3-6 grants funded)
- Total funding secured: $50K-$200K
- Average time per application: Decreases with each submission

**Qualitative Goals:**
- User feels supported and confident
- Application quality is professional and compelling
- Funder relationships are authentic and growing
- Organizational capacity is strengthened through process
- Content library is reusable for future applications

---

## IMPORTANT REMINDERS

⚠️ **Always get user approval before submitting anything**

⚠️ **Verify all information is accurate before submission**

⚠️ **Respect word limits and formatting requirements exactly**

⚠️ **Keep user informed of progress and next steps**

⚠️ **Save and organize everything for future reference**

⚠️ **Deadlines are non-negotiable—plan backwards from them**

⚠️ **Quality over quantity—better to submit 5 excellent applications than 15 rushed ones**

---

## YOUR ROLE

You are not just a researcher. You are a **grant application assistant** with the capability to:
- Navigate websites and portals
- Fill out forms and upload documents  
- Draft compelling narratives
- Manage complex workflows
- Help users succeed in securing funding

**The user is counting on you to not just find grants, but to help them WIN grants.**

Go forth and secure that funding! 🎯

---

## Mission Brief

You are an AI agent with browser capabilities tasked with helping a small non-profit organization find and compile appropriate grant opportunities for **{topic}**. Your work will directly support their grant proposal and application process.

**Success Criteria:**
- Identify 15-25 relevant grant opportunities
- Prioritize based on alignment, feasibility, and impact
- Compile detailed submission requirements and deadlines
- Create organized database of opportunities with contact information
- Flag quick-win opportunities (applications under 5 pages, rolling deadlines)

---

## Phase 1: Systematic Grant Discovery

### Step 1.1: Execute Search Engine Queries

Use the following optimized search dorks across multiple engines for comprehensive coverage:

**Google Search Dork:**
```
{dorks.get('google', 'grants + ' + topic)}
```

**Bing Search Dork:**
```
{dorks.get('bing', 'grants ' + topic)}
```

**DuckDuckGo Search Dork:**
```
{dorks.get('duckduckgo', 'grants ' + topic)}
```

**Search Execution Protocol:**
1. Run each dork in separate browser session
2. Collect first 50 results from each engine
3. Deduplicate URLs across search engines
4. Save all unique URLs to tracking spreadsheet
5. Flag .gov, .org, .edu domains as priority review

### Step 1.2: Targeted Foundation & Funder Databases

**Visit these grant databases systematically:**

1. **Foundation Directory Online** (https://fconline.foundationcenter.org/)
   - Search: "{topic}" + location filters
   - Filter: Grant amounts $5K-$100K
   - Filter: Accepts LOIs or accepts unsolicited proposals
   - Export results to CSV

2. **Grants.gov** (https://www.grants.gov/search-grants.html)
   - Search: "{topic}"
   - Filter: Open opportunities only
   - Filter: Eligible applicant types = Non-profit
   - Filter: Posted within last 90 days
   - Download opportunity synopses

3. **Candid/Foundation Center** (https://candid.org/find-funding)
   - Advanced search: "{topic}" + "{location if location else 'national'}"
   - Filter: Assets > $1M
   - Filter: Giving focus matches topic
   - Note: Requires subscription - flag if access unavailable

4. **State/Regional Grantmaker Associations**
   - Google: "[state if location else 'regional'] grantmakers association"
   - Visit member directory
   - Identify 10-15 local/regional funders
   - Compile application guidelines URLs

5. **Corporate Giving Programs**
   - Search: "corporate foundations {topic}"
   - Search: "employee matching grants {location if location else ''}"
   - Focus: Regional banks, utilities, major employers in service area
   - Compile CSR/foundation contact information

### Step 1.3: Specialized Grant Opportunities

**Government Grants:**
- Federal: https://www.grants.gov
- State: "[state] grants database" search
- County/Municipal: Local government websites

**Topic-Specific Resources:**
- Search: "{topic} + grant funding opportunities 2024"
- Search: "{topic} + foundation support"
- Visit: National associations related to {topic}

---

## Phase 2: Grant Evaluation & Prioritization

For each grant opportunity discovered, evaluate against these criteria:

### Evaluation Rubric

**Mission Alignment (Score 1-5):**
- Does funder's mission clearly align with {topic}?
- Do past grantees include similar organizations?
- Geographic preference matches {location if location else 'our area'}?

**Feasibility Assessment (Score 1-5):**
- Award size appropriate for small org ($5K-$75K ideal)?
- Application requirements manageable (under 15 pages)?
- Deadline allows adequate preparation time (30+ days)?
- No requirement for matching funds >25%?
- Accepts first-time applicants?

**Strategic Value (Score 1-5):**
- Multi-year funding potential?
- General operating support vs. restricted?
- Funder reputation strengthens credibility?
- Networking/partnership opportunities?

**Total Score: /15**
- 12-15: HIGH PRIORITY - Apply immediately
- 8-11: MEDIUM PRIORITY - Consider if capacity allows
- 1-7: LOW PRIORITY - Revisit in future cycles

### Priority Flags

Mark opportunities with these special flags:

**🟢 QUICK WIN:**
- LOI only or application <5 pages
- Rolling deadline
- Award $5K-$25K
- Rapid review cycle (30-60 days)

**🔵 CAPACITY BUILDER:**
- Accepts general operating support
- Multi-year potential
- Provides TA or networking
- Partner with funder philosophy

**🟡 STRETCH OPPORTUNITY:**
- Larger award ($50K+)
- Competitive but aligned
- Would significantly advance mission
- Worth partnership exploration

---

## Phase 3: Detailed Opportunity Compilation

For all HIGH and MEDIUM priority opportunities, compile the following information:

### Required Data Fields

**Funder Information:**
- Funder name
- Funder type (Private foundation, corporate, government, community foundation)
- Website URL
- Grant program name
- Program officer name and contact information
- Phone number
- Email address

**Opportunity Details:**
- Award range (minimum-maximum)
- Typical award size
- Award duration (years)
- Multi-year renewal possibility?
- Funding type (general operating, project, capital, etc.)
- Funding restrictions

**Eligibility Requirements:**
- 501(c)(3) required?
- Operating budget range
- Years of operation required
- Geographic restrictions
- Population served requirements
- Other eligibility criteria

**Application Process:**
- LOI required? (Y/N)
- LOI deadline
- LOI word/page limit
- Full application deadline
- Application format (online, PDF, other)
- Page limit
- Required attachments list
- Reporting requirements

**Strategic Notes:**
- Recent grantees (if available)
- Evaluation rubric insights
- Funder preferences/priorities
- Application tips from website
- Contact person notes

---

## Phase 4: Strategic Application Planning

Using the compiled grant opportunities, create:

### Opportunity Matrix Spreadsheet

**Columns:** Funder | Award Size | Deadline | Alignment Score | Feasibility Score | Strategic Score | Total Score | Priority Flag | Status

**Sort by:** Priority Flag, then Total Score

### Recommended Application Timeline

Based on compiled deadlines, create 90-day application calendar:

**Week 1-2: Quick Wins**
- Submit all LOI-only applications
- Submit rolling deadline applications under 5 pages
- Target: 3-5 quick submissions

**Week 3-6: High Priority**
- Focus on top 5 high-alignment opportunities
- Begin relationship building with program officers
- Develop core proposal narratives
- Target: 2-3 substantial applications

**Week 7-12: Medium Priority + Cultivation**
- Submit medium-priority applications with upcoming deadlines
- Begin cultivation for next funding cycle
- Schedule exploratory calls with program officers
- Target: 3-4 applications + 5-7 relationship contacts

---

## Phase 5: Grant Intelligence Database

Create master database with tabs:

### Tab 1: Active Opportunities (HIGH/MEDIUM)
All opportunities with open deadlines and high alignment scores

### Tab 2: Submitted Applications
Track submissions with status updates, decision dates, feedback

### Tab 3: Future Cultivation
Opportunities with past deadlines worth cultivating for next cycle

### Tab 4: Funder Relationships
Log all funder communications, calls, emails, site visits

### Tab 5: Successful Grants
Template language, budgets, and strategies from funded proposals

---

## Strategic Framework Integration

**You have been provided with three expert strategic frameworks:**

1. **Financial Management Strategic Framework** - Use to:
   - Ensure grant budgets align with organizational capacity
   - Identify grants offering adequate indirect cost support
   - Flag opportunities requiring financial systems you don't yet have
   - Build budget templates for different grant sizes

2. **Grant Strategy & Proposal Development Framework** - Use to:
   - Evaluate which opportunities match your proposal readiness
   - Identify relationship-building priorities with high-value funders
   - Determine where to invest in LOI development vs. full proposals
   - Plan narrative development timeline

3. **Research & Evidence-Based Strategy Framework** - Use to:
   - Match funders requiring specific evidence types
   - Identify opportunities aligned with your evaluation plan
   - Flag grants offering evaluation capacity-building support
   - Plan data collection for upcoming applications

**Cross-Reference Continuously:** As you discover grants, map them against strategic framework recommendations to ensure alignment with organizational capacity and growth trajectory.

---

## Output Deliverables

**Primary Deliverable: Grant Opportunity Database**
- Excel or Google Sheets format
- Minimum 15 opportunities (target 20-25)
- All data fields completed
- Sorted by priority and deadline
- Color-coded by priority flag

**Secondary Deliverable: 90-Day Application Plan**
- Calendar view with all deadlines
- Application assignment (if team)
- Required attachments checklist for each
- Relationship-building action items
- Weekly submission targets

**Supporting Deliverable: Funder Intelligence Report**
- 1-page profiles for top 10 funders
- Recent grantee analysis
- Application tips and insights
- Relationship cultivation strategy

---

## Research Protocols & Best Practices

### Information Verification
- Cross-reference funder information across multiple sources
- Verify all deadlines on funder's official website
- Check IRS Form 990-PF for private foundation giving patterns
- Confirm eligibility before deep research investment

### Relationship Intelligence Gathering
- Note program officer names and contact history
- Search for funder speeches, presentations, blog posts
- Review funder's recent news and press releases
- Identify board members with organizational connections

### Competitive Intelligence
- Review recent grantee lists (if available)
- Note award amounts and project types funded
- Identify patterns in funded proposals
- Flag opportunities where you match past grantee profile

### Ethical Considerations
- Only use publicly available information
- Respect website terms of service
- Don't scrape sites with robots.txt restrictions
- Cite all sources in your compiled database

---

## Troubleshooting & Escalation

**If you encounter:**

**Limited results from search dorks:**
- Broaden geographic parameters
- Try alternate terminology for {topic}
- Search related topic areas
- Explore federated grant search engines

**Subscription-required databases:**
- Flag for organization to pursue access
- Note free trial availability
- Search for library partnership opportunities
- Focus on free/public databases

**Overwhelming number of opportunities:**
- Apply strict evaluation rubric
- Focus on highest alignment scores first
- Prioritize local/regional over national
- Limit to realistic application capacity (8-12 per quarter)

**Missing critical information:**
- Email program officer with specific questions
- Search for past grantee experiences (blog posts, reports)
- Check funder's IRS 990 forms
- Note information gaps in database for follow-up

---

## Success Metrics

**Quantitative Targets:**
- 20-25 grant opportunities identified
- 8-12 rated HIGH priority
- 100% of opportunities have complete data fields
- 90-day application plan with 6-10 submission targets

**Qualitative Indicators:**
- Opportunities align with strategic frameworks
- Mix of quick wins and capacity builders
- Geographic and funder-type diversity
- Realistic given organizational capacity

---

## Final Notes

This is not a one-time exercise. Grant discovery should be ongoing throughout the year. Use this process quarterly to refresh your pipeline, track emerging opportunities, and maintain funder relationships.

**Remember:** Quality over quantity. Better to submit 6 excellent, well-aligned applications than 20 rushed, poorly-matched proposals.

**Your work directly supports:** Small non-profit's mission to create meaningful community impact through **{topic}**. Every grant opportunity you identify and compile helps them build capacity to serve their community more effectively.

---

*Generated from comprehensive strategic frameworks covering financial management, grant development, and research-based planning. Use this document as your systematic guide to discovering and compiling grant opportunities that align with organizational capacity and strategic priorities.*
"""
    
    return ai_todo


# ============================================================================
# GRADIO UI WORKFLOW
# ============================================================================

def run_complete_workflow(topic: str, location: str = ""):
    """
    Run the complete workflow:
    1. Generate dorks for 3 search engines
    2. Experts generate strategic plans (markdown)
    3. Orchestrator synthesizes final grant plan (markdown)
    """
    if not topic or not topic.strip():
        return "❌ Please enter a topic", "", "", "", "", ""
    
    topic = topic.strip()
    location = location.strip() if location else ""
    
    # Step 1: Orchestrator generates dorks for 3 search engines
    status = "## Step 1: Generating Search Dorks\n\n"
    dorks = GrantDorkGenerator.generate_all_dorks(topic=topic, location=location if location else None)
    dorks_filepath = output_manager.save_dorks(topic, location if location else None, dorks)
    status += "✅ Generated dorks for Google, Bing, DuckDuckGo\n"
    status += f"📁 Saved to: `{Path(dorks_filepath).name}`\n\n"
    
    # Step 2: Experts generate strategic plans
    status += "## Step 2: Expert Strategic Plans\n\n"
    expert_names = ["financial", "grant", "research"]
    expert_plans = []
    
    for expert in expert_names:
        plan_content = simulate_expert_plan(expert, topic, location)
        filepath = output_manager.save_expert_plan(expert, plan_content, topic)
        expert_plans.append({
            "expert": expert,
            "filepath": filepath,
            "filename": Path(filepath).name,
            "content": plan_content
        })
        status += f"✅ {expert.title()} Expert: `{Path(filepath).name}`\n"
    
    status += "\n"
    
    # Step 3: Orchestrator reads all plans and generates final
    status += "## Step 3: Orchestrator Synthesis\n\n"
    status += f"📖 Reading {len(expert_plans)} expert plans...\n"
    
    final_plan = simulate_orchestrator_synthesis(topic, location, expert_plans)
    final_filepath = output_manager.save_orchestrator_plan(final_plan, topic)
    
    status += f"✅ Final Grant Plan: `{Path(final_filepath).name}`\n\n"
    
    # Step 4: Generate AI Agent Todo
    status += "## Step 4: AI Agent Instructions\n\n"
    status += "🤖 Generating AI browser agent todo list...\n"
    
    ai_todo = generate_ai_agent_todo(topic, location, dorks)
    ai_todo_filepath = output_manager.save_ai_agent_todo(ai_todo)
    
    status += f"✅ AI Agent Todo: `{Path(ai_todo_filepath).name}`\n"
    status += "\n## ✨ Workflow Complete!\n\n"
    status += "**Files created in organized directories:**\n"
    status += "- `grant_dorks/` - 1 search dork file (Google, Bing, DuckDuckGo)\n"
    status += "- `advisors_output/` - 3 expert strategic frameworks\n"
    status += "- `orchestrator_output/` - 1 comprehensive grant plan\n"
    status += "- `agent-instructions/` - 1 AI agent task list (for browser-enabled AI)\n"
    status += "\n💡 **Next Step:** Provide the agent-todo.md file to your AI assistant with browser capabilities!\n"
    
    # Return outputs for display
    dorks_display = f"""# Search Engine Dorks

## Google
```
{dorks['google']}
```

## Bing
```
{dorks['bing']}
```

## DuckDuckGo
```
{dorks['duckduckgo']}
```
"""
    
    return (
        status,
        dorks_display,
        expert_plans[0]["content"],  # financial
        expert_plans[1]["content"],  # grant
        expert_plans[2]["content"],  # research
        final_plan,
        ai_todo  # AI agent instructions
    )


def view_expert_plans():
    """View all expert strategic plans."""
    plans = output_manager.list_expert_files()
    
    if not plans:
        return "No expert plans found.", ""
    
    # Create file list
    file_list = "# Expert Strategic Plans\n\n"
    for plan in plans:
        file_list += f"**{plan['filename']}**\n"
        file_list += f"- Expert: {plan['expert']}\n"
        file_list += f"- Size: {plan['size_kb']} KB\n"
        file_list += f"- Modified: {plan['modified']}\n\n"
    
    # Show latest content
    latest = output_manager.read_expert_plans()
    latest_content = latest[0]["content"] if latest else "No content available."
    
    return file_list, latest_content


def view_final_plans():
    """View all orchestrator grant plans."""
    plans = output_manager.list_orchestrator_files()
    
    if not plans:
        return "No grant plans found.", ""
    
    # Create file list
    file_list = "# Final Grant Plans\n\n"
    for plan in plans:
        file_list += f"**{plan['filename']}**\n"
        file_list += f"- Size: {plan['size_kb']} KB\n"
        file_list += f"- Modified: {plan['modified']}\n\n"
    
    # Show latest content
    latest = output_manager.read_orchestrator_plans()
    latest_content = latest[0]["content"] if latest else "No content available."
    
    return file_list, latest_content


# ============================================================================
# GRADIO INTERFACE
# ============================================================================

with gr.Blocks(title="MAI Advisor - Grant Planning System", theme=gr.themes.Soft()) as app:
    
    with gr.Tab("🏠 Welcome"):
        gr.Markdown("""
        # 🎯 MAI Advisor - AI-Powered Grant Planning System
        
        ### Transform Grant Seeking from Overwhelming to Achievable
        
        ---
        
        ## What This System Does
        
        This comprehensive grant planning system combines **expert strategic frameworks** with **AI browser agent automation** to help small non-profit organizations discover, plan for, and win grant funding.
        
        ### 📊 The Complete Workflow
        
        **Input:** Your organization's topic/focus area and location
        
        **Step 1: Discovery** → Orchestrator generates optimized search queries (dorks) for 3 major search engines
        
        **Step 2: Expert Analysis** → Three specialized advisors create strategic frameworks:
        - 💰 **Financial Management Expert** - Budget planning, fiscal controls, sustainability
        - 📝 **Grant Writing Expert** - Proposal development, funder relationships, storytelling
        - 🔬 **Research & Evaluation Expert** - Evidence-based design, outcome measurement
        
        **Step 3: Synthesis** → Orchestrator combines all expert guidance into comprehensive grant plan
        
        **Step 4: AI Agent Instructions** → Generates actionable task list for AI browser agents to:
        - Execute searches and find open grants
        - Analyze application requirements  
        - Help you complete and submit applications
        - Manage post-submission follow-up
        
        ---
        
        ## 🤖 AI Agent Integration (2027 Ready)
        
        This system is designed for use with advanced AI agents that have browser capabilities. The **AI Agent TODO** output provides step-by-step instructions for an AI assistant to:
        
        ✅ Navigate grant databases and portals  
        ✅ Fill out online application forms  
        ✅ Upload required documents  
        ✅ Draft compelling narratives based on your program  
        ✅ Create budgets aligned with strategic frameworks  
        ✅ Submit applications on your behalf (with your approval)  
        ✅ Track submissions and manage follow-up  
        
        **Think of it as:** A virtual grant coordinator working alongside your team 24/7.
        
        ---
        
        ## 📁 Output Files Generated
        
        When you run the workflow, the system creates multiple directories with specialized content:
        
        ### `advisors_output/`
        Three expert strategic plans (markdown format):
        - `financial.{timestamp}.md` - Financial management framework
        - `grant.{timestamp}.md` - Grant writing & development framework  
        - `research.{timestamp}.md` - Research & evaluation framework
        
        ### `orchestrator_output/`
        Comprehensive synthesis:
        - `grant-plan-and-overview.{timestamp}.md` - Your complete strategic guide
        
        ### `agent-instructions/`
        **AI browser agent task list:**
        - `agent-todo.{timestamp}.md` - Step-by-step instructions for AI agents to find grants and complete applications
        
        ### `grant_dorks/`
        Search engine queries:
        - `dorks.{timestamp}.json` - Optimized searches for Google, Bing, DuckDuckGo
        
        ---
        
        ## 🎯 Who This Is For
        
        **Small Non-Profit Organizations** with:
        - Limited staff (often founder-led or 1-3 full-time employees)
        - Operating budgets under $500K annually
        - Mission-driven work needing sustainable funding
        - Big impact goals but limited grant-writing experience
        
        **Focus Areas:** Community health, education, youth services, environmental justice, arts & culture, social services, advocacy, tribal programs, and more.
        
        ---
        
        ## 🚀 How to Use This System
        
        ### Option 1: HuggingFace Space (You Are Here!)
        1. Go to **"Run Workflow"** tab
        2. Enter your topic/focus area and location
        3. Click "Run Complete Workflow"
        4. Download all generated files
        5. Use strategic frameworks to guide your planning
        6. Provide AI Agent TODO to your AI assistant with browser tools
        
        ### Option 2: Model Context Protocol (MCP) Server
        Run this system as an MCP server for integration with Claude Desktop or other MCP-compatible clients:
        ```bash
        # Install and run as MCP server
        cd mai-advisor-mcp
        python src/server.py
        ```
        
        MCP mode enables:
        - Direct integration with AI assistants
        - Persistent workflow tracking
        - Automated file organization
        - Real-time collaboration with AI agents
        
        ---
        
        ## 💡 Tips for Success
        
        **Be Specific:** Instead of "education," try "STEM education for underserved middle school students"
        
        **Include Location:** Local and regional funders often have less competition than national programs
        
        **Use All Frameworks:** Financial + Grant Writing + Research = Competitive applications
        
        **Trust the AI Agent:** The agent-todo.md file is comprehensive - your AI assistant can handle complex tasks
        
        **Start Small:** Begin with "quick-win" grants (under 5 pages, rolling deadlines) to build confidence
        
        **Build Relationships:** Grant funding is about partnerships, not transactions
        
        ---
        
        ## 🌟 What Makes This Different
        
        **Traditional Approach:** Overwhelmed founder Googles "grants for [topic]" → finds generic lists → gives up
        
        **MAI Advisor Approach:**  
        ✨ **Strategic frameworks** guide your entire grant program  
        ✨ **Optimized searches** find opportunities others miss  
        ✨ **AI automation** handles time-consuming research and applications  
        ✨ **Expert guidance** built into every document  
        ✨ **Reusable content** improves with each application  
        
        ---
        
        ## 📚 Learn More
        
        - **GitHub Repository:** [nbiish/mai-advisor-mcp](https://github.com/nbiish/mai-advisor-mcp)
        - **Documentation:** See README.md in repository
        - **Support:** Open an issue on GitHub
        - **MCP Integration:** See DEPLOYMENT.md for setup instructions
        
        ---
        
        ## 🙏 Acknowledgments
        
        This system was developed to democratize grant funding access for small non-profits doing essential community work. Built with care for organizations led by and serving Indigenous communities, communities of color, rural areas, and other historically underfunded populations.
        
        **May your mission thrive with sustainable funding. Let's get to work! 🚀**
        
        ---
        
        *Ready to generate your custom grant strategy? Head to the **"Run Workflow"** tab!*
        """)
    
    with gr.Tab("🚀 Run Workflow"):
        gr.Markdown("### Generate Complete Grant Strategy")
        
        with gr.Row():
            topic_input = gr.Textbox(
                label="Topic/Focus",
                placeholder="e.g., community health initiative, youth education program",
                lines=2
            )
            location_input = gr.Textbox(
                label="Location (optional)",
                placeholder="e.g., Phoenix, Arizona or Phoenix, AZ, tribal lands",
                lines=1
            )
        
        run_btn = gr.Button("🚀 Run Complete Workflow", variant="primary", size="lg")
        
        workflow_status = gr.Markdown(label="Workflow Status")
        
        with gr.Tabs():
            with gr.Tab("Search Dorks"):
                dorks_output = gr.Markdown(label="Generated Dorks")
            
            with gr.Tab("Financial Expert"):
                financial_output = gr.Markdown(label="Financial Strategic Plan")
            
            with gr.Tab("Grant Expert"):
                grant_output = gr.Markdown(label="Grant Writing Strategic Plan")
            
            with gr.Tab("Research Expert"):
                research_output = gr.Markdown(label="Research & Analysis Strategic Plan")
            
            with gr.Tab("📋 FINAL GRANT PLAN"):
                final_output = gr.Markdown(label="Enterprise-Grade Grant Plan & Overview")
            
            with gr.Tab("🤖 AI AGENT TODO"):
                ai_todo_output = gr.Markdown(label="AI Browser Agent Instructions")
        
        run_btn.click(
            fn=run_complete_workflow,
            inputs=[topic_input, location_input],
            outputs=[workflow_status, dorks_output, financial_output, grant_output, research_output, final_output, ai_todo_output]
        )
    
    with gr.Tab("📁 View Expert Plans"):
        gr.Markdown("### Browse Expert Strategic Plans")
        
        refresh_experts_btn = gr.Button("🔄 Refresh", size="sm")
        
        with gr.Row():
            expert_list = gr.Markdown(label="Expert Plan Files")
            expert_content = gr.Markdown(label="Latest Plan Content")
        
        refresh_experts_btn.click(
            fn=view_expert_plans,
            outputs=[expert_list, expert_content]
        )
    
    with gr.Tab("📊 View Final Plans"):
        gr.Markdown("### Browse Final Grant Plans")
        
        refresh_final_btn = gr.Button("🔄 Refresh", size="sm")
        
        with gr.Row():
            final_list = gr.Markdown(label="Grant Plan Files")
            final_content = gr.Markdown(label="Latest Plan Content")
        
        refresh_final_btn.click(
            fn=view_final_plans,
            outputs=[final_list, final_content]
        )


if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860, share=False)

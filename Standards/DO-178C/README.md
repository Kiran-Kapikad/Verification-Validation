# DO-178C --- Software Considerations in Airborne Systems and Equipment Certification

Purpose of this document: A practical V&V study and reference
guide for this repository. It explains DO-178C concepts in original
wording, connects them to verification engineering, and provides
worked examples. It is not a reproduction of the DO-178C standard.

## 1. What is DO-178C?

DO-178C, Software Considerations in Airborne Systems and Equipment
Certification, is the principal industry guidance document used to
establish software development assurance for airborne systems and
equipment.

It provides a framework of software life-cycle processes, activities,
objectives, and evidence used to provide confidence that airborne
software performs its intended functions and does not introduce
unacceptable safety-related behavior.

DO-178C is not itself an aviation regulation. In the U.S. certification
context, FAA AC 20-115D recognizes DO-178C as an acceptable means, but
not the only means, for showing compliance with applicable airworthiness
regulations for software aspects of airborne systems and equipment.

V&V perspective: DO-178C is not simply a testing standard.
Verification is one part of a broader life-cycle assurance framework
covering planning, development, verification, configuration management,
quality assurance, and certification liaison.

## 2. Purpose and Scope

The purpose of DO-178C is to provide a systematic approach for achieving
confidence in the software used in airborne systems and equipment.

The scope includes software life-cycle activities associated with:

Planning

Development

Verification

Configuration management

Software quality assurance

Certification liaison

The level of rigor depends on the software's assigned Development
Assurance Level (DAL).

A key principle is that the applicant must be able to show objective
evidence that the applicable objectives have been satisfied.

Important distinction: DO-178C does not prescribe a single
programming language, development environment, test tool, or
organizational structure. It establishes objectives and associated
activities/data; an approved project defines how those objectives are
implemented.

## 3. Software Levels / DAL A--E

DO-178C defines five software levels based on the consequences of
anomalous software behavior.

Level       Consequence of failure

DAL A   Catastrophic
DAL B   Hazardous / severe-major
DAL C   Major
DAL D   Minor
DAL E   No effect

The DAL is determined from the system safety assessment and the
contribution of the software to aircraft/system functions. It is not
simply a measure of software complexity.

Why DAL matters

The DAL affects the rigor and set of objectives applicable to the
software life cycle.

For example, higher-assurance software generally requires more extensive
verification evidence and, at the highest levels, additional structural
coverage and independence considerations.

Important clarification

It is incorrect to think:

"DAL A means the software has the most bugs."

DAL describes the potential safety consequence associated with
failure, not the quality of the code.

## 4. DO-178C Life-Cycle Processes

The major software life-cycle processes can be viewed as:

Planning
   |
   v
Development
   |
   v
Verification
   |
   +--> Configuration Management
   |
   +--> Software Quality Assurance
   |
   v
Certification Liaison

Planning

Defines how the project will satisfy applicable objectives.

Typical planning data includes:

Plan for Software Aspects of Certification (PSAC)

Software Development Plan (SDP)

Software Verification Plan (SVP)

Software Configuration Management Plan (SCMP)

Software Quality Assurance Plan (SQAP)

Development

Produces the software and its development life-cycle data, including
requirements, architecture/design, source code, and executable/object
code as applicable.

Verification

Provides activities and evidence to determine whether development
outputs satisfy their requirements and applicable objectives.

Configuration Management

Controls baselines, versions, changes, and configuration items.

Software Quality Assurance

Provides assurance that defined processes and standards are followed and
that required records/evidence are produced.

Certification Liaison

Coordinates certification-related activities and communication with the
certification authority or designated representatives.

## 5. Planning Process

Planning establishes the project's approach to satisfying the applicable
DO-178C objectives.

A practical planning flow is:

System Safety / Certification Context
            |
            v
Software Level
            |
            v
Applicable Objectives
            |
            v
Development + Verification Strategy
            |
            v
Plans + Standards
            |
            v
Life-Cycle Data / Evidence

Important planning considerations include:

Software level

Development methods

Verification methods

Tool usage

Configuration management

Quality assurance

Traceability

Independence

Review and testing strategy

Certification approach

V&V perspective

A V&V engineer should understand the Software Verification Plan
(SVP) and how verification activities map to requirements, design
data, source code, test environments, coverage objectives, and evidence.

## 6. Development Processes

The development processes produce the software items that must
subsequently be verified.

A simplified relationship is:

High-Level Requirements
        |
        v
Software Architecture / Low-Level Requirements
        |
        v
Source Code
        |
        v
Executable Object Code

The exact development lifecycle can vary, but traceability and
consistency between development artifacts are central.

Verification must address more than execution

Verification can involve:

Reviews

Analyses

Walkthroughs

Inspections

Testing

Coverage analysis

Traceability analysis

Data/control-flow analysis

Interface analysis

The verification method should be appropriate to the item and objective
being verified.

## 7. Verification Process

Verification provides evidence that development outputs satisfy their
specified requirements and applicable verification objectives.

A practical V&V workflow is:

Requirement
   |
   v
Verification Method
   |
   v
Test / Review / Analysis
   |
   v
Result
   |
   v
Evidence
   |
   v
Traceability

Typical verification activities

Requirements reviews

Design reviews

Code reviews

Requirements-based testing

Integration testing

Regression testing

Robustness testing

Structural coverage analysis

Traceability analysis

Verification of derived requirements

Verification of interfaces

Verification vs validation

A useful engineering distinction is:

Verification: Are we correctly implementing the specified
requirements?

Validation: Does the resulting system satisfy its intended
operational purpose?

In a DO-178C project, the formal verification framework is centered on
verification objectives and evidence across the software life cycle.

## 8. Configuration Management

Configuration management ensures that the correct versions of software
and life-cycle data are identified, controlled, and reproducible.

Typical configuration items can include:

Requirements

Source code

Executable/object code

Test procedures

Test results

Plans

Standards

Configuration data

Tool versions

Build scripts

Verification records

Practical Git analogy

A modern engineering workflow may use Git for version control:

Change
  |
  v
Review
  |
  v
Commit
  |
  v
Build / Verification
  |
  v
Baseline / Release

Git is a tool; configuration management is the controlled process around
identifying, reviewing, approving, baselining, and tracking
configuration items.

## 9. Software Quality Assurance

Software Quality Assurance (SQA) provides confidence that the software
life-cycle processes and standards are being followed and that required
records are maintained.

Typical SQA concerns include:

Process compliance

Plan compliance

Standards compliance

Configuration management compliance

Problem-report tracking

Review records

Verification evidence

Baseline control

Audit readiness

V&V vs SQA

They are related but not identical.

V&V asks whether the product and development outputs satisfy
applicable requirements and verification objectives.

SQA provides independent process assurance that the defined
processes and associated standards are followed.

## 10. Certification Liaison

Certification liaison connects the development organization with the
certification authority and the certification basis/process.

This may involve:

Certification planning

Agreement on compliance approach

Review of certification data

Coordination of software life-cycle data

Resolution/clarification of certification questions

Support for certification reviews

In the FAA context, AC 20-115D describes DO-178C as an acceptable means,
but not the only means, of showing compliance for applicable software
aspects.

## 11. Requirements Traceability

Traceability demonstrates relationships between development and
verification artifacts.

A simplified bidirectional chain is:

System Requirement
       |
       v
High-Level Software Requirement
       |
       v
Low-Level Requirement / Design
       |
       v
Source Code
       |
       v
Test Case / Verification
       |
       v
Test Result

Forward traceability

Shows that each applicable requirement is implemented and verified.

Backward traceability

Shows that implementation and verification items can be justified by
originating requirements or approved derived requirements.

Example

Requirement:

The software shall command the actuator to CLOSED when the valid close
command is received and the interlock is satisfied.

Possible traceability:

REQ-ACT-001
    |
    +--> LLR-ACT-021
    |
    +--> CODE-ACT-021
    |
    +--> TEST-ACT-001
    |
    +--> RESULT-ACT-001

A traceability matrix should allow an engineer to identify missing
verification or unexplained implementation.

## 12. Requirements-Based Testing

Requirements-based testing derives test conditions from requirements
rather than merely trying to execute as much code as possible.

Example requirement

If Enable = TRUE and Valid_Command = TRUE, the system shall
transmit the command.

Test conditions should consider:

Enable true/false

Command valid/invalid

Expected transmission

Expected non-transmission

Boundary/robustness behavior where applicable

A simple test matrix:

Test     Enable   Valid Command Expected

T01       FALSE           FALSE No transmission
T02       FALSE            TRUE No transmission
T03        TRUE           FALSE No transmission
T04        TRUE            TRUE Transmission

Important point

Passing all tests does not automatically prove that every structural
coverage objective has been satisfied. Requirements-based testing and
structural coverage answer related but different questions.

## 13. Structural Coverage

Structural coverage examines which structural elements of the
implementation were exercised by the verification tests.

Common coverage measures include:

Statement coverage

Decision coverage

Condition coverage

MC/DC

The purpose is not merely to produce a percentage. Coverage analysis can
reveal portions of implementation that were not exercised by
requirements-based tests.

Simplified workflow

Requirements-Based Tests
        |
        v
Execute Software
        |
        v
Collect Coverage Data
        |
        v
Analyze Uncovered Elements
        |
        +--> Missing Test?
        |
        +--> Deactivated Code?
        |
        +--> Defensive / unreachable code?
        |
        v
Additional Verification / Analysis

For higher DAL software, applicable structural coverage objectives
become increasingly rigorous.

## 14. Statement Coverage

Statement coverage asks whether each executable statement has been
executed by the test set.

Example:

if (temperature > LIMIT)
{
    alarm = TRUE;
}

log_status();

A test with temperature > LIMIT executes both the assignment and
log_status().

A test set that only executes the false branch may execute
log_status() but not the statement alarm = TRUE.

Key limitation

100% statement coverage does not prove that every decision outcome
has been exercised.

It also does not demonstrate independence of individual conditions
within a compound decision.

## 15. Decision Coverage

Decision coverage examines whether the outcomes of a decision have been
exercised.

Example:

if (A)
{
    X();
}
else
{
    Y();
}

To demonstrate both decision outcomes, tests must produce:

A = TRUE  -> X()
A = FALSE -> Y()

Compound decision

For:

if (A && B)

decision coverage requires the overall decision to evaluate both:

TRUE
FALSE

However, a test set achieving decision coverage does not necessarily
demonstrate that A and B independently affect the decision. That is
where MC/DC becomes important.

## 16. MC/DC --- Modified Condition/Decision Coverage

MC/DC demonstrates that each individual condition within a decision has
an independent effect on the decision outcome, subject to the applicable
definition and interpretation of MC/DC.

Consider:

Decision = A AND B

Truth table:

Test     A   B   Decision

T1       F   F          F
T2       F   T          F
T3       T   F          F
T4       T   T          T

One MC/DC test set can be:

T1 = F, F -> F
T2 = F, T -> F
T4 = T, T -> T

To demonstrate independence:

Compare T1 and T2: B changes while A remains F; decision remains F,
so this pair does not demonstrate B's effect.

Compare T2 and T4: A changes while B remains T; decision changes F
-> T. This demonstrates A's effect.

To demonstrate B independently, compare T3 and T4: B changes while A
remains T; decision changes F -> T.

Therefore a valid minimal set for A AND B is:

T2 = F,T -> F
T3 = T,F -> F
T4 = T,T -> T

Here:

T2 vs T4 demonstrates A independently.

T3 vs T4 demonstrates B independently.

Practical MC/DC process

Identify the decision.

Identify individual conditions.

Construct the truth table or logical analysis.

Find pairs where only one condition changes.

Confirm the decision outcome changes.

Select the required tests.

Document the independence argument.

Execute and retain objective evidence.

Important distinction

MC/DC is not simply "test every TRUE/FALSE combination." The objective
is to demonstrate the required independent effect of each condition on
the decision.

## 17. Verification Independence

Verification independence means that, where independence is required,
the verification activity is performed with sufficient separation from
the activity that produced the item being verified.

The intent is to reduce the risk that the same person or team overlooks
an error they introduced.

Independence requirements vary according to the applicable objective and
software level.

Practical example

If an engineer develops a software component and writes the verification
procedure, an independent reviewer or verifier may be required for
specific verification objectives depending on the project's DAL and
approved plans.

Independence should be treated as a defined project process, not as an
informal statement that someone else "looked at it."

## 18. Verification Objectives

A verification objective is a specific outcome that the applicable
life-cycle process must satisfy.

The important concept is:

Objective
   |
   +--> Activity / Method
   |
   +--> Evidence
   |
   v
Objective Satisfaction

Examples of evidence can include:

Review records

Analysis results

Test procedures

Test results

Coverage reports

Traceability matrices

Problem reports

Verification summaries

Why objectives matter

A test can pass while an objective remains unsatisfied if the test did
not use the required method, did not provide the necessary evidence, or
did not address the applicable requirement/coverage condition.

Therefore:

Test pass ≠ automatically equivalent to complete DO-178C objective
satisfaction.

## 19. Software Life-Cycle Data

Life-cycle data is the documented information produced during software
development and verification.

Depending on the project and applicable objectives, examples include:

Planning data

PSAC

SDP

SVP

SCMP

SQAP

Development data

Software requirements

Design/architecture data

Source code

Executable/object code

Interface data

Verification data

Verification procedures

Verification cases

Verification results

Review records

Analysis records

Coverage data

Traceability data

Configuration and quality data

Configuration records

Baselines

Change records

Problem reports

SQA records

Certification data

Certification-related summaries

Compliance evidence

Other agreed certification deliverables

The exact set of life-cycle data is project-specific and depends on the
applicable objectives, plans, and certification approach.

## 20. SOI Reviews

SOI means Stage of Involvement.

FAA software certification guidance commonly describes four stages of
involvement:

SOI         Typical focus

SOI-1   Planning
SOI-2   Development
SOI-3   Verification
SOI-4   Final certification / software accomplishment summary

The exact conduct and depth of involvement depend on the certification
project and authority.

SOI-3 and V&V

SOI-3 is particularly relevant to a V&V engineer because it focuses on
the verification process and associated evidence.

Typical concerns include:

Requirements-based testing

Structural coverage

Verification independence

Traceability

Verification procedures/results

Problem reports

Configuration control

Verification evidence

Important: SOI stages are certification involvement activities; they
should not be treated as four generic software development phases.

## 21. Relationship Between DO-178C and Its Supplements

DO-178C is the core airborne software document.

Related documents address specific technologies or supporting
information:

Document                            Role

DO-178C                         Core airborne software development
assurance

DO-248C                         Supporting information / FAQs for
DO-178C and DO-278A

DO-330                          Software Tool Qualification
Considerations

DO-331                          Model-Based Development &
Verification Supplement

DO-332                          Object-Oriented Technology &
Related Techniques Supplement

DO-333                          Formal Methods Supplement

DO-254                          Airborne Electronic Hardware

DO-331, DO-332 and DO-333 are intended to be used with DO-178C or
DO-278A when their respective technologies are used.

DO-330 addresses qualification considerations for software tools.

DO-254 addresses airborne electronic hardware and therefore belongs to
the broader hardware assurance domain rather than being a DO-178C
software supplement.

## 22. Practical V&V Example

Consider a fictional airborne actuator controller.

Requirement

REQ-ACT-001

When the system is enabled and a valid close command is received,
the software shall command the actuator to the CLOSED state.
Otherwise, the software shall not issue the close command.

Step 1 --- Identify conditions

A = System Enabled
B = Valid Close Command

Decision:

D = A AND B

Step 2 --- Develop requirements-based tests

Test     A   B Expected

T01      F   F No close command
T02      F   T No close command
T03      T   F No close command
T04      T   T Close command

Step 3 --- Select MC/DC tests

A suitable MC/DC set is:

T02: F,T -> F
T03: T,F -> F
T04: T,T -> T

Independence:

A:
T02 -> T04
B:
T03 -> T04

Step 4 --- Traceability

REQ-ACT-001
     |
     +----> TEST-ACT-001
     |
     +----> TEST-ACT-002
     |
     +----> TEST-ACT-003
     |
     +----> Verification Result
     |
     +----> Coverage Evidence

Step 5 --- Verification evidence

A realistic evidence package could contain:

Requirement identifier

Test case identifier

Test procedure

Input values

Expected result

Actual result

Pass/fail

Test environment/configuration

Software baseline

Test execution record

Traceability

Coverage analysis

Problem report, if applicable

This is a demonstration only; it is not a certification artifact.

## 23. Repository Demonstrations & References

The repository should turn the concepts above into practical
demonstrations.

Recommended demonstrations:

Requirements-Based Testing

Verification/Requirements-Based-Testing/

Include:

Fictional requirements

Test conditions

Test cases

Test procedures

Expected results

Traceability matrix

Example execution results

Structural Coverage

Structural-Coverage/
├── Statement-Coverage/
├── Decision-Coverage/
└── MC-DC/

Include worked examples and analysis showing how test cases achieve the
relevant coverage objective.

HSIT

Verification/HSIT/

Demonstrate:

Hardware/software interface assumptions

Test setup

Stimulus

Expected behavior

Interface verification

Result analysis

References

Use authoritative sources for claims about certification and the
standards:

RTCA --- DO-178C and related software standards
<https://www.rtca.org/do-178/>

FAA AC 20-115D --- Airborne Software Development Assurance Using
EUROCAE ED-12( ) and RTCA DO-178( )
<https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf>

FAA AC 20-115D document page
<https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1032046>

FAA --- Software and Airborne Electronic Hardware
<https://www.faa.gov/aircraft/air_cert/design_approvals/air_software/software_regs>

Reference discipline

This repository intentionally does not reproduce the copyrighted
DO-178C standard.

Instead:

Explain concepts in original wording.

Cite authoritative sources.

Clearly distinguish standard-derived requirements from engineering
interpretation.

Label fictional examples as demonstrations.

Never publish employer/customer proprietary requirements, source
code, test procedures, certification evidence, or confidential data.

Key Takeaways

DO-178C should be understood as a software development assurance
framework, not merely a testing checklist.

For a V&V engineer, the most important practical relationships are:

Requirements
     |
     v
Verification Planning
     |
     v
Verification Methods
     |
     +--> Reviews
     +--> Analysis
     +--> Testing
     +--> Coverage
     |
     v
Objective Evidence
     |
     v
Traceability
     |
     v
Configuration / Quality Control
     |
     v
Certification Evidence

The strength of a verification process comes from the combination of
appropriate methods, objective evidence, traceability, configuration
control, independence where applicable, and disciplined review of
anomalies and coverage.

Disclaimer

This document is an independently written technical study/reference
guide. It does not reproduce RTCA DO-178C or any other copyrighted
standard.

All examples in this repository are fictional, generalized, or
independently created for educational and portfolio purposes. No
proprietary source code, confidential requirements, customer
information, restricted test procedures, certification data, or
employer-owned artifacts are intentionally included.

For authoritative requirements and certification guidance, consult the
applicable official RTCA/EUROCAE documents and the certification
authority's current guidance.

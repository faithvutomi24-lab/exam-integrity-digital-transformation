# Exam Integrity Digital Transformation

## Project Overview

This self-directed portfolio project explores how online examination monitoring could be improved through Business Analysis, process analysis, requirements definition, and a technical proof of concept.

The project investigates challenges including false flags, missed suspicious activity, facial-detection limitations, and unreliable network connectivity.

The proposed future-state approach combines technology with human review rather than relying solely on automated decisions.

## Problem Statement

Online examination environments can experience challenges such as:

- False or unnecessary flags
- Missed unusual activity
- Facial-detection limitations
- Environmental conditions affecting detection
- Unreliable network connectivity
- Over-reliance on automated monitoring

The project explores how these challenges could be addressed through a combination of process improvements, technology, and human oversight.

## Business Analysis Approach

The project followed a structured Business Analysis approach:

1. Stakeholder Analysis using CATWOE
2. Current-State Analysis
3. Future-State Analysis
4. Gap Analysis
5. Requirements Definition
6. Process Modelling
7. Technical Proof of Concept
8. Testing and Validation
9. Change Management Considerations

## Stakeholder Analysis

Stakeholders considered in the analysis included:

- Students
- Invigilators
- Educational institutions
- Academic staff
- Technology teams
- Institution management

The CATWOE framework was used to explore the different stakeholder perspectives and the wider system involved in online examination monitoring.

## Current State

The current-state analysis identified challenges around detection accuracy, false flags, missed unusual activity, network reliability, and the need for human judgement when reviewing incidents.

## Future State

The proposed future-state concept incorporates:

- Multiple detection signals
- Human invigilator review
- Secondary-camera capability
- Facial detection
- Low-bandwidth resilience
- Incident logging
- Review and escalation processes

The objective is to provide better decision support while keeping human review involved in important decisions.

## Requirements

### Functional Requirements

The proposed solution should:

- Detect the presence or absence of a face
- Identify when multiple faces are visible
- Detect defined unusual conditions
- Record incidents
- Trigger a human-review indication when appropriate
- Provide session information after monitoring ends

### Non-Functional Requirements

The proposed solution should consider:

- Reliability
- Usability
- Performance
- Network resilience
- Privacy
- Human oversight

## Prototype

A Python and OpenCV proof of concept was developed in VS Code.

The prototype demonstrates:

- Face detection
- No-face detection
- Multiple-face detection
- Unusual incident detection
- Incident counting
- Human-review flagging
- Event logging
- Session summary

The prototype is a technical proof of concept and does not determine whether a learner has cheated.

## Testing

The prototype was tested using several scenarios:

| Test | Result |
|---|---|
| Face detection | PASS |
| No-face detection | PASS |
| Multiple-face detection | PASS |
| Unusual incident detection | PASS |
| Session summary | PASS |

During initial testing, an issue was identified in the incident-counting logic. The counter was increasing repeatedly while the same condition remained active.

The logic was reviewed, the root cause was identified, and the counting mechanism was adjusted. The prototype was then retested successfully.

Detailed testing results are available in the `testing` folder.

## Evidence

Screenshots demonstrating the prototype's tested behaviours are available in the `screenshots` folder.

The evidence includes:

- Face detection
- No-face detection
- Multiple-face detection
- Unusual incident detection
- Session summary

## Case Study

The complete Business Analysis case study is available here:

**[View the Full Case Study PDF](https://drive.google.com/file/d/1KBsBtcfR2BZnxyYh5nOPWHWx-Fpjc8m1/view?usp=sharing)**

Replace the placeholder above with your Google Drive PDF link before committing the README.

## Technologies Used

- Python
- OpenCV
- VS Code

## Project Structure

```text
exam-integrity-digital-transformation/
│
├── README.md
│
├── prototype/
│   ├── exam_monitor.py
│   └── haarcascade_frontalface_default.xml
│
├── testing/
│   └── testing-results.md
│
├── screenshots/
│   ├── face-detected.png
│   ├── no-face-detected.png
│   ├── multiple-faces.png
│   ├── incident-detection.png
│   └── session-summary.png
│
└── Faith_Khosa_Exam_Integrity_Digital_Transformation_Case_Study.pdf

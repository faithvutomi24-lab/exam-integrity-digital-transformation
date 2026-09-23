# Exam Integrity Digital Transformation

## Project Overview

This portfolio project explores how online examination monitoring could be improved through Business Analysis, process analysis, requirements definition, and a technical proof of concept.

The project investigates challenges such as false flags, missed suspicious activity, facial-detection limitations, and unreliable network connectivity.

The proposed future-state approach combines technology with human review rather than relying solely on automated decisions.

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

## Key Requirements

The proposed solution includes:

- Multiple detection signals
- Human invigilator review
- Secondary-camera capability
- Facial detection
- Low-bandwidth resilience
- Incident logging
- Review and escalation processes

## Prototype

A Python and OpenCV proof of concept was developed to demonstrate:

- Face detection
- No-face detection
- Multiple-face detection
- Incident counting
- Human-review flagging
- Event logging
- Session summary

The prototype is a technical proof of concept and does not determine whether a learner has cheated.

## Testing

The prototype was tested against several scenarios, including:

- One face detected
- No face detected
- Multiple faces detected
- Unusual incident detection
- Multiple incidents resulting in a human-review flag
- Session completion and summary

During testing, an issue was identified in the incident-counting logic. The counter was initially increasing repeatedly while the same condition remained active. The logic was corrected so that the incident state was handled appropriately, and the prototype was retested.

## Case Study

The complete Business Analysis case study is available here:

https://drive.google.com/file/d/1KBsBtcfR2BZnxyYh5nOPWHWx-Fpjc8m1/view?usp=sharing
## Technologies Used

- Python
- OpenCV
- VS Code

## Limitations

This project is a self-directed proof of concept.

It does not:

- Determine whether cheating has occurred
- Replace human invigilators
- Implement a production-ready secondary-camera system
- Implement full low-bandwidth recovery
- Provide live invigilator integration
- Represent a production-ready examination platform

## Purpose

The purpose of this project is to demonstrate how Business Analysis techniques can be combined with a technical proof of concept to investigate a real-world problem, define requirements, identify gaps, test a proposed solution, and communicate limitations.

# Testing Results

## Test 1: Face Detection

**Expected Result:**  
A visible face should be detected by the system.

**Result:**  
The system detected the visible face and displayed the face-detection result.

**Evidence:**  
`face-detected.png`

**Status:**  
PASS

---

## Test 2: No Face Detection

**Expected Result:**  
The system should identify when no face is visible.

**Result:**  
The system identified that no face was detected.

**Evidence:**  
`no-face-detected.png`

**Status:**  
PASS

---

## Test 3: Multiple Face Detection

**Expected Result:**  
The system should identify when multiple faces are visible.

**Result:**  
The system detected multiple faces.

**Evidence:**  
`multiple-faces.png`

**Status:**  
PASS

---

## Test 4: Unusual Incident Detection

**Expected Result:**  
An unusual condition should be detected and recorded as an incident.

**Result:**  
The prototype detected the unusual situation and displayed the incident indication.

**Evidence:**  
`incident-detection.png`

**Status:**  
PASS

---

## Test 5: Session Summary

**Expected Result:**  
The system should provide a summary when the monitoring session ends.

**Result:**  
After the camera session ended, the prototype displayed the session summary in the VS Code terminal.

**Evidence:**  
`session-summary.png`

**Status:**  
PASS

---

## Testing Issue Identified

During initial testing, the incident counter increased repeatedly while the same condition remained active.

The logic was reviewed and the root cause was identified. The counting mechanism was adjusted to prevent the same incident from being repeatedly counted across consecutive frames.

The prototype was then retested successfully.

## Testing Conclusion

The prototype successfully demonstrated the tested detection and monitoring behaviours. The testing also demonstrated an iterative problem-solving process by identifying and correcting an issue in the incident-counting logic.

The results represent testing of a self-directed proof of concept and should not be interpreted as validation of a production-ready examination-monitoring system.

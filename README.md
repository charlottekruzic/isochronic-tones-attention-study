# Isochronic tones and its effect on attention
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](https://opensource.org/licenses/MIT)

This repository contains the code and resources used for my research project (TER - Travail d'Étude et de Recherche) at the University of Strasbourg, supervised by Axel HUTT.

## 📃 Project description

This study explores the influence of auditory stimulation using 500Hz isochronic tones with an alpha-band beating frequency of 10Hz on reaction times, which are used as indicators of attention. The experiment evaluates whether listening to isochronic tones during a reaction time task influences the attentional performance of participants.

## 📁 Repository structure

```
isochronic-tones-attention-study/
├── experiment/               # PsychoPy implementation
├── sound_generation/         # Python code to generate audio stimuli
├── sounds/                   # Pre-generated audio files
├── project-report-fr.pdf     # Full research report (in French)
├── LICENCE                   # MIT License
└── README.md
```

## 🔧 Methodology
### 🧪 Experiment design
- Adapted from Deary and Liewald's ["Simple Choice Reaction Time Task"](https://link.springer.com/article/10.3758/s13428-010-0024-1) program, implemented using PsychoPy.
- Includes a custom training phase to familiarize participants with the task
- Two sessions per participant with:
    - Brown noise only (control)
    - Brown noise + isochronic tones (stimulation)
- 300 trials per condition, counterbalanced design

### 🎵 Sound generation
- Python-generated stimuli using scipy and colorednoise:
    - 500Hz isochronic tones with a 10Hz beating frequency
    - Brown noise background (neutral acoustic environment)
    - Compliant with Shannon-Nyquist theorem (44.1kHz sampling)

### 🖥️ Experiment protocol
- Training phase (100 trials, no sound)
- Three test phases per session (300 trials each, sound):
    - Visual color discrimination task
    - Reaction time and accuracy recording
- Identical hardware/software for all participants

### 📊 Data collection
- Automated logging via PsychoPy:
    - Reaction times
    - Response accuracy
- 12 000 data points total (6 participants × 2 000 trials)

### 📈 Data analysis
- Statistical methods:
    - Mann-Whitney U tests
    - Median/IQR comparison across conditions
    - Individual vs. group-level analysis
- Data cleaning:
    - Exclusion of outliers
    - Error trials removed from RT analysis

## 📌 Summary of results
- Significant reduction in reaction times with isochronic tones
- No significant effect on error rates
- Individual variability in responses

## 📑 Full documentation
For complete methodology, detailed results, statistical analysis, and in-depth discussion, please refer to the comprehensive [research report (in French)](project-report-fr.pdf) included in this repository.
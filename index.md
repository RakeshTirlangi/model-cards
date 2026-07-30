---
layout: default
title: 3D Medical Foundation Models Showcase
---

# 3D Medical Foundation Models Showcase

This document provides a high-level summary of the 3D vision-language and foundation models currently researched and documented. Click on the model names to view their detailed model cards.

These models share a focus on processing native 3D volumetric data (like CT and MRI scans) primarily for image-to-text report generation tasks.

| Model Name | Modality | Size | Best/Primary Task |
|---|---|---|---|
| [**BrainGPT**](./BrainGPT.md) | 3D Non-contrast Head/Brain CT | ~7 Billion | 3D Brain CT Radiology Report Generation (High-precision pathological focus) |
| [**Merlin**](./Merlin.md) | 3D CT Volumes (Head, Chest, Abdomen) | ~100M - 200M | Zero-Shot Findings Classification & 3D Semantic Segmentation (Compute efficient) |
| [**Med3DVLM**](./Med3DVLM.md) | 3D Medical Volumes (General CT/MRI) | ~7 Billion | Pan-Organ Report Generation & Medical Visual Question Answering (VQA) |
| [**RAD3D-Prefix**](./RAD3D-Prefix.md) | 3D CT Volumes (Pan-organ applications) | ~1 Billion | Parameter-Efficient Report Generation & Clinical Hallucination Mitigation |
| [**VILA-M3**](./VILA-M3.md) | 3D CT/MRI Volumes and 2D Images | **8B** (Also 3B, 13B, 40B) | Grounded Report Generation via Dynamic Expert Tool Routing (Radiology Agent) |
| [**MedGemma 1.5**](./MedGemma-1.5.md) | 3D CT/MRI, WSI, Longitudinal Scans | **4 Billion** | Native 3D Interpretation & Multimodal Clinical Q&A (Locally deployable) |

---

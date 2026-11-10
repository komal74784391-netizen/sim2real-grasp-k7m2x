# sim2real-grasp

Reference implementation for **"Grasp Affordance Transfer via Simulation
Pretraining"** (CoRL 2024).

The repository contains the affordance predictor, the simulation pretraining
pipeline and the policy distillation scripts described in the paper.

## Layout

- `src/affordance/model.py` - affordance predictor
- `src/sim/pretrain.py` - simulation pretraining loop
- `scripts/pretrain.py` - entry point for pretraining
- `configs/corl.yaml` - paper configuration

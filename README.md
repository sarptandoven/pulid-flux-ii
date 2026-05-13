# PuLID Flux II Replicate Deployment

Replicate/Cog deployment package for generating professional headshots with a PuLID Flux workflow.

## Files

- `predict.py`: Replicate predictor implementation
- `headshot_workflow.json`: ComfyUI workflow used by the predictor
- `replicate.yaml`: Replicate deployment configuration
- `requirements.txt`: Python runtime dependencies

## Local setup

```bash
pip install -r requirements.txt
python -m py_compile predict.py
```

For full local inference, install the model weights and ComfyUI dependencies expected by `predict.py` and `headshot_workflow.json`.

## Replicate deployment

```bash
cog predict -i image=@input.jpg
```

Model weights and generated outputs are intentionally not committed. Keep downloaded checkpoints under ignored `models/` or `checkpoints/` directories.

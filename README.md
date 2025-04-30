# PuLID Flux II Replicate Deployment

This package provides a Replicate deployment for the PuLID Flux II model, which can generate professional headshots from input images.

## Features

- Generate professional headshots from input images
- Customizable style options
- Multiple output samples
- Adjustable guidance scale and steps

## Usage

### Input Parameters

- `image`: (required) URL or path to the input image
- `style`: (optional) Style of the headshot (default: "professional")
- `num_samples`: (optional) Number of samples to generate (default: 1)
- `guidance_scale`: (optional) Guidance scale for generation (default: 7.5)
- `steps`: (optional) Number of inference steps (default: 30)

### Example API Call

```python
import replicate

output = replicate.run(
    "yourusername/pulid-flux-ii",
    input={
        "image": "https://example.com/input.jpg",
        "style": "professional",
        "num_samples": 1,
        "guidance_scale": 7.5,
        "steps": 30
    }
)
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the model locally:
```bash
python predict.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
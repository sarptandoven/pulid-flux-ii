import os
import torch
import numpy as np
from PIL import Image
from typing import Optional, List
from pydantic import BaseModel, Field

class Input(BaseModel):
    image: str = Field(..., description="URL or path to the input image")
    style: str = Field(default="professional", description="Style of the headshot")
    num_samples: int = Field(default=1, ge=1, le=4, description="Number of samples to generate")
    guidance_scale: float = Field(default=7.5, ge=1.0, le=20.0, description="Guidance scale for generation")
    steps: int = Field(default=30, ge=10, le=50, description="Number of inference steps")

def load_workflow():
    """Load the headshot generation workflow"""
    workflow_path = os.path.join(os.path.dirname(__file__), "headshot_workflow.json")
    with open(workflow_path, "r") as f:
        return f.read()

def process_image(image_path: str, workflow: str, params: dict) -> List[str]:
    """Process the input image using PuLID Flux II model"""
    try:
        # Load and validate the input image
        image = Image.open(image_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
            
        # Prepare the workflow with parameters
        workflow_params = {
            "image": image_path,
            "workflow": workflow,
            **params
        }
        
        # Process the image through the model
        outputs = []
        for _ in range(params.get("num_samples", 1)):
            result = process_single_image(workflow_params)
            outputs.append(result)
            
        return outputs
        
    except Exception as e:
        raise Exception(f"Error processing image: {str(e)}")

def process_single_image(params: dict) -> str:
    """Process a single image through the model"""
    try:
        # Initialize model components
        model = load_model()
        
        # Apply the workflow
        result = model.process(**params)
        
        return result
        
    except Exception as e:
        raise Exception(f"Error in single image processing: {str(e)}")

def predict(input: Input) -> List[str]:
    """Main prediction function for Replicate deployment"""
    try:
        # Load the workflow
        workflow = load_workflow()
        
        # Process the image
        outputs = process_image(
            input.image,
            workflow,
            {
                "style": input.style,
                "num_samples": input.num_samples,
                "guidance_scale": input.guidance_scale,
                "steps": input.steps
            }
        )
        
        return outputs
        
    except Exception as e:
        raise Exception(f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    # Test the prediction
    test_input = Input(
        image="sarp.jpeg",
        style="professional",
        num_samples=1,
        guidance_scale=7.5,
        steps=30
    )
    result = predict(test_input)
    print(result) 
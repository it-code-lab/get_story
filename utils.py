import json
import os

def save_data(story, images, metadata, output_dir="output"):
    """Saves the story, images, and metadata to files."""
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "story.json"), "w") as f:
        json.dump({"story": story, "images": images, "metadata": metadata}, f)
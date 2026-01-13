import yaml
import json
import random

FPS = 24
WIDTH = 768
HEIGHT = 432

def new_id(counter):
    counter[0] += 1
    return str(counter[0])


def main():
    with open("jingzhou_ad_video.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    scenes = data["scenes"]
    global_prompt = data["global_prompt"]

    workflow = {}
    node_id = [0]

    # ---------- Global Nodes ----------
    ckpt_id = new_id(node_id)
    workflow[ckpt_id] = {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "realisticVisionV51.safetensors"
        }
    }

    motion_id = new_id(node_id)
    workflow[motion_id] = {
        "class_type": "AnimateDiffLoader",
        "inputs": {
            "model_name": "mm_sd_v15_v2.ckpt"
        }
    }

    apply_id = new_id(node_id)
    workflow[apply_id] = {
        "class_type": "AnimateDiffApply",
        "inputs": {
            "motion_model": [motion_id, 0],
            "model": [ckpt_id, 0]
        }
    }

    decoded_images = []

    # ---------- Scenes ----------
    for idx, scene in enumerate(scenes, 1):
        pos_prompt = f"{global_prompt['positive']}, {scene['prompt']['positive']}"
        neg_prompt = f"{global_prompt['negative']}, {scene['prompt'].get('negative', '')}"

        # Positive
        pos_id = new_id(node_id)
        workflow[pos_id] = {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": pos_prompt,
                "clip": [ckpt_id, 1]
            }
        }

        # Negative
        neg_id = new_id(node_id)
        workflow[neg_id] = {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": neg_prompt,
                "clip": [ckpt_id, 1]
            }
        }

        # Latent
        frames = int(scene["duration_sec"] * FPS)
        latent_id = new_id(node_id)
        workflow[latent_id] = {
            "class_type": "EmptyLatentImage",
            "inputs": {
                "width": WIDTH,
                "height": HEIGHT,
                "batch_size": frames
            }
        }

        # Sampler
        sampler_id = new_id(node_id)
        workflow[sampler_id] = {
            "class_type": "KSampler",
            "inputs": {
                "seed": random.randint(1, 10**9),
                "steps": 20,
                "cfg": 7,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1.0,
                "model": [apply_id, 0],
                "positive": [pos_id, 0],
                "negative": [neg_id, 0],
                "latent_image": [latent_id, 0]
            }
        }

        # Decode
        decode_id = new_id(node_id)
        workflow[decode_id] = {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": [sampler_id, 0],
                "vae": [ckpt_id, 2]
            }
        }

        decoded_images.append([decode_id, 0])

    # ---------- Concat ----------
    concat_id = new_id(node_id)
    workflow[concat_id] = {
        "class_type": "ImageBatchConcat",
        "inputs": {
            "images": decoded_images
        }
    }

    # ---------- Save ----------
    save_id = new_id(node_id)
    workflow[save_id] = {
        "class_type": "SaveImage",
        "inputs": {
            "images": [concat_id, 0],
            "filename_prefix": "jingzhou_full_video"
        }
    }

    with open("jingzhou_full_video_workflow.json", "w", encoding="utf-8") as f:
        json.dump(workflow, f, indent=2, ensure_ascii=False)

    print("✅ 单一 ComfyUI Workflow 已生成：jingzhou_full_video_workflow.json")


if __name__ == "__main__":
    main()

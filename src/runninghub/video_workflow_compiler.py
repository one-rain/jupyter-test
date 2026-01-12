import json
import copy
import random

FPS = 24

with open("business_script.json", "r", encoding="utf-8") as f:
    script = json.load(f)

with open("comfyui_scene_template.json", "r", encoding="utf-8") as f:
    template = json.load(f)

def compile_scene(scene, idx):
    wf = copy.deepcopy(template)

    frame_count = int(scene["duration_sec"] * FPS)

    def replace(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                obj[k] = replace(v)
        elif isinstance(obj, list):
            return [replace(v) for v in obj]
        elif isinstance(obj, str):
            return (
                obj.replace("__POSITIVE_PROMPT__", scene["prompt"]["positive"])
                   .replace("__NEGATIVE_PROMPT__", scene["prompt"]["negative"])
                   .replace("__OUTPUT_PREFIX__", f"scene_{idx:02d}")
            )
        elif isinstance(obj, int) and obj == -1:
            return frame_count
        return obj

    wf = replace(wf)

    # 手动注入 batch_size & seed
    wf["4"]["inputs"]["batch_size"] = frame_count
    wf["7"]["inputs"]["seed"] = random.randint(1, 999999999)

    return wf

scenes = script["scenes"]

for i, scene in enumerate(scenes, 1):
    wf = compile_scene(scene, i)
    with open(f"scene_{i:02d}_workflow.json", "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)

print("✅ 所有 ComfyUI 工作流已生成")

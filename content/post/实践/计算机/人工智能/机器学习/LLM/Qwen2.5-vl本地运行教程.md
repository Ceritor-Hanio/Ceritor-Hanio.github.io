---
title: "Qwen2.5-vl 本地运行教程"
description: ""
slug: "Qwen2.5-vl本地运行教程"
date: 2025-09-15 00:00:00+0000
categories:
    - 计算机
tags:
    - LLM
weight: 1
---

## 0.前置知识
1. Anaconda
2. Pycharm / VS code
	- [Anaconda + VS code](https://www.bilibili.com/video/BV1Fo46e3EAZ/)

## 1. 配置 Python 环境
```pip
conda create --name Qwen python=3.12
conda activate Qwen

pip install qwen-vl-utils[decord]
pip install transformers
pip install accelerate>=0.26.0

pip install torchvision==0.20.0 -f https://download.pytorch.org/whl/torch_stable.html
# 根据显卡型号自行安装对应版本的torchvision

pip install modelscope
```

## 2. 下载模型文件
将python环境导入IDE之后，运行下面代码。
```python
from modelscope import snapshot_download  
model_dir = snapshot_download('Qwen/Qwen2.5-VL-3B-Instruct',local_dir=r"D:\Qwen\Qwen-3b")
#可以装在一个自己喜欢的位置。
```

## 3. 下载并运行源码

1. 命令行运行：（这一步可以跳过）
```bash
git clone https://github.com/QwenLM/Qwen2-VL
cd Qwen2-vl
```
2. 运行官方提供的代码（我微调过）
[魔搭社区](https://www.modelscope.cn/models/Qwen/Qwen2.5-VL-7B-Instruct)

```python
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor  
from qwen_vl_utils import process_vision_info  
import torch  
  
# default: Load the model on the available device(s)  
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(  
    r"D:\Qwen\Qwen-3b",  
    torch_dtype=torch.float16,  # 推荐使用float16节省GPU内存  
    device_map="cuda",  # 强制使用GPU  
    low_cpu_mem_usage=True  # 减少CPU内存占用  
)  
  
# We recommend enabling flash_attention_2 for better acceleration and memory saving, especially in multi-image and video scenarios.  
# model = Qwen2_5_VLForConditionalGeneration.from_pretrained(  
#     "Qwen/Qwen2.5-VL-7B-Instruct",  
#     torch_dtype=torch.bfloat16,  
#     attn_implementation="flash_attention_2",  
#     device_map="auto",  
# )  
  
# default processor  
processor = AutoProcessor.from_pretrained(r"D:\Qwen\Qwen-3b")  
  
# The default range for the number of visual tokens per image in the model is 4-16384.  
# You can set min_pixels and max_pixels according to your needs, such as a token range of 256-1280, to balance performance and cost.  
# min_pixels = 256*28*28  
# max_pixels = 1280*28*28  
# processor = AutoProcessor.from_pretrained("Qwen/Qwen2.5-VL-7B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)  
  
messages = [  
    {  
        "role": "user",  
        "content": [  
            {  
                "type": "image",  
                "image": r"img/",  #此处可以导入本地图片或视频
            },  
            {"type": "text", "text": "用中文描述图片"},  
        ],  
    }  
]  
  
# Preparation for inference  
text = processor.apply_chat_template(  
    messages, tokenize=False, add_generation_prompt=True  
)  
image_inputs, video_inputs = process_vision_info(messages)  
inputs = processor(  
    text=[text],  
    images=image_inputs,  
    videos=video_inputs,  
    padding=True,  
    return_tensors="pt",  
)  
inputs = inputs.to(model.device)  
  
# Inference: Generation of the output  
generated_ids = model.generate(**inputs, max_new_tokens=1024)  
generated_ids_trimmed = [  
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)  
]  
output_text = processor.batch_decode(  
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False  
)  
print(output_text)
```

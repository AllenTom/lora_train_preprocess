import contextlib
import os

import torch

from modules import interrogate

device = torch.device('cpu')
devCPU = cpu = torch.device("cpu")
dtype = torch.float
device_interrogate = torch.device("cpu")
precision = "autocast"  # autocast or full
no_half = False
interrogate_keep_models_in_memory = False
interrogator = interrogate.InterrogateModels("interrogate")
interrogate_clip_skip_categories = []
clip_models_path = "./assets"
danbooru_model_path = "./assets/model-resnet_custom_v3.pt"
blip_model_path = "./assets/model_base_caption_capfilt_large.pth"
med_config = os.path.join("./repositories/BLIP/configs", "med_config.json")
interrogate_clip_dict_limit = 1500
interrogate_clip_num_beams = 1
interrogate_clip_min_length =  24
interrogate_clip_max_length = 48
lowvram = False
medvram = False
interrogate_return_ranks = False
def autocast(disable=False):
    if disable:
        return contextlib.nullcontext()

    if dtype == torch.float32 or precision == "full":
        return contextlib.nullcontext()

    return torch.autocast("cuda")
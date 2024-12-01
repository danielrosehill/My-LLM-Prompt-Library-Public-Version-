---
title: "Read this terminal output, explain what went wrong."
---

## The problem

Linux terminal outputs can be incredibly overwhelming.

Trying to run `pip install whisper-live` gave me this undelightful sprawling mass of text:

```bash
daniel@home:~> pip install whisper-live
Collecting whisper-live
  Using cached whisper_live-0.5.1-py3-none-any.whl.metadata (8.9 kB)
Collecting PyAudio (from whisper-live)
  Using cached PyAudio-0.2.14.tar.gz (47 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting faster-whisper==1.0.1 (from whisper-live)
  Using cached faster_whisper-1.0.1-py3-none-any.whl.metadata (14 kB)
Requirement already satisfied: torch in ./anaconda3/lib/python3.12/site-packages (from whisper-live) (2.5.1)
Collecting torchaudio (from whisper-live)
  Using cached torchaudio-2.5.1-cp312-cp312-manylinux1_x86_64.whl.metadata (6.4 kB)
Requirement already satisfied: websockets in ./anaconda3/lib/python3.12/site-packages (from whisper-live) (12.0)
INFO: pip is looking at multiple versions of whisper-live to determine which version is compatible with other requirements. This could take a while.
Collecting whisper-live
  Using cached whisper_live-0.5.0-py3-none-any.whl.metadata (8.9 kB)
  Using cached whisper_live-0.4.1-py3-none-any.whl.metadata (6.6 kB)
  Using cached whisper_live-0.4.0-py3-none-any.whl.metadata (6.6 kB)
  Using cached whisper_live-0.3.0-py3-none-any.whl.metadata (6.6 kB)
Collecting faster-whisper==0.10.0 (from whisper-live)
  Using cached faster_whisper-0.10.0-py3-none-any.whl.metadata (14 kB)
Collecting whisper-live
  Using cached whisper_live-0.2.1-py3-none-any.whl.metadata (6.6 kB)
  Using cached whisper_live-0.1.0-py3-none-any.whl.metadata (7.7 kB)
  Using cached whisper_live-0.0.11-py3-none-any.whl.metadata (6.2 kB)
Requirement already satisfied: onnxruntime in ./anaconda3/lib/python3.12/site-packages (from whisper-live) (1.20.0)
Collecting ffmpeg-python (from whisper-live)
  Using cached ffmpeg_python-0.2.0-py3-none-any.whl.metadata (1.7 kB)
Requirement already satisfied: scipy in ./anaconda3/lib/python3.12/site-packages (from whisper-live) (1.14.1)
Requirement already satisfied: websocket-client in ./anaconda3/lib/python3.12/site-packages (from whisper-live) (1.8.0)
Collecting av==11.* (from faster-whisper==0.10.0->whisper-live)
  Using cached av-11.0.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.5 kB)
Requirement already satisfied: ctranslate2<5,>=4.0 in ./anaconda3/lib/python3.12/site-packages (from faster-whisper==0.10.0->whisper-live) (4.5.0)
Requirement already satisfied: huggingface-hub>=0.13 in ./anaconda3/lib/python3.12/site-packages (from faster-whisper==0.10.0->whisper-live) (0.26.2)
Collecting tokenizers<0.16,>=0.13 (from faster-whisper==0.10.0->whisper-live)
  Using cached tokenizers-0.15.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.7 kB)
Requirement already satisfied: coloredlogs in ./anaconda3/lib/python3.12/site-packages (from onnxruntime->whisper-live) (15.0.1)
Requirement already satisfied: flatbuffers in ./anaconda3/lib/python3.12/site-packages (from onnxruntime->whisper-live) (24.3.25)
Requirement already satisfied: numpy>=1.21.6 in ./anaconda3/lib/python3.12/site-packages (from onnxruntime->whisper-live) (1.26.4)
Requirement already satisfied: packaging in ./anaconda3/lib/python3.12/site-packages (from onnxruntime->whisper-live) (24.1)
Requirement already satisfied: protobuf in ./anaconda3/lib/python3.12/site-packages (from onnxruntime->whisper-live) (5.28.3)
Requirement already satisfied: sympy in ./anaconda3/lib/python3.12/site-packages (from onnxruntime->whisper-live) (1.13.1)
Requirement already satisfied: future in ./anaconda3/lib/python3.12/site-packages (from ffmpeg-python->whisper-live) (0.18.3)
Requirement already satisfied: filelock in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (3.13.1)
Requirement already satisfied: typing-extensions>=4.8.0 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (4.11.0)
Requirement already satisfied: networkx in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (3.3)
Requirement already satisfied: jinja2 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (3.1.4)
Requirement already satisfied: fsspec in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (2024.6.1)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.4.127 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (12.4.127)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.4.127 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (12.4.127)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.4.127 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (12.4.127)
Requirement already satisfied: nvidia-cudnn-cu12==9.1.0.70 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (9.1.0.70)
Requirement already satisfied: nvidia-cublas-cu12==12.4.5.8 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (12.4.5.8)
Requirement already satisfied: nvidia-cufft-cu12==11.2.1.3 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (11.2.1.3)
Requirement already satisfied: nvidia-curand-cu12==10.3.5.147 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (10.3.5.147)
Requirement already satisfied: nvidia-cusolver-cu12==11.6.1.9 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (11.6.1.9)
Requirement already satisfied: nvidia-cusparse-cu12==12.3.1.170 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (12.3.1.170)
Requirement already satisfied: nvidia-nccl-cu12==2.21.5 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (2.21.5)
Requirement already satisfied: nvidia-nvtx-cu12==12.4.127 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (12.4.127)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.4.127 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (12.4.127)
Requirement already satisfied: triton==3.1.0 in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (3.1.0)
Requirement already satisfied: setuptools in ./anaconda3/lib/python3.12/site-packages (from torch->whisper-live) (75.6.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./anaconda3/lib/python3.12/site-packages (from sympy->onnxruntime->whisper-live) (1.3.0)
Requirement already satisfied: pyyaml<7,>=5.3 in ./anaconda3/lib/python3.12/site-packages (from ctranslate2<5,>=4.0->faster-whisper==0.10.0->whisper-live) (6.0.1)
Requirement already satisfied: requests in ./anaconda3/lib/python3.12/site-packages (from huggingface-hub>=0.13->faster-whisper==0.10.0->whisper-live) (2.32.3)
Requirement already satisfied: tqdm>=4.42.1 in ./anaconda3/lib/python3.12/site-packages (from huggingface-hub>=0.13->faster-whisper==0.10.0->whisper-live) (4.66.5)
Requirement already satisfied: humanfriendly>=9.1 in ./anaconda3/lib/python3.12/site-packages (from coloredlogs->onnxruntime->whisper-live) (10.0)
Requirement already satisfied: MarkupSafe>=2.0 in ./anaconda3/lib/python3.12/site-packages (from jinja2->torch->whisper-live) (2.1.3)
Requirement already satisfied: charset-normalizer<4,>=2 in ./anaconda3/lib/python3.12/site-packages (from requests->huggingface-hub>=0.13->faster-whisper==0.10.0->whisper-live) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in ./anaconda3/lib/python3.12/site-packages (from requests->huggingface-hub>=0.13->faster-whisper==0.10.0->whisper-live) (3.7)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./anaconda3/lib/python3.12/site-packages (from requests->huggingface-hub>=0.13->faster-whisper==0.10.0->whisper-live) (2.2.3)
Requirement already satisfied: certifi>=2017.4.17 in ./anaconda3/lib/python3.12/site-packages (from requests->huggingface-hub>=0.13->faster-whisper==0.10.0->whisper-live) (2024.8.30)
Using cached whisper_live-0.0.11-py3-none-any.whl (25 kB)
Using cached faster_whisper-0.10.0-py3-none-any.whl (1.5 MB)
Using cached av-11.0.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (34.1 MB)
Using cached ffmpeg_python-0.2.0-py3-none-any.whl (25 kB)
Using cached torchaudio-2.5.1-cp312-cp312-manylinux1_x86_64.whl (3.4 MB)
Using cached tokenizers-0.15.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.6 MB)
Building wheels for collected packages: PyAudio
  Building wheel for PyAudio (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for PyAudio (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [14 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build/lib.linux-x86_64-cpython-312/pyaudio
      copying src/pyaudio/__init__.py -> build/lib.linux-x86_64-cpython-312/pyaudio
      running build_ext
      building 'pyaudio._portaudio' extension
      creating build/temp.linux-x86_64-cpython-312/src/pyaudio
      gcc -pthread -B /home/daniel/anaconda3/compiler_compat -fno-strict-overflow -DNDEBUG -O2 -Wall -fPIC -O2 -isystem /home/daniel/anaconda3/include -fPIC -O2 -isystem /home/daniel/anaconda3/include -fPIC -I/usr/local/include -I/usr/include -I/home/daniel/anaconda3/include/python3.12 -c src/pyaudio/device_api.c -o build/temp.linux-x86_64-cpython-312/src/pyaudio/device_api.o
      src/pyaudio/device_api.c:9:10: fatal error: portaudio.h: No such file or directory
          9 | #include "portaudio.h"
            |          ^~~~~~~~~~~~~
      compilation terminated.
      error: command '/usr/bin/gcc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for PyAudio
Failed to build PyAudio
ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (PyAudio)
```

Ugh ... where to even start.

## LLM to the rescue

This prompt is very simple:

>Read this terminal output and explain simply what went wrong. 
>Context: operating system is OpenSUSE Tumbleweed.

The second line is necessary because while the LLM can successfully guess that it's a Linux distribution based upon the file path structure (forward slashes), that's not enough to hone it in on the distro.

And if it guesses the distro wrong, the resolutions it suggests will also potentially be correct.

But with that simple piece of guidance it has enough to help.

## Much better!

**Prompting this and pasting the terminal output got me this which is vastly easier to understand:**

The installation of whisper-live failed because it couldn't build PyAudio, which is one of its dependencies. The specific error occurred because the portaudio.h header file is missing on your OpenSUSE Tumbleweed system.

To fix this, you need to install the PortAudio development package first. On OpenSUSE, you can install it by running:

```bash
sudo zypper install portaudio-devel
```

After installing the development package, try installing whisper-live again with:

```bash
pip install whisper-live
```

 
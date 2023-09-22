# 基于LLM的自动故障分析平台

## 环境准备

```bash
conda activate FeatureRobot
pip3 install -r requirements.txt
```

## 常见错误

###  numpy文件不存在错误
```bash
ImportError: dlopen(/Library/Python/3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so, 0x0002): tried: '/Library/Python/3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so' (mach-o file, but is an incompatible architecture (have 'arm64', need 'x86_64')), '/System/Volumes/Preboot/Cryptexes/OS/Library/Python/3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so' (no such file), '/Library/Python/3.9/site-packages/numpy/core/_multiarray_umath.cpython-39-darwin.so' (mach-o file, but is an incompatible architecture (have 'arm64', need 'x86_64'))
```

解决方案： 
```bash
conda install numpy
```
# Power Equipment Image Dataset

<p align="center">
  <img src='https://raw.githubusercontent.com/xiongsiheng/Power-equipment-image-dataset/main/misc/substation.jpg' width=550>
</p>
<br>
<p align="center">
  <img src='https://raw.githubusercontent.com/xiongsiheng/Power-equipment-image-dataset/main/misc/transmission_line.JPG' width=550>
</p>

## Introduction
The **Power Equipment Image Dataset** consists of four subsets designed for various computer vision tasks related to power systems:

1. **Substation Object Detection**
2. **Transmission Line Classification**
3. **Transmission Line Object Detection**
4. **Drone-captured transmission line images**

### 1. Substation Object Detection

This subset contains **753 substation images** with **polygon mask annotations**.
It includes **18 object categories**:

`capacitor`, `bus`, `pipe`, `filter`, `GIS`, `bushing`, `switch`, `line`, `PT`, `breaker`, `arrester`, `insulator`, `connecting port`, `CT`, `pedestal`, `resistor`, `tower`, and `frame`.

### 2. Transmission Line Classification

This subset includes **7,635 training images** and **2,002 test images** of transmission lines.
It is divided into **four classes**:

* **Porcelain Post Insulator with Crack**
   (Chinese: 瓷柱绝缘子裂纹, *pinyin*: cí zhù jué yuán zǐ liè wén, abbreviation: `czjyz_lw`)
* **Porcelain Post Insulator Damage**
   (Chinese: 瓷柱绝缘子破损, *pinyin*: cí zhù jué yuán zǐ pò sǔn, abbreviation: `czjyz_ps`)
* **Porcelain Post Insulator Flashover**
   (Chinese: 瓷柱绝缘子闪络, *pinyin*: cí zhù jué yuán zǐ shǎn luò, abbreviation: `czjyz_sl`)
* **Wire Insulation Damage**
   (Chinese: 导线绝缘皮破损, *pinyin*: dǎo xiàn jué yuán pí pò sǔn, abbreviation: `dx_jypps`)

### 3. Transmission Line Object Detection

This subset contains **10,348 transmission line images** annotated with **bounding boxes**, covering **28 categories**:

#### **Surge Arrester Issues**

* **Surge Arrester Discoloration** (Chinese: 避雷器变色, *pinyin*: bì léi qì biàn sè, abbreviation: `blq_bs`)
* **Surge Arrester Insulation Breakdown** (Chinese: 避雷器绝缘击穿, *pinyin*: bì léi qì jué yuán jī chuān, abbreviation: `blq_jyjc`)
* **Surge Arrester Aging** (Chinese: 避雷器老化, *pinyin*: bì léi qì lǎo huà, abbreviation: `blq_lh`)
* **Surge Arrester Loose Nut** (Chinese: 避雷器螺母松动, *pinyin*: bì léi qì luó mǔ sōng dòng, abbreviation: `blq_lmsd`)
* **Surge Arrester Damage** (Chinese: 避雷器破损, *pinyin*: bì léi qì pò sǔn, abbreviation: `blq_ps`)
* **Surge Arrester Ground Lead Missing** (Chinese: 避雷器缺线, *pinyin*: bì léi qì quē xiàn, abbreviation: `blq_qx`)
* **Surge Arrester Detachment** (Chinese: 避雷器脱落, *pinyin*: bì léi qì tuō luò, abbreviation: `blq_tl`)
* **Surge Arrester Ground Lead Broken** (Chinese: 避雷器引线断开, *pinyin*: bì léi qì yǐn xiàn duàn kāi, abbreviation: `blq_yxdk`)

#### **Porcelain Post Insulator Issues**

* **Porcelain Post Insulator with Crack** (Chinese: 瓷柱绝缘子裂纹, *pinyin*: cí zhù jué yuán zǐ liè wén, abbreviation: `czjyz_lw`)
* **Porcelain Post Insulator Damage** (Chinese: 瓷柱绝缘子破损, *pinyin*: cí zhù jué yuán zǐ pò sǔn, abbreviation: `czjyz_ps`)
* **Porcelain Post Insulator Flashover** (Chinese: 瓷柱绝缘子闪络, *pinyin*: cí zhù jué yuán zǐ shǎn luò, abbreviation: `czjyz_sl`)
* **Porcelain Post Insulator Missing Lead** (Chinese: 瓷柱绝缘子缺线, *pinyin*: cí zhù jué yuán zǐ quē xiàn, abbreviation: `czjyz_qx`)

#### **Conductor Issues**

* **Conductor Insulation Damage** (Chinese: 导线绝缘皮破损, *pinyin*: dǎo xiàn jué yuán pí pò sǔn, abbreviation: `dx_jypps`)
* **Conductor Strand Breakage** (Chinese: 导线断股, *pinyin*: dǎo xiàn duàn gǔ, abbreviation: `dx_dg`)
* **Conductor Strand Loosening** (Chinese: 导线松股, *pinyin*: dǎo xiàn sōng gǔ, abbreviation: `dx_sg`)
* **Conductor Vegetation Encroachment** (Chinese: 导线树障, *pinyin*: dǎo xiàn shù zhàng, abbreviation: `dx_sz`)
* **Conductor Contact with Crossarm** (Chinese: 导线与横担接触, *pinyin*: dǎo xiàn yǔ héng dān jiē chù, abbreviation: `dx_yhdjc`)

#### **Composite Insulator Issue**

* **Composite Insulator Damage** (Chinese: 复合绝缘子破损, *pinyin*: fù hé jué yuán zǐ pò sǔn, abbreviation: `fhjyz_ps`)

#### **High-Voltage Conductor Joint Issues**

* **High-Voltage Conductor Joint Overheating** (Chinese: 高压导线接点发热, *pinyin*: gāo yā dǎo xiàn jiē diǎn fā rè, abbreviation: `gydxjd_fh`)
* **High-Voltage Conductor Joint Damage** (Chinese: 高压导线接点破损, *pinyin*: gāo yā dǎo xiàn jiē diǎn pò sǔn, abbreviation: `gydxjd_ps`)

#### **Line Hardware Issues**

* **Line Hardware – Terminal Connection Damage** (Chinese: 金具接线破损, *pinyin*: jīn jù jiē xiàn pò sǔn, abbreviation: `jj_jxps`)
* **Line Hardware – Clamp Crack** (Chinese: 金具线夹裂纹, *pinyin*: jīn jù xiàn jiā liè wén, abbreviation: `jj_xjlw`)
* **Line Hardware – Clamp Loose** (Chinese: 金具线夹松动, *pinyin*: jīn jù xiàn jiā sōng dòng, abbreviation: `jj_xjsd`)

#### **Other Issues**

* **Insulator Shed Chipping** (Chinese: 绝缘子伞盘崩口, *pinyin*: jué yuán zǐ sǎn pán bēng kǒu, abbreviation: `jyspbg`)
* **Bird Nest on Line** (Chinese: 鸟窝, *pinyin*: niǎo wō, abbreviation: `nw`)
* **Foreign Object** (Chinese: 异物, *pinyin*: yì wù, abbreviation: `yw`)
* **Ground Lead Broken** (Chinese: 引线断开, *pinyin*: yǐn xiàn duàn kāi, abbreviation: `yxdk`)

### 4. Drone-Captured Transmission Line Images

This subset consists of approximately **3,000 high-resolution images** of transmission lines captured by drones under real-world conditions.


## Quick Start

Follow the steps below to set up and explore the dataset:

```bash
# Clone the repository
git clone https://github.com/xiongsiheng/Power-equipment-image-dataset.git

# Enter the project directory
cd Power-equipment-image-dataset

# Count the number of unique object types in the substation object detection subset
python src/unique_types_extractor.py

# Generate data statistics for the transmission line object detection subset
python src/data_stat.py

# Copy example images for all classes in the transmission line object detection subset
python src/copy_example_images.py
```

We also provide hugging face link [here](https://huggingface.co/datasets/sxiong/Power-equipment-image-dataset).

## Citation

If you find it useful, please cite our paper.
```
@article{xiong2021object,
  title={Object recognition for power equipment via human-level concept learning},
  author={Xiong, Siheng and Liu, Yadong and Yan, Yingjie and Pei, Ling and Xu, Peng and Fu, Xiaofei and Jiang, Xiuchen},
  journal={IET Generation, Transmission \& Distribution},
  volume={15},
  number={10},
  pages={1578--1587},
  year={2021},
  publisher={Wiley Online Library}
}
```

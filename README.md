This project is a simple demo that utilizes [Andrej Karpathy's makemore project](https://github.com/karpathy/makemore) and data from [the chinese-poetry repository](https://github.com/chinese-poetry/chinese-poetry) to generate Chinese poetry using AI.

#### Data

The data was collected from [the Chinese poetry dataset](https://github.com/chinese-poetry/chinese-poetry) using `collect_poetry_dataset.py`.

Example:

```python
$ python3 collect_poetry_dataset.py -i ./../chinese-poetry -c -st -ss
# Ci
INFO:__main__:Collected 159049 sentences from 23 files
INFO:__main__:Sampled 10 random poems:

# Shi - tang
INFO:__main__:Collected 268283 sentences from 58 files
INFO:__main__:Sampled 10 random poems:

# Shi - song
INFO:__main__:Collected 1099146 sentences from 255 files
INFO:__main__:Sampled 10 random poems:
```

The texts wre placed in `ci.txt`, `shi.txt`, `shi_song.txt`, and `shi_tang.txt` respectively. `shi.txt` is the union of `shi_song.txt` and `shi_tang.txt`.

#### Training

Training was done using `makemore.py` directly.

```python
python3 makemore.py -i shi.txt -o shi_100000 --max-steps 100000
```

#### Sample

To get samples from the latest model checkpoint, run

```python
python makemore.py -i shi.txt -o shi_100000 --sample-only
```

The `ci` dataset is slightly better. The `shi` dataset contains some weird characters and not all sentences are actually the poem. E.g. there are some introductory paragraphs in that dataset.

Some example 宋词：
```
恨暮云弥，不禁风细，世间堪喜。

不堪话，小年狂客，床角伴行人。

福禄千秋，庆此世、娱姿懒牡丹芳。

莫算莫多欢易融，分付蟠桃一谢。
```

Some example 诗：
```
南國江南望，吾家一天去。

萬事漫東山下癡，人間不覺不瑞迷。

上方爲我歡如乎，定不知我姑慚誰。

茅舍疏岩红雪袖，但叹无穷寂寥天。
```
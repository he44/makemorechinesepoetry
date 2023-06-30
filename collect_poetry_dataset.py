"""
This file collects Chinese poetry from a GitHub dataset and organizes them
in a text file suitable for `makemore.py`.
Example usage and output:
$ python3 collect_poetry_dataset.py -i ./../chinese-poetry -c -st -ss
INFO:__main__:Collected 159049 sentences from 23 files
INFO:__main__:Sampled 10 random poems:
聊此傲羲皇。
一望朱楼巧小，四边绣幕低垂。
洛浦佩寒如隔日，高唐梦到又何时。
翠深知是深多少，不都放、夕阳红入。
谁为语儒馆，浓墨被诗歌。
东君似怜花透，环碧ㄓ、遮住怕渠惊。
白鸟去边明。
清明世，冰辉太洁，鸥鹭莫惊猜。
锦瑟银屏何处，花雾翻香曲。
历代恢文偃武，四方晏粲无虞。
INFO:__main__:Collected 268283 sentences from 58 files
INFO:__main__:Sampled 10 random poems:
女郎折得殷勤看，道是春風及第花。
告你，告你，休向人間整理。
肯想觀魚處，寒泉照髮斑。
麻引詩人興，鹽牽謝女才。
焉知腸車轉，一夕巡九方。
田氏倉卒骨肉分，青天白日摧紫荆。
周王惑襃姒，城闕成陂陁。
縣庭無事似山齋，滿砌青青旋長苔。
興闌啼鳥換，坐久落花多。
金吾如借問，但道玉山頹。
INFO:__main__:Collected 1099146 sentences from 255 files
INFO:__main__:Sampled 10 random poems:
柴門三叩畧從容，感激聊酬大耳公。
望立人心險，驚飛鳥影斜。
被花惱處君知否，羅襪凌波笑不來。
英聲凜荆揚，盛事踵遐武。
鳳樓好手乃有弟，鐵聲錚錚亦妙器。
淄澠工濫載，管鮑闕周旋。
逋客敢欺桂，秋巖曾遣風。
岷峨人物古，淮海姓名香。
强起出門行，孤夢猶可續。
貌出正偏，見非向背。
"""

import argparse
import glob
import json
import logging
import os
import random
from typing import List

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def _sample_random_poems(poem_texts: list, num_samples: int) -> List[str]:
  """
  Randomly samples poems from the provided list of poems.

  Args:
    poem_texts: A list of strings, each string representing a poem.
    num_samples: The number of poems to sample.

  Returns:
    A list of strings, each string representing a poem.
  """
  return random.sample(poem_texts, num_samples)


# Takes a user specified path as input and reads its contents.
# The path should be a directory containing a collection of text files.
# Each text file should contain a single poem.
# The text files should be encoded in UTF-8.

def collect_poetry_dataset(args: argparse.Namespace) -> None:
  if not os.path.isdir(args.input_path):
    raise ValueError('Input path is not a directory.')
  def _collect_all_text(
        file_pattern: str, input_path: str, output_path: str) -> None:
    """
    Collects all text from the provided list of files and writes the text
    to the provided output path.

    Args:
      file_pattern: The file name pattern to glob in `input_path`.
      input_path: The path to the directory containing the text files.
      output_path: The path to the output file.
    """
    files = glob.glob(os.path.join(input_path, file_pattern))
    poem_texts = []
    for file in files:
      with open(file, 'r') as fp:
        contents = fp.read()
        poems = json.loads(contents)
        for poem in poems:
          poem_texts.extend(poem['paragraphs'])
    logger.info('Collected %d sentences from %d files',
                len(poem_texts), len(files))
    sample_size = 10
    random_poem_texts = _sample_random_poems(poem_texts, sample_size)
    logger.info(
        'Sampled %d random poems:\n%s', sample_size,
        '\n'.join(random_poem_texts))
    with open(output_path, 'w') as fp:
      fp.write('\n'.join(poem_texts))
  if args.ci:
    _collect_all_text('宋词/ci.song.*.json', args.input_path, 'ci.txt')
  if args.shi_tang:
    _collect_all_text('全唐诗/poet.tang.*.json', args.input_path, 'shi_tang.txt')
  if args.shi_song:
    _collect_all_text('全唐诗/poet.song.*.json', args.input_path, 'shi_song.txt')


def main():
  """
  Organizes the provided dataset into a text file suitable for `makemore.py`.
  """
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '-i', '--input-path', required=True,
      help='path to the directory containing text files')
  parser.add_argument(
      '-c', '--ci', action='store_true', help='collect data for ci')
  parser.add_argument(
      '-st', '--shi-tang', action='store_true', help='collect data for shi-tang')
  parser.add_argument(
      '-ss', '--shi-song', action='store_true', help='collect data for shi-song')
  parser.set_defaults(func=collect_poetry_dataset)
  args = parser.parse_args()
  args.func(args)


if __name__ == '__main__':
  main()
